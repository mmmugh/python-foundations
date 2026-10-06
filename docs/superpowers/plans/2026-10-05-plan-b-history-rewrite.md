# Plan B: History Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking. Task 1 stops for Justin's approval.

**Goal:** Produce, locally and nowhere else, a rewritten copy of this repository's history that meets the spec's success criteria 2 to 6, plus one commit that points the hashes cited in files at the new history, ready for Plan C to push.

**Architecture:** The working repository is only read. A `--mirror --no-local` clone of it is rewritten by one `git filter-repo` run: mailmap, three paths removed, commit messages edited by exact phrase. A plain clone of the result is checked by a verify script that is first shown failing against an untouched clone, then gets one translation commit, then is built and tested the way a stranger would. All of Plan B's machinery lives in `~/python_foundations-notes/rewrite/`, outside the repository: it is one-time, and the mailmap it writes holds the address being removed.

**Tech Stack:** git-filter-repo 2.47.0 (Homebrew), git, Python 3.9+ stdlib, POSIX sh, gitleaks 8.30.1, the repository's own `scan_history.py` and `answer_key_guard.py`.

**Spec:** `docs/specs/public-release.md`, decisions 1 to 8. Decisions 5 to 8 (worksheet private, session trailers stripped, the afed4d6 correction, file hashes translated) were made by Justin on 2026-10-05 while this plan was written; read them before starting.

## Global Constraints

- **The working repository is read, never rewritten.** Plan B commits to it exactly once more (Task 2). After Task 4 runs the rewrite, nothing more is committed there. A later commit would be missing from the public history; `verify_rewrite.py`'s `[current]` check catches it, and the fix is to delete `run/` and repeat Tasks 4 to 6.
- **Nothing is pushed, and nothing touches GitHub.** The rewritten history stays in `~/python_foundations-notes/rewrite/run/`. Plan C pushes it.
- **The worksheet and the answer keys are backed up and verified before anything removes them, and are never deleted.**
- **Never type the personal Gmail address or the LAN address** into a tracked file, the plan, a commit message, or terminal output. `rewrite.sh` writes the mailmap from `git log` into the notes directory. The LAN address needs no handling of its own: every copy of it is inside the worksheet.
- **No dropped commit's hash appears in any tracked file.** Six commits are dropped; `translate_shas.py` refuses a file that cites one, because the citation would point at nothing. Refer to them by description. The message edits that must name two of them spell the hashes with `\x` escapes for that reason.
- **Python 3.9 floor** for every tool here, stdlib only, as for the repository's own scripts.
- **Every guard is shown failing once before it is trusted**, and the step says how.
- **Commit trailers.** Working-repository commits keep both trailers; the rewrite strips the session line from them like every other. The translation commit, made after the rewrite in `run/public`, carries `Co-Authored-By` only, per decision 6, and is made under the noreply identity set in that clone, because a fresh clone otherwise falls back to the global identity, which is the Gmail address.
- American spellings, `grey` excepted, and closed em dashes, in every message and file this plan writes.
- **Shell variables do not survive from one tool call to the next.** Begin every command block with
  `RW=$HOME/python_foundations-notes/rewrite; WR=$HOME/python_foundations; M=$RW/run/rewrite.git/filter-repo`.
  The blocks below assume it.

## Review Focus

The five failure modes the spec implies that its success criteria do not exercise, most likely first. Each is pinned in the task named.

1. **A commit reaches the working repository after the rewrite** and is silently missing from what goes public. Pinned by `verify_rewrite.py [current]`: the working repository's `main` must be in filter-repo's commit map. Shown failing in Task 3 (no map), passing in Task 4.
2. **A personal check that checks nothing.** A relative path to the list resolves inside the clone, where no list exists, and `leak-scan` skips a missing list without a word. This happened while this plan's verify script was being prototyped: an untouched clone, carrying 51 Gmail commits, passed. Pinned: `verify_rewrite.py` resolves the path and refuses a missing or empty list, shown in Task 3.
3. **A message edit that reaches a message it was not written for**, or "corrects" a quotation. The commit that Americanized the files lists the British words it replaced; a blind word swap would make it say it replaced "behavior" with "behavior". Pinned by `check_message_edits.py`: exact phrases only, a whitelist of the quoted lines, and `--expect-changed 15`. Task 3.
4. **A hex word in a file that is not a commit**, such as a checksum or a blob id, translated as if it were. Pinned by `translate_shas_test.py`. Task 3.
5. **The translation commit re-introducing the Gmail address** through the clone's fallback identity. Pinned by setting the identity in `run/public` (Task 5 Step 1) and by re-running `verify_rewrite.py`, whose criterion-2 check covers every commit, after the commit.

## What the rewrite will do, measured on 2026-10-05

| | Before | After |
| --- | --- | --- |
| Distinct author/committer addresses | 2 (51 commits on the Gmail address) | 1, the noreply address |
| `answer_key_guard.py --history` | 48 findings | 0 |
| `scan_history.py`, generic patterns | 2 commits blocked (the LAN line, in the worksheet) | 0 |
| `scan_history.py`, personal list | 51 blocked (identities) | 0 |
| gitleaks | 0 | 0 |
| Commits | all of them | six fewer: the commits whose only change was the worksheet |
| Messages edited besides trailers | | 15 |
| `Claude-Session` lines | one per commit since the trailers began | 0 |
| `main`'s tree | | identical to the working repository's |

No commit becomes empty from the answer-key paths alone: every commit that touched them changed other files too. The history is linear, unsigned, and has no merges. `web-app` and the lightweight tag `ws/web-app` are ancestors of `main`; the tag sits on a commit that is dropped, and filter-repo moves such a ref to the nearest commit it keeps.

## File Map

| File | Change | Responsibility |
| --- | --- | --- |
| `.gitignore` | modify | ignore the worksheet |
| `WORKSHEET-2026-09-21-web-app.md` | untrack | stays on disk, private |
| `$RW/inputs/message-edits.txt` | create | every message edit, one per line, in filter-repo's syntax |
| `$RW/inputs/mailmap` | generated | written by `rewrite.sh`; never typed, never tracked |
| `$RW/tools/check_message_edits.py` | create | preview the message edits against the real history |
| `$RW/tools/translate_shas.py` | create | point hashes cited in files at the new history |
| `$RW/tools/translate_shas_test.py` | create | prove it translates commits and nothing else |
| `$RW/tools/verify_rewrite.py` | create | criteria 2 to 6, plus refs, trailers and spellings |
| `$RW/tools/rewrite.sh` | create | mirror clone, one filter-repo run, plain clone |
| `$RW/run/rewrite.git` | generated | the rewritten mirror, with filter-repo's commit-map |
| `$RW/run/public` | generated | the clone that is verified, translated, tested, and pushed in Plan C |

