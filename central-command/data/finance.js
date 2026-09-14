/* Synced from Notion Finance Tracker (collection://3bf811e2-1c7f-80d2-9c10-000b0ef13bee)
   + Bills debt tracker (collection://3bf811e2-1c7f-80dc-a615-000be3abd79f) — do not hand-edit; re-sync instead.
   Amounts in PHP. saved = income − billsTotal (null when either side is missing). */
window.CC_FINANCE = {
  updated: "2026-09-02",
  entries: [
    { date:"2026-08-17", client:"Cuneyt", income:6400, bills:"Initao - 3100 | Dongki Allowance - 500", billsTotal:3600, details:"received through Wise for 15 hours work 7$ per hour from last week" },
    { date:"2026-08-18", client:"Yoni", income:14400, bills:"Rent - 9500 | Laundry - 2000 | Tubil - 1000 | EatOut - 3204 | HBO - 400", billsTotal:16104, details:"Through Wise" },
    { date:"2026-08-20", client:"Chris Caffera", income:8800, bills:"SLoan - 2128 | GLoan - 1300 | HomeCreditCard - 2000", billsTotal:5428, details:"Through Wise" },
    { date:"2026-08-21", client:"Darius", income:1590, bills:null, billsTotal:null, details:"Through Wise" },
    { date:"2026-08-25", client:"Yoni", income:16980, bills:"Homecredit Laptop - 5222 | Claude Max Plan - 8000 | Tawing - 500 | Gerry - 125", billsTotal:13847, details:"Through Wise" },
    { date:"2026-08-25", client:"Cuneyt", income:6400, bills:null, billsTotal:null, details:"Through Wise | Extra money for coffee and food" },
    { date:"2026-08-26", client:"Chris Drew", income:17500, bills:"Loan Ate - 20000", billsTotal:20000, details:"monthly + client commission 400AUD" },
    { date:"2026-08-28", client:"Chris Caffera", income:8950, bills:"iCloud - 700 | Tubil - 1000 | Dongki - 500 | Wifi - 1,500 | Grab&Laag - 3850 | Pampers - 400 | TrashBag - 200 | Movie&Apple TV - 500 | Canva - 300", billsTotal:8950, details:null },
    { date:"2026-08-31", client:"Cuneyt", income:6100, bills:"Eatout N Cafe - 2500 | Initao Allowance - 2000 | Nails - 1500", billsTotal:6000, details:null },
    { date:"2026-09-01", client:"Yoni", income:13300, bills:"Tubil - 1000 | Billease - 2076.07 + 1603.68 | Grocery - (amount TBD)", billsTotal:4679.75, details:"Bills Total is partial — Grocery amount TBD" },
    { date:"2026-09-01", client:"Penji", income:null, bills:null, billsTotal:null, details:"expected" },
    { date:"2026-09-03", client:"Chris Caffera", income:null, bills:null, billsTotal:null, details:"expected" },
    { date:"2026-09-07", client:"Yoni", income:null, bills:null, billsTotal:null, details:"expected" },
    { date:"2026-09-10", client:"Chris Caffera", income:null, bills:null, billsTotal:null, details:"expected" }
  ],
  debts: [
    { from:"Billease Cristy Account", total:12457, monthly:2077, paid:null, due:"2026-09-01" },
    { from:"Billease Eikko Account", total:4811, monthly:1602, paid:null, due:"2026-09-01" },
    { from:"Wifi", total:null, monthly:1500, paid:null, due:"2026-09-03" },
    { from:"Electricity and Water", total:null, monthly:null, paid:null, due:"2026-09-07" },
    { from:"Sloan", total:5700, monthly:1900, paid:3800, due:"2026-09-08" },
    { from:"Gloan", total:19102, monthly:1800, paid:null, due:"2026-09-09" },
    { from:"Atome", total:5990, monthly:2662, paid:null, due:"2026-09-09" },
    { from:"Sloan", total:16341, monthly:2971, paid:null, due:"2026-09-11" },
    { from:"Tiktok Loan", total:5900, monthly:1967, paid:null, due:"2026-09-12" },
    { from:"HomeCredit Refrigerator", total:2672, monthly:1336, paid:null, due:"2026-09-13" },
    { from:"Sloan", total:8744, monthly:2186, paid:null, due:"2026-09-14" },
    { from:"Spaylater", total:57096, monthly:6022, paid:null, due:"2026-09-15" },
    { from:"Apartment", total:null, monthly:9500, paid:null, due:"2026-09-15" },
    { from:"Tiktok", total:4300, monthly:2500, paid:null, due:"2026-09-15" },
    { from:"Gloan", total:6796, monthly:1133, paid:null, due:"2026-09-16" },
    { from:"Home Credit Card", total:20648, monthly:2000, paid:null, due:"2026-09-21" },
    { from:"Gloan", total:9200, monthly:1300, paid:null, due:"2026-09-24" },
    { from:"HomeCredit (Laptop)", total:156660, monthly:5222, paid:null, due:"2026-09-29" },
    { from:"Sloan", total:4255, monthly:2128, paid:null, due:"2026-09-30" }
  ]
};
