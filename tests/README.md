# Verification harness

`python3 build.py --check` runs every example under the local CPython. That is
not the interpreter the course actually runs on. These harnesses run it under
real Pyodide — CPython 3.14 compiled to WebAssembly — which is what a reader's
browser executes.

    cd tests && npm install
    node verify2.mjs           every code box, and the runaway-loop guard
    node validate_shipped.mjs  all 45 exercise checks, via web/box_runner.py
    node validate_stdin.mjs    the input()-driven checks
    node validate_projects.mjs the four interactive chapter projects
    node repl_test.mjs         the scratchpad REPL

Each check is exercised three ways: it must pass a correct answer, pass a
second correct answer written in a different style, and fail a realistic
mistake. A check that cannot tell those apart is worse than no check, and this
is how that is caught — it found two such checks when they were written
(`count_vowels` had no test word containing a "u"; `invert`'s expected value
could not survive JSON, which turns integer dict keys into strings).

`reference_solutions.py`, `stdin_answers.py` and `project_answers.py` hold
those correct-and-incorrect variants. They are test fixtures, not course
content, and are deliberately not the worked solutions in
`content/_solutions.md`.

The pinned Pyodide is 314.0.6 rather than the 314.0.7 the site loads, because
npm here is restricted to packages published before 2026-09-11. Same CPython.
