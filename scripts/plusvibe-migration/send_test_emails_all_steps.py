"""Send test emails for Step 1, 2, and 3 of each of the 12 currently-paused
ESP-split campaigns (36 emails total) to cueneyt.nurdogan@sellervate.de, so
Cüneyt can check inbox placement across the full sequence, not just the
opener. Reuses the render/resolve_spintax/fill_vars helpers from
send_test_emails.py. `from` is the first mailbox currently on each
campaign's roster (post health-removal), pulled live via
campaign/get/accounts rather than assumed.
"""
import json, os, re, subprocess, sys, tempfile

API = "https://api.plusvibe.ai/api/v1"
KEY = os.environ["PV_KEY"]
WS = os.environ["PV_WS"]
TO = "cueneyt.nurdogan@sellervate.de"
SCRATCH = os.path.dirname(__file__)
sys.path.insert(0, SCRATCH)

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

CAMPAIGNS = [
    ("6a8cf6f27e5c6119d8830749", "Amazon Seller US/CA - Google [MIGRATED]", "product"),
    ("6a90cd6f2dbb802b3e05cc6b", "Amazon Seller US/CA - Microsoft [MIGRATED]", "product"),
    ("6a90cd70fdaf9c49f3b0ca64", "Amazon Seller US/CA - Other [MIGRATED]", "product"),
    ("6a90b3bcf68baa1111ed5c7f", "Amazon Seller UK - Google [MIGRATED]", "product"),
    ("6a90cd72b8f24dca09ef6bb8", "Amazon Seller UK - Microsoft [MIGRATED]", "product"),
    ("6a90cd742dbb802b3e05cc6c", "Amazon Seller UK - Other [MIGRATED]", "product"),
    ("6a8ee087c3903d2a71741b72", "Amazon Seller - Rating US - Google [MIGRATED FROM INSTANTLY DRAFT]", "rating"),
    ("6a90cd764fdc64a002d2ca4a", "Amazon Seller - Rating US - Microsoft [MIGRATED FROM INSTANTLY DRAFT]", "rating"),
    ("6a90cd772dbb802b3e05cc6d", "Amazon Seller - Rating US - Other [MIGRATED FROM INSTANTLY DRAFT]", "rating"),
    ("6a90b41d24acfefeb9390a4c", "Amazon Seller - Rating UK - Google [MIGRATED FROM INSTANTLY DRAFT]", "rating"),
    ("6a90cd790d0bcf449012a962", "Amazon Seller - Rating UK - Microsoft [MIGRATED FROM INSTANTLY DRAFT]", "rating"),
    ("6a90cd7b5dddc42c583f1012", "Amazon Seller - Rating UK - Other [MIGRATED FROM INSTANTLY DRAFT]", "rating"),
]


def resolve_spintax(text):
    def pick(m):
        return m.group(1).split("|")[0].strip()
    while "{{RANDOM" in text:
        text = re.sub(r"\{\{RANDOM\s*\|([^{}]*)\}\}", pick, text, count=1)
    return text


def fill_vars(text, from_name):
    for k, v in PLACEHOLDERS.items():
        text = text.replace("{{%s}}" % k, v)
    return text.replace("{{FROM_NAME}}", from_name)


def render(subject, body_lines, from_name, step_num):
    subject = fill_vars(resolve_spintax(subject), from_name)
    body = "".join(f"<p>{fill_vars(resolve_spintax(l), from_name)}</p>" for l in body_lines)
    banner = (f"<p style='color:#888;font-size:12px'>[TEST SEND — Step {step_num}, "
              f"rendered with placeholder lead data, spintax resolved to variant 1]</p>")
    return subject, banner + body


def call(method, path, body=None, query=""):
    url = f"{API}/{path}" + (f"?{query}" if query else "")
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


def send(label, from_email, subject, body_html):
    code, payload = call("POST", "unibox/emails/send", {
        "subject": f"[TEST] {subject}",
        "from": from_email,
        "to": TO,
        "body": body_html,
    }, query=f"workspace_id={WS}")
    ok = code == "200"
    print(f"{'OK ' if ok else 'FAIL'} {label:70s} from={from_email:30s} http={code} {'' if ok else payload[:150]}")
    return ok


def main():
    import sequences as S1
    import sequences_rating as S2
    steps = {
        "product": [(S1.E1_SUBJECT, S1.E1_BODY), (S1.E2_SUBJECT, S1.E2_BODY), (S1.E3_SUBJECT, S1.E3_BODY)],
        "rating": [(S2.E1_SUBJECT, S2.E1_BODY), (S2.E2_SUBJECT, S2.E2_BODY), (S2.E3_SUBJECT, S2.E3_BODY)],
    }

    results = []
    for cid, name, family in CAMPAIGNS:
        code, payload = call("GET", "campaign/get/accounts", query=f"workspace_id={WS}&campaign_id={cid}")
        if code != "200":
            print(f"FAIL could not fetch accounts for {name}: {payload[:150]}")
            continue
        roster = json.loads(payload)
        if not roster:
            print(f"SKIP {name} has zero mailboxes attached")
            continue
        from_email = roster[0]
        from_name = from_email.split("@")[0].capitalize()

        for i, (subj_raw, body_raw) in enumerate(steps[family], start=1):
            subj, body = render(subj_raw, body_raw, from_name, i)
            results.append(send(f"{name} — Step {i}", from_email, subj, body))

    print(f"\n{sum(results)}/{len(results)} sent successfully")


if __name__ == "__main__":
    main()
