"""Inline one built page into a single self-contained HTML file.

    python3 scripts/make_preview.py ch01-your-first-programs [volume-slug]

Useful for sending someone a page to look at, and for checking what the site
looks like without serving it.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT))
from build import assert_nothing_private_published, find_volume  # noqa: E402


def main():
    slug = sys.argv[1] if len(sys.argv) > 1 else "ch01-your-first-programs"
    vol = find_volume(sys.argv[2] if len(sys.argv) > 2 else None)
    page = (SITE / vol["slug"] / f"{slug}.html").read_text()

    page = page.replace(
        '<link rel="stylesheet" href="../app.css">',
        "<style>\n" + (SITE / "app.css").read_text() + "\n</style>",
    )
    page = page.replace(
        '<script type="module" src="../app.js"></script>',
        '<script type="module">\n' + (SITE / "app.js").read_text() + "\n</script>",
    )
    # A single file has no sibling pages to link to.
    page = page.replace('<details class="toc">', '<details class="toc" hidden>')

    # Must sit at the top of site/, not inside the volume: app.js is inlined
    # here, and an inline module resolves "pyodide/" against the document, so
    # the file has to be a sibling of the runtime directory.
    out = SITE / f"{slug}.standalone.html"
    out.write_text(page)
    assert_nothing_private_published()   # this lands in site/, which is published
    print(f"{out.relative_to(ROOT)}  {len(page):,} bytes")


if __name__ == "__main__":
    main()