---

### Task 1: Install git-filter-repo

Ask first: the spec lists installing `git-filter-repo` under "Ask first". Nothing in this task touches the repository.

**Files:** none.

**Interfaces:**
- Produces: `git filter-repo` on PATH, for Task 4.

- [ ] **Step 1: Ask Justin to approve one Homebrew formula**

Say what and why: `git-filter-repo`, the tool the spec names for the rewrite, recommended by git's own documentation over `filter-branch`. It runs only on a clone in the notes directory. Wait for a yes.

- [ ] **Step 2: Install and check**

```bash
brew install git-filter-repo
brew list --versions git-filter-repo
git --version
```

Expected: `git-filter-repo 2.47.0` (a newer 2.x is fine; note it in the handoff); any git 2.36 or later.

---

### Task 2: Make the worksheet private

Decision 5. The worksheet leaves version control here, so that the rewritten `main` can be compared to this one byte for byte (criterion 5). It stays on disk, and sessions keep using it; it just is not committed again.

**Files:**
- Create: `~/python_foundations-notes/worksheet-backup/` (outside the repository)
- Modify: `.gitignore`
- Untrack: `WORKSHEET-2026-09-21-web-app.md`

**Interfaces:**
- Produces: a `main` that tracks no worksheet. Task 4's tree-equality check relies on it.

- [ ] **Step 1: Check the worksheet is committed as it stands, then back it up**

```bash
cd "$WR"
git status --short WORKSHEET-2026-09-21-web-app.md
B="$HOME/python_foundations-notes/worksheet-backup"
mkdir -p "$B"
cp -p WORKSHEET-2026-09-21-web-app.md "$B/"
(cd "$B" && shasum -a 256 WORKSHEET-2026-09-21-web-app.md > SHA256SUMS && shasum -a 256 -c SHA256SUMS)
git show HEAD:WORKSHEET-2026-09-21-web-app.md | cmp - "$B/WORKSHEET-2026-09-21-web-app.md" && echo "backup equals HEAD"
```

Expected: `git status` prints nothing (if it prints ` M`, commit the worksheet first, then repeat); `WORKSHEET-2026-09-21-web-app.md: OK`; `backup equals HEAD`. **Stop here if either check fails.** The private repository on GitHub keeps every earlier version, but do not rely on it.

- [ ] **Step 2: Stop tracking it and ignore it**

```bash
git rm --cached -q WORKSHEET-2026-09-21-web-app.md
cat >> .gitignore <<'GITIGNORE'

# The session worksheet is private (decision 5 of docs/specs/public-release.md).
# It stays on disk and sessions keep writing to it; it is never committed.
WORKSHEET-2026-09-21-web-app.md
GITIGNORE
```

- [ ] **Step 3: Check it survived and is ignored**

```bash
test -f WORKSHEET-2026-09-21-web-app.md && echo "still on disk"
git check-ignore -q WORKSHEET-2026-09-21-web-app.md && echo ignored
git status --short
git add WORKSHEET-2026-09-21-web-app.md 2>&1 | head -1
```

Expected: `still on disk`; `ignored`; exactly `D  WORKSHEET-2026-09-21-web-app.md` and ` M .gitignore`; and the plain `git add` is refused with git's "paths are ignored" message. That refusal is the guard that keeps a habit from re-committing it, shown failing to add.

- [ ] **Step 4: Commit**

The message must not cite any of the six commits the rewrite drops, use a British spelling, or contain a line beginning `Claude-Session:` other than the trailer: Task 3's message checks run over it.

```bash
git add .gitignore
git commit -q -F - <<'MSG'
chore: the session worksheet is private now

Decision 5 of docs/specs/public-release.md. Its FEEDBACK block is internal,
so the worksheet stays on disk, where sessions keep using it, and is no
longer committed; .gitignore makes a plain git add refuse it. It was copied
to ~/python_foundations-notes/worksheet-backup with a SHA256SUMS manifest,
and the copy checked against the committed version, before git stopped
tracking it.

Plan B removes it from every earlier commit. Untracking it first means the
rewritten main can be compared to this one byte for byte.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: <session URL>
MSG
git log --oneline -1
```

- [ ] **Step 5: Tell future sessions**

Add one line to the project memory (`~/.claude/projects/-Users-<user>-python-foundations/memory/python-foundations-course.md`): the worksheet is private and untracked from this commit on; keep writing to it, never commit it, never tag `ws/*`. This overrides the global habit of committing the worksheet.

---

### Task 3: The tools and the inputs, each shown failing first

Everything here lives outside the repository, in `$RW`. Nothing is committed.

**Files:** all under `$RW`, as in the File Map.

**Interfaces:**
- Produces, for Tasks 4 to 6:
  - `python3 $RW/tools/check_message_edits.py REPO EDITS --remove PATH ... --expect-changed N` (exit 0 or 1)
  - `python3 $RW/tools/translate_shas.py COMMIT_MAP FILE ...` (exit 0, or 1 having written nothing)
  - `python3 $RW/tools/verify_rewrite.py --old OLD --new NEW --tree-ref REF --personal LIST --remove PATH ... [--metadata DIR] [--added N]` (exit 0 only if every check passes)
  - `sh $RW/tools/rewrite.sh WORKING_REPO RUN_DIR`
  - `$RW/inputs/message-edits.txt`

- [ ] **Step 1: Write the message edits**

```bash
mkdir -p "$RW/tools" "$RW/inputs"
```

Create `$RW/inputs/message-edits.txt` with exactly this content. Each line is `old==>new` in filter-repo's `--replace-message` syntax: literal lines are applied first, then `regex:` lines, in file order, to every commit message. The fifteen literal spelling lines are exact phrases, one per place a British spelling appears in prose; the lines of the commit that Americanized the files that *name* the British words are quotations and are deliberately absent. The two hashes of dropped commits are spelled with `\x` escapes (`\x33` is `3`, `\x30` is `0`) so that no 7-character hex word for a dropped commit appears in this tracked plan. The last line strips every `Claude-Session` trailer.

