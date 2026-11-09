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
import re
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

    # A fix-the-bug box can start from a loop that never ends. The page's
    # guard stops it with KeyboardInterrupt; verify() runs it under that same
    # guard instead of waiting out its 30-second limit and giving up.
    def verify_one(code, declared):
        built = [("vol", [{"key": "p", "blocks": [("code", code)]}], [])]
        build.BOXES["p#0"] = declared
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                build.verify(built)
            return None, out.getvalue()
        except SystemExit as stop:
            return str(stop), out.getvalue()
        finally:
            del build.BOXES["p#0"]

    forever = "count = 1\nwhile count <= 3:\n    total = count"
    refused, printed = verify_one(forever, {"raises": "KeyboardInterrupt"})
    expect("a loop that never ends, declared KeyboardInterrupt, raises on purpose",
           refused is None and re.search(r"raises on purpose\s+1\b", printed) is not None, True)
    refused, printed = verify_one("print(1)", {"raises": "KeyboardInterrupt"})
    expect("a box declared KeyboardInterrupt that finishes is refused",
           refused is not None and "declared KeyboardInterrupt, raised None" in printed, True)

    bad = 0
    for label, got, want in results:
        bad += got != want
        print(f"  {'ok  ' if got == want else 'FAIL'}  {label}: {got!r}" +
              ("" if got == want else f" (expected {want!r})"))
    print(f"\n{'a declared crash is the declared kind' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
