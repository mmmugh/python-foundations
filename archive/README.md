# Archive

Nothing in here is used to build or run the web app. It is kept because it
explains how the project got here, not because anything depends on it.

| | |
| --- | --- |
| `main.py` | A Replit menu launcher. It printed a list of chapters, read a choice with `input()`, and ran the chosen file with `subprocess.run()`. Web navigation replaced it; no other file in the project ever imported it. |
| `examples/`, `projects/` | The hand-written code bundle, the original deliverable before any of this was a web app. `projects/` was byte-identical to the book. `examples/` was not: it had been adapted to satisfy the bundle's promise that a file "runs start to finish without stopping", which meant commenting out the deliberate errors, wrapping the `input()` examples in functions that were never called, and dropping three examples altogether. The web app has no such constraint, so `site/bundle/` is now generated from the manuscript instead and cannot drift. |
| `split_book.py` | Ran once, to split the exported manuscript into `content/`. `content/` has been the master copy ever since, so this cannot be run again without discarding edits. |
| `SCOPING.md` | The first scoping report, written before the manuscript was known to exist. Its headline finding — that no instructional prose existed — was wrong, and a correction sits at the top of the file. Kept as a record of what was believed at the start. |

## How this project started

The book was not commissioned. It was written by Claude in a chat, in response
to a request for a recommendation of a textbook to buy. The code bundle and the
Replit instructions came from that same accident, and made sense while the
deliverable was a folder of files. They stopped making sense when it became a
browser application, which is why they are here rather than there.