```text
Two judgement calls==>Two judgment calls
the scanner recognises a leak==>the scanner recognizes a leak
rather than the behaviour around it==>rather than the behavior around it
would be checking behaviour==>would be checking behavior
the only rasteriser this project==>the only rasterizer this project
compared against the colour it==>compared against the color it
The cursor was centred vertically==>The cursor was centered vertically
Rasterised at 16px==>Rasterized at 16px
Colours are the site's own==>Colors are the site's own
it did not recognise,==>it did not recognize,
asks that the licence travel==>asks that the license travel
about runtime behaviour was verified==>about runtime behavior was verified
labelled as what it is==>labeled as what it is
relabelled "A sample run"==>relabeled "A sample run"
relabelled "The book showed"==>relabeled "The book showed"
fix: --check leaked a temp file per box, until Python 3.14 choked on them==>fix: --check leaked a temp file per box into a temp dir that stalled Python 3.14
regex:The two million leaked files are not\ntouched from here:==>The two million entries are not\ntouched from here (most were never build.py's: deleting every tmp*.py more\nthan a day old later removed none):
regex:since 147fb\x33d, which is already pushed==>since the worksheet's first commit, which is already pushed
regex:\b147fb\x33d onward==>the worksheet's first commit onward
regex:\b975ae\x30a\.\.HEAD==>0840a6e..HEAD
regex:(?m)^Claude-Session: [^\n]*\n?==>
```

- [ ] **Step 2: Write the message-edit checker**

Create `$RW/tools/check_message_edits.py`:

```python
"""Preview the commit-message rewrite before git-filter-repo runs it.

    python3 check_message_edits.py REPO EDITS --remove PATH [--remove PATH ...]
                                   --expect-changed N

Applies EDITS to every commit message in REPO the way --replace-message does
(literal lines first, then regex: lines, all on bytes, in file order) and
refuses unless:

  - every line of EDITS changes at least one message. A line that changes
    nothing quoted the old text wrong, and the fix it exists for would
    silently not happen;
  - no Claude-Session trailer survives;
  - no British spelling survives, except the lines of the American-spellings
    commit that name the words it replaced. Those are quotations, and the
    rule is to leave a quotation as written;
  - no message still cites a commit the rewrite drops (one whose every change
    is under a --remove path). filter-repo translates the hashes it can and
    leaves those as they are, pointing at nothing;
  - with the trailers set aside, exactly N messages change, so no line
    reaches a message it was not written for.
"""

import argparse
import re
import subprocess
import sys

# Lines of the American-spellings commit that name the British words as the
# words it replaced. Changing them would make that message say it replaced
# "behavior" with "behavior".
QUOTED = {
    b"41 replacements across 13 files: honour, recognise, behaviour, licence,",
    b"modelled, centred, rasterising, colour and litres.",
    b"Most of it is comments and prose, but the litres are course content a learner",
    b"scripts/make_icons.py had colour as a local variable as well as in its",
}
STEMS = re.compile(
    rb"\b[A-Za-z]*(?:our(?:s|ed|ing)?|is(?:e|es|ed|ing|er|ers|ation|ations)|"
    rb"ys(?:e|es|ed|ing)|tre|tres|tred|lled|lling|ence|ogue|ogues|gement|amme|"
    rb"ammes|ilst|ngst)\b")
# Words those endings catch that are spelled the same in American English.
AMERICAN = set(b"""our ours four hour hours your yours tour pour flour sour detour
raise raises raised raising promise promises promised otherwise precise exercise
exercises exercised advise advised surprise surprised compromise expertise comprise
revise revised wise likewise noise concise premise premises rise rises arise praise
devise devised enterprise paradise clockwise pairwise
sense license licensed dense tense defense offense expense fence hence whence since
silence sentence science existence evidence reference references difference
differences sequence sequences experience instance occurrence confidence independence
presence absence audience essence consequence consequences influence preference
inference convenience patience violence conference intelligence dependence
persistence insistence once
called filled spelled rolled pulled killed installed polled scrolled stalled skilled
calling filling spelling rolling pulling killing installing polling scrolling
stalling falling smaller caller
""".split())


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], check=True,
                          capture_output=True).stdout


def load_edits(path):
    literals, regexes = [], []
    with open(path, "rb") as f:
        for raw in f:
            line = raw.rstrip(b"\r\n")
            if not line:
                continue
            old, _, new = line.rpartition(b"==>")
            if not _:
                sys.exit(f"{path}: a line without '==>': {line!r}")
            if old.startswith(b"regex:"):
                regexes.append((line, re.compile(old[6:]), new))
            else:
                literals.append((line, old, new))
    return literals, regexes


def apply(message, literals, regexes, used, sha):
    for line, old, new in literals:
        if old in message:
            used.setdefault(line, set()).add(sha)
            message = message.replace(old, new)
    for line, rx, new in regexes:
        message, n = rx.subn(new, message)
        if n:
            used.setdefault(line, set()).add(sha)
    return message


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("edits")
    ap.add_argument("--remove", action="append", default=[], required=True)
    ap.add_argument("--expect-changed", type=int, required=True)
    args = ap.parse_args()

    literals, regexes = load_edits(args.edits)
    trailer = [(l, rx, n) for l, rx, n in regexes if b"Claude-Session" in l]
    commits = git(args.repo, "rev-list", "--all").split()

    dropped = set()
    for sha in commits:
        paths = git(args.repo, "diff-tree", "--no-commit-id", "--name-only", "-r",
                    "--root", sha).splitlines()
        if paths and all(any(p == r.encode().rstrip(b"/") or p.startswith(r.encode())
                             for r in args.remove) for p in paths):
            dropped.add(sha)

    problems, used, changed = [], {}, 0
    for sha in commits:
        old = git(args.repo, "log", "-1", "--format=%B", sha)
        new = apply(old, literals, regexes, used, sha)
        if sha in dropped:
            continue                      # gone after the rewrite; nothing to check
        untrailered = apply(old, [], trailer, {}, sha)
        if new != untrailered:
            changed += 1
        short = sha[:7].decode()
        if re.search(rb"(?m)^Claude-Session:", new):
            problems.append(f"{short}: a Claude-Session trailer survives")
        for line in new.splitlines():
            if line.strip() in QUOTED:
                continue
            words = {w.decode() for w in STEMS.findall(line)
                     if w.lower() not in AMERICAN}
            if words:
                problems.append(f"{short}: British spelling survives: {sorted(words)} "
                                f"in {line.strip()[:70]!r}")
        for d in dropped:
            if re.search(rb"\b" + d[:7] + rb"[0-9a-f]*\b", new):
                problems.append(f"{short}: still cites {d[:7].decode()}, "
                                f"which the rewrite drops")

    for line, *_ in literals + regexes:
        if line not in used:
            problems.append(f"dead line, changes nothing: {line.decode()[:80]!r}")
    if changed != args.expect_changed:
        problems.append(f"{changed} messages change besides their trailers, "
                        f"expected {args.expect_changed}")

    for p in problems:
        print(f"  {p}")
    print(f"\n{len(commits)} messages, {len(dropped)} dropped by the rewrite, "
          f"{changed} edited besides trailers: "
          f"{'the edits do what they say and nothing else' if not problems else str(len(problems)) + ' problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 3: Watch it fail with no edits**

```bash
cd "$WR"
: > "$RW/inputs/empty.txt"
python3 "$RW/tools/check_message_edits.py" . "$RW/inputs/empty.txt" \
  --remove answer-keys/ --remove volumes/vol1-foundations/answer-keys/ \
  --remove WORKSHEET-2026-09-21-web-app.md --expect-changed 15 > "$RW/red-messages.txt"
