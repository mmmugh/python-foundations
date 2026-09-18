"""Inline one built page into a single self-contained HTML file.

    python3 scripts/make_preview.py ch01-your-first-programs

Useful for sending someone a page to look at, and for checking what the site
looks like without serving it.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"


def main():
    slug = sys.argv[1] if len(sys.argv) > 1 else "ch01-your-first-programs"
    page = (SITE / f"{slug}.html").read_text()

    page = page.replace(
        '<link rel="stylesheet" href="app.css">',
        "<style>\n" + (SITE / "app.css").read_text() + "\n</style>",
    )
    page = page.replace(
        '<script type="module" src="app.js"></script>',
        '<script type="module">\n' + (SITE / "app.js").read_text() + "\n</script>",
    )
    # A single file has no sibling pages to link to.
    page = page.replace('<details class="toc">', '<details class="toc" hidden>')

    out = SITE / f"{slug}.standalone.html"
    out.write_text(page)
    print(f"{out.relative_to(ROOT)}  {len(page):,} bytes")


if __name__ == "__main__":
    main()
