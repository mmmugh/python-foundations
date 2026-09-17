# Scoping Report: Python Foundations → Interactive Web App

Prepared for an engineer with no prior exposure to this repo. It covers what exists today, what
was verified by actually running the code, what is missing, and the runtime-environment decision
for turning this into a web app with instruction text and REPL-style coding boxes.

## What this project is

This repo is a code bundle for a book called *Python Foundations: A First Course in Programming*
— every worked example and end-of-chapter project from the book, twelve chapters covering a
standard first-semester CS1 sequence (print/types → operators → conditionals → loops → functions →
lists → strings → dicts/sets → tuples/records → search & sort → recursion). It ships as 24 flat
`.py` files (`examples/ch01…ch12` and `projects/ch01…ch12`) plus a `main.py` menu launcher meant to
run under Replit — there is no book text, no lesson prose, and no web app here yet. The task this
report scopes is turning that bundle into a self-study web app: instructional writing next to each
concept, and runnable/editable code boxes in the browser.

## Verified state of the code

Every one of the 24 files was actually executed (not just read), with stdin closed (`< /dev/null`)
so any hidden blocking call would surface. Results:

| Result | Count | Which files |
|---|---|---|
| Runs clean, no input needed | 19 / 24 | all 12 `examples/`, plus `projects/` ch01, ch07–ch12 |
| Needs stdin (blocks / errors under `/dev/null`) | 5 / 24 | `projects/` ch02, ch03, ch04, ch05, ch06 |
| Real bugs found | 0 | — |

The 5 "failures" are not bugs. Each is `EOFError: EOF when reading a line` from an `input()` call
that is never reached because stdin was deliberately closed for the test — the same call would work
fine against a real terminal or a real browser prompt. All 5 call `input()` unguarded, either at
module scope (ch02, ch03, ch04) or inside `main()`/a loop that `main()` invokes unconditionally with
no `if __name__` guard (ch05, ch06) — so in every case `input()` fires as soon as the file is run.

**Python-correctness notes** (none are bugs in the sense of "wrong output"):

- `examples/ch04_making_decisions.py` (lines 47–57) contains an intentionally broken `elif` chain,
  explicitly commented `# Do not copy this` — it runs and prints a value, but the value is wrong on
  purpose, as a teaching device. Not a defect.
- `examples/ch09_dictionaries_and_sets.py`'s output depends on dict insertion order, which became a
  *language guarantee* only in Python 3.7 — the README states a 3.6 floor. On every real CPython
  3.7–3.12 (including the 3.12.13 interpreter used for this verification) the output is identical
  and correct; on a hypothetical 3.6 interpreter it would still almost certainly match (CPython 3.6
  already had this behavior as an implementation detail), but it is not *spec-guaranteed* below 3.7.
  Worth a one-line footnote in the app; not worth chasing further since the target runtime (Pyodide,
  see below) is a modern CPython regardless.
- `projects/ch11_measuring_algorithms.py` calls `random.shuffle()` with no seed, so its printed
  comparison counts vary between runs. Not a bug, but relevant to any "checkable answer" feature —
  see the determinism note in the runtime section below.

**README claim check.** README.md makes two specific, checkable claims. Both hold up against the
verified data — the code does **not** contradict the README:

1. *"Examples that ask for typed input are wrapped in functions at the bottom of their file, so the
   file runs start to finish without stopping."* — Confirmed for all three affected files
   (`examples/ch02`, `ch04`, `ch05`): the `input()`-calling functions are defined but never called;
   only a commented-out call sits at the bottom (e.g. `# greeting_demo()`). All 12 `examples/` files
   ran to completion with zero blocking, exactly as claimed.
2. *"Every example in this bundle was run and its output checked against what the book prints."* —
   This claim is scoped to `examples/` (the surrounding text is specifically about the
   `examples/` folder). All 12 ran clean with output that was hand-checked against what the source
   code itself predicts (e.g. `26.2*1.609` prints `42.1558`; `2**3**2` right-associates to `512`).
   No mismatch found. The README separately and correctly describes `projects/` as "ready to run"
   and says projects 2–6 "ask you to type something" — it never claims those run without stdin, so
   the 5 projects that block on `input()` are exactly what the README describes, not a contradiction
   of it.

## The chapter spine

