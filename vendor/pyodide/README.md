# Pyodide 314.0.7 (fetched, not committed)

CPython 3.14 compiled to WebAssembly. Upstream:
<https://github.com/pyodide/pyodide>, licensed MPL-2.0 (`LICENSE` here).
Nothing in this directory is written or edited by this project.

Only three files here are tracked in git—this README, `LICENSE`, and
`CHECKSUMS`. The runtime itself is fetched on the first build and ignored by
git. Five files, about 13 MB, the ones a page actually requests:

| file | what it is |
| --- | --- |
| `pyodide.mjs` | the loader, imported by `app.js` |
| `pyodide.asm.mjs` | the Emscripten glue |
| `pyodide.asm.wasm` | CPython itself |
| `python_stdlib.zip` | the standard library |
| `pyodide-lock.json` | read at startup even with no packages to load |

The rest of the npm package—type declarations, source maps, the bundled
consoles—is another 14 MB that no page ever fetches.

## Fetched once, served locally

The site serves Python from its own origin rather than a CDN: a page load does
not depend on anyone else's uptime, and a room full of students is not pulling
13 MB across the internet per machine. That is about how it is *served*, not
about who distributes it, so the bytes are fetched at install rather than kept
in this repository's history.

`build.py` fetches them when they are missing and verifies them on every build.
To do it by hand, or to move to a newer Pyodide:

    python3 scripts/fetch_pyodide.py             # verify against CHECKSUMS
    python3 scripts/fetch_pyodide.py --download  # fetch what is missing or wrong
    python3 scripts/fetch_pyodide.py --update 314.0.9

## CHECKSUMS

Downloading at install means someone else hands you the bytes, so `CHECKSUMS`
pins the SHA-256 of each file. `build.py` re-checks all five every build and
stops rather than shipping a mismatch to a browser.

The pins were taken from bytes that arrived identically over two independent
channels: the npm registry tarball and the jsdelivr CDN.
