# Access & Identity Register

**Owner:** `cio` · **Created:** 2026-08-25 · **One row per credential, not per tool.**

This is the source of truth for **access** — who can get into what, with which scope, verified when. It is not a tool inventory and it carries no cost or renewal information (`cfo`), and no keep/kill verdict on any tool.

**No secret values appear in this file, ever.** Credentials are identified by filename, variable name, scope, and date. `client_id` values are not secrets and may appear. `client_secret`, `token`, `refresh_token`, and passwords may not. If you are about to paste a value in here, stop — the correct entry is a reference.

---

## ⚠️ Read this before trusting any row below

This register was seeded on **2026-08-25 from a fresh clone of the repository in a remote container.** Every credential file in this system is gitignored — `**/OAuth Credentials/*`, `**/*token*.json`, `**/*credentials*.json`, `.env`, `tools_api_details.md`, `Premium Inboxes.csv` — and therefore **none of them were present to read.**

The specified seeding method — cross-match every `*client_secret*.json` against every `*_token.json` by `client_id`, read each token's `scopes` and `expiry` — **could not be executed.** Rows below marked `⛔ unverified` are unverified for that reason, not because verification was skipped. Each names the command that would settle it, to be run **on Eikko's machine**, where the files actually live.

Rows marked `✅ verified` were confirmed by a command run in this container on 2026-08-25; the command is recorded in the row.

Filling in the `⛔` rows is the register's first real job.

---

## Google / Gmail accounts

Six known inboxes. Scope claims below come from `google_accounts_details.md` and `_shared/connector-status.md` — **both documents, not from the token files** — and are therefore unverified until a token is read.

| Credential | Account / email | Client served | Where it lives | Scopes (claimed) | Can / cannot | Last verified | Owner | Notes |
|---|---|---|---|---|---|---|---|---|
| Native claude.ai Gmail connector | `yeikkomae@gmail.com` | General — Upwork, Onlinejobs, Wise, Krishna, Chris Soriano | claude.ai connector (no local file) | Gmail + Calendar + Drive | Read, and whatever the connector grants | ⛔ unverified | Eikko | The **one** native Gmail slot; claude.ai permits only one account. All other inboxes must use the custom OAuth script. |
| `personal_token.json` | `eikkomaeybanez@gmail.com` | Personal (e.g. Mariette) | `OAuth Credentials/` *(gitignored — absent here)* | `gmail.readonly` + `gmail.compose` | Read + draft. **No `gmail.send`** | ⛔ unverified | Eikko | Paired client_secret documented as `Personal_eikkomaeybanez_client_secret_1080807478962-…json`, project `boxwood-sandbox-505400-q3`. Desktop-app OAuth type. |
| `satlas_token.json` | `eikko@satlas.com.au` | Chris Drew / Satlas, Capital Financing | `OAuth Credentials/` *(gitignored — absent here)* | `gmail.readonly` + `gmail.compose` | Read + draft. **No `gmail.send`** | ⛔ unverified | Client-domain account, Eikko's seat | Account also carries connected apps: Zapmail, InboxKit, PlusVibe. |
| `albertscott_token.json` | `salesmanager@albertscott.com` | Yoni / Albert Scott | `OAuth Credentials/` *(gitignored — absent here)* | `gmail.readonly` + `gmail.compose` | Read + draft. **No `gmail.send`** | ⛔ unverified | Client-domain account, Eikko's seat | ⚠️ **Spelling unconfirmed with Eikko.** Also the one OAuth client registered as *Web application* type (others are *Desktop app*), needing an exact `http://localhost:8080/callback` redirect. |
| `fractio_token.json` | `eikko.ybanez@fractio.co` | Chris Caffera / Fractio | `OAuth Credentials/` *(gitignored — absent here)* | `gmail.readonly` + `gmail.compose` | Read + draft. **No `gmail.send`** | ⛔ unverified | Client-domain account, Eikko's seat | |
| *(none)* | `eikko.ybanez@mycloudgcs.com` | MyCloudGCS | — | — | **No access at all** | n/a — never connected | Client-domain account | Outlook, not Gmail. No account key exists. Has a remote branch `MyCloudGCS` — ✅ verified 2026-08-25 via `git ls-remote --heads origin`. |
| *(none)* | Penji inbox #1 | Penji | — | — | **No access at all** | n/a — never connected | Client-owned | ⛔ The two Penji inboxes are described in the build request but **no Penji email address appears anywhere in this repo** — searched `CLIENT PROFILES/`, `.claude/`, `OUTPUT/`. Addresses need supplying by Eikko. |
| *(none)* | Penji inbox #2 | Penji | — | — | **No access at all** | n/a — never connected | Client-owned | Same. Native Gmail connector is already spent on `yeikkomae@gmail.com`, so both Penji inboxes would need the custom OAuth script — a new `client_secret` per account. |

