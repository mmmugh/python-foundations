"""Nothing in a lesson's exercises is used before a lesson has shown it.

    python3 tests/lesson_vocabulary_test.py

What a lesson teaches is what its examples show: every construct, built-in and
method in the code fences outside its exercise sections. Its exercises, their
starters and their worked solutions may use what this lesson's examples and
every earlier lesson's examples have shown, and nothing else. It is the
practice-page gate (practice_test.py), applied lesson by lesson; the
vocabulary is derived from the course, never typed in, so it cannot drift.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
import build                                                    # noqa: E402
from practice_test import harvest                               # noqa: E402

KINDS = ("nodes", "names", "attrs")


def sections(text):
    """[(is_exercise, code)] for every fence in a page, in order."""
    text = re.sub(r"^<!-- part: .+ -->\n", "", text)
    out, exercise = [], False
    for kind, payload in build.split_blocks(text.split("\n")):
        if kind == "h3":
            exercise = payload in build.EXERCISE_SECTIONS
        elif kind == "code":
            out.append((exercise, payload))
    return out


def violations(pages, solutions):
    taught = {k: set() for k in KINDS}
    found = []
    for slug, text in pages:
        fences = sections(text)
        for is_exercise, code in fences:
            if not is_exercise:
                harvest(code, taught)
        used_by = [(f"{slug} exercise fence", code) for is_exercise, code in fences if is_exercise]
        used_by += [(key, entry["code"]) for key, entry in solutions.items()
                    if key.startswith(f"{slug}#")]
        for where, code in used_by:
            used = {k: set() for k in KINDS}
            if not harvest(code, used):
                found.append(f"{where}: does not parse")
                continue
            for kind in KINDS:
                early = sorted(used[kind] - taught[kind])
                if early:
                    found.append(f"{where}: uses {kind} no lesson has shown yet: {early}")
    return found


def main():
    results = []

    def expect(label, ok, detail=""):
        results.append((label, ok, detail))

    planted = [("ch02a-one", "## L\n\n```python\nprice = 12\nprint(price)\n```\n\n### Practice\n\n"
                             "1. Print it in capitals.\n\n```python\nname = 'ada'\nprint(name.upper())\n```\n")]
    caught = violations(planted, {})
    expect("the gate catches a method no lesson has shown", any("upper" in v for v in caught), str(caught))
    expect("and lets through what the lesson's own examples show",
           not violations([("ch02a-one", "## L\n\n```python\nprice = 12\nprint(price)\n```\n\n"
                                         "### Practice\n\n1. P.\n\n```python\ncost = 3\nprint(cost)\n```\n")], {}))
    expect("a worked solution is held to the same rule",
           any("len" in v for v in violations([("ch02a-one", "## L\n\n```python\nprint(1)\n```\n")],
                                              {"ch02a-one#1": {"code": "print(len('ab'))"}})))

    for vol in build.VOLS:
        meta = json.loads((vol["dir"] / "volume.json").read_text())
        if not meta.get("lessons"):
            continue
        pages = [(p.stem, p.read_text()) for p in build.chapter_files(vol)]
        solutions = {k: v for k, v in build.load_solutions(vol).items()}
        problems = violations(pages, solutions)
        expect(f"{vol['slug']}: nothing in an exercise comes before its lesson", not problems,
               "; ".join(problems))

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + detail + ')'}")
    print(f"\n{'nothing is used before it is taught' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
