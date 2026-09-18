"""Split the exported manuscript into one Markdown file per chapter.

Run once, when the manuscript is first brought into the repo:

    python3 scripts/split_book.py path/to/book-export.md

After that, content/ is the master copy and this script is history.
"""

import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"


def slug(title):
    """Turn a chapter title into a filename stem."""
    text = re.sub(r"`", "", title).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def split(lines):
    """Yield (filename, heading_lines) for front matter, each chapter, appendices."""
    pieces = []
    current = ["00-front-matter", [], None]
    part = None
    fence = False

    for line in lines:
        if line.startswith("```"):
            fence = not fence

        if not fence:
            part_match = re.match(r"^# (Part .+)$", line)
            chapter_match = re.match(r"^## Chapter (\d+) — (.+)$", line)
            appendix_match = re.match(r"^# Appendices\s*$", line)

            if part_match:
                part = part_match.group(1)
                continue          # parts become a field, not a file

            if chapter_match or appendix_match:
                pieces.append(current)
                if chapter_match:
                    number, title = chapter_match.group(1), chapter_match.group(2)
                    name = f"ch{int(number):02d}-{slug(title)}"
                    current = [name, [], part]
                else:
                    current = ["99-appendices", [], None]

        current[1].append(line)

    pieces.append(current)
    return pieces


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/split_book.py <book-export.md>")

    lines = Path(sys.argv[1]).read_text().split("\n")
    CONTENT.mkdir(exist_ok=True)

    for name, body, part in split(lines):
        text = "\n".join(body).strip("\n") + "\n"
        if part:
            text = f"<!-- part: {part} -->\n{text}"
        path = CONTENT / f"{name}.md"
        path.write_text(text)
        print(f"  {path.relative_to(CONTENT.parent)}  {len(text):>7,} chars")


if __name__ == "__main__":
    main()