echo "exit=$?"
grep -c 'trailer survives' "$RW/red-messages.txt"
grep -c 'British spelling survives' "$RW/red-messages.txt"
grep 'still cites' "$RW/red-messages.txt"
tail -1 "$RW/red-messages.txt"
```

Expected: `exit=1`. One `trailer survives` line per kept commit that has the trailer (57 at planning, plus one per commit made since); `16` British-spelling lines; exactly two `still cites` lines, one naming the worksheet's first commit and one naming the review-panel worksheet commit, each cited by a message the rewrite keeps; and a summary ending `0 edited besides trailers: N problem(s)`.

- [ ] **Step 4: Watch it pass with the real edits, under both Pythons**

```bash
for py in python3 /usr/bin/python3; do
  $py "$RW/tools/check_message_edits.py" . "$RW/inputs/message-edits.txt" \
    --remove answer-keys/ --remove volumes/vol1-foundations/answer-keys/ \
    --remove WORKSHEET-2026-09-21-web-app.md --expect-changed 15 | tail -1
done
```

Expected, twice: `... 6 dropped by the rewrite, 15 edited besides trailers: the edits do what they say and nothing else`. If a commit made since planning trips it (a British word, or an edit phrase in its message), fix that message's wording in a new line of the edits file and re-run; do not raise `--expect-changed` to make it pass.

- [ ] **Step 5: Write the translation test, and watch it fail**

Create `$RW/tools/translate_shas_test.py`:

```python
"""Check translate_shas.py moves commit citations and touches nothing else.

    python3 translate_shas_test.py
"""

import subprocess
import sys
import tempfile
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "translate_shas.py"
KEPT_OLD, KEPT_NEW = "1a2b3c4d" + "0" * 32, "9f8e7d6c" + "1" * 32
GONE_OLD = "5e6f7a8b" + "2" * 32
MAP = f"old new\n{KEPT_OLD} {KEPT_NEW}\n{GONE_OLD} {'0' * 40}\n"


def run(text):
    with tempfile.TemporaryDirectory() as tmp:
        cmap, doc = Path(tmp) / "commit-map", Path(tmp) / "doc.md"
        cmap.write_text(MAP)
        doc.write_text(text)
        done = subprocess.run([sys.executable, str(TOOL), str(cmap), str(doc)],
                              capture_output=True, text=True)
        return done.returncode, doc.read_text(), done.stdout + done.stderr