**Verifying command** (run on Eikko's machine, in `RESOURCES/Tools & API Details/OAuth Credentials/`):

```bash
# Scopes + expiry per token — prints field names and values for scopes/expiry ONLY.
for f in *_token.json; do
  echo "== $f"
  python3 -c "import json,sys; d=json.load(open('$f')); print('  scopes:', d.get('scopes')); print('  expiry:', d.get('expiry')); print('  refresh_token present:', bool(d.get('refresh_token')))"
done

# Orphan check — client_secret files matched by no token, by client_id.
python3 - <<'PY'
import json, glob, os
secrets = {}
for f in glob.glob('*client_secret*.json'):
    d = json.load(open(f)); k = (d.get('installed') or d.get('web') or {})
    secrets[k.get('client_id')] = f
used = set()
for f in glob.glob('*_token.json'):
    used.add(json.load(open(f)).get('client_id'))
for cid, f in secrets.items():
    print(('ORPHAN  ' if cid not in used else 'in use  ') + f)
PY
```

Neither command prints a secret value.

### Orphan credential — reported, not confirmed

`google_accounts_details.md` records a second personal `client_secret` file — `Personal_client_secret_2_…json`, project `hermes-personal-access-504417` — as unused, superseded, and "flagged for Eikko to confirm it's safe to delete" as of 2026-08-13.

**Status: ⛔ unverified, and unresolvable from here.** The file is gitignored and absent from this clone; whether it still exists, and whether any token references its `client_id`, needs the orphan-check command above. **Nothing has been deleted, and `cio` will not delete it** — deletion is Eikko's, always.

### The 12-day gap

`inbox-triage.md` states all five Gmail inboxes were live "as of 2026-08-13." `_shared/connector-status.md` carries `Last verified: 2026-08-24`, but that date is sourced in the file itself to "Zapmail / InboxKit / Porkbun rows updated from the 2026-08-22 Satlas infra audit" — **the Gmail rows carry no verification date of their own.**

So the most recent evidence of any of these four OAuth inboxes actually being read is **2026-08-13 — 12 days before this register was created.** Whether the tokens have refreshed themselves since is `⛔ unverified`; it depends on refresh tokens being present, which is exactly what the command above checks.

---

## Raw API keys — by variable name only

| Variable name | Tool | Client served | Variable found? | Last verified | Notes |
|---|---|---|---|---|---|
| `GOOGLE_VA_CLIENT_ID` / `GOOGLE_VA_CLIENT_SECRET` | Google OAuth | General | ❌ **NOT FOUND** | ✅ verified 2026-08-25 | See documentation failure below. |
| `GOOGLE_SATLAS_CLIENT_ID` / `_SECRET` | Google OAuth | Satlas | ❌ **NOT FOUND** | ✅ verified 2026-08-25 | Same. |
| `GOOGLE_FRACTIO_CLIENT_ID` / `_SECRET` | Google OAuth | Fractio | ❌ **NOT FOUND** | ✅ verified 2026-08-25 | Same. |
| `GOOGLE_ALBERTSCOTT_CLIENT_ID` / `_SECRET` | Google OAuth | Albert Scott | ❌ **NOT FOUND** | ✅ verified 2026-08-25 | Same. |
| `APOLLO_API_KEY` | Apollo | Satlas / Chris Drew | ⛔ unverified | ⛔ — doc claims 2026-08-13 vs `/v1/auth/health` | Lives in gitignored `tools_api_details.md`, absent here. |
| `APOLLO_API_KEY_ACCOUNT2` | Apollo | Krishna | ⛔ unverified | ⛔ — doc claims 2026-08-13 | Same. |
| `SATLAS_PLUSVIBE_API_KEY` | PlusVibe | Satlas | ⛔ unverified | ⛔ — doc claims 2026-08-22 | Same. Paired `workspace_id` is documented, not a secret. |
| `STARFIX_INSTANTLY_API_KEY` | Instantly | Cüneyt / Starfix | ⛔ unverified | ⛔ — never tested against API per `connector-status.md` | Separate account from Satlas's. |
| `STARFIX_PLUSVIBE_API_KEY` *(name proposed — variable does not exist)* | PlusVibe | Cüneyt / Starfix | ⛔ unverified | ⛔ — never tested against API | 🔴 **Client-supplied in chat, 2026-08-24** — by-reference row only, no value in this repo. Paired workspace "Cüneyt's Workspace", id `6a8c1c4f92e45be273aa9201` (not a secret), 19 mailboxes connected + warming. Source: `CLIENT PROFILES/Cüneyt - Profile (Starfix).md`. **Eikko places the value.** |
| `STARFIX_HOSTINGER_API_KEY_HELLOSTARFIX` | Hostinger | Cüneyt / Starfix | ⛔ unverified | ⛔ — never tested against API | Domain-scoped. |
| `STARFIX_HOSTINGER_API_KEY_STARFIXONLINE` | Hostinger | Cüneyt / Starfix | ⛔ unverified | ⛔ — never tested against API | Domain-scoped; scope not confirmed per client profile. |
| `STARFIX_HOSTINGER_API_KEY_SELLERVATE` | Hostinger | Cüneyt / Starfix | ⛔ unverified | ⛔ — never tested against API | Domain-scoped; scope not confirmed per client profile. |

**Verifying command:** `grep -oE '^[A-Za-z_][A-Za-z0-9_]*' .env | sort` — prints variable names only, no values.

### 🟡 Register gap — Starfix PlusVibe ran unregistered

**✅ verified 2026-08-25** against `CLIENT PROFILES/Cüneyt - Profile (Starfix).md`: a PlusVibe API key was **"provided directly in chat"** on **2026-08-24** and used to connect 19 mailboxes to workspace `6a8c1c4f92e45be273aa9201`.

That is a live client credential that has never had a register row, and it arrived through exactly the channel the redaction protocol exists for. It is the second Starfix credential known to have come in over chat — the Hostinger keys of 2026-08-13 were the first.

**Proposed — not executed, `cio` places nothing:**
1. Eikko places the value in the gitignored surface he already uses for `STARFIX_*` keys, under a variable name matching the convention above.
2. Ask Cüneyt to delete the key from the chat thread once placed. Plaintext in a chat app on two devices with no expiry is the actual exposure; a register row does nothing to reduce it.
3. Record the placement date in `Last verified` once a live call against the PlusVibe API answers.

### 🔴 Documentation failure — `GOOGLE_*` variables do not exist

`google_accounts_details.md` documents eight `GOOGLE_*_CLIENT_ID` / `GOOGLE_*_CLIENT_SECRET` variables across five accounts, each marked **"Status: Configured ✓"**.

```
$ grep -cE '^GOOGLE_' .env
0
```

**✅ Verified 2026-08-25: zero.** The repository `.env` contains nine variables, all git-sync configuration — `COMMIT_PREFIX`, `CONFIRM_BEFORE_PUSH`, `GIT_BRANCH`, `GIT_REMOTE`, `GIT_REMOTE_URL`, `REQUIRE_PRIVATE_REPO`, `SCAN_FOR_SECRETS`, `SYNC_AUTHOR_EMAIL`, `SYNC_AUTHOR_NAME`. No Google variables, no API keys of any kind.

Those five "Configured ✓" rows describe an environment that does not exist. The custom OAuth script does not read those variables either — it uses `client_secret` JSON files. **This is the second time this document has been found wrong** (the first being its own note that section 6 supersedes its OAuth-flow instructions). See the proposed resolution in `OUTPUT/Security & Access Reviews/2026-08-25.md`.

---

## Plaintext-credential surfaces — location only

Recorded so they are known and watched. **Contents are never reproduced here.** All are gitignored; all are absent from this clone, which is why each is `⛔ unverified`.

| Surface | What it holds | Gitignored? | Present in this clone? |
|---|---|---|---|
| `RESOURCES/Tools & API Details/tools_api_details.md` | Live API keys written out in plaintext, per `.gitignore`'s own comment | ✅ verified 2026-08-25 | ❌ no — ⛔ existence on Eikko's machine unverified |
| `RESOURCES/Tools & API Details/Albertscott Domains and Emails/Premium Inboxes.csv` | 50 rows of mailbox + plaintext password, per `.gitignore`'s own comment | ✅ verified 2026-08-25 | ❌ no. Sibling files *are* present (`GoDaddy.csv`, `Microsoft Office 365.csv`, `Albert Scott Cold Email Project.xlsx`) — ⛔ **these three are tracked and unexamined; whether they carry credentials is unverified** |
| `ARCHIVE - Inactive Automations/smartlead-pipedrive-automation/` | Nested repo with its own `.git` and live `.env` (Smartlead / Pipedrive / Gmail keys) | ✅ verified 2026-08-25 | ❌ no |
| `PROJECTS/Active/smartlead-pipedrive-automation/` | Former location of the above | ✅ verified 2026-08-25 | ❌ no |

⚠️ The three sibling files in `Albertscott Domains and Emails/` are **tracked in git** and were not opened. `Premium Inboxes.csv` was excluded by name; these were not. Whether they contain mailbox passwords is an open question — see the review report.

---

## Git posture — ✅ verified 2026-08-25

```
$ git ls-files | grep -iE '\.env$|token.*\.json|client_secret|credential|\.pem$|\.key$'
(zero rows)

$ git ls-files --error-unmatch .env
error: pathspec '.env' did not match any file(s) known to git
```

**No secret-bearing file is tracked in this repository.** `.gitignore` covers `.env`, `*.env`, `**/OAuth Credentials/*`, `**/*credentials*.json`, `**/*token*.json`, `tools_api_details.md`, `Premium Inboxes.csv`, and both locations of the nested automation repo.

## Repository visibility — ✅ verified 2026-08-25, **private**

The build request listed this as an unverified blocker. It is verifiable, and it was verified:

```
GitHub API → repos/yeikkomae-work-mode/Client-Management-System
  "private": true
  "visibility": "private"
  "forks_count": 0
  "owner": "yeikkomae-work-mode"
```

**This is not a blocker.** The repo is private with no forks, so `OUTPUT/Conversations/` may hold real client threads. Two caveats that keep it worth re-checking: collaborator list was not enumerated, and the six per-client branches (`Albertscott`, `MyCloudGCS`, `Penji`, `Satlas`, `Starfix`) are ⛔ unverified as to who, if anyone, has been given access to them.

---

## Maintenance

Re-verify any row older than **30 days** — the `cio` session opener checks exactly this. A row whose last-verified cell is a claim copied from another document is not verified; put `⛔ unverified` in it and name the command instead.
