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
import json
import sys
import time


class _Deadline:
    """Stops code that will not stop itself.

    A trace function is the one mechanism that lives inside the running program,
    so it is the only way to interrupt a loop on a thread that cannot be
    preempted. Time spent waiting at an input() prompt does not count: a learner
    thinking about what to type has not written a runaway loop.
    """

    def __init__(self, seconds, namespace, stdin=None, check_every=2000):
        self.seconds = seconds
        self.deadline = time.monotonic() + seconds
        self.namespace = namespace
        self.queued = list(stdin) if stdin is not None else None
        self.check_every = check_every
        self.counter = 0

    def _input(self, prompt=""):
        if self.queued is not None:                 # checking: answer from a script
            return self.queued.pop(0) if self.queued else ""
        started = time.monotonic()
        try:
            return builtins.input(prompt)
        finally:
            self.deadline += time.monotonic() - started

    def _guard(self, frame, event, arg):
        self.counter += 1
        if self.counter % self.check_every == 0 and time.monotonic() > self.deadline:
            raise KeyboardInterrupt(
                f"stopped after {self.seconds:g} seconds "
                f"- this looks like a loop that never ends"
            )
        return self._guard

    def __enter__(self):
        self.namespace.setdefault("__name__", "__main__")
        self.namespace["input"] = self._input
        sys.settrace(self._guard)
        return self

    def __exit__(self, *exc):
        sys.settrace(None)
        self.namespace.pop("input", None)
        return False


def run_box(source, seconds, namespace, check_every=2000, stdin=None):
    """exec source in namespace, raising KeyboardInterrupt if it runs too long."""
    with _Deadline(seconds, namespace, stdin, check_every):
        exec(compile(source, "<box>", "exec"), namespace)


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


def from_json(text):
    """Parse a check's data here rather than letting the browser convert it.

    The page hands a check over as its original JSON text, because the
    JavaScript conversion loses two things that matter. JSON's 61.0 is an
    ordinary JavaScript number and arrives as a Python int, so an answer that
    correctly prints "61.0" is marked wrong. And JSON's null arrives as a
    JavaScript null, which is not None, so a case expecting None can never
    match and the check rejects every answer including the right one.

    json.loads has neither problem, and both faults are invisible from
    CPython, where the same file parses correctly.
    """
    return json.loads(text)


def check_function(source, name, cases, seconds=5):
    """Check an answer by calling the function it defines.

    The exercise names the function and its parameters, so that is the contract.
    Nothing here looks at formatting, variable names, comments or stray prints --
    two correct answers written in different styles both pass.
    """
    namespace = {}
    try:
        _capture(source, seconds, namespace)
    except KeyboardInterrupt as e:
        return False, [f"your code never finished -- {e}"]
    except Exception as e:
        return False, [f"your code did not run -- {type(e).__name__}: {e}"]

    function = namespace.get(name)
    if not callable(function):
        return False, [f"no function called {name}() was defined yet"]

    # Calling the function is the part that can loop forever -- `while True` in
    # a body is the canonical beginner mistake in is_prime and binary_search --
    # so the call goes INSIDE the deadline. Running the source under the guard
    # and then calling outside it only protects the definition, which cannot
    # loop.
    failures = []
    try:
        with _Deadline(seconds, namespace):
            for args, expected in cases:
                shown = ", ".join(repr(a) for a in args)
                try:
                    got = function(*args)
                except Exception as e:
                    failures.append(f"{name}({shown}) raised {type(e).__name__}: {e}")
                    continue
                if got != expected:
                    failures.append(f"{name}({shown}) gave {got!r}, expected {expected!r}")
    except KeyboardInterrupt as e:
        return False, [f"{name}() never finished -- {e}"]
    return not failures, failures


def check_output(source, expected, seconds=5):
    """Check an answer by what it prints. Only honest where the exercise pins
    the output completely -- otherwise it fails correct answers."""
    try:
        printed = _capture(source, seconds, {})
    except KeyboardInterrupt as e:
        return False, [f"your code never finished -- {e}"]
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
    against what the course's own code actually prints."""
    try:
        actual = _capture(book_code, seconds, {})
    except BaseException as e:
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


def trace_rows(source, names, max_steps=200):
    """Run `source` and record, after every executed line, the repr of each
    name in `names` ("" for a name not yet set). Output is swallowed.

    The expected answer to a trace table, worked out by Python itself so it can
    never disagree with what the program does.
    """
    import contextlib
    import io

    code = compile(source, "<trace>", "exec")
    namespace = {}
    steps = []

    def snapshot():
        return [repr(namespace[n]) if n in namespace else "" for n in names]

    def local(frame, event, arg):
        if frame.f_code is code and event == "line":
            if len(steps) >= max_steps:
                raise RuntimeError(f"traced more than {max_steps} lines")
            steps.append((frame.f_lineno, snapshot()))
        return local

    def start(frame, event, arg):
        return local if frame.f_code is code else None

    with contextlib.redirect_stdout(io.StringIO()):
        sys.settrace(start)
        try:
            exec(code, namespace)
        finally:
            sys.settrace(None)
    return [(line, steps[i + 1][1] if i + 1 < len(steps) else snapshot())
            for i, (line, _) in enumerate(steps)]


