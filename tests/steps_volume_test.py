"""Check the step-by-step lessons keep the promises the spec makes for them.

    python3 tests/steps_volume_test.py                 # the whole volume
    python3 tests/steps_volume_test.py --only ch02a-naming-a-value

docs/specs/step-by-step-course.md sets a shape for every lesson so that a
beginner meets one idea at a time, practices it at once, and is never handed
a finished answer: a warm-up, practice after each idea, one try it whose hints
walk the problem-solving routine in order, a worked solution behind them, and
a three-line wrap-up. Every exercise has a check or a worked solution, every
worked solution passes its own check, and so does an answer in a different
style, because a check that fails a correct answer teaches the wrong lesson.
The size caps stand in for "20 to 30 minutes": a lesson that outgrows them is
two lessons.
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
from practice_test import run_check                             # noqa: E402

VOLUME = "vol1-steps"
REFERENCE = "99-how-to-start-a-problem"
LESSONS = [
    # (slug, heading, the routine steps the try it's hints walk, in order).
    # No steps means the routine has not arrived yet: the hints are plain.
    ("ch01a-printing", "Lesson 1.1 — Printing", ()),
    ("ch01b-numbers-and-comments", "Lesson 1.2 — Numbers and comments", ()),
    ("ch01c-errors-and-a-receipt", "Lesson 1.3 — When things go wrong, and a receipt",
     ("Say it", "Split it")),
    ("ch02a-naming-a-value", "Lesson 2.1 — Naming a value", ("Say it", "Split it")),
    ("ch02b-names-and-kinds", "Lesson 2.2 — Names that explain, and kinds of value",
     ("Say it", "Split it", "Name it")),
    ("ch02c-asking-the-user", "Lesson 2.3 — Asking the user",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch02d-putting-it-together", "Lesson 2.4 — Putting it together",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch03a-more-arithmetic", "Lesson 3.1 — More arithmetic",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch03b-order-and-rounding", "Lesson 3.2 — Order of operations, and rounding",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch03c-formatting", "Lesson 3.3 — Formatting output",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch03d-joining-text", "Lesson 3.4 — Joining and repeating text",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch03e-comparing", "Lesson 3.5 — Comparing values",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch03f-combining-and-change", "Lesson 3.6 — Combining conditions, and the change machine",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch04a-if-and-else", "Lesson 4.1 — If, and else",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch04b-elif-and-rules", "Lesson 4.2 — Elif, and turning a rule into code",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch04c-nesting-and-truthiness", "Lesson 4.3 — Nesting, and what counts as true",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch04d-checking-input", "Lesson 4.4 — Checking input",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch04e-the-ticket-kiosk", "Lesson 4.5 — The ticket kiosk",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch05a-while", "Lesson 5.1 — Repeating with while",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch05b-for-and-range", "Lesson 5.2 — For, and range()",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch05c-looping-over-text", "Lesson 5.3 — Looping over a string",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch05d-loops-inside-loops", "Lesson 5.4 — Loops inside loops",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch05e-adding-up", "Lesson 5.5 — Adding up as you go",
     ("Say it", "Split it", "Name it", "Check it")),
    ("ch05f-until-a-stop-value", "Lesson 5.6 — Until a stop value, and break",
     ("Say it", "Split it", "Name it", "Check it")),
]
MAX_EXERCISES = 10
MAX_WORDS = 1300
STEPS = ("Say it", "Split it", "Name it", "Build it", "Check it")


def blocks_of(text):
    return build.split_blocks(re.sub(r"^<!-- part: .+ -->\n", "", text).split("\n"))


def exercises(blocks):
    """[(number, section, text, code, hints)], numbered through the page as the build does."""
    found, section = [], None
    for kind, payload in blocks:
        if kind == "h3":
            section = payload if payload in build.EXERCISE_SECTIONS else None
        elif section and kind in ("ol", "ul"):
            for item in payload:
                found.append([len(found) + 1, section, item, "", []])
        elif section and kind == "code" and found:
            found[-1][3] = payload
        elif section and kind == "quote" and found:
            found[-1][4].append(payload)
    return [tuple(x) for x in found]


def prose_words(blocks):
    words = 0
    for kind, payload in blocks:
        if kind in ("p", "quote"):
            words += len(payload.split())
        elif kind in ("ol", "ul"):
            words += sum(len(item.split()) for item in payload)
    return words


def is_awkward(value):
    """0, "", [], {} or a negative number -- the kind of input Check it asks
    a learner to try on purpose, because it is where an off-by-one or an
    unguarded division shows up."""
    if isinstance(value, bool):
        return False
    if isinstance(value, (int, float)):
        return value <= 0
    return value in ("", [], {})


def lesson_problems(slug, heading, hint_steps, text, checks, solutions, alternates):
    problems = []
    say = problems.append
    if not re.match(r"<!-- part: Unit \d+ — .+ -->\n", text):
        say(f"{slug}: the first line must name its unit: <!-- part: Unit N — Title -->")
    blocks = blocks_of(text)
    if next((p for k, p in blocks if k == "h2"), None) != heading:
        say(f"{slug}: the heading must be {heading!r}")

    h3 = [p for k, p in blocks if k == "h3"]
    has_warmup = "Warm-up" in h3
    # The course's first lesson has nothing before it to warm up on.
    no_warmup = slug == LESSONS[0][0]
    if no_warmup and has_warmup:
        say(f"{slug}: nothing comes before it to warm up on, so it has no warm-up")
    if not no_warmup and (not h3 or h3[0] != "Warm-up"):
        say(f"{slug}: the first section must be the warm-up")
    if "Practice" not in h3:
        say(f"{slug}: needs a practice after its new idea")
    if h3.count("Try It") != 1:
        say(f"{slug}: needs exactly one Try It")
    if not h3 or h3[-1] != "What you can do now":
        say(f"{slug}: must end with 'What you can do now'")
    else:
        tail = blocks[[i for i, (k, p) in enumerate(blocks) if k == "h3" and p == h3[-1]][0] + 1:]
        lists = [p for k, p in tail if k in ("ol", "ul")]
        if not lists or len(lists[0]) != 3:
            say(f"{slug}: the wrap-up is three lines")
        if not any(k == "p" and p.startswith("Key words:") for k, p in tail):
            say(f"{slug}: the wrap-up names its key words ('Key words: ...')")

    found = exercises(blocks)
    if len(found) > MAX_EXERCISES:
        say(f"{slug}: {len(found)} exercises; a 20-to-30-minute lesson has at most {MAX_EXERCISES}")
    words = prose_words(blocks)
    if words > MAX_WORDS:
        say(f"{slug}: {words} words of prose; at most {MAX_WORDS}")

    for number, section, item, code, hints in found:
        key = f"{slug}#{number}"
        spec, solution = checks.get(key), solutions.get(key)
        if not spec and not solution:
            say(f"{key}: has neither a check nor a worked solution")
        # A check that passes the starting code says "Correct" to a learner
        # who changed nothing: it cannot see what the exercise asks for.
        if spec and code and spec["kind"] not in ("predict", "trace", "choice"):
            untouched = run_check(spec, code)
            if untouched is not None and untouched[0]:
                say(f"{key}: its check passes the starting code unchanged")
        if spec and spec["kind"] == "function":
            if not any(is_awkward(a) for case in spec["cases"] for a in case[0]):
                say(f"{key}: a function check needs an awkward case (0, empty or negative)")
        for label, answer in (("worked solution", solution and solution["code"]),
                              ("alternate answer", alternates.get(key))):
            if spec and answer:
                result = run_check(spec, answer)
                if result is not None and not result[0]:
                    say(f"{key}: the {label} fails its own check -- {result[1][0] if result[1] else ''}")
        if section == "Try It":
            if [h.split(":")[0] for h in hints[:len(hint_steps)]] != list(hint_steps):
                say(f"{key}: the hints must walk {', '.join(hint_steps)}, in that order")
            # Before the routine arrives (no steps), the hints are plain: they
            # neither link its page nor name its steps in the worked solution.
            if not hints:
                say(f"{key}: a try it has hints, revealed one at a time")
            elif hint_steps and f"({REFERENCE}.html)" not in hints[0]:
                say(f"{key}: the first hint links to the reference page")
            if not solution:
                say(f"{key}: a try it ends in a worked solution")
            elif hint_steps and ("# Say it" not in solution["code"] or "# Split it" not in solution["code"]):
                say(f"{key}: the worked solution keeps its Say it and Split it comments")
            if spec and key not in alternates:
                say(f"{key}: a checked try it needs an alternate answer in _alternates.json")
    return problems


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def trace_problems(slug, text, checks, shown):
    """A trace exercise is a one-step change from a worked trace table: no
    wider than one already shown, and with "not set yet" cells only once a
    worked table has shown one. `shown` carries what earlier pages showed."""
    problems = []
    for kind, payload in blocks_of(text):
        if kind == "table" and cells(payload[0])[0] == "After line":
            body = [cells(r) for r in payload[2:]]
            shown["width"] = max(shown["width"], len(cells(payload[0])) - 1)
            shown["blank"] = shown["blank"] or any(c in ("", "-") for r in body for c in r[1:])
    for number, _, _, code, _ in exercises(blocks_of(text)):
        spec = checks.get(f"{slug}#{number}", {})
        if spec.get("kind") != "trace":
            continue
        if len(spec["names"]) > shown["width"]:
            problems.append(f"{slug}#{number}: traces {len(spec['names'])} variables; no worked "
                            f"table before it shows more than {shown['width']}")
        blanks = any(c == "" for _, row in box_runner.trace_rows(code, spec["names"]) for c in row)
        if blanks and not shown["blank"]:
            problems.append(f"{slug}#{number}: has 'not set yet' cells, which no worked table "
                            f"before it shows")
    return problems


def unit_problems(pages, checks):
    """What the spec asks of each unit as a whole, and of unit 2's lessons."""
    problems = []
    # The spec gives every unit one fix-the-bug practice from a real error.
    # Units are read from LESSONS, so a unit is held to it once it has a lesson.
    for number in sorted({slug[2:4] for slug, *_ in LESSONS}):
        mine = {slug: exercises(blocks_of(text)) for slug, text in pages.items()
                if slug.startswith(f"ch{number}")}
        # A fix-the-bug practice hands over broken code and checks the fixed
        # program by running it: a question that only names an error is not one.
        if not any("error" in item.lower() and code
                   and checks.get(f"{slug}#{n}", {}).get("kind") in ("output", "stdin", "function")
                   for slug, items in mine.items() for n, _, item, code, _ in items):
            problems.append(f"unit {int(number)}: needs a checked fix-the-bug practice that starts from an error")
    unit = {slug: text for slug, text in pages.items() if slug.startswith("ch02")}
    found = {slug: exercises(blocks_of(text)) for slug, text in unit.items()}
    if not any(checks.get(f"ch02a-naming-a-value#{n}", {}).get("kind") == "trace"
               for n, *_ in found.get("ch02a-naming-a-value", [])):
        problems.append("ch02a-naming-a-value: tracing starts here, with a trace table")
    if not any(re.search(r"\b(True|False)\b", json.dumps(checks.get(f"ch02b-names-and-kinds#{n}", {})) + code)
               for n, _, _, code, _ in found.get("ch02b-names-and-kinds", [])):
        problems.append("ch02b-names-and-kinds: True and False get a practice of their own")
    receipt = [code for k, code in blocks_of(unit.get("ch02d-putting-it-together", ""))
               if k == "code" and "input(" in code and "total" in code]
    examples = [code for k, code in blocks_of(unit.get("ch02d-putting-it-together", "")) if k == "code"]
    in_exercises = {code for *_, code, _ in found.get("ch02d-putting-it-together", [])}
    if [c for c in receipt if c in examples and c not in in_exercises]:
        problems.append("ch02d-putting-it-together: the finished receipt is shown in an example")
    return problems


