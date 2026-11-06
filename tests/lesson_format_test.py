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

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'the lesson format holds' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
