# Plan A: Local Readiness Implementation Plan

> **Execution: Native, chosen by Justin on 2026-10-05.** REQUIRED SUB-SKILL: superpowers:executing-plans. Implement every task in the main session, then one fresh reviewer on the most capable model checks the whole branch. Do not switch to subagent-driven: Tasks 1, 2 and 14 stop for Justin's input, which a subagent cannot get. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the repository ready to go public, entirely locally: answer keys out of the tree, every leak and answer-key guard able to scan whole histories, browser tests that work under the GitHub Pages subpath and against a live URL, licenses, and a CI workflow written and linted but not yet run.

**Architecture:** Small stdlib Python scripts and tests in the style already here (`scripts/`, `tests/`), one shared Node module for the two browser tests, and one GitHub Actions workflow whose risky logic lives in a testable script rather than inline YAML. Nothing here touches GitHub or rewrites history; Plans B and C do that.

**Tech Stack:** Python 3.9+ stdlib, POSIX sh, Node 25, Pyodide 314.0.7, playwright-core 1.63.0, gitleaks 8.30.1, actionlint 1.7.12, GitHub Actions.

**Spec:** `docs/specs/public-release.md` (approved 2026-10-05). Read it before starting: it records the decisions this plan implements and the facts behind them.

## Global Constraints

- **Python floor is 3.9.** Every script and test must run under `/usr/bin/python3` (3.9.6, the Command Line Tools' Python). No `match`, no `X | Y` annotations, no parenthesized context managers. `build.py` and `scripts/` are stdlib only.
- **No personal string** in any tracked file, commit message, or CI log. The personal list lives only in `.githooks/leak-patterns.local` (gitignored) and, in Plan C, an Actions secret.
- **No tracked file may contain a leak shape or the answer-key header as written.** Assemble token fixtures from pieces (`"ghp_" + "a" * 36`), and never put the answer-key header on a line of its own; write it inside an escaped string. The hooks and the guard from Task 4 will otherwise refuse the commit, which is them working.
- **Every new guard is shown failing once, on purpose,** and its commit message says how.
- Actions pinned by full commit SHA; workflow-level `permissions: contents: read`; no `pull_request_target`.
- Deploy only the artifact the gates tested, never a rebuild.
- **Plan A changes nothing on GitHub and rewrites no history. Nothing is pushed.**
- **The answer keys are backed up and verified before they are untracked, and never deleted.** They are the only copy of the answers.
- **User-facing text that names the course waits on Open Question 8.** Plan A writes none.
- American spellings (`grey` excepted). In docs and new files, avoid em dashes or close them up; the book's prose keeps its spaced ones.
- Work on `main`, as this repository always has.
- Every commit message ends with:
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: <session URL>
  ```

## Review Focus

The five failure modes the spec implies but its own success criteria do not exercise, most likely first. Each is pinned by a test in the task named.

1. **A runner's toolchain is not this Mac's.** Git there may still name a new branch `master`, and `pre_push_test.py` already fails when it does. Pinned in **Task 5** by forcing `init.defaultBranch=master` locally. Ubuntu also has mawk and GNU grep/sed where `leak-scan` has only run under macOS's tools; the first CI run in Plan C is that verdict, since `leak_scan_test.py` runs in the `leaks` job.
2. **A skipped browser test is a green run that tested nothing.** Pinned in **Task 9**: `REQUIRE_BROWSER=1` turns every skip into a failure, demonstrated with a missing browser binary.
3. **A history scan that cannot see the history reports it clean,** in a shallow clone or a repository with no commits. Pinned in **Tasks 4 and 7**: both history scanners refuse, and tests prove it.
4. **Something added and then deleted between two looks,** the net-diff class that already let a token through pre-push. Pinned for answer keys in **Task 4** (`--history`) and for leaks in **Task 7**.
5. **An empty or comments-only personal list passes silently,** since matching nothing looks exactly like a clean history. Pinned in **Task 12**.

## File Map

| File | Change | Responsibility |
| --- | --- | --- |
| `.gitignore` | modify | ignore the answer keys; stop ignoring the npm lockfile |
| `tests/answer_key_guard.py` | create | refuse a tracked answer key, in the tree or anywhere in history |
| `tests/answer_key_guard_test.py` | create | prove the guard catches keys and nothing else |
| `tests/pre_push_test.py` | modify | name the branch explicitly instead of trusting git's default |
| `.githooks/leak-scan` | modify | redacted mode; attribution line |
| `tests/leak_scan_test.py` | modify | redacted-mode cases |
| `scripts/scan_history.py` | create | leak-scan every commit; refuse a history it cannot see |
| `tests/scan_history_test.py` | create | prove it scans commits, not the final tree |
| `tests/package.json` | modify | pin playwright-core exactly |
| `tests/package-lock.json` | create (tracked) | reproducible `npm ci` |
| `scripts/serve.py` | modify | optional directory argument |
| `tests/browser_harness.mjs` | create | site location (root, subpath, live) and browser launch, shared |
| `tests/browser_test.mjs` | modify | subpath and live modes; status, origin, path and content-type checks |
| `tests/browser_check_test.mjs` | create | the Check button across the JS-to-Python boundary, in a real page |
| `LICENSE`, `LICENSE-COURSE` | create | Apache-2.0; CC BY-NC-SA 4.0 |
| `README.md` | modify | answer keys, leak guard, licenses, Python 3.9 wording |
| `scripts/personal_sweep.sh` | create | CI's personal-strings sweep, testable locally |
| `tests/personal_sweep_test.py` | create | prove it fails safe |
| `.github/workflows/ci.yml` | create | gates, build, deploy, live check |
| `tests/workflow_test.py` | create | pins, permissions, no `pull_request_target` |
| `docs/specs/public-release.md` | modify | correct one statement about playwright-core |

---

### Task 1: Install the two local tools

Ask first: the spec lists new tools under "Ask first". Nothing in this task touches the repository.

**Files:** none.

**Interfaces:**
- Produces: `actionlint` and `gitleaks` on PATH, for Tasks 13 and 14.

- [ ] **Step 1: Ask Justin to approve installing two Homebrew formulae**

Say exactly what and why: `actionlint` (lints the workflow before it ever runs on GitHub) and `gitleaks` (the same scanner CI will run, so its findings are known before Plan B). Wait for a yes.

- [ ] **Step 2: Install and check the versions**

```bash
brew install actionlint gitleaks
actionlint -version
gitleaks version
```

Expected: actionlint `1.7.12`; gitleaks `8.30.x`. CI pins gitleaks `8.30.1`; if Homebrew's is newer, note it in Task 14's commit message rather than changing the pin.

---

### Task 2: The personal list, and a noreply identity for new commits

Needs Justin. Ask at the start. If he has not answered yet, carry on with Task 3 and come back; only Tasks 14 and 15 depend on this one.

**Files:**
- Create: `.githooks/leak-patterns.local` (gitignored; **never** tracked)
- Modify: repository-local git config

**Interfaces:**
- Produces: `.githooks/leak-patterns.local`, read by `leak-scan` by default and by `scan_history.py` through it.

- [ ] **Step 1: Ask Justin for his list**

Explain the format: one extended regular expression per line, matched case-insensitively against added lines and added paths. Remind him of the candidates discussed in conversation, and that **his name must not be on it**: it is intentionally public in `LICENSE`, the README and the commit author field, and listing it would block those files. Do not copy his answer into any file other than the one in Step 2, or into any commit message.

- [ ] **Step 2: Write the file and confirm git ignores it**

Write his lines into `.githooks/leak-patterns.local`. Then:

```bash
git check-ignore -v .githooks/leak-patterns.local
git status --short .githooks/
```

Expected: `check-ignore` names the `.gitignore` rule; `git status` prints nothing.

- [ ] **Step 3: Check nothing in the current tree already matches**

```bash
git grep -n -i -I -E -f .githooks/leak-patterns.local -- . ':!.githooks/leak-patterns.local' || echo "no matches in the tree"
```

Expected: `no matches in the tree`. If something matches, show Justin file and line in this conversation only, and decide with him: remove the content, or narrow the pattern.

- [ ] **Step 4: Show the hook refuses one of his strings**

Take his first pattern's literal form and feed the scanner a synthetic diff containing it, with only the personal list active. Type it at the terminal; do not save it anywhere.

```bash
printf -- '--- a/x\n+++ b/x\n@@ -0,0 +1 @@\n+LITERAL-FROM-HIS-FIRST-LINE\n' \
  | LEAK_PATTERNS=/dev/null .githooks/leak-scan; echo "exit=$?"
```

Expected: `exit=1`. (`LEAK_PATTERNS=/dev/null` turns the generic patterns off: `/dev/null` is not a regular file, so `leak-scan` skips it.)

- [ ] **Step 5: Use the noreply address for every commit from now on**

```bash
git config user.email 71140104+mmmugh@users.noreply.github.com
git config user.email
```

Expected: the noreply address. This is repository-local; Plan B rewrites the older commits.

There is nothing to commit: both changes are untracked by design.

---

### Task 3: Back up the answer keys, then untrack them

The twelve keys are the only copy of the quiz answers: their source, `drafts.json`, no longer exists. The backup comes first, and is verified, before git stops tracking anything. Untracking keeps the files on disk.

**Files:**
- Create: `~/python_foundations-notes/answer-keys-backup/` (outside the repository)
- Modify: `.gitignore`
- Untrack: `volumes/vol1-foundations/answer-keys/*-answers.txt` (12 files)

**Interfaces:**
- Produces: a working tree whose `HEAD` no longer tracks any key. Plan B's rewrite relies on this, so that the rewritten tree equals this one.

- [ ] **Step 1: Copy the keys out, with a checksum manifest**

```bash
B="$HOME/python_foundations-notes/answer-keys-backup"
mkdir -p "$B"
cp -p volumes/vol1-foundations/answer-keys/*-answers.txt "$B/"
(cd volumes/vol1-foundations/answer-keys && shasum -a 256 *-answers.txt) > "$B/SHA256SUMS"
```

- [ ] **Step 2: Verify the backup before going further**

```bash
(cd "$B" && shasum -a 256 -c SHA256SUMS)
ls "$B"/*-answers.txt | wc -l
```

Expected: twelve lines ending `OK`, then `12`. **Stop here if either is wrong.** A second copy also exists in the private GitHub repo's history, under the old root `answer-keys/` path, but do not rely on it.

- [ ] **Step 3: Stop tracking them and ignore them**

```bash
git rm -r --cached -q volumes/vol1-foundations/answer-keys
cat >> .gitignore <<'EOF'

# Quiz answer keys: generated by scripts/make_quizzes.py and private. These
# files are the only copy of the answers (docs/specs/public-release.md).
# tests/answer_key_guard.py fails if one is ever committed.
volumes/*/answer-keys/
answer-keys/
EOF
```

- [ ] **Step 4: Check the files survived and the build does not need them**

```bash
ls volumes/vol1-foundations/answer-keys/*-answers.txt | wc -l
git check-ignore -q volumes/vol1-foundations/answer-keys/ch01-your-first-programs-answers.txt && echo ignored
git status --short | head -15
python3 build.py --check | tail -1
/usr/bin/python3 build.py --check | tail -1
```

Expected: `12`; `ignored`; twelve `D ` lines plus ` M .gitignore`; both builds end `110 checked, 0 mismatched`. The build never reads the keys; it only guards against them reaching `site/`.

- [ ] **Step 5: Commit**

```bash
git add .gitignore
git commit -F - <<'EOF'
chore: stop tracking the quiz answer keys

The spec makes the keys private: decision 2 of docs/specs/public-release.md.
They are generated by scripts/make_quizzes.py from drafts.json, which no
longer exists anywhere, so these twelve files are the only copy of the
answers. They were copied to ~/python_foundations-notes/answer-keys-backup
with a SHA256SUMS manifest, and the manifest verified, before git stopped
tracking anything. The files stay on disk.

They leave the history in Plan B. Untracking them here first means the
rewritten tree can be compared to this one byte for byte.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 4: The answer-key guard

**Files:**
- Create: `tests/answer_key_guard.py`, `tests/answer_key_guard_test.py`
- Modify: `README.md` (the "The answer keys" section)

**Interfaces:**
- Produces: `python3 tests/answer_key_guard.py [--history]`. Exit 0 when clean, 1 with findings, and a nonzero refusal when it cannot see the history (shallow clone, no commits). Run from anywhere inside a repository. Used by Task 13's workflow.

- [ ] **Step 1: Write the test first**

Create `tests/answer_key_guard_test.py`:

```python
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
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/answer_key_guard_test.py`
Expected: every case FAILs or errors, because `tests/answer_key_guard.py` does not exist yet.

- [ ] **Step 3: Write the guard**

Create `tests/answer_key_guard.py`:

```python
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
```

- [ ] **Step 4: Run the test, under both Pythons**

```bash
python3 tests/answer_key_guard_test.py
/usr/bin/python3 tests/answer_key_guard_test.py
```

Expected: every line `ok`, then `the answer-key guard catches keys and nothing else`, exit 0, both times.

- [ ] **Step 5: Show it failing on purpose**

Break the content rule and confirm the renamed-key case notices:

```bash
cp tests/answer_key_guard.py /tmp/answer_key_guard.bak
sed -i '' 's/return any(line.strip() == MARKER/return False and any(line.strip() == MARKER/' tests/answer_key_guard.py
python3 tests/answer_key_guard_test.py | grep -E "FAIL|wrong"
cp /tmp/answer_key_guard.bak tests/answer_key_guard.py
python3 tests/answer_key_guard_test.py | tail -1
```

Expected: exactly one failure, `FAIL  a renamed key is caught by its header`, then the restored run passes. The `--history` case still passes while broken, because history detection uses `git grep` and the path rule, not this function. That is worth knowing: the two modes do not share a single point of failure.

- [ ] **Step 6: Run it against this repository**

```bash
python3 tests/answer_key_guard.py; echo "tree exit=$?"
python3 tests/answer_key_guard.py --history | tail -3; echo "history exit=$?"
```

Expected: `no answer key in the tree`, `tree exit=0`. The history run **fails, and that is expected**: it lists both `answer-keys/` and `volumes/vol1-foundations/answer-keys/` paths. Plan B removes them. Record the finding count for the commit message.

- [ ] **Step 7: Document it in the README**

Append a paragraph to the end of the "The answer keys" section, after the sentence ending `fails the build if one is found.`:

```bash
python3 - <<'EOF'
from pathlib import Path
p = Path("README.md"); s = p.read_text()
anchor = "for the answer-key marker and fails the build if one is found."
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + """

The keys are not in this repository either. They are private and kept outside
version control, and `.gitignore` excludes `volumes/*/answer-keys/`. An ignore
rule does not stop `git add -f`, so `tests/answer_key_guard.py` fails if one is
ever committed, recognizing a key by its path or by the header
`make_quizzes.py` writes into every one; `--history` checks every commit rather
than only the tree.""", 1)
p.write_text(s)
EOF
```

- [ ] **Step 8: Commit**

```bash
git add tests/answer_key_guard.py tests/answer_key_guard_test.py README.md
git commit -F - <<'EOF'
test: refuse a committed answer key, in the tree or anywhere in history

.gitignore stops an accidental add but not `git add -f`. The guard recognizes
a key by path (an answer-keys directory, a *-answers.txt name) and by the
header make_quizzes.py writes into every key, so renaming one does not hide
it; a script that merely mentions the header is not flagged.

--history checks every commit on every ref, because a key added then deleted
is gone from the tree and still in what a public repository publishes. That
is the net-diff mistake the pre-push hook once made with tokens. It refuses a
shallow clone and an empty history rather than reporting either clean.

Shown failing on purpose: with the header check disabled, the renamed-key and
history cases both fail.

Against this repository the tree is clean and the history is not, by design:
both historical answer-keys paths are found. Plan B removes them.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 5: Git tests that do not lean on the developer's git

`pre_push_test.py` calls `git init` without naming the branch, then checks out `main`. That only works where git defaults to `main`, as this Mac's does. Measured with the default forced to `master`, it fails: `error: pathspec 'main' did not match any file(s) known to git`. A CI runner may well be such a machine.

**Files:**
- Modify: `tests/pre_push_test.py:53-54`

**Interfaces:**
- Produces: nothing new. Tasks 4, 7 and 12 already name the branch in their own tests.

- [ ] **Step 1: Reproduce the failure**

```bash
GIT_CONFIG_PARAMETERS="'init.defaultBranch=master'" python3 tests/pre_push_test.py 2>&1 | tail -3
```

Expected: fails with `pathspec 'main' did not match`.

- [ ] **Step 2: Name the branch**

In `tests/pre_push_test.py`, change lines 53 and 54 from:

```python
        subprocess.run(["git", "init", "-q", "--bare", str(remote)], check=True)
        subprocess.run(["git", "init", "-q", str(work)], check=True)
```

to:

```python
        # Name the branch rather than trusting git's default, which is still
        # "master" on some machines; this test checks out "main" below.
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remote)], check=True)
        subprocess.run(["git", "init", "-q", "-b", "main", str(work)], check=True)
