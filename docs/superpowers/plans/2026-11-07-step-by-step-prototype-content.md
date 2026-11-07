# Step-by-step course: the prototype lessons — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write the five prototype lessons of the step-by-step course (lesson 0 and lessons 2.1 to 2.4), the
"How to start a problem" reference page, and the unit 2 quiz, as a new volume `volumes/vol1-steps/`. Build the
private feedback page the learner fills in after each lesson.

**Architecture:** The machinery is on main and described in `docs/lesson-format.md`; read it first. This plan
adds two small build changes:
- an "in progress" mark on the shelf;
- no code bundle for a lesson volume.

It then adds one contract test, `tests/steps_volume_test.py`. That test pins the spec's rules for every lesson
(sections, hints, worked solutions, checks that pass, a size cap), then the lessons are written one task at a
time until it passes. The feedback page is a private claude.ai artifact, kept outside the repository.

**Tech Stack:** Markdown lessons; `_checks.json`, `_solutions.md` and `_boxes.json` as described in
`docs/lesson-format.md`; Python 3.9+ standard library for tests; Node + playwright-core for the browser
smoke test; one HTML artifact with the `db` capability.

**Spec:** `docs/specs/step-by-step-course.md` (approved 2026-11-05). The prototype table, the lesson format, and
the problem-solving routine there are binding.

## Global Constraints

- Every lesson follows the five steps:
  1. warm-up (none in lesson 0, which is itself the review);
  2. one or two new ideas, each with two or three runnable worked examples, each adding at most one new thing;
  3. a tiny practice after each idea;
  4. one try-it with hints revealed one at a time, ending in a worked solution;
  5. a wrap-up of three lines plus the key words.
- Lessons of 20 to 30 minutes. Proxy enforced by the test: at most 10 exercises and 1,300 words of prose per
  lesson.
- No syntax, built-in function or method before an earlier example has shown it. Enforced by
  `tests/lesson_vocabulary_test.py`, which covers hints and choice options too.
- A check tests what a program does, not how it is written. Where wording is free, use the lenient `stdin`
  check (`numbers` or `words`), even with nothing typed, rather than an exact `output` check.
- Routine introduction, from the spec:
  - Say it, Split it and Build it in lesson 0;
  - Name it joins in 2.2;
  - Check it joins in 2.3;
  - all five in 2.4.
- A try-it's hints are the routine's steps, in order, and the first hint links to
  `99-how-to-start-a-problem.html`.
- The receipt in 2.4 is built step by step by the learner; no example fence holds a solved receipt.
- Writing for a 13-year-old who is strong at math and new to programming:
  - short sentences, second person;
  - plain words, with every new term in **bold** where it is first explained;
  - no jokes that need cultural context.
- Never name the first learner or quote their answers anywhere in the repository. The public site never links
  to the feedback page.
- `vol1-foundations` is unchanged: `python3 build.py --check` still reports its 110 outputs checked and 0
  mismatched, plus whatever the new volume adds.
- Python 3.9 floor; no new dependencies. Run every Python test under `python3` and `/usr/bin/python3`.
- Commit messages carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and no `Claude-Session` line.
  Never `--no-verify`.
- American spellings (`grey` excepted), closed em dashes in prose.
- Pushing needs Justin's yes, and pushing main publishes `vol1-steps` on the public site (spec: "Ask first").

## Review Focus

1. **A correct answer worded differently from the worked solution.** For example `print("Coins:", coins)` where
   the solution prints the bare number. It must pass. Pinned in Task 2: `ALTERNATES` in
   `steps_volume_test.py`, one alternate answer per checked try-it, run through the same check.
2. **A phone-width screen.** At 390 px a lesson (including its trace tables and choice options) must not scroll
   sideways. Pinned in Task 8.
3. **The public pages pointing at the private feedback page.** No `claude.ai` anywhere in the volume. Pinned in
   Task 2.
4. **The site served under `/python-foundations/`**, as GitHub Pages serves it. Hint links to the reference page
   and the quiz link must resolve. Pinned in Task 8, which runs the smoke test with `BASE`.
5. **A fix-the-bug example that crashes on purpose.** The build must treat it as intended, not as a failure.
   Pinned in Tasks 4 and 6 by the `_boxes.json` declaration, and verified by `build.py --check`.

---

### Task 1: The shelf shows a volume as "in progress", and a lesson volume has no code bundle

**Files:**
- Modify: `build.py` (`write_library`, `build_volume`)
- Modify: `tests/lesson_trial.py` (the trial volume opts in)
- Create: `tests/shelf_test.py`
- Modify: `docs/lesson-format.md`, `.github/workflows/ci.yml`

**Interfaces:**
- Produces: `volume.json` keys `"lessons": true` (already used by the vocabulary gate) and `"status": "<text>"`.
  - The shelf renders `status` as `<span class="status">in progress</span>` inside the volume's `<h2>`.
  - A volume with `"lessons": true` gets no `bundle/` directory, no `bundle.html` and no "as files" link.
    `write_bundle` only takes `^chNN-` pages, and a lesson page's warm-up and practice fences are exercises, not
    examples.

- [ ] **Step 1: Write the failing test**

Create `tests/shelf_test.py`:

```python
"""Check how the shelf shows a lesson volume.

    python3 tests/shelf_test.py

A volume still being written says so on the front page ("in progress"), so
nobody mistakes it for the finished course. A lesson volume has no code
bundle: the bundle collects a chapter's examples, and a lesson's warm-up and
practice fences are exercises, so the bundle would hand out half-finished
starters as if they were the course's code. Puts the throwaway lesson volume
from lesson_trial.py in place, builds, looks, and takes it away again.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tests"))
import lesson_trial                                             # noqa: E402

SITE = ROOT / "site"


def main():
    problems = []

    def check(ok, what):
        print(f"  {'ok  ' if ok else 'FAIL'}  {what}")
        if not ok:
            problems.append(what)

    try:
        lesson_trial.up()
        index = (SITE / "index.html").read_text()
        heading = re.search(r"<h2>[^\n]*?A Trial Lesson Volume.*?</h2>", index)
        check(heading is not None and '<span class="status">in progress</span>' in heading.group(0),
              "the shelf marks the lesson volume in progress")
        check('href="_trial-lessons/bundle.html"' not in index,
              "the shelf offers no code bundle for a lesson volume")
        check(not (SITE / "_trial-lessons" / "bundle.html").exists(),
              "no bundle page is written for it")
        check('href="vol1-foundations/bundle.html"' in index,
              "the chapter volume keeps its bundle")
        check(index.count('class="status"') == 1,
              "a volume without a status gets no mark")
    finally:
        lesson_trial.down()

    print(f"\n{'the shelf tells the two kinds of volume apart' if not problems else str(len(problems)) + ' wrong'}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
```

In `tests/lesson_trial.py`, change the trial's `volume.json` to opt in:

```python
    (TRIAL / "volume.json").write_text(json.dumps(
        {"number": 98, "title": "A Trial Lesson Volume", "subtitle": "Not a real course",
         "lessons": True, "status": "in progress"}))
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/shelf_test.py; ls volumes`
Expected: FAIL on "marks the lesson volume in progress", "offers no code bundle" and "no bundle page", and
`ls` shows only `vol1-foundations` (the trial is removed even on failure).

- [ ] **Step 3: Implement**

In `build.py` `build_volume`, find the `write_bundle(vol, pages)` call and guard it:

```python
    # A lesson's warm-up and practice fences are exercises, not examples, so a
    # lesson volume has no bundle: it would hand out starters as course code.
    if not vol.get("lessons"):
        write_bundle(vol, pages)
```

In `write_library`, replace the heading line and the bundle link:

```python
        heading = html.escape(vol["title"])
        status = (f' <span class="status">{html.escape(vol["status"])}</span>'
                  if vol.get("status") else "")
        sections.append(f'<h2><a href="{vol["slug"]}/{first}.html">{heading}</a>{status}</h2>')
```

