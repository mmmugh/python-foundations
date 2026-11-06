# Writing a step-by-step lesson

The reference for whoever writes lessons for a step-by-step volume (`volumes/vol1-steps/`). It describes what
the build supports, and every example below is taken from a test, so it is known to work. The why is in
`docs/specs/step-by-step-course.md`.

## The volume

A volume opts into lessons in its `volume.json`:

```json
{"number": 2, "title": "Python Foundations, step by step", "subtitle": "...", "lessons": true}
```

`"lessons": true` turns on the vocabulary gate (below) for that volume. A volume with lesson files
(`chNNx-slug.md`) but without the flag fails the gate, so a forgotten flag cannot switch it off.

## Lesson files

One file per lesson in `content/`, named `chNNx-slug.md`: the unit number, then a letter for the lesson's place
in the unit (`ch02a-naming.md`, `ch02b-kinds.md`, ...). Lessons of one unit sort by filename. The first line
names the unit:

```markdown
<!-- part: Unit 2 — Variables -->
## Lesson 2.1 — Naming a value
```

## Exercise sections

Three `###` headings hold exercises: `Warm-up`, `Practice` and `Try It` (`Steps` is the practice pages' name for
the same thing). A lesson may have several, with prose and examples between them. Each list item under one is an
exercise with its own box; a code fence directly after an item is that exercise's starting code.

Exercises are numbered straight through the page, not per section, because checks and solutions are found by
`<page>#<n>`. In this lesson the warm-up is `#1`, the practice items are `#2` and `#3`, and the try it is `#4`:

````markdown
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
````

## Hints

Each `> ` line directly after an exercise (or after its code fence) is one hint, in order. They are revealed one
per click; the routine's first three steps are the usual hints:

```markdown
1. Add two prices and print the total.

> Say it: two prices go in, their sum comes out.
> Split it: store each price, add them, print the result.
> Name it: `first_price`, `second_price`, `total`.
```

If the exercise has a worked solution, it stays hidden until the last hint has been shown. Hints with no worked
solution behind them are fine. Hints and worked solutions work the same way on every kind of exercise, choice and
trace included.

## Worked solutions

In `content/_solutions.md`, under a heading naming the exercise. A paragraph after the fence is shown as the
note beside the solution:

````markdown
## ch02a-trial#4

```python
first = 3
second = 4
print(first + second)
```
````

## Checks

In `content/_checks.json`, keyed by `<page>#<n>`. A check tests what a program does, never how it is written.
Six kinds:

| Kind | What it checks |
|---|---|
| `output` | the program prints `expected` |
| `stdin` | given `typed` lines, the output holds `numbers` in order |
| `function` | a named function returns each case's result |
| `predict` | the learner's prediction matches what the fence prints |
| `choice` | the learner picked option `answer` (an index from 0) |
| `trace` | a trace table: each named variable's value after each line |

The four original kinds, as vol1-foundations uses them:

```json
{"ch06-functions#1": {"kind": "function", "name": "is_even", "cases": [[[4], true], [[7], false]]},
 "ch01-your-first-programs#4": {"kind": "predict"},
 "ch03-expressions-and-operators#3": {"kind": "output", "expected": "####################"},
 "ch02-variables-and-types#2": {"kind": "stdin", "runs": [{"typed": ["6", "4"], "numbers": [10, 24]}]}}
```

### `choice`

Radio buttons and Check, decided in the page. Options are inline Markdown, so code goes in backticks. `why` is
shown when the pick is right; a wrong pick is not told the answer. A code fence after the item is shown
read-only above the options. The build refuses fewer than two options, or an `answer` that is not one of them.

```json
{"ch02a-trial#2": {"kind": "choice", "options": ["`x`", "`total_price`"], "answer": 1,
                   "why": "It says what the value means."}}
```

### `trace`

The exercise's code fence is the program to trace; `names` are the variables, in column order. The table has a
row per executed line. The expected values are worked out by running the program, at build time and again in
the page, and both must step through it the same way, so the build refuses a program that has:

- a statement spread over several lines, or a statement and its body on one line (`while x: x = x - 1`);
- a comprehension;
- a function, `lambda` or class (lines inside them are not traced);
- `input()`;
- a value a learner cannot write down (`range(3)`, `float('inf')`).

Plain assignments, `if`/`elif`/`else`, and `for` and `while` loops with their bodies on their own lines are fine.

Answers are compared by value: `'Ada'`, `"Ada"` and `Ada` are the same string, `3` is `3.0`, and blank or `-`
means "not set yet". Quotes are optional only when the text could not be read as anything else: `3` written for
the text `'3'` is wrong, and so is `1` for `True`, because the kind of value is part of the answer. A wrong cell
is named by line and variable, and says when the kind is wrong ("you wrote a number; it is text").

````markdown
2. Fill in the table.

```python
price = 12
count = 3
```
````

```json
{"ch02a-trial#3": {"kind": "trace", "names": ["price", "count"]}}
```

## Unit quizzes

One quiz per unit, in the volume's `quizzes.json`, attached to the unit's last lesson by its slug. The quiz is
headed `Unit N - Title` from that lesson's `<!-- part: -->` line, and the lesson's page links to it as
"Unit N quiz". Render with the volume named, since there is more than one:

```json
{"quizzes": [{"slug": "ch02d-together", "questions": [
  {"section": "Vocabulary", "text": "A name for a value is a ____.", "answers": ["variable"]}]}]}
```

```bash
python3 scripts/make_quizzes.py vol1-steps
```

Sections are `Vocabulary`, `Reading code`, `Writing code` and `Why it works`; any other is refused.

## The vocabulary rule

What a lesson teaches is what its examples show: every construct, built-in function and method in the code
fences outside its exercise sections. Its exercises, their starting code and their worked solutions may use what
this lesson's examples and every earlier lesson's examples have shown, and nothing else. So may the
`inline code` in its hints and in its choice options.
`tests/lesson_vocabulary_test.py` enforces it. To use something new in an exercise, show it in an example first.

This fails, because `.upper()` appears only in the exercise:

````markdown
```python
price = 12
print(price)
```

### Practice

1. Print it in capitals.

```python
name = 'ada'
print(name.upper())
```
````

An exercise fence must parse. A fix-the-bug practice should start from an error raised while the program runs
(a `NameError`, a `TypeError`), not from a `SyntaxError`.
