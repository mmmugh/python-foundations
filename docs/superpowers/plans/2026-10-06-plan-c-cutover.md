# Plan C: Cutover Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native) to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking. **Every task from 6 on touches GitHub and starts by asking Justin; wait for an explicit yes for that task.** A yes for one task does not cover the next.

**Goal:** Take Python Foundations public: a new public repository, `mmmugh/python-foundations`, holding Plan B's rewritten history (answer keys included, per the reversed decision 2), deployed by CI to `https://mmmugh.github.io/python-foundations/`, with the old private repository archived and every success criterion in the spec checked.

**Architecture:** Two phases. Phase 1 (Tasks 1 to 5) is local and reversible: it makes the working repository say what the decisions of 2026-10-06 require (keys public, the disclaimer, session lines refused), then runs Plan B's rewrite again with the answer-key paths kept. Phase 2 (Tasks 6 to 15) is the cutover, one GitHub step at a time, ordered so that each one-way step happens only after the checks that would catch its failure: the email block is proven on a scratch private repository before anything is pushed, the old repository's name is freed and the working copy's `origin` re-pointed before the new repository takes that name, and the push itself happens only after the rewrite is re-verified against the working repository as it is at that moment.

**Tech Stack:** git, `gh` 2.90 (logged in as mmmugh, scopes `repo` and `workflow`, SSH), git-filter-repo 2.47.0, Python 3.9+ stdlib, GitHub Actions, GitHub Pages, the repository's own hooks and tests, Plan B's tools in `~/python_foundations-notes/rewrite/tools/`.

**Spec:** `docs/specs/public-release.md`, decisions 1 to 13 and Success Criteria 1 to 12. Decisions 10 to 13, and the reversal of decision 2, were made on 2026-10-06; read them first. Plan B (`docs/superpowers/plans/2026-10-05-plan-b-history-rewrite.md`) describes the rewrite tools this plan runs again.

## Global Constraints

- **Phase 2 waits for Justin at every task.** Each task from 6 on opens with an "Ask Justin" step that says exactly what will change on GitHub. Nothing on GitHub changes without that yes.
- **Between Task 5 and Task 9, nothing is committed to the working repository.** Task 7 changes its remote configuration only. A commit in that window makes the rewrite stale; `verify_rewrite.py [current]`, run again in Task 9 Step 1, catches it, and the fix is to repeat Task 5.
- **No commit carries a `Claude-Session` line** (decision 13). `Co-Authored-By` only. From Task 3 on, the `commit-msg` hook refuses one.
- **Never push the old history to the new repository.** Only `run/public`'s `main`, to `main`, under a remote that is not called `origin`.
- **Never use `--no-verify`.** Never print the personal Gmail address, the LAN address, or the personal list; where a step needs the old address, it reads it from `git log` into a variable and prints nothing.
- **The global git identity on this Mac is the personal Gmail address.** Every clone that commits needs a repo-local `user.email` of `71140104+mmmugh@users.noreply.github.com` first.
- **The answer keys stay off the site.** `build.py`'s whitelist copy and its published-content guard are kept; only the repository-side guard is retired.
- Python 3.9 floor for every script and test; American spellings (`grey` excepted); closed em dashes in new text.
- **Shell variables do not survive from one tool call to the next.** Begin every command block with
  `RW=$HOME/python_foundations-notes/rewrite; WR=$HOME/python_foundations; M=$RW/run/rewrite.git/filter-repo; PUB=$RW/run/public`.

## Review Focus

The five failure modes most likely to bite, that the spec implies and its criteria do not exercise. Each is pinned in the task named.

1. **The old history reaches the new public repository through the old remote name.** The working copy's `origin` names `mmmugh/python-foundations`, which the new public repository takes. Pinned in **Task 7**: `origin` is re-pointed to the renamed private repository before Task 8 creates the public one, and the step proves `origin` resolves there.
2. **A push that scans nothing.** `run/public` has no personal list, `leak-scan` skips a missing list silently, and re-pointing `origin` instead of using a new remote shrinks pre-push's range to one commit. Pinned in **Task 9**: a new remote name, `LEAK_PATTERNS_LOCAL` exported as an absolute path, and a personal history scan immediately before the push.
3. **A stale rewrite.** A commit in the working repository after Task 5 would be missing from the public history. Pinned in **Task 9 Step 1**: the full verify, `[current]` included, runs again just before the push.
4. **An email block that is not actually on.** Pinned in **Task 6**: proven by a rejected push to a scratch *private* repository, so a block that turns out to be off exposes nothing.
5. **A green CI that never ran a gate**: a skipped browser test, an empty secret, a pull request that deploys. Pinned in **Task 13**: one deliberately broken branch per job, an empty-secret run, and a pull request that must not deploy.

---

## Phase 1: local

### Task 1: The answer keys go public

Decision 2, reversed. The twelve keys are tracked again; the repository-side guard that kept them out is retired; the site-side guard that keeps them off the published pages stays, and is shown working first, since from now on it is the only thing between a key and the site.

**Files:**
- Modify: `.gitignore`, `.github/workflows/ci.yml`, `README.md`
- Track: `volumes/vol1-foundations/answer-keys/*-answers.txt` (12, already on disk)
- Delete: `tests/answer_key_guard.py`, `tests/answer_key_guard_test.py`

**Interfaces:**
- Produces: a `main` that tracks all twelve keys, byte for byte the backup in `~/python_foundations-notes/answer-keys-backup/`. Task 4's verify check relies on that.

- [ ] **Step 1: Show the site guard refusing a key, before anything changes**

```bash
cd "$WR"
python3 build.py > /dev/null && echo "built"
cp volumes/vol1-foundations/answer-keys/ch01-your-first-programs-answers.txt site/vol1-foundations/
python3 build.py > /dev/null; echo "build exit with a key in site/=$?"
rm site/vol1-foundations/ch01-your-first-programs-answers.txt
python3 build.py > /dev/null; echo "build exit after removing it=$?"
```

Expected: `built`; then `build exit with a key in site/=1`, with the message `content that must not be published is reachable: [...ch01-your-first-programs-answers.txt]`; then `build exit after removing it=0`. (A rebuild does not remove a stray file from `site/`, which is why the step deletes it by hand.)

