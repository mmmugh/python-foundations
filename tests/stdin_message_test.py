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

    # A program that prints every branch's message, whatever is typed, would
    # pass a check that only asks for the right word to appear. "absent"
    # names the words that must not appear in that run.
    both = 'score = int(input())\nif score >= 50:\n    print("Pass")\nprint("Fail")'
    right = 'score = int(input())\nif score >= 50:\n    print("Pass")\nelse:\n    print("Fail")'
    runs = [{"typed": ["75"], "words": ["pass"], "absent": ["fail"]},
            {"typed": ["45"], "words": ["fail"], "absent": ["pass"]}]
    ok, notes = box_runner.check_stdin(both, runs)
    expect("a program that prints both branches is refused by absent",
           not ok and notes == ["with '75' typed in, your program also printed 'fail', which should not appear here"],
           notes)
    ok, notes = box_runner.check_stdin(right, runs)
    expect("a program that prints only the right branch passes", ok, notes)
    ok, notes = box_runner.check_stdin('print("Pass")', [{"typed": [], "absent": ["pass"]}])
    expect("absent with nothing typed: no mention of typing",
           not ok and notes == ["your program also printed 'pass', which should not appear here"], notes)
    ok, notes = box_runner.check_stdin('print("Fail")', [{"typed": [], "absent": ["PASS"]}])
    expect("absent is case-insensitive, like words, and passes when the word is missing", ok, notes)

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + str(detail) + ')'}")
    print(f"\n{'the message fits whether anything was typed' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
