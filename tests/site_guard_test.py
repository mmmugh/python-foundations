"""Check the build keeps the answer keys off the site.

    python3 tests/site_guard_test.py

The keys are public in the repository (spec decision 2, reversed), but not on
the site: everything under site/ is fetchable by guessing a filename, and a
course page that hands out its answers is a worse course. Two layers stand
between a key and site/: copy_quizzes() copies by whitelist, and
assert_nothing_private_published() fails the build if anything published
carries the answer-key marker. This builds into a temporary directory and
checks each layer, and that the second catches what slips past the first.
"""

import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build                                                    # noqa: E402

QUIZ = "Chapter 1 quiz\n\n1. What does print() do?\n"
KEY = f"Chapter 1 quiz\n{build.ANSWER_MARKER}\n\n1. It writes to the screen.\n"


def guard_refuses():
    """The guard's verdict on the current build.SITE: the message, or None."""
    try:
        build.assert_nothing_private_published()
    except SystemExit as stop:
        return str(stop)
    return None


def main():
    results = []

    def expect(label, ok):
        results.append((label, ok))

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        source = tmp / "quizzes-source"
        source.mkdir()
        (source / "ch01-quiz.txt").write_text(QUIZ)
        (source / "ch01-answers.txt").write_text(KEY)
        build.SITE = tmp / "site"
        (build.SITE / "vol1").mkdir(parents=True)
        build.copy_quizzes({"slug": "vol1", "quizzes": source})
        copied = sorted(p.name for p in (build.SITE / "vol1" / "quizzes").iterdir())
        expect("copy_quizzes copies the quiz and not its key", copied == ["ch01-quiz.txt"])
        expect("a site holding only quizzes builds", guard_refuses() is None)

        # A key named like a quiz gets past the whitelist; the marker must not.
        (source / "ch02-quiz.txt").write_text(KEY)
        build.copy_quizzes({"slug": "vol1", "quizzes": source})
        refused = guard_refuses()
        expect("a key misnamed as a quiz is copied, and the build refuses it",
               refused is not None and "ch02-quiz.txt" in refused)
        (build.SITE / "vol1" / "quizzes" / "ch02-quiz.txt").unlink()

        # The same marker inside a Word document, which is a zip of XML.
        doc = build.SITE / "vol1" / "course.docx"
        with zipfile.ZipFile(doc, "w") as archive:
            archive.writestr("word/document.xml", f"<w:t>{build.ANSWER_MARKER}</w:t>")
        refused = guard_refuses()
        expect("a key inside a .docx is refused", refused is not None and "course.docx" in refused)

    keys = sorted((ROOT / "volumes").glob("*/answer-keys/*-answers.txt"))
    unmarked = [k.name for k in keys if build.ANSWER_MARKER not in k.read_text()]
    expect(f"every real answer key carries the marker the guard looks for ({len(keys)} keys)",
           len(keys) == 12 and not unmarked)

    bad = 0
    for label, ok in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")
    print(f"\n{'no answer key reaches the site' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