- [ ] **Step 2: Stop ignoring the keys, and track them**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path(".gitignore"); s = p.read_text()
old = """
# Quiz answer keys: generated by scripts/make_quizzes.py and private. These
# files are the only copy of the answers (docs/specs/public-release.md).
# tests/answer_key_guard.py fails if one is ever committed.
volumes/*/answer-keys/
answer-keys/
"""
assert s.count(old) == 1
p.write_text(s.replace(old, "", 1))
PY
git add volumes/vol1-foundations/answer-keys/*-answers.txt
git ls-files volumes/vol1-foundations/answer-keys | wc -l
(cd volumes/vol1-foundations/answer-keys && shasum -a 256 -c "$HOME/python_foundations-notes/answer-keys-backup/SHA256SUMS" | grep -c ': OK$')
```

Expected: `12`, then `12`. The comment left at the top of `.gitignore` ("answer-keys/ is tracked on purpose: it belongs in the repo but never in site/") is true again.

- [ ] **Step 3: Retire the repository-side guard**

```bash
git rm -q tests/answer_key_guard.py tests/answer_key_guard_test.py
python3 - <<'PY'
from pathlib import Path
p = Path(".github/workflows/ci.yml"); s = p.read_text()
old = """      - name: The answer-key guard itself
        run: python3 tests/answer_key_guard_test.py
      - name: No answer key in the tree
        run: python3 tests/answer_key_guard.py
      - name: No answer key anywhere in history
        run: python3 tests/answer_key_guard.py --history
"""
assert s.count(old) == 1
p.write_text(s.replace(old, "", 1))
p = Path("README.md"); s = p.read_text()
old = """The keys are not in this repository either. They are private and kept outside
version control, and `.gitignore` excludes `volumes/*/answer-keys/`. An ignore
rule does not stop `git add -f`, so `tests/answer_key_guard.py` fails if one is
ever committed, recognizing a key by its path or by the header
`make_quizzes.py` writes into every one; `--history` checks every commit rather
than only the tree.
"""
new = """The keys are in this repository, in `volumes/<volume>/answer-keys/`, for anyone
who wants to check a quiz. They are kept off the site only so that the course
pages themselves stay free of answers. (They were private for a while before
the repository went public; `docs/specs/public-release.md`, decision 2, records
the reversal.)
"""
assert s.count(old) == 1
p.write_text(s.replace(old, new, 1))
PY
```

- [ ] **Step 4: Check nothing still depends on it, and the build still guards the site**

```bash
grep -rn 'answer_key_guard' README.md .github tests scripts build.py || echo "no references outside docs/"
python3 tests/workflow_test.py | tail -1
actionlint .github/workflows/ci.yml && echo "actionlint: clean"
python3 build.py --check | tail -1
ls site/vol1-foundations | grep -c -- '-answers' || true
```

Expected: `no references outside docs/`; the workflow test's pass line; `actionlint: clean`; `110 checked, 0 mismatched`; `0` keys in `site/`.

- [ ] **Step 5: Commit**

```bash
git add .gitignore .github/workflows/ci.yml README.md
git commit -q -F - <<'MSG'
chore: the answer keys are public

Decision 2 of docs/specs/public-release.md, reversed by Justin before launch.
The twelve keys are tracked again, byte for byte the checksummed backup Plan A
made, and Plan C's rerun of the history rewrite keeps them in history too.
The repository-side guard that refused them, tests/answer_key_guard.py, its
test and its three CI steps, is retired.

The site-side guard stays: build.py copies quizzes by whitelist and refuses a
build that publishes a key, so the course pages stay free of answers. Shown
working first: with a key copied into site/, the build failed naming it.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
git log --oneline -1
```

---

### Task 2: The disclaimer

Decision 10. The name stays; the course says it is independent where a reader first meets the name, the site's front page, and in the README.

**Files:**
- Create: `tests/disclaimer_test.py`
- Modify: `build.py` (a `DISCLAIMER` constant, and `write_library`), `web/app.css` (one rule), `README.md`

**Interfaces:**
- Produces: `build.DISCLAIMER`, rendered by `write_library` as `<p class="notice">` on `site/index.html`.

- [ ] **Step 1: Write the test first**

Create `tests/disclaimer_test.py`:

```python
"""Check the course says it is independent, where a reader meets its name.

    python3 tests/disclaimer_test.py

Spec decision 10: the name stays "Python Foundations", which other courses and
a book series also use, and "Python" is the Python Software Foundation's
registered mark. So the site's front page and the README each say three
things: the course is independent, it is affiliated with and endorsed by no
one of the same name (the PSF included), and "Python" is the PSF's trademark.
This builds the front page into a temporary directory and reads it back.
"""

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build                                                    # noqa: E402

CLAIMS = ("an independent, free course", "not affiliated with", "Python Software Foundation",
          "registered trademark")


def main():
    results = []

    def expect(label, ok):
        results.append((label, ok))

    with tempfile.TemporaryDirectory() as tmp:
        build.SITE = Path(tmp)
        volume = {"slug": "vol1", "title": "A Volume", "subtitle": "", "blurb": ""}
        build.write_library([(volume, [{"slug": "ch01-one", "title": "One"}], None)])
        front = (Path(tmp) / "index.html").read_text()

    for claim in CLAIMS:
        expect(f"the front page says {claim!r}", claim in front)
    expect("the front page still lists the chapters", "vol1/ch01-one.html" in front)
    readme = (ROOT / "README.md").read_text()
    for claim in CLAIMS:
        expect(f"the README says {claim!r}", claim in readme)

    bad = 0
    for label, ok in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")
    print(f"\n{'the course says it is independent, wherever its name first appears' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Watch it fail**

Run: `python3 tests/disclaimer_test.py | tail -1`
Expected: `8 wrong`: none of the four claims is on the front page or in the README yet. (The phrase "an independent, free course" is used rather than "independent" alone, which the README already contains in another sense, and which would pass for the wrong reason.)

- [ ] **Step 3: Write the notice**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path("build.py"); s = p.read_text()
old = '''def write_library(built):'''
new = '''# The course shares its name with other courses and a book series, and "Python"
# is the Python Software Foundation's registered mark. Said on the front page,
# where a reader first meets the name, and in the README (spec decision 10).
DISCLAIMER = ('Python Foundations is an independent, free course. It is not '
              'affiliated with, or endorsed by, the Python Software Foundation or '
              'any other course, book or program of the same name. "Python" is a '
              'registered trademark of the Python Software Foundation.')


def write_library(built):'''
assert s.count(old) == 1; s = s.replace(old, new, 1)
old = '''        nav.append(f'<a href="{vol["slug"]}/{first}.html">{heading}</a>')
'''
new = '''        nav.append(f'<a href="{vol["slug"]}/{first}.html">{heading}</a>')
    sections.append(f'<p class="notice">{html.escape(DISCLAIMER, quote=False)}</p>')
'''
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
p = Path("web/app.css"); s = p.read_text()
old = "/* ---------------------------------------------------------------- footer */\n"
new = old + "\n.notice { margin-top: 3rem; font-size: 0.85rem; color: var(--soft); }\n"
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
p = Path("README.md"); s = p.read_text()
old = """backend, no build toolchain — it is a static site, and Python runs in the
browser via Pyodide.
"""
new = """backend, no build toolchain — it is a static site, and Python runs in the
browser via Pyodide.

**Read it at <https://mmmugh.github.io/python-foundations/>.** Nothing to
install or sign up for: every example runs in your browser.

> Python Foundations is an independent, free course. It is not affiliated with,
> or endorsed by, the Python Software Foundation or any other course, book or
> program of the same name. "Python" is a registered trademark of the Python
> Software Foundation.
"""
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
PY
```

- [ ] **Step 4: Watch it pass, under both Pythons, and nothing else move**

```bash
python3 tests/disclaimer_test.py | tail -1
/usr/bin/python3 tests/disclaimer_test.py | tail -1
python3 build.py --check | tail -1
python3 tests/second_volume_test.py | tail -1
(cd tests && REQUIRE_BROWSER=1 node browser_test.mjs | tail -1)
```

