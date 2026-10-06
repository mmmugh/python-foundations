"""Check scripts/personal_sweep.sh fails safe.

    python3 tests/personal_sweep_test.py

The sweep's job in CI is to never report a clean history it did not check. An
empty secret, or a list of nothing but comments, matches nothing, and matching
nothing is exactly what a clean history looks like. So both must fail, except
on a pull request from a fork, where GitHub withholds secrets by design: that
must say so out loud and exit 0. And a real match must never print what
matched, because the log of a public repository is public.
"""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SWEEP = ROOT / "scripts" / "personal_sweep.sh"
LITERAL = "acme-corp"              # fictional, standing in for a personal string


def repo_with(root, text):
    repo = Path(root) / "repo"
    subprocess.run(["git", "init", "-q", "-b", "main", str(repo)], check=True)
    for key, value in (("user.email", "t@example.invalid"), ("user.name", "t")):
        subprocess.run(["git", "-C", str(repo), "config", key, value], check=True)
    (repo / "notes.md").write_text(text)
    subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-q", "--no-verify", "-m", "c"], check=True)
    return repo


def sweep(repo, patterns, fork=None):
    env = {k: v for k, v in os.environ.items()
           if k not in ("PERSONAL_PATTERNS", "FORK_PULL_REQUEST",
                        "LEAK_PATTERNS", "LEAK_PATTERNS_LOCAL")}
    env["PERSONAL_PATTERNS"] = patterns
    if fork is not None:
        env["FORK_PULL_REQUEST"] = fork
    done = subprocess.run(["sh", str(SWEEP)], cwd=repo, capture_output=True,
                          text=True, env=env)
    return done.returncode, done.stdout + done.stderr


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    with tempfile.TemporaryDirectory() as tmp:
        clean = repo_with(tmp, "ordinary prose\n")

        code, out = sweep(clean, "")
        expect("an empty list fails rather than passing as clean",
               (code, "::error::" in out), (1, True))

        code, out = sweep(clean, "", fork="true")
        expect("an empty list on a fork's pull request skips, loudly",
               (code, "SKIPPED" in out), (0, True))

        code, out = sweep(clean, "# just a comment\n\n   \n")
        expect("a list of only comments and blanks fails too", code, 1)

        code, out = sweep(clean, f"{LITERAL}(\n")
        expect("a list holding a pattern that will not compile fails",
               (code, LITERAL in out.lower()), (1, False))

        code, out = sweep(clean, f"{LITERAL}\n")
        expect("a real list over a clean history passes", code, 0)

    with tempfile.TemporaryDirectory() as tmp:
        leaky = repo_with(tmp, f"we work at {LITERAL.title()}\n")
        code, out = sweep(leaky, f"{LITERAL}\n")
        expect("a match fails the sweep", code, 1)
        expect("...and what matched is never printed", LITERAL in out.lower(), False)

        # A secret pasted with Windows line endings: every pattern then ends
        # in \r, matches nothing, and the history looks clean.
        code, out = sweep(leaky, f"{LITERAL}\r\nsomething-else\r\n")
        expect("a list with CRLF line endings still finds the match", code, 1)

    bad = 0
    for label, ok, got, want in results:
        if not ok:
            bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'the personal sweep never calls an unchecked history clean' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
