"""Check that a declared crash is the crash that actually happens.

    python3 tests/raises_test.py

A box declared `"raises": "SyntaxError"` that actually raises NameError still
passed verify(): the box returned nonzero, and a nonzero return was all the
"raises on purpose" branch asked for. That lets a fix-the-bug exercise teach
the wrong error. build.raised_name() reads the exception name off a box's
own traceback, and verify() now requires it to match what was declared.
"""

import contextlib
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build                                                    # noqa: E402


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got, want))

    run = build.run_box_file("print(total)", "x")
    expect("the exception a box actually raises", build.raised_name(run.stderr), "NameError")

    run = build.run_box_file("print(1)", "x")
    expect("a box that raises nothing names no exception", build.raised_name(run.stderr), None)

    built = [("vol", [{"key": "p", "blocks": [("code", "print(total)")]}], [])]
    build.BOXES["p#0"] = {"raises": "SyntaxError"}
    out = io.StringIO()
    try:
        try:
            with contextlib.redirect_stdout(out):
                build.verify(built)
            refused = None
        except SystemExit as stop:
            refused = str(stop)
    finally:
        del build.BOXES["p#0"]
    expect("a box declared SyntaxError that raises NameError is refused",
           refused is not None and "declared SyntaxError, raised NameError" in out.getvalue(), True)

    bad = 0
    for label, got, want in results:
        bad += got != want
        print(f"  {'ok  ' if got == want else 'FAIL'}  {label}: {got!r}" +
              ("" if got == want else f" (expected {want!r})"))
    print(f"\n{'a declared crash is the declared kind' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