```

- [ ] **Step 3: Verify under a master-default git, a normal one, and Python 3.9**

```bash
GIT_CONFIG_PARAMETERS="'init.defaultBranch=master'" python3 tests/pre_push_test.py | tail -1
python3 tests/pre_push_test.py | tail -1
/usr/bin/python3 tests/pre_push_test.py | tail -1
```

Expected: all three end `pre-push scans what reaches the remote`.

- [ ] **Step 4: Commit**

```bash
git add tests/pre_push_test.py
git commit -F - <<'EOF'
test: pre_push_test names its branch instead of trusting git's default

It ran git init without -b and then checked out "main", which only works where
git already defaults to main, as this Mac's does. With the default forced to
master it failed with "pathspec 'main' did not match". A CI runner can be
exactly that machine. Reproduced with GIT_CONFIG_PARAMETERS before the fix,
passes after under both defaults and under Python 3.9.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 6: A redacted mode for leak-scan

A public repository's CI logs are public. When `LEAK_SCAN_REDACT` is set, a match reports a count and nothing else: not the line, and not the path, because a filename can itself be the match.

**Files:**
- Modify: `.githooks/leak-scan:85-90`
- Modify: `tests/leak_scan_test.py`

**Interfaces:**
- Produces: `leak-scan` honors `LEAK_SCAN_REDACT` (any non-empty value). When set, it prints one line to stderr on a match, `leak-scan: BLOCKED — N added line(s) match a deny pattern (redacted)`, and exits 1. Exit codes are unchanged. Used by Task 7.

- [ ] **Step 1: Write the failing cases**

In `tests/leak_scan_test.py`, replace the existing `scan()` function with these two, which keep `scan()`'s behavior for the existing cases:

```python
def scan_output(diff, redact=False, patterns=None, local=None):
    """(exit code, everything printed). Patterns default to the repo's own."""
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin"}
    if redact:
        env["LEAK_SCAN_REDACT"] = "1"
    with tempfile.TemporaryDirectory() as tmp:
        if patterns is not None:
            p = Path(tmp) / "p"; p.write_text(patterns); env["LEAK_PATTERNS"] = str(p)
        if local is not None:
            p = Path(tmp) / "l"; p.write_text(local); env["LEAK_PATTERNS_LOCAL"] = str(p)
        done = subprocess.run([str(SCAN)], input=diff, capture_output=True,
                              text=True, env=env)
    return done.returncode, done.stdout + done.stderr


def scan(diff, patterns=None, local=None):
    """True when the scan blocks."""
    return scan_output(diff, False, patterns, local)[0] != 0
```

Add this list directly above `def main():`

