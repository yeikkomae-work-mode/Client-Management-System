"""Migrate the 964-lead 'Amazon Seller' campaign drafted on Instantly into PlusVibe.

Source: Instantly campaign id 981b5d19-ea6b-412d-8c98-c00880e35e0a — confirmed still
DRAFT (emails_sent_count: 0), so every lead here is genuinely untouched.

Creates the campaign PAUSED. Nothing sends until it is explicitly activated.
"""
import json, os, subprocess, sys, tempfile

from sequences_rating import build_sequences

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]

LEADS_PATH = os.path.join(os.path.dirname(__file__), "amazon_seller_leads_full.json")

CAMP_NAME = "Amazon Seller - Rating [MIGRATED FROM INSTANTLY DRAFT]"

# hellostarfix.com's 10 mailboxes are the only pool with nothing else assigned —
# the UK/USA Seller campaign already claims starfix.online + sellervate.net.
SENDING_DOMAINS = ("hellostarfix.com",)


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


def accounts():
    res = call("GET", f"account/list?workspace_id={WS}")
    picked = [a for a in res["accounts"]
              if a["email"].split("@")[1] in SENDING_DOMAINS]
    assert all(a["status"] == "ACTIVE" for a in picked), "inactive mailbox picked"
    return picked


def leads():
    raw = json.load(open(LEADS_PATH, encoding="utf-8"))
    out = []
    for r in raw:
        p = r.get("payload", {}) or {}
        out.append({
            "email": r["email"].strip().lower(),
            "first_name": r.get("first_name", "").strip(),
            "last_name": r.get("last_name", "").strip(),
            "company_name": r.get("company_name", "").strip(),
            "company_website": r.get("website", "").strip(),
            "linkedin_person_url": p.get("linkedIn", "").strip(),
            "linkedin_company_url": p.get("Company LinkedIn", "").strip(),
            "phone_number": p.get("Contact Number", "").strip(),
            "country": p.get("Country", "").strip(),
            "custom_variables": {
                # {{custom_rating}} in the copy maps to this key.
                "rating": p.get("Rating", "").strip().replace(",", "."),
                "amazon_url": p.get("Amazon URL", "").strip(),
                "job_title": p.get("jobTitle", "").strip(),
                "industry": p.get("Industry", "").strip(),
                "employees": p.get("Employees", "").strip(),
                "review_count": p.get("Review Count", "").strip(),
            },
        })
    return out


def main():
    accts = accounts()
    lead_rows = leads()
    print(f"mailboxes: {len(accts)} -> {', '.join(a['email'] for a in accts)}")
    print(f"leads: {len(lead_rows)}")
    assert all(l["custom_variables"]["rating"] for l in lead_rows), \
        "a lead is missing rating — {{custom_rating}} would render blank"
    assert len({l["email"] for l in lead_rows}) == len(lead_rows), "duplicate emails in source"

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
            "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
            "timezone": "America/New_York",     # 467 US / 314 UK / ~183 other EU — largest single bloc
            "timing": {"from": "09:00", "to": "17:00"},
        }],
        "stop_on_lead_replied": "yes",
        "is_emailopened_tracking": "yes",
        "is_unsubscribed_link": "yes",
        "is_pause_on_bouncerate": "yes",
        "bounce_rate_limit": 4,
        "var_sel_type": "R_ROBIN",
    })
    print("settings + sequences applied")

    # Upload in batches — 964 leads is well within a single call, but chunk defensively.
    CHUNK = 500
    for i in range(0, len(lead_rows), CHUNK):
        chunk = lead_rows[i:i + CHUNK]
        added = call("POST", "lead/add", {
            "workspace_id": WS,
            "campaign_id": cid,
            "leads": chunk,
            "skip_if_in_workspace": True,
        })
        print(f"batch {i}-{i+len(chunk)}:", json.dumps(added)[:300])

    print(f"\nCAMPAIGN_ID={cid}")


if __name__ == "__main__":
    main()
