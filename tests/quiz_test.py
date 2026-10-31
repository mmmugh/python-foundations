"""Check the quizzes and answer keys are what quizzes.json renders.

    python3 tests/quiz_test.py

The .txt files are generated, but they are also what students print and what
the site serves, so a hand edit to one would quietly part it from its source,
and the next regeneration would undo it. This renders every quiz and key from
volumes/<volume>/quizzes.json in memory and compares them with the files.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.argv = sys.argv[:1]                    # make_quizzes reads a volume slug from argv
import make_quizzes                                             # noqa: E402


def main():
    results = []

    def expect(label, ok, detail=""):
        results.append((label, ok, detail))

    data = json.loads(make_quizzes.SOURCE.read_text())
    files = make_quizzes.outputs(data)
    stale = [p.relative_to(ROOT).as_posix() for p, text in files.items()
             if not p.exists() or p.read_text() != text]
    expect(f"all {len(files)} quizzes and keys are what quizzes.json renders",
           len(files) == 24 and not stale, f"differ: {stale}")

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + detail + ')'}")
    print(f"\n{'every quiz is what its source says' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
