"""Check the wording of check_stdin's failure message.

    python3 tests/stdin_message_test.py

An exercise with no typed input still reports a failure through check_stdin,
and "with nothing typed in, ..." reads as if the learner typed the word
"nothing". An exercise that takes no input should say so by saying nothing
about typing at all.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "web"))
import box_runner                                               # noqa: E402


def main():
    results = []

    def expect(label, ok, detail=""):
        results.append((label, ok, detail))

    ok, notes = box_runner.check_stdin("print(4)", [{"typed": [], "numbers": [5]}])
    expect("no typed input and a wrong answer: no mention of typing",
           not ok and notes[0].startswith("expected 5 among the numbers printed"), notes)

    ok, notes = box_runner.check_stdin("print(4)", [{"typed": ["6"], "numbers": [5]}])
    expect("typed input and a wrong answer: still names what was typed",
           not ok and notes[0].startswith("with '6' typed in"), notes)

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + str(detail) + ')'}")
    print(f"\n{'the message fits whether anything was typed' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
