"""Render the chapter quizzes from structured data.

    python3 scripts/make_quizzes.py [volume-slug]

Reads volumes/<volume>/quizzes.json and writes two files per chapter: the
student's copy into quizzes/, and the answer key into answer-keys/.
Markdown-ish, but named .txt so it opens in any text editor and prints without
ceremony. tests/quiz_test.py fails if a committed file differs from what this
renders, so edit quizzes.json and run this rather than editing the .txt files.

quizzes.json was recovered from the rendered files on 2026-10-30, after the
original drafts.json was lost; rendering it reproduced all 24 files byte for
byte.

Blanks are a fixed width whatever the answer is. A blank sized to its answer
tells the student how long the word is, which is a hint nobody asked for.

The output is pure ASCII, deliberately. A .txt file carries no way to declare
its encoding, and a server sending "text/plain" with no charset leaves the
reader's browser to guess -- which on a phone turned an em dash into "a-EUR-".
An .html page can say <meta charset>; plain text cannot, so it must not need to.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from build import find_volume                                   # noqa: E402

VOLUME = find_volume(sys.argv[1] if len(sys.argv) > 1 else None)
QUIZZES = VOLUME["quizzes"]
SOURCE = VOLUME["dir"] / "quizzes.json"

# Answer keys live OUTSIDE the directory the site is built from, and outside
# the directory the build copies into it. Nothing under site/ is private: a
# file there is fetchable by anyone who guesses its name, without needing any
# traversal bug at all. Keeping the keys out of the copy path is the control;
# an unguessable filename would not be one.
KEYS = VOLUME["dir"] / "answer-keys"
BLANK = "_" * 18
ASCII_ONLY = {"\u2014": "-", "\u2013": "-", "\u2018": "'", "\u2019": "'",
              "\u201c": '"', "\u201d": '"', "\u2026": "...", "\u00a0": " "}
SECTIONS = ["Vocabulary", "Reading code", "Writing code", "Why it works"]
WIDTH = 74


def plain(text):
    """Fold the typographic characters down to ASCII."""
    for fancy, flat in ASCII_ONLY.items():
        text = text.replace(fancy, flat)
    return text


def wrap(text, indent, first_indent=None):
    """Wrap to WIDTH, keeping blanks intact."""
    out, line = [], (first_indent if first_indent is not None else indent)
    start = len(line)
    for word in text.split():
        if len(line) + len(word) + 1 > WIDTH and len(line) > start:
            out.append(line.rstrip())
            line = indent + word
        else:
            line = line + ("" if not line.strip() or line.endswith(" ") else " ") + word
    out.append(line.rstrip())
    return out


def render(quiz, title, number, answers=False):
    lines = [
        "PYTHON FOUNDATIONS",
        plain(f"Chapter {number} - {title}"),
        "",
        "ANSWER KEY" if answers else
        "Name: ________________________________     Date: ______________",
        "",
    ]
    if not answers:
        lines += wrap(
            "Fill in every blank. Where a term is asked for, write the word the "
            "course uses. Where code is asked for, write exact Python. Where "
            "output is asked for, write what the program prints, one line per "
            "line.", "")
        lines.append("")

    n = 0
    for section in SECTIONS:
        items = [q for q in quiz["questions"] if q["section"] == section]
        if not items:
            continue
        lines += ["", section.upper(), "-" * len(section), ""]
        for q in items:
            n += 1
            text, trailing = q["text"], False
            # "What does this print? ____" reads better as the question, then the
            # code, then somewhere to write the answer.
            if q.get("code") and text.rstrip().endswith("____"):
                text, trailing = text.rstrip()[:-4].rstrip(), True
            if not answers:
                text = text.replace("____", BLANK)
            lines += wrap(text, "    ", f"{n:>2}. ")
            if q.get("code"):
                # A program with a blank in it lives here, not in the question
                # text: the text is reflowed to WIDTH, which would run its
                # lines together into one paragraph.
                code = q["code"] if answers else q["code"].replace("____", BLANK)
                lines.append("")
                lines += ["        " + l for l in code.split("\n")]
                if trailing and not answers:
                    lines += ["", "    " + BLANK + BLANK]
            if answers:
                lines.append("")
                for a in q["answers"]:
                    shown = a if "\n" not in a else "\n          ".join(a.split("\n"))
                    lines.append(f"      ANSWER: {shown}")
            lines.append("")
    out = plain("\n".join(lines).rstrip() + "\n")
    stray = sorted({c for c in out if ord(c) > 127})
    if stray:
        raise SystemExit(
            "quiz text must be ASCII, because a .txt cannot declare its encoding. "
            f"Found: {[f'U+{ord(c):04X} {c!r}' for c in stray]}")
    return out


def outputs(data):
    """{path: text} for every quiz and answer key the data describes."""
    quizzes = data["quizzes"] if isinstance(data, dict) else data
    titles = {}
    for md in VOLUME["content"].glob("ch*.md"):
        head = re.search(r"^## Chapter (\d+) — (.+)$", md.read_text(), re.M)
        titles[md.stem] = (int(head.group(1)), head.group(2))
    files = {}
    for quiz in sorted(quizzes, key=lambda q: q["slug"]):
        number, title = titles[quiz["slug"]]
        stem = quiz["slug"]
        files[QUIZZES / f"{stem}-quiz.txt"] = render(quiz, title, number)
        files[KEYS / f"{stem}-answers.txt"] = render(quiz, title, number, answers=True)
    return files


def main():
    data = json.loads(SOURCE.read_text())
    QUIZZES.mkdir(exist_ok=True)
    KEYS.mkdir(exist_ok=True)
    for path, text in outputs(data).items():
        path.write_text(text)
    for quiz in sorted(data["quizzes"], key=lambda q: q["slug"]):
        blanks = sum(q["text"].count("____") + q.get("code", "").count("____")
                     for q in quiz["questions"])
        print(f"  {quiz['slug']:<38}{len(quiz['questions']):>3} questions, {blanks:>3} blanks")


if __name__ == "__main__":
    main()
