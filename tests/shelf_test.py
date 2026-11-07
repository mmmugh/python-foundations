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
        plain = re.search(r'<h2><a href="vol1-foundations/[^"]*">.*?</h2>', index)
        check(plain is not None and 'class="status"' not in plain.group(0),
              "a volume without a status gets no mark")
    finally:
        lesson_trial.down()

    print(f"\n{'the shelf tells the two kinds of volume apart' if not problems else str(len(problems)) + ' wrong'}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
