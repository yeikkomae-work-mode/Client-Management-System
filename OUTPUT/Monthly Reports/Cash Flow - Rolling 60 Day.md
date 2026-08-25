# Cash Flow — Rolling 60 Day

**Generated:** 2026-08-25 · by `cfo` · **window 2026-08-25 → 2026-10-24**
**FX rate:** **NOT SET** (`CLIENT PROFILES/Important info.md`). All figures below are natively ₱; no conversion performed.
**Source:** Notion → Finance Tracker (income) + Bills (obligations), read live.
**This file is overwritten on every run** — it is a rolling view, not an archive.

> ### ⚠️ Opening cash balance is not recorded anywhere
> Not in Notion, not in this repo. The **Running** column below is therefore **cumulative net flow from 2026-08-25**, not a bank balance. It shows *direction and timing*, not solvency. A negative running figure means "you are ₱X down on the period," not "you are overdrawn." **Whether any of this actually clears depends on an opening balance nobody has written down.** Recording it is the single highest-value fix to this report.

---

## Dated ledger

| Date | | Item | ₱ | Running | Flag |
|---|---|---|---|---|---|
| 08-25 | IN | Cüneyt (Sellervate) — Wise | +6,400 | 6,400 | |
| 08-25 | OUT | Homecredit Laptop 5,222 · Dongki & Nanay Allowance 1,000 | −6,222 | 178 | |
| 08-26 | IN | Chris Drew (Satlas) | **not recorded** | 178 | ⚠️ |
| 08-28 | IN | Chris Caffera | **not recorded** | 178 | ⚠️ |
| 08-28 | OUT | Loan Ate | −10,000 | **−9,822** | 🔴 |
| 08-31 | IN | Yoni | **not recorded** | −9,822 | ⚠️ |
| 08-31 | OUT | Loan Ate | −10,000 | **−19,822** | 🔴 |
| 09-01 | OUT | Billease Cristy Account | −2,077 | −21,899 | |
| 09-01 | OUT | Billease Eikko Account | −1,602 | −23,501 | |
| 09-03 | OUT | Wifi | −1,500 | −25,001 | |
| 09-07 | OUT | Electricity and Water | **not recorded** | −25,001 | ⚠️ |
| 09-08 | OUT | Sloan | −1,900 | −26,901 | |
| 09-09 | OUT | Gloan | −1,800 | −28,701 | |
| 09-09 | OUT | Atome | −2,662 | −31,363 | |
| 09-11 | OUT | Sloan | −2,971 | −34,334 | |
| 09-12 | OUT | Tiktok Loan | −1,967 | −36,301 | |
| 09-13 | OUT | HomeCredit Refrigerator | −1,336 | −37,637 | |
| 09-14 | OUT | Sloan | −2,186 | −39,823 | |
| 09-15 | OUT | Tiktok | −2,500 | −42,323 | |
| 09-15 | OUT | Spaylater | −6,022 | −48,345 | |
| 09-15 | OUT | Apartment | −9,500 | **−57,845** | 🔴 |
| 09-16 | OUT | Gloan | −1,133 | −58,978 | |
| 09-21 | OUT | Home Credit Card | −2,000 | −60,978 | |
| 09-24 | OUT | Gloan | −1,300 | −62,278 | |
| 09-29 | OUT | HomeCredit (Laptop) | −5,222 | −67,500 | |
| 09-30 | OUT | Sloan | −2,128 | **−69,628** | |
| 10-01 → 10-24 | — | *No obligation rows and no income rows exist in either data source for October.* | — | −69,628 | ⚠️ |

**Rows with no amount contribute nothing to the running total.** They are shown so the *timing* is visible. They are not modelled as ₱0 and not carried forward from a previous month.

---

## 🔴 The headline: September has ₱49,806 of dated obligations and zero income rows

This is the finding that earns this report its keep.

- **September obligations: ₱49,806**, every one of them dated, spread across 18 rows from 09-01 to 09-30. This figure reconciles exactly to the `Monthly Payment ` sum in the Bills data source.
- **September income: nothing at all.** The Finance Tracker contains **zero rows dated in September**. Not blank rows — *no rows*. Every income row in the database stops at 2026-08-31.

That is not a forecast of trouble; it is an empty forecast. The obligations are scheduled and specific; the income against them has not been entered. **Adding September's expected income rows is the single most urgent data fix in this system.**

## ⚠️ Weeks where obligations land before money does

Flagging sequencing, not just monthly totals — solvent-on-the-month and solvent-on-the-week are different questions, and the second is what actually bounces a payment.

| Week | In (recorded) | Out | Net | Assessment |
|---|---|---|---|---|
| **Aug 25–31** | ₱6,400 recorded; **3 rows blank** | ₱26,222 | **−19,822** | 🔴 **Worst week in the window.** ₱20,000 of `Loan Ate` lands on 08-28 and 08-31 against three income rows that carry no amount. If those three land as expected this is fine; if they slip, ₱20,000 falls due with ₱178 of recorded cover. |
| Sep 1–7 | none | ₱5,179 (+ Electricity/Water, unrecorded) | −5,179 | 🔴 Obligations only. |
| Sep 8–14 | none | ₱13,156 | −13,156 | 🔴 Obligations only. |
| **Sep 15–21** | none | ₱19,155 | **−19,155** | 🔴 **Heaviest obligation week.** Apartment ₱9,500 + Spaylater ₱6,022 + Tiktok ₱2,500 all land on 09-15. |
| Sep 22–30 | none | ₱8,650 | −8,650 | 🔴 Obligations only. |
| Oct 1–24 | none | none | 0 | ⚠️ No data either side. |

**Every week from 09-01 onward shows obligations against zero recorded income.** That is a logging gap, not necessarily a cash crisis — but it cannot be told apart from one using the data as it currently stands.

## Margin

At the **verified 2026-08-25 figures** the brief cites — ₱54,570 received against ₱49,806 fixed obligations — the margin is **₱4,764, or 8.7%**, before food, transport, or tools.

**On live data as read today, income is ₱37,590, which does not cover ₱49,806** — a shortfall of ₱12,216, or −32.5% against obligations. The difference is the single ₱16,980 Yoni row discussed in `2026-08 - Monthly Close.md`. **This is not adjusted to fit.** If that ₱16,980 is restored, the 8.7% margin holds; if it is genuinely gone, August does not cover September.

Either way, **8.7% is a thin margin before food, transport, or tools are counted** — and business tooling (Claude ₱7,000/mo, iCloud ₱600/mo) is not in these numbers at all, because no register exists to hold it. Adding ₱7,600 of real monthly tooling to ₱49,806 takes fixed obligations to **₱57,406**, which exceeds even the ₱54,570 best case.

## What would make this report trustworthy

1. **Record the opening cash balance.** Without it this is flow, not position.
2. **Enter September's expected income rows.** The forecast is currently empty on one side.
3. **Fill the four blank August income amounts.**
4. **Record `Electricity and Water`'s monthly payment** — the only obligation row with no amount.
5. **Build the Tools & Subscriptions register** so ₱7,600+/mo of real tooling stops being invisible.
