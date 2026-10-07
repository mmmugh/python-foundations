"""Check .githooks/commit-msg refuses a message that matches a deny pattern.

    python3 tests/commit_msg_test.py

pre-commit and pre-push read diffs, and a commit message is published with the
commit all the same. This builds a throwaway repository wired to this repo's
hooks, with a fictional personal list, and commits through real git. A refused
commit must leave nothing behind.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Assembled from pieces, like every leak-shaped fixture here: written out, they
# would trip the hooks on the commit that adds this file.
SESSION_URL = "https://claude.ai/code/" + "session_" + "0aB1cD2eF3gH"
GH_TOKEN = "ghp_" + "a" * 36
LITERAL = "acme-corp"              # fictional, standing in for a personal string


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
        for key, value in (("user.email", "t@example.invalid"), ("user.name", "t"),
                           ("core.hooksPath", str(ROOT / ".githooks"))):
            subprocess.run(["git", "-C", str(repo), "config", key, value], check=True)
        listfile = Path(tmp) / "list"
        listfile.write_text(f"{LITERAL}\n")
        env = dict(os.environ, LEAK_PATTERNS_LOCAL=str(listfile))
        made = []

        def commit(message):
            name = f"f{len(made) + len(results)}.md"
            (repo / name).write_text("an ordinary line\n")
            subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
            done = subprocess.run(["git", "-C", str(repo), "commit", "-q", "-F", "-"],
                                  input=message, text=True, capture_output=True, env=env)
            if done.returncode == 0:
                made.append(name)
            return done.returncode == 0

        expect("an ordinary message is committed",
               commit("docs: ordinary\n\nCo-Authored-By: Someone <noreply@example.com>\n"), True)
        expect("a Claude-Session trailer is refused",
               commit(f"docs: x\n\nClaude-Session: {SESSION_URL}\n"), False)
        expect("a token in a message is refused", commit(f"fix: rotate {GH_TOKEN}\n"), False)
        expect("a personal literal in a message is refused",
               commit(f"notes from the {LITERAL.title()} offsite\n"), False)
        expect("the placeholder the history was scrubbed to is allowed",
               commit("docs: y\n\nClaude-Session: <session URL>\n"), True)
        count = subprocess.run(["git", "-C", str(repo), "rev-list", "--count", "HEAD"],
                               capture_output=True, text=True).stdout.strip()
        expect("only the two allowed commits exist", count, "2")

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'a message is scanned before the commit exists' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
