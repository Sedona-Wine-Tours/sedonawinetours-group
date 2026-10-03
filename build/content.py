# -*- coding: utf-8 -*-
"""Page content for sedonawinetours.group. Copy is first-person plural ("we").
Pricing source: Jim's "Summary of Tours Offered – Revised 10-1-25" and policies effective January 24, 2026."""
from build import (ORG, breadcrumbs, faq_schema, faq_html, offers_schema, tour_card,
                   PHONE_MAIN, PHONE_MAIN_TEL, PHONE_WTOS, PHONE_WTOS_TEL, PHONE_SIP, PHONE_SIP_TEL,
                   PHONE_SWA, PHONE_SWA_TEL, ADDRESS, SITE)

def tel(s, t=None, n=None):
    return s.replace("{TEL}", t or PHONE_MAIN_TEL).replace("{NUM}", n or PHONE_MAIN)

FH = "https://fareharbor.com/embeds/book/winetoursofsedona/items/{}/?full-items=yes"
CONFIRM = ''  # site is live: internal confirm badges disabled
WTOS_BOOK = "https://winetoursofsedona.com/book-now-tour-menu/"
SWA_BOOK = "https://www.sedonawineadventures.com/reservations/"
SIP_BOOK = "https://sipsedona.com/"

# ---------------------------------------------------------------- tours
WTOS_TOP = [
  dict(name="Sedona &amp; Verde Valley Tour: Wine, Beer, Raw Chocolate &amp; Lunch", duration="5 hours", meta="Private · All-inclusive", price="$444", price_num="444", price_note="per adult · 6+ $355.20",
       desc="Our most popular tour, and the one for groups that can't agree: four wine or beer flights, $11 in raw artisan chocolate and lunch, routed anywhere in the Verde Valley by what your group likes.",
       includes=["Four wine or beer tasting flights", "$11 in raw chocolate tastings and lunch", "3 p.m. and 4 p.m. departures can upgrade lunch to dinner for $22 per adult", "Private climate-controlled vehicle, Sedona pickup, complimentary photos"],
       url=FH.format(218228), badge="Most popular", fit="mixed groups, celebrations"),
  dict(name="The Terroir of the Verde Valley Wine Trail", duration="5 hours", meta="Private · All-inclusive", price="$375", price_num="375", price_note="per adult · 6+ $300",
       desc="Vineyards only. Four estate tastings chosen for your palate from Alcantara, DA Ranch, Javelina Leap, Oak Creek, Page Springs Cellars, Cove Mesa, Merkin and the Southwest Wine Center — exploring what volcanic soil and high-desert nights do to a grape.",
       includes=["Four wine tasting flights per adult", "Vineyard walk where the winery allows", "Private vehicle, Sedona pickup, complimentary photos"],
       url=FH.format(214370), badge="Wine lover's pick", fit="couples, wine enthusiasts"),
  dict(name="A Multi-Vineyard &amp; Winery Tasting Experience", duration="3 hours", meta="Private · All-inclusive", price="$225", price_num="225", price_note="per adult · 6+ $180",
       desc="Northern Arizona wine country in an afternoon: two flights at estate vineyards along Oak Creek in Page Springs and Cornville, red rocks the whole way. Best Wednesday through Friday.",
       includes=["Two wine tasting flights per adult", "Two of DA Ranch, Javelina Leap, Oak Creek Vineyard, Page Springs Cellars or Cove Mesa", "Private vehicle, Sedona pickup, complimentary photos"],
       url=FH.format(214320), fit="couples, first-timers, short stays"),
]

# (name, duration, retail, note, blurb, url)
WTOS_VINEYARD = [
  ("Alcantara Estate Vineyard Tasting Experience", "3 hrs", "$225", "per adult", "A VIP flight of estate wines and a charcuterie plate at the region's largest estate vineyard, where Oak Creek meets the Verde River.", FH.format(214307)),
  ("A Multi-Vineyard &amp; Winery Tasting Experience", "3 hrs", "$225", "per adult", "Two flights at two Page Springs–area vineyards. Our shortest wine country tour.", FH.format(214320)),
  ("A Taste of Camp Verde's Boutique Vineyards", "4 hrs", "$300", "per adult", "Salt Mine Wine and Clear Creek Vineyard — small-batch, estate-grown, open Saturday and Sunday.", FH.format(380854)),
  ("The Terroir of the Verde Valley Wine Trail", "5 hrs", "$375", "per adult", "Four vineyard tastings, chosen for your palate. Vineyards only.", FH.format(214370)),
  ("Views of Vineyards", "5 hrs", "$375", "per adult", "Alcantara and DA Ranch, two tastings and a charcuterie plate per person. Wednesday–Sunday.", FH.format(281356)),
  ("Date Night with Dinner", "5 hrs", "$777", "per couple", "A double tasting and a glass at DA Ranch, two boxes of Chocolita chocolate, and a full dinner at Up The Creek. Wednesday–Sunday at 3 p.m.", FH.format(282128)),
]
WTOS_TASTING_ROOMS = [
  ("A Taste of “Old Town” Cottonwood", "3 hrs", "$225", "per adult", "Two flights of wine, beer or spirits among Old Town's nine tasting rooms, from Rubrix to Belfry Brewery.", FH.format(214346)),
  ("The Flavors of Historic Jerome", "4 hrs", "$300", "per adult", "Three flights among the tasting rooms of a copper-mining town on Cleopatra Hill.", FH.format(214355)),
  ("Clarkdale Wine &amp; Vineyard Education Experience", "4 hrs", "$300", "per adult", "Southwest Wine Center, Bodega Pierce and Chateau Tumbleweed — student-made wines and the dean who teaches them. Thursday–Sunday; book 7 days ahead.", FH.format(380855)),
  ("Sedona Arizona Wine Tasting Experience", "5 hrs", "$375", "per adult", "Three flights and a charcuterie platter without leaving Sedona: Decanter, Vino Zona, The Art of Wine, Winery 1912 or Vino Di Sedona.", FH.format(216881)),
  ("An Evening in Old Town", "4 hrs", "$444", "per adult", "Three flights, dinner at Merkin Vineyards &amp; Hilltop Trattoria (or DA Vines) and a bottle of wine per couple in quaint Old Town Cottonwood.", FH.format(292881)),
  ("Rock Star Wine Tour", "5 hrs", "$555", "per adult", "Merkin, Caduceus and Four Eight Wineworks: three flights, three glasses and lunch with handmade pasta.", FH.format(234412)),
]
WTOS_ANYWHERE = [
  ("Sedona &amp; Verde Valley: Wine, Beer, Raw Chocolate &amp; Lunch", "5 hrs", "$444", "per adult", "Four flights, $11 in chocolate and lunch, anywhere in the Verde Valley. Our most popular tour.", FH.format(218228)),
  ("A Sedona Wine Lover's Experience", "7 hrs", "$525", "per adult", "Five flights anywhere in the Verde Valley — the full-day immersion.", FH.format(214374)),
  ("Sedona &amp; Wine Bachelorette Special Tour", "8 hrs", "$600", "per adult", "Our longest tour: six flights and lunch, anywhere in the Verde Valley, entirely on the group's schedule.", FH.format(214382)),
]
WTOS_THEMED = [
  ("Tarot &amp; Tastings: A Mystical Wine Experience", "5 hrs", "$375", "per adult", "Two flights, charcuterie, a bottle per couple and a tarot reading at Bohemian Dreamer.", "https://winetoursofsedona.com/tour-packages/"),
  ("Crystals, Creatures &amp; Cabernets", "5 hrs", "$375", "per adult", "Two flights, charcuterie, a bottle per couple and a spirit-animal and crystal reading.", "https://winetoursofsedona.com/tour-packages/"),
  ("Palette &amp; Pour: Wine Tasting and Painting Affair", "5 hrs", "$375", "per adult", "Two flights, charcuterie, a bottle per couple and a guided painting class at Bohemian Dreamer.", "https://winetoursofsedona.com/tour-packages/"),
  ("Sip, Sculpt &amp; Savor: Ceramic Souvenir Experience", "6 hrs", "$450", "per adult", "A ceramics class, two flights, charcuterie and a bottle per couple; The Art of Wine, Vino Di Sedona and Page Springs.", "https://winetoursofsedona.com/tour-packages/"),
  ("Terroir of Arizona &amp; Keepsake Shadowbox", "6 hrs", "$450", "per adult", "Three flights, charcuterie and a shadowbox workshop at Liquiterra Studio.", "https://winetoursofsedona.com/tour-packages/"),
  ("Sedona Vortex Visions: See, Feel, Create", "5 hrs", "$375", "per adult · child $150", "A scenic vortex tour and a shadowbox class at Liquiterra. Family-friendly.", "https://winetoursofsedona.com/tour-packages/"),
  ("Vines &amp; Vistas: Kayak and Wine Experience", "7 hrs", "$666", "per adult · child $300", "Kayak the Verde River, then wine and charcuterie, lunch and two more tastings at Alcantara, Pillsbury, Merkin and Cove Mesa.", "https://winetoursofsedona.com/tour-packages/"),
]
WTOS_OTHER = [
  ("Raw chocolate tours", "3 / 5 / 7 hrs", "$225 · $375 · $525", "per adult", "Charade, Expedition and Ruins &amp; Frenzy: 3, 8 or 11 pieces at Synergy Sedona, Living Chocolate and ChocolaTree. Children 15 and under free.", "https://winetoursofsedona.com/"),
  ("Micro-brewery tours", "4 / 4 / 6 hrs", "$300 · $300 · $450", "per adult", "Verde Valley, historic downtown Flagstaff, or the Arizona Hopful tour of every micro-brewery from Camp Verde to Flagstaff.", "https://winetoursofsedona.com/scenic-micro-brewery-tours/"),
  ("Sedona Red Rock Adventures", "3 – 12 hrs", "$225 – $750", "per adult", "Scenic, sunset, vortex, ancient ruins and the full-day Ruins &amp; Historic Jerome tour. Children 15 and under free on most.", "https://winetoursofsedona.com/"),
  ("Sedona Hiking Adventures", "3 – 4.5 hrs", "$333 · $444", "per adult", "Red Rock State Park guided hike with lunch, or the hike and 75-minute yoga combo.", "https://winetoursofsedona.com/"),
]

SIP_TOP = [
  dict(name="3-Hour Tasting Adventure", duration="3 hours", meta="Small group · Pay-as-you-go", price="$90", price_num="90", price_note="per person + 18% gratuity",
       desc="Sedona wine country without committing a whole day: Oak Creek Vineyard on the Page Springs corridor, then Cove Mesa Vineyard's tasting room in Cornville, where the owners are often pouring.",
       includes=["Local guide, water and pickup within Sedona city limits", "Fixed itinerary — you buy the flights you want at each stop", "Up to 14 guests; make it private for $100 per hour"],
       url="https://sipsedona.com/tours/3-hour-tasting-adventure/", badge="Best first taste", fit="first-timers, casual dates"),
  dict(name="4-Hour SIP &amp; Savor Tour", duration="4 hours", meta="Small group · Pay-as-you-go", price="$120", price_num="120", price_note="per person + 18% gratuity",
       desc="Three very different pours: Alcantara's riverside estate, bold wines and handmade pasta at Merkin Vineyards &amp; Hilltop Trattoria, and a social finish at Arizona Stronghold, the state's largest winemaker.",
       includes=["Local guide, water and pickup within Sedona city limits", "Fixed itinerary — tastings and food paid at each stop", "Up to 14 guests; make it private for $100 per hour"],
       url="https://sipsedona.com/tours/4-hour-sip-savor-tour/", badge="Foodie favorite", fit="foodies, small groups"),
  dict(name="5-Hour Wine, Beer &amp; Beyond Experience", duration="5 hours", meta="Small group · Pay-as-you-go", price="$150", price_num="150", price_note="per person + 18% gratuity",
       desc="The wider Verde Valley in one loop: DA Ranch or Alcantara to start, then Chateau Tumbleweed, Rubrix Wines and Vino Di Sedona — wine, beer and a little beyond.",
       includes=["Local guide, water and pickup within Sedona city limits", "Fixed itinerary — tastings paid at each stop", "Up to 14 guests; private for $500 (5 hours × $100)"],
       url="https://sipsedona.com/", fit="bachelorette parties, mixed groups"),
]

