"""Split campaign 1 (Amazon Seller UK/USA) and campaign 2 (Amazon Seller - Rating)
into separate US-leg and UK-leg campaigns so each can run on its own timezone —
PlusVibe rejects more than one schedule block per campaign, so a single-campaign
dual-timezone setup isn't possible; splitting is the only way to actually match
send time to each lead's region (per Eikko's 2026-08-28 instruction, confirmed
via AskUserQuestion after hitting the schedules-array limit).

Both legs launch ACTIVE, daily_limit=6 (ramp start, +1/day handled by a separate
daily routine), same mailbox pool the original campaign already used.
"""
import csv, json, os, subprocess, sys, tempfile

sys.path.insert(0, os.path.dirname(__file__))
API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
SCRATCH = os.path.dirname(__file__)
TODAY = "2026-08-28"


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


def schedule(tz, daily_limit=6):
    return [{
        "daily_limit": daily_limit,
        "daily_limit_new_lead": daily_limit,
        "start_date": TODAY,
        "end_date": "",
        "days": {"1": True, "2": True, "3": True, "4": True, "5": True},
        "timezone": tz,
        "timing": {"from": "09:00", "to": "17:00"},
    }]


def launch_leg(existing_cid, new_camp_name, uk_leads, us_leads, mailbox_ids, sequences,
               existing_camp_name, existing_leg_done=False, uk_cid=None):
    CHUNK = 500
    if not existing_leg_done:
        # Rename the existing campaign to make clear it's now the US(+other) leg.
        call("PATCH", "campaign/update/campaign", {
            "workspace_id": WS, "campaign_id": existing_cid, "camp_name": existing_camp_name,
        })

        # Remove UK leads from the existing (now US-leg) campaign.
        uk_emails = [l["email"] for l in uk_leads]
        for i in range(0, len(uk_emails), CHUNK):
            res = call("POST", "lead/delete", {
                "workspace_id": WS, "campaign_id": existing_cid,
                "delete_list": uk_emails[i:i + CHUNK],
            })
            print(f"  deleted UK leads from US-leg batch {i}-{i+len(uk_emails[i:i+CHUNK])}: {json.dumps(res)[:150]}")

        # Set US-leg schedule + activate.
        call("PATCH", "campaign/update/campaign", {
            "workspace_id": WS, "campaign_id": existing_cid,
            "status": "ACTIVE",
            "schedules": schedule("America/New_York"),
        })
        print(f"  US-leg ({existing_cid}) renamed, {len(uk_emails)} UK leads removed, ACTIVE at 6/day America/New_York")

    # Create (or reuse) the UK-leg campaign shell.
    if not uk_cid:
        uk_cid = call("POST", "campaign/add/campaign", {"workspace_id": WS, "camp_name": new_camp_name})["id"]

    # Settings + sequences + mailboxes + schedule first, while still PAUSED —
    # PlusVibe rejects status=ACTIVE in the same call that first attaches
    # email_accounts ("Email account must be added before you can start the
    # campaign"), so activation has to be a separate, later PATCH.
    call("PATCH", "campaign/update/campaign", {
        "workspace_id": WS, "campaign_id": uk_cid,
        "status": "PAUSED",
        "sequences": sequences,
        "email_accounts": mailbox_ids,
        "schedules": schedule("Europe/London"),
        "stop_on_lead_replied": "yes",
        "is_emailopened_tracking": "yes",
        "is_unsubscribed_link": "yes",
        "is_pause_on_bouncerate": "yes",
        "bounce_rate_limit": 4,
        "var_sel_type": "R_ROBIN",
    })
    for i in range(0, len(uk_leads), CHUNK):
        chunk = uk_leads[i:i + CHUNK]
        added = call("POST", "lead/add", {
            "workspace_id": WS, "campaign_id": uk_cid, "leads": chunk,
            "skip_if_in_workspace": True,
        })
        print(f"  UK-leg batch {i}-{i+len(chunk)}: {json.dumps(added)[:200]}")

    call("PATCH", "campaign/update/campaign", {
        "workspace_id": WS, "campaign_id": uk_cid, "status": "ACTIVE",
    })
    print(f"  UK-leg ({uk_cid}) created, {len(uk_leads)} leads, ACTIVE at 6/day Europe/London")
    return uk_cid


