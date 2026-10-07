# Spec: Python Foundations goes public

Status: **approved 2026-10-05.** Decisions marked **(decided)** were made by
Justin on that date; decisions 5 to 8 were added the same day, while Plan B was
being written, decision 9 after Plan B's final review, and decisions 10 to 13
on 2026-10-06, when the questions Plan C needed were settled. Decision 2 was
reversed that day. No question remains open.

## Objective

Publish Python Foundations as a public GitHub repository whose site is built
and deployed by CI to GitHub Pages, without publishing anything that should
not be public: the author's personal email, the LAN address once recorded in
the worksheet, the private worksheet itself, or any personal string. (The
quiz answer keys were on this list until decision 2 was reversed.)

Who it is for: a learner who wants to read the course in a browser, with
nothing to install, at `https://mmmugh.github.io/python-foundations/`; and
anyone who wants to read, build or adapt the source.

Success, in one sentence: a stranger can open the URL and run the examples, a
stranger can clone the repo and build it from the README alone, and the
repo's entire history contains nothing on the list above.

### What exists today

- `mmmugh/python-foundations` on GitHub, **private**, 43 commits locally, 17 of
  them never pushed.
- Every commit's author and committer is the personal Gmail address.
- Twelve quiz answer keys are tracked, and have been since they were first
  generated, under two paths: `answer-keys/` and, after the volume move,
  `volumes/vol1-foundations/answer-keys/`. Their source, `drafts.json`, was
  never tracked and **no longer exists anywhere on this machine**. The twelve
  files are the only copy of the answers.
