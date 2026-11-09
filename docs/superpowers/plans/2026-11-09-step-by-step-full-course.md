# Step-by-step course: the whole course — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the rest of Python Foundations in the step-by-step format: unit 1 and units 3 to 12, from
`vol1-foundations` chapters 1 and 3 to 12. The prototype passed the spec's bar on every lesson (2026-11-09), and
the first learner asked for the format across the whole course.

**Architecture:** One plan, approved once, in two parts.
- **Part A (Task 1):** generalizes the prototype's machinery so it scales to 48 lessons, and fixes the learner-facing
  minors the prototype's review deferred.
- **Part B (Tasks 2 to 12):** one task per unit, in course order. Order matters because each unit's vocabulary is what
  the units before it showed.

Each unit task gives the lesson split, the ideas and examples each lesson carries, its checks, its try-it, how the
chapter project is built across the unit, and which audit problems the unit must fix. Every unit task follows the
same build-and-review procedure (below). Exercise wording is written during execution, against the contract test,
which enforces the format.

**Tech Stack:** as the prototype: Markdown lessons, `_checks.json`, `_solutions.md`, `_boxes.json`, `quizzes.json`;
Python 3.9+ standard library tests; Node + playwright-core browser tests.

**Spec:** `docs/specs/step-by-step-course.md`. Read it with `docs/lesson-format.md` and the prototype plan
`docs/superpowers/plans/2026-11-07-step-by-step-prototype-content.md`, whose lessons (`volumes/vol1-steps/content/ch02*.md`)
are the exemplars every unit imitates.

## What the prototype taught (binding on every unit)

The learner's per-lesson answers are in the private feedback page and private memory, never in this repository.
These are the conclusions to apply:

- **The format works as built:**
  - one or two ideas per lesson;
  - two or three examples per idea, each adding one thing;
  - a practice straight after each idea;
  - a try-it whose hints walk the routine;
  - a 20-to-30-minute lesson.

  The learner rated every lesson's pace "about right" and read each at most twice. Do not compress.
- **Motivate before naming.** The routine felt "strange" when lesson 0 announced it before the learner had needed
  it. A new technique arrives after an example where its absence hurts.
- **Previews must not threaten.** A forward reference ("from unit 4 on, every decision...") was read as dread. Say
  what the learner can already do, and introduce what comes next only when it arrives.
- **Each new unit is as gradual as unit 2**, including the harder ones. The learner's standing worry is "this will
  probably get harder".

## Global Constraints

- Everything in the prototype plan's Global Constraints still holds, in particular:
  - at most 10 exercises and 1,300 words of prose per lesson;
  - nothing used before an earlier example shows it;
  - checks test behavior, never form;
  - no check may pass an exercise's starting code;
  - choice answers must not sit in one position;
  - a trace exercise is never wider, nor blanker, than a worked table shown before it;
  - a try-it's hints walk the routine, and the first one links the reference page;
  - every project is built across its unit, never handed over solved.
- **Keep every topic** (spec decision 1). Each old chapter's sections, examples and exercise ideas map to a lesson;
  nothing is dropped silently. A topic that cannot fit is a ledgered ruling and is reported to Justin.
- **Fix what the audit found** (`~/python_foundations-notes/course-audit-2026-11-04/`, private: `SYNTHESIS.md` and the
  raw chapter reports). Each unit task names its items; the unit is not done until each is addressed.
- `vol1-foundations` is unchanged until Task 13 is approved.
- Never name the first learner or quote their answers in the repository.
- Python 3.9 floor; no new dependencies; both Pythons for every Python test.
- Commit messages: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, no `Claude-Session`. Never
  `--no-verify`.
- American spellings (`grey` excepted), closed em dashes.
- **Pushing:** each push to the public repository needs Justin's yes. See "Approval asked for" at the end.

## Review Focus

1. **A unit's vocabulary depending on a later unit.** The gate reads pages in order, so a lesson that uses
   `len()` before unit 7 shows it fails. Pinned by `lesson_vocabulary_test.py` on every unit; Task 1 makes the test
   say which page first showed each name.
2. **Randomness and time in exercises.** Unit 5's guessing game, and anything using `random`, cannot be checked by
   output. Pinned in Task 6: the game is built with the secret number as a variable the checks set, and `random`
   arrives only as a last, unchecked step.