For `examples/`, the only structure inside each file is a run of `# --- Section Name ---` header
comments — no prose follows them, just code. This is what lesson content has to be organized
around. `projects/` files have **zero** section headers each — one continuous script per project.

| Ch. | `examples/` file | Section headers (in order) | `projects/` file | Needs input? |
|---|---|---|---|---|
| 01 | ch01_first_programs.py | Output with print() · One line at a time · Printing numbers · Comments · Try It #4 | ch01_receipt.py | no |
| 02 | ch02_variables_and_types.py | Variables · The four basic types · Naming variables · Try It #4 · The interactive examples | ch02_receipt_improved.py | **yes** |
| 03 | ch03_expressions_and_operators.py | Modulo and floor division · Order of operations · Why 0.1 + 0.2 is not 0.3 · Rounding and formatting · String operators · Comparison and boolean operators · Shorthand assignment · Try It #4 | ch03_change_maker.py | **yes** |
| 04 | ch04_making_decisions.py | Anatomy of an if · elif chains · Nesting · Try It #5 · The interactive examples | ch04_ticket_kiosk.py | **yes** |
| 05 | ch05_repetition.py | The while loop · The for loop and range() · Looping over a string · The accumulator pattern · continue · Try It #7 · The interactive examples | ch05_guessing_game.py | **yes** (uses `random`) |
| 06 | ch06_functions.py | Defining and calling · Parameters · Return values · Scope · Docstrings · Decomposition: Ch.4's kiosk, rewritten · Try It #6 | ch06_grade_calculator.py | **yes** |
| 07 | ch07_lists.py | Creating lists · Indexing · Lists are mutable · Slicing · List methods · Useful built-ins · Looping over lists · Nested lists · A name is not a copy | ch07_gradebook.py | no |
| 08 | ch08_strings_as_data.py | Strings are sequences · Strings are immutable · Chaining methods · Comparing text safely · split() and join() · Processing character by character · A worked example: palindromes · Escape sequences | ch08_text_analyzer.py | no |
| 09 | ch09_dictionaries_and_sets.py | Creating and reading · Adding, changing, removing · Missing keys · Looping · Built-ins on values · Counting: the killer application · Nested dictionaries · Sets | ch09_poll_counter.py | no |
| 10 | ch10_tuples_and_records.py | Tuples · A tuple can be a dictionary key · Unpacking · Records: lists of dictionaries | ch10_inventory.py | no |
| 11 | ch11_searching_and_sorting.py | Linear search · Binary search · Selection sort · Bubble sort · What Python actually does | ch11_measuring_algorithms.py | no (uses `random`, unseeded) |
| 12 | ch12_recursion.py | Factorial, two ways · Following the calls · More examples · When recursion goes wrong: Fibonacci · Binary search, recursively | ch12_student_records.py | no |

76 section headers total across the 12 `examples/` files (per-file counts: 5, 5, 8, 5, 7, 7, 9, 8,
8, 4, 5, 5). Deliberate cross-chapter callbacks exist and are currently unlabeled: ch06 explicitly
redecomposes ch04's ticket-kiosk logic into functions; ch10's "records: lists of dictionaries"
pattern is what `projects/ch10_inventory.py` and `projects/ch12_student_records.py` build on; ch11's
iterative binary search is revisited recursively in ch12 with the same variable names. None of this
is explained anywhere in the code — it has to be written.

## The central gap: there is no instructional prose in this repo

Every file was read in full, along with README.md and main.py. The only text present anywhere is:
one-to-four-line module docstrings, one-line function docstrings, and the 76 bare section-header
comments above — never followed by an explanation, only by code. `git log` shows exactly one commit
(`chore: import the Python Foundations code bundle verbatim from iCloud`), so there's no earlier
draft or companion doc to recover prose from. README.md says outright that the teaching text lives
in the external book this bundle was extracted from.

Sizing this honestly: the unit of writing is not "12 chapters," it's closer to **~100 discrete
passages** — 76 section-header explanations, 12 project walkthroughs (each project is one
unbroken script with no internal seams, so a walkthrough has to be authored as continuous prose, or
the web layer has to invent its own segmentation), and 12 chapter intros. On top of that, exercises
are thin: exactly 6 "Try It" markers exist in the whole bundle (`examples/ch01` through `ch06` only,
numbered #4, #4, #4, #5, #7, #6 — non-sequential, implying the book has more that didn't make it
into this bundle), all of the same "predict the output by hand" style, none in `ch07`–`ch12`, and
none in any project. A self-study site with checkable exercises needs new exercises written for
half the chapters and all twelve projects.

