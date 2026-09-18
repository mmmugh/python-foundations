"""Build the Python Foundations web app from content/ and the code bundle.

    python3 build.py            # write site/
    python3 build.py --check    # also run every code box and report failures

No dependencies. Reads content/*.md, turns every ```python fence into an
editable code box that runs in the browser, and writes one HTML page per
chapter into site/.
"""

import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
SITE = ROOT / "site"

# Boxes that need something declared: a setup prelude (the fence uses a name
# defined in an earlier fence) or an expected exception (the book crashes on
# purpose and the traceback is the lesson). Keyed "<slug>#<box index>".
# build.py --check fails if any box raises without a declaration here.
BOXES = json.loads((CONTENT / "_boxes.json").read_text())

# How to check a Try It answer, keyed "<slug>#<exercise number>". Only the
# exercises that can be checked without ever failing a correct answer appear
# here; the rest render with a Run button and no verdict.
CHECKS = json.loads((CONTENT / "_checks.json").read_text())


# ---------------------------------------------------------------- markdown

def inline(text):
    """Render the inline markdown the book actually uses."""
    spans = []

    def stash(match):
        spans.append(match.group(1))
        return f"\x00{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    def restore(match):
        return f"<code>{html.escape(spans[int(match.group(1))])}</code>"

    return re.sub(r"\x00(\d+)\x00", restore, text)