SWA_TOP = [
  dict(name="Chapels, Where the Rivers Meet, &amp; Wine", duration="3 hours", meta="Private · Pay-as-you-go", price="$150", price_num="150", price_note="per adult + 18% gratuity",
       desc="Alcantara Vineyard at the confluence of Oak Creek and the Verde River: eighty acres of vines, a wedding chapel, a private beach and cliff dwellings on the ridge — at your pace, with your guide.",
       includes=["Private vehicle and guide, exclusive to your group of 2–14", "Tastings paid directly at the winery", "Free pickup anywhere in Sedona"],
       url=SWA_BOOK, badge="Signature", fit="couples, small private groups"),
  dict(name="Ranching Turned Into Wine: Perspectives of DA Ranch", duration="4 hours", meta="Private · Pay-as-you-go", price="$250", price_num="250", price_note="per adult + 18% gratuity",
       desc="A former cattle ranch in Page Springs, now six acres of vines on 350 with springs, a pond and resident goats and donkeys. Includes a vineyard tour April–October or two glasses of wine November–March.",
       includes=["Private vehicle and guide, exclusive to your group", "Vineyard tour or two glasses of wine, by season", "Flexible stops before or after the ranch; closed Monday and Tuesday"],
       url=SWA_BOOK, fit="wine lovers, story lovers"),
  dict(name="Everybody's “ABT” — Adult Beverage Tour", duration="6 hours", meta="Private · Pay-as-you-go", price="$300", price_num="300", price_note="per adult + 18% gratuity",
       desc="Wine, beer, spirits, cider and mead anywhere in the Verde Valley and Flagstaff. The tour for a group where nobody drinks the same thing.",
       includes=["Private vehicle and guide", "Route built around your group's tastes", "Tastings paid directly at each stop"],
       url=SWA_BOOK, fit="mixed groups, celebrations"),
]

# ---------------------------------------------------------------- shared bits
def cta_block(title, text, primary_href, primary_label, phone_tel, phone_label):
    return f'''<section class="tight"><div class="wrap"><div class="cta">
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="actions"><a class="btn btn-primary" href="{primary_href}" rel="noopener">{primary_label}</a><a class="btn btn-ghost" href="tel:{phone_tel}">Call {phone_label}</a></div>
</div></div></section>'''

def pkg_list(items, cta="Book →"):
    return '<div class="packages">' + "".join(
        f'<div class="package"><h4>{n}</h4><div class="pp num">{p}<small> {pn}</small></div><p>{dur} · {d} <a href="{u}" rel="noopener">{cta}</a></p></div>'
        for n, dur, p, pn, d, u in items) + '</div>'

VINEYARDS = ["Alcantara Vineyard", "DA Ranch", "Page Springs Cellars", "Javelina Leap Vineyard", "Oak Creek Vineyards", "Cove Mesa Vineyard", "Salt Mine Wine", "Clear Creek Vineyards", "Echo Canyon Vineyard"]
TASTING_ROOMS = ["Merkin Vineyards &amp; Hilltop Trattoria", "Rubrix Wines", "Eureka Room", "Cellar 433", "Four Eight Wineworks", "Tantrum Wines", "Arizona Stronghold", "DA Vines &amp; Vineyard", "Belfry Brewery", "Southwest Wine Center", "Bodega Pierce", "Chateau Tumbleweed", "Caduceus Cellars", "Cabal Cellars", "Original Jerome Winery", "Passion Cellars", "VinoZona", "Coronado Vineyard", "The Art of Wine", "Vino Di Sedona", "Winery 1912", "Decanter Tasting Room", "Pillsbury Wine Company"]

# ---------------------------------------------------------------- HOME
HOME_FAQ_RAW = [
  ("Which Sedona wine tour company is right for me?",
   "It depends on how you like to travel. If you want everything handled — tastings included, a private vehicle for 2 to 14, hotel pickup — book <a href='wine-tours-of-sedona.html'>Wine Tours of Sedona</a>. If you'd rather keep the price down and enjoy a small-group van with other travelers, paying for tastings as you go, choose <a href='sip-sedona.html'>SIP Sedona</a>. If you want a private guide but the freedom to pick your own stops and pay tasting fees directly, <a href='sedona-wine-adventures.html'>Sedona Wine Adventures</a> was built for you. All three are ours, so the guides, vehicles and standards are the same."),
  ("How much does a Sedona wine tour cost?",
   "Our three divisions are priced by the hour: Wine Tours of Sedona about $75 per person per hour with tastings included, Sedona Wine Adventures $50 per hour with tastings paid as you go, and SIP Sedona $30 per hour on a small-group van. In practice that's $90 for a three-hour SIP Sedona tour, $150 for a three-hour private Sedona Wine Adventure, and $225 for a three-hour all-inclusive Wine Tours of Sedona tour. Full rates, group discounts and add-ons are on our <a href='pricing-and-policies.html'>pricing page</a>."),
  ("What are the most affordable wine tasting tours in Sedona?",
   "SIP Sedona's small-group tours start at $90 per person for three hours (plus 18% gratuity), with tasting fees paid at each winery so you only buy what you want to taste. Sedona Wine Adventures' private Sedona Quickie is $95 for 90 minutes at The Art of Wine. Both are locally owned and guided — not just transportation."),
  ("Where can I book a group wine tasting tour in Sedona with transportation?",
   "Right here. Wine Tours of Sedona and Sedona Wine Adventures run private vehicles for 2 to 14; SIP Sedona's vans and coaches carry 10 to 33; and for 15 or more we combine vehicles or put a step-on guide on your motorcoach — we've handled a dozen to a hundred-plus. Groups of six or more get 20% off Wine Tours of Sedona retail. Call <a href='tel:{TEL}'>{NUM}</a> and we'll narrow the details down in a few minutes before we put anything in writing."),
  ("Are tasting fees included in the price?",
   "With Wine Tours of Sedona, yes — every listed tour includes its tasting flights, and many include food. With SIP Sedona and Sedona Wine Adventures, tastings are pay-as-you-go at each stop, which keeps the base price lower and lets you choose your own flights. Those two divisions add an 18% gratuity to every tour; Wine Tours of Sedona adds it only for groups of six or more."),
  ("Do you pick up from hotels and vacation rentals?",
   "Yes. All three divisions pick up anywhere within Sedona city limits at no charge. Wine Tours of Sedona and Sedona Wine Adventures also pick up outside town for a flat fee — $75 in Cornville, Clarkdale and Cottonwood, $100 in Jerome, $200 in Flagstaff or Munds Park, $300 in Prescott. Day-trippers meet us at The Art of Wine at the Hyatt Piñon Pointe Shops, 101 N Hwy 89A."),
  ("Which wineries and tasting rooms do you visit?",
   "Every stop on the Verde Valley Wine Trail — eight vineyard locations and around twenty tasting rooms — plus seven micro-breweries and Flagstaff. Estate vineyards in Page Springs, Cornville and Camp Verde (Alcantara, DA Ranch, Page Springs Cellars, Javelina Leap, Oak Creek, Cove Mesa, Salt Mine, Clear Creek), the nine tasting rooms of Old Town Cottonwood, historic Jerome, Clarkdale's Southwest Wine Center, and Sedona's own tasting rooms. See the full list below."),
  ("Can I bring my dog on a Sedona wine tour?",
   "Yes, and you'll save 10%. Well-behaved, friendly dogs are welcome on Wine Tours of Sedona and Sedona Wine Adventures tours — use promo code DOGFRIENDLY when you book and we'll route the day through dog-friendly patios. Left yours at home? Our company guide dog, Ama, is happy to fill in."),
  ("How far in advance should I book?",
   "Weekends from March through May and September through November sell out first. Two to three weeks ahead is comfortable; for groups over ten or wedding weekends, give us a month. Some stops need lead time too — the Clarkdale education tour books seven days ahead. Last-minute? Call — we'll tell you honestly what's open."),
]

HOME_FAQ = [(q, tel(a)) for q, a in HOME_FAQ_RAW]

