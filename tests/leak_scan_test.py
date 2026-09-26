"""Check that .githooks/leak-scan blocks what it claims to, and nothing else.

    python3 tests/leak_scan_test.py

The scan guards a repo that is going public, so the cost of it silently
failing open is high and the failure is invisible: a scan that matches nothing
looks exactly like a clean commit. Its scope is also subtler than it appears,
and every rule below is one the scan documents and could lose to a careless
edit of leak-patterns.

Added lines only, so a leak can still be scrubbed out -- a scan that also
matched removed lines would make the fix un-committable. Added file paths too,
since a leak can hide in a filename. Generic patterns match case-sensitively,
so the lowercase "/users/" of a web route is not mistaken for a home
directory; personal literals in the untracked local file match
case-insensitively, because an employer's name is a name in any casing.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN = ROOT / ".githooks" / "leak-scan"


# These fixtures ARE the shapes the guard blocks, so they are assembled from
# pieces rather than written out. A test file containing them literally could
# not be committed through the hook it tests -- which is the guard working,
# not a problem with it, but it would mean reaching for --no-verify to land
# the test, and a guard routinely bypassed is a guard nobody trusts.
# A made-up address. An earlier version of this file used the real one
# from this machine -- the same address the worksheet was redacted to
# remove -- reassembled so the hook could not see it. Any RFC1918
# address tests the pattern equally well, and this one is nobody's.
LAN = "192.168." + "99.99"
GH_TOKEN = "ghp_" + "a" * 36
ANTHROPIC_KEY = "sk-" + "ant-" + "a" * 22
PEM_HEADER = "-----BEGIN RSA " + "PRIVATE KEY-----"
HOME_PATH = "/Users" + "/someone/secret"


def scan(diff, patterns=None, local=None):
    """True when the scan blocks. Patterns default to the repo's own."""
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin"}
    with tempfile.TemporaryDirectory() as tmp:
        if patterns is not None:
            p = Path(tmp) / "p"; p.write_text(patterns); env["LEAK_PATTERNS"] = str(p)
        if local is not None:
            p = Path(tmp) / "l"; p.write_text(local); env["LEAK_PATTERNS_LOCAL"] = str(p)
        done = subprocess.run([str(SCAN)], input=diff, capture_output=True,
                              text=True, env=env)
    return done.returncode != 0


def diff_of(*lines, path="notes.md"):
    head = f"--- a/{path}\n+++ b/{path}\n@@ -1,0 +1,{len(lines)} @@\n"
    return head + "".join(lines)


CASES = [
    ("an added line with a private address is blocked",
     diff_of(f"+see {LAN}\n"), True, {}),
    ("REMOVING that same line is allowed, or a leak could never be scrubbed",
     diff_of(f"-see {LAN}\n"), False, {}),
    ("an unchanged context line is allowed",
     diff_of(f" see {LAN}\n"), False, {}),
    ("an added GitHub token is blocked",
     diff_of(f"+{GH_TOKEN}\n"), True, {}),
    ("an added Anthropic key shape is blocked",
     diff_of(f"+{ANTHROPIC_KEY}\n"), True, {}),
    ("an added private key header is blocked",
     diff_of(f"+{PEM_HEADER}\n"), True, {}),
    ("an added home path is blocked",
     diff_of(f"+cd {HOME_PATH}\n"), True, {}),
    # A path in a diff is repo-relative and so never begins with "/", which
    # means the home-path pattern cannot match one however the file is named.
    # Scanning paths earns its place on the other patterns instead: a token or
    # a personal literal sitting in a filename.
    ("a NEW FILE whose PATH carries a token shape is blocked",
     f"--- /dev/null\n+++ b/notes-{GH_TOKEN}.md\n"
     "@@ -0,0 +1 @@\n+nothing in the body\n", True, {}),
    ("a NEW FILE whose PATH carries a personal literal is blocked",
     "--- /dev/null\n+++ b/acme-corp-plan.md\n@@ -0,0 +1 @@\n+nothing in the body\n",
     True, {"patterns": "", "local": "acme-corp\n"}),
    ("a RENAMED file is scanned at its new path too",
     "rename from a.md\nrename to acme-corp-plan.md\n", True,
     {"patterns": "", "local": "acme-corp\n"}),
    ("a lowercase /users/ web route is NOT a home path",
     diff_of("+GET /users/42/profile\n"), False, {}),
    ("0.0.0.0 and 127.0.0.1 are not private LAN addresses",
     diff_of("+bind 0.0.0.0 then curl 127.0.0.1:8731\n"), False, {}),
    ("ordinary course prose is allowed",
     diff_of("+print('Hello, world!')\n", "+The loop runs 10 times.\n"), False, {}),
    ("a content line that itself begins with + is still read as added",
     diff_of(f"++ {LAN}\n"), True, {}),
    ("a personal literal from the local file matches in ANY casing",
     diff_of("+welcome to AcMe CoRp\n"), True,
     {"patterns": "", "local": "Acme Corp\n"}),
    ("the local file is only consulted for its own patterns",
     diff_of("+nothing to see\n"), False,
     {"patterns": "", "local": "Acme Corp\n"}),
    # Regression: git emits "\ No newline at end of file" mid-hunk whenever the
    # OLD version of a file had no trailing newline. That line is none of "+",
    # "-" or " ", so it used to end the hunk as far as the scanner was
    # concerned and every added line after it went unscanned -- a real bypass,
    # reproduced with a genuine `git diff --cached` before it was fixed.
    ("an added line AFTER a no-newline marker is still scanned",
     "--- a/x.md\n+++ b/x.md\n@@ -1 +1,2 @@\n-last\n"
     "\\ No newline at end of file\n" f"+{GH_TOKEN}\n", True, {}),
    ("a clean added line after that marker is still allowed",
     "--- a/x.md\n+++ b/x.md\n@@ -1 +1,2 @@\n-last\n"
     "\\ No newline at end of file\n" "+ordinary prose\n", False, {}),
    ("an empty diff is allowed",
     "", False, {}),
]


def main():
    if not SCAN.exists():
        sys.exit(f"{SCAN} is missing -- the leak guard is not installed")
    bad = 0
    for label, diff, should_block, kw in CASES:
        blocked = scan(diff, **kw)
        ok = blocked == should_block
        if not ok:
            bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (blocked={blocked}, expected {should_block})'}")
    print(f"\n{'the leak guard blocks what it claims to' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