def main():
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    vol = next((v for v in build.VOLS if v["slug"] == VOLUME), None)
    if vol is None:
        print(f"  FAIL  volumes/{VOLUME} does not exist\n\n1 wrong")
        sys.exit(1)
    meta = json.loads((vol["dir"] / "volume.json").read_text())
    checks = build.load_json(vol, "_checks.json")
    solutions = build.load_solutions(vol)
    alternates = build.load_json(vol, "_alternates.json")
    pages = {p.stem: p.read_text() for p in build.chapter_files(vol)}
    problems = []
    shown = {"width": 0, "blank": False}

    for slug, heading, steps in LESSONS:
        if only and slug not in only:
            # Still read it: what its worked tables show counts for later lessons.
            if slug in pages:
                trace_problems(slug, pages[slug], checks, shown)
            continue
        if slug not in pages:
            problems.append(f"{slug}: missing")
            continue
        problems += lesson_problems(slug, heading, steps, pages[slug], checks, solutions, alternates)
        problems += trace_problems(slug, pages[slug], checks, shown)

    if not only or REFERENCE in only:
        text = pages.get(REFERENCE, "")
        if not text.startswith("## How to start a problem"):
            problems.append(f"{REFERENCE}: missing, or not headed 'How to start a problem'")
        for step in STEPS:
            if f"### {step}" not in text:
                problems.append(f"{REFERENCE}: no section for {step}")

    if not only:
        if not meta.get("lessons") or meta.get("status") != "in progress":
            problems.append('volume.json: needs "lessons": true and "status": "in progress"')
        order = [slug for slug, *_ in LESSONS] + [REFERENCE]
        if list(pages) != order:
            problems.append(f"the pages, in reading order, must be {order}; found {list(pages)}")
        problems += unit_problems(pages, checks)
        # Options are never shuffled, so a pattern in where the right one sits
        # would pass a learner who learned the pattern, not the idea.
        answers = [spec["answer"] for spec in checks.values() if spec.get("kind") == "choice"]
        if answers and max(answers.count(i) for i in set(answers)) > 2 * len(answers) / 3:
            problems.append(f"choice answers sit at the same option too often: {answers}")
        for path in sorted(vol["dir"].rglob("*")):
            if path.is_file() and "claude.ai" in path.read_text(errors="replace"):
                problems.append(f"{path.relative_to(ROOT)}: the public course never links to claude.ai")

    for line in problems:
        print(f"  !! {line}")
    print(f"\n{'the lessons keep their promises' if not problems else str(len(problems)) + ' problem(s)'}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