This means the real scope decision is **where the prose comes from**, and it has to be made before
an engineering plan is written:

- **(a) License/obtain the actual book text** and adapt it against these 76 headers and 12 project
  scripts, checked for accuracy against the source, or
- **(b) Treat this as original authoring**: write new chapter intros, section explanations, project
  walkthroughs, and an expanded exercise set from scratch, using this code purely as the worked
  example backbone.

These two paths differ by an order of magnitude in effort, and (a) carries a copyright question
that has to be resolved (is the book's text owned/licensed for this use?) before any of it is
copied into a public web app. The engineering half described below — sandboxing, REPL boxes,
`input()` handling, output checking — is comparatively well-bounded and well-understood by
comparison. The honest framing for staffing this: **the writing is the project; the runtime is a
solved problem.**

## Runtime: how the code actually executes in the browser

**The `input()` fault line.** Five projects need typed input, but they are not interchangeable.
ch02, ch03, ch04 run a fixed, linear sequence of `input()` calls with no branching on what was
typed — they'd compute the right answer even from a pre-supplied blob of stdin. ch05 (guessing
game) and ch06 (grade calculator) are different: ch05 loops an unknown number of times based on
"too low"/"too high" feedback, and ch06 retries on invalid input via `while True`. These two
specifically need a live, adaptive prompt-then-respond loop — a batch "submit code + stdin, get
stdout back" sandbox cannot deliver the intended experience for them without much heavier
infrastructure (a persistent PTY/websocket bridge per session, closer to what Replit runs).

That fault line, plus a fidelity requirement (this bundle needs real `random`, real f-strings, and
output matching what a real Python book describes) and a maintenance requirement (single author,
low ongoing infra), points at one option:

| Option | Real interactive `input()`? | stdlib/`random`/f-string fidelity | Offline? | Ongoing infra |
|---|---|---|---|---|
| **Pyodide** (CPython → WASM, in-browser) | **Yes, free** — default stdin is `prompt()`, no extra code, as long as it runs on the main thread | Exact — it's real CPython (currently 3.14 under the hood) | Yes, with a small caching layer added | None — static site |
| Server sandbox (Judge0 / Piston-style) | No — these are batch submit-code/stdin, judge-style APIs; breaks ch05/ch06's adaptive loop without building a real terminal backend | Exact (real CPython on the server) | **No** — by construction, every run is a network round trip | Server to host, secure, and pay for indefinitely |
| Skulpt / Runestone ActiveCode | Yes, and with the nicest UX (a styled in-page prompt, not a native dialog) | **Not exact** — Skulpt's own README says Python 3 support is incomplete, and lists `random` as "(partial)" and `collections` as not yet implemented | Yes | None — static site |

**Recommendation: Pyodide, run on the main thread, using its default `input()` behavior.** It's the
only option that is simultaneously real CPython (no fidelity risk against the book), genuinely
interactive with zero extra plumbing, and fully static — no backend, no hosting bill, no security
surface to maintain. Build it as a plain static site (GitHub Pages, Netlify, etc.), load Pyodide
from a pinned CDN version, let `input()` use its default `prompt()` dialog for v1, and persist
learner progress to `localStorage`.

Costs worth knowing going in, not discovering later:

- **First-load size is ~6 MB compressed** (measured directly against the CDN: `pyodide.asm.wasm` is
  3.4 MB brotli-compressed, `python_stdlib.zip` is 2.5 MB) — not the "200+ MB" figure Pyodide's own
  docs cite, which describes the full scientific-stack distribution (numpy/scipy/pandas) this
  project never touches.
- **Offline isn't automatic.** The CDN sends a one-year cache header, so repeat visits reuse the
  cached assets, but true offline-on-first-load behavior needs a deliberately added service worker
  (a known pattern, used by JupyterLite for exactly this) — it's opt-in work, not a default.