and wrap the bundle paragraph in `if not vol.get("lessons"):`. Add to `web/app.css` beside the `.part` rule:

```css
.status { font-size: .7em; font-weight: 600; padding: .1em .5em; border: 1px solid var(--rule); border-radius: 1em; color: var(--soft); vertical-align: middle; }
```

Before running, grep for other links to `bundle.html` (`grep -n 'bundle.html' build.py web/page.html`). Any link
shown on a lesson volume's pages must be guarded the same way; ledger what you find.

- [ ] **Step 4: Run it and watch it pass, with nothing else moving**

```bash
python3 tests/shelf_test.py && /usr/bin/python3 tests/shelf_test.py
python3 build.py --check | tail -1
python3 tests/second_volume_test.py | tail -1
(cd tests && REQUIRE_BROWSER=1 node lesson_browser_test.mjs | tail -1)
ls volumes
```

Expected:
- the pass line twice;
- `110 checked, 0 mismatched`;
- the second-volume pass line;
- the lesson-format browser pass line;
- only `vol1-foundations` in `volumes/`.

To prove vol1 pages are byte-identical, snapshot `site/vol1-foundations` into the scratchpad before Step 3,
rebuild after it, and confirm `diff -r` prints nothing.

- [ ] **Step 5: Document, wire CI, commit**

In `docs/lesson-format.md`, under "The volume", add `"status": "in progress"` to the example, and two sentences:
- the shelf shows `status` beside the title, so drop it when the volume replaces the old course;
- a lesson volume has no code bundle.

In `.github/workflows/ci.yml`, in the browser job's last block (after the lesson browser step), add:

```yaml
      - name: The shelf tells a lesson volume from a chapter volume
        run: python3 tests/shelf_test.py
```

It belongs there because, like the lesson browser test, it rebuilds `site/` around the trial volume. Run
`python3 tests/workflow_test.py` and `actionlint .github/workflows/ci.yml`.

