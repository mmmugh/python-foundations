"""Build the course web app from volumes/ and the code bundle.

    python3 build.py            # write site/
    python3 build.py --check    # also run every code box and report failures

No dependencies. Reads volumes/<volume>/content/*.md, turns every ```python
fence into an editable code box that runs in the browser, and writes one HTML
page per chapter into site/<volume>/.

A volume is a course. There is one today; adding another means adding a
directory with a volume.json in it, and changing nothing here.
"""

import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VOLUMES = ROOT / "volumes"
SITE = ROOT / "site"


def load_volumes():
    """Every course under volumes/, in the order a reader should meet them.

    A volume is self-contained: its own chapters, quizzes, answer keys and
    worked solutions, built into its own directory under site/. Adding volume
    two means adding a directory with a volume.json in it. Nothing in this file
    names a particular volume, and nothing outside volumes/ has to change.
    """
    found = []
    for meta in sorted(VOLUMES.glob("*/volume.json")):
        vol = json.loads(meta.read_text())
        vol["slug"] = meta.parent.name
        vol["dir"] = meta.parent
        vol["content"] = meta.parent / "content"
        vol["quizzes"] = meta.parent / "quizzes"
        if not vol["content"].is_dir():
            sys.exit(f"{meta.parent.name} has a volume.json but no content/")
        if not vol.get("title"):
            sys.exit(f"{meta.parent.name}/volume.json needs a \"title\"")
        found.append(vol)
    if not found:
        sys.exit(f"no volumes found: expected volumes/<name>/volume.json")
    return sorted(found, key=lambda v: (v.get("number", 0), v["slug"]))


VOLS = load_volumes()


def find_volume(name=None):
    """The volume a script should work on.

    With one volume there is nothing to choose. With two, saying which is
    required rather than guessed: quietly exporting the wrong course is worse
    than being asked.
    """
    if name:
        for vol in VOLS:
            if vol["slug"] == name:
                return vol
        sys.exit(f"no volume called {name!r}. There is: "
                 + ", ".join(v["slug"] for v in VOLS))
    if len(VOLS) == 1:
        return VOLS[0]
    sys.exit("there is more than one volume, so say which: "
             + ", ".join(v["slug"] for v in VOLS))


def across_volumes(load):
    """Merge a per-volume mapping into one dict keyed "<volume>/<page>#<n>".

    Every lookup below is by that key, so two volumes can each have a ch01
    without colliding and none of the rendering code has to know volumes exist.
    """
    merged = {}
    for vol in VOLS:
        for key, value in load(vol).items():
            merged[f"{vol['slug']}/{key}"] = value
    return merged


def load_json(vol, name):
    path = vol["content"] / name
    return json.loads(path.read_text()) if path.exists() else {}


# Boxes that need something declared: a setup prelude (the fence uses a name
# defined in an earlier fence) or an expected exception (the course crashes on
# purpose and the traceback is the lesson).
# build.py --check fails if any box raises without a declaration here.
BOXES = across_volumes(lambda vol: load_json(vol, "_boxes.json"))

# How to check a Try It answer. Only the exercises that can be checked without
# ever failing a correct answer appear here; the rest render with a Run button
# and no verdict.
CHECKS = across_volumes(lambda vol: load_json(vol, "_checks.json"))


def load_solutions(vol):
    """Worked solutions for the exercises that have no check, keyed "<page>#<n>".

    Kept as Markdown rather than JSON so they can be edited as writing.
    """
    path = vol["content"] / "_solutions.md"
    if not path.exists():
        return {}
    found, ident, code, note, fence = {}, None, [], [], False
    for line in path.read_text().split("\n"):
        if line.startswith("## ") and not fence:
            if ident:
                found[ident] = {"code": "\n".join(code).strip(),
                                "note": " ".join(note).strip()}
            ident, code, note = line[3:].strip(), [], []
            continue
        if ident is None:
            continue
        if line.startswith("```"):
            fence = not fence
            continue
        if fence:
            code.append(line)
        elif line.strip() and not line.startswith("<!--"):
            note.append(line.strip())
    if ident:
        found[ident] = {"code": "\n".join(code).strip(), "note": " ".join(note).strip()}
    return found