```python
# Redacted mode, for CI, where the log of a public repository is public. A
# match must say there is one and print nothing that matched: not the line,
# and not a path, since a filename can itself be the leak. The last case is
# the other half: without the variable, a human at a terminal still sees what
# matched, so redaction is a mode and not the new default.
REDACT_CASES = [
    # label, diff, pattern kwargs, should block, must not appear, must appear
    ("redacted: a token is blocked and never printed",
     diff_of(f"+export TOKEN={GH_TOKEN}\n"), {}, True, [GH_TOKEN], "redacted"),
    ("redacted: a personal literal in content is never printed",
     diff_of("+we work at acme-corp now\n"),
     {"patterns": "", "local": "acme-corp\n"}, True, ["acme-corp"], "redacted"),
    ("redacted: a personal literal in a PATH is never printed either",
     "--- /dev/null\n+++ b/acme-corp-plan.md\n@@ -0,0 +1 @@\n+nothing in the body\n",
     {"patterns": "", "local": "acme-corp\n"}, True, ["acme-corp"], "redacted"),
    ("redacted: a clean diff passes and prints nothing",
     diff_of("+ordinary prose\n"), {}, False, [], ""),
]
```

In `main()`, before the final `print(...)` summary line, add:

```python
    for label, diff, kw, should_block, hidden, shown in REDACT_CASES:
        code, out = scan_output(diff, True, **kw)
        leaked = [h for h in hidden if h.lower() in out.lower()]
        ok = ((code != 0) == should_block and not leaked and shown in out
              and (should_block or out.strip() == ""))
        if not ok:
            bad += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (exit={code}, leaked={leaked}, output={out.strip()!r})'}")

    code, out = scan_output(diff_of(f"+export TOKEN={GH_TOKEN}\n"), False)
    ok = code != 0 and GH_TOKEN in out
    if not ok:
        bad += 1
    print(f"  {'ok  ' if ok else 'FAIL'}  unredacted: a person at a terminal still sees what matched")
```

- [ ] **Step 2: Run it and watch the new cases fail**

Run: `python3 tests/leak_scan_test.py | grep -E "redacted|unredacted|wrong"`
Expected: the three blocking `redacted:` cases FAIL (the scanner prints the matched text); the clean case and the `unredacted:` case pass.

- [ ] **Step 3: Implement it**

In `.githooks/leak-scan`, replace the final block:

```sh
if [ -n "$matched" ]; then
  echo "leak-scan: BLOCKED — added content matches a deny pattern:" >&2
  printf '%s\n' "$matched" | sed 's/^/    /' >&2
  echo "  Patterns: $PATTERNS (+ $PATTERNS_LOCAL if present)" >&2
  exit 1
fi
exit 0
```

with:

```sh
if [ -n "$matched" ]; then
  if [ -n "${LEAK_SCAN_REDACT:-}" ]; then
    # Redacted, for CI: a public repository's CI logs are public. Print that
    # something matched and how much, and nothing else -- not the line, and
    # not the path, since a filename can itself be the leak. Look at it
    # locally, without this variable set.
    n=$(printf '%s\n' "$matched" | wc -l | tr -d ' ')
    echo "leak-scan: BLOCKED — $n added line(s) match a deny pattern (redacted)" >&2
    exit 1
  fi
  echo "leak-scan: BLOCKED — added content matches a deny pattern:" >&2
  printf '%s\n' "$matched" | sed 's/^/    /' >&2
  echo "  Patterns: $PATTERNS (+ $PATTERNS_LOCAL if present)" >&2
  exit 1
fi
exit 0
```

Also add to the header, after `# pre-commit and pre-push hooks.` (line 4):

```sh
# LEAK_SCAN_REDACT=1 prints a count instead of the match (see the end).
```

- [ ] **Step 4: Run every scanner case, under both Pythons**

```bash
python3 tests/leak_scan_test.py | tail -1
/usr/bin/python3 tests/leak_scan_test.py | tail -1
python3 tests/pre_push_test.py | tail -1
```

Expected: `the leak guard blocks what it claims to` twice, then `pre-push scans what reaches the remote`.

- [ ] **Step 5: Commit**

```bash
git add .githooks/leak-scan tests/leak_scan_test.py
git commit -F - <<'EOF'
feat: leak-scan can redact, for CI logs that are public

With LEAK_SCAN_REDACT set, a match prints a count and nothing that matched:
not the line, and not the path, because a filename can itself be the leak.
The spec first proposed reporting file:line in CI; a path is exactly what a
personal literal in a filename would expose, so not even that.

Tested both ways: redacted output never contains the token, the personal
literal in content, or the one in a path, and a clean diff prints nothing.
Without the variable a person at a terminal still sees the match, so
redaction is a mode, not the new default. The three blocking cases failed
before the change and pass after.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 7: scan_history.py

`git diff <empty tree> HEAD | leak-scan` looks like a history scan and only scans the final tree. That mistake was made once already, during this repository's first audit. This script scans every commit's own diff, and refuses when it cannot see the history.

**Files:**
- Create: `scripts/scan_history.py`, `tests/scan_history_test.py`
- Modify: `README.md` (the "The leak guard" section)

**Interfaces:**
- Consumes: `.githooks/leak-scan` and its `LEAK_SCAN_REDACT` (Task 6); `LEAK_PATTERNS` / `LEAK_PATTERNS_LOCAL` pass through the environment.
- Produces: `python3 scripts/scan_history.py [--redact] [--repo PATH]`. Exit 0 when no commit is blocked, 1 when any is, and a nonzero refusal for a shallow clone or no commits. Each blocked commit prints as `  <7-char sha>  <scanner message>`; the summary reads `N commits scanned, none blocked` or `N commits scanned, M blocked`. Used by Tasks 12 and 13.

- [ ] **Step 1: Write the test first**

Create `tests/scan_history_test.py`:

```python
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
        expect("a personal list from the environment is used", code, 1)
        expect("...and its match is never printed when redacted",
               LITERAL in out.lower(), False)

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
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/scan_history_test.py`
Expected: failures throughout, because the script does not exist yet.

- [ ] **Step 3: Write the script**

Create `scripts/scan_history.py`:

```python
"""Run leak-scan over every commit in a repository's history.

    python3 scripts/scan_history.py [--redact] [--repo PATH]

Exists because scanning history is easy to get wrong in a way that looks
right. `git diff <empty tree> HEAD | leak-scan` reads like a history scan and
only scans the final tree, so a leak added and deleted in between is invisible
to it. That mistake was made once already, in this repository's first audit.
This scans each commit's own diff, which is what a public repository actually
publishes.

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
        scan = subprocess.run([str(SCAN)], input=diff.stdout, capture_output=True, env=env)
        if scan.returncode:
            blocked += 1
            print(f"  {commit[:7]}  {scan.stderr.decode(errors='replace').strip()}")

    print(f"\n{len(commits)} commits scanned, "
          f"{'none blocked' if not blocked else str(blocked) + ' blocked'}")
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the test, under both Pythons**

```bash
python3 tests/scan_history_test.py | tail -1
/usr/bin/python3 tests/scan_history_test.py | tail -1
```

Expected: `every commit is scanned, and nothing it cannot see is called clean`, twice.

- [ ] **Step 5: Show it failing on purpose**

Make the script scan only the final tree, the very mistake it exists to prevent:

```bash
cp scripts/scan_history.py /tmp/scan_history.bak
python3 - <<'EOF'
from pathlib import Path
p = Path("scripts/scan_history.py"); s = p.read_text()
s = s.replace('commits = git(args.repo, "rev-list", "--all").split()',
              'commits = git(args.repo, "rev-list", "-1", "HEAD").split()')
p.write_text(s)
EOF
python3 tests/scan_history_test.py | grep -E "FAIL|wrong"
cp /tmp/scan_history.bak scripts/scan_history.py
python3 tests/scan_history_test.py | tail -1
```

Expected: `FAIL  a leak deleted in a later commit is still found` (and its follow-ons), then the restored run passes.

- [ ] **Step 6: Run it against this repository**

```bash
python3 scripts/scan_history.py --redact; echo "exit=$?"
```

Expected: **exit 1, and that is expected.** Two commits are blocked, the two whose worksheet line carried the LAN address. Plan B rewrites them. Record the count for the commit message. If Task 2 is done, the personal list is active here too; note any extra blocked commits for Plan B, without printing what matched.

- [ ] **Step 7: Mention it in the README**

In the "The leak guard" section, after the paragraph that introduces `tests/pre_push_test.py`, add:

```bash
python3 - <<'EOF'
from pathlib import Path
p = Path("README.md"); s = p.read_text()
anchor = "push carrying a token in its history sailed through."
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + """

