"""Check the quizzes and answer keys are what quizzes.json renders.

    python3 tests/quiz_test.py

The .txt files are generated, but they are also what students print and what
the site serves, so a hand edit to one would quietly part it from its source,
and the next regeneration would undo it. This renders every quiz and key from
volumes/<volume>/quizzes.json in memory and compares them with the files.

It also checks every "Writing code" question is a program a student can read:
the blank sits in the code block, not in the wrapped question text (which
reflows, so a program written there printed as one long paragraph), and with
each answer from the key in the blank, the program compiles.
"""

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
import build                                                     # noqa: E402
import make_quizzes                                              # noqa: E402

UNIT_PAGE = "<!-- part: Unit 2 — Variables -->\n## Lesson 2.4 — Putting it together\n\nText.\n"
UNIT_QUIZ = {"quizzes": [{"slug": "ch02d-together", "questions": [
    {"section": "Vocabulary", "text": "A name for a value is a ____.", "answers": ["variable"]}]}]}


def main():
    results = []

    def expect(label, ok, detail=""):
        results.append((label, ok, detail))

    # Every volume with a quizzes.json, by name: find_volume() with no name
    # stops once there are two content volumes.
    counts = {}
    for vol in build.VOLS:
        source = vol["dir"] / make_quizzes.SOURCE_NAME
        if not source.exists():
            continue
        data = json.loads(source.read_text())
        files = make_quizzes.outputs(data, vol)
        counts[vol["slug"]] = len(files)
        stale = [p.relative_to(ROOT).as_posix() for p, text in files.items()
                 if not p.exists() or p.read_text() != text]
        expect(f"{vol['slug']}: all {len(files)} quizzes and keys are what quizzes.json renders",
               not stale, f"differ: {stale}")

        # Students print these. The question text is wrapped to 74 columns, but a
        # program is not, so a long line in one runs off a printed page.
        wide = [f"{p.name}:{i}" for p, text in files.items() if p.name.endswith("-quiz.txt")
                for i, line in enumerate(text.split("\n"), 1) if len(line) > 79]
        expect(f"{vol['slug']}: no line of a student's quiz is wider than 79 characters", not wide,
               f"too wide: {wide}")

        unreadable = []
        for quiz in data["quizzes"]:
            for n, q in enumerate(quiz["questions"], 1):
                if q["section"] != "Writing code":
                    continue
                where = f"{quiz['slug'][:4]} q{n}"
                code = q.get("code", "")
                if "____" in q["text"] or code.count("____") != 1:
                    unreadable.append(f"{where}: the blank is not in the code block")
                    continue
                # "fill" is the exact code to try, where an answer carries a note
                # for the marker ("any accurate one-line docstring works").
                for answer in q.get("fill", q["answers"]):
                    try:
                        compile(code.replace("____", answer), where, "exec")
                    except SyntaxError as err:
                        unreadable.append(f"{where}: with {answer!r}, {err.msg} (line {err.lineno})")
        # The programs above come from quizzes.json; what students read is what
        # the generator printed. Every program must appear whole in the rendered
        # key (which keeps "____"), so a generator that drops or mangles a line is
        # caught here rather than only by eye.
        by_name = {p.name: text for p, text in files.items()}
        for quiz in data["quizzes"]:
            key_text = by_name[f"{quiz['slug']}-answers.txt"]
            for n, q in enumerate(quiz["questions"], 1):
                if q.get("code"):
                    block = "\n".join("        " + line for line in q["code"].split("\n"))
                    if block not in key_text:
                        unreadable.append(f"{quiz['slug'][:4]} q{n}: the rendered key does not hold the whole program")
        expect(f"{vol['slug']}: every code question is a program that compiles with its answer",
               not unreadable, "; ".join(unreadable))
    expect("vol1-foundations still has its 24 quiz files", counts.get("vol1-foundations") == 24,
           f"{counts}")

    # A unit's quiz hangs off its last lesson and is headed with the unit.
    # outputs() only reads the pages, so the trial lives in a temporary
    # directory: nothing is written under volumes/, and a read-only checkout
    # (the GNU review container mounts one) runs it too.
    with tempfile.TemporaryDirectory() as scratch:
        trial = {"slug": "_trial-units", "dir": Path(scratch),
                 "content": Path(scratch) / "content", "quizzes": Path(scratch) / "quizzes"}
        trial["content"].mkdir()
        (trial["content"] / "ch02d-together.md").write_text(UNIT_PAGE)
        unit_files = make_quizzes.outputs(UNIT_QUIZ, trial)
        heading = next(t for p, t in unit_files.items() if p.name.endswith("-quiz.txt")).split("\n")[1]
        expect("a unit's quiz is headed with the unit", heading == "Unit 2 - Variables", heading)

    # A section name the generator does not know used to drop the question
    # from the quiz and the key without a word, and this test, comparing
    # rendered output with rendered output, could not see it.
    typo = {"slug": "x", "questions": [{"section": "Writing Code", "text": "A ____.", "answers": ["b"]}]}
    try:
        make_quizzes.render(typo, "T", 1)
        expect("a question in an unknown section is refused, not dropped", False, "rendered without it")
    except SystemExit:
        expect("a question in an unknown section is refused, not dropped", True)

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + detail + ')'}")
    print(f"\n{'every quiz is what its source says' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
