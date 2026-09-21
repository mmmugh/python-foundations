"""Fetch and verify the vendored Pyodide runtime.

    python3 scripts/fetch_pyodide.py             # verify vendor/pyodide against CHECKSUMS
    python3 scripts/fetch_pyodide.py --download  # fetch anything missing or wrong
    python3 scripts/fetch_pyodide.py --update 314.0.9   # move to a new Pyodide, re-pin

The site serves Python from its own origin instead of a CDN, so a page load
does not depend on anyone else's uptime and a student in a classroom is not
pulling 13 MB across the internet per machine. Serving it locally is the point;
holding a copy of it in this repository's history is not, so the runtime is
fetched once at install and gitignored.

Downloading at install still means someone else hands you the bytes, which is
what CHECKSUMS is for: the SHA-256 of all five files is tracked, build.py
re-checks them on every build, and a mismatch stops the build rather than
reaching a browser. The pins were taken from bytes that arrived identically
over two independent channels -- the npm registry tarball and the jsdelivr CDN
-- so a later compromise of either one fails this check.
"""

import hashlib
import sys
import urllib.request
from pathlib import Path

VENDOR = Path(__file__).resolve().parent.parent / "vendor" / "pyodide"
CHECKSUMS = VENDOR / "CHECKSUMS"
CDN = "https://cdn.jsdelivr.net/npm/pyodide@{version}/"

# What the browser actually asks for. Not the whole npm package: the .d.ts,
# .map and console.html files are a further 14 MB that no page ever fetches.
RUNTIME = (
    "pyodide.mjs",           # the loader, imported by app.js
    "pyodide.asm.mjs",       # the Emscripten glue, imported by pyodide.mjs
    "pyodide.asm.wasm",      # CPython itself
    "python_stdlib.zip",     # the standard library
    "pyodide-lock.json",     # read at startup even with no packages to load
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pinned():
    """The recorded {name: sha256}, and the version line above them."""
    version, hashes = None, {}
    for line in CHECKSUMS.read_text().splitlines():
        if line.startswith("# pyodide "):
            version = line.split()[2]
        elif line and not line.startswith("#"):
            value, name = line.split(None, 1)
            hashes[name.strip()] = value
    return version, hashes


def download(version, names):
    for name in names:
        url = CDN.format(version=version) + name
        print(f"  downloading {name} ...", end="", flush=True)
        with urllib.request.urlopen(url, timeout=120) as response:
            if response.status != 200:
                sys.exit(f"\n{url} returned {response.status}")
            body = response.read()
        (VENDOR / name).write_bytes(body)
        print(f" {len(body):,} bytes")


def verify(hashes):
    """Return the files that are missing or do not match. Empty list is good."""
    bad = []
    for name, want in hashes.items():
        path = VENDOR / name
        if not path.exists():
            bad.append(f"{name}: missing")
        elif (got := digest(path)) != want:
            bad.append(f"{name}: sha256 {got}, expected {want}")
    return bad


def write_checksums(version):
    lines = [f"# pyodide {version}",
             "# sha256 of every file served from site/pyodide/.",
             f"# Source: {CDN.format(version=version)}",
             ""]
    lines += [f"{digest(VENDOR / name)}  {name}" for name in RUNTIME]
    CHECKSUMS.write_text("\n".join(lines) + "\n")
    print(f"pinned {len(RUNTIME)} files at pyodide {version} -> {CHECKSUMS.name}")


def main(argv):
    VENDOR.mkdir(parents=True, exist_ok=True)

    if "--update" in argv:
        version = argv[argv.index("--update") + 1]
        download(version, RUNTIME)
        write_checksums(version)
        print("now rebuild, and run tests/ against the new runtime before committing")
        return

    if not CHECKSUMS.exists():
        sys.exit("vendor/pyodide/CHECKSUMS is missing -- "
                 "run: python3 scripts/fetch_pyodide.py --update <version>")

    version, hashes = pinned()
    bad = verify(hashes)

    if bad and "--download" in argv:
        download(version, [line.split(":")[0] for line in bad])
        bad = verify(hashes)

    if bad:
        print(f"pyodide {version} in {VENDOR}:", file=sys.stderr)
        for line in bad:
            print(f"  {line}", file=sys.stderr)
        sys.exit("run: python3 scripts/fetch_pyodide.py --download")

    print(f"pyodide {version}: {len(hashes)} files match CHECKSUMS")


if __name__ == "__main__":
    main(sys.argv[1:])