`python3 scripts/scan_history.py` runs the scanner over every commit in the
history, which is what a public repository publishes, rather than over the
final tree. It refuses a shallow clone or an empty history instead of calling
either clean. CI runs it with `--redact`, which prints a commit and a count and
never what matched.""", 1)
p.write_text(s)
EOF
```

- [ ] **Step 8: Commit**

```bash
git add scripts/scan_history.py tests/scan_history_test.py README.md
git commit -F - <<'EOF'
feat: scan_history.py, leak-scan over every commit rather than the tree

`git diff <empty tree> HEAD | leak-scan` reads like a history scan and only
sees the final tree; it was used that way once already, in this repository's
first audit, and reported a history clean that was not. This scans each
commit's own diff with --root and -m, refuses a shallow clone or an empty
history, and passes --redact through to the scanner for CI.

Shown failing on purpose: scanning only HEAD, the leak-then-delete case is
reported clean and the test fails.

Against this repository it blocks two commits today, the two that carried the
LAN address in the worksheet. Expected; Plan B rewrites them.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 8: Pin playwright-core and track the lockfile

`tests/package.json` lists `playwright-core` only as an optional dependency with the range `^1.0.0`, and `tests/package-lock.json` is gitignored. Nothing records what CI would install. 1.63.0 is what is installed and has been run here.

**Files:**
- Modify: `tests/package.json`, `.gitignore`
- Create (tracked): `tests/package-lock.json`
- Modify: `docs/specs/public-release.md` (correct one statement)

**Interfaces:**
- Produces: `npm ci` in `tests/` reproduces the harness exactly; `npm ci --omit=optional` installs it without the browser library. Used by Tasks 9, 10 and 13.

- [ ] **Step 1: Pin it**

In `tests/package.json`, change `"playwright-core": "^1.0.0"` to `"playwright-core": "1.63.0"`. Leave it under `optionalDependencies`: a contributor who never runs the browser test should not need it.

- [ ] **Step 2: Stop ignoring the lockfile and generate it**

```bash
python3 - <<'EOF'
from pathlib import Path
p = Path(".gitignore"); lines = p.read_text().splitlines(keepends=True)
assert sum(l.strip() == "tests/package-lock.json" for l in lines) == 1
p.write_text("".join(l for l in lines if l.strip() != "tests/package-lock.json"))
EOF
(cd tests && npm install --no-audit --no-fund)
git status --short tests/package-lock.json
```

Expected: `?? tests/package-lock.json`.

- [ ] **Step 3: Prove a clean install reproduces it**

```bash
rm -rf tests/node_modules
(cd tests && npm ci --no-audit --no-fund)
python3 -c "import json;print(json.load(open('tests/node_modules/playwright-core/package.json'))['version'])"
(cd tests && node verify2.mjs | tail -1 && node browser_test.mjs | tail -1)
```

Expected: `1.63.0`; `verify2` completes; `browser_test` ends `the page works from a real browser, and talks to nobody else`.

- [ ] **Step 4: Correct the spec**

The spec says `playwright-core` is "declared nowhere in the repo". It is declared, just loosely.

```bash
python3 - <<'EOF'
import re
from pathlib import Path
p = Path("docs/specs/public-release.md"); s = p.read_text()
s, n = re.subn(
    r"- `browser_test\.mjs` needs `playwright-core`, which is declared nowhere in the\s+"
    r"repo; the copy it ran against lived in a session scratchpad and is gone\.",
    "- `browser_test.mjs` needs `playwright-core`, which `tests/package.json` listed\n"
    "  only as an optional dependency with the range `^1.0.0`, and with the lockfile\n"
    "  untracked nothing recorded what would be installed. (Corrected in Plan A: an\n"
    "  earlier draft said it was declared nowhere.)", s)
assert n == 1
for old, new in [
    ("| `playwright-core` | pin at plan time | to be declared as a devDependency |",
     "| `playwright-core` | 1.63.0 | pinned exactly; an optional dependency |"),
    ("tests/package.json               + playwright-core (devDependency)",
     "tests/package.json               playwright-core pinned to 1.63.0"),
]:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
p.write_text(s)
EOF
```

- [ ] **Step 5: Commit**

```bash
git add tests/package.json tests/package-lock.json .gitignore docs/specs/public-release.md
git commit -F - <<'EOF'
build: pin playwright-core and track the test harness lockfile

playwright-core was an optional dependency at ^1.0.0 with the lockfile
gitignored, so nothing recorded what CI would install. Pinned to 1.63.0, the
version installed and run here, and the lockfile is now tracked so `npm ci`
reproduces the harness. A clean `npm ci` was run and verify2 and browser_test
both pass against it.

Corrects the spec, which said the package was declared nowhere. It was
declared, only loosely.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 9: The browser tests' subpath and live modes

GitHub Pages serves a project site under `/<repo>/`. A page that only works at the root (an absolute `/pyodide/` anywhere) passes every local test and breaks on launch day. Only the real host shows the content types it sends. So the browser test gains two modes, and the two browser tests share their setup through one small module.

**Files:**
- Modify: `scripts/serve.py`
- Create: `tests/browser_harness.mjs`
- Modify: `tests/browser_test.mjs` (full replacement below)

**Interfaces:**
- Consumes: `npm ci` from Task 8.
- Produces: `python3 scripts/serve.py [port] [directory]`. From `tests/browser_harness.mjs`: `loadChromium()` returns playwright's `chromium` or exits; `startSite(port)` returns `{ baseUrl, stop }`, with `baseUrl` always ending in `/`; `launch(chromium, stop)` returns a browser or exits; `skip(reason, hint)` exits 0, or 1 when `REQUIRE_BROWSER` is set. Environment: `BASE=/name/` serves `site/` one level down; `SITE_URL=https://…` tests a deployed site and spawns nothing; `REQUIRE_BROWSER=1` makes every skip a failure. Used by Tasks 10 and 13.

- [ ] **Step 1: Record the baseline**

Run: `(cd tests && node browser_test.mjs)`
Expected: all `ok`. This is the behavior that must survive the rewrite.

- [ ] **Step 2: Let serve.py serve any directory**

In `scripts/serve.py`, change the usage line in the docstring from `    python3 scripts/serve.py [port]` to `    python3 scripts/serve.py [port] [directory]`, and after the line `PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8731` add:

```python
# An optional second argument serves a different directory. The browser test
# uses it to put site/ one level down, the way GitHub Pages serves a project
# site under /<repo>/, so that a path that only works at the root is caught.
if len(sys.argv) > 2:
    SITE = Path(sys.argv[2]).resolve()
```

Change the existence check's message so it reads correctly for any directory:

```python
if not SITE.exists():
    sys.exit(f"{SITE} does not exist yet; build first: python3 build.py --check")
```

- [ ] **Step 3: Write the shared harness**

Create `tests/browser_harness.mjs`:

```js
/* Shared by the browser tests: where the site is, and a browser to open it in.
 *
 * Three ways to point a test at the site:
 *
 *     node browser_test.mjs                                  site/ at the root
 *     BASE=/python-foundations/ node browser_test.mjs        site/ one level down
 *     SITE_URL=https://example.github.io/repo/ node ...      a deployed site
 *
 * BASE exists because GitHub Pages serves a project site under /<repo>/, and
 * a page that only works at the root -- an absolute "/pyodide/..." anywhere --
 * passes every local test and breaks on the day it goes live. SITE_URL exists
 * because only the real host shows the content types it actually sends.
 *
 * REQUIRE_BROWSER=1 makes every skip a failure. A skipped browser test exits
 * 0, and in CI that is a green run that tested nothing.
 */

import { spawn } from "node:child_process";
import { mkdtempSync, rmSync, symlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");

/** Exit as skipped -- or as failed, when REQUIRE_BROWSER is set. */
export function skip(reason, hint) {
  if (process.env.REQUIRE_BROWSER) {
    console.log(`FAIL  ${reason} (REQUIRE_BROWSER is set, so this cannot be skipped)`);
    process.exit(1);
  }
  console.log(`skipped: ${reason}`);
  if (hint) console.log(`  ${hint}`);
  process.exit(0);
}

/** playwright's chromium, or exit: skipped when not installed, failed when broken. */
export async function loadChromium() {
  try {
    return (await import("playwright-core")).chromium;
  } catch (e) {
    // Only "it is not installed" is a skip. A corrupted install or a broken
    // import is a failure: swallowing it would turn a real breakage into a
    // green run that says "skipped".
    if (e.code !== "ERR_MODULE_NOT_FOUND") {
      console.log(`FAIL  playwright-core is installed but will not load: ${e.message}`);
      process.exit(1);
    }
    skip("playwright-core is not installed.", "npm ci && npx playwright-core install chromium");
  }
}

/** Start the site (or locate a deployed one). Returns { baseUrl, stop }. */
export async function startSite(port) {
  if (process.env.SITE_URL) {
    const url = process.env.SITE_URL;
    return { baseUrl: url.endsWith("/") ? url : url + "/", stop: () => {} };
  }
  const base = process.env.BASE || "/";
  if (!/^\/([A-Za-z0-9._-]+\/)?$/.test(base)) {
    console.log(`FAIL  BASE must look like /name/ -- got ${JSON.stringify(base)}`);
    process.exit(1);
  }
  let dir = join(ROOT, "site");
  let scratch = null;
  if (base !== "/") {
    // site/ one level down, by symlink rather than copying 14 MB.
    scratch = mkdtempSync(join(tmpdir(), "pf-base-"));
    symlinkSync(join(ROOT, "site"), join(scratch, base.slice(1, -1)));
    dir = scratch;
  }
  const server = spawn("python3", [join(ROOT, "scripts", "serve.py"), String(port), dir],
                       { stdio: "ignore" });
  const stop = () => {
    try { server.kill(); } catch {}
    if (scratch) rmSync(scratch, { recursive: true, force: true });
  };
  process.on("exit", stop);

  // Wait for the server to actually answer rather than guessing at a delay.
  // A fixed sleep here was a race: anything that slows start-up turns into
  // "the page never got there", which reads as a broken site.
  for (let i = 0; ; i++) {
    try { await fetch(`http://localhost:${port}/`); break; }
    catch {
      if (i > 100) { stop(); console.log("  FAIL  the server never came up"); process.exit(1); }
      await new Promise(r => setTimeout(r, 200));
    }
  }
  return { baseUrl: `http://localhost:${port}${base}`, stop };
}

/** A launched browser, or exit: skipped when the binary is missing, failed otherwise. */
export async function launch(chromium, stop) {
  try {
    return await chromium.launch();
  } catch (e) {
    stop();
    // A missing executable is a skip; any other launch failure is a failure.
    // A sandbox problem or a bad launch argument must not read as "no browser
    // installed".
    if (!/Executable doesn't exist|please run.*install/i.test(e.message)) {
      console.log(`FAIL  the browser is installed but would not start: ${e.message.split("\n")[0]}`);
      process.exit(1);
    }
    skip("no browser binary installed.", "npx playwright-core install chromium");
  }
}
```

- [ ] **Step 4: Rewrite browser_test.mjs on the harness**

Replace `tests/browser_test.mjs` entirely with:

```js
/* The only test that starts where a student starts: a real browser, a real
 * page, a real click.
 *
 * Everything else here drives box_runner.py under Pyodide in node, which skips
 * the entire interface -- the module graph, the served content types, and
 * whether Python is fetched from this site or from someone else's CDN. Those
 * are the parts that break when the build is reorganized, and node cannot see
 * any of them.
 *
 * It runs against site/ at the root, one level down (BASE, the way GitHub
 * Pages serves a project site), or a deployed site (SITE_URL); see
 * browser_harness.mjs. Optional locally, because a headless browser is
 * ~140 MB and the rest of this project needs nothing:
 *
 *     npm ci && npx playwright-core install chromium
 *     node browser_test.mjs
 */

import { launch, loadChromium, skip, startSite } from "./browser_harness.mjs";

const PORT = 8741;

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const origin = new URL(baseUrl).origin;
const basePath = new URL(baseUrl).pathname;

// Read the first chapter out of the site under test rather than naming one,
// so this keeps working when a volume is added, renamed or reordered.
let boxes;
try {
  boxes = await (await fetch(`${baseUrl}boxes.json`)).json();
} catch (e) {
  stop();
  console.log(`FAIL  could not read ${baseUrl}boxes.json: ${e.message}`);
  process.exit(1);
}
const first = boxes.find(b => /\/ch\d\d-/.test(b.id));
if (!first) { stop(); skip("no chapter pages in the site -- build first."); }
const PAGE = `${first.volume}/${first.slug}.html`;

const browser = await launch(chromium, stop);
const page = await browser.newPage();

const external = [], escaped = [], failed = [], errored = [], errors = [], fetched = [];
const types = {};
page.on("request", r => {
  const u = new URL(r.url());
  if (u.origin !== origin) external.push(r.url());
  else if (!u.pathname.startsWith(basePath)) escaped.push(u.pathname);
  if (u.pathname.includes("/pyodide/")) fetched.push(u.pathname);
});
page.on("response", r => {
  const u = new URL(r.url());
  if (r.status() >= 400) errored.push(`${r.status()} ${u.pathname}`);
  const name = u.pathname.split("/").pop();
  if (name === "pyodide.mjs" || name.endsWith(".wasm")) types[name] = r.headers()["content-type"] || "";
});
page.on("requestfailed", r => failed.push(`${r.url()} :: ${r.failure()?.errorText}`));
page.on("pageerror", e => errors.push(String(e)));

const problems = [];
const check = (ok, what) => { console.log(`  ${ok ? "ok  " : "FAIL"}  ${what}`);
                              if (!ok) problems.push(what); };

try {
  await page.goto(`${baseUrl}${PAGE}`, { waitUntil: "load" });

  // Pyodide boots on the first Run, not on load: a reader who only reads must
  // not be made to download 13 MB.
  check(fetched.length === 0, "nothing from pyodide/ is fetched before a click");

  const started = Date.now();
  await page.locator("button.run").first().click();
  await page.waitForFunction(
    () => document.querySelector(".runtime .msg")?.textContent?.includes("ready"),
    null, { timeout: 180000 });
  console.log(`        (booted in ${((Date.now() - started) / 1000).toFixed(1)}s)`);

  await page.waitForFunction(
    () => { const r = document.querySelector('.box[data-box="0"] pre.result');
            return r && !r.hidden && r.textContent.trim().length; },
    null, { timeout: 60000 });
  const printed = (await page.locator('.box[data-box="0"] pre.result').textContent()).trim();
  check(printed === "Hello, world!", `Run prints "Hello, world!" (got ${JSON.stringify(printed)})`);

  // Edit then re-run: proves the box runs what the student typed, not the page's copy.
  await page.locator('.box[data-box="0"] textarea').fill('print(6 * 7)\nprint("edited")');
  await page.locator("button.run").first().click();
  await page.waitForFunction(
    () => document.querySelector('.box[data-box="0"] pre.result')?.textContent.includes("42"),
    null, { timeout: 60000 });
  const edited = (await page.locator('.box[data-box="0"] pre.result').textContent()).trim();
  check(edited === "42\nedited", `an edited box runs the edit (got ${JSON.stringify(edited)})`);

  check(fetched.length === 5, `all 5 runtime files come from this site (${fetched.length})`);
  check(external.length === 0,
        `no request leaves this origin${external.length ? ": " + external.join(", ") : ""}`);
  check(escaped.length === 0,
        `every request stays under ${basePath}${escaped.length ? ": " + escaped.join(", ") : ""}`);
  check(errored.length === 0,
        `no response is an error${errored.length ? ": " + errored.join(", ") : ""}`);
  const mjs = types["pyodide.mjs"] || "";
  const wasm = Object.entries(types).find(([name]) => name.endsWith(".wasm"))?.[1] || "";
  check(/javascript/.test(mjs), `pyodide.mjs is served as JavaScript (${mjs || "not seen"})`);
  check(wasm.startsWith("application/wasm"),
        `the runtime .wasm is served as application/wasm (${wasm || "not seen"})`);
  check(failed.length === 0, `no failed request${failed.length ? ": " + failed.join(", ") : ""}`);
  check(errors.length === 0, `no page error${errors.length ? ": " + errors.join(", ") : ""}`);
} catch (e) {
  check(false, `the page never got there: ${e.message.split("\n")[0]}`);
} finally {
  await browser.close();
  stop();
}

console.log(problems.length
  ? `\n${problems.length} problem(s) in the browser`
  : "\nthe page works from a real browser, and talks to nobody else");
process.exit(problems.length ? 1 : 0);
```

- [ ] **Step 5: Run all three modes**

```bash
cd tests
node browser_test.mjs | tail -6
BASE=/python-foundations/ node browser_test.mjs | tail -6
(python3 ../scripts/serve.py 8733 >/dev/null 2>&1 &) ; sleep 1
SITE_URL=http://localhost:8733/ node browser_test.mjs | tail -3
pkill -f "serve.py 8733"
cd ..
```

Expected: every line `ok` in all three, including `every request stays under /python-foundations/`, `no response is an error`, and both content-type checks. In the `SITE_URL` run no server is spawned by the test; it uses the one started on 8733.

- [ ] **Step 6: Show the subpath mode catching what the root cannot**

Make the built page fetch Pyodide from an absolute path. That works at the root and breaks under a subpath:

```bash
sed -i '' 's|new URL("pyodide/", import.meta.url)|new URL("/pyodide/", import.meta.url)|' site/app.js
(cd tests && node browser_test.mjs | tail -1)
(cd tests && BASE=/python-foundations/ node browser_test.mjs | grep -E "FAIL|problem")
python3 build.py >/dev/null && grep -c 'new URL("pyodide/", import.meta.url)' site/app.js
```

Expected: the root run still passes; the `BASE` run FAILs on `every request stays under /python-foundations/` and `no response is an error`. The rebuild restores `site/app.js` (the final `grep` prints `1`).

- [ ] **Step 7: Show REQUIRE_BROWSER turning a skip into a failure**

```bash
(cd tests && PLAYWRIGHT_BROWSERS_PATH=/nonexistent node browser_test.mjs; echo "exit=$?")
(cd tests && REQUIRE_BROWSER=1 PLAYWRIGHT_BROWSERS_PATH=/nonexistent node browser_test.mjs; echo "exit=$?")
```

Expected: first `skipped: no browser binary installed.` and `exit=0`; second `FAIL  no browser binary installed. (REQUIRE_BROWSER is set, …)` and `exit=1`.

- [ ] **Step 8: Commit**

```bash
git add scripts/serve.py tests/browser_harness.mjs tests/browser_test.mjs
git commit -F - <<'EOF'
test: browser test under the Pages subpath and against a live URL

GitHub Pages serves a project site under /<repo>/, so a page that only works
at the root passes every local test and breaks at launch. BASE=/name/ serves
site/ one level down (serve.py now takes an optional directory, and the
harness symlinks site/ into a temp dir) and checks that every request stays
under that path and that no response is an error. SITE_URL points the same
test at a deployed site, since only the real host shows the content types it
sends; pyodide.mjs must arrive as JavaScript and the .wasm as
application/wasm, in every mode.

Shown failing on purpose: with site/app.js fetching Pyodide from an absolute
"/pyodide/", the root run still passes and the BASE run fails on both the
escaped requests and the 404s. That is the case this mode exists for.

REQUIRE_BROWSER=1 turns every skip into a failure, so CI cannot go green
without a browser. Shown with a missing browser binary: exit 0 without it,
exit 1 with it.

Setup shared with the next test moves into browser_harness.mjs.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 10: browser_check_test.mjs

The JSON-boundary fix (`from_json` in `box_runner.py`, used by `web/app.js`) was proven in a real browser by a scratchpad script that was lost with the scratchpad. This puts that proof in the repository, and adds the case it lacked: a wrong answer must still fail.

**Files:**
- Create: `tests/browser_check_test.mjs`

**Interfaces:**
- Consumes: `browser_harness.mjs` from Task 9.
- Produces: `node tests/browser_check_test.mjs`, honoring `BASE`, `SITE_URL` and `REQUIRE_BROWSER`. Used by Task 13.

- [ ] **Step 1: Write the test**

Create `tests/browser_check_test.mjs`:

```js
/* The Check button, end to end, across the JavaScript-to-Python boundary.
 *
 * A check's test cases travel from the page to box_runner.py as JSON. They
 * used to be converted by pyodide.toPy(), which loses two things: JSON's 61.0
 * arrives as a Python int, so an answer correctly printing "61.0" was marked
 * wrong; and JSON's null arrives as a JavaScript null that is not None, so a
 * case expecting None could never match. Both were invisible from CPython and
 * from node. The fix hands the JSON text to Python (from_json in
 * box_runner.py, called from web/app.js). This proves it from a real page,
 * and fails if that fix is reverted.
 *
 * It first lived in a session scratchpad and was lost with it.
 */

import { launch, loadChromium, startSite } from "./browser_harness.mjs";

const PORT = 8742;

const FIND_FOLDER = [
  "def find_folder(folder, name):",
  "    if folder['name'] == name:",
  "        return folder",
  "    for inner in folder['folders']:",
  "        found = find_folder(inner, name)",
  "        if found:",
  "            return found",
  "    return None",
].join("\n");

// Each trial names a practice step by its data-box id. The first two each need
// one half of the fix; the last proves Check is not simply saying yes.
const TRIALS = [
  { box: "vol1-foundations/ch12-recursion-and-problem-solving-practice#6",
    why: "a case expecting None", code: FIND_FOLDER, pass: true },
  { box: "vol1-foundations/ch11-searching-and-sorting-practice#8",
    why: "formatting 61.0, which a JavaScript number turns into 61", pass: true,
    code: [
      "def ranked(results):",
      "    return sorted(results, key=lambda result: result[1])",
      "",
      "def leaderboard_lines(results):",
      "    return [f'{i}. {r[0]} {r[1]}' for i, r in enumerate(ranked(results), 1)]",
    ].join("\n") },
  { box: "vol1-foundations/ch12-recursion-and-problem-solving-practice#6",
    why: "a wrong answer", pass: false,
    code: "def find_folder(folder, name):\n    return folder" },
];

const chromium = await loadChromium();
const { baseUrl, stop } = await startSite(PORT);
const browser = await launch(chromium, stop);
const page = await browser.newPage();

const problems = [];
const check = (ok, what) => { console.log(`  ${ok ? "ok  " : "FAIL"}  ${what}`);
                              if (!ok) problems.push(what); };

try {
  for (const t of TRIALS) {
    await page.goto(`${baseUrl}${t.box.split("#")[0]}.html`, { waitUntil: "load" });
    const box = page.locator(`.box[data-box="${t.box}"]`);
    await box.locator("textarea").fill(t.code);
    await box.locator("button.check").click();
    const result = box.locator(".result").first();
    await page.waitForFunction(
      el => { const s = el.textContent.trim(); return s.length > 0 && !/checking/i.test(s); },
      await result.elementHandle(), { timeout: 240000 });
    const text = (await result.textContent()).trim();
    const passed = /passed all/i.test(text);
    check(passed === t.pass,
          `${t.box.split("/")[1]}: ${t.why} ${t.pass ? "passes" : "is rejected"} (${text.split("\n")[0]})`);
  }
} catch (e) {
  check(false, `the check never finished: ${e.message.split("\n")[0]}`);
} finally {
  await browser.close();
  stop();
}

console.log(problems.length
  ? `\n${problems.length} problem(s) with Check`
  : "\nCheck gets the right answer across the boundary, and still rejects a wrong one");
process.exit(problems.length ? 1 : 0);
```

- [ ] **Step 2: Run it**

Run: `(cd tests && node browser_check_test.mjs)`
Expected: three `ok` lines and the final summary.

- [ ] **Step 3: Show it failing when the fix is reverted**

Put the old conversion back into the built `app.js` (generated output, not the source):

```bash
sed -i '' 's|const cases = data.get("cases");|const cases = pyodide.toPy(spec.cases);|' site/app.js
(cd tests && node browser_check_test.mjs | grep -E "FAIL|problem")
python3 build.py >/dev/null && grep -c 'const cases = data.get("cases");' site/app.js
```

Expected: both `passes` trials FAIL (the `None` case and the `61.0` case); the wrong-answer trial still passes; the rebuild restores `site/app.js` (prints `1`).

- [ ] **Step 4: Run it under the subpath too**

Run: `(cd tests && BASE=/python-foundations/ node browser_check_test.mjs | tail -1)`
Expected: the summary line.

- [ ] **Step 5: Commit**

```bash
git add tests/browser_check_test.mjs
git commit -F - <<'EOF'
test: Check across the JS-to-Python boundary, in a real page

The fix that hands check data to Python as JSON text, because pyodide.toPy()
turns 61.0 into an int and null into something that is not None, was proven
in a real browser by a script that lived in a session scratchpad and was lost
with it. It is here now, against the two practice steps that each need one
half of the fix, plus a wrong answer that must still be rejected, so a Check
that always says yes cannot pass.

Shown failing on purpose: with the old conversion put back into the built
app.js, both right answers are rejected and the wrong one is still rejected.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 11: Licenses, and the README's licensing and Python wording

The licenses match Java Foundations (decision 3). The files are fetched from their publishers and checked against known hashes; the copies in Java Foundations were confirmed byte-identical to those on 2026-10-05.

**Files:**
- Create: `LICENSE`, `LICENSE-COURSE`
- Modify: `README.md`, `.githooks/leak-scan` (one attribution line)

**Interfaces:** none.

- [ ] **Step 1: Fetch both texts and verify them**

```bash
curl -fsSL https://www.apache.org/licenses/LICENSE-2.0.txt -o LICENSE
echo "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30  LICENSE" | shasum -a 256 -c
curl -fsSL https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.txt -o LICENSE-COURSE
echo "e66c269d4819aaab34b49ef5220c4ddab6756f21bb5180761a4eb8561f2b7bbd  LICENSE-COURSE" | shasum -a 256 -c
```

Expected: `LICENSE: OK`, `LICENSE-COURSE: OK`. If either fails, stop: the publisher's text has changed, and Justin decides which version to use.

- [ ] **Step 2: Add the Licenses section and the Python 3.9 wording**

```bash
python3 - <<'EOF'
from pathlib import Path
p = Path("README.md"); s = p.read_text()

old = """Nothing to install—no package manager, no build toolchain, no accounts. A
Python 3 is the only requirement, and `build.py` uses only the standard
library. Verified on 3.9 and 3.14, including `--check`, which runs every
example under whichever interpreter you used."""
new = """Nothing to install—no package manager, no build toolchain, no accounts.
Python 3.9 or newer is the only requirement, and `build.py` uses only the
standard library. On a Mac, the `python3` that comes with the Command Line
Tools, the same install that provides `git`, is 3.9.6, and it works; any
current Python is a better choice. Verified on 3.9 and 3.14, including
`--check`, which runs every example under whichever interpreter you used."""
assert s.count(old) == 1
s = s.replace(old, new)

s = s.rstrip("\n") + """