Expected: `the course says it is independent, wherever its name first appears` twice; `110 checked, 0 mismatched`; the second-volume pass line; the browser test's pass line.

- [ ] **Step 5: Commit**

```bash
git add tests/disclaimer_test.py build.py web/app.css README.md
git commit -q -F - <<'MSG'
docs: say the course is independent, where its name first appears

Decision 10: the name stays "Python Foundations", which other courses and a
book series also use, and "Python" is the Python Software Foundation's
registered mark. The site's front page and the README now say the course is
an independent, free course, affiliated with and endorsed by no one of the
same name, the PSF included, and that "Python" is the PSF's trademark.

tests/disclaimer_test.py builds the front page into a temporary directory
and checks all four claims there and in the README. It failed on all eight
before the change.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
git log --oneline -1
```

---

### Task 3: Session lines refused, locally and in CI

Decision 13. A generic leak pattern for session URLs, which CI's history scan now applies to every commit message, and a `commit-msg` hook that scans each message before the commit exists. Nothing local scanned messages before; the hook applies the personal list too.

**Files:**
- Create: `.githooks/commit-msg` (executable), `tests/commit_msg_test.py`
- Modify: `.githooks/leak-patterns`, `tests/leak_scan_test.py`, `tests/scan_history_test.py`, `.github/workflows/ci.yml`, `README.md`

**Interfaces:**
- Produces: `.githooks/commit-msg MESSAGE_FILE` (exit 0, or 1 having refused); the generic pattern `claude\.ai/code/session_[A-Za-z0-9]{6,}`.

- [ ] **Step 1: Write the failing cases**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path("tests/leak_scan_test.py"); s = p.read_text()
old = 'DASHED_HOME = "-Users" + "-someone-python-foundations"\n'
new = old + '''# A Claude Code session URL. This repository's history was scrubbed of them
# (spec decisions 6, 9 and 13), so one in a file or a message is a regression.
SESSION_URL = "https://claude.ai/code/" + "session_" + "0aB1cD2eF3gH"
'''
assert s.count(old) == 1; s = s.replace(old, new, 1)
old = '''    ("the same path with a placeholder for the name is allowed",
'''
new = '''    ("a Claude Code session URL is blocked",
     diff_of(f"+Claude-Session: {SESSION_URL}\\n"), True, {}),
    ("the placeholder the history was scrubbed to is allowed",
     diff_of("+Claude-Session: <session URL>\\n"), False, {}),
    ("the same path with a placeholder for the name is allowed",
'''
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
p = Path("tests/scan_history_test.py"); s = p.read_text()
old = '''        repo = new_repo(tmp, "plain")
'''
new = '''        repo = new_repo(tmp, "session")
        commit(repo, "a.md", "hello\\n", "docs: x\\n\\nClaude-Session: https://claude.ai/code/"
               + "session_" + "0aB1cD2eF3gH")
        code, out = run(repo, "--redact")
        expect("a session URL in a message is found by the generic patterns", code, 1)

        repo = new_repo(tmp, "plain")
'''
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
PY
```

Create `tests/commit_msg_test.py`:

```python
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
```

- [ ] **Step 2: Watch all three fail**

```bash
python3 tests/leak_scan_test.py | grep -E 'session URL is blocked|wrong'
python3 tests/scan_history_test.py | grep -E 'session URL|wrong'
python3 tests/commit_msg_test.py | tail -1
```

Expected: `FAIL  a Claude Code session URL is blocked` and `1 wrong`; `FAIL  a session URL in a message ...` and `1 wrong`; `4 wrong` (with no hook, the trailer, a token and a personal literal are all committed).

- [ ] **Step 3: The pattern and the hook**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path(".githooks/leak-patterns"); s = p.read_text()
old = "# --- Credential / token shapes (anchored to limit false positives) ---\n"
new = '''# --- A Claude Code session URL. The history was scrubbed of them (spec
# decisions 6, 9 and 13); one in a file or a commit message is a regression.
claude\\.ai/code/session_[A-Za-z0-9]{6,}

''' + old
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
PY
```

Create `.githooks/commit-msg`, then `chmod +x .githooks/commit-msg`:

```sh
#!/bin/sh
# commit-msg: refuse a commit whose message matches a deny pattern, before the
# commit exists. pre-commit and pre-push read diffs only, and a message is
# published with its commit all the same: a Claude-Session URL (spec decision
# 13), a token pasted in, a personal string. CI's scan_history.py reads
# messages too, but on a public repository that is after the fact.
#
# The whole message file goes to leak-scan as the added lines of one synthetic
# file, so the same lists apply, the personal one included. All of it, git's
# comment lines too: with -F or -m, git keeps a '#' line in the message, so
# skipping them would skip text that is published. The one cost: `git commit
# -v` appends the staged diff to this file, so committing the removal of a
# leak with -v is refused too. Commit that one without -v.
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if ! { printf 'diff --git a/.commit b/.commit\n@@ -0,0 +1 @@\n'; sed 's/^/+/' "$1"; } \
     | "$here/leak-scan"; then
  echo "commit-msg: the message was refused and nothing was committed; edit it and commit again" >&2
  exit 1
fi
```

- [ ] **Step 4: Watch them pass: both Pythons, and GNU tools**

```bash
sh -n .githooks/commit-msg && echo "sh ok"
for py in python3 /usr/bin/python3; do
  for t in leak_scan_test scan_history_test commit_msg_test pre_push_test; do
    $py tests/$t.py > /dev/null 2>&1 && echo "ok    $py $t" || echo "FAIL  $py $t"
  done
done
docker run --rm -v "$WR":/repo:ro -w /repo pf-review-gnu sh -c \
  'for t in leak_scan_test scan_history_test commit_msg_test pre_push_test; do python3 tests/$t.py >/dev/null 2>&1 && echo "ok    GNU $t" || echo "FAIL  GNU $t"; done'
```

Expected: `sh ok`, then twelve `ok` lines. (The Docker image is the one Plan A's reviewer built, with GNU grep, sed, mawk and dash; it can only see paths under the home directory, which is why this runs from the working repository. If Justin has removed the image, say so and skip the GNU line rather than calling it passed.)

- [ ] **Step 5: CI and the README**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path(".github/workflows/ci.yml"); s = p.read_text()
old = """      - name: pre-push scans what reaches the remote
        run: python3 tests/pre_push_test.py
"""
new = old + """      - name: Every commit message is scanned before it exists
        run: python3 tests/commit_msg_test.py
"""
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
p = Path("README.md"); s = p.read_text()
old = """remote, where the token is as readable as ever. A commit already made cannot
be fixed by deleting the content in a later one.
"""
new = old + """
`commit-msg` scans each commit message before the commit exists, with the same
lists: a message is published with its commit, and the diff scans never see
it. It is what refuses a `Claude-Session` line, which commits here do not
carry (spec decision 13); CI's history scan refuses one too. One cost: `git
commit -v` puts the staged diff in the message file, so commit the removal of
a leak without `-v`.
"""
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
PY
python3 tests/workflow_test.py | tail -1
actionlint .github/workflows/ci.yml && echo "actionlint: clean"
```

