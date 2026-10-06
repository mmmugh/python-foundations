"""Refuse a repository that tracks a quiz answer key.

    python3 tests/answer_key_guard.py              # the current tree
    python3 tests/answer_key_guard.py --history    # every commit on every ref

The keys are private (docs/specs/public-release.md, decision 2). .gitignore
keeps an accidental `git add -A` from picking them up, but an ignore rule does
not stop `git add -f`, so this is the check that does not depend on it.

A key is recognized two ways, so that renaming one does not hide it: by path,
meaning a directory called answer-keys or a file named *-answers.txt; and by
content, meaning a line that is the answer-key header and nothing else, which
scripts/make_quizzes.py writes into every key. The scripts that merely mention
the header do so inside a longer line, and a test proves they are not flagged.

--history exists because checking only the tree repeats a mistake already made
here once. A key added in one commit and deleted in the next is gone from the
tree and still in the history, which is exactly what a public repository
publishes. The pre-push hook once scanned the net difference of a push for
tokens and let precisely that through.
"""

import os
import subprocess
import sys
from pathlib import PurePosixPath

MARKER = "ANSWER KEY"


def git(repo, *args):
    done = subprocess.run(["git", "-C", repo, "-c", "core.quotePath=false", *args],
                          capture_output=True)
    if done.returncode:
        sys.exit(f"git {' '.join(args)} failed: "
                 f"{done.stderr.decode(errors='replace').strip()}")
    return done.stdout.decode(errors="replace")


def is_key_path(path):
    p = PurePosixPath(path)
    return "answer-keys" in p.parts or p.name.endswith("-answers.txt")


def has_marker(raw):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return any(line.strip() == MARKER for line in text.splitlines())


def tree_findings(top):
    found = []
    for path in git(top, "ls-files", "-z").split("\0"):
        if not path:
            continue
        if is_key_path(path):
            found.append(f"{path}: an answer-key path")
            continue
        full = os.path.join(top, path)
        if os.path.isfile(full):
            with open(full, "rb") as f:
                if has_marker(f.read()):
                    found.append(f"{path}: carries the answer-key header")
    return found


def history_findings(top):
    if git(top, "rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("refusing: this clone is shallow, so most of its history is not here")
    commits = git(top, "rev-list", "--all").split()
    if not commits:
        sys.exit("refusing: no commits found, and an empty history is not a clean one")

    found = []
    paths = set(git(top, "log", "--all", "--format=", "--name-only").splitlines())
    for path in sorted(p for p in paths if p and is_key_path(p)):
        found.append(f"{path}: an answer-key path, somewhere in history")

    grep = subprocess.run(["git", "-C", top, "grep", "-l", "-I", "-E",
                           f"^{MARKER}[[:space:]]*$", *commits, "--"],
                          capture_output=True)
    if grep.returncode not in (0, 1):           # 1 only means no match
        sys.exit(f"git grep failed: {grep.stderr.decode(errors='replace').strip()}")
    first_seen = {}
    for line in grep.stdout.decode(errors="replace").splitlines():
        rev, _, path = line.partition(":")
        first_seen.setdefault(path, rev)
    for path, rev in sorted(first_seen.items()):
        found.append(f"{path} (e.g. at {rev[:7]}): carries the answer-key header")
    return found


def main(argv):
    history = "--history" in argv
    top = git(".", "rev-parse", "--show-toplevel").strip()
    findings = history_findings(top) if history else tree_findings(top)
    scope = "history" if history else "tree"
    for finding in findings:
        print(f"  {finding}")
    print(f"\n{len(findings)} answer-key finding(s) in the {scope}" if findings
          else f"no answer key in the {scope}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