## Licenses

| What | License |
| --- | --- |
| The course: everything under `volumes/`, meaning the chapters and their example programs, exercises, worked solutions, practice pages and quizzes | [CC BY-NC-SA 4.0](LICENSE-COURSE) |
| Everything else: the build, the page scripts, the tests and the git hooks | [Apache-2.0](LICENSE) |
| Pyodide, fetched into `vendor/pyodide/` and served from `site/pyodide/` | its own license, MPL-2.0 ([`vendor/pyodide/LICENSE`](vendor/pyodide/LICENSE)) |

The git hooks in `.githooks/` were adapted from
[tokenwatt](https://github.com/mmmugh/tokenwatt), by the same author, where they
are MIT-licensed.
"""
p.write_text(s)
EOF
```

- [ ] **Step 3: Credit the hooks' origin in the scanner itself**

In `.githooks/leak-scan`, after the line added in Task 6 (`# LEAK_SCAN_REDACT=1 prints a count instead of the match (see the end).`), add:

```sh
# Adapted from tokenwatt (github.com/mmmugh/tokenwatt, MIT), by the same author.
```

- [ ] **Step 4: Check nothing else moved**

```bash
python3 tests/leak_scan_test.py | tail -1
python3 tests/answer_key_guard.py | tail -1
grep -c "^## Licenses" README.md
```

Expected: `the leak guard blocks what it claims to`; `no answer key in the tree`; `1`.

- [ ] **Step 5: Commit**

```bash
git add LICENSE LICENSE-COURSE README.md .githooks/leak-scan
git commit -F - <<'EOF'
docs: licenses, matching Java Foundations

CC BY-NC-SA 4.0 for the course (everything under volumes/), Apache-2.0 for
everything else, Pyodide under its own MPL-2.0. Both texts were fetched from
apache.org and creativecommons.org and verified by SHA-256; the copies in Java
Foundations are byte-identical to them. The hooks credit their origin in
tokenwatt, MIT, same author.

The README now says Python 3.9 works, because it is the python3 the Command
Line Tools give every Mac that has git, and that a current Python is better,
rather than reading as an endorsement of an interpreter past end of life.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 12: personal_sweep.sh

The secret-handling logic for CI lives in a script, not inline YAML, because it is the part most likely to fail silently and inline YAML cannot be tested before it runs. The rule: never report a clean history it did not check.

**Files:**
- Create: `scripts/personal_sweep.sh`, `tests/personal_sweep_test.py`

**Interfaces:**
- Consumes: `scripts/scan_history.py --redact` from Task 7.
- Produces: `sh scripts/personal_sweep.sh`, run from inside the repository to scan. Environment: `PERSONAL_PATTERNS` (the list, required) and `FORK_PULL_REQUEST` (`true` on a fork's pull request). Exit 0 when clean or legitimately skipped, 1 otherwise. Used by Task 13.

- [ ] **Step 1: Write the test first**

Create `tests/personal_sweep_test.py`:

```python
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

        code, out = sweep(clean, f"{LITERAL}\n")
        expect("a real list over a clean history passes", code, 0)

    with tempfile.TemporaryDirectory() as tmp:
        leaky = repo_with(tmp, f"we work at {LITERAL.title()}\n")
        code, out = sweep(leaky, f"{LITERAL}\n")
        expect("a match fails the sweep", code, 1)
        expect("...and what matched is never printed", LITERAL in out.lower(), False)

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
```

- [ ] **Step 2: Run it and watch it fail**

Run: `python3 tests/personal_sweep_test.py`
Expected: failures, because the script does not exist yet.

- [ ] **Step 3: Write the script**

Create `scripts/personal_sweep.sh`:

```sh
#!/bin/sh
# The personal-strings sweep, as CI runs it. Kept out of the workflow file so
# that the part most likely to fail silently can be tested before it runs:
# tests/personal_sweep_test.py.
#
# Scans every commit with the personal list, redacted: a public repository's
# CI logs are public, so a match reports a commit and a count, never the text
# or a path.
#
# A list that matches nothing looks exactly like a clean history, so an empty
# list, or one with nothing but comments, fails. The exception is a pull
# request from a fork, where GitHub withholds secrets by design: there it says
# so and exits 0, and the same sweep runs again on the merge to main.
#
#   PERSONAL_PATTERNS   the list, one ERE per line (an Actions secret in CI)
#   FORK_PULL_REQUEST   "true" on a pull request from a fork
set -eu

if [ -z "${PERSONAL_PATTERNS:-}" ]; then
  if [ "${FORK_PULL_REQUEST:-}" = "true" ]; then
    echo "::notice::personal sweep SKIPPED: secrets are not available to pull requests from forks; it runs again on the merge to main"
    exit 0
  fi
  echo "::error::PERSONAL_PATTERNS is empty, so the personal sweep would check nothing. Set the LEAK_PATTERNS_LOCAL secret."
  exit 1
fi

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
list=$(mktemp)
trap 'rm -f "$list"' EXIT
printf '%s\n' "$PERSONAL_PATTERNS" > "$list"

if ! sed -e '/^[[:space:]]*#/d' -e '/^[[:space:]]*$/d' "$list" | grep -q .; then
  echo "::error::the personal list holds only comments or blank lines, so it would check nothing"
  exit 1
fi

# LEAK_PATTERNS=/dev/null: the generic patterns run in their own CI step, and
# leak-scan skips a patterns file that is not a regular file.
LEAK_PATTERNS=/dev/null LEAK_PATTERNS_LOCAL="$list" python3 "$here/scan_history.py" --redact
```

Then: `chmod +x scripts/personal_sweep.sh`

- [ ] **Step 4: Run the test, under both Pythons**

```bash
python3 tests/personal_sweep_test.py | tail -1
/usr/bin/python3 tests/personal_sweep_test.py | tail -1
```

Expected: `the personal sweep never calls an unchecked history clean`, twice.

- [ ] **Step 5: Show it failing on purpose**

Remove the comments-only guard and confirm the test notices:

```bash
cp scripts/personal_sweep.sh /tmp/personal_sweep.bak
python3 - <<'EOF'
from pathlib import Path
p = Path("scripts/personal_sweep.sh"); s = p.read_text()
start = s.index("if ! sed -e"); end = s.index("fi\n", start) + 3
p.write_text(s[:start] + s[end:])
EOF
python3 tests/personal_sweep_test.py | grep -E "FAIL|wrong"
cp /tmp/personal_sweep.bak scripts/personal_sweep.sh
python3 tests/personal_sweep_test.py | tail -1
```

Expected: `FAIL  a list of only comments and blanks fails too`, then the restored run passes.

- [ ] **Step 6: Commit**

```bash
git add scripts/personal_sweep.sh tests/personal_sweep_test.py
git commit -F - <<'EOF'
feat: the CI personal-strings sweep, as a script that can be tested

Kept out of the workflow so the part most likely to fail silently can be
tested before it ever runs. It never reports a clean history it did not
check: an empty secret fails, and so does a list of only comments or blank
lines, since either matches nothing and matching nothing looks exactly like
a clean history. A fork's pull request, where GitHub withholds secrets by
design, skips loudly with a notice instead. A real match fails redacted and
never prints what matched.

Shown failing on purpose: without the comments-only guard, that case passes
when it must not, and the test catches it.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 13: The workflow, its guard test, and lint

Written and linted here; it first runs in Plan C, after the history is rewritten. Until then the two history checks it runs would fail on today's history, by design.

**Files:**
- Create: `.github/workflows/ci.yml`, `tests/workflow_test.py`

**Interfaces:**
- Consumes: every script and test above.
- Produces: the CI pipeline Plan C turns on. The deploy job's output `page_url` feeds the `live` job.

- [ ] **Step 1: Write the guard test first**

Create `tests/workflow_test.py`:

```python
"""Check the CI workflow keeps the security promises the spec makes.

    python3 tests/workflow_test.py

There is no YAML parser in the standard library, so this reads the workflow
as text. That is enough for what it checks, each of which shows up on a line
of its own, and it does not claim to be more:

  - every action is pinned to a full commit SHA, because a tag can be moved
    by whoever controls the action's repository and a SHA cannot;
  - the default token is read-only, a top-level permissions block granting
    exactly `contents: read`;
  - no `pull_request_target`, which runs a fork's code with this repository's
    secrets and a write token.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))