3. **Functions checked by behavior.** From unit 6, many exercises are "write a function". `function` checks must
   include an awkward case (0, empty, negative) that the spec's Check it step taught. Pinned in Task 1: a contract
   rule that every `function` check has a case with an empty, zero or negative argument.
4. **Long code on a phone.** Units 7 to 12 have longer programs. A fence or trace table wider than 390 px must
   scroll inside its own box, never the page, and stay usable. Pinned in Task 1 (the browser test measures
   containers too).
5. **The old course's links.** Retiring lesson 0, and later the old course, must not leave broken links on the shelf
   or in the new pages. Pinned by `steps_browser_test.mjs` (links resolve), which Task 1 extends to every page in
   the volume.

---

## The procedure every unit task follows

For unit N, with lessons `chNNa-…` to `chNNx-…`:

1. **Read first:**
   - the old chapter `volumes/vol1-foundations/content/chNN-*.md`;
   - its practice page;
   - its quiz in `vol1-foundations/quizzes.json`;
   - its audit report;
   - the two prototype lessons nearest in shape;
   - the private memory notes on the learner's latest feedback, plus a read of the feedback page's `lessons` and
     `units` collections.

   If the learner has reported on new lessons since the last unit, act on each muddiest point first:
   - fix the lesson, or record why not;
   - a point repeated across two lessons must change the course (spec success bar).
2. **Check the stop rule.** If two lessons in a row missed the per-lesson bar, stop building and report to
   Justin (spec).
3. **Write the unit's lessons in order**, one commit per lesson, each passing all three before its commit:
   - `python3 tests/steps_volume_test.py --only <slug>` under both Pythons;
   - `python3 tests/lesson_vocabulary_test.py`;
   - `python3 build.py --check`.

   Add the lesson's row to `LESSONS` in `steps_volume_test.py`. Add its try-it alternate to
   `content/_alternates.json`.
4. **Write the unit quiz:**
   - adapt the old chapter's quiz into `quizzes.json`, keeping every question the unit teaches and adding one
     question on the routine or on tracing;
   - run `python3 scripts/make_quizzes.py vol1-steps`;
   - attach it to the unit's last lesson.
5. **Unit review, by two fresh reviewers in parallel, before the unit's last commit:**
   - **A learner-eyes reader (Sonnet).** The same brief as the prototype's content reader. It looks for checks
     that refuse a correct answer or accept a wrong one, places where two ideas arrive at once, exercises that are
     more than one step from an example, and anything confusing or threatening for the reader.
   - **A contract and code reviewer (Sonnet).** It checks every `_checks.json` entry against its exercise's
     wording, runs plausible beginner answers through `run_check`, and confirms the audit items are addressed.

   Re-grade every finding by its effect on the learner. Fix Critical and Important findings test-first: a contract
   rule where the finding is a class of mistake, a lesson edit where it is one instance. Ledger Minor ones.
6. **Verify the unit end to end:**
   - the whole suite;
   - the browser walk of every checked exercise in the unit at 390 px (wrong answer, then right; the walk script
     is `tests/steps_walk.mjs`, added in Task 1);
   - `steps_browser_test.mjs` at the root and under `BASE`.
7. **Hand over:** worksheet checkpoint, ledger line, and ask Justin to push the unit, unless he has given the
   standing approval below.

---

## Part A

### Task 1: Machinery for 48 lessons, and the deferred minors that reach the learner

**Files:**
- Modify: `tests/steps_volume_test.py`, `tests/steps_browser_test.mjs`, `tests/lesson_vocabulary_test.py`,
  `web/box_runner.py`, `build.py`
- Create: `volumes/vol1-steps/content/_alternates.json`, `tests/steps_walk.mjs`
- Modify: `tests/site_guard_test.py`, `docs/lesson-format.md`, `.github/workflows/ci.yml`

**Interfaces:**
- Produces:
  - `content/_alternates.json`, `{"<slug>#<n>": "<code>"}`, private, never published. `build.PRIVATE_CONTENT` gains
    `"_alternates"`.
  - `steps_volume_test.LESSONS` stays the explicit, ordered list of `(slug, heading, hint steps)`. Each unit task
    appends its rows.
  - `steps_browser_test.mjs` and `steps_walk.mjs` derive their page lists from `site/vol1-steps/*.html`.
  - `steps_walk.mjs` takes an optional unit filter (`node steps_walk.mjs 03`).

