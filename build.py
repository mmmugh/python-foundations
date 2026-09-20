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
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', text)

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
            # Exercise fences still consume a box number, so that "<slug>#<n>"
            # means the same fence here as it does in verify() and the bundle.
            box += sum(1 for kind, _ in blocks[i + 1:j] if kind == "code")
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
            # Pressing Run reproduces the book's output on most boxes, so the
            # panel only earns its place where Run cannot: a transcript that
            # includes typed input, or output that legitimately varies.
            varies = BOXES.get(f"{slug}#{box}", {}).get("varies")
            if "input(" in payload:
                label = "A sample run"
            elif varies:
                label = "The book showed"
            else:
                expected, label = "", ""
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
    """One editable, runnable code box -- or, for a fragment, plain code.

    A syntax reminder like `if condition:` is not a program. Giving it a Run
    button promises something it cannot do, so it renders as code and nothing
    more.
    """
    declared = BOXES.get(f"{slug}#{index}", {})
    if declared.get("reference"):
        return f'<pre class="reference">{html.escape(code)}</pre>' 
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
        summary = inline(label.rstrip(":")) or "What the book prints"
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
        # The front matter's heading is already the book's name.
        heading = page["title"]
        tab = heading if heading.startswith("Python Foundations") else f"{heading} — Python Foundations"
        out = (template
               .replace("{{tab}}", html.escape(tab))
               .replace("{{title}}", html.escape(heading))
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
        blocks = page["blocks"]
        for n, (kind, code) in enumerate(blocks):
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['slug']}#{index}", {})
            expected, label = "", ""
            if n + 1 < len(blocks) and blocks[n + 1][0] == "output":
                expected = blocks[n + 1][1]
            elif (n + 2 < len(blocks) and blocks[n + 1][0] == "p"
                  and blocks[n + 2][0] == "output" and is_output_label(blocks[n + 1][1])):
                label, expected = blocks[n + 1][1], blocks[n + 2][1]
            dump.append({"id": f"{page['slug']}#{index}", "slug": page["slug"],
                         "code": code, "setup": declared.get("setup", ""),
                         "raises": declared.get("raises", ""),
                         "expected": expected, "label": label,
                         "reference": bool(declared.get("reference")),
                         "needs_input": "input(" in code})
            index += 1
    (SITE / "boxes.json").write_text(json.dumps(dump, indent=1))
    page_boxes = dump

    write_bundle(pages)

    total = sum(p["boxes"] for p in pages)
    print(f"built {len(pages)} pages, {total} code boxes -> {SITE.relative_to(ROOT)}/")
    for p in pages:
        print(f"  {p['slug']:<42} {p['boxes']:>3} boxes")

    if check:
        verify(pages, page_boxes)