Expected: the workflow test's pass line; `actionlint: clean`.

- [ ] **Step 6: Commit (the new hook checks this very message)**

```bash
git add .githooks/commit-msg .githooks/leak-patterns tests/commit_msg_test.py \
        tests/leak_scan_test.py tests/scan_history_test.py .github/workflows/ci.yml README.md
git commit -q -F - <<'MSG'
feat: refuse a session line, or any leak, in a commit message

Decision 13: commits here carry Co-Authored-By and no Claude-Session line,
and the history was scrubbed of them. Two guards hold that.

A generic leak pattern for session URLs. scan_history.py reads every commit
message, so CI refuses a trailer on any pushed commit.

A commit-msg hook, which scans the message before the commit exists, with the
generic and the personal lists. Nothing local scanned messages before: the
diff scans never see them, though a message is published with its commit.

Shown failing first: a session URL passed the scanner and the history scan,
and with no hook a trailer, a token and a personal literal were all
committed. All pass after, under 3.14, 3.9 and GNU tools.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
git log --oneline -1
git ls-files -s .githooks/commit-msg | cut -c1-6
```

Expected: the commit, and `100755`.

---

### Task 4: The rewrite tools keep the answer keys

Plan B's tools remove both answer-key directories and check that they are gone. Now the keys are public: the rewrite keeps them, and verify checks that all twelve go out, byte for byte the backup. Outside the repository, plus one line in the Plan B document.

**Files:**
- Modify: `$RW/tools/rewrite.sh`, `$RW/tools/verify_rewrite.py`
- Modify: `docs/superpowers/plans/2026-10-05-plan-b-history-rewrite.md` (its amendment note)

**Interfaces:**
- Consumes: `main` tracking the twelve keys (Task 1).
- Produces: `verify_rewrite.py ... [--keys-backup DIR]` (default `~/python_foundations-notes/answer-keys-backup`), still 20 checks: the answer-key-guard check is replaced by "all 12 answer keys are in REF, matching the backup".

- [ ] **Step 1: Change the tools**

```bash
cp "$RW/tools/rewrite.sh" "$RW/tools/rewrite.sh.plan-b"
cp "$RW/tools/verify_rewrite.py" "$RW/tools/verify_rewrite.py.plan-b"
cd "$RW" && python3 - <<'PY'
from pathlib import Path
p = Path("tools/rewrite.sh"); s = p.read_text()
old = '''    --invert-paths \\
    --path answer-keys/ \\
    --path volumes/vol1-foundations/answer-keys/ \\
    --path WORKSHEET-2026-09-21-web-app.md
'''
new = '''    --invert-paths \\
    --path WORKSHEET-2026-09-21-web-app.md
'''
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
p = Path("tools/verify_rewrite.py"); s = p.read_text()
reps = [
("""import argparse
import os
""", """import argparse
import hashlib
import os
"""),
("""    ap.add_argument("--added", type=int, default=0)
""", """    ap.add_argument("--added", type=int, default=0)
    ap.add_argument("--keys-backup",
                    default=str(Path.home() / "python_foundations-notes" / "answer-keys-backup"))
"""),
("""    bad = sorted(p for p in paths
                 if "answer-keys" in p.split("/") or under(p, args.remove))
    check("3", not bad, f"no removed path in any commit ({len(bad)} found)")
    code, last = run([sys.executable, "tests/answer_key_guard.py", "--history"], new)
    check("3", code == 0, f"answer_key_guard.py --history: {last[0]}")
""", """    bad = sorted(p for p in paths if under(p, args.remove))
    check("3", not bad, f"no removed path in any commit ({len(bad)} found)")
    # The answer keys are public (spec decision 2, reversed in Plan C): all of
    # them must be in what goes out, byte for byte the checksummed backup.
    manifest = [l.split(None, 1) for l in
                (Path(args.keys_backup) / "SHA256SUMS").read_text().splitlines() if l.strip()]
    wrong = []
    for digest, name in manifest:
        blob = subprocess.run(["git", "-C", new, "show", f"{args.tree_ref}:"
                               f"volumes/vol1-foundations/answer-keys/{name.strip()}"],
                              capture_output=True).stdout
        if hashlib.sha256(blob).hexdigest() != digest:
            wrong.append(name.strip())
    check("3", bool(manifest) and not wrong,
          f"all {len(manifest)} answer keys are in {args.tree_ref}, matching the backup "
          f"({wrong or 'all match'})")
"""),
]
for old, new in reps:
    assert s.count(old) == 1, old[:50]
    s = s.replace(old, new, 1)
p.write_text(s)
PY
sh -n "$RW/tools/rewrite.sh" && python3 -c "import ast,sys; ast.parse(open(sys.argv[1]).read())" "$RW/tools/verify_rewrite.py" && echo "both parse"
```

- [ ] **Step 2: Watch the new keys check fail on Plan B's run, which removed them**

```bash
python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PUB" --tree-ref main~1 --added 1 \
  --personal "$WR/.githooks/leak-patterns.local" --remove WORKSHEET-2026-09-21-web-app.md \
  --metadata "$M" | grep -E 'answer keys|checks'
```

Expected: `FAIL  [3] all 12 answer keys are in main~1, matching the backup ([...all twelve names...])`. Other checks may fail too, now that the working repository has moved on (`[current]`, `[5]` tree equality): that run is stale by design, and Task 5 replaces it.

- [ ] **Step 3: Note it in Plan B's document, and commit**

```bash
cd "$WR"
python3 - <<'PY'
from pathlib import Path
p = Path("docs/superpowers/plans/2026-10-05-plan-b-history-rewrite.md"); s = p.read_text()
old = "Spec decision 9 records it.\n"
new = ("Spec decision 9 records it. **Run again by Plan C** after decision 2 was reversed: "
       "`rewrite.sh` no longer removes the two answer-key directories, and `verify_rewrite.py` "
       "checks that all twelve keys go out, matching the backup, in place of the answer-key guard "
       "(Plan C, Task 4).\n")
assert s.count(old) == 1; p.write_text(s.replace(old, new, 1))
PY
git add docs/superpowers/plans/2026-10-05-plan-b-history-rewrite.md
git commit -q -F - <<'MSG'
docs: Plan B's rewrite runs again, keeping the answer keys

Decision 2 was reversed, so Plan C runs Plan B's tools again with the two
answer-key directories kept in history, and verify checks that all twelve
keys go out byte for byte the backup, in place of the retired guard. The
tools live outside the repository; Plan C, Task 4 has the exact changes.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
git log --oneline -1
```

---

### Task 5: Run Plan B's rewrite again

The last working-repository commit before the push is the one Task 4 made. From here to Task 9 nothing is committed to it.

**Files:** recreates `$RW/run/`. The working repository is only read.

**Interfaces:**
- Produces: `$PUB` `main` = the rewrite plus the translation commit, verified 20 of 20 and built and tested. Task 9 pushes it.

- [ ] **Step 1: Pre-flight, and replace Plan B's run**

```bash
cd "$WR"
git status --short
python3 "$RW/tools/check_message_edits.py" . "$RW/inputs/message-edits.txt" \
  --remove WORKSHEET-2026-09-21-web-app.md --expect-changed 15 | tail -1
ls "$RW/run"
rm -rf "$HOME/python_foundations-notes/rewrite/run"
```

