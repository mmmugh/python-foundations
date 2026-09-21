# Python Foundations

*Python Foundations: A First Course in Programming* as a web app: the whole
course, with every example in an editable box that runs in the browser.

Twelve chapters, 157 runnable code boxes, 75 exercises (41 of which check your
answer), an interactive scratchpad, and four appendices. No accounts, no
backend, no build toolchain — it is a static site, and Python runs in the
browser via Pyodide.

## Running it

Nothing to install—no package manager, no build toolchain, no accounts. A
Python 3 is the only requirement, and `build.py` uses only the standard
library. Verified on 3.9 and 3.14, including `--check`, which runs every
example under whichever interpreter you used.

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
button they could not honour.

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
excluding what it recognises as a key — an exclusion rule fails open the first
time a key is named something unexpected — and then greps everything it wrote
for the answer-key marker and fails the build if one is found.

## Editing

Edit `volumes/<volume>/content/*.md` and rebuild. The chapters are the only
source of truth: the code files, the site and the exercise stubs are all
generated from them.
