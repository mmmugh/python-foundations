"""Check the CI workflow keeps the security promises the spec makes.

    python3 tests/workflow_test.py

There is no YAML parser in the standard library, so this reads the workflow
as text, by indentation. That is enough for what it checks, each of which
shows up on lines of its own, and it does not claim to be more:

  - every action is pinned to a full commit SHA, because a tag can be moved
    by whoever controls the action's repository and a SHA cannot;
  - the default token is read-only: a top-level permissions block granting
    exactly `contents: read`;
  - only the deploy job grants itself anything with "write" in it. A job's
    own permissions block overrides the default, so checking the top level
    alone would pass a copy-pasted `contents: write` on any other job. An
    earlier draft of this test did exactly that; the review panel caught it;
  - no `pull_request_target`, which runs a fork's code with this repository's
    secrets and a write token.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))
WRITE_ALLOWED = {"deploy"}


def block_under(lines, i):
    """What lines[i] (a `permissions:` key) grants: its inline value, if any,
    plus every non-comment line nested under it, with trailing comments cut."""
    line = lines[i]
    indent = len(line) - len(line.lstrip())
    grants = []
    inline = re.sub(r"\s+#.*$", "", line.split(":", 1)[1]).strip()
    if inline:
        grants.append(inline)
    for nxt in lines[i + 1:]:
        if nxt.strip() and len(nxt) - len(nxt.lstrip()) <= indent:
            break
        text = re.sub(r"\s+#.*$", "", nxt).strip()
        if text and not text.startswith("#"):
            grants.append(text)
    return grants


def problems_in(path):
    lines = path.read_text().splitlines()
    found = []
    top, job, in_jobs = None, None, False
    for i, line in enumerate(lines):
        n, stripped = i + 1, line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        m = re.match(r"\s*(?:-\s*)?uses:\s*(\S+)", line)
        if m and not re.fullmatch(r"[^@\s]+@[0-9a-f]{40}", m.group(1)):
            found.append(f"{path.name}:{n}: not pinned to a commit SHA: {m.group(1)}")
        if "pull_request_target" in line:
            found.append(f"{path.name}:{n}: pull_request_target")
        if re.match(r"jobs:\s*$", line):
            in_jobs = True
            continue
        if in_jobs:
            m = re.match(r"  ([A-Za-z0-9_-]+):\s*$", line)
            if m:
                job = m.group(1)
        if re.match(r"\s*permissions:", line):
            grants = block_under(lines, i)
            if not line.startswith((" ", "\t")):
                top = grants
            elif job not in WRITE_ALLOWED and any("write" in g for g in grants):
                found.append(f"{path.name}:{n}: job '{job}' grants itself {grants}; "
                             f"only {sorted(WRITE_ALLOWED)} may write")
    if top != ["contents: read"]:
        found.append(f"{path.name}: top-level permissions should be exactly "
                     f"'contents: read', found {top}")
    return found


def main():
    if not WORKFLOWS:
        sys.exit("no workflows found to check -- nothing checked is not the same as passing")
    found = [p for w in WORKFLOWS for p in problems_in(w)]
    for problem in found:
        print(f"  FAIL  {problem}")
    print(f"\n{len(WORKFLOWS)} workflow(s): "
          f"{'pinned, read-only by default, write only in deploy, no pull_request_target' if not found else str(len(found)) + ' problem(s)'}")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
