#!/usr/bin/env bash
#
# sync-to-github.sh — stage, commit and push the Client-Management-System
# folder to GitHub, with pre-flight guards.
#
#   ./scripts/sync-to-github.sh                 # normal sync
#   ./scripts/sync-to-github.sh -m "message"    # custom commit message
#   ./scripts/sync-to-github.sh --dry-run       # show what would happen, push nothing
#   ./scripts/sync-to-github.sh --scan-only     # run the secret scan and exit
#
# Config lives in .env (copy from .env.example). .env is gitignored.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

red()  { printf '\033[31m%s\033[0m\n' "$*"; }
grn()  { printf '\033[32m%s\033[0m\n' "$*"; }
ylw()  { printf '\033[33m%s\033[0m\n' "$*"; }
die()  { red "ABORT: $*"; exit 1; }

# ── args ──────────────────────────────────────────────────────────
DRY_RUN=false; SCAN_ONLY=false; MSG=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--message) MSG="${2:-}"; shift 2 ;;
    --dry-run)    DRY_RUN=true; shift ;;
    --scan-only)  SCAN_ONLY=true; shift ;;
    -h|--help)    sed -n '2,14p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)            die "unknown argument: $1" ;;
  esac
done

# ── config ────────────────────────────────────────────────────────
[[ -f .env ]] || die ".env not found. Run: cp .env.example .env"
set -a; . ./.env; set +a

GIT_REMOTE="${GIT_REMOTE:-origin}"
GIT_BRANCH="${GIT_BRANCH:-main}"
COMMIT_PREFIX="${COMMIT_PREFIX:-Sync}"
REQUIRE_PRIVATE_REPO="${REQUIRE_PRIVATE_REPO:-true}"
SCAN_FOR_SECRETS="${SCAN_FOR_SECRETS:-true}"
CONFIRM_BEFORE_PUSH="${CONFIRM_BEFORE_PUSH:-true}"

git rev-parse --git-dir >/dev/null 2>&1 || die "not a git repository"

# ── 1. remote sanity ──────────────────────────────────────────────
ACTUAL_URL="$(git remote get-url "$GIT_REMOTE" 2>/dev/null || true)"
[[ -n "$ACTUAL_URL" ]] || die "remote '$GIT_REMOTE' does not exist"
if [[ -n "${GIT_REMOTE_URL:-}" && "$ACTUAL_URL" != "$GIT_REMOTE_URL" ]]; then
  die "remote '$GIT_REMOTE' is $ACTUAL_URL but .env expects $GIT_REMOTE_URL"
fi
grn "remote ok  → $ACTUAL_URL"

# ── 2. visibility guard ───────────────────────────────────────────
# A public repo would expose client profiles, meeting notes and lead PII.
SLUG="$(printf '%s' "$ACTUAL_URL" | sed -E 's#^(git@github\.com:|https://github\.com/)##; s#\.git$##')"
if [[ "$REQUIRE_PRIVATE_REPO" == "true" ]]; then
  CODE="$(curl -s -o /dev/null -w '%{http_code}' "https://api.github.com/repos/$SLUG" || echo 000)"
  case "$CODE" in
    200) die "$SLUG is PUBLIC — anyone can read this repo. Make it private in GitHub
       Settings → General → Danger Zone → Change visibility, then re-run.
       (To knowingly push to a public repo: set REQUIRE_PRIVATE_REPO=false in .env)" ;;
    404) grn "visibility ok  → $SLUG is private (or not visible anonymously)" ;;
    *)   ylw "visibility check inconclusive (HTTP $CODE) — continuing" ;;
  esac
else
  ylw "visibility guard DISABLED — pushing regardless of public/private"
fi

# ── 3. stage ──────────────────────────────────────────────────────
git add -A
if git diff --cached --quiet; then grn "nothing to commit — working tree clean"; exit 0; fi

# NUL-delimited so paths with spaces/non-ASCII (e.g. "Cüneyt …") stay intact.
# Hand-rolled loop rather than mapfile -d: macOS ships bash 3.2.
STAGED_ARR=()
while IFS= read -r -d '' _p; do STAGED_ARR+=("$_p"); done \
  < <(git diff --cached --name-only -z)
