

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
    <div><span>Breweries</span><strong class="num">7 in the valley</strong></div>
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
  description="Every winery, vineyard and tasting room near Sedona, AZ — Alcantara, DA Ranch, Page Springs, Old Town Cottonwood, Jerome and Clarkdale — with hours, specialties and which wine tour visits each. From Sedona's guides since 2004.",
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
