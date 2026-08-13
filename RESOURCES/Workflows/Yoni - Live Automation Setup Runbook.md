# Yoni — Live Automation Setup Runbook (Claude Code on the Web)

**Purpose:** Reference for any future session that puts a client-facing automation live via Claude Code on the web — not just SmartLead/Pipedrive. Consolidated from the Aug 12 setup session that connected Yoni's Claude account to SmartLead (custom REST client) and Pipedrive (MCP connector).

**Source material:** `livetoolsrunbook.md` + `yonifullreportlivetools.docx`, both delivered directly by the Claude Code on the web session (never committed to the repo — see the exposure note below for why that matters).

---

## 1. What was actually set up

- **Repo:** `salesmanager-crypto/smartlead-api-client` — https://github.com/salesmanager-crypto/smartlead-api-client (private/inaccessible via public fetch — access it directly via GitHub or the Claude Code on the web environment)
- **Branch:** `claude/campaigns-list-cli-g32fe4`
- **Environment:** "Smartlead+Pipedrive" (Claude Code on the web environment)
- **SmartLead:** custom dependency-free REST client (`src/client.js`) + CLI (`src/cli.js`), talking directly to `https://server.smartlead.ai/api/v1`
- **Pipedrive:** account-level MCP connector — no custom code, no credential file, authorized once at the claude.ai account level

Both are now live and working. The gap between how they got there is the actual lesson here.

---

## 2. The core lesson: MCP connector vs. custom client

| | SmartLead · custom client | Pipedrive · MCP connector |
|---|---|---|
| Setup effort | Manual — `.env` or environment variable, proxy config | None |
| Credential lives in | Session `.env`, or an environment-level env var | Managed by the connector, outside any repo |
| Survives a new chat? | Only if set at the **environment** level, not session `.env` | Always |
| Network path | Raw `fetch` — exposed to sandbox proxy quirks | MCP transport, already sandbox-aware |
| Problems hit | 5 separate blockers (see below) | Zero |

**Takeaway for next time:** if an MCP connector exists for the target service, use it first. A custom REST client is real engineering + credential-lifecycle overhead every single time.

---

## 3. ⚠️ Security flag — needs confirmation, not just documentation

During this setup, **a live SmartLead API key was pasted directly into the chat** instead of being placed straight into a file or the environment settings. The session wrote it to `.env` without echoing it back and flagged it as exposed, recommending rotation in the SmartLead dashboard — because chat transcripts can be logged/retained upstream regardless of what happens in the file system.

**This needs to be confirmed, not assumed:** check whether that key was actually rotated in SmartLead. If not, treat the current key as compromised and rotate it now. This is the single most important action item out of the whole setup — everything else in this doc is process improvement, this one is a live exposure.

**Standing rule for every future live-tool setup:** never paste a real secret into chat. Ask for it to go straight into a file or an environment-settings UI. If one does land in chat anyway, rotate it at the provider — moving it to a safer location afterward is not sufficient on its own.

---

## 4. Credential lifecycle — where things should live

```
Same session only    → repo-local .env (gitignored)
Every future session → environment variable on the Claude Code Environment
Any service, no key  → an authorized MCP connector, if one exists
```

Environment variables only apply to **containers created after** the variable is added — an already-running session won't see it retroactively, even though it looks identical. Verify any new environment variable from a fresh chat, not the one open when you set it.

---

## 5. The proxy gotcha (specific to Node `fetch` in this sandbox)

Node 22's built-in `fetch` doesn't route through the sandbox's required outbound proxy (`HTTPS_PROXY`) by default. A request with a perfectly valid key will fail with a generic `503`/"DNS resolution failure" that looks like a dead key or network — it's neither.

- **Fast fix:** run with `NODE_USE_ENV_PROXY=1` set.
- **Durable fix (not yet done):** wire an explicit `ProxyAgent` from `undici` into the client's `_request()` method when `HTTPS_PROXY`/`https_proxy` is present, so no one has to remember the env flag by hand.

