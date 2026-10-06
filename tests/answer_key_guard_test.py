"""Check tests/answer_key_guard.py catches a committed answer key, and only that.

    python3 tests/answer_key_guard_test.py

Each case builds a throwaway repository in a temp directory and runs the guard
inside it. Nothing here touches this repository.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

GUARD = Path(__file__).resolve().parent / "answer_key_guard.py"
# Escaped rather than written as a block of lines on purpose: a tracked file
# holding the header as a line of its own is exactly what the guard flags, and
# this file is tracked.
KEY_TEXT = "PYTHON FOUNDATIONS\nChapter 1 - Your First Programs\n\nANSWER KEY\n\n1. print\n"


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def new_repo(root, name="repo"):
    repo = Path(root) / name
    subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
    git(repo, "config", "user.email", "t@example.invalid")
    git(repo, "config", "user.name", "t")
    return repo


def commit(repo, files, message="change"):
    for name, text in files.items():
        if text is None:
            git(repo, "rm", "-q", name)
            continue
        path = repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        git(repo, "add", "-f", name)        # -f: these cases mean to defeat .gitignore
    git(repo, "commit", "-q", "-m", message)


def guard(repo, *args):
    done = subprocess.run([sys.executable, str(GUARD), *args], cwd=repo,
                          capture_output=True, text=True)
    return done.returncode, done.stdout + done.stderr


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, {"README.md": "hello\n"})
        expect("a clean tree passes", guard(repo)[0], 0)

        commit(repo, {"tests/stdin_answers.py": "A = {}\n"})
        expect("test fixtures named *_answers.py stay public", guard(repo)[0], 0)

        commit(repo, {"build.py": 'ANSWER_MARKER = "ANSWER KEY"\n'})
        expect("a script that merely mentions the header is not flagged", guard(repo)[0], 0)

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, {"volumes/v/answer-keys/ch01.txt": "anything\n"})
        expect("anything under an answer-keys directory is caught", guard(repo)[0], 1)

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, {"notes/ch01-intro-answers.txt": "anything\n"})
        expect("a file named *-answers.txt is caught wherever it is", guard(repo)[0], 1)

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, {"notes/chapter-one.txt": KEY_TEXT})
        expect("a renamed key is caught by its header", guard(repo)[0], 1)

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, {"README.md": "hello\n"})
        commit(repo, {"answer-keys/ch01-intro-answers.txt": KEY_TEXT}, "add a key")
        commit(repo, {"answer-keys/ch01-intro-answers.txt": None}, "remove it again")
        expect("a key added then deleted leaves the tree clean", guard(repo)[0], 0)
        code, out = guard(repo, "--history")
        expect("...and --history still finds it", code, 1)

        shallow = Path(tmp) / "shallow"
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{repo}", str(shallow)],
                       check=True)
        code, out = guard(shallow, "--history")
        expect("--history refuses a shallow clone", (code != 0, "shallow" in out), (True, True))

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        code, out = guard(repo, "--history")
        expect("--history refuses a repository with no commits",
               (code != 0, "no commits" in out), (True, True))

    bad = 0
    for label, ok, got, want in results:
        if not ok:
            bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'the answer-key guard catches keys and nothing else' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
