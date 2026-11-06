"""Check the trace-table check: the expected table comes from running the code.

    python3 tests/trace_test.py

A trace table asks for each variable's value after each line. The expected
values are never typed in by hand: box_runner works them out by running the
program, so the table cannot disagree with Python. And the learner's answer
is compared by value, not by spelling: 'Ada', "Ada" and Ada are the same
string, 3 is 3.0, and a blank or "-" means "not set yet".
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "web"))
import box_runner                                               # noqa: E402

PROGRAM = "price = 12\ncount = 3\nprice = price + count\nname = 'Ada'\n"
NAMES = ["price", "count", "name"]


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    rows = box_runner.trace_rows(PROGRAM, NAMES)
    expect("one row per executed line", [line for line, _ in rows], [1, 2, 3, 4])
    expect("values after each line", [cells for _, cells in rows],
           [["12", "", ""], ["12", "3", ""], ["15", "3", ""], ["15", "3", "'Ada'"]])

    def check(entered):
        return box_runner.check_trace(PROGRAM, json.dumps({"names": NAMES, "entered": entered}))

    right = [["12", "", ""], ["12", "3", "-"], ["15", "3", ""], ["15.0", "3", "Ada"]]
    expect("a correct table in a different style passes", check(right)[0], True)
    expect("double quotes are as good as single", check(
        [["12", "", ""], ["12", "3", ""], ["15", "3", ""], ["15", "3", '"Ada"']])[0], True)

    wrong = [["12", "", ""], ["12", "3", ""], ["12", "3", ""], ["15", "3", "Ada"]]
    ok, notes = check(wrong)
    expect("a wrong cell fails", ok, False)
    expect("and is named by line and variable", "line 3" in notes[0] and "price" in notes[0], True)
    expect("a missing row fails, not crashes", check(right[:2])[0], False)


    # Found in review. A value whose repr is not a literal must not crash the
    # check (the page's Check button would hang); True is not 1, because the
    # lesson on kinds of value exists to teach exactly that; a wrong kind is
    # said in words; and a table built on another Python is refused plainly.
    def check_src(source, names, entered, **extra):
        return box_runner.check_trace(source, json.dumps({"names": names, "entered": entered, **extra}))

    try:
        outcome = check_src("r = range(3)\n", ["r"], [["range(0, 3)"]])
        expect("a value that is not a literal gives a verdict, not a crash", isinstance(outcome, tuple), True)
    except Exception as e:
        expect("a value that is not a literal gives a verdict, not a crash", repr(e), "a tuple")
    expect("1 is not True", check_src("ok = 5 > 3\n", ["ok"], [["1"]])[0], False)
    expect("True is True", check_src("ok = 5 > 3\n", ["ok"], [["True"]])[0], True)
    expect("True is not 1", check_src("n = 1\n", ["n"], [["True"]])[0], False)
    ok, notes = check_src("s = '3'\n", ["s"], [["3"]])
    expect("a number written for text says so", not ok and "text" in notes[0] and "number" in notes[0], True)
    ok, notes = check_src(PROGRAM, NAMES, right, lines=[1, 2, 3, 3, 4])
    expect("rows from another Python are refused plainly", not ok and "version of Python" in notes[0], True)
    expect("matching rows are accepted", check_src(PROGRAM, NAMES, right, lines=[1, 2, 3, 4])[0], True)

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'trace tables check by value' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
