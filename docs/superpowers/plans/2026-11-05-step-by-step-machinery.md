# Step-by-step course: the machinery — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the build everything the step-by-step lessons need (several exercise sections per page, hints revealed one at a time, multiple-choice and trace-table checks, unit quizzes, and a vocabulary gate for lessons) without changing a byte of what `vol1-foundations` renders.

**Architecture:** The build already renders exercise sections, attaches checks from `_checks.json` by `"<volume>/<page>#<n>"`, and supports several volumes. This plan widens the exercise renderer (`build.py`), adds two check kinds (`choice` in the page, `trace` in `web/box_runner.py`), teaches `web/app.js` to drive them and reveal hints, makes `scripts/make_quizzes.py` volume-explicit with unit titles, and adds a lesson vocabulary gate built on `tests/practice_test.py`'s `harvest()`. Every feature is proven on throwaway volumes; the real `volumes/vol1-steps/` is created by the content plan that follows this one.

**Tech Stack:** Python 3.9+ standard library only (build, tests, box_runner under CPython and Pyodide), vanilla JavaScript in `web/app.js`, Node + playwright-core for browser tests (existing harness in `tests/browser_harness.mjs`).

**Spec:** `docs/specs/step-by-step-course.md` (approved 2026-11-05).

## Global Constraints

- Python 3.9 floor for every script and test; run every Python test under both `python3` (3.14) and `/usr/bin/python3` (3.9.6).
- No new dependencies.
- `vol1-foundations` must render byte-identically: `python3 build.py --check` stays `110 checked, 0 mismatched`, and every existing test stays green.
- A check must never fail a correct answer written in a different style; checks test what a program does, not how it is written.
- No syntax, built-in function or method used before a lesson has taught it (enforced in Task 7).
- Test first: every behavior below gets a test that fails before the code exists.
- Commit messages carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and no `Claude-Session` line (the commit-msg hook refuses one). Never `--no-verify`.
- American spellings (`grey` excepted), closed em dashes in new prose.
- Pushing to the public repository needs Justin's yes. Nothing here creates `volumes/vol1-steps/`.

## Review Focus

1. **A page whose exercise sections are unusual** (only a warm-up, or several sections with a prose paragraph between them) must number exercises continuously and never crash. Pinned in Task 1.
2. **Hints with no worked solution behind them** must reveal every hint and then stop cleanly, not throw. Pinned in Task 2.
3. **Multiple-choice options containing code with `<`, `>` or `&`** must render escaped and still be checkable. Pinned in Task 3.
4. **A trace-table answer written in a different but correct style** (`'Ada'`, `"Ada"` or `Ada`; `3` for `3.0`; blank or `-` for "not set yet") must pass; a wrong cell must be named by line and variable. Pinned in Task 4.
5. **Two real volumes:** every tool that used to assume a single volume (`make_quizzes.py`, `quiz_test.py`, and any script calling `find_volume()` with no name) must keep working when a second content volume exists. Pinned in Task 5.

---

### Task 1: Lessons in order, and exercise numbers that run through a page

**Files:**
- Modify: `build.py` (`page_order`, `render`, `render_exercises`)
- Create: `tests/lesson_format_test.py`
- Modify: `.github/workflows/ci.yml` (run the new test in the build job)

**Interfaces:**
- Produces: `build.EXERCISE_SECTIONS = ("Warm-up", "Practice", "Try It", "Steps")`; `build.render_exercises(slug, blocks, start=1) -> (html: str, count: int)`; `build.page_order(path)` returns a tuple ending in `path.stem`, so lessons of one unit (`ch02a-…`, `ch02b-…`) sort by filename.

- [ ] **Step 1: Write the failing test**

Create `tests/lesson_format_test.py`:

```python
"""Check the lesson format the step-by-step volume relies on.

    python3 tests/lesson_format_test.py

A lesson has several exercise sections (a warm-up, a practice after each new
idea, a "try it"), so its exercises must be numbered straight through the
page: a check is found by "<volume>/<page>#<n>", and two sections that both
start at 1 would give two exercises the same key. Lessons of one unit share a
chapter number (ch02a, ch02b, ...), so they must sort by filename too.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build                                                    # noqa: E402

LESSON = """## Lesson 2.1 — Naming a value

### Warm-up

1. Predict what this prints.

```python
print(2 + 3)
```

### A name for a value

Some prose between sections.

```python
price = 12
print(price)
```

### Practice

1. Print `price` doubled.
2. Store your age in `age` and print it.

### Try It

1. Make `total` hold two prices added together, then print it.
"""


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    page = build.render(build.split_blocks(LESSON.split("\n")), "trial/ch02a-naming")
    numbered = re.findall(r'<div class="box exercise[^"]*" data-box="trial/ch02a-naming#(\d+)"', page)
    expect("exercises are numbered straight through the page", numbered, ["1", "2", "3", "4"])

    only_warmup = build.render(build.split_blocks(
        "## L\n\n### Warm-up\n\n1. One.\n".split("\n")), "trial/ch02b-x")
    expect("a page with only a warm-up renders its one exercise",
           re.findall(r'data-box="trial/ch02b-x#(\d+)"', only_warmup), ["1"])

    names = [Path(n) for n in ("ch02c-c.md", "ch02a-a.md", "99-appendix.md", "ch02b-b.md",
                               "00-front-matter.md", "ch01-one.md")]
    expect("lessons of one unit sort by filename",
           [p.stem for p in sorted(names, key=build.page_order)],
           ["00-front-matter", "ch01-one", "ch02a-a", "ch02b-b", "ch02c-c", "99-appendix"])

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'the lesson format holds' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/lesson_format_test.py`
Expected: FAIL on "exercises are numbered straight through the page" (today `Warm-up` and `Practice` are not exercise sections, and each `Try It` restarts at 1) and on "lessons of one unit sort by filename" (today `page_order` ignores the stem, so ties keep glob order).

- [ ] **Step 3: Implement**

In `build.py`, replace `page_order`:

```python
def page_order(path):
    """Front matter, then the chapters in order, then the appendices.

    Sorting the filenames puts 99-appendices second, because "9" sorts before
    "c" — which read as a missing chapter rather than an ordering accident.
    The stem breaks ties, so the lessons of one unit (ch02a, ch02b, ...) keep
    their order whatever order the filesystem lists them in.
    """
    if path.stem.startswith("00"):
        return (0, 0, path.stem)
    if path.stem.startswith("99"):
        return (2, 0, path.stem)
    return (1, int(path.stem[2:4]), path.stem)
```

Add, above `render`:

```python
# Headings whose list items are exercises, each with its own box and check.
# A chapter has one ("Try It", or "Steps" on a practice page); a lesson has
# several, and its exercises are numbered straight through the page.
EXERCISE_SECTIONS = ("Warm-up", "Practice", "Try It", "Steps")
```

In `render`, add `exercise = 0` beside `box = 0`, and replace the `if kind == "h3" and payload in ("Try It", "Steps"):` branch with:

```python
        if kind == "h3" and payload in EXERCISE_SECTIONS:
            parts.append(f"<h3>{inline(payload)}</h3>")
            j = i + 1
            while j < len(blocks) and blocks[j][0] != "h3":
                j += 1
            rendered, count = render_exercises(slug, blocks[i + 1:j], exercise + 1)
            parts.append(rendered)
            exercise += count
            # Exercise fences still consume a box number, so that "<slug>#<n>"
            # means the same fence here as it does in verify() and the bundle.
            box += sum(1 for kind, _ in blocks[i + 1:j] if kind == "code")
            i = j
            continue
```

Replace `render_exercises`:

```python
def render_exercises(slug, blocks, start=1):
    """Render one exercise section. Returns (html, how many exercises).

    Exercises are numbered across the whole page, not per list or per section,
    because a check is found by "<page>#<n>": a lesson's warm-up, practice and
    try it are one sequence. `start` is the number of this section's first one.
    """
    exercises = []
    for kind, payload in blocks:
        if kind in ("ol", "ul"):
            for item in payload:
                exercises.append({"text": item, "code": ""})
        elif kind == "code" and exercises:
            exercises[-1]["code"] = payload      # a fence belongs to the item above it

    out = [exercise_html(slug, number, exercise)
           for number, exercise in enumerate(exercises, start)]
    return "\n".join(out), len(exercises)
```

Then search the file for any other caller of `render_exercises` (`grep -n "render_exercises" build.py`); if one exists, give it the tuple's first element.

- [ ] **Step 4: Run it and watch it pass, with nothing else moving**

Run:
```bash
python3 tests/lesson_format_test.py && /usr/bin/python3 tests/lesson_format_test.py
python3 build.py --check | tail -1
for t in practice_test second_volume_test site_guard_test quiz_test; do python3 tests/$t.py > /dev/null && echo "ok $t" || echo "FAIL $t"; done
git status --short site/ | wc -l
```
Expected: the pass line twice; `110 checked, 0 mismatched`; four `ok`; and `0` (site/ is ignored; the point is that `git diff --stat` shows only `build.py` and the new test).

To prove `vol1-foundations` renders identically, before Step 3 copy the built site: `cp -R site/vol1-foundations /tmp/claude-scratch-before` (use the session scratchpad), and after Step 4 run `diff -r <that copy> site/vol1-foundations` and expect no output.

- [ ] **Step 5: Wire into CI and commit**

In `.github/workflows/ci.yml`, in the build job's "Practice pages, volumes, the site guard and the disclaimer" step, add a line `python3 tests/lesson_format_test.py` after `python3 tests/quiz_test.py`. Run `python3 tests/workflow_test.py` and `actionlint .github/workflows/ci.yml`.

```bash
git add build.py tests/lesson_format_test.py .github/workflows/ci.yml
git commit -F - <<'MSG'
build: a lesson's exercises are numbered straight through the page

A step-by-step lesson has a warm-up, a practice after each idea and a try it,
each a list of checked exercises. "Warm-up" and "Practice" are now exercise
sections beside "Try It" and "Steps", and numbering runs through the page so
"<page>#<n>" stays unique. Lessons of one unit share a chapter number, so
page_order breaks ties on the filename. vol1-foundations renders unchanged:
every page has exactly one exercise section.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 2: Hints revealed one at a time, then the worked solution

**Files:**
- Modify: `build.py` (`render_exercises`, `exercise_html`)
- Modify: `web/app.js` (a hints handler), `web/app.css` (hint styles)
- Modify: `tests/lesson_format_test.py`

**Interfaces:**
- Consumes: `build.render_exercises(slug, blocks, start)` from Task 1.
- Produces: in the lesson markdown, each `> ` line directly after an exercise item (or after its code fence) is one hint, in order. Rendered as `<div class="hints">` holding `<p class="hint" hidden>` per hint and `<button class="hint-next">`; when hints exist, the worked solution's `<details class="solution">` carries `hidden` until the last hint is shown.

- [ ] **Step 1: Write the failing test**

Append to `main()` in `tests/lesson_format_test.py`, before the results loop:

```python
    hinted = """## L

### Try It

1. Add two prices and print the total.

> Say it: two prices go in, their sum comes out.
> Split it: store each price, add them, print the result.
> Name it: `first_price`, `second_price`, `total`.

2. No hints on this one.
"""
    build.SOLUTIONS["trial/ch02c-hints#1"] = {"code": "total = 3 + 4\nprint(total)", "note": ""}
    html_text = build.render(build.split_blocks(hinted.split("\n")), "trial/ch02c-hints")
    first, second = html_text.split('data-box="trial/ch02c-hints#2"')
    expect("each > line after an exercise is a hidden hint", first.count('<p class="hint" hidden>'), 3)
    expect("hints keep their order", first.index("Say it") < first.index("Split it") < first.index("Name it"), True)
    expect("a hinted exercise has a reveal button", 'class="hint-next"' in first, True)
    expect("its worked solution waits behind the hints", '<details class="solution" hidden>' in first, True)
    expect("an exercise with no hints gets no hint block", 'class="hints"' in second, False)

    no_solution = build.render(build.split_blocks(
        "## L\n\n### Practice\n\n1. Try.\n\n> Say it: a hint.\n".split("\n")), "trial/ch02d-x")
    expect("hints without a worked solution still render", no_solution.count('class="hint"'), 1)
```

(`>` lines on consecutive lines are separate `quote` blocks in `split_blocks`, one per line; that is what makes one line one hint.)

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/lesson_format_test.py`
Expected: FAIL on the hint lines (quotes inside an exercise section are dropped today).

- [ ] **Step 3: Implement the rendering**

In `render_exercises`, add a branch to the loop:

```python
        elif kind == "quote" and exercises:
            exercises[-1].setdefault("hints", []).append(payload)
```

In `exercise_html`, just before `solution = SOLUTIONS.get(key)`, add:

```python
    hints = exercise.get("hints", [])
    if hints:
        body.append('<div class="hints">'
                    + "".join(f'<p class="hint" hidden>{inline(h)}</p>' for h in hints)
                    + f'<button class="hint-next" type="button">Show a hint (1 of {len(hints)})</button>'
                    + '</div>')
```

and change the solution's opening tag so it hides while hints remain:

```python
        hidden = " hidden" if hints else ""
        body.append(f'<details class="solution"{hidden}><summary>Show a solution</summary>'
                    f'<pre>{html.escape(solution["code"])}</pre>{note}</details>')
```

- [ ] **Step 4: Implement the reveal in `web/app.js`**

Append after the `.box` loop (before the scratchpad section):

```javascript
/* ------------------------------------------------------------------ hints */

/* Hints come one at a time, so a stuck learner gets the next step of the
 * thinking rather than the answer. The worked solution, if there is one,
 * appears only after the last hint. */
document.querySelectorAll(".hints").forEach((hints) => {
  const items = [...hints.querySelectorAll(".hint")];
  const button = hints.querySelector(".hint-next");
  const solution = hints.parentElement.querySelector(".solution");
  let shown = 0;
  button.addEventListener("click", () => {
    if (shown === items.length) {          // every hint is out: this click is for the solution
      solution.hidden = false;
      button.hidden = true;
      return;
    }
    items[shown].hidden = false;
    shown += 1;
    if (shown < items.length) {
      button.textContent = `Show another hint (${shown + 1} of ${items.length})`;
    } else if (solution) {
      button.textContent = "Show the worked solution";
    } else {
      button.hidden = true;                // no solution behind the hints: nothing more to show
    }
  });
});
```

