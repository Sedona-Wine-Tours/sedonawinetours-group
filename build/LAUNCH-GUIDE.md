# sedonawinetours.group — Launch & SEO Guide

Prepared September 9, 2026; pricing updated September 13, 2026 from the Summary of Tours Offered (rev. 10-1-25) and the policies effective January 24, 2026 for Jim Reich, Sedona Wine Tours.

## What's in this package

`index.html` (home), `wine-tours-of-sedona.html`, `sip-sedona.html`, `sedona-wine-adventures.html`, `groups-corporate-weddings.html`, `sedona-wineries-and-vineyards.html`, `pricing-and-policies.html`, `thank-you.html`, `404.html`, `contact.php`, `.htaccess`, `assets/styles.css`, `sitemap.xml`, `robots.txt`, and `images/` with your logos. Pages are served at clean URLs (`/sip-sedona`, not `/sip-sedona.html`); the `.htaccess` handles that plus the HTTPS/www redirect, 404 page, compression and caching. Every page is plain HTML and CSS with no framework and no tracking scripts, so it scores well on Core Web Vitals out of the box.

## Where we stand today (from your Search Console, last 6 months)

The .group domain earned roughly 130 impressions and zero clicks in six months. The 23.7 average position is misleading because it sits on almost no traffic; the real story is that the site was invisible. What is encouraging: Google has already been showing it for the long, question-style searches ("where can I book affordable group wine tours in Sedona, Arizona?", "which Sedona group wine tours offer the best value?") that AI-assisted search produces, and it briefly hit position 1 for two of them. The new site is written to own that lane.

Meanwhile winetoursofsedona.com is doing the heavy lifting on the head terms: position 4.8 for "sedona wine tours" (811 impressions), 3.5 for "sedona wine tasting", 3.0 for "wine tours of sedona". We do not want the .group site fighting it for those.

## The keyword split (complement, not compete)

winetoursofsedona.com keeps: sedona wine tours, wine tasting sedona, sedona wineries, sedona vineyard tours, wine tour sedona, and every winery-specific and travel-logistics query it already ranks for.

sedonawinetours.group targets: the "Sedona Wine Tours" brand and "Sedona Wine Tours Group" navigational searches; comparison and decision searches (which Sedona wine tour is right for me, best group wine tours Sedona, affordable wine tasting tours Sedona, Sedona wine tour packages); group and event intent (corporate wine tours Sedona, bachelorette wine tour Sedona, wedding transportation Sedona, wedding shuttle Sedona, group wine tasting Sedona with transportation); and the new in-home product (private in-home wine tasting Sedona, Sedona Cellar Experience); and price-intent searches (Sedona wine tour prices, how much is a wine tour in Sedona, Sedona wine tour cost per person) on the new pricing page. Each of those lives on its own page with its own title, H1, FAQ and FAQPage schema.

## Building it on GoDaddy (Web Hosting with cPanel)

You chose GoDaddy Web Hosting with cPanel — the right call. The site I built is plain HTML, CSS, one PHP file for the contact form and an `.htaccess` file, which is exactly what that plan serves. Here is the whole path, start to finish.