SOLUTIONS = across_volumes(load_solutions)


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
    section = ""
    while i < len(blocks):
        kind, payload = blocks[i]
        if kind == "h3":
            section = payload

        # "A solution:" introduces the listing, which is now behind a
        # disclosure, so the sentence goes with it rather than above the box.
        if (kind == "p" and re.match(r"^A solution", payload)
                and i + 1 < len(blocks) and blocks[i + 1][0] == "code"):
            i += 1
            continue

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
            if section.startswith(("Chapter project", "Capstone project")):
                parts.append(project_box(slug, box, payload, expected, label))
                box += 1
                i += 1
                continue

            varies = BOXES.get(f"{slug}#{box}", {}).get("varies")
            if "input(" in payload:
                label = "A sample run"
            elif varies:
                label = "The course showed"
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


def worked_cases(check):
    """The test cases, written out as calls. For an exercise that names a
    function, these are the specification: "count_above([3, 3, 3], 3) -> 0"
    settles whether the comparison is > or >= without giving any code away."""
    lines = []
    for args, expected in check["cases"]:
        shown = ", ".join(repr(a) for a in args)
        lines.append(f"{check['name']}({shown})  ->  {expected!r}")
    return "\n".join(lines)


def exercise_html(slug, number, exercise):
    check = CHECKS.get(f"{slug}#{number}")
    key = f"{slug}#{number}"
    body = [f'<p class="prompt"><span class="num">{number}</span>{inline(exercise["text"])}</p>']

    starter = exercise["code"]
    if check and check["kind"] == "function" and not starter:
        # The exercise states the signature; use it as the starting line.
        stub = check.get("stub") or next(iter(SIGNATURE.findall(exercise["text"])), "")
        starter = f"def {stub}:\n    " if stub else ""

    if check and check["kind"] == "function":
        body.append('<details class="cases" open><summary>What it should do</summary>'
                    f'<pre>{html.escape(worked_cases(check))}</pre></details>')

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

    solution = SOLUTIONS.get(key)
    if solution:
        note = f'<p class="why">{inline(solution["note"])}</p>' if solution["note"] else ""
        body.append('<details class="solution"><summary>Show a solution</summary>'
                    f'<pre>{html.escape(solution["code"])}</pre>{note}</details>')
    elif not check:
        body.append('<p class="unchecked">No single correct answer to check '
                    'against \u2014 run it and see.</p>')

    attrs = f'<div class="box exercise" data-box="{html.escape(key, quote=True)}"'
    if check:
        attrs += f' data-check="{html.escape(json.dumps(check), quote=True)}"'
    return attrs + ">" + "".join(body) + "</div>"


def project_box(slug, index, code, expected, label=""):
    """A chapter project: something to write, not something to read.

    The prompt says what to build and the printed output says exactly what it
    should produce, which between them is a complete specification. Handing the
    finished listing over as well leaves nothing to do, so it goes behind a
    disclosure and the editor starts with the one line of description the
    listing opens with.
    """
    first = code.split("\n")[0]
    starter = first + "\n\n" if first.startswith("#") else ""

    spec = ""
    if expected:
        heading = "A sample run" if "input(" in code else "What it should print"
        spec = (f'<div class="spec"><p class="spec-head">{heading}</p>'
                f'<pre>{html.escape(expected)}</pre></div>')

    # A project that asks the reader to type something needs a declared check,
    # because the sample run shows the typed values and the checker supplies
    # them silently. Everything else is checkable against the stated output for
    # free: the build already proves that is what this code really produces.
    spec_check = CHECKS.get(f"{slug}#{index}")
    if spec_check is None and expected and "input(" not in code:
        spec_check = {"kind": "output", "expected": expected}
    check = ""
    if spec_check:
        check = (' data-check="' +
                 html.escape(json.dumps(spec_check), quote=True) + '"')

    buttons = '<button class="run">Run</button>'
    if check:
        buttons += '<button class="check">Check</button>'
    buttons += ('<button class="reset" title="Start over">Reset</button>'
                '<span class="status"></span>')

    return (
        f'{spec}'
        f'<div class="box project" data-box="{index}"{check}>'
        f'<textarea spellcheck="false" aria-label="Your program">'
        f'{html.escape(starter)}</textarea>'
        f'<div class="bar">{buttons}</div>'
        f'<pre class="result" hidden></pre>'
        f'<details class="solution"><summary>Show a solution</summary>'
        f'<pre>{html.escape(code)}</pre></details>'
        f'</div>'
    )


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
        summary = inline(label.rstrip(":")) or "What the course prints"
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

