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
    where = [first.find(h) for h in ("Say it", "Split it", "Name it")]
    expect("hints keep their order", -1 not in where and where == sorted(where), True)
    expect("a hinted exercise has a reveal button", 'class="hint-next"' in first, True)
    expect("its worked solution waits behind the hints", '<details class="solution" hidden>' in first, True)
    expect("an exercise with no hints gets no hint block", 'class="hints"' in second, False)

    no_solution = build.render(build.split_blocks(
        "## L\n\n### Practice\n\n1. Try.\n\n> Say it: a hint.\n".split("\n")), "trial/ch02d-x")
    expect("hints without a worked solution still render", no_solution.count('class="hint"'), 1)

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

    build.CHECKS["trial/ch02f-trace#1"] = {"kind": "trace", "names": ["price", "count"]}
    traced = build.render(build.split_blocks(
        "## L\n\n### Practice\n\n1. Fill in the table.\n\n```python\nprice = 12\ncount = 3\n```\n".split("\n")),
        "trial/ch02f-trace")
    expect("a trace exercise renders a row per executed line", traced.count('<tr class="step"'), 2)
    expect("and a cell per name per row", traced.count('<input class="cell"'), 4)
    expect("a trace exercise carries its program for the check", 'data-code=' in traced, True)


    # Found in review: a trace program must give the same rows on the build's
    # Python and the page's, and must give values a learner can write down.
    for label, program in (("a comprehension", "s = [n for n in range(3)]"),
                           ("a statement over two lines", "x = (1 +\n     2)"),
                           ("an if whose test spans lines", "x = 2\nif (x > 0 and\n    x < 5):\n    y = 1"),
                           ("a loop on one line", "x = 3\nwhile x: x = x - 1"),
                           ("a function", "def f():\n    return 1\ny = f()"),
                           ("input()", "name = input()"),
                           ("a value that is not a literal", "x = range(3)")):
        build.CHECKS["trial/ch02g-bad#1"] = {"kind": "trace", "names": ["x"]}
        try:
            build.render(build.split_blocks(
                f"## L\n\n### Practice\n\n1. T.\n\n```python\n{program}\n```\n".split("\n")), "trial/ch02g-bad")
            expect(f"the build refuses a trace of {label}", "accepted", "refused")
        except SystemExit:
            expect(f"the build refuses a trace of {label}", "refused", "refused")
    expect("a trace carries the rows' line numbers for the page to compare",
           '&quot;lines&quot;: [1, 2]' in traced, True)

    # Found in review: hints and a worked solution on a choice or a trace
    # exercise were dropped without a word.
    build.CHECKS["trial/ch02h-x#1"] = {"kind": "choice", "options": ["a", "b"], "answer": 0}
    build.CHECKS["trial/ch02h-x#2"] = {"kind": "trace", "names": ["price"]}
    build.SOLUTIONS["trial/ch02h-x#2"] = {"code": "price = 12", "note": ""}
    both = build.render(build.split_blocks(
        "## L\n\n### Practice\n\n1. Pick.\n\n> Say it: a hint.\n\n2. Trace.\n\n```python\nprice = 12\n```\n\n"
        "> Split it: a hint.\n".split("\n")), "trial/ch02h-x")
    first, second = both.split('data-box="trial/ch02h-x#2"')
    expect("a choice exercise keeps its hints", first.count('class="hint" hidden'), 1)
    expect("a trace exercise keeps its hints", second.count('class="hint" hidden'), 1)
    expect("a trace exercise keeps its worked solution, behind its hints",
           '<details class="solution" hidden>' in second, True)

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'the lesson format holds' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