```bash
git add build.py web/app.css tests/shelf_test.py tests/lesson_trial.py docs/lesson-format.md .github/workflows/ci.yml
git commit -F - <<'MSG'
build: the shelf marks a volume in progress; a lesson volume has no bundle

The step-by-step course goes on the shelf beside the finished one while it is
written, so volume.json can carry a status the shelf shows by its title. And
a lesson volume gets no code bundle: the bundle collects a chapter's examples,
and a lesson's warm-up and practice fences are exercises, so it would hand
out starters as the course's code.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 2: The volume, its reference page, and the contract every lesson must meet

**Files:**
- Create: `volumes/vol1-steps/volume.json`, `volumes/vol1-steps/content/99-how-to-start-a-problem.md`
- Create: `volumes/vol1-steps/content/_checks.json`, `_boxes.json` (both `{}`), and `_solutions.md` (a header
  comment only)
- Create: `tests/steps_volume_test.py`
- Modify: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: `practice_test.run_check(spec, code) -> (ok, notes) | None`; `build.split_blocks`,
  `build.EXERCISE_SECTIONS`, `build.chapter_files`, `build.load_solutions`, `build.load_json`, `build.VOLS`.
- Produces: `python3 tests/steps_volume_test.py [--only <slug> ...]`. With `--only`, it checks only the named
  pages and skips the volume-wide checks, so each lesson task can go green on its own. Lesson slugs, in order:
  - `ch01z-welcome-back`
  - `ch02a-naming-a-value`
  - `ch02b-names-and-kinds`
  - `ch02c-asking-the-user`
  - `ch02d-putting-it-together`
  - `99-how-to-start-a-problem` (the reference page)

- [ ] **Step 1: Write the test**

Create `tests/steps_volume_test.py`:

```python
"""Check the step-by-step lessons keep the promises the spec makes for them.

    python3 tests/steps_volume_test.py                 # the whole volume
    python3 tests/steps_volume_test.py --only ch02a-naming-a-value

docs/specs/step-by-step-course.md sets a shape for every lesson so that a
beginner meets one idea at a time, practices it at once, and is never handed
a finished answer: a warm-up, practice after each idea, one try it whose hints
walk the problem-solving routine in order, a worked solution behind them, and
a three-line wrap-up. Every exercise has a check or a worked solution, every
worked solution passes its own check, and so does an answer in a different
style, because a check that fails a correct answer teaches the wrong lesson.
The size caps stand in for "20 to 30 minutes": a lesson that outgrows them is
two lessons.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
import build                                                    # noqa: E402
from practice_test import run_check                             # noqa: E402

VOLUME = "vol1-steps"
REFERENCE = "99-how-to-start-a-problem"
LESSONS = [
    # (slug, heading, the routine steps the try it's hints walk, in order)
    ("ch01z-welcome-back", "Lesson 0 — Welcome back", ("Say it", "Split it")),
    ("ch02a-naming-a-value", "Lesson 2.1 — Naming a value", ("Say it", "Split it")),
    ("ch02b-names-and-kinds", "Lesson 2.2 — Names that explain, and kinds of value",
     ("Say it", "Split it", "Name it")),
    ("ch02c-asking-the-user", "Lesson 2.3 — Asking the user",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch02d-putting-it-together", "Lesson 2.4 — Putting it together",
     ("Say it", "Split it", "Name it", "Check it")),
]
MAX_EXERCISES = 10
MAX_WORDS = 1300
STEPS = ("Say it", "Split it", "Name it", "Build it", "Check it")

# A correct answer in a different style from the worked solution, for every
# checked try it. Each must pass the same check the solution passes.
ALTERNATES = {
    "ch01z-welcome-back#5": 'print("Pencils: 2 x 1 =", 2 * 1)\nprint("Eraser: 1 x 3 =", 3)\nprint("Total", 2 * 1 + 3)',
    "ch02a-naming-a-value#7": 'coins = 5 - 2 + 4\nprint("Coins:", coins)',
    "ch02b-names-and-kinds#10": 'eggs_per_cake = 3\ncakes = 4\nprint("You need", eggs_per_cake * cakes, "eggs")',
    "ch02c-asking-the-user#7": 'minutes = float(input("How long is the movie, in minutes? "))\nhours = minutes / 60\nprint(hours, "hours")',
    "ch02d-putting-it-together#7": (
        'customer = input("Name: ")\nnotebook = 3.50\npens = 2.25\nstickers = 1.75\nruler = 1.25\n'
        'print("Customer:", customer)\nprint("Notebook", notebook)\nprint("Pens", pens)\n'
        'print("Stickers", stickers)\nprint("Ruler", ruler)\n'
        'print("Total", notebook + pens + stickers + ruler)'),
}


def blocks_of(text):
    return build.split_blocks(re.sub(r"^<!-- part: .+ -->\n", "", text).split("\n"))


def exercises(blocks):
    """[(number, section, text, code, hints)], numbered through the page as the build does."""
    found, section = [], None
    for kind, payload in blocks:
        if kind == "h3":
            section = payload if payload in build.EXERCISE_SECTIONS else None
        elif section and kind in ("ol", "ul"):
            for item in payload:
                found.append([len(found) + 1, section, item, "", []])
        elif section and kind == "code" and found:
            found[-1][3] = payload
        elif section and kind == "quote" and found:
            found[-1][4].append(payload)
    return [tuple(x) for x in found]


def prose_words(blocks):
    words = 0
    for kind, payload in blocks:
        if kind in ("p", "quote"):
            words += len(payload.split())
        elif kind in ("ol", "ul"):
            words += sum(len(item.split()) for item in payload)
    return words


def lesson_problems(slug, heading, hint_steps, text, checks, solutions):
    problems = []
    say = problems.append
    if not re.match(r"<!-- part: Unit \d+ — .+ -->\n", text):
        say(f"{slug}: the first line must name its unit: <!-- part: Unit N — Title -->")
    blocks = blocks_of(text)
    if next((p for k, p in blocks if k == "h2"), None) != heading:
        say(f"{slug}: the heading must be {heading!r}")

    h3 = [p for k, p in blocks if k == "h3"]
    has_warmup = "Warm-up" in h3
    if slug == "ch01z-welcome-back" and has_warmup:
        say(f"{slug}: lesson 0 is the review, so it has no warm-up")
    if slug != "ch01z-welcome-back" and (not h3 or h3[0] != "Warm-up"):
        say(f"{slug}: the first section must be the warm-up")
    if "Practice" not in h3:
        say(f"{slug}: needs a practice after its new idea")
    if h3.count("Try It") != 1:
        say(f"{slug}: needs exactly one Try It")
    if not h3 or h3[-1] != "What you can do now":
        say(f"{slug}: must end with 'What you can do now'")
    else:
        tail = blocks[[i for i, (k, p) in enumerate(blocks) if k == "h3" and p == h3[-1]][0] + 1:]
        lists = [p for k, p in tail if k in ("ol", "ul")]
        if not lists or len(lists[0]) != 3:
            say(f"{slug}: the wrap-up is three lines")
        if not any(k == "p" and p.startswith("Key words:") for k, p in tail):
            say(f"{slug}: the wrap-up names its key words ('Key words: ...')")

    found = exercises(blocks)
    if len(found) > MAX_EXERCISES:
        say(f"{slug}: {len(found)} exercises; a 20-to-30-minute lesson has at most {MAX_EXERCISES}")
    words = prose_words(blocks)
    if words > MAX_WORDS:
        say(f"{slug}: {words} words of prose; at most {MAX_WORDS}")

    for number, section, item, code, hints in found:
        key = f"{slug}#{number}"
        spec, solution = checks.get(key), solutions.get(key)
        if not spec and not solution:
            say(f"{key}: has neither a check nor a worked solution")
        for label, answer in (("worked solution", solution and solution["code"]),
                              ("alternate answer", ALTERNATES.get(key))):
            if spec and answer:
                result = run_check(spec, answer)
                if result is not None and not result[0]:
                    say(f"{key}: the {label} fails its own check -- {result[1][0] if result[1] else ''}")
        if section == "Try It":
            if [h.split(":")[0] for h in hints[:len(hint_steps)]] != list(hint_steps):
                say(f"{key}: the hints must walk {', '.join(hint_steps)}, in that order")
            if not hints or f"({REFERENCE}.html)" not in hints[0]:
                say(f"{key}: the first hint links to the reference page")
            if not solution:
                say(f"{key}: a try it ends in a worked solution")
            elif "# Say it" not in solution["code"] or "# Split it" not in solution["code"]:
                say(f"{key}: the worked solution keeps its Say it and Split it comments")
            if spec and key not in ALTERNATES:
                say(f"{key}: a checked try it needs an alternate answer in ALTERNATES")
    return problems


def unit_problems(pages, checks):
    """What the spec asks of unit 2 as a whole."""
    problems = []
    unit = {slug: text for slug, text in pages.items() if slug.startswith("ch02")}
    found = {slug: exercises(blocks_of(text)) for slug, text in unit.items()}
    if not any("error" in item.lower() and checks.get(f"{slug}#{n}")
               for slug, items in found.items() for n, _, item, _, _ in items):
        problems.append("unit 2: needs a checked fix-the-bug practice that starts from an error")
    if not any(checks.get(f"ch02a-naming-a-value#{n}", {}).get("kind") == "trace"
               for n, *_ in found.get("ch02a-naming-a-value", [])):
        problems.append("ch02a-naming-a-value: tracing starts here, with a trace table")
    if not any(re.search(r"\b(True|False)\b", json.dumps(checks.get(f"ch02b-names-and-kinds#{n}", {})) + code)
               for n, _, _, code, _ in found.get("ch02b-names-and-kinds", [])):
        problems.append("ch02b-names-and-kinds: True and False get a practice of their own")
    receipt = [code for k, code in blocks_of(unit.get("ch02d-putting-it-together", ""))
               if k == "code" and "input(" in code and "total" in code]
    examples = [code for k, code in blocks_of(unit.get("ch02d-putting-it-together", "")) if k == "code"]
    in_exercises = {code for *_, code, _ in found.get("ch02d-putting-it-together", [])}
    if [c for c in receipt if c in examples and c not in in_exercises]:
        problems.append("ch02d-putting-it-together: the finished receipt is shown in an example")
    return problems


def main():
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    vol = next((v for v in build.VOLS if v["slug"] == VOLUME), None)
    if vol is None:
        print(f"  FAIL  volumes/{VOLUME} does not exist\n\n1 wrong")
        sys.exit(1)
    meta = json.loads((vol["dir"] / "volume.json").read_text())
    checks = build.load_json(vol, "_checks.json")
    solutions = build.load_solutions(vol)
    pages = {p.stem: p.read_text() for p in build.chapter_files(vol)}
    problems = []

    for slug, heading, steps in LESSONS:
        if only and slug not in only:
            continue
        if slug not in pages:
            problems.append(f"{slug}: missing")
            continue
        problems += lesson_problems(slug, heading, steps, pages[slug], checks, solutions)

    if not only or REFERENCE in only:
        text = pages.get(REFERENCE, "")
        if not text.startswith("## How to start a problem"):
            problems.append(f"{REFERENCE}: missing, or not headed 'How to start a problem'")
        for step in STEPS:
            if f"### {step}" not in text:
                problems.append(f"{REFERENCE}: no section for {step}")

    if not only:
        if not meta.get("lessons") or meta.get("status") != "in progress":
            problems.append('volume.json: needs "lessons": true and "status": "in progress"')
        order = [slug for slug, *_ in LESSONS] + [REFERENCE]
        if list(pages) != order:
            problems.append(f"the pages, in reading order, must be {order}; found {list(pages)}")
        problems += unit_problems(pages, checks)
        for path in sorted(vol["dir"].rglob("*")):
            if path.is_file() and "claude.ai" in path.read_text(errors="replace"):
                problems.append(f"{path.relative_to(ROOT)}: the public course never links to claude.ai")

    for line in problems:
        print(f"  !! {line}")
    print(f"\n{'the lessons keep their promises' if not problems else str(len(problems)) + ' problem(s)'}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/steps_volume_test.py`
Expected: `FAIL  volumes/vol1-steps does not exist`.

- [ ] **Step 3: Create the volume and the reference page**

`volumes/vol1-steps/volume.json`:

```json
{
  "number": 2,
  "title": "Python Foundations, step by step",
  "subtitle": "The same course in short lessons",
  "blurb": "Short lessons of twenty to thirty minutes: one idea at a time, practice straight after it, and a routine for starting any problem.",
  "lessons": true,
  "status": "in progress"
}
```

`content/_checks.json` and `content/_boxes.json`: `{}`. `content/_solutions.md`:

```markdown
<!-- Worked solutions for vol1-steps, one "## <page>#<n>" heading each. Never published. -->
```

`content/99-how-to-start-a-problem.md` is the reference page. It has no part line, no exercises and no checks,
and must be under 600 words. Write it as follows.

Heading and opening:
- heading `## How to start a problem`;
- a one-paragraph opening: when you don't know where to begin, these five steps give you somewhere to begin,
  and each is small.

Then one `###` section per step, in order. Each section has two or three sentences and the running example's
state at that step, shown as a fence:

- `### Say it`: write the problem in your own words, as a comment at the top.
- `### Split it`: break it into small steps, one comment line each.
- `### Name it`: choose names that say what each value means.
- `### Build it`: turn one comment into code, run it, then the next.
- `### Check it`: try an ordinary input and an awkward one.

The running example is "A bag holds 6 apples. How many apples are in 5 bags?" It is deliberately not any
lesson's try-it, so no solution is spoiled. Use only `print`, numbers, `*` and variables, so the gate stays
green whatever lessons precede it. State no outputs (no `Output:` fences): the page is a reference, not a
lesson. Its finished program:

```python
# Say it: work out how many apples are in 5 bags of 6.
# Split it:
# 1. store how many apples a bag holds
# 2. store how many bags
# 3. multiply, and print the answer
apples_per_bag = 6
bags = 5
print(apples_per_bag * bags)
```

Its Check it section explains how to try a different number of bags (0, then a big number) by editing the
second line, and asks whether the answer still makes sense.

- [ ] **Step 4: Run it**

```bash
python3 tests/steps_volume_test.py --only 99-how-to-start-a-problem && /usr/bin/python3 tests/steps_volume_test.py --only 99-how-to-start-a-problem
python3 tests/steps_volume_test.py | tail -3
python3 tests/lesson_vocabulary_test.py | tail -1
python3 build.py --check | tail -1
```

Expected:
- the `--only` run passes, twice;
- the full run fails, listing each missing lesson;
- the vocabulary gate passes;
- the build still reports `110 checked, 0 mismatched` (the reference page states no outputs).

- [ ] **Step 5: Prove the contract can fire**

The full run fails only on missing lessons, so prove the per-lesson rules fire on a planted lesson. Copy
`tests/steps_volume_test.py` to the scratchpad, add a temporary `LESSONS` entry for a page
`ch02z-planted.md` that has no warm-up and no wrap-up and whose try-it hints are in the wrong order, then run
`--only ch02z-planted`. Expect each of those three rules to print a `!!` line. Delete the planted page and the
copy. Ledger the output.

- [ ] **Step 6: Wire CI and commit**

Add `python3 tests/steps_volume_test.py` to the build job's "Practice pages, volumes, the site guard and the
disclaimer" step, after the vocabulary gate. It will fail until Task 7, so it stays out of CI until then:
- for now, add it with `--only 99-how-to-start-a-problem`;
- Task 7 removes the flag.

```bash
git add volumes/vol1-steps tests/steps_volume_test.py .github/workflows/ci.yml
git commit -F - <<'MSG'
course: the step-by-step volume, its reference page, and its contract

volumes/vol1-steps/ starts with "How to start a problem", the routine every
lesson's hints point to: say it, split it, name it, build it, check it.
steps_volume_test.py pins the shape the spec gives every lesson (warm-up,
practice after each idea, one try it whose hints walk the routine in order,
a worked solution behind them, a three-line wrap-up), runs every worked
solution and an answer in a different style through the same check, and caps
a lesson at ten exercises and 1,300 words.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

## How Tasks 3 to 7 write a lesson

Each lesson task gives:
- the page skeleton;
- every example with its stated output;
- every exercise with its exact check and worked solution;
- the hints;
- what each prose paragraph must say.

The prose is written by the executor, to the Global Constraints' reading level. Then, for each lesson:

1. Run `python3 tests/steps_volume_test.py --only <slug>` first and watch it fail ("missing").
2. Write the page, then add its checks to `_checks.json`, its solutions to `_solutions.md` (one
   `## <slug>#<n>` heading each), and any `_boxes.json` declarations.
3. Run, all of which must pass:
   - `python3 tests/steps_volume_test.py --only <slug>` under both Pythons;
   - `python3 tests/lesson_vocabulary_test.py`;
   - `python3 build.py --check`, still `0 mismatched` with no `UNEXPECTED` box.
4. Open the built page (`python3 scripts/serve.py 8000 site` in the background, then
   `http://localhost:8000/vol1-steps/<slug>.html`) and run one checked exercise through its Check button. Stop
   the server afterward.
5. Commit with a message naming the lesson and what it teaches.

Box numbers in `_boxes.json` count every `python` fence on the page from 0, examples and exercises alike, in
order. Bare output fences (no language) do not count. Each task gives the index; if `build.py --check` reports
an `UNEXPECTED` box, recount, fix the index, and ledger it.

Prose blocks marked **Write:** list what the paragraph must say, not its words. Keep each paragraph to about
four sentences.

---

### Task 3: Lesson 0 — Welcome back

**Files:** Create `volumes/vol1-steps/content/ch01z-welcome-back.md`. Modify `_checks.json` and `_solutions.md`.

**Interfaces:** Consumes Task 2's contract and reference page. Exercises 1 to 5. No `_boxes.json` entries.

The page, in order:

````markdown
<!-- part: Unit 1 — Your first programs -->
## Lesson 0 — Welcome back
````

**Write:** welcome back. This short lesson replays the two things from unit 1 everything else rests on
(printing, and letting Python do arithmetic), then introduces a way to start any problem. About 20 minutes;
every grey box runs.

`### Printing text and numbers`, with three examples, each followed by `Output:` and its output fence:

```python
print("Hello, world!")
```
→ `Hello, world!`

```python
print("Hydrogen", "Helium", "Lithium")
```
→ `Hydrogen Helium Lithium`. **Write:** commas print several things on one line, one space between them.

```python
print(3 + 4)
print("3 + 4")
```
→ `7` then `3 + 4`. **Write:** without quotes Python works it out; with quotes it prints the characters
exactly. Text in quotes is a **string**.

`### Practice`:
1. `Which line prints exactly 3 + 4?` — check
   `{"kind": "choice", "options": ["`print(3 + 4)`", "`print(\"3 + 4\")`"], "answer": 1, "why": "Inside quotes, Python prints the characters exactly."}`
2. ``Print the words `cats` and `dogs` on one line, using one `print()`.`` — check
   `{"kind": "stdin", "runs": [{"typed": [], "words": ["cats", "dogs"]}]}`; solution `print("cats", "dogs")`.

`### Working things out`, with two examples:

```python
# hours in a week
print(24 * 7)
```
→ `168`. **Write:** a **comment** starts with `#`; Python skips it; it is a note for people.

```python
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 / 4)
```
→ `14`, `6`, `40`, `2.5`. **Write:** the four operators; `*` multiplies and `/` divides.

`### Practice`:

3. ``Make Python work out the number of minutes in a week. Use a calculation, not the answer.`` — check
   `{"kind": "stdin", "runs": [{"typed": [], "numbers": [10080]}]}`; solution
   `# minutes in a week\nprint(7 * 24 * 60)`.
4. `Predict what this prints, then press Check.`, with this fence, and check `{"kind": "predict"}`:

```python
print("2 * 3")
print(2 * 3)
```

`### A way to start any problem`

**Write:**
- Here is a problem sentence: "Print a receipt for 3 notebooks at 2 dollars each, with the total."
- Before writing code, **Say it**: say what the program must do, in your own words, as a comment.
- Then **Split it**: list the small steps, one comment each.
- Then **Build it**: turn one comment into code, run it, then the next.

Then three examples, each building on the last (stated outputs: none, then one line, then two lines):

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the item line
# 2. print the total
```

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the item line
# 2. print the total
print("3 notebooks at 2 dollars each")
```
→ `3 notebooks at 2 dollars each`

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the item line
# 2. print the total
print("3 notebooks at 2 dollars each")
print("Total:", 3 * 2)
```
→ `3 notebooks at 2 dollars each` / `Total: 6`

**Write:** the comments stay in the finished program, where they explain it. Link
`[How to start a problem](99-how-to-start-a-problem.html)`: the whole routine, which the coming lessons add to.

`### Try It`:

5. `Print a receipt for 2 pencils at 1 dollar each and 1 eraser at 3 dollars, with the total worked out by Python.`

> Say it: in your own words, what must the receipt show? Write it as a comment. ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: three steps, one comment each: the pencils line, the eraser line, the total.

Check `{"kind": "stdin", "runs": [{"typed": [], "numbers": [5]}]}`. Solution:

```python
# Say it: show what was bought, then what it all costs.
# Split it:
# 1. print the pencils line
# 2. print the eraser line
# 3. print the total, worked out by Python
print("2 pencils at 1 dollar each")
print("1 eraser at 3 dollars")
print("Total:", 2 * 1 + 3)
```

Solution note: "Your words can differ. What matters is a comment for each step, and a total Python works out."

`### What you can do now`: three items:
- print text and numbers;
- let Python do arithmetic;
- start a problem by saying it and splitting it into steps.

Then `Key words: **string**, **comment**, **Say it, Split it, Build it**.`

Commit: `course: lesson 0, welcome back` with a body naming the recap and the routine's first three steps.

---

### Task 4: Lesson 2.1 — Naming a value

**Files:** Create `ch02a-naming-a-value.md`. Modify `_checks.json`, `_solutions.md`, `_boxes.json`.

**Interfaces:** Exercises 1 to 7. `_boxes.json`: `"ch02a-naming-a-value#4": {"raises": "NameError", "why": "Fix-the-bug practice: the name is used before it exists."}` (box 4 is exercise 4's fence).

````markdown
<!-- part: Unit 2 — Variables and types -->
## Lesson 2.1 — Naming a value
````

**Write:** one sentence on what this lesson does: give a value a name, change it, and follow a program line by
line.

`### Warm-up`:
1. `Predict what this prints, then press Check.`, with fence `print("2 + 2", 2 + 2)` and check
   `{"kind": "predict"}`.
2. ``What does Python do with a line that starts with `#`?`` — check
   `{"kind": "choice", "options": ["Runs it", "Skips it: it is a note for people"], "answer": 1, "why": "A comment is for whoever reads the code."}`

`### A name for a value`, with three examples and outputs:
- `price = 12` then `print(price)` → `12`.
- `price = 12`, `count = 3`, `print(price * count)` → `36`.
- `player = "Ada"`, `print("Hello,", player)` → `Hello, Ada`.

**Write:**
- A **variable** is a name for a value.
- `=` is not "equals" from math. It means "let the name on the left stand for the value on the right", so
  read `price = 12` as "let price be 12". The name always goes on the left.
- After that, writing the name gives the value.

`### Practice`:
3. ``Store `7` in a variable called `days`, then print how many hours that is: `days` times 24.`` — check
   `{"kind": "stdin", "runs": [{"typed": [], "numbers": [168]}]}`; solution `days = 7\nprint(days * 24)`.
4. `This program stops with an error. Run it and read the last line of the error. Then fix it so it prints 5.`,
   with this fence:

```python
print(total)
total = 5
```

Check `{"kind": "stdin", "runs": [{"typed": [], "numbers": [5]}]}`. Solution `total = 5\nprint(total)`, with
the note: "Python runs top to bottom, so a name must get its value before anything uses it. The error said
`NameError: name 'total' is not defined`, which means not defined *yet*."

`### Changing a value`, with three examples and outputs:
- `score = 10`, `score = 20`, `print(score)` → `20`. **Write:** a name can be pointed at a new value; the old
  one is forgotten.
- `count = 5`, `count = count + 1`, `print(count)` → `6`. **Write:** Python works out the right side first (5 +
  1), then points the name at the answer.

  Introduce a **trace table**: one row per line, the value of each variable after that line. Show this
  table:

  | After line | count |
  | --- | --- |
  | 1 | 5 |
  | 2 | 6 |
  | 3 | 6 |

  (Row 3, the `print`, changes nothing.) **Write:** tracing by hand is how you check what a program does
  before you run it.
- `a = 10`, `b = a`, `a = 99`, `print(a, b)` → `99 10`. **Write:** `b = a` gave `b` the value 10 at that
  moment. `b` does not follow `a` afterward.

`### Practice`:
5. `Fill in the table: the value of each variable after each line. Leave a cell empty (or write -) if the variable has no value yet. Then press Check.`
   Fence `price = 12\ncount = 3\nprice = price + count`, check `{"kind": "trace", "names": ["price", "count"]}`.
6. `Fill in the table, then press Check.` Fence `lives = 3\nlives = lives - 1\nlives = lives + 2`, check
   `{"kind": "trace", "names": ["lives"]}`.

`### Try It`:

7. `A game gives you 5 coins. You spend 2, then find 4 more. Use one variable, and print how many coins you have at the end.`

> Say it: what happens to the coins, in your own words? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: one step for each thing that happens: start with 5, spend 2, find 4, print.

Check `{"kind": "stdin", "runs": [{"typed": [], "numbers": [7]}]}`. Solution:

```python
# Say it: start with 5 coins, spend 2, find 4, show what is left.
# Split it:
# 1. start with 5 coins
# 2. spend 2
# 3. find 4 more
# 4. print the coins
coins = 5
coins = coins - 2
coins = coins + 4
print(coins)
```

`### What you can do now`: three items:
- give a value a name;
- change it, including from its own old value;
- trace a program line by line.

Then `Key words: **variable**, **trace table**.`

---

### Task 5: Lesson 2.2 — Names that explain, and kinds of value

**Files:** Create `ch02b-names-and-kinds.md`. Modify `_checks.json`, `_solutions.md`.

**Interfaces:** Exercises 1 to 10. No `_boxes.json` entries.

````markdown
<!-- part: Unit 2 — Variables and types -->
## Lesson 2.2 — Names that explain, and kinds of value
````

`### Warm-up`:
1. `Fill in the table, then press Check.` Fence `x = 4\nx = x * 2`, check `{"kind": "trace", "names": ["x"]}`.
2. `Predict what this prints, then press Check.` Fence `a = 3\nb = a\na = 8\nprint(a, b)`, check
   `{"kind": "predict"}`.

`### Names that explain`, with two examples:
- `d = 14` then `print(d * 24)` → `336`.
- `days_until_exam = 14` then `print(days_until_exam * 24)` → `336`.

**Write:**
- Same program, same answer. A week from now, only the second still tells you what it is about.
- This is **Name it**, the third step of the routine: choose names that say what each value means.
- The rules Python enforces, as a list: letters, digits and underscores only; no digit first; no spaces.
- Capital letters matter: `Score` and `score` are different names.
- The habit is **snake_case**: lowercase words joined by underscores.

`### Practice`:
3. `Which name says what the number means?` — check
   `{"kind": "choice", "options": ["`x = 3600`", "`seconds_per_hour = 3600`"], "answer": 1, "why": "The name says what 3600 is."}`
4. `Which of these is a name Python accepts?` — check
   `{"kind": "choice", "options": ["`2nd_place`", "`second_place`", "`second place`"], "answer": 1, "why": "A name cannot start with a digit or contain a space."}`
5. ``This works out how many pencils are in 3 boxes of 2. Rename `a`, `b` and `c` so the program explains itself. It should still print 6.``
   Fence `a = 3\nb = 2\nc = a * b\nprint(c)`; check `{"kind": "stdin", "runs": [{"typed": [], "numbers": [6]}]}`.
   Solution `boxes = 3\npencils_per_box = 2\ntotal_pencils = boxes * pencils_per_box\nprint(total_pencils)`,
   with the note "Any names that say what each number is are right."

`### Kinds of value`

**Write:** every value has a **type**, its kind. Show a three-row table:

| Type | Kind | Examples |
| --- | --- | --- |
| `int` | whole number | `7`, `0`, `-250` |
| `float` | number with a decimal point | `3.14`, `7.0` |
| `str` | text, in quotes | `"hello"`, `"7"` |

Then two examples:
- `print(type(7))`, `print(type(7.0))`, `print(type("7"))` → `<class 'int'>`, `<class 'float'>`,
  `<class 'str'>`. **Write:** `type()` tells you the kind.
- `print(7 + 7)`, `print("7" + "7")` → `14`, `77`. **Write:** adding numbers adds; adding strings glues them
  end to end, which is called **concatenation**.

`### Practice`:
6. `Predict what this prints, then press Check.` Fence `print(type(2.5))`, check `{"kind": "predict"}`.
7. `What kind of value is "42", with the quotes?` — check
   `{"kind": "choice", "options": ["a whole number, `int`", "text, `str`"], "answer": 1, "why": "Quotes make it text, whatever is inside."}`

`### True and False`

Two examples:
- `game_over = False`, `print(game_over)`, `print(type(game_over))` → `False`, `<class 'bool'>`.
- `print(type(True))`, `print(type("True"))` → `<class 'bool'>`, `<class 'str'>`.

**Write:**
- `True` and `False` are a kind of value of their own, called **bool**.
- They have a capital letter and no quotes. With quotes, they would just be text.
- Programs make every decision with them, from unit 4 on.

`### Practice`:
8. `Which one is a True/False value, not text?` — check
   `{"kind": "choice", "options": ["`\"False\"`", "`False`", "`false`"], "answer": 1, "why": "No quotes, and a capital F."}`
9. `Fill in the table, then press Check.` Fence `lights_on = False\nlights_on = True`, check
   `{"kind": "trace", "names": ["lights_on"]}`.

`### Try It`:

10. `A recipe uses 3 eggs for each cake. You are baking 4 cakes. Store each number in a variable whose name says what it is, then print how many eggs you need.`

> Say it: what are you working out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: store the eggs per cake, store the number of cakes, multiply and print.
> Name it: a name for each number that a friend would understand, such as `eggs_per_cake`.

Check `{"kind": "stdin", "runs": [{"typed": [], "numbers": [12]}]}`. Solution:

```python
# Say it: work out how many eggs 4 cakes need, at 3 eggs a cake.
# Split it:
# 1. store the eggs each cake needs
# 2. store how many cakes
# 3. multiply, and print the answer
eggs_per_cake = 3
cakes = 4
print(eggs_per_cake * cakes)
```

`### What you can do now`: three items:
- choose names that explain;
- tell `int`, `float`, `str` and `bool` apart with `type()`;
- know that `"7"` and `7` are different kinds of value.

Then `Key words: **snake_case**, **type**, **int**, **float**, **str**, **bool**, **concatenation**.`

---

### Task 6: Lesson 2.3 — Asking the user

**Files:** Create `ch02c-asking-the-user.md`. Modify `_checks.json`, `_solutions.md`, `_boxes.json`.

**Interfaces:** Exercises 1 to 7. `_boxes.json`: `"ch02c-asking-the-user#6": {"raises": "ValueError", "why": "Shows the error an awkward input causes."}` (box 6 is the `int("fourteen")` example; see the count below).

````markdown
<!-- part: Unit 2 — Variables and types -->
## Lesson 2.3 — Asking the user
````

`### Warm-up`:
1. `What does print("5" + "5") print?` — check
   `{"kind": "choice", "options": ["`10`", "`55`"], "answer": 1, "why": "Two strings glued together."}`
2. `Which name explains itself best?` — check
   `{"kind": "choice", "options": ["`n`", "`number_of_guests`"], "answer": 1, "why": "It says what the number counts."}`

`### Asking a question`. Example (box 0):

```python
name = input("What is your name? ")
print("Nice to meet you,", name)
```

then `A sample run:` and an output fence: `What is your name? Ada` / `Nice to meet you, Ada`.

**Write:**
- `input()` pauses, waits for typing and Enter, and gives back what was typed.
- The text in the brackets is the **prompt**. End it with a space.
- On this page, Run opens a box to type in.

`### Practice`:
3. `Ask for the user's favorite animal, and print a sentence that uses it.` — check
   `{"kind": "stdin", "runs": [{"typed": ["otter"], "words": ["otter"]}]}`; solution
   `animal = input("What is your favorite animal? ")\nprint("I like", animal, "too!")`.

`### Text, not a number`. Three examples. The first is box 1:

```python
age = input("How old are you? ")
print(age + 1)
```

then `If the user types `14`, this crashes:` and output fence
`TypeError: can only concatenate str (not "int") to str`.

**Write:** `input()` always gives back text, even when the typing is digits. `"14" + 1` makes no sense to
Python.

Box 2:

```python
age = int(input("How old are you? "))
print("Next year you will be", age + 1)
```

then `A sample run:` with `How old are you? 14` / `Next year you will be 15`.

**Write:** `int()` turns text into a whole number. Read the line from the inside out: `input()` first, then
`int()`.

Box 3:

```python
price = float(input("Price: "))
print(price * 2)
```

then `A sample run:` with `Price: 2.5` / `5.0`. **Write:** `float()` for numbers with a decimal point.

`### Practice`:
4. `This program stops with an error when you type a number. Run it, type 60, and read the last line of the error. Then fix it.` Fence (box 4):

```python
height = input("Height in inches: ")
print("That is", height / 12, "feet")
```

Check `{"kind": "stdin", "runs": [{"typed": ["60"], "numbers": [5]}]}`. Solution
`height = float(input("Height in inches: "))\nprint("That is", height / 12, "feet")`, with the note "`int()`
works too, for whole inches."

5. `Ask for two whole numbers, and print their sum.` — check
   `{"kind": "stdin", "runs": [{"typed": ["6", "4"], "numbers": [10]}, {"typed": ["0", "-3"], "numbers": [-3]}]}`.
   Solution `first = int(input("First number: "))\nsecond = int(input("Second number: "))\nprint(first + second)`.

`### Check it: try an awkward input`

**Write:**
- **Check it** is the routine's last step: once it works with an ordinary input, try one that might break it:
  0, a negative number, a decimal, a word.
- Two things to know first.

Box 5: `print(int("14"))`, `print(int(3.9))` → `14`, `3`. **Write:** `int()` of a decimal cuts off the part
after the point; it does not round.

Box 6 (declared `raises`):

```python
number = int("fourteen")
```

Copy the pattern of `ch01-your-first-programs`'s SyntaxError example for the label and fence that follow.
That is a paragraph ending `responds with something like:` and then an output fence holding
`ValueError: invalid literal for int() with base 10: 'fourteen'`. If `build.py --check` disputes the stated
output, match its exact text and ledger it. **Write:** a word cannot become a whole number, and later units
show how a program can cope with that.

`### Practice`:
6. `A program asks "Cookies: " and runs int(input(...)) on the answer. Which input is the awkward one worth trying?` — check
   `{"kind": "choice", "options": ["`10`", "`ten`"], "answer": 1, "why": "A word cannot become a whole number, so int() stops with a ValueError."}`

`### Try It`:

7. `Ask how many minutes a movie lasts, and print how many hours that is.`

> Say it: minutes go in; what comes out? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: ask for the minutes, turn them into a number, divide by 60, print.
> Name it: what would you call the minutes, and the hours?
> Check it: try 90, then 45. Do the answers make sense?

Check `{"kind": "stdin", "runs": [{"typed": ["90"], "numbers": [1.5]}, {"typed": ["120"], "numbers": [2]}]}`.
Solution:

```python
# Say it: ask for a movie's length in minutes, and show it in hours.
# Split it:
# 1. ask for the minutes, as a number
# 2. divide by 60
# 3. print the hours
minutes = int(input("How many minutes is the movie? "))
hours = minutes / 60
print("That is", hours, "hours")
```

Solution note: "45 gives 0.75 hours, which is right: three quarters of an hour."

`### What you can do now`: three items:
- ask the user for text with `input()`;
- turn it into a number with `int()` or `float()`;
- check a program with an awkward input.

Then `Key words: **input()**, **prompt**, **int()**, **float()**, **Check it**.`

---

### Task 7: Lesson 2.4 — Putting it together, and the unit 2 quiz

**Files:**
- Create `ch02d-putting-it-together.md`.
- Modify `_checks.json` and `_solutions.md`.
- Create `volumes/vol1-steps/quizzes.json`, and generate `quizzes/` and `answer-keys/` from it.
- Modify `.github/workflows/ci.yml`: drop the `--only` flag from Task 2.

**Interfaces:** Exercises 1 to 7. No `_boxes.json` entries. The unit quiz attaches to `ch02d-putting-it-together`.

````markdown
<!-- part: Unit 2 — Variables and types -->
## Lesson 2.4 — Putting it together
````

`### Warm-up`:
1. `Predict what this prints, then press Check.` Fence `price = 3.5\nprint(price * 2)`, check
   `{"kind": "predict"}`.
2. `What kind of value does input() give back?` — check
   `{"kind": "choice", "options": ["a number, if you type digits", "text, always"], "answer": 1, "why": "Even digits come back as text. That is why int() and float() exist."}`

`### The problem`

**Write:**
- Lesson 0's receipt typed every price twice: once to show it, once in the total. Change one and forget the
  other, and the receipt lies.
- Here is the problem sentence: "Write a receipt program for the Corner Store. It asks for the customer's name,
  stores each price once in a variable with a clear name, and works out the total from those variables."
- This lesson builds it with the whole routine. You write every line.

Then one example, comments only (box 1, no output):

```python
# Say it: ask who the customer is, then print a receipt whose total
# is worked out from the prices, each stored once.
# Split it:
# 1. ask for the customer's name and print it
# 2. store each price in a variable
# 3. print a line for each item
# 4. work out the total from the variables and print it
```

**Write (Name it):**
- The names this receipt will use: `customer`, `notebook_price`, `pens_price`, `stickers_price`, `total`.
- Why each says what it holds.

`### Practice`. These are the routine's Build it step; each starts from the plan.

3. `Step 1: under the plan, ask for the customer's name and print "Customer:" followed by it. Run it.`
   Starter fence (box 2) is the comments above. Check
   `{"kind": "stdin", "runs": [{"typed": ["Ada"], "words": ["Ada"]}]}`. Solution: comments, then
   `customer = input("Customer name: ")\nprint("Customer:", customer)`.
4. `Steps 2 and 3: store the three prices in variables (notebook 3.50, pens 2.25, stickers 1.75) and print a line for each item. Copy your step 1 in first.`
   No starter fence. Check `{"kind": "stdin", "runs": [{"typed": ["Ada"], "numbers": [3.5, 2.25, 1.75]}]}`.
   Solution: comments, step 1, the three `*_price` assignments, and three `print("Notebook", notebook_price)`
   style lines.
5. `Step 4: work out the total from the three variables, and print it.`
   Check `{"kind": "stdin", "runs": [{"typed": ["Ada"], "numbers": [3.5, 2.25, 1.75, 7.5]}]}`. Solution: the
   whole receipt so far plus `total = notebook_price + pens_price + stickers_price` and `print("Total", total)`.

`### Check it`

**Write:**
- Run your receipt with an ordinary name, then an awkward one: press Enter without typing. Does it still make
  sense?
- Then change one price. The line and the total change together, because both read the same variable: one
  fact, stored in one place.

`### Practice`:
6. `You change pens_price to 3.00 and run it again. What happens to the total?` — check
   `{"kind": "choice", "options": ["It stays 7.5 until you change the total too", "It becomes 8.25 by itself"], "answer": 1, "why": "The total is worked out from the variables each time the program runs."}`

`### Try It`:

7. `The store starts selling rulers at 1.25. Add a ruler to your receipt, so its line and the total are both right. Copy your receipt from exercise 5 in first.`

> Say it: what has to change on the receipt? ([How to start a problem](99-how-to-start-a-problem.html))
> Split it: add a comment for each new step, where it belongs in the plan.
> Name it: what will you call the ruler's price?
> Check it: is the new total 8.75? Then change the ruler's price. Does the total follow?

Check `{"kind": "stdin", "runs": [{"typed": ["Ada"], "numbers": [1.25, 8.75]}]}`. The worked solution is the
full receipt with the ruler: the plan's comments with a ruler step added, `ruler_price = 1.25`, its line printed
after stickers, and `total` including it. It is the only place the finished receipt appears, behind all four
hints.

`### What you can do now`: three items:
- turn a problem sentence into a plan of comments;
- build it a step at a time;
- check it with an awkward input and a changed value.

Then `Key words: **Say it**, **Split it**, **Name it**, **Build it**, **Check it**.` Then one sentence: "That
is the end of unit 2. Its quiz is below: fill it in, then show or print it."

**The unit 2 quiz.** Create `volumes/vol1-steps/quizzes.json` with
`{"quizzes": [{"slug": "ch02d-putting-it-together", "questions": [...]}]}`:
- every question of `vol1-foundations`' `ch02-variables-and-types` quiz, copied verbatim (all 16 are taught in
  2.1 to 2.3);
- two additions, appended in their sections:
  - `{"section": "Reading code", "text": "What does this print? ____", "code": "coins = 5\ncoins = coins - 2\ncoins = coins + 4\nprint(coins)", "answers": ["7"]}`
  - `{"section": "Why it works", "text": "Trying an input that might break a program, such as a word where a number is expected, is the ____ it step of the routine.", "answers": ["Check"]}`

Run `python3 scripts/make_quizzes.py vol1-steps`. It writes `volumes/vol1-steps/quizzes/` and
`volumes/vol1-steps/answer-keys/`. The quiz must be headed `Unit 2 - Variables and types`.

- [ ] Verify:

```bash
python3 tests/steps_volume_test.py && /usr/bin/python3 tests/steps_volume_test.py
python3 tests/quiz_test.py | tail -3
python3 tests/lesson_vocabulary_test.py | tail -1
python3 build.py --check | tail -1
head -3 volumes/vol1-steps/quizzes/ch02d-putting-it-together-quiz.txt
grep -o '<p class="quiz">.*quiz</a>' site/vol1-steps/ch02d-putting-it-together.html
```

Expected:
- the whole-volume pass line, twice;
- `vol1-steps: all 2 quizzes and keys are what quizzes.json renders` among the quiz lines;
- the gate passes, and the build reports `0 mismatched`;
- the heading `Unit 2 - Variables and types`;
- a link labeled `Unit 2 quiz`.

Remove `--only 99-how-to-start-a-problem` from the CI line; run `python3 tests/workflow_test.py` and
`actionlint`.

Commit lesson 2.4 and the quiz together: `course: lesson 2.4, the receipt built step by step, and the unit 2 quiz`.

---

### Task 8: The lessons in a real browser, on a phone-width screen and under the Pages path

**Files:**
- Create: `tests/steps_browser_test.mjs`
- Modify: `.github/workflows/ci.yml` (browser job)

**Interfaces:** Consumes `browser_harness.mjs`: `startSite(port) -> {baseUrl, stop}`,
`launch(chromium, stop) -> browser`, `loadChromium()`. Uses the built site as it is; it does not rebuild.

- [ ] **Step 1: Write the test**

```javascript
/* The step-by-step lessons in a real browser. Every page loads without a
 * script error, fits a 390-pixel phone screen without sideways scrolling,
 * and its links (hints to the reference page, the unit quiz) resolve. One
 * checked exercise goes through Python in the page. Run it with BASE=/name/
 * too, the way GitHub Pages serves the site. */
import { launch, loadChromium, startSite } from "./browser_harness.mjs";

const PORT = 8744;
const PAGES = ["ch01z-welcome-back", "ch02a-naming-a-value", "ch02b-names-and-kinds",
               "ch02c-asking-the-user", "ch02d-putting-it-together", "99-how-to-start-a-problem"];

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const browser = await launch(chromium, stop);
let bad = 0;
const expect = (label, ok) => { if (!ok) bad++; console.log(`  ${ok ? "ok  " : "FAIL"}  ${label}`); };
try {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const errors = [];
  page.on("pageerror", (e) => errors.push(e.message));
  for (const slug of PAGES) {
    const url = `${baseUrl}vol1-steps/${slug}.html`;
    const response = await page.goto(url, { waitUntil: "load" });
    expect(`${slug} loads`, response && response.ok());
    expect(`${slug} fits a phone screen`, await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth));
    for (const href of await page.$$eval("a[href]", (as) => as.map((a) => a.href))) {
      if (!href.startsWith(baseUrl)) continue;
      const linked = await page.request.get(href);
      if (!linked.ok()) expect(`${slug} links to ${href}`, false);
    }
  }
  expect("no page raised a script error", errors.length === 0);

  await page.goto(`${baseUrl}vol1-steps/ch02a-naming-a-value.html`, { waitUntil: "load" });
  const box = page.locator('[data-box="vol1-steps/ch02a-naming-a-value#3"]');
  await box.locator("textarea").fill("days = 7\nprint(days * 24)");
  await box.locator(".check").click();
  await page.waitForFunction(() => /passed|failed/.test(
    document.querySelector('[data-box="vol1-steps/ch02a-naming-a-value#3"] .result').className), null, { timeout: 60000 });
  expect("a lesson exercise is checked by Python in the page",
         (await box.locator(".result").getAttribute("class")).includes("passed"));
} finally {
  await browser.close();
  stop();
}
console.log(`\n${bad ? bad + " wrong" : "the lessons work in a real browser, on a phone, under any path"}`);
process.exit(bad ? 1 : 0);
```

- [ ] **Step 2: Run it, and prove it can fail**

```bash
python3 build.py > /dev/null
cd tests && REQUIRE_BROWSER=1 node steps_browser_test.mjs && REQUIRE_BROWSER=1 BASE=/python-foundations/ node steps_browser_test.mjs
```

Expected: the pass line twice.

Then prove the phone check fires. Temporarily add `<pre>` with an 80-character unbroken line to the reference
page's prose (not a fence). Rebuild, expect "99-how-to-start-a-problem fits a phone screen" to FAIL. Remove it
and rebuild. If a real page fails the phone check, fix the CSS cause (`web/app.css`), not the test, and confirm
`vol1-foundations` still renders identically apart from `app.css`.

- [ ] **Step 3: Wire CI and commit**

In `.github/workflows/ci.yml`'s browser job, after "Check works across the JavaScript-to-Python boundary" and
before the lesson-trial block (which rebuilds `site/`), add:

```yaml
      - name: The lessons work on a phone, at the root
        working-directory: tests
        run: node steps_browser_test.mjs
      - name: The lessons work under /<repo>/
        working-directory: tests
        env:
          BASE: /${{ github.event.repository.name }}/
        run: node steps_browser_test.mjs
```

Run `python3 tests/workflow_test.py` and `actionlint`. Commit: `test: the lessons in a real browser, on a phone
and under the Pages path`.

---

### Task 9: The private feedback page

**Files:** none in the repository. The page source lives at
`~/python_foundations-notes/feedback-page/index.html` (private, outside the repo), and is published as a
private claude.ai artifact.

**Interfaces:** Writes to the artifact's own database. Collection `lessons`: `{lesson, pace, explain, reads,
help, muddiest, submittedAt, version: 1}`. Collection `units`: `{unit, pace, hardest, hardest_why, next,
submittedAt, version: 1}`. Nothing is read back by the page beyond showing "sent".

- [ ] **Step 1: Load the skills the page needs**

Before writing anything:
- call the Artifact tool with `action: "quickstart"` and `intent: "other"`;
- load `artifact-capabilities`;
- read `db.d.ts` and `claude.d.ts` for the current contract.

Read the check-in survey page (its URL is in the worksheet and in private memory; `action: "read"`) and copy
four of its working patterns:
- the draft kept in `localStorage`;
- the "Copy my answers" fallback when saving is unavailable;
- the plain wording for a 13-year-old;
- the `db` setup that worked for the learner, including whichever sharing level and capabilities it used, so
  the learner can submit exactly as they did there.

- [ ] **Step 2: Write the page**

One page, two modes, chosen by a picker at the top:

The picker offers `Lesson 0`, `Lesson 2.1`, `Lesson 2.2`, `Lesson 2.3`, `Lesson 2.4`, and
`Unit 2 check-in`.

After a lesson, everything is a tap except the muddiest point:

| Question | Answers |
|---|---|
| How was the pace? | way too slow, a bit slow, about right, a bit fast, way too fast |
| Could you explain this lesson to a friend? | yes, mostly, not really |
| How many times did you read it? | once, twice, three or more |
| Did you need help? | no, a little, a lot |
| What is still the least clear? | free text, with "nothing" as a one-tap answer |

The help question is worded as the survey worded its help question. It is optional; flag it to Justin as the
one assumption here.

The unit check-in:

| Question | Answers |
|---|---|
| How was the pace across the unit? | the same five-step scale |
| Which lesson was hardest? | lesson picker |
| Why? | free text |
| Do you want to start unit 3? | yes, maybe, I'd rather stop (the survey's wording) |

The page states, in one line, that only the parent who shared it sees the answers, naming them as the survey
did. It collects no name.

- [ ] **Step 3: Publish privately and verify the round trip**

Publish with the capabilities Step 1 established. Then:
1. Ask Justin to open it and submit one lesson answer marked as a test (for example a muddiest point of
   "test"). That runs the real entry point, a person tapping in the page.
2. Read it back with `ArtifactData` `query` on `lessons`.
3. With Justin's OK, delete that one test row.

Give Justin the link to share with the learner the same way he shared the survey. Record the URL, and the
collection names, in the worksheet and in the private learner memory. Neither is in the repository.

---

### Task 10: The whole suite, then hand over

- [ ] **Step 1: Run everything**

```bash
for py in python3 /usr/bin/python3; do
  for t in practice_test second_volume_test leak_scan_test pre_push_test scan_history_test personal_sweep_test \
           workflow_test disclaimer_test commit_msg_test site_guard_test quiz_test lesson_format_test trace_test \
           lesson_vocabulary_test steps_volume_test; do
    $py tests/$t.py > /dev/null 2>&1 && echo "ok    $py $t" || echo "FAIL  $py $t"
  done
done
python3 build.py --check | tail -1
cd tests && for t in verify2 validate_shipped validate_stdin validate_projects; do node $t.mjs > /dev/null 2>&1 && echo "ok $t" || echo "FAIL $t"; done
for t in browser_test browser_check_test steps_browser_test lesson_browser_test; do REQUIRE_BROWSER=1 node $t.mjs | tail -1; done
cd .. && python3 tests/shelf_test.py | tail -1
docker run --rm -v "$PWD":/repo:ro -w /repo pf-review-gnu sh -c 'for t in steps_volume_test lesson_vocabulary_test quiz_test; do python3 tests/$t.py >/dev/null 2>&1 && echo "ok GNU $t" || echo "FAIL GNU $t"; done'
```

Expected:
- 30 `ok` lines for Python;
- the build reports 0 mismatched;
- four node `ok` lines;
- four browser pass lines;
- the shelf pass line;
- three GNU `ok` lines.

- [ ] **Step 2: Read every lesson as the learner will**

Serve the site and read each lesson page top to bottom at phone width. Do every exercise, using a wrong answer
first and then the right one. Ledger anything that reads as more than one new idea at once, or any exercise
whose wording admits an answer its check refuses.

- [ ] **Step 3: Hand over**

Update the worksheet:
- STATUS and NEXT;
- a checkpoint saying the prototype is ready for the learner, with the success bar and the stop rule from the
  spec.

Then ask Justin before pushing. Pushing main publishes `vol1-steps` on the public site, marked "in progress",
and the learner reads the lessons there.
