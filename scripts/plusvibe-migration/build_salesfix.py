"""Build the SalesFix-signed campaign held back from build_batch2.py pending
brand confirmation. Eikko confirmed 2026-08-27: SalesFix is legitimate, keep
the branding untouched (no Starfix-style swap).

Depends on other24_full.json and verified_good_emails.json from the
build_batch2.py run (pull + dedupe + MillionVerifier already done there —
not repeated here).
"""
import hashlib, json, os, re

import build_batch2 as B

SCRATCH = os.path.dirname(__file__)
GROUP_SIG = "41be2f2e7c"
CAMP_NAME = "Sports & Fitness / Pet / Baby / Review2-DE (SalesFix) [MIGRATED]"


def sig(detail):
    seqs = detail.get("sequences") or [{}]
    steps = seqs[0].get("steps", [])
    bodies = []
    for s in steps:
        for v in s.get("variants", []):
            b = re.sub(r'<[^>]+>', '', v.get("body", ""))
            b = re.sub(r'\s+', ' ', b).strip()
            bodies.append(b[:120])
    return hashlib.md5("|".join(bodies).encode()).hexdigest()[:10]


def main():
    data = json.load(open(os.path.join(SCRATCH, "other24_full.json")))
    verified_good = set(json.load(open(os.path.join(SCRATCH, "verified_good_emails.json"))))

    sig_to_cnames = {}
    for cname, c in data.items():
        sig_to_cnames.setdefault(sig(c["detail"]), []).append(cname)

    members = sig_to_cnames[GROUP_SIG]
    detail = data[members[0]]["detail"]
    raw_leads = []
    for m in members:
        raw_leads.extend(data[m]["leads"])

    sequences = B.convert_sequences(detail, fix_brand=False)  # keep SalesFix as-is
    lead_rows = B.build_leads(raw_leads, verified_good)
    print(f"members: {members}")
    print(f"raw leads: {len(raw_leads)}  verified+usable: {len(lead_rows)}  steps: {len(sequences)}")

    full = json.dumps(sequences)
    assert "SalesFix" in full and "salesfix.ai" in full, "brand text should survive untouched"

    mailboxes = B.accounts()
    cid = os.environ.get("PV_CAMPAIGN_ID")
    if cid:
        print(f"reusing existing campaign shell: {cid}")
    else:
        cid = B.call("POST", "campaign/add/campaign", {"workspace_id": B.WS, "camp_name": CAMP_NAME})["id"]
        print(f"campaign created: {cid}")

    B.call("PATCH", "campaign/update/campaign", {
        "workspace_id": B.WS,
        "campaign_id": cid,
        "status": "PAUSED",
        "sequences": sequences,
        "email_accounts": mailboxes,
        "schedules": [{
            "daily_limit": 30,
            "daily_limit_new_lead": 30,
            "start_date": "2026-09-07",
            "end_date": "",
            "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
            "timezone": "America/New_York",
            "timing": {"from": "09:00", "to": "17:00"},
        }],
        "stop_on_lead_replied": "yes",
        "is_emailopened_tracking": "yes",
        "is_unsubscribed_link": "yes",
        "is_pause_on_bouncerate": "yes",
        "bounce_rate_limit": 4,
        "var_sel_type": "R_ROBIN",
    })
    print("settings applied")

    # PlusVibe caps lead/add at 500 per call.
    CHUNK = 500
    for i in range(0, len(lead_rows), CHUNK):
        chunk = lead_rows[i:i + CHUNK]
        added = B.call("POST", "lead/add", {
            "workspace_id": B.WS, "campaign_id": cid, "leads": chunk,
            "skip_if_in_workspace": True,
        })
        print(f"batch {i}-{i+len(chunk)}:", json.dumps(added))

    print(f"\nCAMPAIGN_ID={cid}")


if __name__ == "__main__":
    main()
