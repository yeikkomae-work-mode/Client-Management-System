# Draft WhatsApp reply to Chris — 2 Sep (after seeing the sheet)

---

Thanks for sending the sheet — that explains it. Two things.

**First: this isn't the list I built.** Mine was 116 rows across Japan, China and Vietnam — soy sauce, sake, whisky, tea, snacks, fish sauce, mooncakes. This sheet is 110 rows, Japan only, and includes knives, ceramics and chopsticks, which I never researched. Only 15 companies even overlap.

**Second: I ran the whole sheet through a deliverability check, and half of it is bad.**

- **39 of 98 email addresses cannot receive mail.** 33 of them are on domains that don't exist at all.
- **40 of 98 websites don't resolve** — that's the "websites don't work" you hit.
- **55 of 110 rows unusable.** Exactly half.

You can see the pattern in how it was built — nearly every address is `info@` plus a domain guessed from the company name. `info@masamoto.jp`, `info@sekkarice.com`, `info@daio-wasabi.co.jp`, `info@kono-su.co.jp`. None of those domains exist. One of them, `info@yoshiiroknife.com`, is just a misspelling of `yoshihiroknife.com` with a letter dropped.

**The one that tells you the most: the sheet has `pr@kikkoman.com`.** That's the exact fake address I flagged back on 25 August — it doesn't exist anywhere on any Kikkoman site. Kikkoman publishes no email at all. So whatever generated this sheet made the same mistake I'd already caught and written up.

A few more that look fine but are wrong:
- Mizkan: sheet has `press@mizkan.com`, real one is `Communications@mizkan.com`
- Ito En: sheet has `marketing@`, real one is `customerservice@`
- **Yamasa: sheet has `info@yamasa.org` — yamasa.org is a Japanese language school, not the soy sauce company**
- Gekkeikan, Kinjirushi and Yamamotoyama all point at domains that don't exist. I have the real ones.

Also #87 and #105 are the same company (Yamamotoyama), and #91 and #97 are both Mizkan.

**What I'd do right now:**

1. **Stop sending from this sheet.** At a 40% bounce rate you'll burn your sending domain, and that's much harder to repair than the list is.
2. I've attached an audited version — filter `EMAIL DELIVERABILITY` to `MX OK` and those 59 rows are safe to send today.
3. Give me the go-ahead and I'll rebuild the broken 55 properly — off the companies' real websites, with a source link on every row, same as I did before.

Let me know and I'll start on the 55.
