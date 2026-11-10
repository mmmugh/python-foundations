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
    refused("a fence inside the steps before step 1 is refused (the page would drop it)",
            GOOD.replace("### Steps\n\n", "### Steps\n\n```python\nprint(1)\n```\n\n"), "before the first exercise")
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