- The LAN address is gone from the working tree but present in the added
  content of two historical commits (the worksheet's KEY-FACTS line). Every
  copy of it but one is inside the worksheet, which decision 5 removes. The
  other is a test fixture in 21a13f2 that built the address from two string
  literals, so no scan for the whole address could see it; the next commit,
  b595b31, says so and replaced it with a made-up one. An earlier draft of this
  spec said every copy was in the worksheet. The final review of Plan B found
  the fixture; decision 9 replaces it.
- Leak-scanning hooks are installed (`.githooks/`, 28 scanner cases, 7 push
  cases), but `.githooks/leak-patterns.local` was never created, so no
  personal string is checked anywhere.
- No CI. No LICENSE. `site/` is gitignored and built locally only.
- `browser_test.mjs` needs `playwright-core`, which `tests/package.json` listed
  only as an optional dependency with the range `^1.0.0`, and with the lockfile
  untracked nothing recorded what would be installed. (Corrected in Plan A: an
  earlier draft said it was declared nowhere.)
- `tests/package-lock.json` is gitignored, so `npm` installs are not
  reproducible.
- The in-browser round-trip test that proved the JSON boundary fix (a check
  expecting `None`, a check formatting `61.0`) also lived only in a
  scratchpad. Nothing in the repo covers that boundary in a real browser.

### Decisions **(decided)**

1. **History is rewritten, then pushed to a brand-new repository.** GitHub's
   own documentation says commits removed by a force-push stay reachable
   "directly via their SHA-1 hashes in cached views on GitHub" until Support
   garbage-collects them, so flipping the existing private repo public would
   expose exactly what the rewrite removed. A new repository never held those
   objects. The old private repo is renamed and kept, private, as a backup.
2. **Everything is public, the answer keys included. (Reversed 2026-10-06.)**
   First decided the other way: the keys were to leave the repository and its
   history for a private companion, and Plan A untracked them and added a
   guard. Justin reversed it before launch. The keys are tracked again, the
   history keeps them, and `tests/answer_key_guard.py` and its CI steps are
   retired. `build.py` still keeps them off the site, so the course pages stay
   free of answers; anyone who wants them finds them in the repository. Worked
   solutions are shown on the site behind a disclosure, as before.
3. **Licenses match Java Foundations.** CC BY-NC-SA 4.0 for the course
   (everything under `volumes/`), Apache-2.0 for everything else, third-party
   material under its own license (`vendor/pyodide/LICENSE`, MPL-2.0).
4. **The personal-strings sweep runs locally and in CI, redacted.** Locally,
   the hooks block before a commit exists. In CI, the same list comes from an
   Actions secret and catches commits made elsewhere. CI runs after a push, so
   on a public repo it detects rather than prevents, and its logs are public,
   so it never prints what matched.
5. **The worksheet is private.** `WORKSHEET-2026-09-21-web-app.md` is untracked
   and gitignored, backed up to the private notes directory, and removed from
   every commit by the rewrite. The six commits whose only change was the
   worksheet become empty and are dropped. Two commit messages cite two of
   them; the message edits reword those citations. (Was Open Question 4.)
6. **`Claude-Session` trailers are stripped** from every commit message by the
   rewrite. `Co-Authored-By` lines stay. The same session URL also sat in the
   plans' commit-message templates; it is replaced with `<session URL>` in the
   working copies and, by decision 9, in every older version. (Was Open
   Question 6.)
7. **One commit message is corrected.** 98c0b9c attributed the 2.1M-entry temp
   directory to build.py's leaked files; a later cleanup showed most were never
   build.py's. The rewrite replaces its subject and that one sentence, and
   leaves its measured facts as written. British spellings in messages are
   Americanized by exact phrase, not word by word, because the commit that
   Americanized the files names the British words it replaced, and those
   lines are quotations.
8. **Hashes cited in files are translated.** filter-repo rewrites the hashes
   cited in commit messages but not those in files. After the rewrite is
   verified, one commit on the new history maps each cited hash to its new one
   from filter-repo's commit map. The rewrite changes no file in `main`'s
   tree; decision 9 changes only older versions of files.
9. **Text replaced in every older blob**, by a `--replace-text` file that the
   rewrite script generates from history, so that nothing it removes is ever
   typed: the 21a13f2 fixture line becomes b595b31's made-up one; the session
   URL becomes `<session URL>`; and the home directory in Claude Code's
   dash-encoded form (`-Users-<name>-…`), which reached Plan B's text, becomes
   `-Users-<user>-…`. The working copies were changed the same way first, so
   criterion 5 holds, and `.githooks/leak-patterns` now blocks the dash form.
   Decided by Justin on 2026-10-06, after the final review of Plan B.
10. **The name stays "Python Foundations", with a disclaimer.** The README and
    the site's front page say the course is independent and free, is not
    affiliated with or endorsed by the Python Software Foundation or any other
    course, book or program of the same name, and that "Python" is a
    registered trademark of the PSF. (Was Open Question 8.)
11. **The old repository becomes `python-foundations-private`, archived.** It
    stays private and read-only, as the backup of the original history. The
    working copy's `origin` is pointed at it straight after the rename, before
    the new public repository takes the old name, so that no stray push can
    send the old history there. A git bundle of the full original history is
    kept in the private notes directory too, since the archived repository
    lacks the commits that were never pushed to it. (Was Open Question 3.)
12. **External references get a note, not a translation.** The tokenwatt
    findings and this project's seed prompts cite pre-rewrite hashes; each
    gains one line saying those hashes name commits in the archived private
    repository. The Java project's own notes and repository are its own
    session's business. (Was Open Question 7.)
13. **No commit carries a `Claude-Session` line from now on.** `Co-Authored-By`
    stays. A generic leak pattern for session URLs makes CI, which reads every
    commit message, refuse one, and a `commit-msg` hook refuses one locally,
    before the commit exists. That hook scans each message with the generic
    and personal lists, which nothing local did before.

## Tech Stack

| Piece | Version | Notes |
| --- | --- | --- |
| Python | 3.14 locally; **3.9 is the floor** | `build.py` is stdlib only; 3.9.6 is the `python3` that macOS's Command Line Tools provide |
| Node | 25 (v25.9.0 locally) | test harnesses only |
| Pyodide | 314.0.7 | fetched into `vendor/pyodide/`, pinned by `CHECKSUMS` |
| `pyodide` (npm) | 314.0.7 | already pinned in `tests/package.json` |
| `playwright-core` | 1.63.0 | pinned exactly; an optional dependency |
| gitleaks | pin at plan time | CLI binary, version and checksum pinned, not the Action |
| git-filter-repo | current | one-time rewrite; **not installed yet** |
| GitHub Actions | pinned by full commit SHA | public repo: no floating tags |

gitleaks is run as a pinned, checksummed binary rather than through its
Action, for the same reason Pyodide is pinned by `CHECKSUMS`: the project
does not run code it has not identified.

## Commands

Existing, unchanged:

```
python3 build.py --check                      # build site/ and verify every example
python3 scripts/serve.py [port]               # serve site/, default :8731
python3 scripts/fetch_pyodide.py              # verify vendor/pyodide/ against CHECKSUMS
python3 scripts/fetch_pyodide.py --download   # re-fetch anything missing or wrong
python3 scripts/make_icons.py                 # macOS only; re-render PNG icons

python3 tests/practice_test.py
python3 tests/second_volume_test.py
python3 tests/leak_scan_test.py
python3 tests/pre_push_test.py
(cd tests && npm ci && node verify2.mjs)
(cd tests && node validate_shipped.mjs)
(cd tests && node validate_stdin.mjs)
(cd tests && node validate_projects.mjs)
(cd tests && node browser_test.mjs)
```

New in this work (names are proposals; the plan may refine them):

```
python3 scripts/scan_history.py               # leak-scan every commit, not the final tree
python3 scripts/scan_history.py --redact      # what CI runs: never prints matched text
(cd tests && BASE=/python-foundations/ node browser_test.mjs)   # under the Pages subpath
(cd tests && SITE_URL=https://mmmugh.github.io/python-foundations/ node browser_test.mjs)
(cd tests && node browser_check_test.mjs)     # promoted from scratchpad: Check round-trip
python3 tests/answer_key_guard.py             # retired by Plan C: the keys are public (decision 2)
```

One-time, during the rewrite (Plan B):

```
brew install git-filter-repo
git clone --mirror --no-local <local repo> rewrite.git    # --no-local, or filter-repo's
cd rewrite.git                                            # fresh-clone check refuses it
git filter-repo --mailmap mailmap --replace-text blob-replacements.txt \
    --replace-message message-edits.txt \
    --invert-paths --path answer-keys/ --path volumes/vol1-foundations/answer-keys/ \
    --path WORKSHEET-2026-09-21-web-app.md
```

`scripts/scan_history.py` exists because scanning history is easy to get
wrong: `git diff <empty-tree> HEAD | leak-scan` looks like a history scan and
only scans the final tree. That mistake was made once already, during the
first audit of this repo. One script, used by CI and by hand, means the
correct loop is written once.

## Project Structure

New and changed paths only:

```
LICENSE                          Apache-2.0
LICENSE-COURSE                   CC BY-NC-SA 4.0
README.md                        gains a public-facing top section and a
                                 Licenses table; developer docs stay below
.github/workflows/ci.yml         gates, build, deploy, live check
.gitignore                       + the worksheet
.githooks/leak-scan              + LEAK_SCAN_REDACT mode
.githooks/leak-patterns.local    NEVER tracked; Justin's personal strings
scripts/scan_history.py          leak-scan over every commit
tests/package.json               playwright-core pinned to 1.63.0
tests/package-lock.json          now tracked, for npm ci
tests/browser_test.mjs           + BASE (subpath) and SITE_URL (live) modes
tests/browser_check_test.mjs     promoted from scratchpad
tests/answer_key_guard.py        added in Plan A, retired in Plan C (decision 2)
.githooks/commit-msg             Plan C: scans every message before it exists
docs/specs/public-release.md     this file
```

Outside the repo:

```
mmmugh/python-foundations-private   the current private repo, renamed; backup
<private companion>                 the twelve answer keys (see Open Questions)
```

## Code Style

Match what is already here. The conventions that matter most for this work:

- **Every guard is shown failing once,** on purpose, before it is trusted, and
  the commit message says how. A guard that has never failed has not been
  tested.
- **Guards are whitelists.** Deploy what was built and tested, by artifact,
  rather than rebuilding for deploy; check that only the noreply address
  appears in history, rather than that the Gmail address does not.
- **Fixtures that demonstrate a leak pattern are assembled from pieces,** or
  the hook refuses the commit that adds the test:

```python
# These fixtures ARE the shapes the guard blocks, so they are assembled from
# pieces rather than written out. A test file containing them literally could
# not be committed through the hook it tests.
GH_TOKEN = "ghp_" + "a" * 36
```

- **Comments and commit messages say why,** at length. The commit log is this
  project's design record; the Java port was briefed to read it.
- American spellings, `grey` excepted. Closed em dashes in docs; the book's
  prose keeps its spaced em dashes.
- No personal string in any tracked file, including this one.

## Testing Strategy

### The CI pipeline

One workflow, `.github/workflows/ci.yml`, on every push and every pull
request. Workflow-level `permissions: contents: read`; only the deploy job is
granted more. All actions pinned by commit SHA. No `pull_request_target`.

| Job | Needs | Runs |
| --- | --- | --- |
| `leaks` | — | `leak_scan_test.py`, `pre_push_test.py`, `scan_history.py --redact` with the generic patterns, gitleaks over full history with `--redact`, the personal sweep (`answer_key_guard.py` until Plan C retired it) |
| `build` | — | matrix Python 3.9 and 3.14: fetch and verify Pyodide (cached by `CHECKSUMS` hash), `build.py --check`, `practice_test.py`, `second_volume_test.py`. The 3.14 leg uploads `site/` twice from the same directory: once as a normal artifact for the other jobs, once as the Pages artifact |
| `node-gates` | `build` | `npm ci`, then `verify2`, `validate_shipped`, `validate_stdin`, `validate_projects` against the built `site/` |
| `browser` | `build` | Chromium via `playwright-core`; `browser_test` at the root **and** under `/python-foundations/`; `browser_check_test` |
| `deploy` | all of the above | only on push to `main`; deploys the Pages artifact that was tested — never a rebuild |
| `live` | `deploy` | polls the live site until its build marker matches the commit, then runs `browser_test` against the live URL and asserts content types |

The `checkout` in `leaks` uses full history (`fetch-depth: 0`); a shallow
clone would scan one commit and report the history clean.

### The personal sweep in CI

- The list lives in the Actions secret `LEAK_PATTERNS_LOCAL`, written to a
  temporary file for the job and pointed at by the scanner's existing
  `LEAK_PATTERNS_LOCAL` variable.
- Output is redacted: a match reports the commit and a count, never the line
  and **never the path**, because a filename can itself be the match. This is
  stricter than the "file:line" first proposed, for that reason.
- **On push to `main` with the secret missing, the job fails.** An empty
  pattern list matches nothing and looks exactly like a clean history.
- On a pull request from a fork, secrets are not available; the job prints an
  explicit skip rather than passing silently. The same check then runs on the
  merge commit to `main`.
- GitHub masks secret values in logs, but nothing here relies on it.

### Why a live check, and a build marker

Testing the build artifact proves the build. It does not prove that what a
reader receives from `mmmugh.github.io` works: a project site is served under
a subpath, Pages chooses its own content types, and a `.mjs` served as the
wrong type or a `.wasm` without `application/wasm` breaks Pyodide in ways a
local server never shows. Only a test against the real URL closes that loop.

Pages sends `cache-control: max-age=600`, so for up to ten minutes the CDN
may serve the previous deploy, and a live test could pass against the old
site. CI therefore writes the commit SHA into `site/build.txt` after
`build.py` (so `build.py` stays deterministic, and `--check` stays
byte-for-byte), and the `live` job waits for that file to match before
testing anything.

### New tests, and what each one must prove failing

| Test | Must fail when |
| --- | --- |
| `leak_scan_test.py` + redact cases | redacted output contains the pattern text, the matched line, or a matched path |
| `scan_history.py` (exercised in `pre_push_test.py` or its own test) | a leak in a middle commit, deleted later, is missed |
| `answer_key_guard.py` (retired in Plan C) | an answer key is tracked under any path, or a tracked file under `volumes/` carries the answer-key header |
| `browser_test.mjs` with `BASE` | any request escapes the subpath or the runtime fails to load there |
| `browser_check_test.mjs` | the JSON boundary fix is reverted (the `None` case and the `61.0` case both fail) |
| CI as a whole | a pushed branch with a wrong expected output, a token, or a broken page goes red — proven once per job |

## Boundaries

**Always**
- Run every gate before committing, and show each new guard failing once.
- Back up the answer keys and verify the backup by checksum **before** any
  step that removes them.
- Deploy only the artifact that passed the gates.
- Pin actions by SHA; grant the minimum `permissions` per job.
- Keep personal strings out of tracked files, commit messages and CI logs.

**Ask first**
- Anything that touches GitHub: creating or renaming a repository, changing
  repository or account settings, adding secrets, enabling Pages, branch
  protection, and **every push**.
- Installing `git-filter-repo`, adding `playwright-core`, adding gitleaks.
- Editing files outside this repository — the Java port's notes and the
  tokenwatt findings both cite commit SHAs that the rewrite will change.
- A custom domain, Dependabot, or any automation that opens pull requests.
- Deleting anything: the old private repo, the answer-key backup, the old
  local working copy.

**Never**
- Commit `.githooks/leak-patterns.local`, or the personal list in any form.
- Push the old history to the new repository, or make the old repository
  public.
- Use `pull_request_target`, or print a secret or a matched personal string.
- Land work with `--no-verify`.
- Delete the answer keys without a verified backup. They are irreplaceable.

## Success Criteria

Each of these is a check someone can run, not a judgment.

1. `https://mmmugh.github.io/python-foundations/` serves the course; the `live`
   job passes against it: Run prints `Hello, world!`, no request leaves the
   origin, `.mjs` and `.wasm` arrive with working content types, and
   `build.txt` equals the deployed commit.
2. `git log --format='%ae%n%ce' | sort -u` on the public repo prints exactly one
   line: `71140104+mmmugh@users.noreply.github.com`.
3. No commit in the public history contains the worksheet. (This criterion
   also covered the answer keys until decision 2 was reversed; the twelve keys
   are now tracked, and match the checksummed backup.)
4. `scan_history.py` with the generic and the personal patterns, and gitleaks,
   all report zero findings across every commit of the public history.
5. The rewritten `HEAD`'s tree equals the pre-rewrite `HEAD`'s tree — the
   answer keys having been untracked in Plan A — so the rewrite changed
   history and nothing else. Any commit dropped because it became empty is
   listed, not discovered: six are predicted, the commits whose only change
   was the worksheet.
6. Every commit SHA quoted in a commit message resolves in the new history.
7. CI runs every gate on push and on pull request; a deliberately broken
   branch turns each job red once; pull requests never deploy.
8. The personal sweep redacts (proven by test), fails on `main` when its secret
   is missing, and skips loudly on fork pull requests.
9. A fresh clone of the public repo, following only its README, passes
   `build.py --check`.
10. Push protection is on, and **Block command line pushes that expose my
    email** is on — proven by a scratch push of a commit carrying the old
    address being rejected.
11. Locally: hooks active, `leak-patterns.local` present, and
    `user.email` set to the noreply address.
12. `LICENSE`, `LICENSE-COURSE` and the README's Licenses table are present,
    and the Pyodide license notice is retained.

## Proposed Split into Plans

Split by reversibility. Each plan ends where the next step is harder to undo.

**Plan A — local readiness.** No history rewrite, nothing on GitHub. Back up
and untrack the answer keys; licenses and README; personal list; redact mode,
`scan_history.py`, `answer_key_guard.py`; subpath and live modes for
`browser_test`; promote `browser_check_test`; declare `playwright-core` and
track the lockfile; write `ci.yml` and lint it. Ends with every gate green
locally. Fully reversible.

**Plan B — history rewrite.** On a mirror clone; the working repo is not
touched. Mailmap; path removal for both answer-key directories and the
worksheet; text replaced in older blobs (decision 9); message edits
(spellings by exact phrase, the 98c0b9c correction, the session trailers);
then one commit translating the hashes cited in files.
Verify criteria 2 through 6 locally and keep filter-repo's commit map. Nothing
pushed. Reversible: delete the clone.

**Plan C — cutover.** It begins locally, because the questions it needed
changed what goes public: the answer keys are tracked again (decision 2), the
disclaimer is written (10), session lines are refused locally and in CI (13),
and Plan B's rewrite is run again with the answer-key paths kept. Then the
GitHub steps, each of which needs Justin's explicit go-ahead: prove the email
block, bundle the original history, rename and archive the old repo and
re-point the working copy (11), create the new one with push protection, the
Actions secret and the Pages source, then push. Watch the first CI run, add
branch protection once its checks exist, prove CI catches breakage, verify the
live site, run the fresh-clone check, swap the working copy's history for the
new repository's while keeping its untracked files, and add a note to each
external reference (12). The push is the one-way door: once public, anything
in that history is public.

## Open Questions

1. **The personal list — resolved.** It exists, locally only, in
   `.githooks/leak-patterns.local`; its contents are deliberately not here.
2. **The private companion for the keys — moot.** Decision 2 was reversed;
   the keys are public.
3. **The old repository's new name — resolved.** See decision 11.
4. **The worksheet — resolved: private.** See decision 5.
5. **Python 3.9 in CI — resolved: keep it.** The first draft of this question
   said 3.9 "may not be installable on current runners". That was never
   checked, and it is false: setup-python's manifest carries 3.9.25 for Ubuntu
   22.04 and 24.04, x64 and arm64. It also missed why 3.9 matters. On a Mac,
   `/usr/bin/python3` is the same stub binary as `/usr/bin/git`, both handing
   off to the Command Line Tools, whose Python is 3.9.6 (June 2021, branch
   end-of-life since 2025-10-31). Anyone who can run the README's `git clone`
   already has that interpreter, so supporting it is what makes "nothing to
   install" true. Re-verified 2026-10-05: `build.py --check` and all four
   Python tests pass under 3.9.6. The 3.9 row in the CI matrix is the only
   thing that would catch a 3.10+ feature slipping into `build.py`. The README
   should say 3.9 *works* and recommend a current Python, not endorse 3.9.
6. **`Claude-Session` trailers — resolved: stripped.** See decision 6.
7. **External references — resolved: a note in each.** See decision 12.
8. **The course's name — resolved: "Python Foundations", with a disclaimer.**
   See decision 10. The research that informed it follows. The Pages URL
   contains the repo name and a rename after launch moves the site and breaks
   every shared link. Researched 2026-10-05: neither "Python Foundations" nor
   "Java Foundations" is a registered US mark (a register mirror, not a
   clearance search). But neither name is stale. "Python Foundations" is in
   active use by Pluralsight, Coursera/Packt, Zenva, and a book series launched
   in 2026; the PSF policy allows "Python" in the name of a free publication,
   but not inside a trademark of one's own. "Java Foundations" is the name of
   Oracle's own beginner course and of Oracle's 1Z0-811 exam, and Oracle's Java
   branding guidelines list "Java [My Product]" as the incorrect form, "[My
   Product] for Java" as the correct one. So the Java course must be renamed
   regardless, and a shared family name for both courses is worth
   considering. A rename touches titles across the whole site, so the
   user-facing text in Plan A (README introduction, license headers) is best
   written after this is settled.