- [ ] **Step 1: Alternates move to a private data file.**
  - Test first: `site_guard_test.py` plants `site/vol1-steps/_alternates.json` and expects the build guard to refuse
    it. Watch it fail.
  - Then add `"_alternates"` to `PRIVATE_CONTENT`, move the dictionary into the JSON file (same five entries), and
    load it in the test with `build.load_json(vol, "_alternates.json")`.
  - Run the contract test: it passes, and the planted-alternate failure from the prototype still fires (change one
    entry to a wrong answer, watch it fail, restore).

- [ ] **Step 2: Every `function` check has an awkward case (Review Focus 3).**
  - Contract rule: a `function` check must include a case with a `0`, `""`, `[]`, `{}` or negative number among its
    arguments. Message: `"<key>: a function check needs an awkward case (0, empty or negative)"`.
  - Prove it fires on a planted check, then remove the plant.

- [ ] **Step 3: The stdin message on an exercise with no input.**
  - `trace_test.py`-style test in a new `tests/stdin_message_test.py`. `check_stdin(source, [{"typed": [], "numbers": [5]}])`
    on `print(4)` must fail with a message starting `expected 5 among the numbers printed`, with no "typed in".
    With `typed: ["6"]` the message still starts `with '6' typed in`.
  - Watch it fail, then in `check_stdin` use a prefix that is empty when nothing is typed:
    `lead = f"with {shown} typed in, " if typed else ""`.
  - Run `node validate_stdin.mjs` and `validate_shipped.mjs`; both unchanged.

- [ ] **Step 4: A declared crash must be the declared kind.**
  - Test first, in `site_guard_test.py`'s style but in a new `tests/raises_test.py`. It calls
    `build.run_box_file('print(total)', 'x')` and a new `build.raised_name(stderr)`, which returns the exception's name or `None`,. It expects
    `'NameError'`, and expects `verify()`'s check to refuse a box declared `SyntaxError` that raises `NameError`.
  - Implement: in `verify()`, the `elif declared.get("raises"):` branch also requires
    `raised_name(run.stderr) == declared["raises"]`, else it counts as UNEXPECTED with the message
    `declared <X>, raised <Y>`.
  - `build.py --check` must still report 0 unexpected across both volumes. If a vol1-foundations declaration is
    wrong, report it and do not change vol1 without Justin's yes.

- [ ] **Step 5: Containers on a phone (Review Focus 4).**
  - `steps_browser_test.mjs` additionally asserts, for each `pre`, `.trace-wrap` and `.options` on each page:
    `scrollWidth <= clientWidth`, or the element's computed `overflow-x` is `auto`/`scroll`. A container may scroll
    inside itself; it must never push the page.
  - Derive the page list from the built directory.
  - Prove it fires by planting `white-space:nowrap; overflow:visible` on a `pre` in the built page.

- [ ] **Step 6: The walk script.** Promote the scratch walk from the prototype (wrong answer then right, every checked
  exercise, 390 px) to `tests/steps_walk.mjs`.
  - It builds its answers from the course's own data by calling `python3 tests/steps_answers.py <unit>`, a new
    small script that prints the JSON the scratch version wrote.
  - Run it on the prototype: 35/35.
  - Add it to the CI browser job after `steps_browser_test.mjs`.

- [ ] **Step 7: The vocabulary gate names where a word was first shown.** When the gate refuses a name, its message
  adds the page that will first show it, if any later page does. That tells an author whether to reorder or to add
  an example. Test: the planted `upper` case's message names no page (none shows it). A planted case whose name a
  later page shows names that page.

- [ ] **Step 8:** Full suite, both Pythons, GNU; commit per step; ledger.

---

## Part B: the units

Every lesson row below gives: the slug, the title, what it teaches (one or two ideas), and what its practice and
try-it must include. "Fix" lines are the audit's items for that unit. Hint steps:
- unit 1: none until 1.3, which introduces the routine;
- unit 2: as built;
- units 3 to 12: Say it, Split it, Name it, Check it.

