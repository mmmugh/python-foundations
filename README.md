# Python Foundations

*Python Foundations: A First Course in Programming* as a web app: the whole
course, with every example in an editable box that runs in the browser.

Twelve chapters, 157 runnable code boxes, 75 exercises (41 of which check your
answer), an interactive scratchpad, and four appendices. No accounts, no
backend, no build toolchain — it is a static site, and Python runs in the
browser via Pyodide.

## Running it

Nothing to install—no package manager, no build toolchain, no accounts.
Python 3.9 or newer is the only requirement, and `build.py` uses only the
standard library. On a Mac, the `python3` that comes with the Command Line
Tools, the same install that provides `git`, is 3.9.6, and it works; any
current Python is a better choice. Verified on 3.9 and 3.14, including
`--check`, which runs every example under whichever interpreter you used.

```
git clone https://github.com/mmmugh/python-foundations.git
cd python-foundations
python3 build.py --check          # build site/ and verify every example
python3 scripts/serve.py          # serve it on :8731
```

`scripts/serve.py` exists rather than `python3 -m http.server` because that
sends plain text with no charset, and a browser left to guess turns a UTF-8 em
dash into `a-EUR-`. The quizzes are pure ASCII so it cannot bite them; the
server says the charset anyway.

Then open <http://localhost:8731/>. The first build downloads the Python
runtime once (13 MB, see below); after that nothing here touches the network.

## What is here

```
volumes/                one directory per course
  vol1-foundations/
    volume.json           its title, subtitle and place in the order
    content/              the manuscript, one Markdown file per chapter
      _boxes.json           boxes needing a setup line, an error, or no Run button
      _checks.json          how each checkable exercise is checked
      _solutions.md         worked answers—never published whole
    quizzes/              one fill-in-the-blank quiz per chapter
    answer-keys/          the matching keys—NEVER copied into site/ (see below)
build.py                volumes/ -> site/. No dependencies
web/                    page template, stylesheet, browser runtime
  box_runner.py           runs a box, stops a runaway loop, checks an answer
scripts/                preview builder, Word export, quiz renderer, local server
vendor/pyodide/         CPython 3.14 as WebAssembly; fetched, not committed
tests/                  harnesses that run the course under real Pyodide
archive/                how the project got here; nothing depends on it
```

`site/` is generated and not tracked. It looks like this:

```
site/
  index.html            the way in: every volume and its chapters
  app.js  app.css       shared by every volume
  pyodide/              shared too—fetched once, not once per volume
  vol1-foundations/
    ch01-....html  ...  the chapters
    quizzes/            the student copies only
    bundle/             the course's code as .py files
```

## Adding a volume

Make a directory under `volumes/` with a `volume.json` in it and a `content/`
beside it, then build. Nothing in `build.py` names a volume, and nothing
outside `volumes/` has to change:

```json
{ "number": 2, "title": "Python Further", "subtitle": "A Second Course",
  "blurb": "One sentence for the contents page." }
```

Chapters are `chNN-slug.md`, with `00-` for front matter and `99-` for
appendices; that is the whole naming convention. Quizzes and answer keys go in
`quizzes/` and `answer-keys/` inside the volume.

`python3 tests/second_volume_test.py` proves this still holds: it creates a
throwaway volume, builds it, checks that it got its own directory, that its
pages reach the shared runtime rather than copying it, and that the library
page stops calling itself volume one—then deletes it again.

`python3 scripts/make_docx.py` writes a volume's chapters out as a Word file,
into that volume's directory in `site/`. It is the only thing here that needs a
package (`python-docx`); the course builds fine without it, and the download
link simply does not appear.

## `build.py --check`

The build refuses to ship a course that is wrong about itself:

- every code box is executed; one that fails without being declared as a
  deliberate teaching error fails the build
- every deterministic example's printed output is compared against what the
  chapter claims it prints, and a mismatch fails the build

It has caught two real errors so far: a stated output in Chapter 7 that the
code did not produce, and sixteen appendix fragments that were offering a Run
button they could not honor.

## The Python runtime