def bundle_name(text):
    """A filename stem from a heading: "Chapter project: a receipt" -> receipt."""
    text = re.sub(r"^.*?:\s*", "", text)
    text = re.sub(r"^(a|an|the)\s+", "", text.strip(), flags=re.I)
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def write_bundle(pages):
    """Write the book's code out as .py files, generated from the manuscript.

    These used to be maintained by hand, and drifted from the book in fourteen
    places -- every one of them forced by the promise that a file runs start to
    finish without stopping. Generating them means the promise is kept by a
    rule that states itself in each file's header, instead of by edits nobody
    can see from the chapter.
    """
    out = SITE / "bundle"
    out.mkdir(exist_ok=True)
    written = []

    for page in pages:
        if not re.match(r"^ch\d\d-", page["slug"]):
            continue
        number = int(page["slug"][2:4])
        stem = page["slug"][5:].replace("-", "_")

        section, index = None, 0
        examples, project, project_title = [], None, ""
        for kind, payload in page["blocks"]:
            if kind == "h3":
                section = payload
                continue
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['slug']}#{index}", {})
            index += 1
            if (section or "").startswith(("Chapter project", "Capstone project")):
                project, project_title = payload, section
            elif section != "Try It":
                examples.append((section, payload, declared.get("raises")))

        files = [(f"ch{number:02d}_{stem}.py", page["title"], examples, True)]
        if project:
            files.append((f"ch{number:02d}_{bundle_name(project_title)}.py",
                          project_title, [(None, project, None)], False))

        for name, title, items, with_headers in files:
            body, muted, asks = [], 0, False
            for heading, code, raises in items:
                if with_headers and heading:
                    rule = "-" * max(3, 74 - len(heading))
                    body.append(f"# --- {re.sub(r'`', '', heading)} {rule}\n")
                if raises:
                    muted += 1
                    body.append(f"# Commented out: the book runs this to show {raises}.\n"
                                f"# Uncomment it to see the error for yourself.\n")
                    body.append("".join(f"# {l}\n" if l.strip() else "#\n"
                                        for l in code.split("\n")))
                else:
                    body.append(code + "\n")
                if "input(" in code:
                    asks = True
                body.append("\n")

            notes = [f'"""{title}', "",
                     f"Generated from content/{page['slug']}.md by build.py.",
                     "Edit the chapter, not this file."]
            if muted:
                one = muted == 1
                notes += ["",
                          f"{muted} example{'' if one else 's'} below "
                          f"{'runs' if one else 'run'} on purpose in the book, to show the",
                          f"error {'it raises' if one else 'they raise'}. Left live here "
                          f"{'it' if one else 'they'} would stop this file before the",
                          "rest of the chapter ran, so "
                          f"{'it is' if one else 'they are'} commented out below.",
                          f"Uncomment {'it' if one else 'one'} to see what the book describes."]
            if asks:
                notes += ["", "This file stops and waits wherever the chapter asks you to",
                          "type something."]
            notes += ['"""', "", ""]

            (out / name).write_text("\n".join(notes) + "".join(body).rstrip() + "\n")
            written.append((name, title, muted, asks))

    index_rows = "".join(
        f'<tr><td><a href="bundle/{n}">{n}</a></td><td>{html.escape(t)}</td>'
        f'<td>{"error demos commented out" if m else ""}'
        f'{" · asks you to type" if a else ""}</td></tr>'
        for n, t, m, a in written)
    template = (ROOT / "web" / "page.html").read_text()
    (SITE / "bundle.html").write_text(
        template.replace("{{tab}}", "The code as files — Python Foundations")
        .replace("{{title}}", "The code as files").replace("{{part}}", "")
        .replace("{{slug}}", "bundle").replace("{{nav}}", '<a href="index.html">Contents</a>')
        .replace("{{prevnext}}", '<a class="prev" href="99-appendices.html">&larr; Appendices</a>')
        .replace("{{body}}",
                 "<h2>The code as files</h2>"
                 "<p>Every example and project from the book, generated from the "
                 "chapters themselves so the two cannot disagree. You need Python "
                 "3.6 or newer and nothing else.</p>"
                 f"<table><thead><tr><th>File</th><th>Chapter</th><th>Notes</th>"
                 f"</tr></thead><tbody>{index_rows}</tbody></table>"))
    print(f"generated {len(written)} bundle files -> {(out).relative_to(ROOT)}/")


def verify(pages, dump):
    """Run every code box on this machine's python3 and report what happens."""
    print("\nchecking every code box against python3:")
    tally = {"clean": 0, "needs input": 0, "raises on purpose": 0,
             "reference, not run": 0, "UNEXPECTED": 0}
    problems = []

    for page in pages:
        index = 0
        for kind, code in page["blocks"]:
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['slug']}#{index}", {})
            index += 1
            if declared.get("reference"):
                tally["reference, not run"] += 1
                continue
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
    audit_book_output(dump)


def audit_book_output(dump):
    """Check every printed output in the book against what the code really does.

    The book states its own output beside each example. Where the example is
    deterministic and needs no typing, that statement is checkable -- and a
    wrong one teaches the wrong lesson, so it fails the build rather than
    shipping.
    """
    print("\nchecking the book's own printed output against reality:")
    checked = mismatched = 0
    for box in dump:
        if not box["expected"] or box["needs_input"] or box["raises"] or box["reference"]:
            continue
        if BOXES.get(box["id"], {}).get("varies"):
            continue

        source = (box["setup"] + "\n" if box["setup"] else "") + box["code"]
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(source + "\n")
            temp = f.name
        run = subprocess.run([sys.executable, temp], capture_output=True, text=True,
                             stdin=subprocess.DEVNULL, timeout=30)
        if run.returncode != 0:
            continue
        checked += 1

        tidy = lambda t: "\n".join(l.rstrip() for l in t.strip("\n").split("\n")).strip()
        if tidy(run.stdout) != tidy(box["expected"]):
            mismatched += 1
            print(f"  !! {box['id']}")
            print(f"       book says : {tidy(box['expected'])!r}")
            print(f"       really is : {tidy(run.stdout)!r}")

    print(f"  {checked} checked, {mismatched} mismatched")
    if mismatched:
        sys.exit(f"\n{mismatched} place(s) where the book states an output the code "
                 f"does not produce")


if __name__ == "__main__":
    build(check="--check" in sys.argv)