**Step 1 — Add the hosting plan.** In your GoDaddy account go to Products → Web Hosting → Add (the Linux "Web Hosting" plan; Economy is enough for this site, Deluxe if you'd rather host more than one site on it). When it asks which domain to attach, choose sedonawinetours.group. GoDaddy will offer to install WordPress or Website Builder; decline both — we're uploading our own files.

**Step 2 — Upload the site.** Open cPanel (Products → Web Hosting → Manage → cPanel Admin) and click File Manager. Open the `public_html` folder and delete anything GoDaddy placed there (usually a placeholder `index.html` and a `cgi-bin` folder you can leave). Click Upload, drag in `sedonawinetours-group-site.zip`, wait for the bar to finish, then close the upload tab. Back in File Manager, right-click the zip → Extract → extract to `/public_html`. The files land inside a `site` folder; open it, select all (Select All button), then Move → set the destination to `/public_html` → Move Files. Delete the empty `site` folder and the zip. Turn on "Show Hidden Files" in File Manager's Settings (top right) once to confirm `.htaccess` is there — it does the HTTPS redirect, the clean URLs and the caching.

**Step 3 — Point the domain and turn on HTTPS.** If the domain and hosting are in the same GoDaddy account and you attached the domain in Step 1, GoDaddy sets DNS automatically; give it up to an hour. If the domain still shows the old Website Builder site, go to Domains → sedonawinetours.group → DNS and confirm the `A` record points to the hosting IP shown in cPanel (Server Information → Shared IP Address) and that `www` is a `CNAME` to `@`. In cPanel → SSL/TLS Status, select the domain and click Run AutoSSL; GoDaddy issues a free certificate in minutes. Then cancel the Website Builder subscription — but only after `https://www.sedonawinetours.group` shows the new site.

**Step 4 — Contact form email.** The form posts to `contact.php`, which emails `info@winetoursofsedona.com`. Change that address on line 3 of `contact.php` if you want inquiries elsewhere. For deliverability, add `website@sedonawinetours.group` as a forwarder in cPanel → Forwarders (so the From address exists) and, in Domains → DNS, add the SPF record GoDaddy hosting suggests under Email Deliverability. Submit the form once to test; the thank-you page confirms it fired.

**Step 5 — Tell Google.** In Search Console (the `sc-domain:sedonawinetours.group` property already exists), Sitemaps → add `https://www.sedonawinetours.group/sitemap.xml`. Then URL Inspection → paste each of the seven page URLs → Request Indexing. Add the site to Bing Webmaster Tools too (Import from Search Console takes one click). Finally, add the "Part of the Sedona Wine Tours family" footer link on the three brand sites — that's what will move rankings fastest.

**Weekly cadence (set up).** Every Monday at 8 a.m. Arizona time you receive the "Weekly specials questionnaire" email; reply inline by Tuesday night. Every Wednesday at 9 a.m. the refresh task reads your reply, updates the homepage specials (`build/specials.json`, max three, each with an end date), features the tour you named, rotates one seasonal paragraph for freshness, checks prices against the public booking pages, rebuilds, commits to GitHub and reports the four tracked rankings. cPanel's Git deploy publishes the commit.

**Tour Chooser.** The five-question quiz on the homepage scores every tour in `build/chooser.py` against the visitor's answers (party size, style, hours, what they drink, must-have) and shows the three best fits with booking buttons. Fifteen-plus parties are routed to a call; weddings to SIP Sedona's shuttles; "tasting at our rental" to The Sedona Cellar Experience. To add a tour to the chooser, add one line to `TOURS` with its tags.

**Direct bookings.** Every Wine Tours of Sedona "Book now" opens FareHarbor in a lightframe over the page (the FareHarbor embed script is on every page), so the visitor books into your dashboard without leaving the site; SIP Sedona and Sedona Wine Adventures buttons go to those sites' booking pages, which feed the same FareHarbor account.

**How updates work from here.** You tell me the change in plain English — "the Terroir tour is now $395," "add a new fall tour," "swap the hero photo" — and I regenerate the site and send you a fresh zip. You repeat Step 2 (upload, extract, move: about two minutes), or, when your computer is linked to our session, I can do the upload myself through your browser while you watch. Every fact lives in one file, `build/content.py`, so a price change is a one-line edit on my side, and the monthly FareHarbor refresh task already knows how to rebuild. If you ever want to make small text edits yourself, cPanel's File Manager has an Edit button that opens any page in a code editor; the text is plain enough to find and change.

**If you'd rather never touch cPanel again.** cPanel has a Git Version Control feature: connect it to a private GitHub repository once, and every time I push an update you click "Update from Remote" (or a scheduled cron does it). Say the word and I'll set that up with you — it needs you to create a free GitHub account and paste one token.

## Keyword map (from Search Console across all four properties, last 90 days)

Real search volume, not guesses. The numbers are impressions your own sites received, which is the most reliable demand signal available for this market.

| Page | Primary target (impressions) | Supporting terms | Title tag |
|---|---|---|---|
| Home `/` | sedona wine tours (2,458 on sipsedona, 811 on WTOS) | sedona wine tasting tours (116), sedona wine tours packages (73), best sedona wine tours (37), wine tours in sedona az (79) | Sedona Wine Tours \| Wine Tasting Tours, Private, Group & Packages |
| Wine Tours of Sedona | private wine tours sedona, sedona vineyard tours (489) | wine tours of sedona (463), verde valley wine tour (110), luxury wine tour sedona | Private Sedona Wine & Vineyard Tours \| Wine Tours of Sedona |
| SIP Sedona | sedona wine tour bus (43), sedona shuttle service (263) | group transportation arizona (396), sip sedona (154), inexpensive wine tour sedona (26), wedding shuttle sedona | Sedona Wine Tour Bus & Group Shuttle \| SIP Sedona Wine Tours |
| Sedona Wine Adventures | private wine tasting arizona (117), da ranch sedona (323) | da ranch winery sedona (110), sedona wine adventures (81), verde valley wine tours (203) | Private Wine Tasting Tours Sedona \| Sedona Wine Adventures |
| Groups & weddings | group wine tours sedona, corporate coach sedona arizona (53) | sedona bachelorette party (112), group transportation arizona (396), wedding transportation sedona | Group Wine Tours Sedona \| Corporate, Bachelorette & Weddings |
| Wineries & vineyards | wineries in sedona (578), sedona wineries (923) | winery in sedona (497), vineyards in sedona (309), wineries sedona arizona (337), cottonwood wineries (117), da ranch (1,355) | Wineries in Sedona & Verde Valley Vineyards \| Insider's Guide |
| Pricing & policies | sedona wine tour prices / cost | how much is a wine tour in sedona, sedona wine tour cost per person | Sedona Wine Tour Prices & Cost \| Discounts & Policies |

Two things to know about this map. First, "sedona wineries / wineries in sedona / winery in sedona" is the largest pool of demand none of your sites currently wins (positions 8–26); the new wineries guide is written for it, and it is the page most likely to earn links from travel blogs. Second, the head term "sedona wine tours" now appears in the umbrella site's title as well as the brand sites'. That is deliberate: all four domains are yours, so a second listing on page one is pure gain, and the umbrella page answers a different intent (comparison) than the brand pages (booking).

## Before launch — the confirm list

Everything marked with a yellow "Confirm" badge in the preview:

1. The Sedona Cellar Experience (FareHarbor item 752593): price, duration, minimum and maximum group size, and what is poured. The copy is written to hold any answer; add the specifics and remove the badge in `index.html` (search for `Confirm`).
2. Top three tours per division. The lists are ranked from the public sites; replace with FareHarbor's actual most-booked items if different. Each card lives in `build/content.py` (`WTOS_TOP`, `SIP_TOP`, `SWA_TOP`) if you keep the build, or directly in the three division HTML files.
3. Reviews. Three real quotes from winetoursofsedona.com are used. Adding one recent review per division with the guide's name and the platform it came from would let us add AggregateRating schema (do not add the schema without real, displayed reviews).
4. Verde Valley Spirits stops: the site names Spirits & Spice, Redwall Distillery and the Southwest Wine Center plus Old Town Cottonwood's new distilleries — confirm those are current once the distilleries open.
5. Office hours in the contact section (8 a.m. to 6 p.m. is a placeholder).

## Pricing sources used

All Wine Tours of Sedona retail prices, durations, inclusions and stops come from the Summary of Tours Offered (rev. 10-1-25); the group figures shown on the site are the retail-less-20% net rates (the 18% group gratuity is described, not folded into the displayed number, so the numbers stay honest and simple). SIP Sedona tours are $90/$120/$150/$240 plus 18%, with shuttles at $250 per hour (10- and 14-passenger vans) and $400 per hour (25-, 30-, 33-passenger coaches). Sedona Wine Adventures tours are $150/$250/$95/$250/$300 plus 18%. Discounts, add-ons, pickup fees, gratuity and cancellation follow the policies effective January 24, 2026. When the master sheet changes, `build/content.py` holds every number in one place (`WTOS_*`, `SIP_TOP`, `SWA_TOP`, and the pricing page section).

## Logos already in place

The Sedona Wine Tours emblem (`images/swt-emblem.webp`, header/footer at `swt-emblem-sm.webp`) and the three division badges (`images/badge-wtos.png`, `badge-sip.png`, `badge-swa.png`) are used throughout, and `og-sedona-wine-tours.jpg` was generated from the emblem for social previews. The Wine Tours of Sedona badge is the full-resolution standalone logo. All three division badges (`badge-wtos.png`, `badge-sip.png`, `badge-swa.png`) are the full-resolution standalone logos you supplied.

## Photography shot list (drop into `images/`, then swap the placeholder blocks)

The social preview image is already generated from the emblem. Homepage hero: the emblem now anchors it; a guide and two guests at Alcantara's river patio at golden hour is the ideal frame. Cellar Experience: a guide pouring a flight on a vacation-rental patio with the rocks lit behind. Divisions: one vehicle shot per division (SUV, SIP van, coach) so the fleet section can become photographic. Wineries: one wide shot each of Page Springs vines, Old Town Cottonwood's main street, and Jerome from below. Always compress to under 200 KB and use descriptive file names and alt text (`alcantara-vineyards-verde-river-patio-sedona-wine-tour.jpg`).

## Off-page work that moves rankings (in priority order)

Link the three brand sites to this one. Add "Part of the Sedona Wine Tours family" with a link to www.sedonawinetours.group in the footer of winetoursofsedona.com, sipsedona.com and sedonawineadventures.com, and link each brand's About page to its division page here. Those three aged, trusted domains are the strongest links this site can get, and today they point nowhere.

Google Business Profile: keep each division's GBP pointing at its own site (that is what wins the map pack). Create or claim a LinkedIn page and a Facebook page for "Sedona Wine Tours" with this URL, and list this URL on the Sedona Chamber and Visit Sedona directories as the parent company.

Consistency: use exactly "2020 Contractors Road, Suite 3, Sedona, AZ 86336" and "(928) 504-2445" everywhere the parent company appears.

Content cadence: one new decision-style page every four to six weeks, written to the questions Search Console shows — for example "Sedona wine tour vs. Cottonwood wine tour: which should you book?", "Best Sedona wine tours for a bachelorette party (by group size)", "Corporate retreat wine tours in Sedona: a planner's guide". Each gets FAQ schema and links to the relevant division.

## On the position goal

Positions 1–5 for the brand and the group/comparison terms are realistic within a few months once the site is live, linked from the brand sites and indexed. "Never below position 5" is not something any site can guarantee — rankings move with Google's updates, seasonality and competitors — but the structure here (unique intent per page, schema, internal links, fast static pages, monthly refresh) is what keeps a site on page one durably. Check Search Console monthly alongside the FareHarbor refresh.