def top_level_permissions(lines):
    for i, line in enumerate(lines):
        if re.match(r"permissions:\s*$", line):
            block = []
            for nxt in lines[i + 1:]:
                if nxt.strip() and not nxt.startswith((" ", "\t")):
                    break
                if nxt.strip() and not nxt.strip().startswith("#"):
                    block.append(nxt.strip())
            return block
    return None


def problems_in(path):
    text = path.read_text()
    lines = text.splitlines()
    found = []
    for n, line in enumerate(lines, 1):
        if line.lstrip().startswith("#"):
            continue
        m = re.match(r"\s*(?:-\s*)?uses:\s*(\S+)", line)
        if m and not re.fullmatch(r"[^@\s]+@[0-9a-f]{40}", m.group(1)):
            found.append(f"{path.name}:{n}: not pinned to a commit SHA: {m.group(1)}")
        if "pull_request_target" in line:
            found.append(f"{path.name}:{n}: pull_request_target")
    block = top_level_permissions(lines)
    if block != ["contents: read"]:
        found.append(f"{path.name}: top-level permissions should be exactly "
                     f"'contents: read', found {block}")
    return found


def main():
    if not WORKFLOWS:
        sys.exit("no workflows found to check -- nothing checked is not the same as passing")
    found = [p for w in WORKFLOWS for p in problems_in(w)]
    for problem in found:
        print(f"  FAIL  {problem}")
    print(f"\n{len(WORKFLOWS)} workflow(s): "
          f"{'pinned, read-only by default, no pull_request_target' if not found else str(len(found)) + ' problem(s)'}")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and watch it refuse**