- **Main-thread execution is what makes `input()` free, and it's also the risk.** A learner-edited
  program with an accidental infinite loop (a mistyped `while True:` with no `break` — a plausible
  beginner mistake in an editable code box) will hang the tab with no built-in interrupt; the only
  recovery is reloading and losing anything unsaved. The fix (running in a Web Worker) reopens the
  `input()` problem, requiring either cross-origin-isolation headers plus `SharedArrayBuffer`, or the
  newer JSPI ("stack switching") mechanism — which is real but not yet universally supported
  (Chrome has had it since May 2025; Safari only landed it around Safari 26/27, dated Feb 2026;
  Firefox's status was contradictory across sources I checked). Mitigate for v1 with autosave-on-edit
  (not only on successful run), and revisit a Worker+JSPI setup later only if hangs prove to be a
  real problem in practice.
- **Determinism for checkable answers.** `examples/ch09_dictionaries_and_sets.py` prints raw sets
  directly, and set iteration order can vary across processes (Python randomizes string hashing by
  default); `projects/ch11_measuring_algorithms.py`'s unseeded `random.shuffle()` makes its printed
  comparison counts vary run to run by design. Any exact-stdout-match exercise checker needs to
  special-case both — an order-insensitive comparison for the set examples, or a `random.seed()`
  call for the sort-counting project.
- **Progress persistence is the same problem regardless of runtime choice** — `localStorage` for a
  no-backend static site either way. This is one more point against a server-executed sandbox: it
  would need real backend infrastructure (accounts or at least a database) just to persist progress,
  on top of everything else it costs.
- **`main.py` is not something to port.** Its only job is print a menu, `input()` a choice, and
  `subprocess.run()` the chosen file, then loop. No `examples/` or `projects/` file touches
  `subprocess`, `os`, `sys`, or `argv` (confirmed by grep). Ordinary web navigation — a sidebar or
  router plus a per-box "Run" button — replaces `main.py` wholesale; there's nothing in it to adapt.

## Open questions for the author

These are decisions a fresh engineer cannot make alone — each one materially changes scope, cost,
or legal exposure:

1. **Where does the instructional prose come from?** License/obtain the book's actual text and
   adapt it against the 76 section headers and 12 project scripts, or write original prose from
   scratch using this code as the worked-example backbone? This is the single biggest scope lever
   in the whole project (see "The central gap" above) and has a copyright dimension if the book
   text itself isn't owned/licensed for reuse in a public web app.
2. **How big should the exercise set be?** The bundle ships exactly 6 "predict the output"
   Try-Its, confined to chapters 1–6, with none in chapters 7–12 or in any of the 12 projects. Is
   the target "port the 6 that exist" or "author a fuller exercise set across all 12 chapters and
   projects," and should exercises stay predict-the-output only or add write-your-own-code tasks?
3. **Is a native `prompt()` dialog acceptable for `input()` in v1**, or is a styled in-page input
   box a launch requirement? The former is free (Pyodide's default); the latter needs JSPI or a
   Worker+`SharedArrayBuffer` setup, both real engineering, and JSPI's cross-browser support is
   still settling as of this research (confirmed solid only on Chrome).
4. **How much should v1 protect against a learner's infinite loop hanging the tab?** Options range
   from "accept the risk, ship an autosave and a 'reload if stuck' note" (cheap, matches the
   recommended main-thread setup) to "move execution to a Worker" (safer, but reopens the `input()`
   problem and adds real complexity). Which is acceptable for launch?
5. **Should the exceptions gap be patched or left as-is?** `try`/`except` is taught exactly once,
   ad hoc, in `examples/ch04_making_decisions.py`, and never revisited — even though chapters 7–10
   go on to show commented-out lines that deliberately raise `IndexError`/`KeyError`/`TypeError`
   ("uncomment to see it") without ever pairing them with the handling pattern taught two chapters
   earlier. Is this the source book's own pedagogical choice to preserve as-is, or worth new content
   to close?
6. **Is offline-first (usable with zero network on a first visit) a real launch requirement**, or is
   "works offline after the first visit, via normal browser caching" good enough for v1? The former
   needs a deliberately built service-worker caching layer; the latter needs nothing extra.
7. **How should progress be stored** — `localStorage` only for a fully static, no-account site (the
   assumption this report runs with), or is a login/account/backend planned for a later version
   that would change the "fully static" architecture recommended here?