def main():
    # --- Campaign 1: Amazon Seller UK/USA ---
    CSV_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
                "Cüneyt - Cleaned Lead Lists (2026-08-21)/3_UK_USA_Amazon_Seller_CLEANED.csv")
    DUP_PATH = ("/home/user/Client-Management-System/OUTPUT/Campaign Tracking/"
                "Cüneyt - Cleaned Lead Lists (2026-08-21)/cross_file_duplicate_emails.csv")
    dupes = {r["Email"].strip().lower() for r in csv.DictReader(open(DUP_PATH, encoding="utf-8-sig"))}
    rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")))
    c1_leads = []
    for r in rows:
        email = r["Email"].strip().lower()
        if email in dupes:
            continue
        c1_leads.append({
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
                "product_category": r["Product Type"].strip(),
                "amazon_url": r["Amazon"].strip(),
                "job_title": r["Title"].strip(),
                "revenue": r["Revenue"].strip(),
                "industry": r["Industry"].strip(),
            },
        })
    c1_uk = [l for l in c1_leads if l["country"] == "United Kingdom"]
    c1_us = [l for l in c1_leads if l["country"] != "United Kingdom"]
    print(f"Campaign 1: {len(c1_leads)} total -> {len(c1_us)} US/other, {len(c1_uk)} UK")

    import sequences as S1
    res = call("GET", f"account/list?workspace_id={WS}")
    c1_mailboxes = [a["id"] for a in res["accounts"]
                    if a["email"].split("@")[1] in ("sellervate.net", "starfix.online")]

    uk_cid_1 = launch_leg(
        existing_cid="6a8cf6f27e5c6119d8830749",
        new_camp_name="Amazon Seller UK [MIGRATED]",
        uk_leads=c1_uk, us_leads=c1_us,
        mailbox_ids=c1_mailboxes,
        sequences=S1.build_sequences(),
        existing_camp_name="Amazon Seller US/CA [MIGRATED]",
        existing_leg_done=True, uk_cid="6a90b3bcf68baa1111ed5c7f",
    )

    # --- Campaign 2: Amazon Seller - Rating ---
    raw964 = json.load(open(os.path.join(SCRATCH, "amazon_seller_leads_full.json"), encoding="utf-8"))
    c2_leads = []
    seen = set()
    for r in raw964:
        p = r.get("payload", {}) or {}
        email = r["email"].strip().lower()
        seen.add(email)
        c2_leads.append({
            "email": email,
            "first_name": r.get("first_name", "").strip(),
            "last_name": r.get("last_name", "").strip(),
            "company_name": r.get("company_name", "").strip(),
            "company_website": r.get("website", "").strip(),
            "linkedin_person_url": p.get("linkedIn", "").strip(),
            "linkedin_company_url": p.get("Company LinkedIn", "").strip(),
            "phone_number": p.get("Contact Number", "").strip(),
            "country": p.get("Country", "").strip(),
            "custom_variables": {
                "rating": p.get("Rating", "").strip().replace(",", "."),
                "amazon_url": p.get("Amazon URL", "").strip(),
                "job_title": p.get("jobTitle", "").strip(),
                "industry": p.get("Industry", "").strip(),
                "employees": p.get("Employees", "").strip(),
                "review_count": p.get("Review Count", "").strip(),
            },
        })
    raw363 = json.load(open(os.path.join(SCRATCH, "leftover_rating_leads.json"), encoding="utf-8"))
    for r in raw363:
        email = r["email"].strip().lower()
        if email in seen:
            continue
        seen.add(email)
        c2_leads.append({
            "email": email,
            "first_name": r["first_name"], "last_name": r["last_name"],
            "company_name": r["company_name"], "company_website": r["company_website"],
            "linkedin_person_url": r["linkedin_person_url"], "linkedin_company_url": r["linkedin_company_url"],
            "phone_number": r["phone_number"], "country": r["country"],
            "custom_variables": {
                "rating": r["rating"], "amazon_url": r["amazon_url"], "job_title": r["job_title"],
                "industry": r["industry"], "employees": r["employees"], "review_count": r["review_count"],
            },
        })
    c2_uk = [l for l in c2_leads if l["country"] == "United Kingdom"]
    c2_us = [l for l in c2_leads if l["country"] != "United Kingdom"]
    print(f"Campaign 2: {len(c2_leads)} total -> {len(c2_us)} US/other, {len(c2_uk)} UK")

    import sequences_rating as S2
    c2_mailboxes = [a["id"] for a in res["accounts"] if a["email"].split("@")[1] == "hellostarfix.com"]

    uk_cid_2 = launch_leg(
        existing_cid="6a8ee087c3903d2a71741b72",
        new_camp_name="Amazon Seller - Rating UK [MIGRATED FROM INSTANTLY DRAFT]",
        uk_leads=c2_uk, us_leads=c2_us,
        mailbox_ids=c2_mailboxes,
        sequences=S2.build_sequences(),
        existing_camp_name="Amazon Seller - Rating US [MIGRATED FROM INSTANTLY DRAFT]",
    )

    print(f"\nNew UK campaigns: {uk_cid_1}, {uk_cid_2}")


if __name__ == "__main__":
    main()