HOME_BODY = f'''
<section class="hero hero-dark"><div class="wrap">
  <div>
    <span class="eyebrow">Sip. Savor. Explore. · Sedona's most experienced wine tour company, since 2004</span>
    <h1>Sedona wine tours, three ways. <em>One family of local guides since 2004.</em></h1>
    <p class="lede">We're the local company behind <strong>Wine Tours of Sedona</strong>, <strong>SIP Sedona</strong> and <strong>Sedona Wine Adventures</strong>. Whether you want an all-inclusive private day, a small-group van to the Verde Valley's best tasting rooms, or a pay-as-you-go adventure that unfolds your way, one of our three divisions was built for exactly how you like to travel. We're not the biggest wine tour company in Sedona. We intend to be the best.</p>
    <div class="actions"><a class="btn btn-primary" href="#chooser">Find the right tour for me</a><a class="btn btn-ghost" href="tel:{PHONE_MAIN_TEL}">Call {PHONE_MAIN}</a></div>
    <div class="proof">
      <div><strong class="num">2004</strong>guiding Sedona wine country</div>
      <div><strong class="num">8 + 20</strong>vineyards &amp; tasting rooms on the trail</div>
      <div><strong class="num">2–33</strong>guests per vehicle</div>
      <div><strong>Best of the Best</strong>Readers' Choice 2023 &amp; 2024</div>
    </div>
  </div>
  <div class="emblem"><img src="images/swt-emblem.webp" alt="Sedona Wine Tours emblem: Cathedral Rock at sunset over Verde Valley vineyards, with Wine Tours of Sedona, SIP Sedona and Sedona Wine Adventures" width="900" height="900" fetchpriority="high"></div>
</div></section>

<!--SPECIALS-->
<!--CHOOSER-->
<section id="divisions"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Our divisions</span><h2>Which Sedona wine tour is right for you?</h2></div><p>Same guides, same standards, same red rocks. The difference is how much you'd like us to handle — and how you'd like to pay for it.</p></div>
  <div class="divisions">
    <article class="division brand-wtos">
      <img class="badge-img" src="images/badge-wtos.png" alt="Wine Tours of Sedona — Est. 2004 logo" width="96" height="96">
      <span class="tag">Wine Tours of Sedona</span>
      <h3>Luxury, all-inclusive, private</h3>
      <div class="fit">For couples and groups of 2–14 who want the whole day handled — tastings, food, photos and a private vehicle to yourselves.</div>
      <dl><dt>Format</dt><dd>Private, never grouped</dd><dt>Tastings</dt><dd>Included in the price</dd><dt>Rate</dt><dd class="num">About $75 per person per hour</dd><dt>From</dt><dd class="num">$225 per adult · 3 hrs</dd></dl>
      <div class="actions"><a class="btn btn-primary" href="wine-tours-of-sedona.html">Explore Wine Tours of Sedona</a><a class="btn btn-ghost" href="tel:{PHONE_WTOS_TEL}">{PHONE_WTOS}</a></div>
    </article>
    <article class="division brand-sip">
      <img class="badge-img" src="images/badge-sip.png" alt="SIP Sedona — Sip Socially logo" width="96" height="96">
      <span class="tag">SIP Sedona</span>
      <h3>Social, budget-friendly, group</h3>
      <div class="fit">For travelers who'd rather spend on wine than on the ride — a small-group van of up to 14, a fun guide, and tastings paid as you go.</div>
      <dl><dt>Format</dt><dd>Small group, fixed itineraries</dd><dt>Tastings</dt><dd>Pay at each stop</dd><dt>Rate</dt><dd class="num">$30 per person per hour</dd><dt>From</dt><dd class="num">$90 per person · 3 hrs</dd></dl>
      <div class="actions"><a class="btn btn-primary" href="sip-sedona.html">Explore SIP Sedona</a><a class="btn btn-ghost" href="tel:{PHONE_SIP_TEL}">{PHONE_SIP}</a></div>
    </article>
    <article class="division brand-swa">
      <img class="badge-img" src="images/badge-swa.png" alt="Sedona Wine Adventures — Exploring Arizona Wines logo" width="96" height="96">
      <span class="tag">Sedona Wine Adventures</span>
      <h3>Private, personalized, pay-as-you-go</h3>
      <div class="fit">For independent travelers who want a private guide and total control of the pace, the stops and the budget.</div>
      <dl><dt>Format</dt><dd>Private, groups of 2–14</dd><dt>Tastings</dt><dd>Pay directly at each winery</dd><dt>Rate</dt><dd class="num">$50 per person per hour</dd><dt>From</dt><dd class="num">$95 per adult · 90 min</dd></dl>
      <div class="actions"><a class="btn btn-primary" href="sedona-wine-adventures.html">Explore Sedona Wine Adventures</a><a class="btn btn-ghost" href="tel:{PHONE_SWA_TEL}">{PHONE_SWA}</a></div>
    </article>
  </div>
  <div class="compare"><table>
    <caption class="sr-only">Side-by-side comparison of our three Sedona wine tour divisions</caption>
    <thead><tr><th scope="col">Compare</th><th scope="col">Wine Tours of Sedona</th><th scope="col">SIP Sedona</th><th scope="col">Sedona Wine Adventures</th></tr></thead>
    <tbody>
      <tr><th scope="row">Best for</th><td class="c1">Anniversaries, proposals, first visits, guests who want zero decisions</td><td class="c2">Bachelorette parties, friends, solo travelers, value seekers</td><td class="c3">Repeat visitors, wine geeks, anyone who hates a fixed itinerary</td></tr>
      <tr><th scope="row">Vehicle</th><td class="c1">Private, climate-controlled, yours alone (2–14)</td><td class="c2">Shared van up to 14; private for $100 per hour</td><td class="c3">Private, exclusive to your group (2–14)</td></tr>
      <tr><th scope="row">Itinerary</th><td class="c1">Changes with your palate and interests</td><td class="c2">Fixed per tour</td><td class="c3">Changes with your palate and interests</td></tr>
      <tr><th scope="row">Tasting fees</th><td class="c1">Included</td><td class="c2">Paid at each stop</td><td class="c3">Paid at each stop</td></tr>
      <tr><th scope="row">Gratuity</th><td class="c1">18% added only for groups of 6+</td><td class="c2">18% added to every tour</td><td class="c3">18% added to every tour</td></tr>
      <tr><th scope="row">Add-ons</th><td class="c1">Lunch, dinner, dinner transport, scenic Sedona, charcuterie</td><td class="c2">None — keep it simple</td><td class="c3">Dinner transport; DOGFRIENDLY discount</td></tr>
      <tr><th scope="row">Pickup</th><td class="c1">Free in Sedona; flat fees beyond</td><td class="c2">Sedona city limits only</td><td class="c3">Free in Sedona; flat fees beyond</td></tr>
      <tr><th scope="row">Starting price</th><td class="c1 num">$225 / adult · 3 hrs</td><td class="c2 num">$90 / person · 3 hrs</td><td class="c3 num">$95 / adult · 90 min</td></tr>
    </tbody>
  </table></div>
  <p style="margin-top:1.2rem;color:var(--ink-2)">Every rate, discount and policy in one place: <a href="pricing-and-policies.html">Pricing &amp; policies</a>.</p>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Why guests choose us</span><h2>Why we're the best choice for a wine tour while you're in Sedona</h2></div><p>Twenty-two years, three brands, one promise: quality tour experiences, private and personalized, with complete flexibility throughout.</p></div>
  <div class="pillars">
    <div class="pillar"><div class="glyph">04</div><h3>Sedona's most experienced wine tour company</h3><p>We started Wine Tours of Sedona in 2004, before the Verde Valley had an AVA (it earned one in December 2021) and before most of today's tasting rooms existed. We know which cellar door to knock on.</p></div>
    <div class="pillar"><div class="glyph">G</div><h3>Guides, not drivers</h3><p>Every tour is led by a trained local guide who shares the geology, the vortex sites, the flora and fauna, Native American and pioneer history, a little western-movie lore and a lot of Sedona fun facts between pours.</p></div>
    <div class="pillar"><div class="glyph">VV</div><h3>The whole Verde Valley Wine Trail</h3><p>Every vineyard and tasting room from Camp Verde to Jerome, plus every micro-brewery to Flagstaff. We route by what you like, not by who pays us a commission.</p></div>
    <div class="pillar"><div class="glyph">Q</div><h3>Quality over quantity</h3><p>Three great tastings beat six rushed ones. Our itineraries leave room to linger, ask questions and buy a bottle you'll still be talking about at home.</p></div>
    <div class="pillar"><div class="glyph">P</div><h3>Door-to-door, safely and comfortably</h3><p>Free pickup anywhere in Sedona, fully enclosed climate-controlled vehicles with onboard WiFi and a cell booster, unlimited bottled water, and a sober professional at the wheel on the switchbacks to Jerome.</p></div>
    <div class="pillar"><div class="glyph">PH</div><h3>You go home with the photos</h3><p>Your guide shoots the day and sends complimentary digital photos and videos by email and text afterward — no phone juggling at the vineyard.</p></div>
  </div>
  <div class="promise">
    <div><span class="eyebrow">Our vision</span><p>We nurture community through relationships with other small, local Arizona businesses, and we share our passions for nature, wine, food and people. This is an experience, not just a tour — and every booking supports the local economy and Sedona's performing arts.</p></div>
    <div><span class="eyebrow">What we stand for</span><p>Customers first. Fun, win-win relationships. Humility with ambition. Honesty, integrity, candor and kindness. Quality over quantity. And sustainability — we call it <em>Breathe</em>.</p></div>
  </div>
</div></section>

<section id="packages"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Tour packages · Wine Tours of Sedona</span><h2>Every Wine Tours of Sedona package, with current prices</h2></div><p>Our all-inclusive flagship. Prices are retail per adult (21+), private to your party, with tasting flights, a climate-controlled vehicle, Sedona pickup and photos included. Groups of six or more save 20%; non-drinking adults save 25%; children 17 and under ride free.</p></div>
  <h3 style="margin-bottom:.5rem">Vineyard tours</h3>
  {pkg_list(WTOS_VINEYARD)}
  <h3 style="margin:2.5rem 0 .5rem">Tasting-room tours</h3>
  {pkg_list(WTOS_TASTING_ROOMS)}
  <h3 style="margin:2.5rem 0 .5rem">Anywhere in the Verde Valley</h3>
  {pkg_list(WTOS_ANYWHERE)}
  <h3 style="margin:2.5rem 0 .5rem">Wine + experience packages</h3>
  {pkg_list(WTOS_THEMED, "Details →")}
  <h3 style="margin:2.5rem 0 .5rem">Beyond wine</h3>
  {pkg_list(WTOS_OTHER, "Details →")}
  <p style="margin-top:1.5rem;color:var(--ink-2)">Add lunch ($55) or dinner ($111) to any wine tour, a two-hour Scenic Sedona extension ($99 per person at booking), or a charcuterie board with an extra tasting ($99). Gift cards available in any amount. <a href="pricing-and-policies.html">All add-ons and policies →</a></p>
  <p><a class="btn btn-ghost" href="{WTOS_BOOK}" rel="noopener">Book on winetoursofsedona.com</a></p>
</div></section>

<section id="cellar" class="brand-wtos" style="background:linear-gradient(135deg,var(--syrah-soft),var(--ground))"><div class="wrap split">
  <div class="art">“The tasting room comes to you.”<span>Photo: guide pouring a flight on a vacation-rental patio at golden hour — see shot list</span></div>
  <div>
    <span class="eyebrow">New · Private in-home wine tasting</span>
    <h2>The Sedona Cellar Experience</h2>
    <p class="lede">Some evenings you don't want to go anywhere. Our guide brings a curated flight of Arizona wines to your Sedona vacation rental or resort suite and walks your group through them — the stories, the soils, the winemakers — while the red rocks do the lighting.</p>
    <p>Perfect for a first night in town, a rehearsal-dinner wind-down, a girls' weekend that doesn't want to get back in a van, or a corporate group who'd rather taste in the boardroom than the tasting room.</p>
    <p><a class="btn btn-primary" href="{FH.format(752593)}" rel="noopener">Book The Sedona Cellar Experience</a> <a class="btn btn-ghost" href="tel:{PHONE_WTOS_TEL}">Ask us: {PHONE_WTOS}</a></p>
  </div>
</div></section>

<section><div class="wrap split">
  <div>
    <span class="eyebrow">Groups · Corporate · Weddings</span>
    <h2>Bring everyone. We'll bring the vehicles.</h2>
    <p class="lede">Bachelorette weekends, company retreats, family reunions and wedding parties are what we do best — from a private vehicle for two to a 33-passenger coach, and from a dozen guests to a hundred-plus with multiple vehicles or a step-on guide.</p>
    <ul style="color:var(--ink-2)">
      <li>Groups of 6–14: 20% off every Wine Tours of Sedona tour</li>
      <li>Wedding guest shuttles between ceremony, reception and lodging — through SIP Sedona, from $250 per hour</li>
      <li>Step-on guide service for groups arriving on their own motorcoach, at 20% off</li>
      <li>Corporate days with private tastings, lunch and a route that leaves time to talk</li>
    </ul>
    <p><a class="btn btn-primary" href="groups-corporate-weddings.html">Plan a group tour or event</a></p>
  </div>
  <div class="fleet">
    <div><strong class="num">2–14</strong><span>Private vehicles</span><em>Wine Tours of Sedona · Sedona Wine Adventures</em></div>
    <div><strong class="num">10</strong><span>Luxury van</span><em>$250 / hour</em></div>
    <div><strong class="num">14</strong><span>Executive van</span><em>$250 / hour</em></div>
    <div><strong class="num">25–30</strong><span>Coach bus</span><em>$400 / hour</em></div>
    <div><strong class="num">33</strong><span>Coach bus</span><em>$400 / hour</em></div>
  </div>
</div></section>

<section id="wineries" style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Where we go</span><h2>The Sedona wineries and Verde Valley vineyards we visit</h2></div><p>The Verde Valley became Arizona's newest American Viticultural Area in December 2021 for good reason: volcanic soils, high-desert days and cool nights that grow serious Rhône, Spanish and Italian varietals. Eight vineyard locations, about twenty tasting rooms, seven micro-breweries — we know all of them.</p></div>
  <h3 style="margin-bottom:.6rem">Estate vineyards</h3>
  <div class="wineries">{"".join(f"<span>{w}</span>" for w in VINEYARDS)}</div>
  <h3 style="margin:1.6rem 0 .6rem">Tasting rooms, breweries &amp; more</h3>
  <div class="wineries">{"".join(f"<span>{w}</span>" for w in TASTING_ROOMS)}</div>
  <div class="regions">
    <div class="region"><h3>Page Springs &amp; Cornville</h3><p>Where northern Arizona's modern wine story began — estate vineyards along Oak Creek, twenty minutes from Sedona. DA Ranch's Capra is a house favorite.</p></div>
    <div class="region"><h3>Camp Verde</h3><p>Alcantara's eighty acres at the river confluence, plus boutique Salt Mine Wine and Clear Creek Vineyards, open Friday to Sunday.</p></div>
    <div class="region"><h3>Old Town Cottonwood</h3><p>Nine tasting rooms on five quaint, walkable historic blocks, Merkin's handmade pasta, and three distilleries arriving.</p></div>
    <div class="region"><h3>Jerome &amp; Clarkdale</h3><p>A copper-mining town on Cleopatra Hill with seven tasting rooms, and Yavapai College's Southwest Wine Center, where students grow and make the wine.</p></div>
  </div>
  <p style="margin-top:1.6rem"><a class="btn btn-ghost" href="sedona-wineries-and-vineyards.html">Our guide to every winery and vineyard near Sedona</a></p>
</div></section>

<!--REVIEWS-->
<!--SOCIAL-->

<section id="faq" style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Questions &amp; answers</span><h2>Planning a Sedona wine tour? Start here.</h2></div></div>
  {faq_html(HOME_FAQ)}
</div></section>

<section id="contact"><div class="wrap contact-grid">
  <div>
    <span class="eyebrow">Talk to a local</span>
    <h2>Not sure which division? Call us.</h2>
    <p class="lede">A five-minute conversation beats twenty emails. Tell us who's coming, when, and what you like to drink, and we'll match you to the right tour — or build one.</p>
    <div class="lines">
      <div><span class="dot" style="background:var(--ink)"></span><strong>Sedona Wine Tours (all divisions)</strong><a href="tel:{PHONE_MAIN_TEL}">{PHONE_MAIN}</a></div>
      <div><span class="dot" style="background:var(--syrah)"></span><strong>Wine Tours of Sedona</strong><a href="tel:{PHONE_WTOS_TEL}">{PHONE_WTOS}</a></div>
      <div><span class="dot" style="background:var(--cathedral)"></span><strong>SIP Sedona</strong><a href="tel:{PHONE_SIP_TEL}">{PHONE_SIP}</a></div>
      <div><span class="dot" style="background:var(--verde)"></span><strong>Sedona Wine Adventures</strong><a href="tel:{PHONE_SWA_TEL}">{PHONE_SWA}</a></div>
    </div>
    <p style="margin-top:1.2rem;color:var(--ink-2)">{ADDRESS} · Mail: P.O. Box 1280, Sedona, AZ 86339<br>Day-trip meeting point: The Art of Wine, Hyatt Piñon Pointe Shops, 101 N Hwy 89A, Sedona<br>Tours depart daily; office hours 8 a.m. – 6 p.m. Arizona time.</p>
    <img src="images/three-divisions-banner.jpg" alt="Sedona Wine Tours — Wine Tours of Sedona, SIP Sedona and Sedona Wine Adventures logos over the red rocks" width="650" height="360" loading="lazy" style="border-radius:12px;margin-top:1rem;border:1px solid var(--line)">
  </div>
  <form name="contact" method="POST" action="/contact.php">
    <input type="text" name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
    <label>Your name<input type="text" name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label>
    <label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
    <label>Which division interests you?<select name="division"><option>Not sure — help me choose</option><option>Wine Tours of Sedona (private, all-inclusive)</option><option>SIP Sedona (small group, pay-as-you-go)</option><option>Sedona Wine Adventures (private, pay-as-you-go)</option><option>Group, corporate or wedding</option><option>The Sedona Cellar Experience (in-home)</option></select></label>
    <label>Dates, group size and what you'd love to taste<textarea name="message" rows="4" required></textarea></label>
    <button class="btn btn-primary" type="submit">Send message</button>
  </form>
</div></section>
'''

