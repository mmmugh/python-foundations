"""Check the course says it is independent, where a reader meets its name.

    python3 tests/disclaimer_test.py

Spec decision 10: the name stays "Python Foundations", which other courses and
a book series also use, and "Python" is the Python Software Foundation's
registered mark. So the site's front page and the README each say three
things: the course is independent, it is affiliated with and endorsed by no
one of the same name (the PSF included), and "Python" is the PSF's trademark.
This builds the front page into a temporary directory and reads it back.
"""

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build                                                    # noqa: E402

CLAIMS = ("an independent, free course", "not affiliated with", "Python Software Foundation",
          "registered trademark")


def main():
    results = []

    def expect(label, ok):
        results.append((label, ok))

    with tempfile.TemporaryDirectory() as tmp:
        build.SITE = Path(tmp)
        volume = {"slug": "vol1", "title": "A Volume", "subtitle": "", "blurb": ""}
        build.write_library([(volume, [{"slug": "ch01-one", "title": "One"}], None)])
        front = (Path(tmp) / "index.html").read_text()

    for claim in CLAIMS:
        expect(f"the front page says {claim!r}", claim in front)
    expect("the front page still lists the chapters", "vol1/ch01-one.html" in front)
    readme = (ROOT / "README.md").read_text()
    for claim in CLAIMS:
        expect(f"the README says {claim!r}", claim in readme)

    bad = 0
    for label, ok in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")
    print(f"\n{'the course says it is independent, wherever its name first appears' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