Run: `python3 tests/workflow_test.py`
Expected: exits nonzero with `no workflows found to check`.

- [ ] **Step 3: Write the workflow**

Create `.github/workflows/ci.yml`:

```yaml
# CI for the course: every gate on every push and pull request, then, on main
# only, deploy the exact artifact those gates tested to GitHub Pages and test
# the live site.
#
# Security posture for a public repository (docs/specs/public-release.md):
# actions pinned by full commit SHA, a read-only token by default, write access
# for the deploy job alone, no pull_request_target, and nothing that prints a
# secret or a matched personal string. tests/workflow_test.py checks the first
# three.
name: ci

on:
  push:
  pull_request:
    branches: [main]

permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}

jobs:
  leaks:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          fetch-depth: 0            # a shallow clone would scan one commit and call it clean
          persist-credentials: false
      - uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0
        with:
          python-version: "3.14"
      - name: The scanner blocks what it claims to
        run: python3 tests/leak_scan_test.py
      - name: pre-push scans what reaches the remote
        run: python3 tests/pre_push_test.py
      - name: The history scan and the personal sweep behave
        run: |
          python3 tests/scan_history_test.py
          python3 tests/personal_sweep_test.py
      - name: Every commit, generic patterns (redacted)
        run: python3 scripts/scan_history.py --redact
      - name: gitleaks over the full history (redacted)
        env:
          GITLEAKS_VERSION: 8.30.1
          GITLEAKS_SHA256: 551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb
        run: |
          tarball="gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz"
          curl -fsSLO "https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/${tarball}"
          echo "${GITLEAKS_SHA256}  ${tarball}" | sha256sum -c -
          tar -xzf "${tarball}" gitleaks
          ./gitleaks git --redact --no-banner --log-opts="--all" .
      - name: Every commit, personal patterns (redacted)
        env:
          PERSONAL_PATTERNS: ${{ secrets.LEAK_PATTERNS_LOCAL }}
          FORK_PULL_REQUEST: ${{ github.event.pull_request.head.repo.fork || 'false' }}
        run: sh scripts/personal_sweep.sh
      - name: The answer-key guard itself
        run: python3 tests/answer_key_guard_test.py
      - name: No answer key in the tree
        run: python3 tests/answer_key_guard.py
      - name: No answer key anywhere in history
        run: python3 tests/answer_key_guard.py --history
      - name: The workflow keeps its own promises
        run: python3 tests/workflow_test.py

  build:
    runs-on: ubuntu-24.04
    strategy:
      fail-fast: false
      matrix:
        # 3.9 is the python3 the Command Line Tools give every Mac with git.
        python: ["3.9", "3.14"]
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          persist-credentials: false
      - uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0
        with:
          python-version: ${{ matrix.python }}
      - uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: vendor/pyodide
          key: pyodide-${{ hashFiles('vendor/pyodide/CHECKSUMS') }}
      - name: Fetch Pyodide and verify it against CHECKSUMS
        run: python3 scripts/fetch_pyodide.py --download
      - name: Build, and verify every example
        run: python3 build.py --check
      - name: Practice pages and volumes
        run: |
          python3 tests/practice_test.py
          python3 tests/second_volume_test.py
      - name: Mark the build with its commit
        if: matrix.python == '3.14'
        run: echo "${GITHUB_SHA}" > site/build.txt
      - name: Keep the site for the jobs that test it
        if: matrix.python == '3.14'
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: site
          path: site/
          if-no-files-found: error
      - name: Keep the same bytes for Pages
        if: matrix.python == '3.14'
        uses: actions/upload-pages-artifact@fc324d3547104276b827a68afc52ff2a11cc49c9 # v5.0.0
        with:
          path: site/

  node-gates:
    needs: build
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          persist-credentials: false
      - uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7.0.0
        with:
          node-version: "25"
          cache: npm
          cache-dependency-path: tests/package-lock.json
      - uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          name: site
          path: site
      - name: Install the harness, without the browser library
        working-directory: tests
        run: npm ci --omit=optional --no-audit --no-fund
      - name: Pyodide harnesses
        working-directory: tests
        run: |
          node verify2.mjs
          node validate_shipped.mjs
          node validate_stdin.mjs
          node validate_projects.mjs

  browser:
    needs: build
    runs-on: ubuntu-24.04
    env:
      REQUIRE_BROWSER: "1"          # a skipped browser test must not read as green
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          persist-credentials: false
      - uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7.0.0
        with:
          python-version: "3.14"    # serve.py serves the site
      - uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7.0.0
        with:
          node-version: "25"
          cache: npm
          cache-dependency-path: tests/package-lock.json
      - uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          name: site
          path: site
      - name: Install the harness and Chromium
        working-directory: tests
        run: |
          npm ci --no-audit --no-fund
          npx playwright-core install --with-deps chromium
      - name: The page works at the root
        working-directory: tests
        run: node browser_test.mjs
      - name: The page works under /<repo>/, the way Pages serves it
        working-directory: tests
        env:
          BASE: /${{ github.event.repository.name }}/
        run: node browser_test.mjs
      - name: Check works across the JavaScript-to-Python boundary
        working-directory: tests
        run: node browser_check_test.mjs

  deploy:
    needs: [leaks, build, node-gates, browser]
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-24.04
    permissions:
      contents: read
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    concurrency:
      group: pages
      cancel-in-progress: false
    outputs:
      page_url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/configure-pages@45bfe0192ca1faeb007ade9deae92b16b8254a0d # v6.0.0
      - id: deployment
        uses: actions/deploy-pages@368f82528645a54fb793d4d04e342629a3f51346 # v5.0.1

  live:
    needs: deploy
    runs-on: ubuntu-24.04
    env:
      REQUIRE_BROWSER: "1"
      SITE_URL: ${{ needs.deploy.outputs.page_url }}
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          persist-credentials: false
      - uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7.0.0
        with:
          node-version: "25"
          cache: npm
          cache-dependency-path: tests/package-lock.json
      - name: Install the harness and Chromium
        working-directory: tests
        run: |
          npm ci --no-audit --no-fund
          npx playwright-core install --with-deps chromium
      - name: Wait until the live site is this build
        # Pages sends max-age=600, so for up to ten minutes the previous deploy
        # can still be what a reader gets. Test nothing until it is not.
        run: |
          base="${SITE_URL%/}/"
          for i in $(seq 1 72); do
            if [ "$(curl -fsS "${base}build.txt" 2>/dev/null)" = "${GITHUB_SHA}" ]; then
              echo "live at ${base}"; exit 0
            fi
            sleep 10
          done
          echo "::error::${base} never served build ${GITHUB_SHA}"
          exit 1
      - name: The live page works, under its real host and path
        working-directory: tests
        run: node browser_test.mjs
      - name: Check works on the live site
        working-directory: tests
        run: node browser_check_test.mjs
```

