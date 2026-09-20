# Python Foundations

*Python Foundations: A First Course in Programming* as a web app: the whole
book, with every example in an editable box that runs in the browser.

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
scripts/       a one-file preview builder
archive/       how the project got here; nothing depends on it
```

`site/` is generated and not tracked. `site/bundle/` holds the book's code as
`.py` files, generated from the chapters so the two cannot disagree.

## `build.py --check`

The build refuses to ship a book that is wrong about itself:

- every code box is executed; one that fails without being declared as a
  deliberate teaching error fails the build
- every deterministic example's printed output is compared against what the
  chapter claims it prints, and a mismatch fails the build

It has caught two real errors so far: a stated output in Chapter 7 that the
code did not produce, and sixteen appendix fragments that were offering a Run
button they could not honour.

## Editing

Edit `content/*.md` and rebuild. The chapters are the only source of truth —
the code files, the site and the exercise stubs are all generated from them.
