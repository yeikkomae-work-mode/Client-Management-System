"""Set the sender signature on every PlusVibe inbox in Cüneyt's workspace.

18 of 19 inboxes had no signature at all; the one that did misspelled the brand
as "SellerVeta". This writes a consistent SellerVate sign-off across all of them,
following the house format already in use.

Dry-run by default. Pass --apply to actually write.
"""
import json, os, subprocess, sys, tempfile

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]

BRAND = "SellerVate"
SITE = "sellervate.de"

# Role mailboxes — their stored first_name is the local part ("Audits", "Hello"),
# which would sign a cold email "Best, Audits". They get a team sign-off instead.
ROLE_BOXES = {"audits", "hello"}


def call(method, path, body=None):
    cmd = ["curl", "-sS", "-X", method, f"{API}/{path}",
           "-H", f"x-api-key: {KEY}", "-H", "Content-Type: application/json",
           "-w", "\n%{http_code}"]
    if body is not None:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(body, tmp); tmp.close()
        cmd += ["-d", f"@{tmp.name}"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    payload, _, code = out.rpartition("\n")
    if code.strip() != "200":
        sys.exit(f"HTTP {code.strip()} on {method} {path}\n{payload}")
    return json.loads(payload or "{}")


def signature_for(email, first_name):
    """House format, matching the one signature already on the account."""
    local = email.split("@")[0].lower()
    if local in ROLE_BOXES:
        return f"<div>Best,<br><br>The {BRAND} Team<br>{SITE}</div>"
    return f"<div>Best,<br><br>{first_name}<br>{BRAND} | {SITE}</div>"


def main():
    apply = "--apply" in sys.argv
    accts = call("GET", f"account/list?workspace_id={WS}")["accounts"]

    plan = []
    for a in accts:
        first = (a.get("payload", {}).get("name", {}).get("first_name") or "").strip()
        current = (a.get("payload", {}).get("signature") or "").strip()
        plan.append((a["id"], a["email"], current, signature_for(a["email"], first)))

    for _, email, current, new in plan:
        print(f"{email}")
        print(f"   before: {current or '(empty)'}")
        print(f"   after:  {new}")
    print(f"\n{len(plan)} inboxes")

    if not apply:
        print("\nDRY RUN — pass --apply to write.")
        return

    for acct_id, email, _, new in plan:
        call("PUT", "account/bulk-update",
             {"workspace_id": WS, "ids": [acct_id], "signature": new})
        print(f"set: {email}")


if __name__ == "__main__":
    main()
