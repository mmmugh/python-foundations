"""Check the practice pages against the two promises they make.

    python3 tests/practice_test.py

A practice page says: here is one project, built in steps, solvable with what
you have met so far. That is two claims, and both are easy to break by
accident while writing prose.

1. Nothing is used before it is taught. The vocabulary is not a table kept by
   hand -- it is derived from the course itself. Everything the chapters up to
   and including chapter N actually show in a code fence is fair game at
   chapter N, and anything else is not. A hand-written table would drift; this
   cannot, because it IS the course.

   It caught a real one straight away: a worked solution for chapter 4 used a
   conditional expression, which nothing before chapter 5 shows.

2. Every worked solution passes its own check. Nothing else runs these --
   validate_shipped.mjs exercises the fixtures in reference_solutions.py, not
   the solutions a reader is shown -- so without this a solution can quietly
   stop working, and the first to find out is a student who opens it while
   stuck.
"""

import ast
import builtins
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "web"))
import box_runner                                               # noqa: E402
import build                                                    # noqa: E402

BUILTINS = set(dir(builtins))


def harvest(source, into):
    """Add every construct `source` uses to `into`. False if it will not parse."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    for node in ast.walk(tree):
        into["nodes"].add(type(node).__name__)
        if isinstance(node, ast.Attribute):
            into["attrs"].add(node.attr)
        # Builtins only. A learner invents their own variable names, and
        # "wind" not appearing in chapter 3 says nothing about anything.
        if isinstance(node, ast.Name) and node.id in BUILTINS:
            into["names"].add(node.id)
    return True


def fences(path):
    text = re.sub(r"^<!-- part: .+ -->\n", "", path.read_text())
    return [code for kind, code in build.split_blocks(text.split("\n"))
            if kind == "code"]


def vocabulary(vol):
    """{chapter number: everything the course has shown by the end of it}."""
    cumulative, seen = {}, {"nodes": set(), "names": set(), "attrs": set()}
    for path in build.chapter_files(vol):
        if not re.match(r"^ch\d\d-", path.stem):
            continue
        for code in fences(path):
            harvest(code, seen)          # fences that raise on purpose may not parse
        cumulative[int(path.stem[2:4])] = {k: set(v) for k, v in seen.items()}
    return cumulative


def run_check(spec, code):
    if spec["kind"] == "output":
        return box_runner.check_output(code, spec["expected"])
    if spec["kind"] == "stdin":
        return box_runner.check_stdin(code, spec["runs"])
    if spec["kind"] == "function":
        return box_runner.check_function(
            code, spec["name"], [(tuple(a), e) for a, e in spec["cases"]])
    return None


def main():
    problems = []
    for vol in build.VOLS:
        pages = build.practice_files(vol)
        if not pages:
            continue
        print(f"{vol['slug']}: {len(pages)} practice page(s)")
        known = vocabulary(vol)
        solutions = build.load_solutions(vol)
        checks = json.loads((vol["content"] / "_checks.json").read_text())

        for path in pages:
            chapter = int(path.stem[2:4])
            slug = f"{path.stem}-practice"
            mine = {k: v for k, v in solutions.items() if k.startswith(f"{slug}#")}
            if not mine:
                problems.append(f"{slug}: no worked solutions at all")
                continue

            late = checked = 0
            for key, entry in sorted(mine.items()):
                used = {"nodes": set(), "names": set(), "attrs": set()}
                if not harvest(entry["code"], used):
                    problems.append(f"{key}: the solution does not parse")
                    continue
                for kind in ("nodes", "names", "attrs"):
                    extra = sorted(used[kind] - known[chapter][kind])
                    if extra:
                        late += 1
                        problems.append(f"{key}: uses {kind} the course has not "
                                        f"shown by chapter {chapter}: {extra}")
                spec = checks.get(key)
                if spec:
                    result = run_check(spec, entry["code"])
                    if result is not None:
                        checked += 1
                        ok, why = result
                        if not ok:
                            problems.append(f"{key}: the worked solution fails its "
                                            f"own check -- {why[0] if why else ''}")
            print(f"  {slug:<44} {len(mine):>2} steps, {checked:>2} checked, "
                  f"{'nothing early' if not late else str(late) + ' TOO EARLY'}")

    for line in problems:
        print(f"  !! {line}")
    print(f"\n{'the practice pages keep their promises' if not problems else str(len(problems)) + ' problem(s)'}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
