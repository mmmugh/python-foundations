# Python Foundations

*Python Foundations: A First Course in Programming* as a web app: the whole
course, with every example in an editable box that runs in the browser.

Twelve chapters, 157 runnable code boxes, 75 exercises (41 of which check your
answer), an interactive scratchpad, and four appendices. No accounts, no
backend, no build toolchain — it is a static site, and Python runs in the
browser via Pyodide.

## Running it

```
python3 build.py --check          # build site/ and verify every example
python3 -m http.server 8731 --directory site
```

Then open <http://localhost:8731/>. Nothing to install: `build.py` uses only
the standard library, and the page loads Pyodide from a CDN on first visit.

## What is here

```
content/       the manuscript, one Markdown file per chapter — the master copy
  _boxes.json    boxes needing a setup line, an expected error, or no Run button
  _checks.json   how each checkable exercise is checked
build.py       content/ -> site/. ~600 lines, no dependencies
web/           page template, stylesheet, browser runtime
  box_runner.py  runs a box, stops a runaway loop, checks an answer
scripts/       preview builder, Word export, quiz renderer
quizzes/       one fill-in-the-blank quiz per chapter, linked from the site
answer-keys/   the matching keys — NEVER copied into site/ (see below)
archive/       how the project got here; nothing depends on it
```

`site/` is generated and not tracked. `site/bundle/` holds the course's code as
`.py` files, generated from the chapters so the two cannot disagree.

`python3 scripts/make_docx.py` writes `site/python-foundations.docx` from the
same chapters. It is the only thing here that needs a package (`python-docx`);
the course builds fine without it, and the download link simply does not appear.

## `build.py --check`

The build refuses to ship a course that is wrong about itself:

- every code box is executed; one that fails without being declared as a
  deliberate teaching error fails the build
- every deterministic example's printed output is compared against what the
  chapter claims it prints, and a mismatch fails the build

It has caught two real errors so far: a stated output in Chapter 7 that the
code did not produce, and sixteen appendix fragments that were offering a Run
button they could not honour.

## The answer keys

`quizzes/*-quiz.txt` is copied into `site/` and linked from the foot of each
chapter. `answer-keys/*-answers.txt` is not, and must not be: everything under
`site/` is fetchable by anyone who guesses a filename, with no traversal bug
required. `build.py` copies by an explicit whitelist of `*-quiz.txt` rather than
excluding what it recognises as a key — an exclusion rule fails open the first
time a key is named something unexpected — and then greps everything it wrote
for the answer-key marker and fails the build if one is found.

## Editing

Edit `content/*.md` and rebuild. The chapters are the only source of truth —
the code files, the site and the exercise stubs are all generated from them.
