"""Check how the shelf tells volumes apart.

    python3 tests/shelf_test.py

Three things the shelf must get right, none of them visible with only one
volume around: a retired volume is taken off the shelf but its pages, boxes,
checks, quizzes and bundle still build (retiring is not deleting); a lesson
volume has no code bundle (a lesson's warm-up and practice fences are
exercises, not examples to hand out as files); and a status mark appears
beside a volume's title only when that volume actually has a status. Puts
the throwaway lesson volume from lesson_trial.py in place, builds, looks,
and takes it away again.
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

        # (a) vol1-foundations is retired: off the shelf, but still published.
        check('vol1-foundations/' not in index,
              "a retired volume is off the shelf")
        check((SITE / "vol1-foundations" / "ch01-your-first-programs.html").exists(),
              "a retired volume's pages still build")
        check((SITE / "vol1-foundations" / "bundle.html").exists(),
              "a retired volume's bundle still builds")

        # (b) a lesson volume has no code bundle.
        check('href="_trial-lessons/bundle.html"' not in index,
              "the shelf offers no code bundle for a lesson volume")
        check(not (SITE / "_trial-lessons" / "bundle.html").exists(),
              "no bundle page is written for a lesson volume")

        # (c) a status mark appears only for a volume that has a status.
        # Anchored to the trial's own heading: the shelf is one line, and an
        # unanchored match would run from one heading to another, passing a
        # real volume's mark off as the trial's.
        heading = re.search(r'<h2><a href="_trial-lessons/[^"]*">A Trial Lesson Volume</a>.*?</h2>', index)
        check(heading is not None and '<span class="status">in progress</span>' in heading.group(0),
              "a volume with a status gets the mark")
        plain = re.search(r'<h2><a href="vol1-steps/[^"]*">.*?</h2>', index)
        check(plain is not None and 'class="status"' not in plain.group(0),
              "a volume without a status gets no mark")
    finally:
        lesson_trial.down()

    print(f"\n{'the shelf tells volumes apart' if not problems else str(len(problems)) + ' wrong'}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