Add to `web/app.css` (beside the existing `.solution` rules; use the file's existing tokens):

```css
.hints { display: grid; gap: .5rem; margin: .75rem 0; }
.hint { margin: 0; padding: .5rem .75rem; border-left: 3px solid var(--accent); background: var(--surface); }
.hint-next { justify-self: start; }
```

If `--accent` or `--surface` do not exist in `web/app.css`, use the tokens its `.solution` and `.cases` rules use (read them first) instead; ledger the substitution.

- [ ] **Step 5: Run the tests and commit**

```bash
python3 tests/lesson_format_test.py && /usr/bin/python3 tests/lesson_format_test.py
python3 build.py --check | tail -1
(cd tests && REQUIRE_BROWSER=1 node browser_test.mjs | tail -1)
git add build.py web/app.js web/app.css tests/lesson_format_test.py
git commit -F - <<'MSG'
feat: hints revealed one at a time, then the worked solution

A "> " line directly after an exercise is one hint. They render hidden and
come out one per click, so a stuck learner gets the next step of the
thinking (say it, split it, name it) before any answer; the worked solution
appears only after the last. The JavaScript is proven in a real browser in
the trial-lesson test (Task 6).

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

Expected: the pass lines; `110 checked, 0 mismatched`; the browser pass line.

---

### Task 3: The multiple-choice check

**Files:**
- Modify: `build.py` (`exercise_html`, and a spec validator)
- Modify: `web/app.js` (choice boxes), `web/app.css`
- Modify: `tests/lesson_format_test.py`

**Interfaces:**
- Produces: a `_checks.json` entry `{"kind": "choice", "options": ["...", "..."], "answer": <int index>, "why": "<shown when right>"}`. Rendered as `<div class="box exercise choice" data-box=… data-check=…>` with a `<fieldset class="options">` of radio inputs named after the key, an optional read-only `<pre class="given">` for the exercise's code fence, a Check button, no Run or Reset, no code textarea. `build.validate_check(key, spec)` exits the build with a message for a malformed `choice` or `trace` spec.

- [ ] **Step 1: Write the failing test**

Append to `main()` in `tests/lesson_format_test.py`:

```python
    build.CHECKS["trial/ch02e-choice#1"] = {
        "kind": "choice", "options": ["`x = 3600`", "`seconds_per_hour = 3600`", "`a < b & c`"],
        "answer": 1, "why": "The name says what the number means."}
    choice = build.render(build.split_blocks(
        "## L\n\n### Practice\n\n1. Which name explains itself?\n".split("\n")), "trial/ch02e-choice")
    expect("a choice exercise renders one radio per option", choice.count('type="radio"'), 3)
    expect("a choice exercise has no code textarea", '<textarea' in choice, False)
    expect("a choice exercise has no Run button", 'class="run"' in choice, False)
    expect("code in an option is escaped", "a &lt; b &amp; c" in choice, True)

    for label, bad_spec in (("an answer outside the options", {"kind": "choice", "options": ["a", "b"], "answer": 2}),
                            ("only one option", {"kind": "choice", "options": ["a"], "answer": 0})):
        try:
            build.validate_check("trial/x#1", bad_spec)
            expect(f"the build refuses {label}", "accepted", "refused")
        except SystemExit:
            expect(f"the build refuses {label}", "refused", "refused")
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/lesson_format_test.py`
Expected: FAIL on the four choice lines, and an `AttributeError` for `validate_check` (record it; the refusal lines count as failing).

- [ ] **Step 3: Implement**

In `build.py`, above `exercise_html`, add:

```python
def validate_check(key, spec):
    """Refuse a check that cannot work, at build time rather than in front of a
    learner. Only the kinds added for lessons are validated here; the original
    four are covered by validate_shipped.mjs and practice_test.py."""
    kind = spec.get("kind")
    if kind == "choice":
        options = spec.get("options") or []
        if len(options) < 2:
            sys.exit(f"{key}: a choice check needs at least two options")
        if not isinstance(spec.get("answer"), int) or not 0 <= spec["answer"] < len(options):
            sys.exit(f"{key}: a choice check's answer must be the index of one option")
    if kind == "trace" and not spec.get("names"):
        sys.exit(f"{key}: a trace check needs the names of the variables to trace")
```

At the top of `exercise_html`, after `check = CHECKS.get(...)` and `key = ...`, add:

```python
    if check:
        validate_check(key, check)
    if check and check["kind"] == "choice":
        return choice_html(key, number, exercise, check)
```

and add the renderer:

```python
def choice_html(key, number, exercise, check):
    """A multiple-choice exercise: radio buttons and Check, no code to run."""
    body = [f'<p class="prompt"><span class="num">{number}</span>{inline(exercise["text"])}</p>']
    if exercise["code"]:
        body.append(f'<pre class="given">{html.escape(exercise["code"])}</pre>')
    name = html.escape(key, quote=True)
    options = "".join(
        f'<label><input type="radio" name="{name}" value="{i}"> <span>{inline(text)}</span></label>'
        for i, text in enumerate(check["options"]))
    body.append(f'<fieldset class="options"><legend class="sr-only">Choose one</legend>{options}</fieldset>')
    body.append('<div class="bar"><button class="check">Check</button><span class="status"></span></div>'
                '<pre class="result" hidden></pre>')
    return (f'<div class="box exercise choice" data-box="{name}" '
            f'data-check="{html.escape(json.dumps(check), quote=True)}">' + "".join(body) + "</div>")
```

In `web/app.js`, change the generic loop's selector from `".box"` to `".box:not(.choice):not(.trace)"`, and append before the hints section:

```javascript
/* ----------------------------------------------------------------- choices */

/* A multiple-choice exercise is checked in the page: there is no program to
 * run, only which option was picked. A wrong pick is not told the answer. */
document.querySelectorAll(".box.choice").forEach((box) => {
  const spec = JSON.parse(box.dataset.check);
  const button = box.querySelector(".check");
  const result = box.querySelector(".result");
  button.addEventListener("click", () => {
    const picked = box.querySelector("input:checked");
    result.hidden = false;
    if (!picked) {
      result.className = "result failed";
      result.textContent = "Pick one first.";
    } else if (Number(picked.value) === spec.answer) {
      result.className = "result passed";
      result.textContent = spec.why ? `Correct. ${spec.why}` : "Correct.";
    } else {
      result.className = "result failed";
      result.textContent = "Not that one. Have another look.";
    }
  });
});
```

In `web/app.css` add:

```css
.options { border: 0; padding: 0; margin: .5rem 0; display: grid; gap: .4rem; }
.options label { display: flex; gap: .5rem; align-items: baseline; cursor: pointer; }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
pre.given { margin: .5rem 0; }
```

- [ ] **Step 4: Run the tests**

Run: `python3 tests/lesson_format_test.py && /usr/bin/python3 tests/lesson_format_test.py && python3 build.py --check | tail -1`
Expected: the pass lines, then `110 checked, 0 mismatched`.

- [ ] **Step 5: Commit**

```bash
git add build.py web/app.js web/app.css tests/lesson_format_test.py
git commit -F - <<'MSG'
feat: a multiple-choice check, for naming and concept questions

"Which name explains itself?" has no program to run, so a choice exercise is
radio buttons and Check, decided in the page. A wrong pick is not told the
answer. The build refuses a choice check with fewer than two options or an
answer that is not one of them, before a learner can meet it.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 4: The trace-table check

**Files:**
- Modify: `web/box_runner.py` (`trace_rows`, `check_trace`)
- Modify: `build.py` (`trace_html`)
- Modify: `web/app.js` (trace boxes; expose `check_trace` to the page)
- Create: `tests/trace_test.py`
- Modify: `tests/lesson_format_test.py`, `.github/workflows/ci.yml`

**Interfaces:**
- Produces: `box_runner.trace_rows(source, names) -> list[tuple[int, list[str]]]`, one row per executed line: `(line number, [repr of each name after that line, or "" if not yet set])`. `box_runner.check_trace(source, payload) -> (bool, list[str])`, where `payload` is the JSON text `{"names": [...], "entered": [[cell, ...], ...]}`. A `_checks.json` entry `{"kind": "trace", "names": ["price", "count"]}` on an exercise whose code fence is the program to trace.

- [ ] **Step 1: Write the failing test**

Create `tests/trace_test.py`:

```python
"""Check the trace-table check: the expected table comes from running the code.

    python3 tests/trace_test.py

A trace table asks for each variable's value after each line. The expected
values are never typed in by hand: box_runner works them out by running the
program, so the table cannot disagree with Python. And the learner's answer
is compared by value, not by spelling: 'Ada', "Ada" and Ada are the same
string, 3 is 3.0, and a blank or "-" means "not set yet".
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "web"))
import box_runner                                               # noqa: E402

PROGRAM = "price = 12\ncount = 3\nprice = price + count\nname = 'Ada'\n"
NAMES = ["price", "count", "name"]


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    rows = box_runner.trace_rows(PROGRAM, NAMES)
    expect("one row per executed line", [line for line, _ in rows], [1, 2, 3, 4])
    expect("values after each line", [cells for _, cells in rows],
           [["12", "", ""], ["12", "3", ""], ["15", "3", ""], ["15", "3", "'Ada'"]])

    def check(entered):
        return box_runner.check_trace(PROGRAM, json.dumps({"names": NAMES, "entered": entered}))

    right = [["12", "", ""], ["12", "3", "-"], ["15", "3", ""], ["15.0", "3", "Ada"]]
    expect("a correct table in a different style passes", check(right)[0], True)
    expect("double quotes are as good as single", check(
        [["12", "", ""], ["12", "3", ""], ["15", "3", ""], ["15", "3", '"Ada"']])[0], True)

    wrong = [["12", "", ""], ["12", "3", ""], ["12", "3", ""], ["15", "3", "Ada"]]
    ok, notes = check(wrong)
    expect("a wrong cell fails", ok, False)
    expect("and is named by line and variable", "line 3" in notes[0] and "price" in notes[0], True)
    expect("a missing row fails, not crashes", check(right[:2])[0], False)

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'trace tables check by value' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/trace_test.py`
Expected: `AttributeError: module 'box_runner' has no attribute 'trace_rows'`.

- [ ] **Step 3: Implement in `web/box_runner.py`**

Add after `check_prediction`:

```python
def trace_rows(source, names, max_steps=200):
    """Run `source` and record, after every executed line, the repr of each
    name in `names` ("" for a name not yet set). Output is swallowed.

    The expected answer to a trace table, worked out by Python itself so it can
    never disagree with what the program does.
    """
    import contextlib
    import io

    code = compile(source, "<trace>", "exec")
    namespace = {}
    steps = []

    def snapshot():
        return [repr(namespace[n]) if n in namespace else "" for n in names]

    def local(frame, event, arg):
        if frame.f_code is code and event == "line":
            if len(steps) >= max_steps:
                raise RuntimeError(f"traced more than {max_steps} lines")
            steps.append((frame.f_lineno, snapshot()))
        return local

    def start(frame, event, arg):
        return local if frame.f_code is code else None

    with contextlib.redirect_stdout(io.StringIO()):
        sys.settrace(start)
        try:
            exec(code, namespace)
        finally:
            sys.settrace(None)
    return [(line, steps[i + 1][1] if i + 1 < len(steps) else snapshot())
            for i, (line, _) in enumerate(steps)]


def _same_value(entered, expected):
    """Does what the learner wrote mean the value Python holds? By value, not
    spelling: quotes optional around text, 3 for 3.0, "-" or blank for unset."""
    import ast

    entered = entered.strip()
    if expected == "":
        return entered in ("", "-")
    value = ast.literal_eval(expected)
    try:
        return ast.literal_eval(entered) == value
    except (ValueError, SyntaxError):
        return isinstance(value, str) and entered == value


def check_trace(source, payload):
    """Check a trace table. `payload` is JSON text: {"names", "entered"}."""
    import json

    data = json.loads(payload)
    names, entered = data["names"], data["entered"]
    try:
        rows = trace_rows(source, names)
    except BaseException as e:
        return False, [f"the program itself failed: {e}"]
    if len(entered) != len(rows):
        return False, [f"the table has {len(rows)} rows; {len(entered)} were filled in"]
    for (line, want), got in zip(rows, entered):
        for name, w, g in zip(names, want, got):
            if not _same_value(g, w):
                shown = w if w else "not set yet"
                return False, [f"line {line}, {name}: you wrote {g.strip() or 'nothing'!r}, it is {shown}"]
    return True, []
```

`sys` is already imported at the top of `box_runner.py`; check, and add `import sys` there if not.

- [ ] **Step 4: Run it and watch it pass**

Run: `python3 tests/trace_test.py && /usr/bin/python3 tests/trace_test.py`
Expected: `trace tables check by value`, twice.

- [ ] **Step 5: Render the table, failing test first**

Append to `main()` in `tests/lesson_format_test.py`:

```python
    build.CHECKS["trial/ch02f-trace#1"] = {"kind": "trace", "names": ["price", "count"]}
    traced = build.render(build.split_blocks(
        "## L\n\n### Practice\n\n1. Fill in the table.\n\n```python\nprice = 12\ncount = 3\n```\n".split("\n")),
        "trial/ch02f-trace")
    expect("a trace exercise renders a row per executed line", traced.count('<tr class="step"'), 2)
    expect("and a cell per name per row", traced.count('<input class="cell"'), 4)
    expect("a trace exercise carries its program for the check", 'data-code=' in traced, True)
```

Run `python3 tests/lesson_format_test.py`; expect the three trace lines to FAIL. Then in `build.py`, near the top imports, make box_runner importable:

```python
sys.path.insert(0, str(Path(__file__).resolve().parent / "web"))
import box_runner                                               # noqa: E402
```

In `exercise_html`, after the choice return, add `if check and check["kind"] == "trace": return trace_html(key, number, exercise, check)`, and add:

```python
def trace_html(key, number, exercise, check):
    """A trace table: the program, read-only, and a row of cells per executed line."""
    code = exercise["code"]
    if not code:
        sys.exit(f"{key}: a trace exercise needs a code fence to trace")
    rows = box_runner.trace_rows(code, check["names"])
    lines = code.split("\n")
    head = "".join(f"<th>{html.escape(n)}</th>" for n in check["names"])
    body_rows = "".join(
        f'<tr class="step"><td><code>{line}: {html.escape(lines[line - 1].strip())}</code></td>'
        + "".join(f'<td><input class="cell" aria-label="{html.escape(n, quote=True)} after line {line}" '
                  f'spellcheck="false"></td>' for n in check["names"])
        + "</tr>"
        for line, _ in rows)
    name = html.escape(key, quote=True)
    return (f'<div class="box exercise trace" data-box="{name}" '
            f'data-check="{html.escape(json.dumps(check), quote=True)}" '
            f'data-code="{html.escape(code, quote=True)}">'
            f'<p class="prompt"><span class="num">{number}</span>{inline(exercise["text"])}</p>'
            f'<pre class="given">{html.escape(code)}</pre>'
            f'<div class="trace-wrap"><table class="trace-table"><thead><tr><th>After line</th>{head}</tr></thead>'
            f'<tbody>{body_rows}</tbody></table></div>'
            '<div class="bar"><button class="check">Check</button><span class="status"></span></div>'
            '<pre class="result" hidden></pre></div>')
```

- [ ] **Step 6: Drive it from the page**

In `web/app.js`, add `"check_trace"` to the list of names exported from the harness (the array at the line beginning `for (const name of [` that lists `"check_prediction", "check_stdin", "repl_run"`), then append before the hints section:

```javascript
/* ------------------------------------------------------------ trace tables */

/* A trace table is checked by Python: box_runner runs the program, works out
 * each variable after each line, and compares by value, not spelling. */
document.querySelectorAll(".box.trace").forEach((box) => {
  const spec = JSON.parse(box.dataset.check);
  const button = box.querySelector(".check");
  const status = box.querySelector(".status");
  const result = box.querySelector(".result");
  button.addEventListener("click", async () => {
    button.disabled = true;
    status.textContent = pyodide ? "checking…" : "starting Python…";
    await boot();
    const entered = [...box.querySelectorAll("tr.step")].map((row) =>
      [...row.querySelectorAll("input.cell")].map((cell) => cell.value));
    const outcome = python.check_trace(box.dataset.code,
      JSON.stringify({ names: spec.names, entered }));
    const passed = outcome.get(0);
    const notes = outcome.get(1).toJs();
    outcome.destroy();
    result.hidden = false;
    result.className = passed ? "result passed" : "result failed";
    result.textContent = passed ? "Correct, every value." : notes.join("\n");
    status.textContent = "";
    button.disabled = false;
  });
});
```

In `web/app.css` add:

```css
.trace-wrap { overflow-x: auto; }
.trace-table { border-collapse: collapse; margin: .5rem 0; }
.trace-table th, .trace-table td { padding: .3rem .5rem; border: 1px solid var(--line, #ccc); text-align: left; }
.trace-table input.cell { width: 6rem; font: inherit; }
```

(Use the file's existing border token in place of `--line` if it has one.)

- [ ] **Step 7: Run everything touched, wire CI, commit**

```bash
python3 tests/trace_test.py && /usr/bin/python3 tests/trace_test.py
python3 tests/lesson_format_test.py && /usr/bin/python3 tests/lesson_format_test.py
python3 build.py --check | tail -1
(cd tests && npm ci --no-audit --no-fund > /dev/null && node validate_shipped.mjs | tail -1 && node verify2.mjs | tail -1)
```

Expected: the pass lines; `110 checked, 0 mismatched`; the two node lines unchanged from before this task. Add `python3 tests/trace_test.py` to the CI build step after the line Task 1 added; run `python3 tests/workflow_test.py` and `actionlint`.

```bash
git add web/box_runner.py build.py web/app.js web/app.css tests/trace_test.py tests/lesson_format_test.py .github/workflows/ci.yml
git commit -F - <<'MSG'
feat: a trace-table check, worked out by running the program

Tracing by hand (each variable's value after each line) is a skill the course
needed and never taught. A trace exercise shows its program and a row of cells
per executed line; box_runner works out the expected values by running the
program under a line tracer, so the table cannot disagree with Python, and
compares by value: 'Ada', "Ada" and Ada are one string, 3 is 3.0, "-" is
"not set yet". A wrong cell is named by line and variable.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 5: Quizzes for units, and tools that no longer assume one volume

**Files:**
- Modify: `scripts/make_quizzes.py`, `tests/quiz_test.py`, `build.py` (the quiz link label)
- Modify: any script found in Step 1 that calls `find_volume()` with no name in a path CI runs

**Interfaces:**
- Produces: `make_quizzes.outputs(data, vol) -> {Path: text}`; `make_quizzes.SOURCE_NAME = "quizzes.json"`; a quiz's heading reads `Unit N - Title` when its page carries `<!-- part: Unit N — Title -->`, and `Chapter N - Title` as today otherwise. The page's quiz link reads `Unit N quiz` for a unit page.

- [ ] **Step 1: Find every single-volume assumption**

Run: `grep -n "find_volume(" scripts/*.py tests/*.py build.py`
Record each caller that passes no name. `make_quizzes.py` is one; list the others in the ledger. Each must either take a volume explicitly or loop over `build.VOLS`.

- [ ] **Step 2: Write the failing test**

In `tests/quiz_test.py`, replace the module-level `sys.argv = sys.argv[:1]` / `import make_quizzes` pair and the start of `main()` so that the test loops over every volume with a `quizzes.json`, and add a two-volume trial:

```python
import shutil                                                    # add to the imports

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
import build                                                     # noqa: E402
import make_quizzes                                              # noqa: E402

UNIT_PAGE = "<!-- part: Unit 2 — Variables -->\n## Lesson 2.4 — Putting it together\n\nText.\n"
UNIT_QUIZ = {"quizzes": [{"slug": "ch02d-together", "questions": [
    {"section": "Vocabulary", "text": "A name for a value is a ____.", "answers": ["variable"]}]}]}
```

and in `main()`:

```python
    total = 0
    for vol in build.VOLS:
        source = vol["dir"] / make_quizzes.SOURCE_NAME
        if not source.exists():
            continue
        data = json.loads(source.read_text())
        files = make_quizzes.outputs(data, vol)
        total += len(files)
        stale = [p.relative_to(ROOT).as_posix() for p, text in files.items()
                 if not p.exists() or p.read_text() != text]
        expect(f"{vol['slug']}: all {len(files)} quizzes and keys are what quizzes.json renders",
               not stale, f"differ: {stale}")
        # ... the existing width and compile checks, unchanged, run on `data` and `files`
    expect("vol1-foundations still has its 24 quiz files", total >= 24, f"{total}")

    trial = {"slug": "_trial-units", "dir": ROOT / "volumes" / "_trial-units",
             "content": ROOT / "volumes" / "_trial-units" / "content",
             "quizzes": ROOT / "volumes" / "_trial-units" / "quizzes"}
    try:
        trial["content"].mkdir(parents=True)
        (trial["content"] / "ch02d-together.md").write_text(UNIT_PAGE)
        unit_files = make_quizzes.outputs(UNIT_QUIZ, trial)
        heading = next(t for p, t in unit_files.items() if p.name.endswith("-quiz.txt")).split("\n")[1]
        expect("a unit's quiz is headed with the unit", heading, "Unit 2 - Variables")
    finally:
        shutil.rmtree(trial["dir"], ignore_errors=True)
```

Move the existing width and compile-checks loops inside the per-volume loop, unchanged, operating on that volume's `data` and `files`.

- [ ] **Step 3: Run it and watch it fail**

Run: `python3 tests/quiz_test.py`
Expected: FAIL (`outputs()` takes one argument; `SOURCE_NAME` does not exist; there is no unit heading).

- [ ] **Step 4: Implement**

In `scripts/make_quizzes.py`:

- Replace the module-level `VOLUME = find_volume(...)`, `QUIZZES = ...`, `SOURCE = ...` and `KEYS = ...` lines with `SOURCE_NAME = "quizzes.json"`, keeping the `KEYS` comment above a function.
- Give `render` a `label="Chapter"` keyword and use it: `plain(f"{label} {number} - {title}")`.
- Replace `outputs` and `main`:

```python
def titles_of(vol):
    """{page slug: (label, number, title)} for every page a quiz can belong to.

    A chapter names itself in its "## Chapter N — Title" heading. A lesson
    belongs to a unit, named in its "<!-- part: Unit N — Title -->" line; a
    unit's quiz hangs off its last lesson and is headed with the unit.
    """
    found = {}
    for md in vol["content"].glob("*.md"):
        text = md.read_text()
        unit = re.match(r"<!-- part: (Unit) (\d+) — (.+?) -->", text)
        head = re.search(r"^## (Chapter) (\d+) — (.+)$", text, re.M)
        match = unit or head
        if match:
            found[md.stem] = (match.group(1), int(match.group(2)), match.group(3))
    return found


def outputs(data, vol):
    """{path: text} for every quiz and answer key the data describes."""
    quizzes = data["quizzes"] if isinstance(data, dict) else data
    titles = titles_of(vol)
    files = {}
    for quiz in sorted(quizzes, key=lambda q: q["slug"]):
        label, number, title = titles[quiz["slug"]]
        stem = quiz["slug"]
        files[vol["quizzes"] / f"{stem}-quiz.txt"] = render(quiz, title, number, label=label)
        files[vol["dir"] / "answer-keys" / f"{stem}-answers.txt"] = render(
            quiz, title, number, answers=True, label=label)
    return files


def main():
    vol = find_volume(sys.argv[1] if len(sys.argv) > 1 else None)
    data = json.loads((vol["dir"] / SOURCE_NAME).read_text())
    vol["quizzes"].mkdir(exist_ok=True)
    (vol["dir"] / "answer-keys").mkdir(exist_ok=True)
    for path, text in outputs(data, vol).items():
        path.write_text(text)
    for quiz in sorted(data["quizzes"], key=lambda q: q["slug"]):
        blanks = sum(q["text"].count("____") + q.get("code", "").count("____")
                     for q in quiz["questions"])
        print(f"  {quiz['slug']:<38}{len(quiz['questions']):>3} questions, {blanks:>3} blanks")
```

Update the module docstring's usage line to `python3 scripts/make_quizzes.py [volume-slug]   # required once there are two volumes`.

In `build.py` `build_volume`, replace the quiz link's label expression with:

```python
                unit = re.match(r"(Unit \d+)", page["part"] or "")
                label = (f"{unit.group(1)} quiz" if unit else
                         f'Chapter {page["title"].split()[1].rstrip("—").strip()} quiz')
                extras.append(
                    f'<p class="quiz"><a href="quizzes/{quiz.name}">{label}</a>'
                    f' — fill it in, then show or print it</p>')
```

Fix each other caller recorded in Step 1 the same way: take the volume as an argument, or loop over `build.VOLS`.

- [ ] **Step 5: Run it and watch it pass, with vol1 unchanged**

```bash
python3 tests/quiz_test.py && /usr/bin/python3 tests/quiz_test.py
python3 scripts/make_quizzes.py vol1-foundations > /dev/null && git status --short volumes/
python3 build.py --check | tail -1
python3 tests/second_volume_test.py | tail -1
```

Expected: the pass lines; no output from `git status` (regenerating vol1 changes nothing); `110 checked, 0 mismatched`; the second-volume pass line.

- [ ] **Step 6: Commit**

```bash
git add scripts/make_quizzes.py tests/quiz_test.py build.py
git commit -F - <<'MSG'
build: quizzes for units, and a quiz tool that names its volume

The step-by-step course ends each unit with a quiz. make_quizzes.py now
renders one volume at a time, given by name, and heads a quiz "Unit N -
Title" when its page belongs to a unit; the page's link reads "Unit N
quiz". quiz_test.py checks every volume that has a quizzes.json. A second
content volume used to stop both: find_volume() with no name exits when
there are two. vol1-foundations' 24 files regenerate byte for byte.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 6: The whole lesson format, end to end, in a real browser

**Files:**
- Create: `tests/lesson_trial.py`, `tests/lesson_browser_test.mjs`
- Modify: `.github/workflows/ci.yml` (browser job)

**Interfaces:**
- Consumes: everything from Tasks 1 to 5.
- Produces: `python3 tests/lesson_trial.py up` writes `volumes/_trial-lessons/` (one lesson with a warm-up predict, a choice, a trace, and a hinted try-it with a worked solution) and builds the site; `python3 tests/lesson_trial.py down` removes it and rebuilds. `tests/lesson_browser_test.mjs` runs `up`, drives the page, and runs `down` in a `finally`.

- [ ] **Step 1: Write the trial volume**

Create `tests/lesson_trial.py`:

```python
"""Put a throwaway lesson volume in place, or take it away again.

    python3 tests/lesson_trial.py up     # write volumes/_trial-lessons/ and build
    python3 tests/lesson_trial.py down   # remove it and build again

Used by lesson_browser_test.mjs, which needs a built page that uses every
part of the lesson format. Nothing here is real course content.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRIAL = ROOT / "volumes" / "_trial-lessons"

LESSON = """<!-- part: Unit 2 — A trial unit -->
## Lesson 2.1 — A trial lesson

### Warm-up

1. Predict what this prints.

```python
print(2 + 3)
```

### Practice

1. Which name explains itself?
2. Fill in the table.

```python
price = 12
count = 3
```

### Try It

1. Add two prices and print the total.

> Say it: two prices go in, their sum comes out.
> Split it: store each price, add them, print the result.
"""

CHECKS = {
    "ch02a-trial#1": {"kind": "predict"},
    "ch02a-trial#2": {"kind": "choice", "options": ["`x`", "`total_price`"], "answer": 1,
                      "why": "It says what the value means."},
    "ch02a-trial#3": {"kind": "trace", "names": ["price", "count"]},
}
SOLUTIONS = "## ch02a-trial#4\n\n```python\nfirst = 3\nsecond = 4\nprint(first + second)\n```\n"


def build():
    subprocess.run([sys.executable, "build.py"], cwd=ROOT, check=True, capture_output=True)


def up():
    if TRIAL.exists():
        sys.exit(f"{TRIAL} already exists; run 'down' first")
    (TRIAL / "content").mkdir(parents=True)
    (TRIAL / "volume.json").write_text(json.dumps(
        {"number": 98, "title": "A Trial Lesson Volume", "subtitle": "Not a real course"}))
    (TRIAL / "content" / "ch02a-trial.md").write_text(LESSON)
    (TRIAL / "content" / "_checks.json").write_text(json.dumps(CHECKS))
    (TRIAL / "content" / "_boxes.json").write_text("{}")
    (TRIAL / "content" / "_solutions.md").write_text(SOLUTIONS)
    build()


def down():
    shutil.rmtree(TRIAL, ignore_errors=True)
    build()


if __name__ == "__main__":
    {"up": up, "down": down}[sys.argv[1]]()
```

- [ ] **Step 2: Write the failing browser test**

Create `tests/lesson_browser_test.mjs`, modeled on `tests/browser_check_test.mjs` (read it first for `launch`, `loadChromium`, `startSite`, the skip-when-no-browser behavior, and how it waits for Python):

```javascript
/* The lesson format in a real browser: a hint revealed one at a time, then the
 * worked solution; a multiple-choice check; a trace-table check. Builds a
 * throwaway lesson volume, and removes it again whatever happens. */
import { execFileSync } from "node:child_process";
import { launch, loadChromium, startSite, ROOT } from "./browser_harness.mjs";

const PORT = 8743;
const trial = (step) => execFileSync("python3", ["tests/lesson_trial.py", step], { cwd: ROOT, stdio: "inherit" });

const chromium = await loadChromium();
trial("up");
let bad = 0;
const expect = (label, ok) => { if (!ok) bad++; console.log(`  ${ok ? "ok  " : "FAIL"}  ${label}`); };
try {
  const stop = await startSite(PORT);
  const { browser, page } = await launch(chromium, stop);
  try {
    await page.goto(`http://localhost:${PORT}/_trial-lessons/ch02a-trial.html`);
    const hinted = page.locator('[data-box="_trial-lessons/ch02a-trial#4"]');
    await hinted.locator(".hint-next").click();
    expect("the first hint shows", await hinted.locator(".hint").nth(0).isVisible());
    expect("the second hint waits", !(await hinted.locator(".hint").nth(1).isVisible()));
    await hinted.locator(".hint-next").click();
    expect("the solution waits until every hint is shown", !(await hinted.locator(".solution").isVisible()));
    await hinted.locator(".hint-next").click();
    expect("then the worked solution shows", await hinted.locator(".solution").isVisible());

    const choice = page.locator('[data-box="_trial-lessons/ch02a-trial#2"]');
    await choice.locator('input[value="0"]').check();
    await choice.locator(".check").click();
    expect("a wrong choice is told so", (await choice.locator(".result").textContent()).startsWith("Not that one"));
    await choice.locator('input[value="1"]').check();
    await choice.locator(".check").click();
    expect("the right choice is told why", (await choice.locator(".result").textContent()).includes("says what"));

    const trace = page.locator('[data-box="_trial-lessons/ch02a-trial#3"]');
    const cells = trace.locator("input.cell");
    for (const [i, v] of ["12", "-", "12", "3"].entries()) await cells.nth(i).fill(v);
    await trace.locator(".check").click();
    await page.waitForFunction(() => document.querySelector('[data-box="_trial-lessons/ch02a-trial#3"] .result').className.includes("passed")
      || document.querySelector('[data-box="_trial-lessons/ch02a-trial#3"] .result').className.includes("failed"), null, { timeout: 60000 });
    expect("a correct trace table passes", (await trace.locator(".result").getAttribute("class")).includes("passed"));
    await cells.nth(2).fill("13");
    await trace.locator(".check").click();
    await page.waitForFunction(() => document.querySelector('[data-box="_trial-lessons/ch02a-trial#3"] .result').className.includes("failed"), null, { timeout: 60000 });
    expect("a wrong cell is named by line and variable", (await trace.locator(".result").textContent()).includes("line 2, price"));
  } finally {
    await browser.close();
    stop();
  }
} finally {
  trial("down");
}
console.log(`\n${bad ? bad + " wrong" : "the lesson format works in a real browser"}`);
process.exit(bad ? 1 : 0);
```

Read `browser_harness.mjs`'s `launch` and `startSite` before running, and match their real signatures and return values (the code above assumes `startSite(port)` returns a stop function and `launch(chromium, stop)` returns `{browser, page}`; if they differ, adapt the calls and ledger it). With `"13"` typed for `price` after line 2, the note `check_trace` writes is `line 2, price: you wrote '13', it is 12`, which the last assertion looks for.

- [ ] **Step 3: Run it**

Run: `cd tests && REQUIRE_BROWSER=1 node lesson_browser_test.mjs`
Expected: it fails first if any of Tasks 2 to 4's JavaScript is wrong; fix the cause (systematic-debugging), never the assertion, except where Step 2 says. Final: `the lesson format works in a real browser`, and `ls volumes/` shows no `_trial-lessons` afterwards.

- [ ] **Step 4: Wire into CI and commit**

In `.github/workflows/ci.yml`'s browser job, add a step after the existing browser tests:

```yaml
      - name: The lesson format works in a real browser
        working-directory: tests
        run: node lesson_browser_test.mjs
```

Run `python3 tests/workflow_test.py` and `actionlint .github/workflows/ci.yml`.

```bash
git add tests/lesson_trial.py tests/lesson_browser_test.mjs .github/workflows/ci.yml
git commit -F - <<'MSG'
test: the lesson format, end to end in a real browser

A throwaway lesson volume uses every part of the format: a warm-up, a
multiple-choice check, a trace table, and a try it with hints and a worked
solution. The test reveals the hints one at a time and sees the solution only
after the last, checks a wrong and a right choice, and checks a correct and
a wrong trace table through Python in the page. The volume is removed
afterwards, whatever happens.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 7: The vocabulary gate for lessons

**Files:**
- Create: `tests/lesson_vocabulary_test.py`
- Modify: `.github/workflows/ci.yml`

**Interfaces:**
- Consumes: `practice_test.harvest(source, into) -> bool` (unchanged); `build.split_blocks`; `build.EXERCISE_SECTIONS`; `build.chapter_files(vol)`; `build.load_solutions(vol)`.
- Produces: `lesson_vocabulary_test.violations(pages, solutions) -> list[str]`, where `pages` is a list of `(slug, markdown text)` in reading order and `solutions` maps `"<slug>#<n>"` to `{"code": str}`. A volume opts in with `"lessons": true` in its `volume.json`.

Spec note (ruling for the executor): the spec says each lesson "declares what it teaches". The existing practice-page gate derives the vocabulary from the code the course actually shows instead, and its docstring explains why a hand-kept table drifts. This plan follows the derived approach: what a lesson's examples show is what it teaches. Record this in the ledger as a ruling.

- [ ] **Step 1: Write the test, including a planted violation**

Create `tests/lesson_vocabulary_test.py`:

```python
"""Nothing in a lesson's exercises is used before a lesson has shown it.

    python3 tests/lesson_vocabulary_test.py

What a lesson teaches is what its examples show: every construct, built-in and
method in the code fences outside its exercise sections. Its exercises, their
starters and their worked solutions may use what this lesson's examples and
every earlier lesson's examples have shown, and nothing else. It is the
practice-page gate (practice_test.py), applied lesson by lesson; the
vocabulary is derived from the course, never typed in, so it cannot drift.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
import build                                                    # noqa: E402
from practice_test import harvest                               # noqa: E402

KINDS = ("nodes", "names", "attrs")


def sections(text):
    """[(is_exercise, code)] for every fence in a page, in order."""
    text = re.sub(r"^<!-- part: .+ -->\n", "", text)
    out, exercise = [], False
    for kind, payload in build.split_blocks(text.split("\n")):
        if kind == "h3":
            exercise = payload in build.EXERCISE_SECTIONS
        elif kind == "code":
            out.append((exercise, payload))
    return out


def violations(pages, solutions):
    taught = {k: set() for k in KINDS}
    found = []
    for slug, text in pages:
        fences = sections(text)
        for is_exercise, code in fences:
            if not is_exercise:
                harvest(code, taught)
        used_by = [(f"{slug} exercise fence", code) for is_exercise, code in fences if is_exercise]
        used_by += [(key, entry["code"]) for key, entry in solutions.items()
                    if key.startswith(f"{slug}#")]
        for where, code in used_by:
            used = {k: set() for k in KINDS}
            if not harvest(code, used):
                found.append(f"{where}: does not parse")
                continue
            for kind in KINDS:
                early = sorted(used[kind] - taught[kind])
                if early:
                    found.append(f"{where}: uses {kind} no lesson has shown yet: {early}")
    return found


def main():
    results = []

    def expect(label, ok, detail=""):
        results.append((label, ok, detail))

    planted = [("ch02a-one", "## L\n\n```python\nprice = 12\nprint(price)\n```\n\n### Practice\n\n"
                             "1. Print it in capitals.\n\n```python\nname = 'ada'\nprint(name.upper())\n```\n")]
    caught = violations(planted, {})
    expect("the gate catches a method no lesson has shown", any("upper" in v for v in caught), str(caught))
    expect("and lets through what the lesson's own examples show",
           not violations([("ch02a-one", "## L\n\n```python\nprice = 12\nprint(price)\n```\n\n"
                                         "### Practice\n\n1. P.\n\n```python\ncost = 3\nprint(cost)\n```\n")], {}))
    expect("a worked solution is held to the same rule",
           any("len" in v for v in violations([("ch02a-one", "## L\n\n```python\nprint(1)\n```\n")],
                                              {"ch02a-one#1": {"code": "print(len('ab'))"}})))

    for vol in build.VOLS:
        meta = json.loads((vol["dir"] / "volume.json").read_text())
        if not meta.get("lessons"):
            continue
        pages = [(p.stem, p.read_text()) for p in build.chapter_files(vol)]
        solutions = {k: v for k, v in build.load_solutions(vol).items()}
        problems = violations(pages, solutions)
        expect(f"{vol['slug']}: nothing in an exercise comes before its lesson", not problems,
               "; ".join(problems))

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + detail + ')'}")
    print(f"\n{'nothing is used before it is taught' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Prove the gate fires, then that it passes**

Run: `python3 tests/lesson_vocabulary_test.py`
Expected: all three synthetic lines `ok` on the first run, because each one is a planted case written to fire (or not) by construction. To prove the gate itself can fail, temporarily change `if not is_exercise:` to `if True:` (exercise code would then teach itself), run again, and expect the first and third lines to FAIL; restore the line, delete `tests/__pycache__/lesson_vocabulary_test*.pyc` and `tests/__pycache__/practice_test*.pyc` (see the mutation-testing note in memory: a same-length edit restored within a second can leave stale bytecode), and run again: all `ok`, under both `python3` and `/usr/bin/python3`.

- [ ] **Step 3: Wire into CI and commit**

Add `python3 tests/lesson_vocabulary_test.py` to the CI build step after the lines Tasks 1 and 4 added; run `python3 tests/workflow_test.py` and `actionlint`.

```bash
git add tests/lesson_vocabulary_test.py .github/workflows/ci.yml
git commit -F - <<'MSG'
test: nothing in a lesson's exercises comes before a lesson has shown it

The audit found syntax used before it is taught, down to a reference
solution using ord() and chr(), which the course never shows. For lessons,
what a lesson's examples show is what it teaches; its exercises and worked
solutions may use that and every earlier lesson's examples, nothing more. It
is practice_test.py's derived vocabulary, applied per lesson, for volumes
whose volume.json says "lessons": true. Shown firing on planted cases, and
failing when the exercise/example split is removed.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

---

### Task 8: The authoring reference, and the whole suite

**Files:**
- Create: `docs/lesson-format.md`

**Interfaces:**
- Consumes: Tasks 1 to 7. Produces the reference the content plan's authors follow.

- [ ] **Step 1: Write the reference**

Create `docs/lesson-format.md` describing, with one short example each, exactly what Tasks 1 to 7 built: lesson file naming (`chNNx-slug.md`, the unit in `<!-- part: Unit N — Title -->`), the exercise sections (`Warm-up`, `Practice`, `Try It`) and their straight-through numbering, hints (`> ` lines after an exercise, in the order Say it, Split it, Name it), worked solutions in `_solutions.md` under `## <slug>#<n>`, the six check kinds with a `_checks.json` example for `choice` and `trace`, unit quizzes in `quizzes.json` attached to a unit's last lesson, `"lessons": true` in `volume.json`, and the vocabulary rule. Copy each example from a test in this plan, so every example is known to work.

- [ ] **Step 2: Run the whole suite**

```bash
for py in python3 /usr/bin/python3; do
  for t in practice_test second_volume_test leak_scan_test pre_push_test scan_history_test personal_sweep_test \
           workflow_test disclaimer_test commit_msg_test site_guard_test quiz_test lesson_format_test trace_test \
           lesson_vocabulary_test; do
    $py tests/$t.py > /dev/null 2>&1 && echo "ok    $py $t" || echo "FAIL  $py $t"
  done
done
python3 build.py --check | tail -1
cd tests && for t in verify2 validate_shipped validate_stdin validate_projects; do node $t.mjs > /dev/null 2>&1 && echo "ok $t" || echo "FAIL $t"; done
REQUIRE_BROWSER=1 node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 node browser_check_test.mjs | tail -1
REQUIRE_BROWSER=1 node lesson_browser_test.mjs | tail -1
```

Expected: 28 `ok` lines for Python, `110 checked, 0 mismatched`, four node `ok`, and three browser pass lines. Run `docker run --rm -v "$PWD":/repo:ro -w /repo pf-review-gnu sh -c 'for t in lesson_format_test trace_test lesson_vocabulary_test quiz_test; do python3 tests/$t.py >/dev/null 2>&1 && echo "ok GNU $t" || echo "FAIL GNU $t"; done'` and expect four `ok`.

- [ ] **Step 3: Commit**

```bash
git add docs/lesson-format.md
git commit -F - <<'MSG'
docs: how to write a step-by-step lesson

One page for whoever writes the lessons: file names and units, the three
exercise sections, hints, worked solutions, the six check kinds, unit
quizzes, and the vocabulary rule, each with an example taken from a test.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

Ask Justin before pushing any of these commits.