HOME = dict(
  slug="index.html",
  title="Sedona Wine Tours | Wine Tasting Tours, Private, Group &amp; Packages",
  description="Sedona wine tours since 2004: private all-inclusive, small-group and pay-as-you-go wine tasting tours to Verde Valley wineries and vineyards. Compare packages and prices. (928) 504-2445.",
  body=HOME_BODY,
  schema=[ORG, faq_schema(HOME_FAQ), {"@context":"https://schema.org","@type":"WebSite","url":SITE,"name":"Sedona Wine Tours","publisher":{"@id":f"{SITE}/#org"}}],
)

# ---------------------------------------------------------------- WTOS
WTOS_FAQ_RAW = [
  ("What does “all-inclusive” mean on a Wine Tours of Sedona tour?", "The listed price covers your private climate-controlled vehicle and guide, free pickup anywhere in Sedona, every tasting flight named in the tour, unlimited bottled water, complimentary photos and videos, and — on tours that say so — charcuterie, lunch or dinner. You bring your appetite and a credit card for the bottles you'll want to take home. If a busy tasting room means fewer stops than advertised, ask your guide for an extra flight or glass instead."),
  ("Is the tour really private?", "Yes. Every Wine Tours of Sedona reservation is private to your party of 2 to 14. You are never grouped with strangers, and the itinerary bends to your palate and interests. Fifteen or more? Call %s and we'll bring more vehicles." % PHONE_WTOS),
  ("How does group pricing work?", "Groups of six to fourteen adults take 20% off retail on every Wine Tours of Sedona tour, and an 18% gratuity is added for groups of six or more. Non-drinking adults are 25% off retail. Children 17 and under are free, though we don't recommend wine tours for kids. One 10% discount (military, AAA, seniors 65+, returning guests, or the DOGFRIENDLY code) can be applied instead of, not on top of, the group rate — whichever is higher."),
  ("What can we add on?", "Lunch for $55 per person (one dish, whole party) or dinner for $111 (appetizer, entrée, dessert and a beverage or flight); a two-hour Scenic Sedona extension for $99 per person if added at booking; a charcuterie board with an additional tasting and 75 more minutes for $99; and Transportation To &amp; From Dinner, a flat $150 for the group, so nobody drives after the tour."),
  ("How is Wine Tours of Sedona different from SIP Sedona?", "Wine Tours of Sedona is private and all-inclusive at about $75 per person per hour; SIP Sedona is a small-group van at $30 per hour where tastings are paid as you go. Same owners, same guides, different formats. <a href='index.html#divisions'>Our comparison</a> lays it out side by side."),
]

WTOS_FAQ = [(q, tel(a, PHONE_WTOS_TEL, PHONE_WTOS)) for q, a in WTOS_FAQ_RAW]

WTOS_BODY = f'''
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Division 1 of 3 · The original, since 2004</span>
    <div class="h1-row"><img src="images/badge-wtos.png" alt="Wine Tours of Sedona logo, established 2004" width="120" height="120"><h1>Wine Tours of Sedona</h1></div>
    <p class="lede">Luxury · All-inclusive · Private. The flagship we founded in 2004, and the way most of our guests first fell for Arizona wine: a private vehicle for 2 to 14, a guide who knows every winemaker by name, every tasting already paid for, and nothing to think about but the next pour.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem"><a class="btn btn-primary" href="{WTOS_BOOK}" rel="noopener">Book on winetoursofsedona.com</a><a class="btn btn-ghost" href="tel:{PHONE_WTOS_TEL}">Call {PHONE_WTOS}</a></div>
  </div>
  <div class="facts">
    <div><span>Format</span><strong>Private to your party, 2–14</strong></div>
    <div><span>Tastings</span><strong>Included, always</strong></div>
    <div><span>Rate</span><strong class="num">~$75 pp / hour · from $225</strong></div>
    <div><span>Groups of 6+</span><strong>20% off retail</strong></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Most popular</span><h2>Our three most-booked Wine Tours of Sedona tours</h2></div><p>Retail per adult; the 6+ price shown is the 20% group rate before the 18% group gratuity. We refresh this list monthly from FareHarbor.</p></div>
  <div class="tours">{"".join(tour_card(t) for t in WTOS_TOP)}</div>
  <p style="margin-top:1.5rem"><a class="btn btn-ghost" href="index.html#packages">See all Wine Tours of Sedona packages and prices</a></p>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Why this division</span><h2>Why Wine Tours of Sedona is the luxury choice</h2></div></div>
  <div class="pillars">
    <div class="pillar"><div class="glyph">1</div><h3>Never grouped with strangers</h3><p>Your vehicle, your pace, your playlist. Proposals have happened on our tours; so have quiet anniversaries where nobody said a word for ten minutes at Alcantara's river bend.</p></div>
    <div class="pillar"><div class="glyph">2</div><h3>Quality over quantity</h3><p>We'd rather you remember three wines than forget six. Tastings are unhurried and, wherever the winery allows, come with a walk through the vines or a look in the barrel room.</p></div>
    <div class="pillar"><div class="glyph">3</div><h3>Food that matches the wine</h3><p>Charcuterie at the first stop, handmade pasta at Merkin's Hilltop Trattoria, dinner at Up The Creek across the water from DA Ranch — Date Night and An Evening in Old Town are dinner reservations with a wine tour attached.</p></div>
    <div class="pillar"><div class="glyph">4</div><h3>Guides who've been here since the beginning</h3><p>Jim founded the company in 2004 and still guides. Juan Manuel and Ed Benoit are the names guests write about in reviews. You'll understand why by the second stop.</p></div>
    <div class="pillar"><div class="glyph">5</div><h3>Beyond wine</h3><p>The same team runs our raw-chocolate, micro-brewery, vortex, ancient-ruins and hiking tours, and combines them into experience packages — tarot, painting, ceramics, kayaking — you won't find anywhere else in Sedona.</p></div>
    <div class="pillar"><div class="glyph">6</div><h3>Your bottles get home safely</h3><p>Ask your guide about a Canyon Cooler for the drive back to Phoenix or the flight home. Arizona wine deserves better than a hot trunk.</p></div>
  </div>
</div></section>

<!--REVIEWS-->
<!--SOCIAL-->
<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Questions</span><h2>Wine Tours of Sedona, answered</h2></div></div>
  {faq_html(WTOS_FAQ)}
</div></section>
{cta_block("Ready for the all-inclusive day?", "Browse every tour and book instantly on the Wine Tours of Sedona site, or call and we'll build something custom.", "https://www.winetoursofsedona.com", "Visit winetoursofsedona.com", PHONE_WTOS_TEL, PHONE_WTOS)}
'''

WTOS = dict(
  slug="wine-tours-of-sedona.html", brand_class="brand-wtos",
  title="Private Sedona Wine &amp; Vineyard Tours | Wine Tours of Sedona",
  description="Private, all-inclusive Sedona wine tours and Verde Valley vineyard tours since 2004. Tastings included, free Sedona pickup, private vehicle for 2–14. From $225; groups of 6+ save 20%. (928) 224-2991.",
  body=WTOS_BODY,
  schema=[breadcrumbs([("Home","index.html"),("Wine Tours of Sedona","wine-tours-of-sedona.html")]), offers_schema("Wine Tours of Sedona", WTOS_TOP, "https://www.winetoursofsedona.com"), faq_schema(WTOS_FAQ)],
)

