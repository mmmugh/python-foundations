"""Render the chapter quizzes from structured data.

    python3 scripts/make_quizzes.py drafts.json

Writes two files per chapter into quizzes/: the student's copy, and the answer
key. Markdown-ish, but named .txt so it opens in any text editor and prints
without ceremony.

Blanks are a fixed width whatever the answer is. A blank sized to its answer
tells the student how long the word is, which is a hint nobody asked for.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUIZZES = ROOT / "quizzes"

# Answer keys live OUTSIDE the directory the site is built from, and outside
# the directory the build copies into it. Nothing under site/ is private: a
# file there is fetchable by anyone who guesses its name, without needing any
# traversal bug at all. Keeping the keys out of the copy path is the control;
# an unguessable filename would not be one.
KEYS = ROOT / "answer-keys"
BLANK = "_" * 18
SECTIONS = ["Vocabulary", "Reading code", "Writing code", "Why it works"]
WIDTH = 74


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
        f"Chapter {number} — {title}",
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
        lines += ["", section.upper(), "─" * len(section), ""]
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
                lines.append("")
                lines += ["        " + l for l in q["code"].split("\n")]
                if trailing and not answers:
                    lines += ["", "    " + BLANK + BLANK]
            if answers:
                lines.append("")
                for a in q["answers"]:
                    shown = a if "\n" not in a else "\n          ".join(a.split("\n"))
                    lines.append(f"      ANSWER: {shown}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    data = json.loads(Path(sys.argv[1]).read_text())
    quizzes = data["quizzes"] if isinstance(data, dict) else data
    QUIZZES.mkdir(exist_ok=True)
    KEYS.mkdir(exist_ok=True)

    titles = {}
    for md in ROOT.joinpath("content").glob("ch*.md"):
        head = re.search(r"^## Chapter (\d+) — (.+)$", md.read_text(), re.M)
        titles[md.stem] = (int(head.group(1)), head.group(2))

    for quiz in sorted(quizzes, key=lambda q: q["slug"]):
        number, title = titles[quiz["slug"]]
        stem = quiz["slug"]
        (QUIZZES / f"{stem}-quiz.txt").write_text(render(quiz, title, number))
        (KEYS / f"{stem}-answers.txt").write_text(
            render(quiz, title, number, answers=True))
        blanks = sum(q["text"].count("____") for q in quiz["questions"])
        print(f"  {stem:<38}{len(quiz['questions']):>3} questions, {blanks:>3} blanks")


if __name__ == "__main__":
    main()