**Diagnostic sequence before blaming the key or the API** (don't guess — check in this order):
```bash
getent hosts server.smartlead.ai
curl -sS -o /dev/null -w "%{http_code}\n" -x "$HTTPS_PROXY" \
  --cacert /root/.ccr/ca-bundle.crt https://server.smartlead.ai/api/v1/campaigns/
```
If `curl` through the proxy returns a real status code (even a 401), the network and DNS are fine — the problem is specific to the client code not using the proxy.

---

## 6. Known code gaps (SmartLead client — not yet fixed, none triggered a real failure)

- **No proxy awareness in `client.js`'s `_request()`** — the one gap that actually caused a failure (see Section 5). Confirmed root cause, not yet patched at the source.
- **No request timeout** — `fetch` has no `signal`/`AbortController`, so a hung SmartLead API call would hang the CLI indefinitely.
- **No argument validation in `cli.js`** — e.g. `campaigns:get` with no ID silently requests `/campaigns/undefined` instead of failing with a clear local error.
- **`leads:block` hardcodes `client_id: null`** — can't be scoped to a specific client from the CLI, only via direct use of `SmartleadClient` in code.

---

## 7. Checklist for the next live-tool setup

- [ ] Check for an existing MCP connector before building a custom client
- [ ] If a custom client is the only option, configure the credential at the **environment** level from day one — never treat a session `.env` as permanent
- [ ] Never paste a live secret into chat, under any circumstance
- [ ] If a secret does land in chat, rotate it at the provider immediately — don't just relocate it
- [ ] Confirm `.gitignore` covers the credential file before writing it, then verify with `git check-ignore -v` and `git status --short`
- [ ] In a proxied sandbox, don't trust a generic 5xx/DNS-looking error at face value — run the `getent hosts` + `curl` diagnostic first
- [ ] For Node `fetch` behind a proxy: set `NODE_USE_ENV_PROXY=1`, or better, bake a permanent `ProxyAgent` into the client so it isn't a flag someone has to remember
- [ ] After changing an environment's env vars, verify from a **new** session, not the one open when the change was made

---

## 8. Quick reference

**Verify a credential file is actually ignored**
```bash
git check-ignore -v .env
git status --short
```

**Run behind this sandbox's proxy**
```bash
NODE_USE_ENV_PROXY=1 node src/cli.js campaigns:list
```

---

---

## 9. Verified directly against the live repo (Aug 12, via GitHub connector)

Access was initially blocked (404 from the authorized account despite being added as a collaborator — root cause was the OAuth app needing separate org authorization, resolved by making the repo public). Once accessible, checked the actual repo against every claim in this doc:

**Confirmed accurate:**
- `.env` was never committed — not in the root listing, and `.gitignore` correctly lists `.env` first. README also explicitly warns "never paste your real key into a chat/AI tool — edit the file directly," which makes the earlier chat-paste incident more notable, not less.
- The proxy-awareness gap is still open. `src/client.js`'s `_request()` still calls the bare `fetch` global with no `ProxyAgent`/`dispatcher` and no `signal`/timeout — the "durable fix" from Section 5/6 has not been implemented yet.
- `leads:block` in `src/cli.js` still hardcodes `client_id: null` exactly as flagged — confirmed in the live code.
- **The SmartLead↔Pipedrive automation transfer actually happened and is more complete than expected.** `docs/Smartlead-Pipedrive-Automation-Workflow.md` in the repo is the workflow doc from this project, committed verbatim by Yoni's Claude session. On top of it, `scripts/scheduled-inbox-sync-prompt.md` is a full self-contained scheduled-task prompt that operationalizes it — category IDs, a `.last-checkpoint` file for incremental runs, CSV action logging (`logs/inbox-sync-log.csv`), and a weekly full-backlog-scan mode. This is real, running automation, not just documentation.

**Correction needed:**
- The branch this doc originally cited (`claude/campaigns-list-cli-g32fe4`) does not exist in the repo. Actual branches: `claude/smartlead-api-github-u4lz9v`, `claude/smartlead-pipedrive-setup-uejr6x`, `main`, `main-1y6og8`. Likely the original branch was merged/deleted, or the runbook was written against a different session than the one that ended up committing the automation.

**Still unverified — could not check from the repo:**
- Whether the exposed SmartLead API key was actually rotated. Repo inspection can only confirm `.env` itself was never committed — it can't confirm what happened to a key that was pasted into a chat and written to a gitignored file. GitHub secret scanning isn't available on this repo (Advanced Security isn't enabled), so this must be confirmed directly in the SmartLead dashboard, not by inspecting the code.

---

**Last Updated:** August 12, 2026
**Related:** `Smartlead-Pipedrive-Automation-Workflow.md` (the day-to-day categorization/sync process this infrastructure runs) — this file is about the underlying live connection setup, that one is about what runs on top of it.