def _same_value(entered, expected):
    """Does what the learner wrote mean the value Python holds? By value, not
    spelling: quotes optional around text, 3 for 3.0, "-" or blank for unset.
    True and False are their own kind of value, so 1 is not True."""
    import ast

    entered = entered.strip()
    if expected == "":
        return entered in ("", "-")
    try:
        value = ast.literal_eval(expected)
    except Exception:
        return entered == expected       # not a literal: only its exact repr matches
    try:
        got = ast.literal_eval(entered)
    except Exception:
        return isinstance(value, str) and entered == value
    if isinstance(value, bool) or isinstance(got, bool):
        return type(got) is type(value) and got == value
    return got == value


def _kind(text):
    """What kind of value `text` reads as, in the course's words."""
    import ast

    try:
        value = ast.literal_eval(text)
    except Exception:
        return "text"                    # an unquoted word reads as text
    if isinstance(value, bool):
        return "True or False"
    if isinstance(value, (int, float)):
        return "a number"
    return "text" if isinstance(value, str) else f"a {type(value).__name__}"


def check_trace(source, payload):
    """Check a trace table. `payload` is JSON text: {"names", "entered", "lines"}.

    "lines" are the rows' line numbers as the build's Python traced them. A
    different Python can step through the same program differently, and then
    the table on the page cannot be checked here: say so, rather than mark a
    correct table wrong.
    """
    data = json.loads(payload)
    names, entered = data["names"], data["entered"]
    try:
        rows = trace_rows(source, names)
    except BaseException as e:
        return False, [f"the program itself failed: {e}"]
    if data.get("lines") and [line for line, _ in rows] != data["lines"]:
        return False, ["this table was made on a different version of Python than the one in "
                       "this page, so it cannot be checked here; the course needs fixing, not your answer"]
    if len(entered) != len(rows):
        return False, [f"the table has {len(rows)} rows; {len(entered)} were filled in"]
    for (line, want), got in zip(rows, entered):
        for name, w, g in zip(names, want, got):
            if not _same_value(g, w):
                shown = w if w else "not set yet"
                note = f"line {line}, {name}: you wrote {g.strip() or 'nothing'!r}, it is {shown}"
                if g.strip() and w and _kind(g.strip()) != _kind(w):
                    note += f" (you wrote {_kind(g.strip())}; it is {_kind(w)})"
                return False, [note]
    return True, []

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
    pin must come out, in order. "5 x 1 = 5" and a bare "5" both pass. Words
    listed as "absent" (another branch's message) must not come out at all.

    Input is supplied without echoing it back, so a value that was typed in
    cannot be mistaken for a value the program worked out.
    """
    for attempt in runs:
        typed = list(attempt.get("typed", []))
        shown = ", ".join(repr(t) for t in typed)
        lead = f"with {shown} typed in, " if typed else ""
        try:
            printed = _capture(source, seconds, {}, stdin=typed)
        except KeyboardInterrupt as e:
            return False, [f"{lead}your code never finished -- {e}"]
        except Exception as e:
            return False, [f"{lead}your code stopped: "
                           f"{type(e).__name__}: {e}"]

        wanted = attempt.get("numbers")
        if wanted:
            found = _numbers_in(printed)
            miss = _in_order(found, wanted, lambda a, b: abs(a - b) < 0.005)
            if miss is not None:
                seen = ", ".join(_readable(n) for n in found[:10]) or "nothing"
                more = ", ..." if len(found) > 10 else ""
                return False, [f"{lead}expected {_readable(miss)} among "
                               f"the numbers printed, in order. Got: {seen}{more}"]

        words = attempt.get("words")
        if words:
            lowered, at = printed.lower(), 0
            for word in words:
                found_at = lowered.find(word.lower(), at)
                if found_at < 0:
                    return False, [f"{lead}expected to see "
                                   f"{word!r} in what you printed"]
                at = found_at + len(word)

        exact = attempt.get("contains")
        if exact and exact not in printed:
            return False, [f"{lead}expected this line: {exact!r}"]

        # A decision's other branches: words that must not appear in this
        # run, so printing every branch's message unconditionally fails.
        for word in attempt.get("absent", []):
            if word.lower() in printed.lower():
                return False, [f"{lead}your program also printed {word!r}, "
                               f"which should not appear here"]

    return True, []


def repl_run(source, seconds, namespace):
    """Run one scratchpad entry, the way an interactive interpreter would.

    Returns (text, incomplete). `incomplete` means the entry opened a block or
    a bracket and the console should keep taking lines instead of running it.

    A bare expression shows its value here, because that is what a REPL is --
    and deliberately NOT in the code boxes, where a file is being modeled and
    `2 + 3` on its own line correctly prints nothing.
    """
    import ast
    import codeop

    try:
        if codeop.compile_command(source, "<scratchpad>", "exec") is None:
            return "", True
    except (SyntaxError, ValueError, OverflowError):
        pass                       # a real error: let the compile below report it

    with _Deadline(seconds, namespace):
        tree = ast.parse(source, "<scratchpad>", "exec")
        last = tree.body[-1] if tree.body else None

        if isinstance(last, ast.Expr):
            head = ast.Module(body=tree.body[:-1], type_ignores=[])
            exec(compile(head, "<scratchpad>", "exec"), namespace)
            value = eval(compile(ast.Expression(last.value), "<scratchpad>", "eval"),
                         namespace)
            namespace["_"] = value
            return ("" if value is None else repr(value)), False

        exec(compile(tree, "<scratchpad>", "exec"), namespace)
        return "", False
