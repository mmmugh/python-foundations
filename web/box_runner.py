"""Runs one code box, and stops it if it runs away.

Loaded into Pyodide once at startup and called for every Run. Kept as Python
rather than a string inside app.js so it can be read and tested on its own.

A beginner's `while True:` with no `break` freezes the tab, and on the main
thread there is no way to interrupt it from outside: JavaScript runs to
completion, so no Stop button can ever be clicked. A trace function is the one
mechanism that lives *inside* the running program and can stop it.

It cannot stop a loop that never returns to Python bytecode -- `sum(range(10**10))`
runs to the end no matter what this does.
"""

import builtins
import sys
import time


def run_box(source, seconds, namespace, check_every=2000):
    """exec source in namespace, raising KeyboardInterrupt if it runs too long.

    Time spent waiting at an input() prompt does not count against the limit.
    A learner thinking about what to type has not written a runaway loop.
    """
    deadline = time.monotonic() + seconds
    counter = 0

    def timed_input(prompt=""):
        nonlocal deadline
        started = time.monotonic()
        try:
            return builtins.input(prompt)
        finally:
            deadline += time.monotonic() - started

    def guard(frame, event, arg):
        nonlocal counter
        counter += 1
        if counter % check_every == 0 and time.monotonic() > deadline:
            raise KeyboardInterrupt(
                f"stopped after {seconds:g} seconds "
                f"- this looks like a loop that never ends"
            )
        return guard

    namespace["__name__"] = "__main__"
    namespace["input"] = timed_input

    sys.settrace(guard)
    try:
        exec(compile(source, "<box>", "exec"), namespace)
    finally:
        sys.settrace(None)
        namespace.pop("input", None)
