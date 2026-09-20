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


def run_box(source, seconds, namespace, check_every=2000, stdin=None):
    """exec source in namespace, raising KeyboardInterrupt if it runs too long.

    Time spent waiting at an input() prompt does not count against the limit.
    A learner thinking about what to type has not written a runaway loop.
    """
    deadline = time.monotonic() + seconds
    counter = 0

    queued = list(stdin) if stdin is not None else None

    def timed_input(prompt=""):
        nonlocal deadline
        if queued is not None:                      # checking: answer from a script
            return queued.pop(0) if queued else ""
        started = time.monotonic()
        try:
            return builtins.input(prompt)
        finally:
            deadline += time.monotonic() - started  # thinking time is not a runaway loop

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


def _capture(source, seconds, namespace, stdin=None):
    """Run source under the same guard, collecting whatever it printed."""
    import io

    buffer = io.StringIO()
    stdout, sys.stdout = sys.stdout, buffer
    try:
        run_box(source, seconds, namespace, stdin=stdin)
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


def _readable(n):
    """Show 555555.0 as 555555, not 5.55556e+06. A learner is looking at their
    own output here, so it has to read back the way they wrote it."""
    return str(int(n)) if n == int(n) and abs(n) < 1e15 else f"{n:g}"


def _numbers_in(text):
    import re

    return [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", text)]


def _in_order(found, wanted, match):
    """Is `wanted` a subsequence of `found`? Returns the first miss, or None."""
    i = 0
    for want in wanted:
        while i < len(found) and not match(found[i], want):
            i += 1
        if i == len(found):
            return want
        i += 1
    return None


def check_stdin(source, runs, seconds=5):
    """Check an answer that asks the user for input.

    The exercise says what to compute but not how to word it, so the wording is
    not tested. Fixed input goes in; the numbers or keywords the exercise does
    pin must come out, in order. "5 x 1 = 5" and a bare "5" both pass.

    Input is supplied without echoing it back, so a value that was typed in
    cannot be mistaken for a value the program worked out.
    """
    for attempt in runs:
        typed = list(attempt.get("typed", []))
        shown = ", ".join(repr(t) for t in typed) or "nothing"
        try:
            printed = _capture(source, seconds, {}, stdin=typed)
        except Exception as e:
            return False, [f"with {shown} typed in, your code stopped: "
                           f"{type(e).__name__}: {e}"]

        wanted = attempt.get("numbers")
        if wanted:
            found = _numbers_in(printed)
            miss = _in_order(found, wanted, lambda a, b: abs(a - b) < 0.005)
            if miss is not None:
                seen = ", ".join(_readable(n) for n in found[:10]) or "nothing"
                more = ", ..." if len(found) > 10 else ""
                return False, [f"with {shown} typed in, expected {_readable(miss)} among "
                               f"the numbers printed, in order. Got: {seen}{more}"]

        words = attempt.get("words")
        if words:
            lowered, at = printed.lower(), 0
            for word in words:
                found_at = lowered.find(word.lower(), at)
                if found_at < 0:
                    return False, [f"with {shown} typed in, expected to see "
                                   f"{word!r} in what you printed"]
                at = found_at + len(word)

        exact = attempt.get("contains")
        if exact and exact not in printed:
            return False, [f"with {shown} typed in, expected this line: {exact!r}"]

    return True, []