# ---------------------------------------------------------------- SIP
SIP_FAQ_RAW = [
  ("How does pay-as-you-go tasting work?", "Your SIP Sedona ticket covers the guide, the ride, pickup within Sedona city limits and bottled water, plus an 18% gratuity added at checkout. At each winery you buy the flight or glass you want — usually $12 to $25 — so you're never paying for a tasting you'd have skipped."),
  ("Will I be with other people?", "Usually — SIP Sedona tours are small-group, up to 14 guests, and plenty of people leave with new friends. Want the van to yourselves? Make any tour private for a flat $100 per hour: $300 for the 3-hour, $500 for the 5-hour."),
  ("Where do you pick up?", "Hotels and vacation rentals within Sedona city limits. Staying outside town? Meet us at The Art of Wine at the Hyatt Piñon Pointe Shops, 101 N Hwy 89A."),
  ("Can I add lunch or change the route?", "SIP Sedona keeps it simple: itineraries are fixed per tour and there are no add-ons. If you want lunch, dinner or a custom route, our <a href='wine-tours-of-sedona.html'>Wine Tours of Sedona</a> and <a href='sedona-wine-adventures.html'>Sedona Wine Adventures</a> divisions do exactly that."),
  ("Can SIP Sedona shuttle our wedding guests?", "Yes — coordinated pickups between hotels, ceremony and reception in vans and coaches from 10 to 33 passengers, anywhere in the Verde Valley: $250 per hour for the 10- and 14-passenger vans, $400 per hour for the 25-, 30- and 33-passenger coaches. Call <a href='tel:{TEL}'>{NUM}</a> for a quote."),
]

SIP_FAQ = [(q, tel(a, PHONE_SIP_TEL, PHONE_SIP)) for q, a in SIP_FAQ_RAW]

SIP_BODY = f'''
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Division 2 of 3 · Social &amp; group tours</span>
    <div class="h1-row"><img src="images/badge-sip.png" alt="SIP Sedona logo — Sip Socially" width="120" height="120"><h1>SIP Sedona</h1></div>
    <p class="lede">Social · Budget-friendly · Group. The small-group van we built for travelers who'd rather spend their money on wine than on the ride — $30 per person per hour, fixed itineraries to the Verde Valley's best stops, and the wedding and special-event transportation that keeps a whole guest list together.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem"><a class="btn btn-primary" href="{SIP_BOOK}" rel="noopener">Book on sipsedona.com</a><a class="btn btn-ghost" href="tel:{PHONE_SIP_TEL}">Call {PHONE_SIP}</a></div>
  </div>
  <div class="facts">
    <div><span>Format</span><strong>Small group, up to 14</strong></div>
    <div><span>Tastings</span><strong>Pay at each stop</strong></div>
    <div><span>Rate</span><strong class="num">$30 pp / hour · from $90</strong></div>
    <div><span>Make it private</span><strong class="num">$100 per hour</strong></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Most popular</span><h2>Our three most-booked SIP Sedona tours</h2></div><p>Prices are per person, 21+, plus an 18% gratuity. Tastings and food are purchased at each stop, so the price you see is the price of the ride and the guide.</p></div>
  <div class="tours">{"".join(tour_card(t) for t in SIP_TOP)}</div>
  <p style="margin-top:1.5rem;color:var(--ink-2)">Also on the schedule: the <strong>8-Hour SIP All Day Experience</strong>, $240 — seven stops from The Art of Wine and Winery 1912 through Javelina Leap, Cove Mesa, Alcantara and Cellar 433 to Arizona Stronghold. <a href="https://sipsedona.com/tours/8-hour-sip-all-day-experience/" rel="noopener">Details →</a></p>
</div></section>

<section id="events" style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Wedding &amp; special event transportation</span><h2>Keep your guests together, on time and stress-free</h2></div><p>The same vans and coaches that run our wine tours are available by the hour, anywhere in the Verde Valley, for weddings, elopements, corporate retreats, milestone birthdays and airport transfers from Phoenix Sky Harbor or Flagstaff.</p></div>
  <div class="fleet">
    <div><strong class="num">10</strong><span>Luxury van</span><em>$250 / hour</em></div>
    <div><strong class="num">14</strong><span>Executive van</span><em>$250 / hour</em></div>
    <div><strong class="num">25</strong><span>Coach bus</span><em>$400 / hour</em></div>
    <div><strong class="num">30</strong><span>Coach bus</span><em>$400 / hour</em></div>
    <div><strong class="num">33</strong><span>Coach bus</span><em>$400 / hour</em></div>
  </div>
  <div class="split" style="margin-top:2.5rem">
    <div class="panel">
      <h3>Weddings &amp; elopements</h3>
      <ul><li>Coordinated pickups between hotels, ceremony and reception</li><li>Return runs at the end of the night so nobody drives</li><li>Custom routes for a red-rock photo stop between venues</li><li>Locally based drivers who know every resort driveway in Sedona</li></ul>
      <a class="btn btn-primary" href="https://sipsedona.com/all-shuttles/" rel="noopener">Request a wedding shuttle quote</a>
    </div>
    <div class="panel">
      <h3>Corporate retreats &amp; celebrations</h3>
      <ul><li>Bachelor and bachelorette weekends in one vehicle</li><li>Team offsites with a wine or brewery afternoon built in</li><li>Conference and resort transfers, Phoenix and Flagstaff airports</li><li>Flexible hourly booking — add a Jerome stop, a sunset viewpoint, a dinner drop</li></ul>
      <a class="btn btn-ghost" href="groups-corporate-weddings.html">Plan a group day</a>
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Why this division</span><h2>Why SIP Sedona is the smart, social choice</h2></div></div>
  <div class="pillars">
    <div class="pillar"><div class="glyph">$</div><h3>Value without the trade-offs</h3><p>Same owners and guides as our luxury division at $30 per person per hour. You give up the private vehicle and the prepaid flights — and keep the local knowledge, the safe ride and the good company.</p></div>
    <div class="pillar"><div class="glyph">14</div><h3>Small group, not a bus tour</h3><p>Fourteen guests at most, a guide who knows everyone's name by the second stop, and vans with WiFi and a cell booster for the photos you'll want to post.</p></div>
    <div class="pillar"><div class="glyph">7</div><h3>Stops worth the seat</h3><p>Oak Creek, Cove Mesa, Alcantara, Merkin, Arizona Stronghold, Chateau Tumbleweed, Winery 1912, Cellar 433 — every itinerary is built from the Verde Valley's best-loved rooms.</p></div>
    <div class="pillar"><div class="glyph">21+</div><h3>Built for celebrations</h3><p>Bachelorette parties are our specialty. Bring the group, we'll bring the playlist, and the wineries will bring the sparkling. Book the whole van and it's yours.</p></div>
  </div>
</div></section>

<!--REVIEWS-->
<!--SOCIAL-->
<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Questions</span><h2>SIP Sedona, answered</h2></div></div>
  {faq_html(SIP_FAQ)}
</div></section>
{cta_block("Grab a seat — or the whole van.", "Scheduled tours book instantly on sipsedona.com. For weddings, events and private vans, call and we'll sort the details in one conversation.", SIP_BOOK, "Visit sipsedona.com", PHONE_SIP_TEL, PHONE_SIP)}
'''

SIP = dict(
  slug="sip-sedona.html", brand_class="brand-sip",
  title="Sedona Wine Tour Bus &amp; Group Shuttle | SIP Sedona Wine Tours",
  description="Affordable small-group Sedona wine tours from $90 on a shared wine tour bus, pay-as-you-go tastings, plus Sedona shuttle service for weddings, events and groups of 10–33. (928) 308-5166.",
  body=SIP_BODY,
  schema=[breadcrumbs([("Home","index.html"),("SIP Sedona","sip-sedona.html")]), offers_schema("SIP Sedona", SIP_TOP, "https://sipsedona.com"), faq_schema(SIP_FAQ),
          {"@context":"https://schema.org","@type":"Service","name":"Wedding and special event transportation in Sedona","provider":{"@type":"Organization","name":"SIP Sedona","url":"https://sipsedona.com","telephone":PHONE_SIP_TEL},"areaServed":"Sedona and the Verde Valley, Arizona","serviceType":"Wedding shuttle, event shuttle, group transportation, airport transfer","offers":{"@type":"Offer","priceCurrency":"USD","price":"250","description":"10–14 passenger vans $250 per hour; 25–33 passenger coaches $400 per hour"}}],
)

# ---------------------------------------------------------------- SWA
SWA_FAQ = [
  ("What does pay-as-you-go mean on a private tour?", "You pay us $50 per person per hour for the private vehicle and your guide's time, plus an 18% gratuity. Tasting fees and any meals you pay directly at each winery. It keeps the tour price honest and lets you decide, glass by glass, where the money goes."),
  ("Can we change the plan mid-tour?", "That's the point. Loved the second winery? Stay. Bored of reds? Your guide knows where the sparkling is. The itinerary changes with your palate and interests — it's a suggestion, not a contract."),
  ("Is Sedona Wine Adventures the same company as Wine Tours of Sedona?", "Yes — same locally owned group, same standards, different format. Wine Tours of Sedona is all-inclusive at about $75 per hour; Sedona Wine Adventures is private and pay-as-you-go at $50. <a href='index.html#divisions'>Compare the three divisions.</a>"),
  ("Can I bring my dog, and what about dinner?", "Dogs are welcome — well-behaved and friendly — and the DOGFRIENDLY promo code takes 10% off. Lunch and dinner add-ons aren't offered on this division, but Transportation To &amp; From Dinner is: a flat $150 for the group, so you can book a table for the end of the tour and let us drive."),
  ("How short can a tour be?", "Ninety minutes. A Sedona Quickie is $95 — one great stop at The Art of Wine for guests with a dinner reservation or a tight itinerary."),
]

SWA_BODY = f'''
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Division 3 of 3 · Private &amp; off the beaten path</span>
    <div class="h1-row"><img src="images/badge-swa.png" alt="Sedona Wine Adventures logo" width="120" height="120"><h1>Sedona Wine Adventures</h1></div>
    <p class="lede">Private · Personalized · Pay-as-you-go. This isn't a cookie-cutter route. Every Sedona Wine Adventures tour is exclusive to your group of 2 to 14 and unfolds your way — you decide the pace, the stops and how long to linger, and you pay for tastings and meals directly, so you're in control of the experience and the budget.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem"><a class="btn btn-primary" href="{SWA_BOOK}" rel="noopener">Reserve on sedonawineadventures.com</a><a class="btn btn-ghost" href="tel:{PHONE_SWA_TEL}">Call {PHONE_SWA}</a></div>
  </div>
  <div class="facts">
    <div><span>Format</span><strong>Private, exclusive to your group</strong></div>
    <div><span>Tastings</span><strong>Paid directly at each winery</strong></div>
    <div><span>Rate</span><strong class="num">$50 pp / hour · from $95</strong></div>
    <div><span>Dogs</span><strong>Welcome — 10% off with DOGFRIENDLY</strong></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Most popular</span><h2>Our three most-booked Sedona Wine Adventures</h2></div><p>Prices are per adult plus an 18% gratuity; tastings and meals are paid directly at each stop.</p></div>
  <div class="tours">{"".join(tour_card(t) for t in SWA_TOP)}</div>
  <p style="margin-top:1.5rem;color:var(--ink-2)">Also popular: <strong>Verde Valley Spirits</strong> (5 hrs, $250) — Spirits &amp; Spice, Redwall Distillery, the Southwest Wine Center and Old Town Cottonwood's new distilleries — and <strong>A Sedona Quickie</strong> (90 min, $95) at The Art of Wine. <a href="https://www.sedonawineadventures.com/adventures/" rel="noopener">All adventures →</a></p>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Why this division</span><h2>Why independent travelers choose Sedona Wine Adventures</h2></div></div>
  <div class="pillars">
    <div class="pillar"><div class="glyph">→</div><h3>Freedom, with a designated driver</h3><p>The private-tour feeling of driving yourselves through wine country — without anyone having to spit.</p></div>
    <div class="pillar"><div class="glyph">$</div><h3>Honest pricing</h3><p>You see exactly what the ride costs ($50 per person per hour) and exactly what each tasting costs. No bundled flights you didn't want.</p></div>
    <div class="pillar"><div class="glyph">?</div><h3>Guides who love a detour</h3><p>Our guides keep things fun, engaging and effortlessly informative — Arizona wine country's stories, the volcanic soil under the vines, and the tasting room that isn't on the map yet.</p></div>
    <div class="pillar"><div class="glyph">2+</div><h3>Right-sized for two</h3><p>Couples and small groups get the same private treatment as a party of fourteen. Ninety minutes or six hours; it's your afternoon.</p></div>
  </div>
</div></section>

<!--REVIEWS-->
<!--SOCIAL-->
<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Questions</span><h2>Sedona Wine Adventures, answered</h2></div></div>
  {faq_html(SWA_FAQ)}
</div></section>
{cta_block("Your afternoon, your route.", "Reserve online or call — tell us what you like and we'll suggest a starting point. You can change your mind at every stop.", "https://www.sedonawineadventures.com", "Visit sedonawineadventures.com", PHONE_SWA_TEL, PHONE_SWA)}
'''

