"""Check scripts/scan_history.py scans every commit, not the final tree.

    python3 tests/scan_history_test.py

Builds throwaway repositories in a temp directory. The case that matters most
is a leak added in one commit and deleted in the next: the final tree is clean,
and a scanner that only reads the tree reports it clean. A public repository
publishes every commit, so this must not.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "scan_history.py"
# Assembled from pieces: a file containing it literally could not be committed
# through the hooks this tests.
GH_TOKEN = "ghp_" + "a" * 36
LITERAL = "acme-corp"              # fictional, standing in for a personal string


def git(repo, *args):
    done = subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True)
    return done.stdout.strip()


def new_repo(root, name="repo"):
    repo = Path(root) / name
    subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
    git(repo, "config", "user.email", "t@example.invalid")
    git(repo, "config", "user.name", "t")
    return repo


def commit(repo, name, text, message):
    path = repo / name
    if text is None:
        git(repo, "rm", "-q", name)
    else:
        path.write_text(text)
        git(repo, "add", name)
    git(repo, "commit", "-q", "--no-verify", "-m", message)
    return git(repo, "rev-parse", "--short=7", "HEAD")


def run(repo, *args, **env_extra):
    env = dict(os.environ)
    # The developer's own personal list must not leak into these cases.
    env["LEAK_PATTERNS_LOCAL"] = "/dev/null"
    env.update(env_extra)
    done = subprocess.run([sys.executable, str(SCRIPT), "--repo", str(repo), *args],
                          capture_output=True, text=True, env=env)
    return done.returncode, done.stdout + done.stderr


def main():
    results = []

    # A "found" case checks the summary as well as the exit code: the scan also
    # exits 1 when it refuses to scan at all (a shallow clone, no commits), and
    # a refusal must not pass for a match.
    def expect(label, got, want):
        results.append((label, got == want, got, want))

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        clean = commit(repo, "a.md", "hello\n", "clean")
        leak = commit(repo, "s.md", f"token={GH_TOKEN}\n", "leak")
        gone = commit(repo, "s.md", None, "remove it again")

        code, out = run(repo)
        expect("a leak deleted in a later commit is still found", code, 1)
        expect("...and the leaking commit is named", leak in out, True)
        expect("...and the clean ones are not", (clean in out, gone in out), (False, False))
        expect("...and the summary counts it", "1 blocked" in out, True)
        expect("unredacted, a person sees the match", GH_TOKEN in out, True)

        code, out = run(repo, "--redact")
        expect("redacted, it is still found", code, 1)
        expect("redacted, the token is never printed", GH_TOKEN in out, False)
        expect("redacted, it says so", "redacted" in out, True)

        shallow = Path(tmp) / "shallow"
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{repo}", str(shallow)],
                       check=True)
        code, out = run(shallow)
        expect("a shallow clone is refused, not scanned",
               (code != 0, "shallow" in out), (True, True))

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, "a.md", "hello\n", "clean")
        commit(repo, "b.md", "more prose\n", "clean too")
        code, out = run(repo)
        expect("a clean history passes", (code, "none blocked" in out), (0, True))

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        code, out = run(repo)
        expect("a repository with no commits is refused",
               (code != 0, "no commits" in out), (True, True))

    with tempfile.TemporaryDirectory() as tmp:
        repo = new_repo(tmp)
        commit(repo, "a.md", f"we work at {LITERAL.title()}\n", "personal")
        listfile = Path(tmp) / "list"
        listfile.write_text(f"{LITERAL}\n")
        code, out = run(repo, "--redact", LEAK_PATTERNS="/dev/null",
                        LEAK_PATTERNS_LOCAL=str(listfile))
        expect("a personal list from the environment is used",
               (code, "1 blocked" in out), (1, True))
        expect("...and its match is never printed when redacted",
               LITERAL in out.lower(), False)

    # A merge can introduce content of its own, in a conflict resolution or
    # an "evil merge". git diff-tree shows a merge's diff only when asked
    # (-m), so without it this commit would be skipped.
    with tempfile.TemporaryDirectory() as tmp:
        listfile = Path(tmp) / "list"
        listfile.write_text(f"{LITERAL}\n")
        repo = new_repo(tmp)
        commit(repo, "a.md", "hello\n", "base")
        git(repo, "checkout", "-q", "-b", "side")
        commit(repo, "b.md", "side\n", "side")
        git(repo, "checkout", "-q", "main")
        commit(repo, "c.md", "main\n", "main")
        git(repo, "merge", "-q", "--no-ff", "--no-commit", "side")
        (repo / "d.md").write_text(f"slipped in at {LITERAL}\n")
        git(repo, "add", "d.md")
        git(repo, "commit", "-q", "--no-verify", "-m", "merge side")
        merge = git(repo, "rev-parse", "--short=7", "HEAD")
        code, out = run(repo, "--redact", LEAK_PATTERNS="/dev/null",
                        LEAK_PATTERNS_LOCAL=str(listfile))
        expect("a leak introduced only by a merge commit is found",
               (code, merge in out), (1, True))

    # git octal-escapes a non-ASCII filename unless core.quotePath is off,
    # and no pattern for the real name matches the escaped one.
    with tempfile.TemporaryDirectory() as tmp:
        accented = "caf\u00e9-corp"
        listfile = Path(tmp) / "list"
        listfile.write_text(f"{accented}\n", encoding="utf-8")
        repo = new_repo(tmp)
        commit(repo, f"{accented.title()} plan.md", "nothing in the body\n", "add")
        code, out = run(repo, "--redact", LEAK_PATTERNS="/dev/null",
                        LEAK_PATTERNS_LOCAL=str(listfile))
        expect("a personal literal in a non-ASCII filename is found",
               (code, "1 blocked" in out), (1, True))

    # A commit publishes more than its diff: its message, and the name and
    # address of whoever wrote and committed it. Neither the diff scan nor
    # gitleaks reads those, so this does.
    with tempfile.TemporaryDirectory() as tmp:
        listfile = Path(tmp) / "list"
        listfile.write_text(f"{LITERAL}\n")
        personal = {"LEAK_PATTERNS": "/dev/null", "LEAK_PATTERNS_LOCAL": str(listfile)}

        repo = new_repo(tmp, "message")
        commit(repo, "a.md", "hello\n", f"notes from the {LITERAL.title()} offsite")
        code, out = run(repo, "--redact", **personal)
        expect("a personal literal in a commit message is found",
               (code, "1 blocked" in out), (1, True))
        expect("...and is never printed when redacted", LITERAL in out.lower(), False)

        repo = new_repo(tmp, "token-message")
        commit(repo, "a.md", "hello\n", f"rotate {GH_TOKEN}")
        code, out = run(repo)
        expect("a token in a commit message is found",
               (code, "1 blocked" in out), (1, True))

        repo = new_repo(tmp, "identity")
        git(repo, "config", "user.name", f"someone at {LITERAL}")
        commit(repo, "a.md", "hello\n", "ordinary")
        code, out = run(repo, "--redact", **personal)
        expect("a personal literal in the author's name is found",
               (code, "1 blocked" in out), (1, True))

        repo = new_repo(tmp, "session")
        commit(repo, "a.md", "hello\n", "docs: x\n\nClaude-Session: https://claude.ai/code/"
               + "session_" + "0aB1cD2eF3gH")
        code, out = run(repo, "--redact")
        expect("a session URL in a message is found by the generic patterns",
               (code, "1 blocked" in out), (1, True))

        repo = new_repo(tmp, "plain")
        commit(repo, "a.md", "hello\n", "ordinary")
        code, out = run(repo, "--redact", **personal)
        expect("an ordinary message and identity pass", code, 0)

    bad = 0
    for label, ok, got, want in results:
        if not ok:
            bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'every commit is scanned, and nothing it cannot see is called clean' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
