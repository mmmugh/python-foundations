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
