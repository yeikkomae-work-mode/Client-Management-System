"""Send one test email per PlusVibe campaign (11 total) to
cueneyt.nurdogan@sellervate.de, rendering each campaign's actual Step-1
Variant-A copy (spintax resolved to its first branch, merge vars filled
with clearly-marked test placeholders). Read-only against Instantly data
already pulled this project; only unibox/emails/send is a live write.
"""
import json, os, re, subprocess, sys, tempfile

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
TO = "cueneyt.nurdogan@sellervate.de"
SCRATCH = os.path.dirname(__file__)

PLACEHOLDERS = {
    "first_name": "there",
    "company_name": "Example Amazon Co",
    "custom_product_category": "kitchen accessories",
    "custom_rating": "3.8",
    "custom_website": "example-store.com",
    "custom_job_title": "Store Manager",
    "custom_linkedin": "",
    "custom_location": "",
    "custom_phone": "",
    "custom_personalization": "",
    "sender_signature": "Best,<br>{{FROM_NAME}}",
}


def resolve_spintax(text):
    def pick(m):
        opts = m.group(1).split("|")
        return opts[0].strip()
    while "{{RANDOM" in text:
        text = re.sub(r"\{\{RANDOM\s*\|([^{}]*)\}\}", pick, text, count=1)
    return text


def fill_vars(text, from_name):
    for k, v in PLACEHOLDERS.items():
        text = text.replace("{{%s}}" % k, v)
    text = text.replace("{{FROM_NAME}}", from_name)
    return text


def render(subject, body_lines_or_html, from_name, is_html=False):
    subject = fill_vars(resolve_spintax(subject), from_name)
    if is_html:
        body = fill_vars(body_lines_or_html, from_name)
    else:
        body = "".join(f"<p>{fill_vars(resolve_spintax(l), from_name)}</p>" for l in body_lines_or_html)
    banner = "<p style='color:#888;font-size:12px'>[TEST SEND — rendered with placeholder lead data, spintax resolved to variant 1]</p>"
    return subject, banner + body


def call(method, path, body=None, query=""):
    url = f"{API}/{path}"
    if query:
        url += f"?{query}"
    cmd = ["curl", "-sS", "-X", method, url,
           "-H", f"x-api-key: {KEY}", "-H", "Content-Type: application/json",
           "-w", "\n%{http_code}"]
    if body is not None:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        json.dump(body, tmp); tmp.close()
        cmd += ["-d", f"@{tmp.name}"]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    payload, _, code = out.rpartition("\n")
    return code.strip(), payload


def send(campaign_label, from_email, subject, body_html):
    code, payload = call("POST", "unibox/emails/send", {
        "subject": f"[TEST] {subject}",
        "from": from_email,
        "to": TO,
        "body": body_html,
    }, query=f"workspace_id={WS}")
    ok = code == "200"
    print(f"{'OK ' if ok else 'FAIL'} {campaign_label:55s} from={from_email:30s} http={code} {payload[:150] if not ok else ''}")
    return ok


def sig(detail):
    import hashlib
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
    mailboxes = [
        "kevin@hellostarfix.com", "ryan@hellostarfix.com", "david@hellostarfix.com",
        "emma@hellostarfix.com", "alex@hellostarfix.com", "audits@hellostarfix.com",
        "chris@hellostarfix.com", "hello@hellostarfix.com", "laura@hellostarfix.com",
        "james@hellostarfix.com", "alex@starfix.online",
    ]
    mb = iter(mailboxes)
    results = []

    # --- Campaign 1: Amazon Seller UK/USA [MIGRATED] (product category) ---
    sys.path.insert(0, SCRATCH)
    import sequences as S1
    from_email = next(mb)
    subj, body = render(S1.E1_SUBJECT, S1.E1_BODY, from_email.split("@")[0].capitalize())
    results.append(send("Amazon Seller UK/USA [MIGRATED]", from_email, subj, body))

    # --- Campaign 2: Amazon Seller - Rating [MIGRATED FROM INSTANTLY DRAFT] ---
    import sequences_rating as S2
    from_email = next(mb)
    subj, body = render(S2.E1_SUBJECT, S2.E1_BODY, from_email.split("@")[0].capitalize())
    results.append(send("Amazon Seller - Rating [MIGRATED FROM INSTANTLY DRAFT]", from_email, subj, body))

    # --- Campaigns 3-10: build_batch2.py GROUPS ---
    import build_batch2 as B
    data = json.load(open(os.path.join(SCRATCH, "other24_full.json")))
    sig_to_cnames = {}
    for cname, c in data.items():
        sig_to_cnames.setdefault(sig(c["detail"]), []).append(cname)

    for group_sig, camp_name, fix_brand in B.GROUPS:
        members = sig_to_cnames[group_sig]
        detail = data[members[0]]["detail"]
        sequences = B.convert_sequences(detail, fix_brand)
        step1 = sequences[0]
        variant = step1["variations"][0]
        from_email = next(mb)
        subj, body = render(variant["subject"], variant["body"], from_email.split("@")[0].capitalize(), is_html=True)
        results.append(send(camp_name, from_email, subj, body))

    # --- Campaign 11: SalesFix (brand-fixed, no spintax, no merge vars) ---
    seqs = json.load(open(os.path.join(SCRATCH, "salesfix_sequences_fixed.json")))
    variant = seqs[0]["variations"][0]
    from_email = next(mb)
    subj, body = render(variant["subject"], variant["body"], from_email.split("@")[0].capitalize(), is_html=True)
    results.append(send("Sports & Fitness / Pet / Baby / Review2-DE (SalesFix) [MIGRATED]", from_email, subj, body))

    print(f"\n{sum(results)}/{len(results)} sent successfully")


if __name__ == "__main__":
    main()