Expected: no status output; `... 6 dropped by the rewrite, 15 edited besides trailers: the edits do what they say and nothing else` (the commits since Plan B add messages, none of which trips it); `public  rewrite.git`, the directory being replaced.

- [ ] **Step 2: Rewrite, and read filter-repo's report**

```bash
sh "$RW/tools/rewrite.sh" "$WR" "$RW/run" > "$RW/rewrite-output.txt" 2>&1; echo "exit=$?"
tail -3 "$RW/rewrite-output.txt"
cat "$M/suboptimal-issues"
awk 'NR > 1 && $2 ~ /^0+$/' "$M/commit-map" | wc -l
git -C "$RW/run/rewrite.git" for-each-ref --format='%(refname)'
```

Expected: `exit=0`; `Completely finished ...` and the two `rewritten`/`clone` lines; `No filtering problems encountered.`; `6`; `refs/heads/main`, `refs/heads/web-app`, `refs/tags/ws/web-app`.

- [ ] **Step 3: Verify: one failure, the file citations**

```bash
python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PUB" --tree-ref main \
  --personal "$WR/.githooks/leak-patterns.local" --remove WORKSHEET-2026-09-21-web-app.md \
  --metadata "$M" | grep -E 'FAIL|checks'
```

Expected: `FAIL  [6] no tracked file cites a pre-rewrite commit (N citations do)` and `20 checks, 1 failed`. Every other check passes, the new answer-key check included.

- [ ] **Step 4: Translate the citations and commit, in the clone**

```bash
cd "$PUB"
git config user.name "Justin Stewart"
git config user.email 71140104+mmmugh@users.noreply.github.com
git config core.hooksPath .githooks
python3 "$RW/tools/translate_shas.py" "$M/commit-map" $(git ls-files '*.md') | grep -v '^    0 '
git add -A
LEAK_PATTERNS_LOCAL="$WR/.githooks/leak-patterns.local" git commit -q -F - <<'MSG'
docs: point cited commits at the rewritten history

filter-repo rewrote every commit, and with it the hashes cited in commit
messages, but not those cited in files. The spec and the plans cite commits
by hash; each citation now names the same commit in this history, at the same
length, from filter-repo's commit map. Nothing else changed.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
git log --format='%h %ae %s' -1
```

Expected: a `translated` line for the spec and each plan, Plan C's own document included; the commit, under the noreply address. The commit-msg hook in the clone checks the message on the way.

- [ ] **Step 5: Verify: all twenty**

```bash
python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PUB" --tree-ref main~1 --added 1 \
  --personal "$WR/.githooks/leak-patterns.local" --remove WORKSHEET-2026-09-21-web-app.md \
  --metadata "$M"; echo "exit=$?"
```

Expected: `20 checks, all pass: the rewrite meets criteria 2 to 6`, `exit=0`.

- [ ] **Step 6: Build and test the clone the way a stranger would**

```bash
cd "$PUB"
cp "$WR"/vendor/pyodide/pyodide* "$WR"/vendor/pyodide/python_stdlib.zip vendor/pyodide/
python3 scripts/fetch_pyodide.py | tail -1
python3 build.py --check | tail -1
/usr/bin/python3 build.py --check | tail -1
for py in python3 /usr/bin/python3; do
  for t in practice_test second_volume_test leak_scan_test pre_push_test scan_history_test \
           personal_sweep_test workflow_test disclaimer_test commit_msg_test; do
    $py tests/$t.py > "$RW/t.out" 2>&1; printf "%-16s %-22s exit=%s\n" "$py" "$t" "$?"
  done
done
cd tests && npm ci --no-audit --no-fund > /dev/null
for t in verify2 validate_shipped validate_stdin validate_projects; do
  node $t.mjs > "$RW/n.out" 2>&1; printf "%-18s exit=%s\n" "$t" "$?"
done
REQUIRE_BROWSER=1 node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 BASE=/python-foundations/ node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 node browser_check_test.mjs | tail -1
cd .. && git status --short
```

Expected: `5 files match CHECKSUMS`; `110 checked, 0 mismatched` twice; eighteen `exit=0`; four `exit=0`; three pass lines; no status output.

---

## Phase 2: GitHub, one step at a time

### Task 6: Prove the email block, on a scratch private repository

Criterion 10, first half. GitHub can refuse a push carrying the address it keeps private, but only if two account settings are on, and they can only be set in the web UI. Proven here on a *private* scratch repository, so that if the block turns out to be off, the test commit exposes nothing.

**Files:** none tracked. A scratch directory `$RW/email-block-check`.

- [ ] **Step 1: Ask Justin**

Ask him to turn on, at <https://github.com/settings/emails>: **Keep my email addresses private**, and **Block command line pushes that expose my email**. Then ask to approve: creating a private scratch repository `mmmugh/pf-email-block-check`, one test push to it of a commit authored with the old address, and deleting the repository afterwards. Wait for a yes.

- [ ] **Step 2: The scratch repository and the test commit**

```bash
gh repo create mmmugh/pf-email-block-check --private --description "Scratch: proves the email push block. Delete after use."
git init -q -b main "$RW/email-block-check"
cd "$RW/email-block-check"
old=$(git -C "$WR" log --all --format=%ae | grep -v -x -F 71140104+mmmugh@users.noreply.github.com | sort -u)
test "$(printf '%s\n' "$old" | grep -c .)" = 1 && echo "one old address found (not printed)"
echo "scratch" > README.md
git add README.md
git -c user.name="Justin Stewart" -c user.email="$old" commit -q -m "scratch: email block check"
```

Expected: the repository is created; `one old address found (not printed)`. (The working repository still has the old history at this point; Task 11 swaps it.)

- [ ] **Step 3: The push must be refused**

```bash
cd "$RW/email-block-check"
git push -q git@github.com:mmmugh/pf-email-block-check.git main > "$RW/email-block.out" 2>&1; echo "exit=$?"
grep -c 'GH007' "$RW/email-block.out"
```