COUNT="${#STAGED_ARR[@]}"
[[ "$COUNT" -eq 0 ]] && { grn "nothing to commit"; exit 0; }
STAGED="$(printf '%s\n' "${STAGED_ARR[@]}")"
echo; ylw "$COUNT file(s) staged:"; printf '%s\n' "$STAGED" | sed 's/^/    /' | head -40
[[ "$COUNT" -gt 40 ]] && echo "    … and $((COUNT-40)) more"

# ── 4. pre-flight secret scan ─────────────────────────────────────
if [[ "$SCAN_FOR_SECRETS" == "true" ]]; then
  echo; ylw "scanning staged files for credentials…"
  FINDINGS=""

  # 4a. filename denylist
  NAME_HITS="$(printf '%s\n' "$STAGED" \
    | grep -ivE '\.(example|sample|template|dist)$' \
    | grep -iE '(^|/)\.env($|\.)|client_secret|_token\.json|credential|(password|passwords)\.(csv|txt|xlsx)|\.(pem|key|p12|pfx)$' || true)"
  [[ -n "$NAME_HITS" ]] && FINDINGS+=$'sensitive filename:\n'"$(printf '%s\n' "$NAME_HITS" | sed 's/^/    /')"$'\n'

  # 4b. content patterns (skip binaries)
  PAT='sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{20,}|gho_[A-Za-z0-9]{36}|AIza[0-9A-Za-z_-]{35}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----'
  while IFS= read -r f; do
    [[ -f "$f" ]] || continue
    case "$f" in *.xlsx|*.docx|*.pdf|*.png|*.jpg|*.jpeg|*.gif|*.zip) continue ;; esac
    HIT="$(grep -nIoE "$PAT" "$f" 2>/dev/null | head -2 || true)"
    [[ -n "$HIT" ]] && FINDINGS+="credential in $f:"$'\n'"$(printf '%s\n' "$HIT" | cut -c1-24 | sed 's/^/    /; s/$/…/')"$'\n'
  done < <(printf '%s\n' "${STAGED_ARR[@]}")

  # 4c. CSV/XLSX with a password column header
  while IFS= read -r f; do
    [[ -f "$f" && "$f" == *.csv ]] || continue
    head -1 "$f" 2>/dev/null | grep -qiE '(^|,)"?pass(word)?"?(,|$)' \
      && FINDINGS+="password column in $f"$'\n'
  done < <(printf '%s\n' "${STAGED_ARR[@]}")

  if [[ -n "$FINDINGS" ]]; then
    echo; red "── SECRET SCAN FAILED ──"; printf '%s' "$FINDINGS"
    git reset >/dev/null
    die "staged changes were unstaged. Add the offending paths to .gitignore
       (or remove the secret), then re-run. To skip: SCAN_FOR_SECRETS=false in .env"
  fi
  grn "secret scan clean"
fi

$SCAN_ONLY && { git reset >/dev/null; grn "--scan-only: nothing committed"; exit 0; }

# ── 5. commit ─────────────────────────────────────────────────────
[[ -n "$MSG" ]] || MSG="$COMMIT_PREFIX: $(date '+%Y-%m-%d %H:%M')"
AUTHOR_ARGS=()
# NB: deliberately NOT named GIT_AUTHOR_* — those are git's own env vars, and
# exporting them empty from .env silently overrides your git config.
if [[ -n "${SYNC_AUTHOR_NAME:-}" && -n "${SYNC_AUTHOR_EMAIL:-}" ]]; then
  AUTHOR_ARGS=(--author="$SYNC_AUTHOR_NAME <$SYNC_AUTHOR_EMAIL>")
fi

if $DRY_RUN; then
  echo; ylw "--dry-run: would commit \"$MSG\" and push to $GIT_REMOTE/$GIT_BRANCH"
  git reset >/dev/null; exit 0
fi

git commit -q ${AUTHOR_ARGS[@]+"${AUTHOR_ARGS[@]}"} -m "$MSG"
grn "committed: $MSG"

# ── 6. push ───────────────────────────────────────────────────────
if [[ "$CONFIRM_BEFORE_PUSH" == "true" ]]; then
  echo; read -r -p "Push $COUNT file(s) to $GIT_REMOTE/$GIT_BRANCH? [y/N] " REPLY
  [[ "$REPLY" =~ ^[Yy]$ ]] || { ylw "push cancelled — commit kept locally, undo with: git reset --soft HEAD~1"; exit 0; }
fi

git push "$GIT_REMOTE" "HEAD:$GIT_BRANCH"
grn "pushed to $GIT_REMOTE/$GIT_BRANCH"
