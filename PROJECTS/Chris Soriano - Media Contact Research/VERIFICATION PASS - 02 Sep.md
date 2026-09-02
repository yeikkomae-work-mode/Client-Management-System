# Verification pass — 2 Sep 2026

Triggered by Chris reporting bounces and dead websites.

---

## 1. First, a scope flag

Chris said he was working through **"Japanese rice and Japanese blades."**

**Neither category exists in the list I built.** My rice rows are China and Vietnam only.
There is no knives/blades category at all — zero rows, any country. The 21 categories I
covered are: wasabi, soy sauce, rice vinegar, nori, whisky, sake, green tea, snacks (Japan);
soy, oyster, vinegar, rice, mooncakes, snacks, baijiu, tea (China); chili sauce, fish sauce,
coffee, noodles, rice paper, rice, snacks, alcohol, condensed milk, tea (Vietnam).

So at least part of what he's clicking through came from somewhere else. Worth establishing
before anyone re-does work — otherwise we're fixing a list that isn't ours.

**Second thing worth saying plainly:** of the 116 rows, only 43 ever had an email. 19 were
web-form URLs and 12 were phone-only or "no contact published," because those companies
publish no email at all. If those cells were treated as an address list, they would read as
bounces. That's a column-usage problem, not a data-accuracy problem.

## 2. Every domain tested

98 unique domains, live HTTP + DNS check.

**Genuinely broken — my errors, now fixed:**

| # | Company | Problem | Fixed to |
|---|---------|---------|----------|
| 101 | Richy (Tipo) | `richyexport.com` — **dead domain**, apex and www both NXDOMAIN | `richy.com.vn` (live) + new email |
| 69 | Bama Tea | `en.int-bamatea.com` — **dead domain**, NXDOMAIN | `bamatea.com` (resolves, unreachable from outside China) |
| 45 | Gold Plum | `jcof.com` does not resolve | `jscof.com` is live → `zhanghui@jscof.com` |

**Not actually broken** — several domains fail on the bare apex but work on `www`
(cofco.com, want-want.com, prb.cn, zjhengshun.com). Those are fine; a checker that only
tests the apex reports false deaths.

**Mainland China / Vietnam sites are geo-blocked from my end** (Wuyutai, HEYTEA, Bama,
Trung Nguyên, Vinamit, Tufoco, Guanshengyuan). Unreachable here ≠ dead. Those need a
browser in-region.

## 3. Emails pulled directly off the websites

Not from search — fetched the actual pages and read the source.

| # | Company | New email | Note |
|---|---------|-----------|------|
| 74 | **Masan / CHIN-SU** | `pr@msn.masangroup.com` | **Decoded from Cloudflare obfuscation.** Dedicated PR desk. Covers CHIN-SU + Phúc Long + Vinacafe |
| 55 | **Maxim's / Mei-Xin** | `pcr@maxims.com.hk` | PCR = Public/Corporate Relations — a real PR desk |
| 104 | SABECO | `sabeco@sabeco.com.vn` | also `sales.export@sabeco.com.vn` |
| 84 | King Coffee | `cs@kingcoffee.com` | also `kcf.franchise@kingcoffee.com` |
| 88 | Acecook | `info@acecookvietnam.com` | note `.com`, not `.vn` |
| 101 | Richy | `info@richy.com.vn` | from the corrected domain |
| 59 | White Rabbit / Bright Food | `gmspjt@brightfood.com` | was "no contact found" |
| 65 | Luzhou Laojiao | `schk@lzlj.com` | was "no contact found" |
| 76 | Nam Dương | `info-ndfc@vn.wilmar-intl.com` | see ownership note below |
| 90 | SAFOCO | `safoco@hcm.vnn.vn` | was no-email |
| 93 | Three Ladies | `sales@cpacificfoods.com` | US importer |
| 31 | Sugimoto Tea | `info@sugimotousa.com` | was form-only |
| 32 | Aiya Matcha | `info@aiya-america.com` | replaces the masked PR Newswire one |

**43 → 56 rows with a real email.**

## 4. Social routes added — 20 companies

Chris asked for social as a fallback. New column. For the Japanese majors that genuinely
publish no email (Kikkoman, Yamasa, Marukan, Gekkeikan, Ozeki, Kinjirushi, Glico, Suntory,
Nikka), a DM is now the documented alternative.

## 5. Two more junk addresses caught

- **`maruiwasabi.com` is a parked template site, not the company.** The emails on it belong
  to typeface designers (`amkryukov@gmail.com`, `jonpinhorn.typedesign@gmail.com`).
  Anyone scraping it would have mailed strangers.
- **King Coffee's own site prints `info@domainname.com`** — an unedited template
  placeholder sitting live on their contact page. Ignore it.
- **Gạo Ông Cua**: a gmail surfaced but traces to a *different* rice seller. Not safe. The
  founder's phone printed on the packaging is still the real route.

## 6. Ownership finding

**Nam Dương is Wilmar International-owned** (its contact address is `@wilmar-intl.com`) —
same parent group as Arowana rice. Not an independent Vietnamese sponsor. Adds to the
existing traps: Masan owns CHIN-SU + Phúc Long + Vinacafe; Vinamilk owns Ông Thọ +
Southern Star; COFCO owns China Tea + Fortune.

## 7. Still open

Geo-blocked from here, need an in-region browser: Wuyutai, HEYTEA, Bama Tea,
Trung Nguyên, Vinamit, Tufoco/Bamboo Tree, Guanshengyuan. Suntory still blocks all
automation — its media page needs one manual open.
