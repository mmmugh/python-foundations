"""Run leak-scan over every commit in a repository's history.

    python3 scripts/scan_history.py [--redact] [--repo PATH]

Exists because scanning history is easy to get wrong in a way that looks
right. `git diff <empty tree> HEAD | leak-scan` reads like a history scan and
only scans the final tree, so a leak added and deleted in between is invisible
to it. That mistake was made once already, in this repository's first audit.
This scans each commit's own diff, which is what a public repository actually
publishes, and with it the parts of a commit that are not in any diff: its
message, and the name and address of its author and committer. gitleaks reads
none of those, so nothing else here would.

It refuses, rather than reporting clean, when it cannot see the history: no
commits at all, or a shallow clone, where everything before the cut-off is
missing and an empty result would mean nothing.

--redact sets LEAK_SCAN_REDACT for the scanner, so a match prints the commit
and a count, never the matched text or a path. CI uses it, because a public
repository's CI logs are public. Patterns come from the scanner's usual
places, or from LEAK_PATTERNS / LEAK_PATTERNS_LOCAL in the environment.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

SCAN = Path(__file__).resolve().parent.parent / ".githooks" / "leak-scan"


def git(repo, *args):
    done = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if done.returncode:
        sys.exit(f"git {' '.join(args)} failed: {done.stderr.strip()}")
    return done.stdout


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run leak-scan over every commit.")
    parser.add_argument("--redact", action="store_true",
                        help="never print matched text or paths (for CI)")
    parser.add_argument("--repo", default=".",
                        help="repository to scan (default: the current directory)")
    args = parser.parse_args(argv)

    if git(args.repo, "rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("refusing: this clone is shallow, so most of its history is not here. "
                 "Fetch it in full (in CI, actions/checkout with fetch-depth: 0).")
    commits = git(args.repo, "rev-list", "--all").split()
    if not commits:
        sys.exit("refusing: no commits found, and an empty history is not a clean one")

    env = dict(os.environ)
    if args.redact:
        env["LEAK_SCAN_REDACT"] = "1"

    blocked = 0
    for commit in commits:
        # --root shows a first commit against the empty tree, -m shows a merge
        # against each parent, and quotePath off keeps a non-ASCII filename
        # readable to the patterns rather than octal-escaped past them.
        diff = subprocess.run(
            ["git", "-C", args.repo, "-c", "core.quotePath=false", "diff-tree",
             "-p", "-U0", "--root", "-m", "--no-color", commit],
            capture_output=True)
        if diff.returncode:
            sys.exit(f"git diff-tree failed on {commit[:7]}")
        # The message and the identities follow the diff as one more added
        # file. The "diff --git" line closes whatever hunk came before, so the
        # scanner reads them as added lines and as nothing else.
        meta = subprocess.run(
            ["git", "-C", args.repo, "show", "-s",
             "--format=%an <%ae>%n%cn <%ce>%n%B", commit],
            capture_output=True)
        if meta.returncode:
            sys.exit(f"git show failed on {commit[:7]}")
        added = b"".join(b"+" + line + b"\n" for line in meta.stdout.splitlines())
        text = diff.stdout + b"diff --git a/.commit b/.commit\n@@ -0,0 +1 @@\n" + added
        scan = subprocess.run([str(SCAN)], input=text, capture_output=True, env=env)
        if scan.returncode:
            blocked += 1
            print(f"  {commit[:7]}  {scan.stderr.decode(errors='replace').strip()}")

    print(f"\n{len(commits)} commits scanned, "
          f"{'none blocked' if not blocked else str(blocked) + ' blocked'}")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
