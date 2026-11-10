# Extra-practice pages for the step-by-step course — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give each of the twelve units in `vol1-steps` one optional extra-practice page, offered from the unit's
last lesson, and never needed to continue (spec: "Each unit has one optional extra-practice page, labeled
optional, never needed to continue").

**Architecture:** Two parts.
- **Part A (Task 1):** machinery. The build already supports practice pages, but only for chapter volumes:
  - it pairs `practice/<stem>.md` with the page whose slug is `<stem>`;
  - `practice_test.py` derives its vocabulary from chapter files.

  A lesson volume has no page named `ch05`. Task 1 pairs `practice/chNN.md` with unit NN's last lesson, labels
  the link optional, and holds the pages to the lesson volume's own gates:
  - the vocabulary gate;
  - a practice-page contract in `steps_volume_test.py`;
  - the browser walk.
- **Part B (Tasks 2 to 5):** the twelve pages, three units per task, in course order.

**Tech Stack:** as the course: Markdown pages, `_checks.json`, `_solutions.md`, `_alternates.json`; Python 3.9+
standard-library tests; Node + playwright-core browser tests.

**Spec:** `docs/specs/step-by-step-course.md` (the lesson format, and "Each unit has one optional extra-practice
page"). Read it with:
- `docs/lesson-format.md`;
- the full-course plan, `docs/superpowers/plans/2026-11-09-step-by-step-full-course.md`, whose "What the
  prototype taught" section binds here too.

## Global Constraints

- **Optional, and never needed to continue:**
  - a practice page teaches nothing new: no example fences, only steps;
  - nothing in a lesson, quiz or hint points to it as something to do first;
  - its only way in is the link at the foot of its unit's last lesson;
  - its only way out is back to that lesson.
- **Vocabulary:** a unit's practice page may use what every lesson up to and including that unit's last lesson
  shows, and nothing a later unit shows. This is the lesson vocabulary rule, applied as if the page came right
  after the unit's last lesson.
- **Every step is a program:**
  - each step has a check of kind `output`, `stdin` or `function`, and a worked solution;
  - checks test behavior, never form;
  - no check passes a step's starting code;
  - every `function` check has an awkward case: `0`, `""`, `[]`, `{}` or a negative number.
- **The last step is like a try-it:** it builds the whole project. Its hints walk the routine for that unit (the
  same steps as the unit's last lesson), and the first hint links `99-how-to-start-a-problem.html`. Its worked
  solution keeps its Say it and Split it comments, and it has an alternate in `_alternates.json`.
- **Size:** 3 to 10 steps, at most 1,300 words of prose.
- **Projects are built step by step**, each step one step beyond the last, never handed over solved.
- Never name the first learner or quote their answers in the repository.
- Python 3.9 floor; no new dependencies; both Pythons for every Python test.
- Commit messages: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, no `Claude-Session`. Never
  `--no-verify`.
- American spellings (`grey` excepted), closed em dashes in prose. Site strings in `build.py` keep the
  codebase's spaced ` — `, matching their neighbors.
- **Pushing:** see "Approval asked for". The standing yes for the full-course plan does not cover this plan.

## Review Focus

1. **"Optional" read as "behind".** A learner who sees a link at the foot of a lesson may think she has to do it
   before moving on. The link must say it is optional and that nothing later needs it. Pinned in Task 1:
   - `lesson_practice_test.py` asserts the link's words;
   - `steps_browser_test.mjs` asserts every practice page is offered, as optional, from a lesson.
2. **A practice page using a later unit's vocabulary.** For example, the old chapter 6 page returns a tuple, which
   arrives in unit 10, and the old chapter 4 page uses `.isdigit()`, which arrives in 8.6. Pinned in Task 1:
   `with_practice()` places each page after its unit, and a planted page using a later unit's method is caught,
   with the lesson that first shows it named.
3. **A practice page that quietly teaches.** An example fence on the page would make its vocabulary "shown", and
   a later lesson could lean on it without the gate noticing. Pinned in Task 1: the contract refuses any fence
   above the steps, and the section rule refuses one before the first step.
4. **The walk skipping practice pages in silence.** `steps_answers.py` reads only lesson files today, so a practice
   page's checks would never be clicked through in the browser. Pinned in Task 1: the walk's list includes every
   practice page's checked steps, and `unit_of()` assigns a practice page its unit.
5. **A misnamed practice file** (`ch5.md`, `ch05a.md`, `ch13.md`): it must stop the build with a message naming
   the file, never build a page linked from nowhere. Pinned in Task 1: `practice_owner()` returns `None` for each,
   and the build exits on `None`.

Long project programs on a phone are covered without new work. `steps_browser_test.mjs` already walks every built
page at 390 px, and a practice page is a built page.

---

## Part A

### Task 1: Practice pages in a lesson volume

**Files:**
- Modify: `build.py`:
  - `practice_files` docstring;
  - the practice loop in `build_volume`;
  - the foot-of-page link.
- Modify: `tests/steps_volume_test.py`:
  - extract `dropped_blocks()`, `exercise_problems()` and `routine_problems()` from `lesson_problems()`;
  - add `practice_problems()`;
  - call it from `main()`.
- Modify: `tests/lesson_vocabulary_test.py`: add `with_practice()`, and gate practice pages in `main()`.
- Modify: `tests/practice_test.py`: say out loud that a lesson volume's pages are checked elsewhere, and skip them.
- Modify: `tests/steps_answers.py`: add `unit_of()`, and include practice pages.
- Modify: `tests/steps_browser_test.mjs`: every practice page is offered, as optional.
- Create: `tests/lesson_practice_test.py`: planted cases for all of the above.
- Modify: `.github/workflows/*.yml`: run `tests/lesson_practice_test.py` beside `steps_volume_test.py`.
- Modify: `docs/lesson-format.md`: a section "Extra-practice pages".

**Interfaces:**
- Produces, in `build.py`:
  - `practice_owner(vol: dict, stem: str, pages: list[dict]) -> dict | None`;
  - `practice_link(vol: dict, practice: dict) -> str`.
- Produces, in `tests/steps_volume_test.py`:
  - `dropped_blocks(slug, blocks) -> list[str]`;
  - `exercise_problems(key, spec, solution, alternate, code) -> list[str]`;
  - `routine_problems(key, hints, hint_steps, solution, spec, has_alternate) -> list[str]`;
  - `practice_problems(stem, text, hint_steps, checks, solutions, alternates) -> list[str]`;
  - `PRACTICE_KINDS = ("output", "stdin", "function")`.
- Produces, in `tests/lesson_vocabulary_test.py`: `with_practice(pages, practice) -> (list, list)`, returning the
  pages in order and the stems that name no unit.
- Produces, in `tests/steps_answers.py`: `unit_of(slug, text) -> int | None`.
- The practice page's slug is `chNN-practice`, its keys are `chNN-practice#<n>`, and its file is
  `volumes/vol1-steps/practice/chNN.md`. Tasks 2 to 5 rely on these names.

- [ ] **Step 1: Write the failing test file `tests/lesson_practice_test.py`**

```python
"""The extra-practice pages of a lesson volume keep the spec's promise.

    python3 tests/lesson_practice_test.py

"Each unit has one optional extra-practice page, labeled optional, never
needed to continue." A lesson volume has no page named after a unit, so the
build pairs practice/chNN.md with unit NN's last lesson, the one that carries
the unit's quiz. These are planted cases for each piece: the pairing, the
link's words, the page contract, where the vocabulary gate places a page, and
which unit the browser walk files it under. The real pages are checked by
steps_volume_test.py, lesson_vocabulary_test.py and steps_walk.mjs.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
import build                                                    # noqa: E402
from lesson_vocabulary_test import violations, with_practice    # noqa: E402
from steps_answers import unit_of                               # noqa: E402
from steps_volume_test import practice_problems                 # noqa: E402

LESSON_VOL = {"slug": "v", "lessons": True}
CHAPTER_VOL = {"slug": "v"}
UNIT5 = [{"slug": "ch05a-while"}, {"slug": "ch05b-for"}, {"slug": "ch06a-defining"}]
ROUTINE = ("Say it", "Split it", "Name it")

GOOD = """## Extra practice: a countdown

Optional: more practice on this unit, if you want it.

### Steps

1. Print `3`.
2. Print `3`, `2` and `1`, one per line.

```python
print(3)
```

3. Print every number from 5 down to 1, then `Go!`.

> Say it: count down, then go. See [How to start a problem](99-how-to-start-a-problem.html).
> Split it: start at 5; print and step down while above 0; print Go!.
> Name it: `count`.
"""
CHECKS = {"ch05-practice#1": {"kind": "output", "expected": "3"},
          "ch05-practice#2": {"kind": "output", "expected": "3\n2\n1"},
          "ch05-practice#3": {"kind": "output", "expected": "5\n4\n3\n2\n1\nGo!"}}
SOLUTIONS = {"ch05-practice#1": {"code": "print(3)"},
             "ch05-practice#2": {"code": "print(3)\nprint(2)\nprint(1)"},
             "ch05-practice#3": {"code": "# Say it: count down, then go.\n# Split it: start, loop, go.\n"
                                         "count = 5\nwhile count > 0:\n    print(count)\n"
                                         "    count = count - 1\nprint('Go!')"}}
ALTERNATES = {"ch05-practice#3": "for n in [5, 4, 3, 2, 1]:\n    print(n)\nprint('Go!')"}


def main():
    results = []

    def expect(label, ok, detail=""):
        results.append((label, ok, detail))

    owner = build.practice_owner(LESSON_VOL, "ch05", UNIT5)
    expect("practice/ch05.md belongs to unit 5's last lesson",
           owner is not None and owner["slug"] == "ch05b-for", str(owner))
    for stem in ("ch5", "ch05a", "ch07", "ch05-while"):
        expect(f"practice/{stem}.md names no unit, so it has no owner",
               build.practice_owner(LESSON_VOL, stem, UNIT5) is None)
    chapters = [{"slug": "ch04-making-decisions"}]
    expect("a chapter volume still pairs by the chapter's own name",
           build.practice_owner(CHAPTER_VOL, "ch04-making-decisions", chapters) is chapters[0])

    page = {"slug": "ch05-practice", "title": "Extra practice: a countdown"}
    link = build.practice_link(LESSON_VOL, page)
    expect("the link says the page is optional and that nothing later needs it",
           'href="ch05-practice.html"' in link and "optional" in link.lower()
           and "Nothing later needs it" in link, link)
    old = build.practice_link(CHAPTER_VOL, page)
    expect("a chapter volume's link keeps its wording",
           "one project, built step by step" in old, old)

    good = practice_problems("ch05", GOOD, ROUTINE, CHECKS, SOLUTIONS, ALTERNATES)
    expect("a page that keeps every promise passes", not good, "; ".join(good))

    def refused(label, text, needle, checks=CHECKS, alternates=ALTERNATES):
        found = practice_problems("ch05", text, ROUTINE, checks, SOLUTIONS, alternates)
        expect(label, any(needle in p for p in found), "; ".join(found) or "nothing refused")

    refused("a page that does not say it is optional is refused",
            GOOD.replace("Optional: more", "More"), "optional")
    refused("an example fence above the steps is refused (the page would teach)",
            GOOD.replace("### Steps", "```python\nprint(1)\n```\n\n### Steps"), "teaches nothing new")
    refused("a second section is refused", GOOD.replace("3. Print every", "### Try It\n\n1. Print every"),
            "one section")
    refused("a heading that does not say extra practice is refused",
            GOOD.replace("## Extra practice: a countdown", "## A countdown"), "Extra practice")
    refused("a step checked by a choice is refused: every step is a program",
            GOOD, "a program check",
            checks={**CHECKS, "ch05-practice#1": {"kind": "choice", "options": ["a", "b"], "answer": 1}})
    refused("a last step whose hints skip Split it is refused",
            GOOD.replace("> Split it: start at 5; print and step down while above 0; print Go!.\n", ""),
            "walk Say it, Split it, Name it")
    refused("a last step without an alternate is refused", GOOD, "alternate", alternates={})
    refused("a check that passes the starting code is refused", GOOD, "starting code",
            checks={**CHECKS, "ch05-practice#2": {"kind": "output", "expected": "3"}})

    lessons = [("ch02a-one", "## L\n\n```python\nprint(1)\n```\n"),
               ("ch03a-two", "## L\n\n```python\nname = 'ada'\nprint(name.upper())\n```\n")]
    early = "## Extra practice: x\n\nOptional.\n\n### Steps\n\n1. Shout it.\n\n```python\nprint('a'.upper())\n```\n"
    placed, unplaced = with_practice(lessons, [("ch02", early), ("ch09", early)])
    expect("a practice page sits right after its unit's last lesson",
           [slug for slug, _ in placed] == ["ch02a-one", "ch02-practice", "ch03a-two"],
           str([slug for slug, _ in placed]))
    expect("a practice page whose unit has no lessons is reported, not dropped", unplaced == ["ch09"])
    caught = violations(placed, {})
    expect("unit 2's practice may not use what unit 3 first shows, and the message says where it is shown",
           any("ch02-practice" in v and "first shown by ch03a-two" in v for v in caught), str(caught))
    later, _ = with_practice(lessons, [("ch03", early)])
    expect("unit 3's practice may use what unit 3 shows", not violations(later, {}), str(violations(later, {})))

    expect("a lesson's unit comes from its part line",
           unit_of("ch05a-while", "<!-- part: Unit 5 — Repetition -->\n## L") == 5)
    expect("a practice page's unit comes from its name", unit_of("ch05-practice", "## Extra practice: x") == 5)
    expect("the reference page has no unit", unit_of("99-how-to-start-a-problem", "## How") is None)

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + detail + ')'}")
    print(f"\n{'the practice pages keep the spec' + chr(39) + 's promise' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it to see it fail**

Run: `python3 tests/lesson_practice_test.py`

Expected: an `ImportError` on `with_practice` (or the first missing name). That is the red: none of the
interfaces exist yet.

- [ ] **Step 3: Add `practice_owner` and `practice_link` to `build.py`, and use them**

Put these after `practice_files`. Also extend that function's docstring with one sentence: "In a lesson volume the
file is named after the unit (practice/ch05.md), and belongs to the unit's last lesson."

```python
def practice_owner(vol, stem, pages):
    """The page a practice file belongs to, or None.

    In a chapter volume, the chapter it is named after. In a lesson volume no
    page is named after a unit, so practice/ch05.md belongs to unit 5's last
    lesson: the one that carries the unit's quiz, where the reader finishes
    the unit. A name that is not exactly chNN has no owner, so a typo stops
    the build instead of publishing a page that nothing links to.
    """
    if not vol.get("lessons"):
        return next((p for p in pages if p["slug"] == stem), None)
    if not re.fullmatch(r"ch\d\d", stem):
        return None
    unit = [p for p in pages if re.match(rf"{stem}[a-z]-", p["slug"])]
    return unit[-1] if unit else None


def practice_link(vol, practice):
    """The line at the foot of a page that offers its practice page.

    A lesson volume says the page is optional, and that nothing after it
    needs it: a learner who sees a link at the end of a lesson otherwise
    reads it as one more thing she has to do before going on.
    """
    title = html.escape(practice["title"])
    if vol.get("lessons"):
        return (f'<p class="practice"><a href="{practice["slug"]}.html">{title}</a>'
                f' — optional, for when you want more practice on this unit. '
                f'Nothing later needs it.</p>')
    return (f'<p class="practice"><a href="{practice["slug"]}.html">{title}</a>'
            f' — one project, built step by step, using only what you have met so far</p>')
```

In `build_volume`'s practice loop, replace the owner lookup and the `sys.exit` message, and set the part line:

```python
        owner = practice_owner(vol, path.stem, pages)
        if owner is None:
            named = ("no unit with lessons in content/ (lesson volumes name a practice "
                     "file after its unit: practice/ch05.md)" if vol.get("lessons")
                     else "no chapter of that name in content/")
            sys.exit(f"{vol['slug']}/practice/{path.name} has {named}")
```

and `"part": owner["part"] if vol.get("lessons") else owner["title"],`. A lesson page's part is its unit line,
which is what a practice page belongs to.

In the foot-of-page block, replace the inline `extras.append(f'<p class="practice">…')` with
`extras.append(practice_link(vol, practice))`.

- [ ] **Step 4: Refactor `tests/steps_volume_test.py`, then add `practice_problems`**

Move three pieces of `lesson_problems` into functions, unchanged in behavior:
- **`dropped_blocks(slug, blocks)`:** the section-whitelist loop, from `shown_in_section = ...` through its
  `say(...)`. It returns the list of messages instead of calling `say`.
- **`exercise_problems(key, spec, solution, alternate, code)`:**
  - the "untouched" check;
  - the awkward-case check;
  - the worked-solution and alternate loop.

  It does not include "neither a check nor a worked solution", which stays in `lesson_problems`.
- **`routine_problems(key, hints, hint_steps, solution, spec, has_alternate)`:** the body of
  `if section == "Try It":`.

`lesson_problems` then reads:

```python
    problems += dropped_blocks(slug, blocks)
    ...
    for number, section, item, code, hints in found:
        key = f"{slug}#{number}"
        spec, solution = checks.get(key), solutions.get(key)
        if not spec and not solution:
            say(f"{key}: has neither a check nor a worked solution")
        problems += exercise_problems(key, spec, solution, alternates.get(key), code)
        if section == "Try It":
            problems += routine_problems(key, hints, hint_steps, solution, spec, key in alternates)
```

Run `python3 tests/steps_volume_test.py` now, before going on. It must still say `the lessons keep their
promises`, because the refactor changes no behavior.

Then add:

```python
# A practice step is a program to write, so it is checked by running it.
PRACTICE_KINDS = ("output", "stdin", "function")
MIN_STEPS, MAX_STEPS = 3, 10


def practice_problems(stem, text, hint_steps, checks, solutions, alternates):
    """What an extra-practice page promises (spec: "one optional
    extra-practice page, labeled optional, never needed to continue").

    Optional: its introduction says so. Never needed: it teaches nothing, so
    no later lesson can come to depend on it -- its only fences are its
    steps' starting code, and the vocabulary gate places it after its unit.
    One project in steps: every step is a program, checked by running it and
    solved, and the last step builds the whole thing the way a try it does.
    """
    slug = f"{stem}-practice"
    problems = []
    say = problems.append
    blocks = blocks_of(text)
    heading = next((p for k, p in blocks if k == "h2"), "")
    if not heading.startswith("Extra practice: "):
        say(f"{slug}: the heading must start 'Extra practice: ' (found {heading!r})")
    h3 = [p for k, p in blocks if k == "h3"]
    if h3 != ["Steps"]:
        say(f"{slug}: one section, 'Steps'; found {h3}")
    top = next((i for i, (k, _) in enumerate(blocks) if k == "h3"), len(blocks))
    if "optional" not in " ".join(p for k, p in blocks[:top] if k == "p").lower():
        say(f"{slug}: the introduction must say the page is optional")
    if any(k == "code" for k, _ in blocks[:top]):
        say(f"{slug}: a code fence above the steps is an example, and a practice page teaches nothing new")
    problems += dropped_blocks(slug, blocks)

    found = exercises(blocks)
    if not MIN_STEPS <= len(found) <= MAX_STEPS:
        say(f"{slug}: {len(found)} steps; a practice page has {MIN_STEPS} to {MAX_STEPS}")
    if prose_words(blocks) > MAX_WORDS:
        say(f"{slug}: {prose_words(blocks)} words of prose; at most {MAX_WORDS}")
    for number, _, _, code, hints in found:
        key = f"{slug}#{number}"
        spec, solution = checks.get(key), solutions.get(key)
        if not spec or spec["kind"] not in PRACTICE_KINDS:
            say(f"{key}: every step needs a program check ({', '.join(PRACTICE_KINDS)})")
        if not solution:
            say(f"{key}: every step needs a worked solution")
        problems += exercise_problems(key, spec, solution, alternates.get(key), code)
        if number == len(found):
            problems += routine_problems(key, hints, hint_steps, solution, spec, key in alternates)
    return problems
```

In `main()`, after the `LESSONS` loop, add the practice pages. A page's hint steps are its unit's last lesson's.
Every file must name a unit that has lessons; that every unit has a page is added in Task 5.

```python
    steps_of = {}
    for slug, _, steps in LESSONS:
        steps_of[slug[:4]] = steps          # the last lesson of each unit wins
    for path in build.practice_files(vol):
        if only and f"{path.stem}-practice" not in only:
            continue
        if path.stem not in steps_of:
            problems.append(f"practice/{path.name}: names no unit (practice files are chNN.md)")
            continue
        problems += practice_problems(path.stem, path.read_text(), steps_of[path.stem],
                                      checks, solutions, alternates)
```

- [ ] **Step 5: Add `with_practice` to `tests/lesson_vocabulary_test.py`, and gate the real pages**

```python
def with_practice(pages, practice):
    """`pages` in reading order, with each practice page placed right after
    its unit's last lesson. A unit's extra practice may use everything the
    unit shows and nothing a later one does; placing it is how the gate,
    which reads in order, knows that. Returns (pages, stems naming no unit),
    so a page with nowhere to go is reported rather than quietly skipped."""
    out, unplaced = list(pages), []
    for stem, text in practice:
        at = [i for i, (slug, _) in enumerate(out) if re.match(rf"{stem}[a-z]-", slug)]
        if not at:
            unplaced.append(stem)
            continue
        out.insert(at[-1] + 1, (f"{stem}-practice", text))
    return out, unplaced
```

In `main()`'s lesson-volume branch, replace `pages = [...]` with:

```python
        pages, unplaced = with_practice([(p.stem, p.read_text()) for p in files],
                                        [(p.stem, p.read_text()) for p in build.practice_files(vol)])
        expect(f"{vol['slug']}: every practice page names a unit with lessons", not unplaced, str(unplaced))
```

- [ ] **Step 6: `tests/practice_test.py` hands lesson volumes over, out loud**

In `main()`'s volume loop, right after `if not pages: continue`:

```python
        if vol.get("lessons"):
            # Its vocabulary is derived from chapter files (ch05-...), which a
            # lesson volume has none of. The lesson volume's own gates check
            # these pages instead: lesson_vocabulary_test.py and
            # steps_volume_test.py.
            print(f"{vol['slug']}: {len(pages)} practice page(s), checked by "
                  f"lesson_vocabulary_test.py and steps_volume_test.py")
            continue
```

- [ ] **Step 7: `tests/steps_answers.py` walks practice pages too**

```python
def unit_of(slug, text):
    """The unit a page belongs to: a lesson's part line, or a practice page's
    name (ch05-practice). None for a page outside any unit."""
    match = UNIT.match(text)
    if match:
        return int(match.group(1))
    practice = re.fullmatch(r"ch(\d\d)-practice", slug)
    return int(practice.group(1)) if practice else None
```

In `answers()`, after `pages = ...`, add
`pages.update({f"{p.stem}-practice": p.read_text() for p in build.practice_files(vol)})`. Then replace the
two-line unit filter (`match = ...` and `if unit and ...`) with:

```python
        if unit and unit_of(slug, text) != int(unit):
            continue
```

- [ ] **Step 8: `tests/steps_browser_test.mjs`: every practice page is offered, as optional**

Before the loop, add `const offered = new Set();`. Inside the loop, after the links check:

```js
    for (const p of await page.$$eval("p.practice", (ps) => ps.map((p) => ({
      href: p.querySelector("a")?.getAttribute("href") || "", text: p.textContent })))) {
      if (/optional/i.test(p.text) && /Nothing later needs it/.test(p.text)) offered.add(p.href.replace(/\.html$/, ""));
    }
```

After the loop:

```js
  for (const slug of PAGES.filter((s) => s.endsWith("-practice"))) {
    expect(`${slug} is offered from its unit, labeled optional`, offered.has(slug));
  }
```

Update the file's header comment: "Practice pages are built pages too, so they are walked here, and each must be
offered from a lesson, labeled optional."

- [ ] **Step 9: CI and the authoring reference**

Add `python3 tests/lesson_practice_test.py` to the workflow's Python test list, right after
`python3 tests/steps_volume_test.py`. Run `python3 tests/workflow_test.py`, in case it pins that list.

Add a section to `docs/lesson-format.md`, after "Unit quizzes":

````markdown
## Extra-practice pages

One optional page per unit, in `practice/chNN.md` (the unit's number, no letter). The build publishes it as
`chNN-practice.html`, offers it at the foot of the unit's last lesson as optional, and links it back there; it is
not in the reading order or the contents. Its keys are `chNN-practice#<n>`.

```markdown
## Extra practice: a secret code

Optional: one more project for this unit, if you want it. Nothing later needs it.

### Steps

1. Shift one letter...
```

`steps_volume_test.py` holds it to:
- one `### Steps` section, and no fence above it: the page teaches nothing new;
- an introduction that says it is optional;
- 3 to 10 steps, each with a check of kind `output`, `stdin` or `function`, and a worked solution;
- a last step that builds the whole project like a try it: hints that walk the routine, and an alternate.

`lesson_vocabulary_test.py` reads the page as if it came right after its unit's last lesson.
````

Also replace "(`Steps` is the practice pages' name for the same thing)" in "Exercise sections" with "(`Steps` is
the extra-practice pages' section; see below)".

- [ ] **Step 10: Run everything**

Under both Pythons (`python3` and `/usr/bin/python3`):
- `python3 tests/lesson_practice_test.py`: every line `ok`;
- `python3 tests/steps_volume_test.py`;
- `python3 tests/lesson_vocabulary_test.py`;
- `python3 tests/practice_test.py`: the old volume's twelve pages still checked, unchanged output;
- `python3 build.py --check`;
- the rest of the suite as CI runs it.

Then the browser tests:
- `node tests/steps_browser_test.mjs`, at the root and with `BASE=/python-foundations/`;
- `node tests/steps_walk.mjs`: still 669 exercises, since no practice pages exist yet.

- [ ] **Step 11: Prove the pairing end to end with a throwaway page, then remove it**

The planted tests cover the functions. This step covers the round trip: file, build, link, page, walk.
1. Write a three-step `volumes/vol1-steps/practice/ch01.md`, with its checks, solutions and alternate.
2. Run `python3 build.py`, then confirm:
   - `site/vol1-steps/ch01c-errors-and-a-receipt.html` carries the optional link;
   - `site/vol1-steps/ch01-practice.html` links back;
   - the shelf's contents list does not include it;
   - `node tests/steps_walk.mjs 01` walks its three steps;
   - `node tests/steps_browser_test.mjs` passes.
3. Remove the throwaway page and its entries, rebuild, and confirm the walk is back to 669. Do not commit the
   throwaway page.

- [ ] **Step 12: Commit**

```bash
git add build.py tests/lesson_practice_test.py tests/steps_volume_test.py tests/lesson_vocabulary_test.py \
        tests/practice_test.py tests/steps_answers.py tests/steps_browser_test.mjs .github/workflows \
        docs/lesson-format.md
git commit -m "course: extra-practice pages for a lesson volume, one per unit, offered as optional

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

## Part B: the pages

### The procedure every page follows

For unit N's page, `volumes/vol1-steps/practice/chNN.md`:

1. **Read first:**
   - the unit's lessons in `vol1-steps`, all of them: the page may use only what they and earlier units show;
   - the old practice page `volumes/vol1-foundations/practice/chNN-*.md` and its checks and solutions, where the
     page adapts one;
   - `unit-common.md` in the full-course plan's workspace (`.superpowers/sdd/2026-11-09-step-by-step-full-course/`).
2. **Write the page:**
   - an introduction that names the project, says it is optional, and says what the reader will have at the end;
   - its steps, each one step beyond the last, ending in the whole project;
   - each step's check in `content/_checks.json`, its worked solution in `content/_solutions.md`, and the last
     step's alternate in `content/_alternates.json`.

   When a step prints a decision's message, refuse the print-every-branch answer with `absent`.
3. **Gates, before the page's commit, all green:**
   - `python3 tests/steps_volume_test.py --only chNN-practice` under both Pythons;
   - `python3 tests/lesson_vocabulary_test.py`;
   - `python3 build.py --check`;
   - `node tests/steps_walk.mjs NN`.
4. **One commit per page:** `course: unit N's extra practice, <the project>`.
5. **Task review**, after the task's three pages, by two fresh Sonnet reviewers in parallel. They are the same
   two as the full-course units:
   - **learner-eyes:** a step more than one step from the last, a check refusing a correct answer or taking a
     wrong one, anything that reads as required or as a threat;
   - **checks against wording:** every check against its step's words, with plausible beginner answers run
     through `run_check`.

   Fix Critical and Important findings test-first; ledger Minor ones.
6. **Verify the task end to end:**
   - the whole suite;
   - `node tests/steps_walk.mjs` (all units);
   - `node tests/steps_browser_test.mjs` at the root and under `BASE`.

The tables below give each page's project and what it must cover. Step wording is written during execution,
against the contract.

### Task 2: Units 1 to 3

| Page | Project | Source | Must cover |
|---|---|---|---|
| `ch01.md` | a film club flyer | old ch01 practice (7 steps) | printing lines and blank lines, a number worked out by arithmetic, a comment at the top. Unit 1 has no input, so the checks are `output` |
| `ch02.md` | a hiking trip planner | old ch02 practice (7 steps) | names for values, `input()` and converting it, a value worked out from two inputs; `stdin` checks with an awkward run |
| `ch03.md` | a pizza party splitter | old ch03 practice (8 steps), plus the parked tax-percentage step | `//` and `%` for slices left over; `round()` and `:.2f` for money; the tax step as one step beyond the bill step, never as a jump |

### Task 3: Units 4 to 6

| Page | Project | Source | Must cover |
|---|---|---|---|
| `ch04.md` | a launch console | old ch04 practice (8 steps) | `if`/`elif`/`else`, `and`, bands in the right order, a verdict, and a HOLD line. The old fuel step's `.isdigit()` arrives in 8.6, so replace that step with what unit 4 shows (4.4's input checks); `absent` on every verdict |
| `ch05.md` | a savings goal tracker | old ch05 practice (8 steps) | a `for` over weeks, a running total, a `while` until a goal, a stop value; awkward runs (goal already met, a first 0) |
| `ch06.md` | a unit converter toolkit | old ch06 practice (8 steps) | one function per conversion, returned and rounded, then a program that calls them. The old step 6 returns a tuple, which arrives in 10.1: replace it, for example with two functions (`hours_in`, `minutes_left`). `function` checks with a 0 or negative case |

### Task 4: Units 7 to 9

| Page | Project | Source | Must cover |
|---|---|---|---|
| `ch07.md` | a playlist manager | old ch07 practice (8 steps) | add, insert, remove, slice, sort and search a list; `function` checks with an `[]` case. Each function must not change the list it is given, unless its step says it does |
| `ch08.md` | a secret code (Caesar shift) | parked from Task 8 (ruling: "Caesar moves to the optional extra practice") | the alphabet as a string, `.find()`, `% 26` to wrap, leaving non-letters alone (`find` gives `-1`), decoding with a negative shift (the awkward case), and capitals via `.lower()` or a second alphabet. No `ord`/`chr`, which the course never shows. The old log-line parser stays in the retired volume |
| `ch09.md` | a lost property register | old ch09 practice (8 steps) | a dictionary of items, adding and looking up with a missing-key guard, counting by kind, a set of places; `function` checks with a `{}` case |

### Task 5: Units 10 to 12, and the whole set

| Page | Project | Source | Must cover |
|---|---|---|---|
| `ch10.md` | a bus timetable | old ch10 practice (8 steps) | tuples as records, unpacking, a list of records sorted by a key, grouping by route. A tuple a function returns is checked with an `output` check and pinned calling code, because a `function` check cannot compare a tuple with JSON |
| `ch11.md` | a race leaderboard | old ch11 practice (8 steps), plus the parked "two closest values" (Task 11 ruling) | search and sort by time, ties, then the two closest finishing times. `abs()` is never taught, so sort first and subtract neighbors |
| `ch12.md` | the Tower of Hanoi | parked from Task 12 (ruling: "Tower of Hanoi to the optional extra practice; digit_sum not placed") | first `digit_sum(n)` by recursion (base case `0`, the awkward case), then Hanoi's moves printed for 1, 2 and 3 discs, then a function counting the moves for n discs (`0` discs is `0` moves). The old folder-tree page stays in the retired volume |

**Then, for the whole set:**
- Add to `steps_volume_test.py`'s `main()`, under `if not only:`, the rule that every unit has its page:

  ```python
        units = sorted({slug[:4] for slug, *_ in LESSONS})
        stems = [p.stem for p in build.practice_files(vol)]
        if stems != units:
            problems.append(f"practice/: one page per unit, {units}; found {stems}")
  ```
- Delete one page locally to watch the rule fail, then restore it.
- A final whole-branch review on the most capable model.
- A learner-eyes reading of all twelve pages in one pass, for drift between them.

### Task 6: Hand over

- Full suite, and the browser walk of every unit, which now counts more than 669.
- Worksheet checkpoint and ledger line.
- **Report to Justin:**
  - the twelve projects;
  - every old step that was replaced, and why;
  - deferred minors.
- Ask before pushing, unless a standing yes was given below.

---

## Approval asked for

Approving this plan approves Task 1's machinery and the twelve pages as tabled, including:
- the Caesar shift in place of the log-line parser;
- the Tower of Hanoi in place of the folder tree.

Two things it does not approve without your word:

1. **Pushing.** Choose one:
   - a standing yes per task: push each task (Task 1, then each three-unit batch) when its review is clean and
     its suite is green, with a note each time;
   - or one push at the end, after Task 6.
2. **How it runs:**
   - subagent-driven, as the full course: a fresh implementer per task, on the most capable model for the page
     tasks (writing steps is judgment) and a standard model for Task 1, then two Sonnet reviewers per task;
   - or native, in this session, with one final review.