### Task 2: Unit 1 — Your first programs (replaces lesson 0)

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch01a-printing` | 1.1 Printing | `print()`, strings and quotes, one line at a time, several items with commas, `print()` for a blank line | predict the order of lines; choice on matching quotes; try-it: three lines about yourself (stdin `words` check on fixed words the exercise names) |
| `ch01b-numbers-and-comments` | 1.2 Numbers and comments | numbers without quotes, `+ - * /`, the value vs the text describing it, comments | predict `3 + 4` vs `"3 + 4"`; minutes-in-a-week (calculation); try-it: a two-line calculation with a comment |
| `ch01c-errors-and-a-receipt` | 1.3 When things go wrong, and a receipt | reading an error from the bottom up (`SyntaxError`, `NameError`), then the routine: Say it, Split it, Build it | fix-the-bug from a real `NameError` (`Print("hi")`); the receipt: first the learner tries it cold in a box with no hints (unchecked, "try it, then read on"), then the routine is shown as the way out, then the receipt is built step by step |

- Unit 1 ends with its quiz, adapted from the old chapter 1 quiz.
- **Fix:** the try-it shape (ch01 #3, asterisk triangle) was the first plan-level exercise. In 1.1 it becomes an
  example first ("a shape built line by line"), then a practice changing its size.
- **Fix:** the "Printing numbers" section packed three ideas into one example. 1.2 gives each its own.
- **Retire lesson 0:**
  - delete `ch01z-welcome-back.md`, its checks, solutions and alternates, and its `LESSONS` row;
  - in 2.4, replace "Lesson 0's receipt" with "Unit 1's receipt";
  - in 2.1's warm-up, check every reference is still true.
- **Learner fix:** 2.2's sentence "From unit 4 on, every decision a program makes comes down to `True` or
  `False`." becomes "You will use `True` and `False` a lot. For now, it is enough to know they are their own
  kind of value." Re-run the browser walk for unit 2.

### Task 3: Unit 3 — Expressions and operators

The densest old chapter (eight sections), and where the first learner places the start of the trouble. Five lessons.

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch03a-more-arithmetic` | 3.1 More arithmetic | `//` and `%` (one example each, then together as "how many whole, how many left"), `**` | trace a `//`/`%` pair; minutes to hours-and-minutes; try-it: seconds to minutes and seconds |
| `ch03b-order-and-rounding` | 3.2 Order of operations, and rounding | precedence and parentheses; `round()`; why `0.1 + 0.2` is not `0.3` (one example, no theory) | predict two expressions differing only in parentheses; choice on precedence; try-it: an average rounded to 1 place |
| `ch03c-formatting` | 3.3 Formatting output | f-strings, then `:.2f`; string `+` and `*` | rewrite a print as an f-string (stdin `words`); dollars to 2 places; try-it: a price line with `:.2f` |
| `ch03d-comparing` | 3.4 Comparing values | `== != < > <= >=` giving `True`/`False` (the bool payoff, stated kindly); `=` vs `==` practiced, not just stated | trace with a bool; fix-the-bug: `print(score = 10)`, which raises a real `TypeError` because `=` stores and does not compare, fixed to `print(score == 10)`; try-it: is a number even (prints `True`/`False`) |
| `ch03e-combining-and-change` | 3.5 Combining conditions, and the change machine | `and`, `or`, `not`; `+=` and friends; then the chapter project | choice on `and`/`or`; trace with `+=`; the change-making machine built across the lesson's try-it and two practices (from `//` and `%` in 3.1), never shown solved |

- **Fix:**
  - `=` vs `==` (prose only in the old chapter) gets its own fix-the-bug practice;
  - the change-maker's greedy reasoning, explained after the fact in the old chapter, becomes the try-it's Split it
    hint;
  - the `//` + `%` pattern gets its name ("how many whole, how many left") when first used, and is reused by name.