SWA = dict(
  slug="sedona-wine-adventures.html", brand_class="brand-swa",
  title="Private Wine Tasting Tours Sedona | Sedona Wine Adventures",
  description="Private Arizona wine tasting tours from Sedona — Alcantara, DA Ranch, Verde Valley spirits — with your own guide and vehicle for 2–14, pay-as-you-go tastings, from $95. (928) 366-8476.",
  body=SWA_BODY,
  schema=[breadcrumbs([("Home","index.html"),("Sedona Wine Adventures","sedona-wine-adventures.html")]), offers_schema("Sedona Wine Adventures", SWA_TOP, "https://www.sedonawineadventures.com"), faq_schema(SWA_FAQ)],
)

# ---------------------------------------------------------------- GROUPS
GROUPS_FAQ_RAW = [
  ("How large a group can you take on a Sedona wine tour?", "Two to fourteen in a private vehicle, ten to thirty-three in a SIP Sedona van or coach, and larger with multiple vehicles running the same itinerary — we've handled a dozen to a hundred-plus. Groups of fifteen or more with their own motorcoach can use our step-on guide service at a 20% discount, or we can provide the transportation for $3,000 plus the per-person rate."),
  ("What's the group discount?", "Groups of six to fourteen adults get 20% off retail on every Wine Tours of Sedona tour; an 18% gratuity is added for six or more. For example, the Terroir of the Verde Valley Wine Trail is $375 retail and $300 per adult for a group, $354 with gratuity. Non-drinking adults are 25% off. For fifteen or more, call (928) 224-2991."),
  ("Do you do corporate wine tours and team building?", "Yes. A typical corporate day is a private vehicle or coach, a welcome tasting with charcuterie, lunch at Merkin's Hilltop Trattoria or a vineyard picnic, and a route that leaves time for the group to actually talk. We invoice the company and handle dietary requests."),
  ("What's the best Sedona bachelorette wine tour?", "For most parties it's SIP Sedona's 5-Hour Wine, Beer &amp; Beyond booked as a private van ($500 plus tastings and gratuity), or Wine Tours of Sedona's 8-hour Bachelorette Special ($600 retail, $480 per adult for six or more — six flights and lunch included) if you want everything prepaid. Call us and we'll match the format to the group."),
  ("Can you shuttle wedding guests between venues?", "That's SIP Sedona's specialty: coordinated pickups from Sedona hotels and rentals to ceremony and reception, with return runs at night. Vans are $250 per hour and coaches $400 per hour, anywhere in the Verde Valley."),
  ("How do we book a group?", "Call us first at <a href='tel:{TEL}'>{NUM}</a>. In five minutes we'll pin down dates, headcount, vehicle and format, then confirm everything by email so there's nothing to misread. Payment is due in full at booking, and every guest signs our online waiver before the day."),
]

GROUPS_FAQ = [(q, tel(a)) for q, a in GROUPS_FAQ_RAW]

GROUPS_BODY = f'''
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Groups · Corporate · Bachelorette · Weddings</span>
    <h1>Group wine tours and event transportation in Sedona</h1>
    <p class="lede">We're the only Sedona wine tour company that can seat a party of two or a party of thirty-three — and route either one through the Verde Valley's best tasting rooms with a guide who makes the day. Corporate retreats, bachelorette weekends, reunions and wedding parties are what our three divisions were built to share.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem"><a class="btn btn-primary" href="tel:{PHONE_MAIN_TEL}">Call {PHONE_MAIN} to plan</a><a class="btn btn-ghost" href="index.html#contact">Send group details</a></div>
  </div>
  <div class="facts">
    <div><span>Group discount</span><strong>20% off for 6–14 adults</strong></div>
    <div><span>Vehicles</span><strong>Private 2–14 · vans &amp; coaches to 33</strong></div>
    <div><span>Step-on guide</span><strong>20% off for 15+ with own coach</strong></div>
    <div><span>Planning</span><strong>One phone call, then email</strong></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">How we match groups</span><h2>Pick the format, we'll pick the vehicle</h2></div></div>
  <div class="divisions">
    <article class="division brand-wtos"><img class="badge-img" src="images/badge-wtos.png" alt="Wine Tours of Sedona logo" width="96" height="96"><span class="tag">Wine Tours of Sedona</span><h3>All-inclusive private groups</h3><div class="fit">Best for corporate days and celebrations where one person is paying and nobody should reach for a wallet.</div><dl><dt>Includes</dt><dd>Tastings, food options, photos</dd><dt>Groups 6–14</dt><dd>20% off retail + 18% gratuity</dd><dt>Try</dt><dd>Bachelorette Special · 8 hrs · $600 ($480 group)</dd></dl><div class="actions"><a class="btn btn-primary" href="wine-tours-of-sedona.html">See tours</a></div></article>
    <article class="division brand-sip"><img class="badge-img" src="images/badge-sip.png" alt="SIP Sedona logo" width="96" height="96"><span class="tag">SIP Sedona</span><h3>Private vans &amp; coaches by the hour</h3><div class="fit">Best for big parties on a budget and for wedding guest shuttles. Everyone pays their own tastings; the group pays the vehicle.</div><dl><dt>Vans</dt><dd class="num">10–14 seats · $250 / hour</dd><dt>Coaches</dt><dd class="num">25–33 seats · $400 / hour</dd><dt>Private tour</dt><dd>Any SIP tour + $100 / hour</dd></dl><div class="actions"><a class="btn btn-primary" href="sip-sedona.html#events">Fleet &amp; events</a></div></article>
    <article class="division brand-swa"><img class="badge-img" src="images/badge-swa.png" alt="Sedona Wine Adventures logo" width="96" height="96"><span class="tag">Sedona Wine Adventures</span><h3>Small private groups, flexible route</h3><div class="fit">Best for four to fourteen friends who want a private guide and the freedom to change plans at every stop.</div><dl><dt>Format</dt><dd>Private, pay-as-you-go</dd><dt>Try</dt><dd>Everybody's ABT · 6 hrs · $300</dd><dt>Or</dt><dd>Perspectives of DA Ranch · $250</dd></dl><div class="actions"><a class="btn btn-primary" href="sedona-wine-adventures.html">See adventures</a></div></article>
  </div>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap split">
  <div class="panel">
    <span class="eyebrow">Corporate &amp; team building</span>
    <h3>A retreat day people will still mention next quarter</h3>
    <p style="color:var(--ink-2)">Private vehicle, a welcome flight with charcuterie, a long lunch at a vineyard or Merkin's trattoria, and a guide who keeps the day moving without rushing the conversation. We invoice the company, handle dietary notes, and can add a Scenic Sedona extension or a sunset finish.</p>
    <ul><li>Groups of 6 to 14 in one private vehicle; 33 in a coach; larger with a second guide</li><li>Optional private tastings and behind-the-scenes barrel rooms</li><li>Step-on guide service for groups arriving by motorcoach — 20% off for 15+ adults</li></ul>
  </div>
  <div class="panel">
    <span class="eyebrow">Weddings &amp; celebrations</span>
    <h3>From the bachelorette to the send-off</h3>
    <p style="color:var(--ink-2)">A wine tour for the bridal party on Friday, guest shuttles between hotels, ceremony and reception on Saturday, and a brunch run on Sunday if you need it. SIP Sedona's coordinated pickups keep the whole guest list together and off the road.</p>
    <ul><li>Vans and coaches for 10 to 33 guests, by the hour, return runs at night</li><li>Bachelorette tours with one vehicle for everyone</li><li>In-home tastings at the rental the night before — ask about <a href="index.html#cellar">The Sedona Cellar Experience</a></li></ul>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">How it works</span><h2>Booking a group in three steps</h2></div></div>
  <div class="pillars">
    <div class="pillar"><div class="glyph">1</div><h3>Call us</h3><p>Five minutes on the phone at {PHONE_MAIN}: dates, headcount, what the group likes to drink, any budget or dietary notes. We'll recommend a division and a vehicle on the spot.</p></div>
    <div class="pillar"><div class="glyph">2</div><h3>We confirm by email</h3><p>Itinerary, pricing, pickup point and payment terms in writing, so everyone from the maid of honor to the CFO is looking at the same page.</p></div>
    <div class="pillar"><div class="glyph">3</div><h3>Show up thirsty</h3><p>Your guide meets you at the hotel or rental. Everything else — routes, reservations, the good patio seats — is handled.</p></div>
  </div>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Questions</span><h2>Group tours, answered</h2></div></div>
  {faq_html(GROUPS_FAQ)}
</div></section>
{cta_block("Let's plan your group's day in Sedona.", "One call and we'll narrow it down; then we'll confirm every detail by email. Groups of 2 to 33 per vehicle, corporate to bachelorette to wedding shuttle.", "index.html#contact", "Send us the details", PHONE_MAIN_TEL, PHONE_MAIN)}
'''

GROUPS = dict(
  slug="groups-corporate-weddings.html",
  title="Group Wine Tours Sedona | Corporate, Bachelorette &amp; Weddings",
  description="Corporate wine tours, bachelorette parties, reunions and wedding guest shuttles in Sedona for 2–33 guests per vehicle. Groups of 6+ save 20%; vans $250/hr, coaches $400/hr. Call (928) 504-2445.",
  body=GROUPS_BODY,
  schema=[breadcrumbs([("Home","index.html"),("Groups, corporate & weddings","groups-corporate-weddings.html")]), faq_schema(GROUPS_FAQ)],
)

# ---------------------------------------------------------------- PRICING & POLICIES
PRICING_FAQ = [
  ("What's your cancellation policy?", "We know plans change. Cancel 24 hours or more before your tour and we'll issue a gift card for the full amount to use on any future tour. Inside 24 hours we're unable to issue a gift card, and we don't offer cash refunds — by then your guide and vehicle are reserved for you. If one guest drops out but the booking stands, that guest receives 75% of their price back (a 25% administrative fee applies)."),
  ("When do I pay?", "Payment in full at booking — Visa, Mastercard, American Express, Discover or PayPal online or by phone. Prefer a check? Make it payable to Sedona Hiking Adventures, LLC, mail it to P.O. Box 1280, Sedona, AZ 86339, and let us have it seven or more days before the tour."),
  ("Is gratuity included?", "Gratuity is added, not included. SIP Sedona and Sedona Wine Adventures add 18% to every tour; Wine Tours of Sedona adds 18% only for groups of six or more. On other Wine Tours of Sedona tours, tipping is at your discretion — guests typically leave 15 to 25%, and guides can accept PayPal, Venmo or Apple Pay."),
  ("Can children or guests under 21 come?", "Children 17 and under ride free but aren't recommended on wine or brewery tours; they're free on most scenic Red Rock Adventures and, up to age 15, on raw chocolate tours. Adults 18 to 20 are $35 per person per hour and can't taste. Children must be accompanied by a parent or guardian."),
  ("What should I bring?", "Comfortable footwear, sunglasses, layers in the cooler months, a camera and a desire to have a great day with us. Please skip heavy perfume or cologne — it fights the wine — and note that all our tours, rest stops included, are smoke-free."),
  ("What if a winery is too busy for all our stops?", "Busy weekends sometimes mean fewer stops than advertised. We don't prorate refunds for that, but your guide will happily arrange an extra flight or glass elsewhere, or swap an included tasting for a comparable glass of wine."),
]

