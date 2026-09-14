/* Campaigns data — live Smartlead pull (Albert Scott) 2026-09-02 via connector;
   Satlas = documented figures from client profile (Aug 12 audit); Cüneyt = summary (Task Tracker Aug 31);
   Zapmail domains carried from 2026-08-26 snapshot. Do not hand-edit; re-sync instead.
   Campaign fields: leads (unique), ns=not started, ip=in progress, comp=completed,
   uSent/uOpen/uClick = unique counts, replies, bounces, sent = total emails. uOpen 0 ⇒ open tracking off. */
window.CC_CAMPAIGNS = {
  updated: "2026-09-02",
  sources: [
    {
      key:"albertscott", label:"Smartlead — Albert Scott", client:"Yoni (Albert Scott)", live:true,
      statusCounts:{ active:19, paused:21, completed:143, drafted:6, stopped:8, total:197 },
      campaigns:[
        { name:"Newtopia Now 2026 Cards", leads:165, ns:58, ip:98, comp:7, uSent:107, uOpen:44, uClick:18, replies:1, bounces:7, sent:107 },
        { name:"Super Zoo 2026 Cards", leads:727, ns:395, ip:298, comp:15, uSent:331, uOpen:119, uClick:51, replies:6, bounces:27, sent:331 },
        { name:"Eikko - Cosmoprof", leads:1724, ns:985, ip:672, comp:37, uSent:738, uOpen:390, uClick:111, replies:4, bounces:59, sent:967 },
        { name:"Eikko - Global Pet", leads:717, ns:167, ip:534, comp:1, uSent:567, uOpen:101, uClick:43, replies:5, bounces:17, sent:648 },
        { name:"Rachel - IFA (intro before the show)", leads:1751, ns:885, ip:645, comp:205, uSent:866, uOpen:0, uClick:0, replies:20, bounces:26, sent:1036 },
        { name:"Eikko - Expo West Q4", leads:4005, ns:2166, ip:1636, comp:116, uSent:1982, uOpen:1444, uClick:430, replies:37, bounces:192, sent:2827 },
        { name:"Eikko - Sweets and Snacks Q4", leads:2810, ns:1298, ip:1348, comp:119, uSent:1678, uOpen:1062, uClick:677, replies:18, bounces:172, sent:2541 },
        { name:"Eikko - Winter Fancy Fair Q4", leads:431, ns:0, ip:171, comp:252, uSent:430, uOpen:259, uClick:152, replies:3, bounces:56, sent:990 },
        { name:"Eikko - Fancy Foods Q4", leads:12100, ns:9897, ip:1011, comp:1122, uSent:2405, uOpen:1321, uClick:816, replies:30, bounces:238, sent:5277 },
        { name:"Eikko - Toy Fair Q4", leads:3878, ns:2962, ip:650, comp:228, uSent:1263, uOpen:684, uClick:328, replies:17, bounces:367, sent:1837 },
        { name:"Rachel - Pitti Immagine Uomo", leads:472, ns:0, ip:392, comp:66, uSent:472, uOpen:0, uClick:0, replies:17, bounces:50, sent:1228 },
        { name:"Rachel - Spoga+gafa", leads:348, ns:0, ip:260, comp:12, uSent:348, uOpen:0, uClick:0, replies:19, bounces:65, sent:930 },
        { name:"Rachel - ISM Cologne", leads:1226, ns:0, ip:1058, comp:39, uSent:1226, uOpen:0, uClick:0, replies:30, bounces:124, sent:2552 },
        { name:"Eikko - ICAST 2026", leads:358, ns:0, ip:228, comp:72, uSent:358, uOpen:0, uClick:0, replies:29, bounces:37, sent:993 },
        { name:"Rachel - Nordstil", leads:386, ns:0, ip:10, comp:299, uSent:386, uOpen:152, uClick:41, replies:21, bounces:69, sent:1353 },
        { name:"Eikko - Cosmoprof 2026", leads:411, ns:0, ip:309, comp:44, uSent:411, uOpen:0, uClick:0, replies:27, bounces:38, sent:1084 },
        { name:"John - IHS", leads:1496, ns:0, ip:8, comp:1424, uSent:1490, uOpen:0, uClick:0, replies:35, bounces:122, sent:5501 },
        { name:"Rachel - Global Brands 3", leads:1146, ns:0, ip:123, comp:975, uSent:1146, uOpen:211, uClick:166, replies:27, bounces:156, sent:4082 },
        { name:"Cosmoprof Follow up", leads:1483, ns:0, ip:16, comp:1292, uSent:1483, uOpen:0, uClick:0, replies:54, bounces:127, sent:4214 }
      ]
    },
    {
      key:"satlas", label:"PlusVibe — Satlas", client:"Chris Drew (Satlas)", live:false,
      note:"Documented figures from the Aug 12 audit (client profile). Account-wide: 5,005 leads · 662 contacted · 30-day reply 0.66% (target 2%) · bounce 1.28%. 2 drafts held back + 3 Capital Financing shells.",
      docCampaigns:[
        { name:"Mortgage Brokers - Catchall", leads:109, contactedPct:70.6, repliedPct:0, bouncedPct:23.5 },
        { name:"Mortgage Brokers - Google/Microsoft & Others", leads:459, contactedPct:21.4, repliedPct:3.1, bouncedPct:7.1 },
        { name:"Financial Planner - Catchall", leads:291, contactedPct:27.1, repliedPct:1.3, bouncedPct:9 },
        { name:"Financial Planner - Microsoft", leads:2677, contactedPct:2.9, repliedPct:0, bouncedPct:1 },
        { name:"Commercial Real Estate - Catchall", leads:73, contactedPct:15.1, repliedPct:0, bouncedPct:5 },
        { name:"Commercial Real Estate - Microsoft", leads:1170, contactedPct:7, repliedPct:0, bouncedPct:2.3 },
        { name:"Commercial Real Estate - Google & Others", leads:225, contactedPct:32, repliedPct:1.4, bouncedPct:10.7 }
      ]
    },
    {
      key:"starfix", label:"PlusVibe — Cüneyt (Starfix)", client:"Cüneyt (Starfix)", live:true, activeCount:12,
      note:"LIVE via PlusVibe API 2026-09-02 (key in backend/.env as PLUSVIBE_SELLERVATE_API_KEY — never commit it). Summary endpoint exposes no per-campaign lead totals. 12 active / 9 paused migrated campaigns; sends resumed Sep 1.",
      campaigns:[
              {
                      "name": "Amazon Seller US/CA - Google [MIGRATED]",
                      "status": "ACTIVE",
                      "contacted": 19,
                      "sent": 23,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 3
              },
              {
                      "name": "Amazon Seller - Rating US - Google [MIGRATED FROM INSTANTLY DRAFT]",
                      "status": "ACTIVE",
                      "contacted": 16,
                      "sent": 23,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Amazon Seller UK - Google [MIGRATED]",
                      "status": "ACTIVE",
                      "contacted": 17,
                      "sent": 22,
                      "read": 3,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 2
              },
              {
                      "name": "Amazon Seller - Rating UK - Google [MIGRATED FROM INSTANTLY DRAFT]",
                      "status": "ACTIVE",
                      "contacted": 16,
                      "sent": 23,
                      "read": 4,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Amazon Seller US/CA - Microsoft [MIGRATED]",
                      "status": "ACTIVE",
                      "contacted": 17,
                      "sent": 21,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 3
              },
              {
                      "name": "Amazon Seller US/CA - Other [MIGRATED]",
                      "status": "ACTIVE",
                      "contacted": 12,
                      "sent": 14,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 5
              },
              {
                      "name": "Amazon Seller UK - Microsoft [MIGRATED]",
                      "status": "ACTIVE",
                      "contacted": 16,
                      "sent": 20,
                      "read": 1,
                      "replied": 0,
                      "bounced": 1,
                      "completed": 3
              },
              {
                      "name": "Amazon Seller UK - Other [MIGRATED]",
                      "status": "ACTIVE",
                      "contacted": 12,
                      "sent": 15,
                      "read": 3,
                      "replied": 0,
                      "bounced": 1,
                      "completed": 5
              },
              {
                      "name": "Amazon Seller - Rating US - Microsoft [MIGRATED FROM INSTANTLY DRAFT]",
                      "status": "ACTIVE",
                      "contacted": 18,
                      "sent": 23,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 2
              },
              {
                      "name": "Amazon Seller - Rating US - Other [MIGRATED FROM INSTANTLY DRAFT]",
                      "status": "ACTIVE",
                      "contacted": 17,
                      "sent": 23,
                      "read": 0,
                      "replied": 0,
                      "bounced": 1,
                      "completed": 1
              },
              {
                      "name": "Amazon Seller - Rating UK - Microsoft [MIGRATED FROM INSTANTLY DRAFT]",
                      "status": "ACTIVE",
                      "contacted": 17,
                      "sent": 23,
                      "read": 5,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 1
              },
              {
                      "name": "Amazon Seller - Rating UK - Other [MIGRATED FROM INSTANTLY DRAFT]",
                      "status": "ACTIVE",
                      "contacted": 17,
                      "sent": 23,
                      "read": 3,
                      "replied": 0,
                      "bounced": 1,
                      "completed": 3
              },
              {
                      "name": "Liste von Dennis + 50K DE Amazon Leads [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "USA Seller [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Amazon Seller 2cnd (2) [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Sports & Fitness Reviews (SellerVate) [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "UK Seller [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Amazon Ops Support [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Starfix New US Leads 2026-07-29 [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Review [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              },
              {
                      "name": "Sports & Fitness / Pet / Baby / Review2-DE (SalesFix) [MIGRATED]",
                      "status": "PAUSED",
                      "contacted": 0,
                      "sent": 0,
                      "read": 0,
                      "replied": 0,
                      "bounced": 0,
                      "completed": 0
              }
      ]
    },
    {
      key:"zapmail", label:"Zapmail — Satlas domains", client:"Chris Drew (Satlas)", live:false,
      note:"Snapshot 2026-08-26. 10 domains / 30 mailboxes, health 87/100 'good', isWarmedUp false on all — the degraded Zapmail batch from the infra audit.",
      domains:["satlasdiscover.com","gosatlas.com","satlasgo.com","satlastry.com","discoversatlas.com","satlaspartner.com","satlaswork.com","satlasworks.com","trysatlas.com","partnersatlas.com"],
      healthScore:87, mailboxes:30, warmedUp:false
    }
  ]
};