### Task 4: Unit 4 — Making decisions

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch04a-if-and-else` | 4.1 If, and else | the shape of `if` (colon, indent), `else` | predict with an `if`; fix-the-bug from a real `TypeError` (`if age > 12:` where `age` came from `input()` unconverted); a missing colon and bad indentation are shown as examples with their errors, never as exercises (see Note); try-it: pass or fail on a score |
| `ch04b-elif-and-rules` | 4.2 Elif, and turning a rule into code | `elif`; a worked example that builds a multi-part rule from a sentence (the leap-year shape, on a different rule) | choice on which branch runs; try-it: the leap-year rule itself, with hints that Split it clause by clause |
| `ch04c-nesting-and-truthiness` | 4.3 Nesting, and what counts as true | nested `if`; truthiness with code (`if name:` on `""` and `"Ada"`) | trace through a nested `if`; predict truthiness; try-it: a two-question decision |
| `ch04d-validating-and-the-kiosk` | 4.4 Checking input, and the ticket kiosk | validating input (`.isdigit()` only if shown first; otherwise range checks); the kiosk built step by step | the kiosk across two practices and the try-it, each one decision deeper |

- **Fix:**
  - leap year was the book's first plan-level exercise with no model, so 4.2 models a rule first;
  - truthiness had no code, so 4.3 has examples and a predict;
  - the kiosk arrived three levels deep and solved, so 4.4 builds it a level at a time.
- **Note:** a `SyntaxError` exercise cannot pass the vocabulary gate (it does not parse). Indentation and colon
  mistakes are taught as examples with their error shown (declared in `_boxes.json`), and practiced as choice
  items.

### Task 5: Unit 5 — Repetition

The old cliff. Five lessons, one loop idea each.

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch05a-while` | 5.1 Repeating with while | `while` with a counter; tracing a loop | trace table of a 3-pass loop (rows repeat; the trace check handles it); try-it: count down from 5 |
| `ch05b-for-and-range` | 5.2 For and range() | `for` with `range(n)`, then `range(a, b)`, then `range(a, b, step)`: one example each, every form run | predict each `range` form; try-it: the first 10 square numbers |
| `ch05c-looping-over-text` | 5.3 Looping over a string | `for ch in text` | count a letter; try-it: print a word one letter per line, then count its vowels |
| `ch05d-adding-up` | 5.4 Adding up as you go | the accumulator; then the sentinel loop ("read, loop, read again") combined with a total, as a worked example; "largest so far", with its starting-value bug shown and fixed in code | trace an accumulator; fix-the-bug: largest-so-far starting at 0 with all-negative input (Check it); try-it: add numbers until 0 (stdin check with typed sequences, including an awkward first 0) |
| `ch05e-stopping-and-the-game` | 5.5 Stopping early, and a guessing game | `break`, `continue`; the guessing game built step by step | the game across practices with the secret number set by a variable the checks give (`secret = 7` in the starter, stdin runs typing guesses); `random` is shown last, as an example only, with "replace the 7 with this" |

- **Fix:**
  - the old "for and range()" section had five ideas in three examples, and two forms were never run;
  - the sum-until-0 exercise had no example;
  - the largest-so-far bug was named but never exercised;
  - the guessing game had no check.
- **Machinery check:** confirm the `trace` check handles a loop's repeated lines (rows are per executed line).
  Write one trace exercise over a 3-pass loop and run its check before relying on it. If the row labels repeat
  confusingly, ledger it and keep loop traces to at most 3 passes.

### Task 6: Unit 6 — Functions

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch06a-defining` | 6.1 Making your own function | `def`, calling it, parameters | `function`-style practice is not yet possible (no return); stdin checks on printing functions; try-it: `greet(name)` |
| `ch06b-returning` | 6.2 Giving back a value | `return`; a multi-branch return as a worked example (the `letter_grade` shape) before any exercise needs one | `function` checks with awkward cases; try-it: `largest_of_three` (now after its model) |
| `ch06c-scope-and-docstrings` | 6.3 Where names live, and describing a function | local vs global (one example each), docstrings | predict a scope example; fix-the-bug from a real `NameError` caused by scope; try-it: `is_even` with a docstring |
| `ch06d-splitting-into-functions` | 6.4 Splitting a problem into functions | Split it, where each step becomes a function, from a blank problem statement; `main()` built up from two small functions before the project | the grade calculator built function by function; try-it: `is_prime` (Split it: what does "prime" mean, step by step) |

- **Fix:**
  - `largest_of_three` and `is_prime` needed an algorithm with no model, so each comes after one;
  - decomposition was taught on a finished program only, so 6.4 starts blank;
  - `main()` had no lead-in, so 6.4 builds one small one first.

### Task 7: Unit 7 — Lists

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch07a-lists-and-indexing` | 7.1 Lists, and finding an item | making a list, indexing (positive, then negative, one example each), changing an item | trace a list (cells hold lists by value); `IndexError` fix-the-bug; try-it: first and last of a list |
| `ch07b-slicing` | 7.2 Slicing | `[a:b]`, then omitted ends, then a step: one example each (the old section put four ideas in one) | predict slices; try-it: middle three items |
| `ch07c-methods-and-built-ins` | 7.3 Changing a list, and asking about it | `append`, `insert`, `remove`, `pop` (each demonstrated), then `len`, `sum`, `max`, `min`, `sorted` | function checks with an empty-list case; try-it: average of a list (empty list is the Check it case) |
| `ch07d-looping-and-the-gradebook` | 7.4 Looping over lists, and a gradebook | `for x in list`, nested lists as rows; the gradebook built step by step | the gradebook across practices; `index(max(...))` only after both are shown; comprehensions are not used (old chapter used them in the project unannounced) |

