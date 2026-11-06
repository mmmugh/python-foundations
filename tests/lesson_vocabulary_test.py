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


def hint_snippets(text):
    """The `inline code` in every hint (a "> " line in an exercise section)."""
    text = re.sub(r"^<!-- part: .+ -->\n", "", text)
    out, exercise = [], False
    for kind, payload in build.split_blocks(text.split("\n")):
        if kind == "h3":
            exercise = payload in build.EXERCISE_SECTIONS
        elif kind == "quote" and exercise:
            out += INLINE_CODE.findall(payload)
    return out


INLINE_CODE = re.compile(r"`([^`]+)`")


def unflagged(meta, stems):
    """True when a volume has lesson files but has not opted into this gate.
    Gating only flagged volumes would let a forgotten flag pass in silence."""
    return not meta.get("lessons") and any(re.match(r"^ch\d\d[a-z]-", s) for s in stems)


def violations(pages, solutions, checks=None):
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
        # Inline code in a hint or an option is held to the rule too; a
        # snippet that is not Python on its own (a lone operator) is skipped.
        snippets = [(f"{slug} hint", code) for code in hint_snippets(text)]
        snippets += [(f"{key} option", code) for key, spec in (checks or {}).items()
                     if key.startswith(f"{slug}#") and spec.get("kind") == "choice"
                     for option in spec["options"] for code in INLINE_CODE.findall(option)]
        used_by += [(where, code) for where, code in snippets if harvest(code, {k: set() for k in KINDS})]
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
        files = build.chapter_files(vol)
        if unflagged(meta, [p.stem for p in files]):
            expect(f"{vol['slug']}: has lesson files, so needs \"lessons\": true in volume.json", False,
                   "the vocabulary gate would skip it")
            continue
        if not meta.get("lessons"):
            continue
        pages = [(p.stem, p.read_text()) for p in files]
        solutions = {k: v for k, v in build.load_solutions(vol).items()}
        problems = violations(pages, solutions, build.load_json(vol, "_checks.json"))
        expect(f"{vol['slug']}: nothing in an exercise comes before its lesson", not problems,
               "; ".join(problems))


    # Found in review: the spec holds hints and options to the same rule, and
    # a lesson volume without the flag must not pass by being skipped.
    hinted = [("ch02a-one", "## L\n\n```python\nprint(1)\n```\n\n### Practice\n\n1. P.\n\n"
                            "> Say it: use `name.upper()`.\n")]
    expect("a hint is held to the same rule", any("upper" in v for v in violations(hinted, {})))
    chose = [("ch02a-one", "## L\n\n```python\nprint(1)\n```\n\n### Practice\n\n1. Which?\n")]
    expect("a choice option is held to the same rule", any("len" in v for v in violations(
        chose, {}, {"ch02a-one#1": {"kind": "choice", "options": ["`len(x)`", "`print(x)`"], "answer": 1}})))
    expect("lesson files without the lessons flag are refused",
           unflagged({}, ["00-front-matter", "ch02a-naming"]))
    expect("a chapter volume needs no flag", not unflagged({}, ["ch01-your-first-programs"]))

    bad = 0
    for label, ok, detail in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}{'' if ok else '  (' + detail + ')'}")
    print(f"\n{'nothing is used before it is taught' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
