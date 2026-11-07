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
    done = subprocess.run([sys.executable, "build.py"], cwd=ROOT, capture_output=True, text=True)
    if done.returncode:
        sys.exit(f"the build failed:\n{done.stdout[-1500:]}{done.stderr[-1500:]}")


def up():
    if TRIAL.exists():
        sys.exit(f"{TRIAL} already exists; run 'down' first")
    (TRIAL / "content").mkdir(parents=True)
    (TRIAL / "volume.json").write_text(json.dumps(
        {"number": 98, "title": "A Trial Lesson Volume", "subtitle": "Not a real course",
         "lessons": True, "status": "in progress"}))
    (TRIAL / "content" / "ch02a-trial.md").write_text(LESSON)
    (TRIAL / "content" / "_checks.json").write_text(json.dumps(CHECKS))
    (TRIAL / "content" / "_boxes.json").write_text("{}")
    (TRIAL / "content" / "_solutions.md").write_text(SOLUTIONS)
    # A quiz on the unit's lesson, so the page's quiz link (labeled with the
    # unit, not a chapter) is on the page to be checked.
    (TRIAL / "quizzes").mkdir()
    (TRIAL / "quizzes" / "ch02a-trial-quiz.txt").write_text(
        "PYTHON FOUNDATIONS\nUnit 2 - A trial unit\n")
    build()


def down():
    shutil.rmtree(TRIAL, ignore_errors=True)
    build()


if __name__ == "__main__":
    {"up": up, "down": down}[sys.argv[1]]()
