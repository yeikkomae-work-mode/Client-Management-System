# Draft WhatsApp reply to Chris — 2 Sep

Send as a few messages.

---

Went back through every site on the list. Found real errors on my end and fixed them — but there's one thing I need to check with you first.

**You mentioned Japanese rice and Japanese blades.** Neither of those is on the list I built. My rice rows are China and Vietnam only, and there's no knives/blades category at all — zero entries, any country. So at least some of what you're clicking through came from a different list. Can you send me the exact sheet you're working from? If there's a second list in play I want to be fixing the right one.

**One thing about the columns.** Out of 116 rows only 43 ever had an actual email. The rest are web forms, phone numbers, or "no contact published" — because a lot of these Japanese and Chinese companies genuinely don't publish an email address anywhere. If those cells got pulled into a send list they'd bounce, but that's the column being used as an address rather than the data being wrong. Only email out of the "Best Media Contact" column where it actually contains an @.

**Now the real errors — mine, and fixed:**
- Richy: I had `richyexport.com`, which is a dead domain. Real site is richy.com.vn. New email `info@richy.com.vn`.
- Bama Tea: I had `en.int-bamatea.com`, also dead.
- Gold Plum: I had `jcof.com` — doesn't resolve. It's `jscof.com`, so `zhanghui@jscof.com`.

Sorry about those three. They'd have wasted your time.

**And the upside — I pulled emails straight off the sites this time instead of trusting search. 43 real emails is now 56.** Best of them:

- **Masan / CHIN-SU: `pr@msn.masangroup.com`** — their PR desk. It was hidden behind Cloudflare scrambling so it doesn't show in any search; I decoded it out of the page source. That one contact covers CHIN-SU, Phúc Long and Vinacafe.
- **Maxim's: `pcr@maxims.com.hk`** — PCR is Public/Corporate Relations, an actual PR desk.
- SABECO, King Coffee, Acecook, White Rabbit/Bright Food, Luzhou Laojiao, SAFOCO, Sugimoto, Aiya — all new, all read off the live site.

**I also added a social column** for the ~20 companies that publish no email at all. For Kikkoman, Yamasa, Marukan, Gekkeikan, Ozeki, Glico and Suntory, a DM is genuinely the only inbound route that exists.

**Two more things I caught so you don't hit them:**
- `maruiwasabi.com` is a parked template site, not the company — the emails on it belong to typeface designers. Don't scrape it.
- King Coffee's own contact page has `info@domainname.com` sitting on it, an unedited template placeholder. Ignore it.

**Also: Nam Dương is Wilmar International-owned** — not an independent Vietnamese company. Same group as Arowana rice.

Still can't reach Wuyutai, HEYTEA, Bama Tea, Trung Nguyên, Vinamit and Tufoco — those are geo-blocked from where I'm working. They're not dead, I just can't load them from here. You'd get through from Asia.

Updated sheet attached.