def split_blocks(lines):
    """Group lines into (kind, payload) blocks. Fences are never reinterpreted."""
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            tag = line[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code" if tag == "python" else "output", "\n".join(body)))
            continue

        if not line.strip():
            i += 1
            continue

        heading = re.match(r"^(#{1,3}) (.+)$", line)
        if heading:
            blocks.append((f"h{len(heading.group(1))}", heading.group(2)))
            i += 1
            continue

        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            blocks.append(("table", rows))
            continue

        if re.match(r"^\s*(\d+\.|[-*])\s", line):
            items = []
            ordered = bool(re.match(r"^\s*\d+\.", line))
            while i < len(lines) and re.match(r"^\s*(\d+\.|[-*])\s", lines[i]):
                items.append(re.sub(r"^\s*(\d+\.|[-*])\s+", "", lines[i]))
                i += 1
            blocks.append(("ol" if ordered else "ul", items))
            continue

        if line.startswith(">"):
            blocks.append(("quote", line.lstrip("> ")))
            i += 1
            continue

        para = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(```|#{1,3} |\||>|\s*(\d+\.|[-*])\s)", lines[i]
        ):
            para.append(lines[i])
            i += 1
        blocks.append(("p", " ".join(para)))

    return blocks


def is_output_label(text):
    """A short line ending in a colon that introduces a block of output."""
    return text.endswith(":") and len(text) <= 60


def render_table(rows):
    cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
    head, body = cells[0], [r for r in cells[2:]]
    out = ["<table><thead><tr>"]
    out += [f"<th>{inline(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def render(blocks, slug):
    """Blocks to HTML. Code fences become boxes; the next output fence is its answer."""
    parts = []
    box = 0
    i = 0
    while i < len(blocks):
        kind, payload = blocks[i]

        if kind == "h3" and payload == "Try It":
            parts.append(f"<h3>{inline(payload)}</h3>")
            j = i + 1
            while j < len(blocks) and blocks[j][0] != "h3":
                j += 1
            parts.append(render_exercises(slug, blocks[i + 1:j]))
            i = j
            continue

        if kind == "code":
            expected, label, skip = "", "", 0
            # The book almost always writes a short label between a code fence
            # and its output ("Output:", "A sample run:", "The last line raises:").
            if i + 1 < len(blocks) and blocks[i + 1][0] == "output":
                expected, skip = blocks[i + 1][1], 1
            elif (i + 2 < len(blocks) and blocks[i + 1][0] == "p"
                  and blocks[i + 2][0] == "output" and is_output_label(blocks[i + 1][1])):
                label, expected, skip = blocks[i + 1][1], blocks[i + 2][1], 2
            i += skip
            parts.append(code_box(slug, box, payload, expected, label))
            box += 1

        elif kind == "output":
            parts.append(f'<pre class="output-only">{html.escape(payload)}</pre>')
        elif kind in ("h1", "h2", "h3"):
            parts.append(f"<{kind}>{inline(payload)}</{kind}>")
        elif kind == "p":
            parts.append(f"<p>{inline(payload)}</p>")
        elif kind in ("ol", "ul"):
            items = "".join(f"<li>{inline(x)}</li>" for x in payload)
            parts.append(f"<{kind}>{items}</{kind}>")
        elif kind == "table":
            parts.append(render_table(payload))
        elif kind == "quote":
            parts.append(f"<blockquote>{inline(payload)}</blockquote>")

        i += 1
    return "\n".join(parts)


SIGNATURE = re.compile(r"`([a-z_][a-z_0-9]*\([^)]*\))`")


def render_exercises(slug, blocks):
    """Render a Try It section as numbered exercises, each with its own box.

    Exercises are numbered across the whole section, not per list, because the
    book's numbering runs straight through even where a code fence splits it.
    """
    exercises = []
    for kind, payload in blocks:
        if kind in ("ol", "ul"):
            for item in payload:
                exercises.append({"text": item, "code": ""})
        elif kind == "code" and exercises:
            exercises[-1]["code"] = payload      # a fence belongs to the item above it

    out = []
    for number, exercise in enumerate(exercises, 1):
        out.append(exercise_html(slug, number, exercise))
    return "\n".join(out)


def exercise_html(slug, number, exercise):
    check = CHECKS.get(f"{slug}#{number}")
    key = f"{slug}#{number}"
    body = [f'<p class="prompt"><span class="num">{number}</span>{inline(exercise["text"])}</p>']

    starter = exercise["code"]
    if check and check["kind"] == "function" and not starter:
        # The exercise states the signature; use it as the starting line.
        stub = check.get("stub") or next(iter(SIGNATURE.findall(exercise["text"])), "")
        starter = f"def {stub}:\n    " if stub else ""

    if check and check["kind"] == "predict":
        body.append('<label class="ask">Write down what you think it prints, '
                    'then press Check.</label>'
                    '<textarea class="prediction" spellcheck="false" rows="3" '
                    'aria-label="Your prediction"></textarea>')

    body.append(f'<textarea spellcheck="false" aria-label="Python code, editable">'
                f'{html.escape(starter)}</textarea>')

    buttons = '<button class="run">Run</button>'
    if check:
        buttons += '<button class="check">Check</button>'
    buttons += ('<button class="reset" title="Undo your edits">Reset</button>'
                '<span class="status"></span>')
    body.append(f'<div class="bar">{buttons}</div><pre class="result" hidden></pre>')

    if not check:
        body.append('<p class="unchecked">No single correct answer to check '
                    'against \u2014 run it and see.</p>')

    attrs = f'<div class="box exercise" data-box="{html.escape(key, quote=True)}"'
    if check:
        attrs += f' data-check="{html.escape(json.dumps(check), quote=True)}"'
    return attrs + ">" + "".join(body) + "</div>"


def code_box(slug, index, code, expected, label=""):
    """One editable, runnable code box."""
    declared = BOXES.get(f"{slug}#{index}", {})
    setup = declared.get("setup")
    crash = declared.get("raises")

    head = []
    if crash:
        head.append(f'<p class="note">This raises <code>{crash}</code> on purpose. '
                    f'{html.escape(declared.get("why", ""))} Run it and read the traceback.</p>')
    if setup:
        head.append(f'<pre class="setup">{html.escape(setup)}</pre>')

    answer = ""
    if expected:
        generic = label.lower().rstrip(":") in ("", "output")
        summary = "What the book prints" if generic else inline(label.rstrip(":"))
        answer = (f'<details class="expected"><summary>{summary}</summary>'
                  f'<pre>{html.escape(expected)}</pre></details>')

    attrs = f'<div class="box" data-box="{index}"'
    if setup:
        # Newlines must be entity-encoded or the parser folds them into spaces.
        encoded = html.escape(setup, quote=True).replace("\n", "&#10;")
        attrs += f' data-setup="{encoded}"'

    return (
        f'{attrs}>'
        f'{"".join(head)}'
        f'<textarea spellcheck="false" aria-label="Python code, editable">'
        f'{html.escape(code)}</textarea>'
        f'<div class="bar"><button class="run">Run</button>'
        f'<button class="reset" title="Undo your edits">Reset</button>'
        f'<span class="status"></span></div>'
        f'<pre class="result" hidden></pre>{answer}</div>'
    )


# ---------------------------------------------------------------- pages

def chapter_files():
    return sorted(CONTENT.glob("*.md"))


def title_of(path, blocks):
    for kind, payload in blocks:
        if kind == "h2":
            return payload
        if kind == "h1":
            return payload
    return path.stem


def build(check=False):
    SITE.mkdir(exist_ok=True)
    pages = []

    for path in chapter_files():
        text = path.read_text()
        part = None
        part_match = re.match(r"<!-- part: (.+) -->", text)
        if part_match:
            part = part_match.group(1)
            text = text.split("\n", 1)[1]

        blocks = split_blocks(text.split("\n"))
        pages.append({
            "slug": path.stem,
            "title": title_of(path, blocks),
            "part": part,
            "blocks": blocks,
            "boxes": sum(1 for k, _ in blocks if k == "code"),
        })

    template = (ROOT / "web" / "page.html").read_text()
    for n, page in enumerate(pages):
        nav = "".join(
            f'<a href="{p["slug"]}.html"{" class=here" if p is page else ""}>'
            f'{html.escape(p["title"])}</a>'
            for p in pages
        )
        prev_next = "".join([
            f'<a class="prev" href="{pages[n-1]["slug"]}.html">&larr; '
            f'{html.escape(pages[n-1]["title"])}</a>' if n else "",
            f'<a class="next" href="{pages[n+1]["slug"]}.html">'
            f'{html.escape(pages[n+1]["title"])} &rarr;</a>' if n + 1 < len(pages) else "",
        ])
        out = (template
               .replace("{{title}}", html.escape(page["title"]))
               .replace("{{part}}", html.escape(page["part"] or ""))
               .replace("{{nav}}", nav)
               .replace("{{body}}", render(page["blocks"], page["slug"]))
               .replace("{{prevnext}}", prev_next)
               .replace("{{slug}}", page["slug"]))
        (SITE / f"{page['slug']}.html").write_text(out)

    runner = json.dumps((ROOT / "web" / "box_runner.py").read_text())
    for name in ("app.js", "app.css"):
        text = (ROOT / "web" / name).read_text().replace("{{harness}}", runner)
        (SITE / name).write_text(text)

    (SITE / "index.html").write_text((SITE / f"{pages[0]['slug']}.html").read_text())

    # Machine-readable box list, so the boxes can be run outside this script.
    dump = []
    for page in pages:
        index = 0
        for kind, code in page["blocks"]:
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['slug']}#{index}", {})
            dump.append({"id": f"{page['slug']}#{index}", "slug": page["slug"],
                         "code": code, "setup": declared.get("setup", ""),
                         "raises": declared.get("raises", ""),
                         "needs_input": "input(" in code})
            index += 1
    (SITE / "boxes.json").write_text(json.dumps(dump, indent=1))

    total = sum(p["boxes"] for p in pages)
    print(f"built {len(pages)} pages, {total} code boxes -> {SITE.relative_to(ROOT)}/")
    for p in pages:
        print(f"  {p['slug']:<42} {p['boxes']:>3} boxes")

    if check:
        verify(pages)


def verify(pages):
    """Run every code box on this machine's python3 and report what happens."""
    print("\nchecking every code box against python3:")
    tally = {"clean": 0, "needs input": 0, "raises on purpose": 0, "UNEXPECTED": 0}
    problems = []

    for page in pages:
        index = 0
        for kind, code in page["blocks"]:
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['slug']}#{index}", {})
            index += 1
            if "input(" in code:
                tally["needs input"] += 1
                continue

            source = code
            if declared.get("setup"):
                source = declared["setup"] + "\n" + code

            with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
                f.write(source + "\n")
                temp = f.name
            run = subprocess.run([sys.executable, temp], capture_output=True,
                                 text=True, stdin=subprocess.DEVNULL, timeout=30)

            if run.returncode == 0:
                tally["clean"] += 1
            elif declared.get("raises"):
                tally["raises on purpose"] += 1
            elif page["slug"] == "99-appendices":
                tally["raises on purpose"] += 1      # syntax skeletons, not programs
            else:
                tally["UNEXPECTED"] += 1
                problems.append((f"{page['slug']}#{index - 1}",
                                 code.strip().split("\n")[0],
                                 run.stderr.strip().split("\n")[-1]))

    for key, count in tally.items():
        print(f"  {key:<20} {count:>3}")
    for where, first, err in problems:
        print(f"  !! {where:<40} {first[:34]!r}  {err[:60]}")
    if problems:
        sys.exit(f"\n{len(problems)} box(es) fail unexpectedly")
    print("  all boxes behave as expected")


if __name__ == "__main__":
    build(check="--check" in sys.argv)