def main():
    results = []

    def expect(label, got, want):
        results.append((label, got == want, got, want))

    code, out, _ = run("fixed at 1a2b3c4 and again at 1a2b3c4d0000.\n")
    expect("a kept commit is translated, keeping each citation's length",
           (code, out), (0, "fixed at 9f8e7d6 and again at 9f8e7d6c1111.\n"))

    checksum = "1a2b3c4d" + "e" * 56
    code, out, _ = run(f"sha256 {checksum}\n")
    expect("a 64-character checksum that starts like a commit is left alone",
           (code, out), (0, f"sha256 {checksum}\n"))

    code, out, _ = run("the blob e69de29 and the run 551f6fc8\n")
    expect("hex that is no commit's prefix is left alone",
           (code, out), (0, "the blob e69de29 and the run 551f6fc8\n"))

    code, out, msg = run("see 1a2b3c4, and 5e6f7a8 which was dropped\n")
    expect("a citation of a dropped commit is refused, and the file left as it was",
           (code != 0, out, "5e6f7a8" in msg),
           (True, "see 1a2b3c4, and 5e6f7a8 which was dropped\n", True))

    bad = 0
    for label, ok, got, want in results:
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              f"{'' if ok else f'  (got {got!r}, wanted {want!r})'}")
    print(f"\n{'citations move with the history, and nothing else does' if not bad else f'{bad} wrong'}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

Run: `python3 "$RW/tools/translate_shas_test.py"`
Expected: `4 wrong`, because `translate_shas.py` does not exist yet.

- [ ] **Step 6: Write the translator, and watch the test pass under both Pythons**

Create `$RW/tools/translate_shas.py`:

```python
"""Point the commit hashes cited in files at the rewritten history.

    python3 translate_shas.py COMMIT_MAP FILE [FILE ...]

git-filter-repo rewrites the hashes cited in commit messages, but not those
cited in files. COMMIT_MAP is filter-repo's commit-map: a header line, then
"old new" per commit, with an all-zeros new hash for a commit it dropped.

In each FILE, every 7-to-40-character hex word that is the prefix of exactly
one old commit becomes the same-length prefix of that commit's new hash. A hex
word that is no commit's prefix, such as a checksum or a blob id, is left
alone. A word naming a dropped commit has nothing to point at, so it is
refused, and no file is written at all, rather than leaving a document citing
something that no longer exists.
"""

import re
import sys

HEX = re.compile(r"\b[0-9a-f]{7,40}\b")
NULL = "0" * 40


def load_map(path):
    with open(path) as f:
        header = f.readline().split()
        if header[:2] != ["old", "new"]:
            sys.exit(f"{path}: not a filter-repo commit-map (header {header})")
        return dict(line.split() for line in f if line.strip())


def translate(text, pairs):
    """(new text, number translated, problems)."""
    problems, count = [], 0

    def sub(match):
        nonlocal count
        word = match.group(0)
        hits = [old for old in pairs if old.startswith(word)]
        if not hits:
            return word
        if len(hits) > 1:
            problems.append(f"{word} is the prefix of {len(hits)} commits")
            return word
        new = pairs[hits[0]]
        if new == NULL:
            problems.append(f"{word} names a commit the rewrite dropped")
            return word
        count += 1
        return new[:len(word)]

    return HEX.sub(sub, text), count, problems


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    pairs = load_map(argv[0])
    results, problems = [], []
    for name in argv[1:]:
        with open(name, encoding="utf-8") as f:
            text = f.read()
        new, count, found = translate(text, pairs)
        problems += [f"{name}: {p}" for p in found]
        results.append((name, text, new, count))
    for p in problems:
        print(f"  {p}")
    if problems:
        print(f"\n{len(problems)} citation(s) cannot be translated; no file was written")
        return 1
    for name, text, new, count in results:
        if new != text:
            with open(name, "w", encoding="utf-8") as f:
                f.write(new)
        print(f"  {count:3} translated  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

```bash
python3 "$RW/tools/translate_shas_test.py" | tail -1
/usr/bin/python3 "$RW/tools/translate_shas_test.py" | tail -1
```

Expected, twice: `citations move with the history, and nothing else does`.

- [ ] **Step 7: Write the verify script**

Create `$RW/tools/verify_rewrite.py`:

```python
"""Check a rewritten history against the spec's success criteria 2 to 6.

    python3 verify_rewrite.py --old OLD --new NEW --tree-ref REF --personal LIST
                              --remove PATH [--remove PATH ...] [--metadata DIR]
                              [--added N]

OLD is the working repository the rewrite was made from. NEW is a non-bare
clone of the rewritten repository: answer_key_guard.py needs a work tree.
REF names the commit in NEW whose tree must equal OLD's main, the rewrite's own
tip, before anything committed on top of it. DIR is filter-repo's metadata
directory (commit-map, suboptimal-issues). N is how many commits were made in
NEW after the rewrite (default 0). LIST is the personal-strings file.

Every check prints one line naming the criterion it serves. Exit 0 only when
all pass. Run once against a plain clone of OLD first: it must fail, and the
failures say what the rewrite has to change.
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_message_edits import AMERICAN, QUOTED, STEMS   # noqa: E402

NOREPLY = "71140104+mmmugh@users.noreply.github.com"
CORRECTED_SUBJECT = "into a temp dir that stalled Python 3.14"
HEX = re.compile(r"\b[0-9a-f]{7,40}\b")


def git(repo, *args, check=True):
    done = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)
    if check and done.returncode:
        sys.exit(f"git {' '.join(args)} in {repo} failed: {done.stderr.strip()}")
    return done.stdout


def run(cmd, cwd, **env):
    full = dict(os.environ, **env)
    done = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=full)
    return done.returncode, (done.stdout + done.stderr).strip().splitlines()[-1:] or [""]


def under(path, removed):
    return any(path == r.rstrip("/") or path.startswith(r) for r in removed)


def dropped_by(repo, removed):
    """Commits in repo whose every change is under a removed path."""
    out = set()
    for sha in git(repo, "rev-list", "--all").split():
        paths = git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r",
                    "--root", sha).splitlines()
        if paths and all(under(p, removed) for p in paths):
            out.add(sha)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--tree-ref", required=True)
    ap.add_argument("--personal", required=True)
    ap.add_argument("--remove", action="append", required=True)
    ap.add_argument("--metadata")
    ap.add_argument("--added", type=int, default=0)
    args = ap.parse_args()
    old, new = args.old, args.new
    # Resolved here, not where the scanner runs: a relative path would name a
    # file inside NEW, which has none, and leak-scan skips a missing list
    # without a word -- a personal check that checks nothing and passes.
    personal = Path(args.personal).resolve()
    if not personal.is_file() or not any(
            l.strip() and not l.lstrip().startswith("#")
            for l in personal.read_text().splitlines()):
        sys.exit(f"refusing: {personal} is missing or holds no patterns")
    results = []

    def check(criterion, ok, what):
        results.append(ok)
        print(f"  {'ok  ' if ok else 'FAIL'}  [{criterion}] {what}")

    # The rewrite must be of OLD as it is now: a commit made to the working
    # repository after the rewrite would be missing from what goes public.
    old_main = git(old, "rev-parse", "main").strip()
    cmap = {}
    if args.metadata and (Path(args.metadata) / "commit-map").exists():
        lines = (Path(args.metadata) / "commit-map").read_text().split("\n")[1:]
        cmap = dict(l.split() for l in lines if l.strip())
    check("current", old_main in cmap,
          f"the rewrite covers the working repo's main as it is now ({old_main[:7]})")

    emails = set(git(new, "log", "--all", "--format=%ae%n%ce").split())
    check("2", emails == {NOREPLY},
          f"every author and committer is the noreply address ({len(emails)} distinct)")

    paths = set(git(new, "log", "--all", "--format=", "--name-only").split("\n")) - {""}
    bad = sorted(p for p in paths
                 if "answer-keys" in p.split("/") or under(p, args.remove))
    check("3", not bad, f"no removed path in any commit ({len(bad)} found)")
    code, last = run([sys.executable, "tests/answer_key_guard.py", "--history"], new)
    check("3", code == 0, f"answer_key_guard.py --history: {last[0]}")

    code, last = run([sys.executable, "scripts/scan_history.py", "--redact"], new,
                     LEAK_PATTERNS_LOCAL="/dev/null")
    check("4", code == 0, f"generic patterns over every commit: {last[0]}")
    code, last = run([sys.executable, "scripts/scan_history.py", "--redact"], new,
                     LEAK_PATTERNS="/dev/null", LEAK_PATTERNS_LOCAL=str(personal))
    check("4", code == 0, f"personal list over every commit: {last[0]}")
    code, _ = run(["gitleaks", "git", "--redact", "--no-banner",
                   "--log-opts=--all", "."], new)
    check("4", code == 0, f"gitleaks over every commit (exit {code})")

    old_tree = git(old, "rev-parse", "main^{tree}").strip()
    new_tree = git(new, "rev-parse", f"{args.tree_ref}^{{tree}}").strip()
    check("5", old_tree == new_tree,
          f"{args.tree_ref}'s tree equals the working repo's main ({new_tree[:7]} vs {old_tree[:7]})")
    expected = dropped_by(old, args.remove)
    actual = {o for o, n in cmap.items() if set(n) == {"0"}}
    check("5", bool(cmap) and actual == expected,
          f"dropped commits are the {len(expected)} predicted, no more, no fewer "
          f"({len(actual)} dropped)")
    old_count = int(git(old, "rev-list", "--count", "main"))
    new_count = int(git(new, "rev-list", "--count", args.tree_ref))
    check("5", new_count == old_count - len(expected),
          f"{args.tree_ref} has {new_count} commits; {old_count} less {len(expected)} dropped")
    on_top = int(git(new, "rev-list", "--count", f"{args.tree_ref}..main"))
    check("5", on_top == args.added,
          f"main is {args.tree_ref} plus {on_top} commit(s); expected {args.added}")

    # Every branch and tag survives, even one whose commit was dropped:
    # filter-repo moves such a ref to the nearest commit it kept.
    old_refs = [r for r in git(old, "for-each-ref", "--format=%(refname)",
                               "refs/heads", "refs/tags").split()]
    new_refs = set(git(new, "for-each-ref", "--format=%(refname)").split())
    missing = [r for r in old_refs
               if r.replace("refs/heads/", "refs/remotes/origin/") not in new_refs]
    check("refs", not missing, f"every branch and tag survives ({missing or 'all'})")

    messages = git(new, "log", "--all", "--format=%H%x00%B%x01")
    unresolved = set()
    trailers = british = 0
    corrected = False
    for entry in messages.split("\x01"):
        sha, _, body = entry.strip("\n").partition("\x00")
        if not sha:
            continue
        for word in set(HEX.findall(body)):
            if git(new, "cat-file", "-t", word, check=False).strip() != "commit":
                unresolved.add(word)
        trailers += len(re.findall(r"(?m)^Claude-Session:", body))
        corrected |= CORRECTED_SUBJECT in body
        for line in body.splitlines():
            if line.strip().encode() in QUOTED:
                continue
            british += sum(1 for w in STEMS.findall(line.encode())
                           if w.lower() not in AMERICAN)
    check("6", not unresolved,
          f"every hash a message cites is a commit here ({len(unresolved)} not: "
          f"{sorted(unresolved)[:5]})")
    # filter-repo translates the hashes cited in messages; files are this
    # plan's job (translate_shas.py), and until it runs this check fails.
    stale = set()
    for name in git(new, "ls-files").splitlines():
        try:
            text = (Path(new) / name).read_text(encoding="utf-8")
        except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
            continue
        for word in set(HEX.findall(text)):
            if any(o.startswith(word) and cmap[o] != o for o in cmap):
                stale.add(f"{name}:{word}")
    check("6", bool(cmap) and not stale,
          f"no tracked file cites a pre-rewrite commit ({len(stale)} citations do)")
    issues = Path(args.metadata or "/nonexistent") / "suboptimal-issues"
    check("6", issues.exists() and "No filtering problems" in issues.read_text(),
          "filter-repo reports no commit cited after being dropped")
    check("msg", trailers == 0, f"no Claude-Session trailer ({trailers} found)")
    check("msg", british == 0, f"no British spelling outside quotations ({british} found)")
    check("msg", corrected, "afed4d6's subject carries the corrected cause")

    failed = results.count(False)
    print(f"\n{len(results)} checks, "
          f"{'all pass: the rewrite meets criteria 2 to 6' if not failed else str(failed) + ' failed'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 8: Watch it fail against an untouched clone**

An untouched clone is the history as it would go public without Plan B, so nearly every check must fail, each for a reason the rewrite exists to remove.

```bash
PLAIN="$RW/red-plain"      # disposable: an untouched clone, kept only for this check
git clone -q --no-local "$WR" "$PLAIN"
/usr/bin/python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PLAIN" --tree-ref main \
  --personal "$WR/.githooks/leak-patterns.local" \
  --remove answer-keys/ --remove volumes/vol1-foundations/answer-keys/ \
  --remove WORKSHEET-2026-09-21-web-app.md; echo "exit=$?"
```

Expected: `exit=1`, `18 checks, 13 failed`. The thirteen: `[current]` (no commit map); `[2]` (2 distinct addresses); both `[3]` (25 removed paths, and 48 answer-key findings); both scans in `[4]` (generic: 2 blocked; personal: 51 blocked); `[5]` dropped commits and commit count; `[6]` file citations and the filter-repo report; and all three `[msg]` checks (trailers, 16 British spellings, the uncorrected subject). The five that pass are correct to pass on an untouched history: gitleaks, tree equality, nothing added on top, every ref present, and the hashes messages cite all resolve.

- [ ] **Step 9: Show the personal check refusing a list that checks nothing**

```bash
PLAIN="$RW/red-plain"
/usr/bin/python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PLAIN" --tree-ref main \
  --personal /nonexistent --remove x 2>&1 | tail -1
printf '# only a comment\n' > "$RW/inputs/comments-only.txt"
/usr/bin/python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$PLAIN" --tree-ref main \
  --personal "$RW/inputs/comments-only.txt" --remove x 2>&1 | tail -1
```

Expected, twice: `refusing: ... is missing or holds no patterns`.

- [ ] **Step 10: Write the rewrite script**

Create `$RW/tools/rewrite.sh`:

```sh
#!/bin/sh
# Rewrite the working repository's history into a fresh directory (Plan B).
#
#   sh rewrite.sh WORKING_REPO RUN_DIR
#
# RUN_DIR must not exist: the script refuses rather than reuse one. It makes
#   RUN_DIR/rewrite.git  a --mirror clone of WORKING_REPO, rewritten in place,
#                        with filter-repo's commit-map and reports in
#                        RUN_DIR/rewrite.git/filter-repo/
#   RUN_DIR/public       a plain clone of the rewritten history, which
#                        verify_rewrite.py checks and Plan C pushes from
# WORKING_REPO is only read. Nothing is pushed anywhere.
set -eu

NOREPLY=71140104+mmmugh@users.noreply.github.com
src=$(CDPATH= cd -- "$1" && pwd)
run=$2
inputs=$(CDPATH= cd -- "$(dirname -- "$0")/../inputs" && pwd)

if [ -e "$run" ]; then
  echo "refusing: $run already exists; delete it or choose another" >&2
  exit 1
fi

# The mailmap is written from the history itself, so the address it replaces
# is never typed into the plan or any tracked file. Exactly one address
# besides the noreply one is expected; anything else is a surprise worth
# stopping for.
others=$(git -C "$src" log --all --format='%ae%n%ce' | sort -u | grep -v -x -F "$NOREPLY" || true)
count=$(printf '%s' "$others" | grep -c . || true)
if [ "$count" -ne 1 ]; then
  echo "refusing: expected one address to map to the noreply one, found $count" >&2
  exit 1
fi
printf 'Justin Stewart <%s> <%s>\n' "$NOREPLY" "$others" > "$inputs/mailmap"

mkdir -p "$run"
# --no-local: a local clone hard-links its objects and fails filter-repo's
# fresh-clone check. filter-repo's manual names this flag as the fix, not
# --force, which would also switch off the checks that protect a real repo.
git clone -q --mirror --no-local "$src" "$run/rewrite.git"
(
  cd "$run/rewrite.git"
  git filter-repo \
    --mailmap "$inputs/mailmap" \
    --replace-message "$inputs/message-edits.txt" \
    --invert-paths \
    --path answer-keys/ \
    --path volumes/vol1-foundations/answer-keys/ \
    --path WORKSHEET-2026-09-21-web-app.md
)
git clone -q --no-local "$run/rewrite.git" "$run/public"
echo "rewritten: $run/rewrite.git"
echo "clone to verify and push from: $run/public"
```

```bash
sh -n "$RW/tools/rewrite.sh" && echo "syntax ok"
mkdir -p "$RW/run-refusal-check"
sh "$RW/tools/rewrite.sh" "$WR" "$RW/run-refusal-check" 2>&1 | tail -1
rmdir "$RW/run-refusal-check"
```

Expected: `syntax ok`, then `refusing: ... already exists; delete it or choose another`. The refusal is checked before anything else runs, so an earlier run is never overwritten.

---

### Task 4: The rewrite

**Files:** creates `$RW/run/` (rewrite.git and public). The working repository is only read.

**Interfaces:**
- Consumes: `rewrite.sh`, `message-edits.txt`, `verify_rewrite.py` (Task 3).
- Produces: `$RW/run/rewrite.git` with `filter-repo/commit-map`, and `$RW/run/public`, whose `main` is the rewritten history. Task 5 commits on top of it.

- [ ] **Step 1: Pre-flight**

```bash
cd "$WR"
git status --short
git branch --show-current
git rev-parse --short main
test -e "$RW/run" && echo "run/ exists: stop" || echo "no run/ yet"
```

Expected: no status output; `main`; a hash to write down; `no run/ yet`. If `run/` exists from an earlier attempt, look at it, then delete it only if it is this plan's own output.

- [ ] **Step 2: Rewrite**

```bash
sh "$RW/tools/rewrite.sh" "$WR" "$RW/run"
```

Expected: filter-repo's progress lines ending in a line like `New history written in ... seconds; now repacking/cleaning...` and `Completely finished after ... seconds.`, then `rewritten: .../run/rewrite.git` and `clone to verify and push from: .../run/public`. Nothing should print the Gmail address; if anything does, stop and tell Justin, without copying it.

- [ ] **Step 3: Read filter-repo's own report**

```bash
cat "$M/suboptimal-issues"
awk 'NR > 1 && $2 ~ /^0+$/' "$M/commit-map" | wc -l
cat "$M/ref-map"
git -C "$RW/run/rewrite.git" for-each-ref --format='%(refname)'
```

Expected: `No filtering problems encountered.`; `6` dropped; the ref-map lists `refs/heads/main`, `refs/heads/web-app` and `refs/tags/ws/web-app` with new hashes; and the mirror's refs are those three, with no `refs/remotes/` left. (The mirror copied the working repository's stale `refs/remotes/origin/main`; filter-repo deletes it and keeps `refs/heads/main`, as its source does when the two differ.)

- [ ] **Step 4: Verify**

```bash
python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$RW/run/public" --tree-ref main \
  --personal "$WR/.githooks/leak-patterns.local" \
  --remove answer-keys/ --remove volumes/vol1-foundations/answer-keys/ \
  --remove WORKSHEET-2026-09-21-web-app.md --metadata "$M"; echo "exit=$?"
```

Expected: `exit=1` with exactly one failure: `[6] no tracked file cites a pre-rewrite commit (N citations do)`, where N is the count of hashes cited in the spec and the two plans. That is Task 5's job, and it is this task's red. Every other check is `ok`, including `[current]`, `[2]` (1 distinct), both `[3]`, all three `[4]`, all `[5]` (tree equal, 6 dropped as predicted), `[refs]`, and the `[msg]` checks. If anything else fails: stop, note it, `rm -rf "$RW/run"`, fix the input, and repeat from Step 1.

- [ ] **Step 5: Look at the result with your own eyes**

```bash
cd "$RW/run/public"
git log --format='%h %ae %s' | head -5
git log --format=%B -1 :/'stalled Python 3.14' | head -3
git log --all --format=%B | grep -c '^Claude-Session:'
git log --format='%h %s' -1 ws/web-app
```

Expected: the noreply address on every line; the corrected afed4d6 subject; `0`; and the tag on the commit just before the review-panel worksheet commit it used to name.

---

### Task 5: Point the hashes cited in files at the new history

Decision 8. filter-repo translated the hashes in messages; this translates the ones in files, as one commit on top of the rewritten `main`.

**Files:** in `$RW/run/public` only: `docs/specs/public-release.md`, `docs/superpowers/plans/2026-10-05-plan-a-local-readiness.md`, `docs/superpowers/plans/2026-10-05-plan-b-history-rewrite.md`, and any other `.md` that cites a commit.

**Interfaces:**
- Consumes: `translate_shas.py` (Task 3), `$M/commit-map` (Task 4).
- Produces: `main` in `$RW/run/public` = the rewritten tip plus one commit. Plan C pushes this.

- [ ] **Step 1: Give the clone the right identity and the hooks**

```bash
cd "$RW/run/public"
git config user.name "Justin Stewart"
git config user.email 71140104+mmmugh@users.noreply.github.com
git config core.hooksPath .githooks
git config user.email
```

Expected: the noreply address. Without this the commit takes the global identity, which is the address the whole rewrite removed.

- [ ] **Step 2: Translate**

```bash
python3 "$RW/tools/translate_shas.py" "$M/commit-map" $(git ls-files '*.md')
git diff --stat
```

Expected: a `translated` line per file, nonzero for the spec and both plans, zero elsewhere; `git diff --stat` shows only those files. If it prints `cannot be translated; no file was written`, a file cites a dropped commit: reword that citation in the working repository, and start Plan B again from Task 4 (the working repository has changed).

- [ ] **Step 3: Commit, with the personal list active in the hook**

```bash
git add -A
LEAK_PATTERNS_LOCAL="$WR/.githooks/leak-patterns.local" git commit -q -F - <<'MSG'
docs: point cited commits at the rewritten history

filter-repo rewrote every commit, and with it the hashes cited in commit
messages, but not those cited in files. The spec and both plans cite commits
by hash; each citation now names the same commit in this history, at the same
length, from filter-repo's commit map. Nothing else changed.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
MSG
git log --format='%h %ae %s' -1
```

Expected: the commit, under the noreply address.

- [ ] **Step 4: Verify again: everything passes**

```bash
python3 "$RW/tools/verify_rewrite.py" --old "$WR" --new "$RW/run/public" --tree-ref main~1 --added 1 \
  --personal "$WR/.githooks/leak-patterns.local" \
  --remove answer-keys/ --remove volumes/vol1-foundations/answer-keys/ \
  --remove WORKSHEET-2026-09-21-web-app.md --metadata "$M"; echo "exit=$?"
```

Expected: `18 checks, all pass: the rewrite meets criteria 2 to 6`, `exit=0`. `--tree-ref main~1` because the tree that must equal the working repository's is the rewrite's own, before this commit.

---

### Task 6: Build and test the rewritten clone the way a stranger would

Not a spec criterion for Plan B, but the cheapest moment to find out that the rewritten history does not build: before it is public.

**Files:** none tracked. `vendor/pyodide/` and `tests/node_modules/` are filled in `run/public`; both are ignored.

- [ ] **Step 1: Pyodide, copied locally and checked against CHECKSUMS**

```bash
cd "$RW/run/public"
cp "$WR"/vendor/pyodide/pyodide* "$WR"/vendor/pyodide/python_stdlib.zip vendor/pyodide/
python3 scripts/fetch_pyodide.py | tail -1
```

Expected: `pyodide 314.0.7: 5 files match CHECKSUMS`. If a file is missing, `python3 scripts/fetch_pyodide.py --download` fetches it, which needs the network.

- [ ] **Step 2: Build under both Pythons, and every Python test**

```bash
python3 build.py --check | tail -1
/usr/bin/python3 build.py --check | tail -1
for py in python3 /usr/bin/python3; do
  for t in practice_test second_volume_test leak_scan_test pre_push_test \
           answer_key_guard_test scan_history_test personal_sweep_test workflow_test; do
    $py tests/$t.py > "$RW/t.out" 2>&1; printf "%-16s %-22s exit=%s\n" "$py" "$t" "$?"
  done
done
```

Expected: `110 checked, 0 mismatched` twice; sixteen `exit=0`.

- [ ] **Step 3: The Node and browser gates**

```bash
cd tests
npm ci --no-audit --no-fund > /dev/null
for t in verify2 validate_shipped validate_stdin validate_projects; do
  node $t.mjs > "$RW/n.out" 2>&1; printf "%-18s exit=%s\n" "$t" "$?"
done
REQUIRE_BROWSER=1 node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 BASE=/python-foundations/ node browser_test.mjs | tail -1
REQUIRE_BROWSER=1 node browser_check_test.mjs | tail -1
cd ..
git status --short
```

Expected: four `exit=0`; three success summaries; no status output.

---

### Task 7: Hand off to Plan C

**Files:** the private worksheet in the working repository (untracked now). Nothing is committed anywhere: a commit to the working repository would make the rewrite stale.

- [ ] **Step 1: Record what Plan C inherits**

Add a checkpoint to the worksheet with:
- `$RW/run/public` is what Plan C pushes; its `main` is the rewrite plus the translation commit. Record both hashes.
- `$M/commit-map` maps every old commit to its new one: Plan C's source for open question 7 (the Java brief and the tokenwatt findings cite old hashes) and for translating the private worksheet's own citations if Justin wants.
- The six dropped commits, by subject; and that `ws/web-app` now sits on the commit before its old one.
- `web-app` is a stale branch and `ws/web-app` tags a worksheet commit that is now private: recommend pushing `main` only. Plan C decides.
- **Any commit to the working repository from now on, including Plan C's own plan document, makes this rewrite stale.** Either write Plan C's plan first and repeat Tasks 4 to 6 (about ten minutes, all scripted), or commit Plan C's plan to the new repository after the push.
- Criterion 3 has a second half Plan B cannot check: the keys in their private companion, with matching checksums. That is open question 2, and Plan C's.
- `$RW/red-plain` (Task 3's untouched clone) is disposable; Justin may delete it.
- Still open: questions 2 (the keys' private companion), 3 (the old repository's name), 7 (external references), 8 (the course name, before Plan C). And whether commits after the cutover keep the `Claude-Session` trailer, which decision 6 strips from history but does not decide for the future.

- [ ] **Step 2: Confirm nothing left the machine**

```bash
cd "$WR"
git status --short
git log --oneline origin/main..main | wc -l
git -C "$RW/run/public" remote -v
```

Expected: no status output; the unpushed count; and `run/public`'s only remote is `origin` pointing at `$RW/run/rewrite.git`, a directory. Nothing was pushed.

Plan B is done when Task 5's verify passes, Task 6's gates are green, and Task 7 is recorded.