- **Fix:**
  - slicing's four ideas in one example;
  - project syntax used before it was taught (`index(max())`, comprehensions).

  Comprehensions are kept as a topic: a short example section in 7.4, after the loop they replace, marked
  "another way to write it", and not required by any exercise.

### Task 8: Unit 8 — Strings as data

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch08a-methods` | 8.1 Strings can't change, and their methods | immutability (one example); `upper`, `lower`, `strip`, `replace`, `find`, `count`, `startswith`, `endswith`, `isdigit`, each with its own example (the old table showed four of them nowhere else) | choice on immutability; function checks; try-it: tidy a messy name |
| `ch08b-comparing-split-join` | 8.2 Comparing text, split and join | comparing safely (`lower()` both sides); `split()`, `join()` | try-it: count words in a sentence |
| `ch08c-character-by-character` | 8.3 One character at a time | processing characters; palindromes as a worked example built with the routine | try-it: is it a palindrome, ignoring spaces and case |
| `ch08d-escapes-and-analyzer` | 8.4 Special characters, and a text analyzer | escape sequences; the analyzer built step by step | analyzer across practices |

- **Fix:**
  - the `caesar_shift` reference solution used `ord`/`chr`, which are never taught. If the Caesar exercise is kept,
    8.3 teaches `ord` and `chr` with an example each first; otherwise it moves to the optional extra practice
    (ruling, ledgered).
  - Project format specifications were used before being explained; the analyzer's output format is shown as a
    worked example first.

### Task 9: Unit 9 — Dictionaries and sets

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch09a-dictionaries` | 9.1 Looking things up by name | creating, reading, adding, changing; `KeyError` and `get()` | `KeyError` fix-the-bug; try-it: a phone-book lookup |
| `ch09b-looping-and-counting` | 9.2 Looping over a dictionary, and counting | `for key in d`, `.items()`; the counting pattern | try-it: count letters in a word |
| `ch09c-nested` | 9.3 Dictionaries inside dictionaries | nested dictionaries, one level at a time; `dict.copy()` taught here (the old practice needed it untaught) | try-it: read one value two levels down |
| `ch09d-sets-and-the-poll` | 9.4 Sets, choosing a container, and a poll counter | sets; which container when; the poll counter built step by step | `invert` gets a model first, and checks on the easy items too |

- **Fix:**
  - checks sat on the hardest item only (1 of 7), so every unit-9 practice gets a check;
  - `invert` was plan-level with no model;
  - `dict.copy()` was used untaught.

