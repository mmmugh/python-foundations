"""A runaway loop inside a learner's function must stop, not hang the tab.

The Check button was calling the learner's function AFTER the deadline's
context manager had exited and run sys.settrace(None), so the guard protected
only the function's definition -- which cannot loop -- and not the call, which
is where `while True` in is_prime or a binary_search that never moves lo/hi
actually loops. In a browser there is no watchdog and no Stop button, so it
hung the tab until a forced reload.

    python3 tests/regression_check_function.py
"""

import signal
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "web"))
import box_runner  # noqa: E402

CASES = [
    ("is_even, infinite loop in the body",
     "def is_even(n):\n    while True:\n        pass\n", "is_even", [[[4], True]]),
    ("binary_search, lo and hi never move",
     "def binary_search(items, target):\n    lo, hi = 0, len(items)\n"
     "    while lo < hi:\n        mid = (lo + hi) // 2\n    return lo\n",
     "binary_search", [[[[1, 3, 5], 3], 1]]),
    ("a correct answer still passes",
     "def is_even(n):\n    return n % 2 == 0\n", "is_even", [[[4], True], [[7], False]]),
]


def watchdog(signum, frame):
    raise TimeoutError("the guard did not stop it")


def main():
    signal.signal(signal.SIGALRM, watchdog)
    failed = 0
    for label, code, name, cases in CASES:
        signal.alarm(8)
        try:
            passed, notes = box_runner.check_function(code, name, cases, seconds=2)
            expected = "correct" in label
            ok = passed is expected
            print(f"  {'ok  ' if ok else 'FAIL'} {label:<38} {notes[0][:46] if notes else 'passed'}")
            failed += not ok
        except TimeoutError:
            print(f"  FAIL {label:<38} STILL HANGING past the deadline")
            failed += 1
        finally:
            signal.alarm(0)
    if failed:
        sys.exit(f"{failed} case(s) failed")
    print("  a runaway loop inside a checked answer is stopped")


if __name__ == "__main__":
    main()