The code boxes run real CPython 3.14, compiled to WebAssembly by
[Pyodide](https://github.com/pyodide/pyodide) (MPL-2.0). The site serves it
from its own origin rather than loading it from a CDN at page load: nothing
about reading this course depends on someone else's uptime, and a classroom of
thirty is not pulling 13 MB across the internet thirty times.

Those 13 MB are *not* in this repository. Serving the runtime locally is the
point; carrying a copy of someone else's binaries in this history is not. The
first `build.py` fetches them into `vendor/pyodide/` (gitignored) and says so;
every build after that finds them already there.

What is tracked is enough to get exactly those bytes back and prove they are
the right ones. `vendor/pyodide/CHECKSUMS` pins the SHA-256 of each file,
`build.py` re-checks all five on every build and refuses to ship a mismatch,
and the fetch is a script you can run yourself:

```
python3 scripts/fetch_pyodide.py             # verify against CHECKSUMS
python3 scripts/fetch_pyodide.py --download  # re-fetch anything missing or wrong
python3 scripts/fetch_pyodide.py --update 314.0.9   # move to a new Pyodide
```

The pinned hashes were taken from bytes that arrived identically over two
independent channels—the npm registry tarball and the jsdelivr CDN—so a later
compromise of either one fails the build instead of reaching a browser.

If you need a build machine with no network, run the fetch once somewhere that
has one and copy `vendor/pyodide/` across; the checksums will confirm it
arrived intact.

## The answer keys

A volume's `quizzes/*-quiz.txt` is copied into `site/` and linked from the foot
of each chapter. Its `answer-keys/*-answers.txt` is not, and must not be:
everything under
`site/` is fetchable by anyone who guesses a filename, with no traversal bug
required. `build.py` copies by an explicit whitelist of `*-quiz.txt` rather than
excluding what it recognizes as a key — an exclusion rule fails open the first
time a key is named something unexpected — and then greps everything it wrote
for the answer-key marker and fails the build if one is found.

The keys are not in this repository either. They are private and kept outside
version control, and `.gitignore` excludes `volumes/*/answer-keys/`. An ignore
rule does not stop `git add -f`, so `tests/answer_key_guard.py` fails if one is
ever committed, recognizing a key by its path or by the header
`make_quizzes.py` writes into every one; `--history` checks every commit rather
than only the tree.

## The leak guard

This repo is meant to be public, so `.githooks/leak-scan` reads a diff and
refuses anything whose **added** lines or added file paths match a deny
pattern: absolute home directories, private LAN addresses, and the shapes of
AWS keys, GitHub tokens, API keys and PEM private keys. It runs from
`pre-commit` and again from `pre-push`, which catches anything committed with
`--no-verify` or pushed from another clone.

`pre-push` scans **each new commit separately**, not the difference between
the two ends of the push. Scanning the net is the obvious implementation and
it is wrong: a leak committed with `--no-verify` and deleted in a later commit
nets to nothing, so the push is allowed — and both commits still land in the
remote, where the token is as readable as ever. A commit already made cannot
be fixed by deleting the content in a later one.

Git does not carry hooks in a clone, so after cloning:

    git config core.hooksPath .githooks

Only added lines are scanned, so a leak already committed can still be removed
— a scan that also matched removals would make the fix un-committable. Added
paths are scanned because a leak can hide in a filename. Generic patterns match
case-sensitively, so a lowercase `/users/` route is not mistaken for a home
directory.

Anything personal — an employer, a codename, a private hostname — goes in
`.githooks/leak-patterns.local`, which is gitignored and matched
case-insensitively. Copy `leak-patterns.local.example` to start one. The
tracked pattern file holds shapes only and is safe to publish, which is the
point: a deny list that itself leaks is no use.

Known blind spot, documented rather than hidden: a binary file produces no
added lines, so a secret inside one is not seen.

`python3 tests/leak_scan_test.py` checks the scanner blocks what it claims to
and allows what it should, including the scrub-out case.
`python3 tests/pre_push_test.py` is a separate question — whether the hook
hands the scanner the right diffs — and answers it by pushing at a throwaway
bare remote in a temp directory. The scanner was already correct on the day a
push carrying a token in its history sailed through.

`python3 scripts/scan_history.py` runs the scanner over every commit in the
history, which is what a public repository publishes, rather than over the
final tree. It refuses a shallow clone or an empty history instead of calling
either clean. CI runs it with `--redact`, which prints a commit and a count and
never what matched.

## Editing

Edit `volumes/<volume>/content/*.md` and rebuild. The chapters are the only
source of truth: the code files, the site and the exercise stubs are all
generated from them.

## Licenses

| What | License |
| --- | --- |
| The course: everything under `volumes/`, meaning the chapters and their example programs, exercises, worked solutions, practice pages and quizzes | [CC BY-NC-SA 4.0](LICENSE-COURSE) |
| Everything else: the build, the page scripts, the tests and the git hooks | [Apache-2.0](LICENSE) |
| Pyodide, fetched into `vendor/pyodide/` and served from `site/pyodide/` | its own license, MPL-2.0 ([`vendor/pyodide/LICENSE`](vendor/pyodide/LICENSE)) |

The git hooks in `.githooks/` were adapted from
[tokenwatt](https://github.com/mmmugh/tokenwatt), by the same author, where they
are MIT-licensed.
