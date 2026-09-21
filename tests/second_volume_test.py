"""Prove a second volume needs nothing but a directory.

    python3 tests/second_volume_test.py

The whole point of volumes/ is that adding a course means adding a directory
with a volume.json in it, and editing no code. That is easy to believe and easy
to break -- a hardcoded slug, a path joined one level too high, a guard that
only looks where volume one happens to live -- and none of it shows up while
there is only one volume.

So this makes a throwaway volume, runs the real build, checks what came out,
and removes it again.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRIAL = ROOT / "volumes" / "_trial-volume"
SITE = ROOT / "site"

CHAPTER = '''<!-- part: Part One -->
## Chapter 1 — A Trial Chapter

One box, one stated output, so the build has something to check.

```python
print(6 * 7)
```

Output:

```
42
```
'''


def write_trial():
    (TRIAL / "content").mkdir(parents=True)
    (TRIAL / "quizzes").mkdir()
    (TRIAL / "volume.json").write_text(json.dumps({
        "number": 99, "title": "A Trial Volume",
        "subtitle": "Not a real course",
        "blurb": "Written and deleted by tests/second_volume_test.py.",
    }))
    (TRIAL / "content" / "00-front-matter.md").write_text(
        "## A Trial Volume\n\nA throwaway volume.\n")
    (TRIAL / "content" / "ch01-a-trial-chapter.md").write_text(CHAPTER)
    for name in ("_boxes.json", "_checks.json"):
        (TRIAL / "content" / name).write_text("{}")


def main():
    if TRIAL.exists():
        sys.exit(f"{TRIAL} already exists -- remove it and run again")

    problems = []

    def check(ok, what):
        print(f"  {'ok  ' if ok else 'FAIL'}  {what}")
        if not ok:
            problems.append(what)

    write_trial()
    try:
        run = subprocess.run([sys.executable, "build.py", "--check"],
                             cwd=ROOT, capture_output=True, text=True, timeout=900)
        check(run.returncode == 0,
              f"the build succeeds with two volumes (exit {run.returncode})")
        if run.returncode != 0:
            print(run.stdout[-2000:] or run.stderr[-2000:])
            raise SystemExit(1)

        out = SITE / "_trial-volume"
        check(out.is_dir(), "the new volume gets its own directory in site/")
        page = out / "ch01-a-trial-chapter.html"
        check(page.exists(), "its chapter is rendered")

        text = page.read_text() if page.exists() else ""
        check('href="../app.css"' in text and 'src="../app.js"' in text,
              "its pages reach the shared stylesheet and runtime one level up")
        check('data-volume="_trial-volume"' in text,
              "its pages carry the volume, so saved work cannot collide")
        check(not (out / "pyodide").exists() and (SITE / "pyodide").is_dir(),
              "the 13 MB runtime is shared, not copied per volume")

        index = (SITE / "index.html").read_text()
        check('href="_trial-volume/00-front-matter.html"' in index,
              "the library page lists it")
        check("All volumes" in index,
              "the library page stops calling itself volume one")

        boxes = json.loads((SITE / "boxes.json").read_text())
        mine = [b for b in boxes if b["volume"] == "_trial-volume"]
        check(len(mine) == 1 and mine[0]["id"] == "_trial-volume/ch01-a-trial-chapter#0",
              "its boxes are listed under ids that carry the volume")

        check("111 checked" in run.stdout or "checked, 0 mismatched" in run.stdout,
              "its stated output is checked like any other")
    finally:
        # Deliberately NOT deleting site/_trial-volume by hand: the build is
        # supposed to notice the volume is gone and take its pages down. Doing
        # it here would hide a volume that stays published after being removed.
        shutil.rmtree(TRIAL, ignore_errors=True)
        again = subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                               capture_output=True, text=True, timeout=900)
        left = (SITE / "_trial-volume").exists()
        check(not left and again.returncode == 0,
              "removing a volume takes its pages down again")
        if left:
            shutil.rmtree(SITE / "_trial-volume", ignore_errors=True)

    print("\n" + ("a second volume is just a directory"
                  if not problems else f"{len(problems)} problem(s)"))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
