"""Print a wrong-then-right answer for every checked exercise in vol1-steps.

    python3 tests/steps_answers.py            # every lesson
    python3 tests/steps_answers.py 02          # only unit 2's lessons

steps_walk.mjs drives a real browser through every checked exercise, typing
the wrong answer first (which must fail) and the right one second (which
must pass). The answers come from the course's own data -- the check, the
worked solution, the exercise's own fence -- never typed in by hand, so they
cannot drift from what the lessons actually ask.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "web"))
import box_runner                                               # noqa: E402
import build                                                    # noqa: E402
from steps_volume_test import VOLUME, blocks_of, exercises       # noqa: E402

UNIT = re.compile(r"<!-- part: Unit (\d+) ")


def answer_for(slug, number, spec, code, solutions):
    key = f"{slug}#{number}"
    kind = spec["kind"]
    if kind == "choice":
        right = spec["answer"]
        wrong = 1 if right == 0 else 0
        return kind, right, wrong
    if kind == "predict":
        right = box_runner._capture(code, 5, {})
        return kind, right, "no idea"
    if kind == "trace":
        rows = box_runner.trace_rows(code, spec["names"])
        right = [cell for _, cells in rows for cell in cells]
        wrong = ["999"] * len(right)
        return kind, right, wrong
    solution = solutions[key]
    return kind, solution["code"], "print('not yet')"


def built_slugs(vol):
    """The lesson pages the site actually serves, from its built HTML.

    steps_walk.mjs clicks through what a learner is served, not what the
    source happens to contain -- a page dropped from the build (or never
    rebuilt after it was added to the source) must not be walked as if it
    were there, and must not be silently skipped either.
    """
    site_dir = build.SITE / vol["slug"]
    if not site_dir.exists():
        sys.exit(f"{site_dir} does not exist -- run python3 build.py before walking the site")
    return {p.stem for p in site_dir.glob("*.html")}


def answers(unit=None):
    vol = next(v for v in build.VOLS if v["slug"] == VOLUME)
    checks = build.load_json(vol, "_checks.json")
    solutions = build.load_solutions(vol)
    pages = {p.stem: p.read_text() for p in build.chapter_files(vol)}
    built = built_slugs(vol)

    checked_slugs = {key.split("#")[0] for key in checks}
    unbuilt = sorted(checked_slugs - built)
    if unbuilt:
        sys.exit(f"{VOLUME}: checks exist for {unbuilt}, but site/{VOLUME} has no built page "
                 f"for them -- run python3 build.py")

    out, produced, in_scope = [], set(), set()
    for slug in sorted(built):
        text = pages.get(slug)
        if text is None:
            continue
        match = UNIT.match(text)
        if unit and (not match or match.group(1) != str(int(unit))):
            continue
        in_scope.add(slug)
        for number, _, _, code, _ in exercises(blocks_of(text)):
            key = f"{slug}#{number}"
            spec = checks.get(key)
            if not spec:
                continue
            kind, right, wrong = answer_for(slug, number, spec, code, solutions)
            out.append({"slug": slug, "n": number, "kind": kind, "right": right, "wrong": wrong})
            produced.add(key)

    stale = sorted(key for key in checks if key.split("#")[0] in in_scope and key not in produced)
    if stale:
        sys.exit(f"{VOLUME}: checks exist for {stale}, but the built page has no exercise that "
                 f"matches -- stale content, or the site needs rebuilding")
    return out


def main():
    unit = sys.argv[1] if len(sys.argv) > 1 else None
    print(json.dumps(answers(unit)))


if __name__ == "__main__":
    main()