PRICING_BODY = f'''
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Pricing &amp; policies · Effective January 24, 2026</span>
    <h1>Sedona wine tour prices, plainly</h1>
    <p class="lede">Every rate, discount, add-on and policy across our three divisions on one page, so there are no surprises at booking. Prices are per person and are the retail rates quoted to individuals; group rates and discounts are below.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem"><a class="btn btn-primary" href="index.html#packages">See every tour and price</a><a class="btn btn-ghost" href="tel:{PHONE_MAIN_TEL}">Call {PHONE_MAIN}</a></div>
  </div>
  <div class="facts">
    <div><span>Wine Tours of Sedona</span><strong class="num">~$75 pp / hour, tastings included</strong></div>
    <div><span>Sedona Wine Adventures</span><strong class="num">$50 pp / hour + tastings</strong></div>
    <div><span>SIP Sedona</span><strong class="num">$30 pp / hour + tastings</strong></div>
    <div><span>Adults 18–20</span><strong class="num">$35 pp / hour, no tasting</strong></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Rates by division</span><h2>How each division is priced</h2></div><p>Some tours run a little above the base hourly rate because they include more — a charcuterie plate, a vineyard tour, dinner. Overtime is billed at the same hourly rate with no discounts.</p></div>
  <div class="compare"><table>
    <thead><tr><th scope="col"></th><th scope="col">Wine Tours of Sedona</th><th scope="col">SIP Sedona</th><th scope="col">Sedona Wine Adventures</th></tr></thead>
    <tbody>
      <tr><th scope="row">Base rate</th><td class="c1 num">About $75 per person per hour</td><td class="c2 num">$30 per person per hour</td><td class="c3 num">$50 per person per hour</td></tr>
      <tr><th scope="row">Format</th><td class="c1">Private, 2–14 guests</td><td class="c2">Small group up to 14; private for $100 per hour × tour length</td><td class="c3">Private, 2–14 guests</td></tr>
      <tr><th scope="row">Tasting fees</th><td class="c1">Included</td><td class="c2">Paid at each stop</td><td class="c3">Paid at each stop</td></tr>
      <tr><th scope="row">Gratuity (18%)</th><td class="c1">Added for groups of 6+ only</td><td class="c2">Added to every tour</td><td class="c3">Added to every tour</td></tr>
      <tr><th scope="row">Group discount</th><td class="c1">20% off retail for 6–14 adults; 15+ call</td><td class="c2">None</td><td class="c3">Small group rates on select tours</td></tr>
      <tr><th scope="row">Non-drinking adult</th><td class="c1">25% off retail</td><td class="c2">—</td><td class="c3">—</td></tr>
      <tr><th scope="row">Children 0–17</th><td class="c1">Free (not recommended on wine tours)</td><td class="c2">21+ only</td><td class="c3">Free</td></tr>
      <tr><th scope="row">Pickup</th><td class="c1">Free in Sedona; flat fee beyond</td><td class="c2">Sedona city limits only</td><td class="c3">Free in Sedona; flat fee beyond</td></tr>
    </tbody>
  </table></div>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Discounts</span><h2>Ten percent off, and who gets it</h2></div><p>One discount per booking — we apply whichever is highest. Discounts apply to add-ons but not to overtime.</p></div>
  <div class="pillars">
    <div class="pillar"><div class="glyph">★</div><h3>U.S. military</h3><p>Past or present. Thank you for your service.</p></div>
    <div class="pillar"><div class="glyph">A</div><h3>AAA members</h3><p>Show your card at pickup.</p></div>
    <div class="pillar"><div class="glyph">65</div><h3>Seniors 65+</h3><p>You've earned the good bottle.</p></div>
    <div class="pillar"><div class="glyph">↻</div><h3>Returning guests</h3><p>Anyone who has toured with Wine Tours of Sedona, Sedona Red Rock Adventures or Sedona Hiking Adventures before.</p></div>
    <div class="pillar"><div class="glyph">DOG</div><h3>Bring your dog</h3><p>Promo code <strong>DOGFRIENDLY</strong> on Wine Tours of Sedona and Sedona Wine Adventures. Well-behaved and friendly, please.</p></div>
    <div class="pillar"><div class="glyph">6+</div><h3>Groups of six or more</h3><p>20% off retail on every Wine Tours of Sedona tour — the biggest saving we offer, and it can't be combined with the 10% discounts.</p></div>
  </div>
</div></section>

<section><div class="wrap split">
  <div class="panel">
    <span class="eyebrow">Add-ons · Wine Tours of Sedona (dinner transport also on Sedona Wine Adventures)</span>
    <h3>Make the day longer, or tastier</h3>
    <ul>
      <li><strong>Lunch</strong> — $55 per person, one dish; the whole party adds it.</li>
      <li><strong>Dinner</strong> — $111 per person: appetizer, entrée, dessert and one beverage or flight; the whole party adds it.</li>
      <li><strong>Transportation To &amp; From Dinner</strong> — a flat $150 per group. Book a table for your tour's finish time and we'll add three hours to get you there and home. Responsible drinking is paramount to us.</li>
      <li><strong>Scenic Sedona</strong> — two more hours for $99 per person if added at booking (about a third off our normal rate): Oak Creek Canyon, Chapel of the Holy Cross, Bell Rock, Cathedral Rock, Airport Mesa vortex, Rachel's Knoll, the Amitabha Stupa, Schuerman Cemetery.</li>
      <li><strong>Charcuterie board + one more tasting + 75 minutes</strong> — $99 per person; all adults add it.</li>
    </ul>
    <p style="color:var(--ink-2);font-size:.92rem">SIP Sedona keeps things simple with no add-ons; Sedona Wine Adventures offers dinner transport but not lunch or dinner.</p>
  </div>
  <div class="panel">
    <span class="eyebrow">Pickup · Wine Tours of Sedona &amp; Sedona Wine Adventures</span>
    <h3>Free in Sedona, flat fees beyond</h3>
    <ul>
      <li><strong>Anywhere in Sedona</strong> — free, hotels and vacation rentals included.</li>
      <li><strong>Cornville, Clarkdale, Cottonwood</strong> — $75</li>
      <li><strong>Jerome</strong> — $100</li>
      <li><strong>Flagstaff, Munds Park</strong> — $200</li>
      <li><strong>Prescott</strong> — $300</li>
      <li><strong>Phoenix metro</strong> — $2,000</li>
    </ul>
    <p style="color:var(--ink-2);font-size:.92rem">Day-trippers meet at The Art of Wine, Hyatt Piñon Pointe Shops, 101 N Hwy 89A, Sedona — just note “day trip” on your questionnaire. SIP Sedona picks up within Sedona city limits only.</p>
  </div>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Groups of 15 or more</span><h2>Big groups, two ways</h2></div></div>
  <div class="split">
    <div class="panel"><h3>Step-on guide</h3><p style="color:var(--ink-2)">Your group arrives on its own motorcoach and one of our guides steps on to lead the day — 20% off the per-person tour rate for fifteen or more adults.</p></div>
    <div class="panel"><h3>We provide the transportation</h3><p style="color:var(--ink-2)">$3,000 plus the per-person rate, and we bring the vehicles, the guides and the itinerary. We've handled a dozen to a hundred-plus guests. Call <a href="tel:{PHONE_WTOS_TEL}">{PHONE_WTOS}</a>.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Policies</span><h2>The fine print, in plain English</h2></div></div>
  {faq_html(PRICING_FAQ)}
  <p style="margin-top:1.5rem;color:var(--ink-2);font-size:.92rem">Every guest signs our online liability waiver before the tour (one per person, referencing your FareHarbor booking number). Guests who arrive intoxicated can't be taken out, and that booking isn't refundable — for everyone's safety. Sedona Wine Tours is not responsible for traffic, weather on the day, acts of God, or service timelines at the locations we visit. Policies effective January 24, 2026.</p>
</div></section>
{cta_block("Questions about a rate? Just ask.", "We'd rather explain it on the phone than have you guess. Call any division, or send us the details and we'll quote it in writing.", "index.html#contact", "Send us the details", PHONE_MAIN_TEL, PHONE_MAIN)}
'''

PRICING = dict(
  slug="pricing-and-policies.html",
  title="Sedona Wine Tour Prices &amp; Cost | Discounts &amp; Policies",
  description="How much does a Sedona wine tour cost? Current rates from $30 to $75 per person per hour across our three divisions, group and 10% discounts, add-ons, pickup fees, gratuity and cancellation policy.",
  body=PRICING_BODY,
  schema=[breadcrumbs([("Home","index.html"),("Pricing & policies","pricing-and-policies.html")]), faq_schema(PRICING_FAQ)],
)


# ---------------------------------------------------------------- WINERIES
WINERY_FAQ_RAW = [
  ("Are there wineries in Sedona itself?", "Sedona has tasting rooms rather than vineyards — The Art of Wine, Vino Di Sedona, Winery 1912, VinoZona and Decanter pour Arizona wines in town. The vineyards are twenty to forty minutes away in the Verde Valley: Page Springs, Cornville, Camp Verde, Cottonwood, Clarkdale and Jerome. That drive is exactly why a guided wine tour makes sense here."),
  ("How many wineries are near Sedona?", "The Verde Valley AVA has eight vineyard locations, around twenty tasting rooms and seven micro-breweries, and the count keeps growing — three distilleries are arriving in Old Town Cottonwood. We visit all of them."),
  ("Which Sedona winery is best?", "Honestly, it depends on what you like. For scenery, Alcantara on the Verde River. For a story, DA Ranch's cattle-ranch-turned-vineyard. For food, Merkin Vineyards' handmade pasta. For a Zinfandel, Javelina Leap's estate. For sweet wines, Oak Creek Vineyards. Tell your guide your palate and we'll build the route — that's what the Terroir of the Verde Valley Wine Trail tour is for."),
  ("Can I visit Sedona wineries without a tour?", "You can, but someone has to drive the switchbacks, and DA Ranch, Bodega Pierce and the Southwest Wine Center are closed some days or need reservations. Our guides handle the days, the reservations and the driving, and the tasting fees are included on Wine Tours of Sedona. Call <a href='tel:{TEL}'>{NUM}</a>."),
  ("What is the Verde Valley Wine Trail?", "A loose circuit of vineyards and tasting rooms along Oak Creek and the Verde River, from Camp Verde through Cornville, Page Springs, Cottonwood and Clarkdale up to Jerome. Volcanic soils, high-desert elevation and cool nights give the wines their character. The Verde Valley became an American Viticultural Area in December 2021."),
]
WINERY_FAQ = [(q, tel(a)) for q, a in WINERY_FAQ_RAW]

def winery(name, place, blurb):
    return f'<div class="winery"><h3>{name}</h3><span class="place">{place}</span><p>{blurb}</p></div>'

