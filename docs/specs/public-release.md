# Spec: Python Foundations goes public

Status: **approved 2026-10-05.** Decisions marked **(decided)** were made by
Justin on that date; everything under Open Questions is not yet decided.

## Objective

Publish Python Foundations as a public GitHub repository whose site is built
and deployed by CI to GitHub Pages, without publishing anything that should
not be public: the author's personal email, the quiz answer keys, the LAN
address once recorded in the worksheet, or any personal string.

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
  content of two historical commits (the worksheet's KEY-FACTS line).
- Leak-scanning hooks are installed (`.githooks/`, 28 scanner cases, 7 push
  cases), but `.githooks/leak-patterns.local` was never created, so no
  personal string is checked anywhere.
- No CI. No LICENSE. `site/` is gitignored and built locally only.
- `browser_test.mjs` needs `playwright-core`, which is declared nowhere in the
  repo; the copy it ran against lived in a session scratchpad and is gone.
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
2. **Answer keys are private; everything else is public.** The twelve keys
   leave the repository and every commit of its history, and live in a private
   companion. Worked solutions are already shown on the site behind a
   disclosure, and the test fixtures in `tests/` must stay public because CI
   cannot validate the checks without them.
3. **Licenses match Java Foundations.** CC BY-NC-SA 4.0 for the course
   (everything under `volumes/`), Apache-2.0 for everything else, third-party
   material under its own license (`vendor/pyodide/LICENSE`, MPL-2.0).
4. **The personal-strings sweep runs locally and in CI, redacted.** Locally,
   the hooks block before a commit exists. In CI, the same list comes from an
   Actions secret and catches commits made elsewhere. CI runs after a push, so
   on a public repo it detects rather than prevents, and its logs are public,
   so it never prints what matched.

## Tech Stack

| Piece | Version | Notes |
| --- | --- | --- |
| Python | 3.14 locally; **3.9 is the floor** | `build.py` is stdlib only; 3.9.6 is the `python3` that macOS's Command Line Tools provide |
| Node | 25 (v25.9.0 locally) | test harnesses only |
| Pyodide | 314.0.7 | fetched into `vendor/pyodide/`, pinned by `CHECKSUMS` |
| `pyodide` (npm) | 314.0.7 | already pinned in `tests/package.json` |
| `playwright-core` | pin at plan time | to be declared as a devDependency |
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
python3 tests/answer_key_guard.py             # no answer key tracked, by path or content
```

One-time, during the rewrite (Plan B):

```
brew install git-filter-repo
git clone --mirror <local repo> rewrite.git
git -C rewrite.git filter-repo --mailmap mailmap --replace-text replacements \
    --invert-paths --path answer-keys/ --path volumes/vol1-foundations/answer-keys/ \
    --message-callback '<American spellings, from the df232d4 word list>'
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
.gitignore                       + volumes/*/answer-keys/
.githooks/leak-scan              + LEAK_SCAN_REDACT mode
.githooks/leak-patterns.local    NEVER tracked; Justin's personal strings
scripts/scan_history.py          leak-scan over every commit
tests/package.json               + playwright-core (devDependency)
tests/package-lock.json          now tracked, for npm ci
tests/browser_test.mjs           + BASE (subpath) and SITE_URL (live) modes
tests/browser_check_test.mjs     promoted from scratchpad
tests/answer_key_guard.py        new
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
| `leaks` | — | `leak_scan_test.py`, `pre_push_test.py`, `scan_history.py --redact` with the generic patterns, gitleaks over full history with `--redact`, the personal sweep, `answer_key_guard.py` |
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
| `answer_key_guard.py` | an answer key is tracked under any path, or a tracked file under `volumes/` carries the answer-key header |
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
3. No commit in the public history contains a path with `answer-keys` in it,
   and the twelve keys exist in the private companion with checksums matching
   the originals.
4. `scan_history.py` with the generic and the personal patterns, and gitleaks,
   all report zero findings across every commit of the public history.
5. The rewritten `HEAD`'s tree equals the pre-rewrite `HEAD`'s tree — the
   answer keys having been untracked in Plan A — so the rewrite changed
   history and nothing else. Any commit dropped because it became empty is
   listed, not discovered.
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
touched. Mailmap, path removal for both answer-key directories, text
replacement, message spellings. Verify criteria 2 through 6 locally and keep
filter-repo's commit map. Nothing pushed. Reversible: delete the clone.

**Plan C — cutover.** Every step here needs Justin's explicit go-ahead. Rename
the old repo, create the new one, set push protection, the email block, the
Actions secret and the Pages source, then push. Watch the first CI run, add
branch protection once its checks exist, verify the live site, run the
fresh-clone check, swap the local working copy for a clone of the new repo
while keeping the untracked files it needs, and — if approved — update the
SHAs cited outside the repo. The push is the one-way door: once public,
anything in that history is public.

## Open Questions

1. **The personal list.** What goes in it is Justin's call. Candidates are
   discussed in conversation, deliberately not here.
2. **The private companion for the keys.** A private repository (proposed:
   `mmmugh/python-foundations-answers`, cloned into the now-ignored
   `answer-keys/` path so authoring does not change) or the private notes
   directory.
3. **The old repository's new name.** Proposed:
   `python-foundations-private`.
4. **The worksheet** (`WORKSHEET-2026-09-21-web-app.md`). It is part of the
   design record, and the Java port reads it, but its FEEDBACK block is
   internal. Keep it as is, move it under `docs/`, or keep it private.
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
6. **`Claude-Session` trailers.** They become public. They grant no access, but
   they do expose session IDs. The default is to keep them.
7. **External references.** The Java brief and the tokenwatt findings cite
   SHAs that the rewrite will change. Update them from the commit map, or note
   the change once in each.
8. **The course's name. Must be decided before Plan C,** because the Pages URL
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