def page_order(path):
    """Front matter, then the chapters in order, then the appendices.

    Sorting the filenames puts 99-appendices second, because "9" sorts before
    "c" — which read as a missing chapter rather than an ordering accident.
    """
    if path.stem.startswith("00"):
        return (0, 0)
    if path.stem.startswith("99"):
        return (2, 0)
    return (1, int(path.stem[2:4]))


def chapter_files(vol):
    """The pages of one volume.

    A leading underscore means a file that feeds the build rather than one the
    reader sees -- _solutions.md holds the worked answers. Publishing it would
    hand over every solution on one page, so the rule is a whitelist of what a
    page looks like, not a blacklist of what it must not be.
    """
    return sorted((p for p in vol["content"].glob("*.md")
                   if not p.stem.startswith("_")), key=page_order)


def title_of(path, blocks):
    for kind, payload in blocks:
        if kind == "h2":
            return payload
        if kind == "h1":
            return payload
    return path.stem


def build(check=False):
    SITE.mkdir(exist_ok=True)
    for stale in SITE.glob("*.standalone.html"):
        stale.unlink()          # previews are built on demand; do not leave old ones

    # Shared by every volume, and the reason the volumes live in one site: the
    # runtime is fetched and served once rather than once per course, and a
    # reader who moves from volume one to volume two does not download Python
    # again or lose the scratchpad.
    runner = json.dumps((ROOT / "web" / "box_runner.py").read_text())
    for name in ("app.js", "app.css"):
        text = (ROOT / "web" / name).read_text().replace("{{harness}}", runner)
        (SITE / name).write_text(text)
    copy_runtime()

    built = [build_volume(vol) for vol in VOLS]
    prune_removed_volumes()

    # One machine-readable list of every box in every volume, so the boxes can
    # be run outside this script. Ids carry the volume, so they stay unique.
    (SITE / "boxes.json").write_text(
        json.dumps([box for _, _, boxes in built for box in boxes], indent=1))

    write_library(built)
    assert_nothing_private_published()

    for vol, pages, boxes in built:
        print(f"built {len(pages)} pages, {len(boxes)} code boxes "
              f"-> site/{vol['slug']}/")
        for page in pages:
            print(f"  {page['slug']:<42} {page['boxes']:>3} boxes")

    if check:
        verify(built)


# Dropped into every volume directory this script writes, so it can recognise
# its own output later. Nothing reads it; its existence is the whole point.
BUILT_MARKER = ".built-volume"


def prune_removed_volumes():
    """Delete output for volumes that no longer exist.

    site/ is not rebuilt from empty, so a volume that is deleted or renamed
    otherwise leaves its pages behind: unlinked from the contents, still
    fetchable by anyone who has the URL. Withdrawn writing that stays published
    is the kind of thing nobody notices until someone else does.

    Only directories carrying BUILT_MARKER are removed -- a whitelist of what
    this script made, not a blacklist of what it does not recognise. Deleting
    by non-recognition would take a .well-known/ put there for a certificate,
    or a .git/ used to publish site/ to a hosting branch, with one printed line
    as the only warning.
    """
    keep = {vol["slug"] for vol in VOLS}
    for path in sorted(SITE.iterdir()):
        if path.is_dir() and path.name not in keep and (path / BUILT_MARKER).exists():
            shutil.rmtree(path)
            print(f"removed site/{path.name}/ -- no volume by that name any more")