Expected: a nonzero exit, and at least one `GH007` line (GitHub's "your push would publish a private email address"). Do not print the output file. **If the push succeeds, stop:** the block is off. The commit sits in a private repository only; tell Justin, delete the repository, and do not continue until a repeat of this step is refused.

- [ ] **Step 4: Delete the scratch repository**

`gh` needs the `delete_repo` scope, which it lacks. Ask Justin to run `! gh auth refresh -h github.com -s delete_repo` (it opens a browser), or to delete the repository in the web UI. Then:

```bash
gh repo delete mmmugh/pf-email-block-check --yes
gh repo view mmmugh/pf-email-block-check > /dev/null 2>&1 || echo "gone"
rm -rf "$HOME/python_foundations-notes/rewrite/email-block-check"
```

Expected: `gone`.

---

### Task 7: Bundle the original history, rename and archive the old repository

Decision 11. The new public repository needs the name `python-foundations`, so the old one is renamed and archived, as the private backup. The working copy's `origin` is re-pointed before the name is reused (Review Focus 1). The archived repository lacks the commits never pushed to it, so a bundle of the full original history goes into the notes directory first.

**Files:** creates `~/python_foundations-notes/original-history.bundle`. Changes the working repository's remote configuration, nothing tracked.

- [ ] **Step 1: The bundle (local)**

```bash
cd "$WR"
git bundle create "$HOME/python_foundations-notes/original-history.bundle" --all
git bundle verify "$HOME/python_foundations-notes/original-history.bundle" 2>&1 | tail -1
git bundle list-heads "$HOME/python_foundations-notes/original-history.bundle" | awk '{print $2}'
git rev-list --all --count
```

Expected: `... is okay`; the heads `refs/heads/main`, `refs/heads/web-app`, `refs/remotes/origin/main`, `refs/tags/ws/web-app`; the original commit count.

- [ ] **Step 2: Ask Justin**

Rename `mmmugh/python-foundations` to `python-foundations-private`, point the working copy's `origin` at it, and archive it (read-only, still private). Wait for a yes.

- [ ] **Step 3: Rename, and re-point `origin` straight away**

```bash
cd "$WR"
gh repo rename python-foundations-private --repo mmmugh/python-foundations --yes
git remote set-url origin git@github.com:mmmugh/python-foundations-private.git
git remote -v
git ls-remote origin refs/heads/main
```

Expected: the rename succeeds; `origin` shows the `-private` URL for fetch and push; `ls-remote` prints the old remote `main` (the commit the old repository last received), proving `origin` resolves to the renamed repository.

- [ ] **Step 4: Archive it**

```bash
gh repo archive mmmugh/python-foundations-private --yes
gh repo view mmmugh/python-foundations-private --json name,visibility,isArchived
```

Expected: `{"isArchived":true,"name":"python-foundations-private","visibility":"PRIVATE"}`.

---

### Task 8: Create the public repository and its settings

**Files:** none.

- [ ] **Step 1: Ask Justin**

Create `mmmugh/python-foundations`, public and empty; turn on secret scanning and push protection; set the Actions secret `LEAK_PATTERNS_LOCAL` from the personal list; set Pages to deploy from GitHub Actions. Nothing is pushed yet. Wait for a yes.

- [ ] **Step 2: Create it**

```bash
gh repo create mmmugh/python-foundations --public --disable-wiki \
  --description "Python Foundations: a free, independent first course in programming, with every example runnable in the browser." \
  --homepage "https://mmmugh.github.io/python-foundations/"
gh repo view mmmugh/python-foundations --json visibility,isEmpty,url
```

Expected: `"visibility":"PUBLIC"`, `"isEmpty":true`.

- [ ] **Step 3: Secret scanning and push protection**

```bash
gh api -X PATCH repos/mmmugh/python-foundations --input - <<'JSON'
{"security_and_analysis": {"secret_scanning": {"status": "enabled"},
                           "secret_scanning_push_protection": {"status": "enabled"}}}
JSON
gh api repos/mmmugh/python-foundations --jq '.security_and_analysis'
```

Expected: both `"status":"enabled"`. (Criterion 10, second half.)

- [ ] **Step 4: The Actions secret**

```bash
gh secret set LEAK_PATTERNS_LOCAL --repo mmmugh/python-foundations < "$WR/.githooks/leak-patterns.local"
gh secret list --repo mmmugh/python-foundations
```

Expected: `LEAK_PATTERNS_LOCAL` listed. Its comment lines are harmless: `personal_sweep.sh` and `leak-scan` drop them, and strip trailing whitespace and CRs.

- [ ] **Step 5: Pages from GitHub Actions**

```bash
gh api -X POST repos/mmmugh/python-foundations/pages -f build_type=workflow
gh api repos/mmmugh/python-foundations/pages --jq '.build_type, .html_url'
```

Expected: `workflow`, then `https://mmmugh.github.io/python-foundations/`. If GitHub refuses to configure Pages on an empty repository, note the error and repeat this step right after Task 9; Task 10 then reruns the deploy.

---

### Task 9: The push

The one-way door. Everything before it can be undone; nothing in what it sends can be.

**Files:** none tracked. Changes `$PUB`'s remotes.

- [ ] **Step 1: Re-verify, against the working repository as it is now**

```bash
python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PUB" --tree-ref main~1 --added 1 \
  --personal "$WR/.githooks/leak-patterns.local" --remove WORKSHEET-2026-09-21-web-app.md \
  --metadata "$M" | tail -1
```

Expected: `20 checks, all pass: the rewrite meets criteria 2 to 6`. `[current]` passing means no commit reached the working repository since Task 5. If anything fails, stop.

- [ ] **Step 2: A new remote, and no remote-tracking refs**

```bash
cd "$PUB"
git remote remove origin
git remote add github git@github.com:mmmugh/python-foundations.git
git for-each-ref --format='%(refname)' refs/remotes | wc -l
git remote -v
```

Expected: `0`, then only `github`. Removing `origin` drops `refs/remotes/origin/*`, so a stray `--mirror` could not publish them, and a new remote name keeps pre-push's range the whole history (Review Focus 2).

- [ ] **Step 3: Scan everything one last time, the personal list included**

```bash
cd "$PUB"
LEAK_PATTERNS=/dev/null LEAK_PATTERNS_LOCAL="$WR/.githooks/leak-patterns.local" python3 scripts/scan_history.py --redact | tail -1
LEAK_PATTERNS_LOCAL=/dev/null python3 scripts/scan_history.py --redact | tail -1
git rev-parse --short main; git rev-list --count main
```

Expected: `N commits scanned, none blocked`, twice; the hash and count to tell Justin.

- [ ] **Step 4: Ask Justin**

Say exactly: push `run/public`'s `main` (hash and count from Step 3) to `github.com/mmmugh/python-foundations` as `main`, and nothing else: no other branch, no tag. Wait for a yes.

- [ ] **Step 5: Push**

```bash
cd "$PUB"
LEAK_PATTERNS_LOCAL="$WR/.githooks/leak-patterns.local" git push github main:main > "$RW/push.out" 2>&1; echo "exit=$?"
tail -4 "$RW/push.out"
git ls-remote github
gh api repos/mmmugh/python-foundations/tags --jq length
```

Expected: `exit=0` (the pre-push hook scanned every commit, with the personal list, and passed); `ls-remote` shows `HEAD` and `refs/heads/main` at the Step 3 hash and nothing else; `0` tags.

---

### Task 10: The first CI run, and the live site

Criterion 1.

- [ ] **Step 1: Watch the run**

```bash
id=$(gh run list --repo mmmugh/python-foundations --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$id" --repo mmmugh/python-foundations --exit-status > /dev/null; echo "exit=$?"
gh run view "$id" --repo mmmugh/python-foundations --json jobs --jq '.jobs[] | "\(.name)  \(.conclusion)"'
```

Expected: `exit=0`, and every job `success`: `leaks`, `build (3.9)`, `build (3.14)`, `node-gates`, `browser`, `deploy`, `live`. Write down the job names exactly as printed; Task 12 needs them. If `deploy` failed because Pages was not yet configured (Task 8 Step 5), configure it now, then `gh run rerun "$id" --repo mmmugh/python-foundations --failed` and watch again.

- [ ] **Step 2: The live site, from here**

```bash
curl -fsS https://mmmugh.github.io/python-foundations/build.txt; echo
git -C "$PUB" rev-parse main
cd "$WR/tests"
REQUIRE_BROWSER=1 SITE_URL=https://mmmugh.github.io/python-foundations/ node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 SITE_URL=https://mmmugh.github.io/python-foundations/ node browser_check_test.mjs | tail -1
```

Expected: the two hashes are equal; both browser tests print their pass line against the live site.

---

### Task 11: Swap the working copy's history for the public one

Done now, straight after the push, so that every branch the remaining tasks make is cut from the public history. Until this step the working repository still holds the old history, and a branch made from it and pushed would publish exactly what the rewrite removed. The directory stays where it is (the project memory is keyed by its path); only its `.git` changes, and every untracked file stays: the private worksheet, the personal list, the fetched runtime.

**Files:** moves `$WR/.git` to `~/python_foundations-notes/original-history.git`; the working tree's tracked files become the public `main`.

- [ ] **Step 1: Ask Justin**

Move the working copy's `.git` (the original history) into the notes directory, and put a clone of the public repository's history in its place, keeping every untracked file. Wait for a yes.

- [ ] **Step 2: Swap**

```bash
cd "$WR"
git status --short
git bundle verify "$HOME/python_foundations-notes/original-history.bundle" 2>&1 | tail -1
mv .git "$HOME/python_foundations-notes/original-history.git"
git clone -q --no-checkout git@github.com:mmmugh/python-foundations.git "$RW/swap"
mv "$RW/swap/.git" .git
rmdir "$RW/swap"
git reset -q --hard
git config user.name "Justin Stewart"
git config user.email 71140104+mmmugh@users.noreply.github.com
git config core.hooksPath .githooks
```

Expected: no status output before the move; `... is okay`. `git reset --hard` writes the public `main` over the tracked files: the translation commit's three documents change, nothing else, and untracked files are not touched.

- [ ] **Step 3: Check it (criterion 11)**

```bash
cd "$WR"
git log --oneline -1
git rev-parse main; git -C "$PUB" rev-parse main
git status --short
git remote -v
git config core.hooksPath; git config user.email
test -f .githooks/leak-patterns.local && echo "personal list present"
test -f WORKSHEET-2026-09-21-web-app.md && git check-ignore -q WORKSHEET-2026-09-21-web-app.md && echo "worksheet present, ignored"
git log --format='%ae%n%ce' | sort -u
```

Expected: the translation commit; equal hashes; no status output; `origin` is `git@github.com:mmmugh/python-foundations.git`; `.githooks`; the noreply address; `personal list present`; `worksheet present, ignored`; one address, the noreply one.

---

### Task 12: Branch protection

- [ ] **Step 1: Ask Justin**

Protect `main`: no force-push, no deletion, and pull requests must pass the five gate jobs before merging. Justin, as an admin, can still push to `main` directly (`enforce_admins: false`); say so, and ask whether he would rather require pull requests of himself too. Wait for a yes.

- [ ] **Step 2: Apply it**

Use the job names Task 10 printed; these are the expected ones.

```bash
gh api -X PUT repos/mmmugh/python-foundations/branches/main/protection --input - <<'JSON'
{"required_status_checks": {"strict": false,
   "contexts": ["leaks", "build (3.9)", "build (3.14)", "node-gates", "browser"]},
 "enforce_admins": false,
 "required_pull_request_reviews": null,
 "restrictions": null,
 "allow_force_pushes": false,
 "allow_deletions": false}
JSON
gh api repos/mmmugh/python-foundations/branches/main/protection \
  --jq '.required_status_checks.contexts, .allow_force_pushes.enabled, .allow_deletions.enabled'
```

Expected: the five names, `false`, `false`.

---

### Task 13: Prove CI catches what it is for

Criteria 7 and 8. Every branch here is made in the working repository, which since Task 11 holds the public history, and pushed to `origin`, the public repository. The changes are harmless or deliberately broken tests, and every branch is deleted afterwards. (Their commits stay fetchable by hash on GitHub; nothing in them is private.)

- [ ] **Step 1: Ask Justin**

Push five scratch branches to the public repository, open one pull request and close it unmerged, and delete the Actions secret for one run before restoring it. Wait for a yes.

- [ ] **Step 2: A pull request never deploys**

```bash
cd "$WR"
git switch -q -c ci-check-pr main
printf '\n<!-- CI check from Plan C, Task 13. -->\n' >> README.md
git commit -q -am "ci check: a pull request must not deploy

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin ci-check-pr
gh pr create --repo mmmugh/python-foundations --base main --head ci-check-pr \
  --title "CI check: a pull request must not deploy" --body "Scratch pull request for Plan C, Task 13. Closed unmerged."
gh pr checks ci-check-pr --repo mmmugh/python-foundations --watch > /dev/null; echo "checks exit=$?"
id=$(gh run list --repo mmmugh/python-foundations --branch ci-check-pr --event pull_request --limit 1 --json databaseId --jq '.[0].databaseId')
gh run view "$id" --repo mmmugh/python-foundations --json jobs --jq '.jobs[] | "\(.name)  \(.conclusion)"'
gh pr close ci-check-pr --repo mmmugh/python-foundations --delete-branch
git switch -q main && git branch -q -D ci-check-pr
```

Expected: `checks exit=0`; the five gates `success` and `deploy` and `live` `skipped`; the pull request closed and its branch deleted.

- [ ] **Step 3: One broken branch per gate, each red**

```bash
cd "$WR"
# leaks: the scanner's own test fails
git switch -q -c ci-check-leaks main
python3 - <<'PY'
from pathlib import Path
p = Path("tests/leak_scan_test.py")
p.write_text('raise SystemExit("deliberately broken: Plan C CI check")\n' + p.read_text())
PY
git commit -q -am "ci check: break the leaks job

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin ci-check-leaks
# build: a wrong expected output, the case the spec names
git switch -q -c ci-check-build main
python3 - <<'PY'
from pathlib import Path
import glob
p = Path(glob.glob("volumes/vol1-foundations/content/ch01-*.md")[0]); s = p.read_text()
old = "Output:\n\n```\nHello, world!\n```"
assert s.count(old) == 1
p.write_text(s.replace(old, "Output:\n\n```\nHello, World!\n```", 1))
PY
git commit -q -am "ci check: break the build job

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin ci-check-build
# node-gates and browser: one test in each fails; build stays green so both run
git switch -q -c ci-check-runtime main
python3 - <<'PY'
from pathlib import Path
for name in ("tests/validate_projects.mjs", "tests/browser_test.mjs"):
    p = Path(name)
    p.write_text('throw new Error("deliberately broken: Plan C CI check");\n' + p.read_text())
PY
git commit -q -am "ci check: break the node-gates and browser jobs

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin ci-check-runtime
git switch -q main
```

Then, for each of `ci-check-leaks`, `ci-check-build`, `ci-check-runtime`:

```bash
b=ci-check-leaks    # then ci-check-build, then ci-check-runtime
id=$(gh run list --repo mmmugh/python-foundations --branch "$b" --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$id" --repo mmmugh/python-foundations > /dev/null
gh run view "$id" --repo mmmugh/python-foundations --json jobs --jq '.jobs[] | "\(.name)  \(.conclusion)"'
```

Expected: `ci-check-leaks`: `leaks failure`, the rest `success` (deploy and live `skipped`, since this is not `main`). `ci-check-build`: both `build` legs `failure`, and `node-gates` and `browser` `skipped`, since they need it. `ci-check-runtime`: `build` `success`, `node-gates failure`, `browser failure`. Every gate has gone red once.

- [ ] **Step 4: An empty secret fails the personal sweep**

```bash
cd "$WR"
gh secret delete LEAK_PATTERNS_LOCAL --repo mmmugh/python-foundations
git switch -q -c ci-check-secret main
printf '\n<!-- CI check from Plan C, Task 13: empty secret. -->\n' >> README.md
git commit -q -am "ci check: the personal sweep with no secret

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin ci-check-secret
git switch -q main
id=$(gh run list --repo mmmugh/python-foundations --branch ci-check-secret --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$id" --repo mmmugh/python-foundations > /dev/null
gh run view "$id" --repo mmmugh/python-foundations --log-failed | grep -c 'PERSONAL_PATTERNS is empty'
gh secret set LEAK_PATTERNS_LOCAL --repo mmmugh/python-foundations < "$WR/.githooks/leak-patterns.local"
gh run rerun "$id" --repo mmmugh/python-foundations --failed
gh run watch "$id" --repo mmmugh/python-foundations --exit-status > /dev/null; echo "after restoring the secret: exit=$?"
```

Expected: a count of at least `1`, then `after restoring the secret: exit=0`. The sweep treats a push to `main` and to any other branch alike (only a fork's pull request is excused), so a branch push proves what criterion 8 asks of `main`.

- [ ] **Step 5: Clean up, and record what could not be proven**

```bash
cd "$WR"
for b in ci-check-leaks ci-check-build ci-check-runtime ci-check-secret; do
  git push -q origin --delete "$b"; git branch -q -D "$b"
done
gh api repos/mmmugh/python-foundations/branches --jq '.[].name'
git status --short
```

Expected: only `main`; no status output. Not provable from one account: the sweep's loud skip on a pull request from a fork (criterion 8, third clause). `personal_sweep_test.py` covers it; record it as covered by test, not by GitHub.

---

### Task 14: The fresh-clone check

Criteria 9, 2, 3 and 12, against the real public repository, following only its README.

- [ ] **Step 1: Clone and build, as a stranger would**

```bash
git clone -q https://github.com/mmmugh/python-foundations.git "$RW/fresh-clone"
cd "$RW/fresh-clone"
python3 build.py --check 2>&1 | tail -2
```

Expected: `... fetching them (once)` and `110 checked, 0 mismatched`.

- [ ] **Step 2: What the public history holds**

```bash
cd "$RW/fresh-clone"
git log --format='%ae%n%ce' | sort -u
git log --all --format= --name-only | grep -c -x 'WORKSHEET-2026-09-21-web-app.md' || true
git ls-files volumes/vol1-foundations/answer-keys | wc -l
ls LICENSE LICENSE-COURSE vendor/pyodide/LICENSE; grep -c '^## Licenses' README.md
```

Expected: exactly `71140104+mmmugh@users.noreply.github.com` (criterion 2); `0` (criterion 3); `12`; the three license files and `1` (criterion 12).

---

### Task 15: External notes, and closing out

Decision 12, and the record.

**Files:** outside the repository: `~/tokenwatt-notes/LEAK-SCAN-FINDINGS-2026-09-26.md`, `~/python_foundations-notes/pyfound-seed-prompt.txt`, `~/python_foundations-notes/SEED-PROMPT.txt`. In the repository: `docs/specs/public-release.md`.

- [ ] **Step 1: A note atop each external file that cites old hashes**

```bash
python3 - <<'PY'
from pathlib import Path
home = Path.home()
note = ("Note (Plan C cutover): the python-foundations commit hashes in this file name commits in the "
        "original history, kept in the archived private repository mmmugh/python-foundations-private. "
        "The public mmmugh/python-foundations carries a rewritten history; "
        "~/python_foundations-notes/rewrite/run/rewrite.git/filter-repo/commit-map maps each old "
        "hash to its new one.")
for path, prefix in ((home / "tokenwatt-notes/LEAK-SCAN-FINDINGS-2026-09-26.md", "> "),
                     (home / "python_foundations-notes/pyfound-seed-prompt.txt", ""),
                     (home / "python_foundations-notes/SEED-PROMPT.txt", "")):
    text = path.read_text()
    if "Plan C cutover" not in text:
        path.write_text(prefix + note + "\n\n" + text)
    print(f"noted: {path.name}")
PY
```

Expected: three `noted:` lines. The Java project's notes and repository are its own session's to handle: tell Justin the commit map's path, to pass on.

- [ ] **Step 2: Record the launch in the spec, as the first commit made in public**

Record the launch date in the status line, and which task checked each criterion:

```bash
cd "$WR"
python3 - "$(date +%F)" <<'PY'
import sys
from pathlib import Path
day = sys.argv[1]
p = Path("docs/specs/public-release.md"); s = p.read_text()
old = "Status: **approved 2026-10-05.**"
assert s.count(old) == 1
s = s.replace(old, f"Status: **launched {day}; approved 2026-10-05.**", 1)
old = "Each of these is a check someone can run, not a judgment.\n"
assert s.count(old) == 1
s = s.replace(old, old + f"""
**Results at launch ({day}), with the Plan C task that checked each:** 1, the
live job and the browser tests against the live URL (Task 10); 2, 3, 9 and 12,
the fresh clone (Task 14); 4, 5 and 6, `verify_rewrite.py` 20 of 20 (Task 5,
again in Task 9); 7, one broken branch per gate and a pull request that did
not deploy (Task 13); 8, the empty-secret run (Task 13), with the fork clause
covered by `personal_sweep_test.py` only, since one account cannot make a fork
pull request; 10, the refused scratch push and push protection (Tasks 6 and
8); 11, the swapped working copy (Task 11).
""", 1)
p.write_text(s)
PY
```

Then commit:

```bash
cd "$WR"
git add docs/specs/public-release.md
git commit -q -F - <<'MSG'
docs: the spec records the launch

Every success criterion, and the task in Plan C that checked it. The fork
pull request clause of criterion 8 is covered by personal_sweep_test.py, not
by GitHub, since it cannot be produced from one account.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
```

Ask Justin before pushing it: it is the first ordinary push to the public repository. Then `git push -q origin main`, and watch its run go green as in Task 10 Step 1.

- [ ] **Step 3: The private record**

Update the private worksheet's STATUS and NEXT, and the project memory: launched; the working copy holds the public history; the original history is in `~/python_foundations-notes/original-history.git`, in `original-history.bundle`, and in the archived private repository. Offer, and do not do unasked: deleting `$RW/run`, `$RW/fresh-clone` and the Docker image `pf-review-gnu`.

Plan C is done when Task 15's push is green and every success criterion has a result recorded against it.