WINERIES_BODY = f"""
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Wineries &amp; vineyards near Sedona · The Verde Valley AVA</span>
    <h1>Sedona wineries and Verde Valley vineyards: our insider's guide</h1>
    <p class="lede">We've been driving the Verde Valley Wine Trail since 2004 — since before it was an AVA, and before most of these tasting rooms opened. Here's every vineyard, tasting room and brewery we visit, what each one does best, and the days you can't get in. Then let us do the driving.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.4rem"><a class="btn btn-primary" href="index.html#divisions">Find a wine tour</a><a class="btn btn-ghost" href="tel:{PHONE_MAIN_TEL}">Call {PHONE_MAIN}</a></div>
  </div>
  <div class="facts">
    <div><span>Vineyards</span><strong class="num">8 estate locations</strong></div>
    <div><span>Tasting rooms</span><strong class="num">About 20</strong></div>
    <div><span>Breweries</span><strong class="num">7 in the Verde Valley</strong></div>
    <div><span>AVA since</span><strong>December 2021</strong></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Page Springs, Cornville &amp; Camp Verde</span><h2>The estate vineyards</h2></div><p>Where northern Arizona's modern wine story began: vines along Oak Creek and the Verde River, twenty to thirty minutes from Sedona.</p></div>
  <div class="winery-grid">
    {winery("Alcantara Vineyard", "Camp Verde · daily 11 a.m.–2 p.m. (3 p.m. April–October)", "The largest continuous estate vineyard in the region — about 80 acres and 35 wines — at the confluence of Oak Creek and the Verde River. A wedding chapel, a private beach, cliff dwellings on the ridge, and their Confluence red blend. Ask about a barrel-room look when the winemaker is around.")}
    {winery("DA Ranch (Dancing Apache Ranch)", "Page Springs · closed Monday &amp; Tuesday", "A former working cattle ranch, now six acres of vines on 350 with springs, a pond, goats and donkeys — the Petznick family's retreat. Wines are sold only to Arizona residents and the wine club, which makes a tasting here the only way most visitors ever try them. Our favorite red is the Capra. Sister winery: Chateau Tumbleweed.")}
    {winery("Page Springs Cellars", "Page Springs", "Creekside tastings under the sycamores from one of the valley's founding producers.")}
    {winery("Javelina Leap Vineyard", "Page Springs", "Award-winning estate Zinfandel and a patio that looks straight at the red rocks.")}
    {winery("Oak Creek Vineyards", "Page Springs", "Approachable reds and whites, and the valley's go-to for sweet and dessert wines. The first stop on our SIP Sedona 3-Hour Tasting Adventure.")}
    {winery("Cove Mesa Vineyard", "Cornville · opened November 2022", "A modern tasting room where the owners are often pouring, with a proper food menu — the second stop on the 3-Hour Tasting Adventure.")}
    {winery("Salt Mine Wine", "Camp Verde · Friday–Sunday", "Established 2012, five acres and 500–600 cases a year, known for a steel-aged Malvasia Blanca. A boutique stop on our Taste of Camp Verde tour.")}
    {winery("Clear Creek Vineyards (Rio Claro)", "Camp Verde · Friday–Sunday", "Established 2015, 100% estate fruit, wines aged three to seven years before release and shipped to about 34 states.")}
  </div>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Old Town Cottonwood</span><h2>Nine tasting rooms on five walkable blocks</h2></div><p>Quaint, historic and forty minutes from Sedona. Our Taste of Old Town, Evening in Old Town and Rock Star tours live here.</p></div>
  <div class="winery-grid">
    {winery("Merkin Vineyards &amp; Hilltop Trattoria", "Old Town Cottonwood", "Maynard James Keenan's flagship: estate wines with handmade pasta and local vegetables. Dinner on An Evening in Old Town; lunch on the Rock Star Wine Tour.")}
    {winery("Four Eight Wineworks", "Old Town Cottonwood &amp; Jerome", "Also Keenan's — a cooperative that gives young Arizona winemakers a tasting room.")}
    {winery("Rubrix Wines", "Old Town Cottonwood", "Formerly Burning Tree Cellars; a stop on the 5-Hour Wine, Beer &amp; Beyond Experience.")}
    {winery("Arizona Stronghold", "Old Town Cottonwood", "The state's largest winemaker — flights or by-the-glass in a lively room. The social finish to the 4-Hour SIP &amp; Savor Tour.")}
    {winery("DA Vines &amp; Vineyard", "Old Town Cottonwood", "DA Ranch's in-town tasting room, and home to some of our favorite wines in Arizona.")}
    {winery("Eureka Room", "Old Town Cottonwood", "Small-batch wines from boutique winemakers across the state.")}
    {winery("Cellar 433", "Old Town Cottonwood", "Wines from John McLaughlin, one of Arizona's largest grape growers.")}
    {winery("Tantrum Wines", "Old Town Cottonwood", "One of the few female-owned wineries in Arizona, with a whimsical room to match.")}
    {winery("Belfry Brewery", "Old Town Cottonwood", "For the beer drinker in the group — and there's always one.")}
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Jerome &amp; Clarkdale</span><h2>A ghost town and a college that grows its own</h2></div></div>
  <div class="winery-grid">
    {winery("Caduceus Cellars", "Jerome", "Keenan's Jerome tasting room, inside the Puscifer store, on the Flavors of Historic Jerome and Rock Star tours.")}
    {winery("Cabal Cellars", "Jerome", "Conspiracy-theory labels and serious wine.")}
    {winery("Passion Cellars · Original Jerome Winery · VinoZona · Coronado Vineyard", "Jerome", "The rest of the hill: seven rooms in a copper-mining town of 450 residents, with views to the San Francisco Peaks. Coronado is the newest. Lunch, if you add it, is The Haunted Hamburger.")}
    {winery("Southwest Wine Center", "Clarkdale · Thursday–Sunday, reservations", "Yavapai College's two-year winemaking program, pouring wines grown and made on campus. The heart of our Clarkdale Wine &amp; Vineyard Education Experience.")}
    {winery("Bodega Pierce", "Clarkdale · reservations", "Michael Pierce, dean of the college wine program, making a Malvasia Blanca we love.")}
    {winery("Chateau Tumbleweed", "Clarkdale", "DA Ranch's sister winery, mostly Willcox fruit, with the most informative (and funniest) labels in the valley.")}
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Flagstaff · 30 miles north, 7,000 feet up</span><h2>The Flagstaff breweries we visit</h2></div><p>Flagstaff's eight breweries are the stops on the city's official Brewery Trail, and the reason our micro-brewery tours don't stop at the valley line. It's a mountain town with a college, a railroad and a serious beer scene — cooler by fifteen degrees, which is exactly what you want in July. We run a dedicated historic downtown Flagstaff brewery tour, and the Arizona Hopful tour strings every brewery from Camp Verde to Flagstaff into one day.</p></div>
  <div class="winery-grid">
    {winery("Mother Road Brewing Company", "Southside &amp; downtown Flagstaff", "Flagstaff's best-known brewery, named for Route 66 and famous for Tower Station IPA. Two spots: the original Butler Avenue brewery and a downtown taproom.")}
    {winery("Historic Brewing Company — Barrel + Bottle House", "Downtown Flagstaff", "Historic's downtown tasting room, with a long list that includes their cult Piehole Porter, a cherry-vanilla porter people drive up for.")}
    {winery("Dark Sky Brewing Company", "Downtown Flagstaff", "Small-batch and always changing — the board can turn over weekly. Named for Flagstaff's status as the world's first International Dark Sky City.")}
    {winery("Beaver Street Brewery", "Southside Flagstaff", "The elder statesman, open since 1994, with wood-fired pizza and a family-friendly brewpub feel. A reliable first or last stop.")}
    {winery("Lumberyard Brewing Company", "Southside Flagstaff", "Beaver Street's sister brewery inside a restored 1900s lumber mill building — bigger room, bigger patio, a full menu, and a big Flagstaff IPA.")}
    {winery("Flagstaff Brewing Company", "Historic downtown, on Route 66", "A downtown fixture since 1994 with a lively patio and a deep whiskey list to go with the house beers.")}
    {winery("Wanderlust Brewing Company", "East Flagstaff", "The beer nerd's favorite: Belgian-inspired and barrel-aged ales in a no-frills industrial taproom. Try the 928 Local farmhouse ale.")}
    {winery("Grand Canyon Brewing + Distillery", "Flagstaff taproom (brewed in Williams)", "Northern Arizona's largest brewery, with a Flagstaff taproom pouring the full line plus their own spirits. Sunset Amber is the crowd-pleaser.")}
  </div>
  <p style="margin-top:1.2rem"><a class="btn btn-primary" href="https://winetoursofsedona.com/scenic-micro-brewery-tours/" rel="noopener">See our micro-brewery tours</a> <a class="btn btn-ghost" href="index.html#packages">All tour packages</a></p>
</div></section>

<section style="background:var(--ground-2)"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">In Sedona</span><h2>Tasting rooms you can walk to</h2></div><p>No vineyards in town, but five rooms pouring Arizona wine — the basis of our Sedona Arizona Wine Tasting Experience and the Sedona Quickie.</p></div>
  <div class="winery-grid">
    {winery("The Art of Wine", "Hyatt Piñon Pointe Shops, 101 N Hwy 89A", "Our day-trip meeting point and the Sedona Quickie's home — a curated Arizona list in uptown.")}
    {winery("Vino Di Sedona", "West Sedona", "Wine bar, bottle shop and live music; the last stop on the Wine, Beer &amp; Beyond loop.")}
    {winery("Winery 1912 · VinoZona · Decanter", "Sedona", "Three more rooms for a walkable afternoon of Arizona wine without leaving the red rocks.")}
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Questions</span><h2>Sedona wineries, answered</h2></div></div>
  {faq_html(WINERY_FAQ)}
</div></section>
{cta_block("Let us drive you to all of them.", "Every stop on this page is on a Wine Tours of Sedona, SIP Sedona or Sedona Wine Adventures route. Tell us what you like to drink and we'll pick the day.", "index.html#divisions", "Compare our wine tours", PHONE_MAIN_TEL, PHONE_MAIN)}
"""

WINERIES_PAGE = dict(
  slug="sedona-wineries-and-vineyards.html",
  title="Wineries in Sedona &amp; Verde Valley Vineyards | Insider's Guide",
  description="Every winery, vineyard, tasting room and brewery near Sedona, AZ — Alcantara, DA Ranch, Page Springs, Old Town Cottonwood, Jerome, Clarkdale and Flagstaff's eight breweries — with specialties and which tour visits each. From Sedona's guides since 2004.",
  body=WINERIES_BODY,
  schema=[breadcrumbs([("Home","index.html"),("Wineries & vineyards near Sedona","sedona-wineries-and-vineyards.html")]), faq_schema(WINERY_FAQ)],
)

THANKS_BODY = f"""<section><div class="wrap"><span class="eyebrow">Message received</span><h1>Thanks — we'll be in touch within a business day.</h1><p class="lede">In the meantime, the fastest way to lock in a date is a quick call: <a href="tel:{PHONE_MAIN_TEL}">{PHONE_MAIN}</a>. Or keep browsing the tours.</p><p><a class="btn btn-primary" href="index.html#divisions">Compare our three divisions</a> <a class="btn btn-ghost" href="index.html#packages">Tour packages &amp; prices</a></p></div></section>"""

THANKS = dict(
  slug="thank-you.html",
  title="Thanks — we'll be in touch | Sedona Wine Tours",
  description="Your message reached Sedona Wine Tours. We'll reply within one business day — or call (928) 504-2445 to talk now.",
  body=THANKS_BODY, schema=[], current="index.html",
)