- [ ] **Step 4: Run the guard test and the linter**

```bash
python3 tests/workflow_test.py
/usr/bin/python3 tests/workflow_test.py | tail -1
actionlint .github/workflows/ci.yml && echo "actionlint: clean"
```

Expected: `1 workflow(s): pinned, read-only by default, no pull_request_target` twice; `actionlint: clean`. If actionlint reports anything, fix it in the YAML and re-run; do not silence it.

- [ ] **Step 5: Show the guard test failing on purpose**

```bash
cp .github/workflows/ci.yml /tmp/ci.bak
python3 - <<'EOF'
from pathlib import Path
p = Path(".github/workflows/ci.yml"); s = p.read_text()
p.write_text(s.replace("actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
                       "actions/checkout@v7.0.1", 1))
EOF
python3 tests/workflow_test.py | grep -E "FAIL|problem"
cp /tmp/ci.bak .github/workflows/ci.yml
python3 tests/workflow_test.py | tail -1
```

Expected: `FAIL  ci.yml:<line>: not pinned to a commit SHA: actions/checkout@v7.0.1`, then the restored run passes.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/ci.yml tests/workflow_test.py
git commit -F - <<'EOF'
ci: the workflow, written and linted, not yet run

Jobs: leaks (scanner and push tests, every commit with generic and personal
patterns redacted, gitleaks 8.30.1 pinned by checksum, the answer-key guard
over tree and history), build (3.9 and 3.14: fetch Pyodide against
CHECKSUMS, build --check, practice and volume tests, then the same site/
uploaded twice, for the tests and for Pages), node-gates, browser (root,
under /<repo>/, and the Check round trip, with REQUIRE_BROWSER so a skip
fails), deploy (main only, the tested artifact, never a rebuild) and live
(waits for build.txt to match the commit, then the browser tests against the
real URL).

Every action is pinned by commit SHA, the token is read-only except in
deploy, there is no pull_request_target, and tests/workflow_test.py checks
those three. Shown failing on purpose with one action pinned by tag.
actionlint reports nothing.

It first runs in Plan C. Until the history is rewritten, the two history
checks would fail on today's commits, by design.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 14: gitleaks over the history, locally

CI will run gitleaks on every push. Its findings on today's history belong to Plan B, known in advance rather than discovered on the first public push.

**Files:**
- Possibly create: `.gitleaks.toml`, only if Justin approves allowlist entries

**Interfaces:**
- Produces: a list of findings, real or false positive, for Plan B.

- [ ] **Step 1: Run it the way CI will**

```bash
gitleaks git --redact --no-banner --log-opts="--all" .; echo "exit=$?"
```

Expected: `exit=0` with no leaks found. If so, skip to Step 4.

- [ ] **Step 2: If there are findings, look at them unredacted, locally only**

```bash
gitleaks git --no-banner --log-opts="--all" --report-format json --report-path /tmp/gitleaks.json . || true
python3 -c "import json; [print(f['RuleID'], f['File'], f['Commit'][:7]) for f in json.load(open('/tmp/gitleaks.json'))]"
```

Read `/tmp/gitleaks.json` (outside the repository). Classify each finding with Justin:
- **A real secret:** goes on Plan B's replacement list. If it is a live credential, Justin rotates it first.
- **A false positive:** Justin approves an allowlist entry, and the entry records the reason.

- [ ] **Step 3: If Justin approved allowlist entries, add them and re-run**

Write `.gitleaks.toml` at the repository root in the format documented for the installed gitleaks version (`gitleaks --help` names the config flags; the project's README documents allowlists). Every entry carries a one-line comment saying why it is safe. Re-run Step 1 until it exits 0.

- [ ] **Step 4: Record the result**

If nothing was found, there is nothing to commit; note `gitleaks: 0 findings across N commits` for Task 15. If `.gitleaks.toml` was added:

```bash
git add .gitleaks.toml
git commit -F - <<'EOF'
ci: gitleaks allowlist, each entry with Justin's sign-off and a reason

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
EOF
```

---

### Task 15: Every gate, once, the way CI will run them

**Files:** none.

**Interfaces:**
- Produces: Plan A's verdict, plus the list of history findings Plan B must remove.

- [ ] **Step 1: The build, under both Pythons**

```bash
python3 build.py --check | tail -1
/usr/bin/python3 scripts/fetch_pyodide.py | tail -1
/usr/bin/python3 build.py --check | tail -1
```

Expected: both builds `110 checked, 0 mismatched`; the 3.9 fetch verifies against CHECKSUMS.

- [ ] **Step 2: Every Python test, under both Pythons, with a master-default git**

```bash
for py in python3 /usr/bin/python3; do
  for t in practice_test second_volume_test leak_scan_test pre_push_test \
           answer_key_guard_test scan_history_test personal_sweep_test workflow_test; do
    GIT_CONFIG_PARAMETERS="'init.defaultBranch=master'" $py tests/$t.py >/tmp/t.out 2>&1
    printf "%-16s %-24s exit=%s  %s\n" "$py" "$t" "$?" "$(tail -1 /tmp/t.out)"
  done
done
```

Expected: sixteen lines, all `exit=0`.

- [ ] **Step 3: The Node and browser gates**

```bash
cd tests
npm ci --no-audit --no-fund >/dev/null
for t in verify2 validate_shipped validate_stdin validate_projects; do
  node $t.mjs >/tmp/n.out 2>&1; printf "%-18s exit=%s  %s\n" "$t" "$?" "$(tail -1 /tmp/n.out)"
done
REQUIRE_BROWSER=1 node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 BASE=/python-foundations/ node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 node browser_check_test.mjs | tail -1
cd ..
```

Expected: four `exit=0`; three success summaries.

- [ ] **Step 4: The lint and the scanners**

```bash
actionlint .github/workflows/ci.yml && echo "actionlint: clean"
python3 tests/answer_key_guard.py | tail -1
gitleaks git --redact --no-banner --log-opts="--all" . >/dev/null 2>&1; echo "gitleaks exit=$?"
```

Expected: `actionlint: clean`; `no answer key in the tree`; `gitleaks exit=0` (or Task 14's approved result).

- [ ] **Step 5: The history findings Plan B inherits**

```bash
python3 tests/answer_key_guard.py --history | tail -1
python3 scripts/scan_history.py --redact | tail -1
LEAK_PATTERNS=/dev/null python3 scripts/scan_history.py --redact | tail -1
```

Expected, and **not** failures of Plan A: the answer-key paths under both historical directories; `2 blocked` for the generic patterns (the LAN address); and the personal-list count from Task 2, ideally `none blocked`. Write these three numbers into the handoff for Plan B. They are its acceptance tests: after the rewrite, all three must report clean.

- [ ] **Step 6: Confirm nothing is pushed and nothing is on GitHub**

```bash
git status --short | head -5
git log --oneline origin/main..HEAD | wc -l
git ls-files | grep -c "answer-keys" || true
```

Expected: a clean tree; the unpushed count has grown by Plan A's commits; `0` tracked answer-key paths.

Plan A is done when every step above matches its expected result.
