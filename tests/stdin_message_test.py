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
    # names other branches' whole lines, which must not be printed in that
    # run. Whole lines only: a correct answer's own wording, or a debug print,
    # may contain another branch's word or number without being refused.
    both = 'score = int(input())\nif score >= 50:\n    print("Pass")\nprint("Fail")'
    right = 'score = int(input())\nif score >= 50:\n    print("Pass")\nelse:\n    print("Fail")'
    runs = [{"typed": ["75"], "words": ["pass"], "absent": ["Fail"]},
            {"typed": ["45"], "words": ["fail"], "absent": ["Pass"]}]
    ok, notes = box_runner.check_stdin(both, runs)
    expect("a program that prints both branches is refused by absent",
           not ok and notes == ["with '75' typed in, your program also printed the line 'Fail', "
                                "which should not appear here"], notes)
    ok, notes = box_runner.check_stdin(right, runs)
    expect("a program that prints only the right branch passes", ok, notes)
    wordy = right.replace('"Fail"', '"Fail, you did not pass"')
    ok, notes = box_runner.check_stdin(wordy, runs)
    expect("another branch's word inside a longer line is not refused", ok, notes)
    zero = ('n = int(input())\nif n > 0:\n    print("positive")\nelif n < 0:\n    print("negative")\n'
            'else:\n    print("It\'s zero, not positive or negative.")')
    ok, notes = box_runner.check_stdin(zero, [{"typed": ["0"], "words": ["zero"], "absent": ["positive", "negative"]}])
    expect("a zero line that names the other branches passes", ok, notes)
    debug = 'price = 10\nprint("Full price:", price)\nprice -= 3\nprint(f"Price: ${price}")'
    ok, notes = box_runner.check_stdin(debug, [{"typed": [], "numbers": [7], "absent": ["Price: $10"]}])
    expect("a debug print holding another run's price passes", ok, notes)
    ok, notes = box_runner.check_stdin('print("  pass ")', [{"typed": [], "absent": ["Pass"]}])
    expect("absent with nothing typed: no mention of typing; lines compare stripped and case-insensitively",
           not ok and notes == ["your program also printed the line 'Pass', which should not appear here"], notes)

    # A loop that reads until a stop value keeps asking if the stop value
    # never comes, or comes and is missed. The check has typed every line it
    # had, so input() gets "" from then on: int("") is a ValueError about '',
    # and a loop that skips bad input never finishes. Neither says what
    # happened, so the message does.
    missed = 'n = int(input())\nwhile n > 100:\n    n = int(input())\nprint(n)'
    ok, notes = box_runner.check_stdin(missed, [{"typed": ["500", "300"], "numbers": [5]}])
    expect("a loop that asks past the typed lines says so, then names the error",
           not ok and notes[0].startswith("with '500', '300' typed in, your program asked for more input "
                                          "than was typed in, and then stopped: ValueError"), notes)
    skipping = ('while True:\n    try:\n        n = int(input())\n        break\n'
                '    except ValueError:\n        print("again")\nprint(n)')
    ok, notes = box_runner.check_stdin(skipping, [{"typed": ["x"], "numbers": [5]}], seconds=1)
    expect("a loop that asks past the typed lines forever says so",
           not ok and notes[0].startswith("with 'x' typed in, your program asked for more input "
                                          "than was typed in, and never finished"), notes)
    ok, notes = box_runner.check_stdin('print(int(input()) + 1)', [{"typed": [], "numbers": [5]}])
    expect("input() with nothing typed in: says no input is typed for this check",
           not ok and notes[0].startswith("your program asked for input, but this check types none in, "
                                          "and then stopped: ValueError"), notes)
    ok, notes = box_runner.check_stdin('print(int(input()))\nprint(1/0)', [{"typed": ["4"], "numbers": [4]}])
    expect("an error with every typed line used: no mention of asking for more",
           not ok and notes[0] == "with '4' typed in, your code stopped: ZeroDivisionError: division by zero", notes)

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + str(detail) + ')'}")
    print(f"\n{'the message fits whether anything was typed' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