### Task 10: Unit 10 — Tuples and records

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch10a-tuples-and-unpacking` | 10.1 Tuples, and unpacking | why an unchangeable list; unpacking | try-it: swap two values by unpacking |
| `ch10b-records` | 10.2 Records: a list of dictionaries | one record, then a list of them; reading a field from each | try-it: names of everyone over an age |
| `ch10c-working-with-records-and-inventory` | 10.3 Working with records, and an inventory | sorting by a field, totals, grouping, one idea per example; `.setdefault()` explained where first used (the old chapter used it before explaining) | the inventory built step by step; `distance` gets its model first |

- **Fix:**
  - "Working with records" had five ideas, one example each, so it is split across 10.3's examples with a
    practice after each;
  - `.setdefault()` was used before it was explained;
  - the only check sat on the hardest item.

### Task 11: Unit 11 — Searching and sorting

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch11a-linear-search` | 11.1 Looking through a list | linear search, traced | trace; try-it: index of the first match, or -1 (empty list is the Check it case) |
| `ch11b-binary-search` | 11.2 Halving the search | binary search, traced row by row on a 7-item list | trace (at most 3 passes); try-it: binary search on a sorted list |
| `ch11c-counting-and-selection` | 11.3 Counting the work, and selection sort | counting steps instead of the old complexity table (a small table built by the learner); selection sort traced | try-it: count comparisons for a list of 5 |
| `ch11d-bubble-and-python` | 11.4 Bubble sort, and what Python does | bubble sort; `sorted` and `key=` (shown before used) | measuring project built step by step |

- **Fix:**
  - #2, #4, #7 and the project were plan-level with no check, so each gets a model and a check;
  - the practice page's tie-breaking rule was never taught, so 11.4 teaches it.

### Task 12: Unit 12 — Recursion and problem solving

| Slug | Lesson | Teaches | Practice and try-it |
|---|---|---|---|
| `ch12a-the-two-parts` | 12.1 A function that calls itself | base case and recursive case; following the calls with a call table | trace a countdown's calls; try-it: sum 1 to n recursively |
| `ch12b-more-examples` | 12.2 Three shapes of recursion | one pattern per section (factorial, string reversal, list sum), each with a practice | function checks with an empty or zero case |
| `ch12c-when-it-goes-wrong` | 12.3 When recursion goes wrong, and when to use it | missing base case (`RecursionError`, declared); Fibonacci's repeated work, counted | fix-the-bug from a `RecursionError`; choice on when to use recursion |
| `ch12d-the-capstone` | 12.4 Putting it all together: a records system | the routine on the largest problem in the course, Split into functions; built step by step across practices; `enumerate(..., start=1)` shown before used | the capstone; Tower of Hanoi moves to the optional extra practice unless it fits with a model and a check |

- **Fix:**
  - the old chapter had no problem-solving section despite its title; 12.4 is that section;
  - "More examples" had three patterns with one example each;
  - `enumerate(..., start=1)` was used before being shown.

### Task 13: Hand over, and the cutover question

- Full suite, the browser walk of every unit, a final whole-course review on the most capable model (the
  executing-plans final review), and the learner-eyes reader over the whole course in one pass, looking for drift
  between units.
- **Report to Justin:**
  - lesson count;
  - every topic-mapping ruling;
  - deferred minors;
  - the learner's feedback so far.
- **Ask, do not act:**
  - whether the new course replaces `vol1-foundations` (spec decision 3: "then the new one replaces it");
  - whether to build the optional extra-practice page per unit, deferred since the prototype.

---

## Approval asked for

Approving this plan approves Part A, all eleven units in order, retiring lesson 0, and the 2.2 sentence change.
Two things it does not approve without your word:

1. **Pushing.** Choose one:
   - a standing yes to push each unit when its review is clean and its suite is green (one message each time saying
     what went out);
   - or ask before every push.
2. **How it runs:**
   - subagent-driven: a fresh implementer per unit on the most capable model (writing lessons is judgment), and
     two Sonnet reviewers per unit;
   - or a Workflow per unit doing the same as a pipeline, which you have used before.

   Either way the units run in order, because each unit's vocabulary is what earlier units showed.

## Decisions (Justin, 2026-11-09)

- The plan is approved as written: Part A, units 1 and 3 to 12 in order, retiring lesson 0, the 2.2 rewrite.
- **Pushing:** a standing yes to push each unit once its review is clean and its whole suite is green, with a note
  to Justin each time saying what went out. Anything else (a push mid-unit, a fix outside the plan) still asks.
- **Execution:** subagent-driven. A fresh implementer per unit on the most capable model, then two Sonnet reviewers
  (learner-eyes, checks against wording). The controller verifies and fixes between units.
- **The end:** once every unit passes, the new course replaces `vol1-foundations` on the shelf. Task 13 does the
  cutover and still asks before that push, since it changes what every visitor sees.

