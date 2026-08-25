"""Migrate the drafted 'UK/USA Amazon Seller' campaign (Cüneyt / Starfix) into PlusVibe.

Creates the campaign PAUSED. Nothing sends until it is explicitly activated.
"""
import csv, json, os, subprocess, sys, tempfile

from sequences import build_sequences

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]

CSV_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
            "Cüneyt - Cleaned Lead Lists (2026-08-21)/3_UK_USA_Amazon_Seller_CLEANED.csv")
DUP_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
            "Cüneyt - Cleaned Lead Lists (2026-08-21)/cross_file_duplicate_emails.csv")

CAMP_NAME = "Amazon Seller UK/USA [MIGRATED]"

# sellervate.net + starfix.online — same pairing the previous Amazon Seller
# campaign used in Instantly (per the client profile).
SENDING_DOMAINS = ("sellervate.net", "starfix.online")


def call(method, path, body=None):
    """PlusVibe sits behind Cloudflare, which rejects urllib's UA — shell out to curl."""
    cmd = ["curl", "-sS", "-X", method, f"{API}/{path}",
           "-H", f"x-api-key: {KEY}", "-H", "Content-Type: application/json",
           "-w", "\n%{http_code}"]
    tmp = None
    if body is not None:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(body, tmp)
        tmp.close()
        cmd += ["-d", f"@{tmp.name}"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    payload, _, code = out.rpartition("\n")
    if code.strip() != "200":
        sys.exit(f"HTTP {code.strip()} on {method} {path}\n{payload}")
    return json.loads(payload or "{}")


def accounts():
    res = call("GET", f"account/list?workspace_id={WS}")
    picked = [a for a in res["accounts"]
              if a["email"].split("@")[1] in SENDING_DOMAINS]
    assert all(a["status"] == "ACTIVE" for a in picked), "inactive mailbox picked"
    return picked


def leads():
    dupes = {r["Email"].strip().lower() for r in csv.DictReader(open(DUP_PATH, encoding="utf-8-sig"))}
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    out, skipped = [], []
    for r in rows:
        email = r["Email"].strip().lower()
        if email in dupes:                      # already live in the MAIN List campaign
            skipped.append(email)
            continue
        out.append({
            "email": email,
            "first_name": r["First Name"].strip(),
            "last_name": r["Last Name"].strip(),
            "company_name": r["Company Name"].strip(),
            "company_website": r["Website"].strip(),
            "linkedin_person_url": r["Person Linkedin"].strip(),
            "linkedin_company_url": r["Company Linkedin URL"].strip(),
            "phone_number": r["Contact Number"].strip(),
            "country": r["Country"].strip(),
            "custom_variables": {
                # {{product_category}} in the copy maps to this key.
                "product_category": r["Product Type"].strip(),
                "amazon_url": r["Amazon"].strip(),
                "job_title": r["Title"].strip(),
                "revenue": r["Revenue"].strip(),
                "industry": r["Industry"].strip(),
            },
        })
    return out, skipped


def main():
    accts = accounts()
    lead_rows, skipped = leads()
    print(f"mailboxes: {len(accts)} -> {', '.join(a['email'] for a in accts)}")
    print(f"leads: {len(lead_rows)} (skipped {len(skipped)} cross-file dupes: {skipped})")
    assert all(l["custom_variables"]["product_category"] for l in lead_rows), \
        "a lead is missing product_category — {{product_category}} would render blank"

    cid = os.environ.get("PV_CAMPAIGN_ID")
    if cid:
        print(f"reusing existing campaign shell: {cid}")
    else:
        cid = call("POST", "campaign/add/campaign",
                   {"workspace_id": WS, "camp_name": CAMP_NAME})["id"]
        print(f"campaign created: {cid}")

    call("PATCH", "campaign/update/campaign", {
        "workspace_id": WS,
        "campaign_id": cid,
        "status": "PAUSED",                     # nothing sends until explicitly activated
        "sequences": build_sequences(),
        "email_accounts": [a["id"] for a in accts],
        "schedules": [{
            "daily_limit": 30,                  # account-wide convention post-DKIM fix
            "daily_limit_new_lead": 30,
            "start_date": "2026-09-07",         # 14 days after warmup began (Aug 24)
            "end_date": "",
            # Only enabled days may appear as keys (1=Mon..7=Sun); a key set
            # to false is rejected outright. Mon-Fri here.
            "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
            "timezone": "America/New_York",     # 63 US / 45 UK / 1 CA — 9am ET is in-hours for both
            "timing": {"from": "09:00", "to": "17:00"},
        }],
        "stop_on_lead_replied": "yes",
        "is_emailopened_tracking": "yes",       # audit rec #1 — fleet-wide open-tracking blind spot
        "is_unsubscribed_link": "yes",
        "is_pause_on_bouncerate": "yes",
        "bounce_rate_limit": 4,
        "var_sel_type": "R_ROBIN",
    })
    print("settings + sequences applied")

    added = call("POST", "lead/add", {
        "workspace_id": WS,
        "campaign_id": cid,
        "leads": lead_rows,
        "skip_if_in_workspace": True,
    })
    print("leads added:", json.dumps(added)[:400])
    print(f"\nCAMPAIGN_ID={cid}")


if __name__ == "__main__":
    main()