def build_volume(vol):
    """Render one volume into site/<volume>/. Returns (vol, pages, boxes)."""
    out_dir = SITE / vol["slug"]
    out_dir.mkdir(exist_ok=True)
    (out_dir / BUILT_MARKER).write_text(vol["slug"] + "\n")
    pages = []

    for path in chapter_files(vol):
        text = path.read_text()
        part = None
        part_match = re.match(r"<!-- part: (.+) -->", text)
        if part_match:
            part = part_match.group(1)
            text = text.split("\n", 1)[1]

        blocks = split_blocks(text.split("\n"))
        pages.append({
            "slug": path.stem,
            # Lookups into BOXES, CHECKS and SOLUTIONS are by this, not by
            # slug: two volumes can each have a ch01.
            "key": f"{vol['slug']}/{path.stem}",
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
        # The front matter's heading is already the volume's name.
        heading = page["title"]
        tab = heading if heading.startswith(vol["title"]) else f"{heading} — {vol['title']}"
        # A chapter with a quiz gets a quiet link to it. The answer key is not
        # linked, and more to the point is not in site/ at all.
        quiz = vol["quizzes"] / f"{page['slug']}-quiz.txt"
        quiz_link = ""
        if quiz.exists():
            quiz_link = (f'<p class="quiz"><a href="quizzes/{quiz.name}">'
                         f'Chapter {page["title"].split()[1].rstrip("—").strip()} quiz</a>'
                         f' — fill it in, then show or print it</p>')

        (out_dir / f"{page['slug']}.html").write_text(
            fill(template, vol, tab=tab, title=heading, part=page["part"] or "",
                 nav=nav, body=render(page["blocks"], page["key"]),
                 quiz=quiz_link, prevnext=prev_next, slug=page["slug"]))

    boxes = box_list(vol, pages)
    write_bundle(vol, pages)
    copy_quizzes(vol)
    return vol, pages, boxes


def fill(template, vol, *, tab, title, part, nav, body, quiz, prevnext, slug,
         root="../", home=None):
    """Put one page together.

    `root` is how a page reaches the shared files: volume pages sit one level
    down from app.css, app.js and the runtime, the library page sits beside
    them.
    """
    return (template
            .replace("{{root}}", root)
            .replace("{{home}}", html.escape(home or vol["title"]))
            .replace("{{quiz}}", quiz)
            .replace("{{tab}}", html.escape(tab))
            .replace("{{title}}", html.escape(title))
            .replace("{{part}}", html.escape(part))
            .replace("{{nav}}", nav)
            .replace("{{body}}", body)
            .replace("{{prevnext}}", prevnext)
            .replace("{{volume}}", html.escape(vol["slug"], quote=True))
            .replace("{{slug}}", slug))


def box_list(vol, pages):
    """Every code box in one volume, as data, with its stated output."""
    dump = []
    for page in pages:
        index = 0
        blocks = page["blocks"]
        for n, (kind, code) in enumerate(blocks):
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['key']}#{index}", {})
            expected, label = "", ""
            if n + 1 < len(blocks) and blocks[n + 1][0] == "output":
                expected = blocks[n + 1][1]
            elif (n + 2 < len(blocks) and blocks[n + 1][0] == "p"
                  and blocks[n + 2][0] == "output" and is_output_label(blocks[n + 1][1])):
                label, expected = blocks[n + 1][1], blocks[n + 2][1]
            dump.append({"id": f"{page['key']}#{index}", "volume": vol["slug"],
                         "slug": page["slug"],
                         "code": code, "setup": declared.get("setup", ""),
                         "raises": declared.get("raises", ""),
                         "expected": expected, "label": label,
                         "reference": bool(declared.get("reference")),
                         "needs_input": "input(" in code})
            index += 1
    return dump


def write_library(built):
    """site/index.html: the way in, whatever number of volumes there are.

    With one volume this reads as its table of contents; with two it reads as a
    shelf. Not a redirect and not a picker that wastes a click either way.
    """
    template = (ROOT / "web" / "page.html").read_text()
    sections, nav = [], []
    for vol, pages, _ in built:
        first = pages[0]["slug"] if pages else ""
        heading = html.escape(vol["title"])
        sections.append(f'<h2><a href="{vol["slug"]}/{first}.html">{heading}</a></h2>')
        if vol.get("subtitle"):
            sections.append(f'<p class="part">{html.escape(vol["subtitle"])}</p>')
        if vol.get("blurb"):
            sections.append(f'<p>{html.escape(vol["blurb"])}</p>')
        sections.append("<ul class=\"contents\">" + "".join(
            f'<li><a href="{vol["slug"]}/{p["slug"]}.html">{html.escape(p["title"])}</a></li>'
            for p in pages) + "</ul>")
        sections.append(f'<p><a href="{vol["slug"]}/bundle.html">'
                        f'The code from {heading} as files</a></p>')
        nav.append(f'<a href="{vol["slug"]}/{first}.html">{heading}</a>')

    # With one volume this page is that volume's contents and should carry its
    # name; with two it is a shelf and must not claim to be either of them.
    only = built[0][0] if len(built) == 1 else None
    name = only["title"] if only else "All volumes"
    # No volume of its own: the page is the shelf, and data-volume must not
    # claim it is volume one, in case it ever grows a code box.
    (SITE / "index.html").write_text(
        fill(template, {"slug": "", "title": name}, root="", home=name,
             tab=name, title=name, part="",
             nav="".join(nav), body="".join(sections),
             quiz="", prevnext="", slug="index"))


ANSWER_MARKER = "ANSWER KEY"

# Content that must never be published whole. Per-exercise reveals are fine;
# a single page carrying the lot is not.
PRIVATE_CONTENT = ("_solutions", "_boxes", "_checks")


def copy_runtime():
    """Put Python into the site, after proving it is the Python we meant.

    The page loads the interpreter from this site rather than a CDN, so these
    bytes are what a student actually runs. They are not committed -- 13 MB of
    someone else's binaries do not belong in this history -- so the first build
    fetches them, and every build re-checks them against the pinned hashes.

    Fetching here rather than telling the reader to run another script keeps
    the install to one command. It is not silent: it says what it is doing, it
    only happens when something is missing or wrong, and after that the build
    touches the network never again.
    """
    sys.path.insert(0, str(ROOT / "scripts"))
    import fetch_pyodide

    if not fetch_pyodide.CHECKSUMS.exists():
        sys.exit("vendor/pyodide/CHECKSUMS is missing -- this is not a complete "
                 "checkout of the repository")

    version, hashes = fetch_pyodide.pinned()
    bad = fetch_pyodide.verify(hashes)

    # Missing and wrong are different. Missing is the first build, and fetching
    # it is the whole reason this is one command instead of two. Wrong means a
    # file is there and is not the file CHECKSUMS names -- a truncated download,
    # a damaged disk, or someone editing the interpreter a student runs. Quietly
    # re-downloading over that would repair the site and hide the event, so it
    # stops the build and asks to be told to refetch.
    if bad and all(line.endswith("missing") for line in bad):
        absent = [line.split(":")[0] for line in bad]
        print(f"pyodide {version}: {len(absent)} of {len(hashes)} runtime files "
              f"are not here yet, fetching them (once)")
        try:
            fetch_pyodide.download(version, absent)
        except OSError as e:
            sys.exit(f"could not fetch pyodide {version}: {e}\n"
                     "this build needs the network once; after that it does not")
        bad = fetch_pyodide.verify(hashes)

    if bad:
        sys.exit("the pyodide runtime does not match vendor/pyodide/CHECKSUMS:\n  "
                 + "\n  ".join(bad)
                 + "\nthese are the bytes a student would run, so this build stops.\n"
                 "run: python3 scripts/fetch_pyodide.py --download")

    target = SITE / "pyodide"
    target.mkdir(exist_ok=True)
    for name in hashes:
        shutil.copyfile(fetch_pyodide.VENDOR / name, target / name)

    # Pyodide is MPL-2.0, which asks that the licence travel with the binary.
    # site/ is what gets hosted, so the copy has to be there and not only here.
    shutil.copyfile(fetch_pyodide.VENDOR / "LICENSE", target / "LICENSE")
    print(f"copied pyodide {version} -> site/pyodide/ ({len(hashes)} files, verified)")


def copy_quizzes(vol):
    """Copy one volume's student quizzes into the site, and nothing else.

    An explicit whitelist, not an exclusion: a rule that copies everything
    except the files it recognises as keys fails open the moment a key is named
    something unexpected. This fails closed. The answer keys sit in the same
    volume directory, one level up from here, and are never copied.
    """
    source = vol["quizzes"]
    if not source.exists():
        return
    target = SITE / vol["slug"] / "quizzes"
    target.mkdir(exist_ok=True)
    for stale in target.glob("*"):
        stale.unlink()
    copied = 0
    for quiz in sorted(source.glob("*-quiz.txt")):
        (target / quiz.name).write_text(quiz.read_text())
        copied += 1

    if copied:
        print(f"copied {copied} quizzes -> site/{vol['slug']}/quizzes/ "
              f"(no answer keys)")


def assert_nothing_private_published():
    """Everything under site/ is public. Prove nothing private got there.

    This is deliberately NOT inside copy_quizzes(): it used to be, and an early
    `if not source.exists(): return` meant the whole scan was skipped whenever
    quizzes/ was absent. Moving or renaming that directory disarmed the guard
    instead of failing the build.
    """
    leaked = sorted({p.relative_to(SITE) for p in SITE.rglob("*") if p.is_file()
                     and (any(p.stem.startswith(n) for n in PRIVATE_CONTENT)
                          or (p.suffix in (".txt", ".md", ".html")
                              and ANSWER_MARKER in p.read_text(errors="ignore")))})
    # Word documents are a zip of XML, so a plain read finds nothing in them.
    for doc in SITE.rglob("*.docx"):
        import zipfile
        with zipfile.ZipFile(doc) as archive:
            body = archive.read("word/document.xml").decode("utf-8", "ignore")
        if ANSWER_MARKER in body or "Worked solutions" in body:
            leaked.append(doc.relative_to(SITE))
    if leaked:
        sys.exit(f"content that must not be published is reachable: {leaked}")


def bundle_name(text):
    """A filename stem from a heading: "Chapter project: a receipt" -> receipt."""
    text = re.sub(r"^.*?:\s*", "", text)
    text = re.sub(r"^(a|an|the)\s+", "", text.strip(), flags=re.I)
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def write_bundle(vol, pages):
    """Write the book's code out as .py files, generated from the manuscript.

    These used to be maintained by hand, and drifted from the book in fourteen
    places -- every one of them forced by the promise that a file runs start to
    finish without stopping. Generating them means the promise is kept by a
    rule that states itself in each file's header, instead of by edits nobody
    can see from the chapter.
    """
    out = SITE / vol["slug"] / "bundle"
    out.mkdir(parents=True, exist_ok=True)
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
            declared = BOXES.get(f"{page['key']}#{index}", {})
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
                    body.append(f"# Commented out: the course runs this to show {raises}.\n"
                                f"# Uncomment it to see the error for yourself.\n")
                    body.append("".join(f"# {l}\n" if l.strip() else "#\n"
                                        for l in code.split("\n")))
                else:
                    body.append(code + "\n")
                if "input(" in code:
                    asks = True
                body.append("\n")

            notes = [f'"""{title}', "",
                     f"Generated from {vol['slug']}/content/{page['slug']}.md "
                     f"by build.py.",
                     "Edit the chapter, not this file."]
            if muted:
                one = muted == 1
                notes += ["",
                          f"{muted} example{'' if one else 's'} below "
                          f"{'runs' if one else 'run'} on purpose in the course, to show the",
                          f"error {'it raises' if one else 'they raise'}. Left live here "
                          f"{'it' if one else 'they'} would stop this file before the",
                          "rest of the chapter ran, so "
                          f"{'it is' if one else 'they are'} commented out below.",
                          f"Uncomment {'it' if one else 'one'} to see what the course describes."]
            if asks:
                notes += ["", "This file stops and waits wherever the chapter asks you to",
                          "type something."]
            notes += ['"""', "", ""]

            (out / name).write_text("\n".join(notes) + "".join(body).rstrip() + "\n")
            written.append((name, title, muted, asks))

    # The Word export needs python-docx, which nothing else here does. If it is
    # not installed, the course still builds; only the download row disappears.
    document_row = ""
    docx = SITE / vol["slug"] / vol.get("docx", f"{vol['slug']}.docx")
    if docx.exists():
        size = docx.stat().st_size / 1024
        document_row = (
            "<h3>The whole course as a document</h3>"
            "<p>The same text you are reading, as a Word file, for reading away "
            "from a browser or for printing. Generated from the chapters, so it "
            "matches what is on these pages.</p>"
            f'<p><a href="{docx.name}">{docx.name}</a> '
            f"({size:,.0f} KB)</p><h3>The code</h3>")

    index_rows = "".join(
        f'<tr><td><a href="bundle/{n}">{n}</a></td><td>{html.escape(t)}</td>'
        f'<td>{"error demos commented out" if m else ""}'
        f'{" · asks you to type" if a else ""}</td></tr>'
        for n, t, m, a in written)
    template = (ROOT / "web" / "page.html").read_text()
    last = pages[-1]["slug"] if pages else ""
    (SITE / vol["slug"] / "bundle.html").write_text(
        fill(template, vol,
             tab=f"The code as files — {vol['title']}",
             title="The code as files", part="", quiz="", slug="bundle",
             nav="".join(f'<a href="{p["slug"]}.html">{html.escape(p["title"])}</a>'
                         for p in pages),
             prevnext=f'<a class="prev" href="{last}.html">&larr; '
                      f'{html.escape(pages[-1]["title"])}</a>' if pages else "",
             body="<h2>Downloads</h2>"
                  + document_row +
                  "<p>Every example and project from the course, generated from the "
                  "chapters themselves so the two cannot disagree. You need Python "
                  "3.6 or newer and nothing else.</p>"
                  f"<table><thead><tr><th>File</th><th>Chapter</th><th>Notes</th>"
                  f"</tr></thead><tbody>{index_rows}</tbody></table>"))
    print(f"generated {len(written)} bundle files -> site/{vol['slug']}/bundle/")


def verify(built):
    """Run every code box in every volume on this machine's python3."""
    print("\nchecking every code box against python3:")
    tally = {"clean": 0, "needs input": 0, "raises on purpose": 0,
             "reference, not run": 0, "UNEXPECTED": 0}
    problems = []

    for page in (page for _, pages, _ in built for page in pages):
        index = 0
        for kind, code in page["blocks"]:
            if kind != "code":
                continue
            declared = BOXES.get(f"{page['key']}#{index}", {})
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
                problems.append((f"{page['key']}#{index - 1}",
                                 code.strip().split("\n")[0],
                                 run.stderr.strip().split("\n")[-1]))

    for key, count in tally.items():
        print(f"  {key:<20} {count:>3}")
    for where, first, err in problems:
        print(f"  !! {where:<40} {first[:34]!r}  {err[:60]}")
    if problems:
        sys.exit(f"\n{len(problems)} box(es) fail unexpectedly")
    print("  all boxes behave as expected")
    audit_book_output([box for _, _, boxes in built for box in boxes])


def audit_book_output(dump):
    """Check every printed output against what the code really does.

    Each chapter states its own output beside each example. Where the example is
    deterministic and needs no typing, that statement is checkable -- and a
    wrong one teaches the wrong lesson, so it fails the build rather than
    shipping.
    """
    print("\nchecking the course's own printed output against reality:")
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
            print(f"     course says : {tidy(box['expected'])!r}")
            print(f"       really is : {tidy(run.stdout)!r}")

    print(f"  {checked} checked, {mismatched} mismatched")
    if mismatched:
        sys.exit(f"\n{mismatched} place(s) where the course states an output the code "
                 f"does not produce")


if __name__ == "__main__":
    build(check="--check" in sys.argv)
