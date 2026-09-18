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


def _capture(source, seconds, namespace):
    """Run source under the same guard, collecting whatever it printed."""
    import io

    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        run_box(source, seconds, namespace)
    finally:
        sys.stdout = stdout
    return buffer.getvalue()


def check_function(source, name, cases, seconds=5):
    """Check an answer by calling the function it defines.

    The exercise names the function and its parameters, so that is the contract.
    Nothing here looks at formatting, variable names, comments or stray prints --
    two correct answers written in different styles both pass.
    """
    namespace = {}
    try:
        _capture(source, seconds, namespace)
    except Exception as e:
        return False, [f"your code did not run -- {type(e).__name__}: {e}"]

    function = namespace.get(name)
    if not callable(function):
        return False, [f"no function called {name}() was defined yet"]

    failures = []
    for args, expected in cases:
        shown = ", ".join(repr(a) for a in args)
        try:
            got = function(*args)
        except Exception as e:
            failures.append(f"{name}({shown}) raised {type(e).__name__}: {e}")
            continue
        if got != expected:
            failures.append(f"{name}({shown}) gave {got!r}, expected {expected!r}")
    return not failures, failures


def check_output(source, expected, seconds=5):
    """Check an answer by what it prints. Only honest where the exercise pins
    the output completely -- otherwise it fails correct answers."""
    try:
        printed = _capture(source, seconds, {})
    except Exception as e:
        return False, [f"your code did not run -- {type(e).__name__}: {e}"]

    if printed.strip() != expected.strip():
        got = printed.strip().split("\n")
        want = expected.strip().split("\n")
        for n, (a, b) in enumerate(zip(got, want), 1):
            if a != b:
                return False, [f"line {n} printed {a!r}, expected {b!r}"]
        if len(got) != len(want):
            return False, [f"printed {len(got)} lines, expected {len(want)}"]
    return True, []


def check_prediction(book_code, prediction, seconds=5):
    """For 'predict the output' items: compare what the learner wrote down
    against what the book's own code actually prints."""
    try:
        actual = _capture(book_code, seconds, {})
    except Exception as e:
        return False, [f"the example itself failed: {e}"], ""

    def tidy(text):
        return [line.rstrip() for line in text.strip("\n").split("\n")]

    got, want = tidy(prediction), tidy(actual)
    if got == want:
        return True, [], actual
    for n, (a, b) in enumerate(zip(got, want), 1):
        if a != b:
            return False, [f"line {n}: you said {a!r}, it prints {b!r}"], actual
    return False, [f"you wrote {len(got)} lines, it prints {len(want)}"], actual
