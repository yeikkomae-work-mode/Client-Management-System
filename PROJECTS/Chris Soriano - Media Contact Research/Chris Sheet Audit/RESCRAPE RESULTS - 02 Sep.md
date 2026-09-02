# Full rescrape of Chris's Japan sheet — 2 Sep 2026

Went through every one of the 55 broken/wrong rows individually: real website located,
press or marketing email searched for first, generic email as fallback, social media as
last resort. Every contact was verified by fetching the actual page, not taken from search
snippets. Slower than a bulk pass, but that was the brief — quality over speed.

---

## Result

| | Rows |
|---|---:|
| **Fixed with a verified real contact (website/email/social)** | **52** |
| Carried through unchanged (already OK from the original audit) | 55 |
| **Genuinely unresolved — need your input** | **3** |
| **Total** | **110** |

**64 of 110 rows now have a real, verified email address** (up from 43 originally usable).
The rest have a verified website, phone, or social handle as the documented route where the
company simply doesn't publish an email — same honesty standard as the first project.

Deliverable: **`MASTER - Corrected Japan Sheet (110 rows).csv`** — same row order and
company names as your original sheet, with WEBSITE / EMAIL corrected in place and two new
columns: `CONTACT TYPE` and `STATUS`.

---

## The 3 that need you, not more searching

These aren't domain typos — the sheet's row doesn't clearly correspond to a findable real
company. Fabricating a plausible-looking answer here would be worse than flagging it:

- **#70 Inoue Jozo** (soy sauce) — there's an "Inoue Shoyu" in Shimane, and separately a
  cluster of soy sauce makers in Yuasa, Wakayama (the "birthplace of soy sauce" story this
  category implies). No company matching "Inoue Jozo" specifically in Yuasa turned up.
- **#76 Utogi Wasabi** — Utogi is a **region** in Shizuoka City, not a company name. It's
  known as the birthplace of wasabi cultivation, but the only business there is a
  restaurant/souvenir shop, not an obvious wasabi producer or exporter.
- **#99 Naogen** — this turned out to be a real company, **but it's a soy sauce maker in
  Kanazawa**, not a vinegar producer. It was miscategorized under "Sushi Vinegar."

Tell me what you were actually trying to list for these three and I'll finish them.

---

## Worth knowing about how this was built

**Two more addresses that were on-page but still bad:**

- **Sakai Takayuki** (#3) — `info@sakaitakayukiknives.com` is genuinely printed on their own
  contact page, but the domain **has no MX record** (confirmed on three independent DNS
  resolvers). Mail sent there bounces even though the address looks completely legitimate.
  This is the kind of trap that a plausibility check alone would never catch — I only found
  it by testing mail deliverability directly. Use their contact form instead.
- **Yugeta Shoyu** (#68) — the site that looks official, `yugeta-soy-sauce.com`, has
  `info@mysite.com` sitting live on it — an unedited Wix template placeholder. The real site
  is `yugeta.com`.

**A parked/fake site, same pattern as Tamanishiki last time:** none new this pass, but
worth remembering the standard — a resolving domain is not proof it's the right domain.

**Duplicates found:** #87 and #105 are both Yamamotoyama (nori and tea — one company, one
pitch). #91 and #97 are both Mizkan.

**Category error found:** #99 Naogen, noted above.

**Genuine dead ends** (real companies, no discoverable email or even accessible official
site after a real search): Miyabi Urushi Kogei (chopsticks/tableware, Nagano) and Chichibu
Distillery / Venture Whisky both have no findable direct contact route — social media only.
Sunlife (chopsticks) has an address but no phone or email published anywhere.

---

## Best new finds this pass

- **Daio Wasabi Farm** — `koho@daiowasabi.jp` (*koho* = "public relations" in Japanese) —
  a genuine PR desk, separate from their tourism and webshop addresses.
- **Hasami Porcelain** — `sales@saikaiusa.com`, their actual US-side arm.
- **Wasabi Essentials / Pacific Coast Wasabi** — `info@wasabia.com`, decoded out of
  Cloudflare obfuscation (same technique that found Masan's PR desk last time).
