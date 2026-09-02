# Audit — Chris's Google Sheet (110 rows)

Sheet: `1iN56T5SvqaBbJX24qYKrOsWGSUr5BAFN1DPMuMqgjNg` (tab gid 1327145444)
Audited 2 Sep 2026.

---

## This is not the list I built

| | My list (delivered Aug 25) | Chris's sheet |
|---|---|---|
| Rows | 116 | 110 |
| Countries | Japan, China, Vietnam | Japan only |
| Categories | 21 food/drink | 11, incl. **Knives, Ceramics, Chopsticks** |
| Columns | Contact type, source URL, confidence | Website, Email, Sent |

Knives, ceramics and chopsticks appear nowhere in my research. Neither does Japanese
rice. **Only 15 companies overlap at all**, and where they do, this sheet's contact
disagrees with what I verified on the company's own website.

Every row is marked **"LEAD BY: Eikko."**

## The numbers

| Verdict | Rows |
|---|---:|
| OK | 55 |
| **Broken — both website and email dead** | **32** |
| Broken — website dead | 8 |
| Broken — email undeliverable | 7 |
| Wrong contact (I verified the real one) | 8 |
| **Total unusable** | **55 of 110 — exactly half** |

- **39 of 98 email addresses cannot receive mail.** 33 sit on domains that do not exist.
- **40 of 98 websites do not resolve.** That is Chris's "the websites don't work."

## How it was generated

Near-universal `info@` + a domain guessed from the company name:

`info@masamoto.jp` · `info@tamakirice.com` · `info@sekkarice.com` · `info@yamaroku4.com`
`info@daio-wasabi.co.jp` · `info@utogi-wasabi.jp` · `info@kono-su.co.jp` · `info@naogen.jp`

None of those domains exist. The generator invented a plausible domain, prefixed `info@`,
and never checked. **`info@yoshiiroknife.com`** is a misspelling of the real
`yoshihiroknife.com` — a dropped `h`.

## Verified-wrong contacts

These resolve, so they look fine, but the address is not what the company publishes:

| # | Company | Sheet says | Actually |
|---|---|---|---|
| 62 | Kikkoman | `pr@kikkoman.com` | **Fabricated.** I flagged this exact address on 25 Aug — it exists nowhere on any Kikkoman property. They publish no email at all |
| 91/97 | Mizkan | `press@mizkan.com` | `Communications@mizkan.com` — from their real PR page |
| 107 | Ito En | `marketing@itoen.com` | `customerservice@itoen.com` |
| 31 | Suntory | `press@beamsuntory.com` | Not published; real media page blocks bots |
| 93 | Marukan | `info@marukan-usa.com` | Publishes no email — form only |
| 63 | Yamasa | `info@yamasa.org` | **yamasa.org is a Japanese language school**, not the soy sauce maker |
| 21 | Dassai | `info@dassai.us` | `press@dassai.com` — dassai.us has no MX |
| 23 | Hakkaisan | `info@hakkaisan.com` | `press@hakkaisan.co.jp` + named English-language PR staff |
| 29 | Gekkeikan | `gekkeikanusa.com` | Domain doesn't exist. Real: `us.gekkeikan.com`, phone only |
| 71 | Kinjirushi | `kinjirushi.com` | Domain doesn't exist. Real: `kinjirushiusa.com` |
| 87/105 | Yamamotoyama | `yamamotoyama-usa.com` | Domain doesn't exist. Real: `yamamotoyama.com` |

**`pr@kikkoman.com` is the single most telling item.** It is the exact hallucination I
identified and documented on 25 August. Its presence here means this sheet was built by a
tool that produced the same fabrication — and that the warning never reached whoever built it.

## Duplicates

- **#87 and #105 are both Yamamotoyama** — same company, same dead domain, listed twice.
- **#91 and #97 are both Mizkan** (Mizkan / "Mizkan Zenmi").

## What Chris should do right now

1. **Stop sending from this sheet.** Half of it bounces. Continued sending damages his
   sending-domain reputation, which is far more expensive to fix than the list.
2. Filter `EMAIL DELIVERABILITY` to `MX OK` — those 59 rows are safe to send today.
3. The 55 broken rows need rebuilding from the companies' actual websites.

## Deliverable

`AUDIT - Chris Google Sheet.csv` — all 110 rows with four added columns:
`WEBSITE STATUS`, `EMAIL DELIVERABILITY`, `VERDICT`, plus `CORRECTED WEBSITE` /
`CORRECTED CONTACT` where I have verified replacements.
