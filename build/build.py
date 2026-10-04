#!/usr/bin/env python3
"""Builds the Sedona Wine Tours site into ../site and a single-file preview."""
import json, os, re, shutil
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent / "site"
SITE = "https://www.sedonawinetours.group"
PHONE_MAIN = "(928) 504-2445"; PHONE_MAIN_TEL = "+19285042445"
PHONE_WTOS = "(928) 224-2991"; PHONE_WTOS_TEL = "+19282242991"
PHONE_SIP = "(928) 308-5166"; PHONE_SIP_TEL = "+19283085166"
PHONE_SWA = "(928) 366-8476"; PHONE_SWA_TEL = "+19283668476"
ADDRESS = "2020 Contractors Road, Suite 3, Sedona, AZ 86336"

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Figtree:wght@400;500;600;700&display=swap">'

CSS = (HERE / "styles.css").read_text() + __import__("reviews").REVIEWS_CSS + __import__("social").SOCIAL_CSS

NAV = [
    ("index.html", "Home"),
    ("wine-tours-of-sedona.html", "Wine Tours of Sedona"),
    ("sip-sedona.html", "SIP Sedona"),
    ("sedona-wine-adventures.html", "Sedona Wine Adventures"),
    ("groups-corporate-weddings.html", "Groups &amp; Weddings"),
    ("sedona-wineries-and-vineyards.html", "Wineries"),
    ("pricing-and-policies.html", "Pricing"),
    ("blog/index.html", "Blog"),
]

def clean(slug):
    if slug == "index.html": return "/"
    if slug == "blog/index.html": return "/blog"
    return "/" + slug[:-5]

def cleanify(html):
    """Rewrite internal .html links to extensionless URLs (served by .htaccess)."""
    html = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1) or ""}"', html)
    for href, _ in NAV + [("pricing-and-policies.html", ""), ("sedona-wineries-and-vineyards.html", ""), ("reviews.html", ""), ("404.html", ""), ("thank-you.html", ""), ("blog/index.html", "")]:
        html = re.sub(r'href="' + re.escape(href) + r'(#[^"]*)?"', lambda m, h=href: f'href="{clean(h)}{m.group(1) or ""}"', html)
    return html

def header(current):
    links = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        cls = ' class="nav-home"' if href == "index.html" else ""
        links += f'<a href="{href}"{cur}{cls}>{label}</a>'
    return f'''<header class="site-header"><div class="wrap">
  <a class="wordmark" href="index.html" aria-label="Sedona Wine Tours home"><img class="mark" src="/images/swt-emblem-sm.webp" alt="" width="40" height="40"><span>Sedona Wine Tours<small>Sip. Savor. Explore. · Est. 2004</small></span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="primary-nav" onclick="var n=document.getElementById('primary-nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
  <nav class="primary" id="primary-nav" aria-label="Primary">{links}<a class="btn btn-phone" href="tel:{PHONE_MAIN_TEL}">{PHONE_MAIN}</a></nav>
</div></header>'''

FOOTER = f'''<footer><div class="wrap">
  <div class="cols">
    <div>
      <a class="wordmark" href="index.html"><img class="mark" src="/images/swt-emblem-sm.webp" alt="" width="40" height="40"><span>Sedona Wine Tours</span></a>
      <p style="margin-top:.8rem;max-width:36ch">One locally owned family of Sedona wine tour guides since 2004 — three divisions, one standard of hospitality.</p>
      <p><a href="tel:{PHONE_MAIN_TEL}">{PHONE_MAIN}</a><br>{ADDRESS}</p>
    </div>
    <div><h4>Our divisions</h4><ul>
      <li><a href="wine-tours-of-sedona.html">Wine Tours of Sedona</a> · <a href="https://www.winetoursofsedona.com" rel="noopener">site</a></li>
      <li><a href="sip-sedona.html">SIP Sedona</a> · <a href="https://sipsedona.com" rel="noopener">site</a></li>
      <li><a href="sedona-wine-adventures.html">Sedona Wine Adventures</a> · <a href="https://www.sedonawineadventures.com" rel="noopener">site</a></li>
    </ul></div>
    <div><h4>Plan your visit</h4><ul>
      <li><a href="groups-corporate-weddings.html">Group, corporate &amp; wedding tours</a></li>
      <li><a href="pricing-and-policies.html">Pricing, discounts &amp; policies</a></li>
      <li><a href="index.html#packages">Tour packages</a></li>
      <li><a href="index.html#cellar">In-home wine tasting</a></li>
      <li><a href="sedona-wineries-and-vineyards.html">Wineries &amp; vineyards near Sedona</a></li>
      <li><a href="reviews.html">Guest reviews, all divisions</a></li>
      <li><a href="index.html#faq">Questions &amp; answers</a></li>
    </ul></div>
    <div><h4>Direct lines</h4><ul>
      <li>Wine Tours of Sedona <a href="tel:{PHONE_WTOS_TEL}">{PHONE_WTOS}</a></li>
      <li>SIP Sedona <a href="tel:{PHONE_SIP_TEL}">{PHONE_SIP}</a></li>
      <li>Sedona Wine Adventures <a href="tel:{PHONE_SWA_TEL}">{PHONE_SWA}</a></li>
    </ul></div>
  </div>
  <div class="legal"><span>© 2026 Sedona Wine Tours. All tours depart from Sedona, Arizona and serve the Verde Valley, Jerome, Cottonwood, Page Springs, Cornville, Clarkdale, Camp Verde and Flagstaff.</span><span>Please drink responsibly. Guests must be 21+ to taste.</span></div>
</div></footer>'''

def page(slug, title, description, body, schema, current=None, brand_class="", canonical=None, og_title=None, chatbot=None):
    canonical = canonical or (SITE + ("/" if slug == "index.html" else clean(slug)))
    bot = chatbot_snippet(chatbot or CHATBOT_DEFAULT.get(slug) or CHATBOT_DEFAULT.get(current or ""))
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sedona Wine Tours">
<meta property="og:title" content="{og_title or title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/images/og-sedona-wine-tours.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-AZ"><meta name="geo.placename" content="Sedona"><meta name="geo.position" content="34.8697;-111.7610"><meta name="ICBM" content="34.8697, -111.7610">
{FONTS}
<link rel="stylesheet" href="/assets/styles.css">
<link rel="alternate" type="application/rss+xml" title="Sedona Wine Tours blog" href="/blog/feed.xml">
<script src="https://fareharbor.com/embeds/api/v1/?autolightframe=yes" async defer></script>
{ld}
</head>
<body class="{brand_class}">
<a class="sr-only" href="#main">Skip to content</a>
{header(current or slug)}
<main id="main">
{body}
</main>
{FOOTER}
{bot}
</body>
</html>'''

# ---------- Chatbots (Yonder) ----------
# build/chatbots.json: {"wtos": "<script ...>", "sip": "...", "swa": "..."} — the exact install
# snippet Yonder gives for each division's bot. Pages map to a division below; pages not
# listed get no chatbot. Empty string = none.
CHATBOT_DEFAULT = {"wine-tours-of-sedona.html": "wtos", "sip-sedona.html": "sip", "sedona-wine-adventures.html": "swa",
                   "index.html": "wtos", "groups-corporate-weddings.html": "wtos", "pricing-and-policies.html": "wtos",
                   "sedona-wineries-and-vineyards.html": "wtos", "reviews.html": "wtos", "blog/index.html": "wtos"}
def chatbot_snippet(key):
    f = HERE / "chatbots.json"
    if not key or not f.exists():
        return ""
    return json.load(open(f)).get(key, "") or ""

# ---------- Shared schema ----------
ORG = {
  "@context": "https://schema.org",
  "@type": ["Organization", "TourOperator", "LocalBusiness"],
  "@id": f"{SITE}/#org",
  "name": "Sedona Wine Tours",
  "alternateName": ["Sedona Wine Tours Group"],
  "url": SITE,
  "telephone": PHONE_MAIN_TEL,
  "foundingDate": "2004",
  "founder": {"@type": "Person", "name": "Jim Reich"},
  "address": {"@type": "PostalAddress", "streetAddress": "2020 Contractors Road, Suite 3", "addressLocality": "Sedona", "addressRegion": "AZ", "postalCode": "86336", "addressCountry": "US"},
  "geo": {"@type": "GeoCoordinates", "latitude": 34.8697, "longitude": -111.7610},
  "areaServed": [{"@type": "City", "name": "Sedona"}, {"@type": "Place", "name": "Verde Valley"}, {"@type": "City", "name": "Cottonwood"}, {"@type": "City", "name": "Jerome"}, {"@type": "City", "name": "Cornville"}, {"@type": "City", "name": "Clarkdale"}, {"@type": "City", "name": "Camp Verde"}, {"@type": "City", "name": "Flagstaff"}],
  "priceRange": "$90–$777",
  "subOrganization": [
    {"@type": "Organization", "name": "Wine Tours of Sedona", "url": "https://www.winetoursofsedona.com", "telephone": PHONE_WTOS_TEL},
    {"@type": "Organization", "name": "SIP Sedona", "url": "https://sipsedona.com", "telephone": PHONE_SIP_TEL},
    {"@type": "Organization", "name": "Sedona Wine Adventures", "url": "https://www.sedonawineadventures.com", "telephone": PHONE_SWA_TEL},
  ],
  "sameAs": ["https://www.winetoursofsedona.com", "https://sipsedona.com", "https://www.sedonawineadventures.com"] + __import__("social").same_as(),
}

def breadcrumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + ("" if u == "index.html" else clean(u))} for i, (n, u) in enumerate(items)]}

def faq_schema(qas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in qas]}

def faq_html(qas):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qas) + "</div>"

def offers_schema(name, tours, brand_url):
    return {"@context": "https://schema.org", "@type": "ItemList", "name": name, "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": {"@type": "TouristTrip", "name": t["name"], "description": re.sub(r"<[^>]+>", "", t["desc"]), "url": t["url"], "touristType": t.get("fit", ""),
          "offers": {"@type": "Offer", "price": t["price_num"], "priceCurrency": "USD", "url": t["url"], "availability": "https://schema.org/InStock"}, "provider": {"@type": "Organization", "name": name, "url": brand_url}}}
        for i, t in enumerate(tours)]}

def tour_card(t, brand_class=""):
    badge = f'<span class="badge">{t["badge"]}</span>' if t.get("badge") else ""
    incl = "".join(f"<li>{i}</li>" for i in t.get("includes", []))
    return f'''<article class="tour {brand_class}">
  <div class="meta"><span>{t["duration"]}</span><span>{t["meta"]}</span></div>
  <h3>{t["name"]}</h3>
  <div class="price num">{t["price"]}<small> {t["price_note"]}</small></div>
  <p>{t["desc"]}</p>
  {"<ul>"+incl+"</ul>" if incl else ""}
  <div class="actions">{badge} <a class="btn btn-primary" href="{t["url"]}" rel="noopener">{t.get("cta","Book this tour")}</a></div>
</article>'''

def specials_html():
    sp = json.loads((HERE / "specials.json").read_text())
    if not sp.get("items"):
        return ""
    cards = ""
    for it in sp["items"]:
        badge = ""  # confirm badges disabled now that the site is live
        cards += f'<article class="special brand-{it.get("division","wtos")}"><h3>{it["title"]}</h3><p>{it["text"]}</p><p>{badge}<a class="btn btn-primary" href="{it["url"]}" rel="noopener">{it["cta"]}</a></p></article>'
    return f'<section id="specials" class="tight specials-wrap"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Specials &amp; what\'s new</span><h2>{sp["heading"]}</h2></div><p>Updated {sp["updated"]}. New offers land here every week.</p></div><div class="specials">{cards}</div></div></section>'

def build():
    from content import HOME, WTOS, SIP, SWA, GROUPS, PRICING, WINERIES_PAGE, THANKS
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    (OUT / "assets" / "styles.css").write_text(CSS)
    shutil.copytree(HERE / "images", OUT / "images")
    (OUT / "images" / "README.txt").write_text("Drop photography here. See IMAGE-SHOT-LIST.md for what to shoot / which existing photos to use.\nRequired: og-sedona-wine-tours.jpg (1200x630) for social sharing previews.\n")
    pages = [HOME, WTOS, SIP, SWA, GROUPS, PRICING, WINERIES_PAGE]
    from chooser import chooser_html
    HOME["body"] = HOME["body"].replace("<!--CHOOSER-->", chooser_html()).replace("<!--SPECIALS-->", specials_html())
    from reviews import load_reviews, reviews_home_html, reviews_division_html, reviews_page_body, reviews_schema
    from social import social_home_html, social_division_html
    reviews = load_reviews()
    HOME["body"] = HOME["body"].replace("<!--REVIEWS-->", reviews_home_html(reviews)).replace("<!--SOCIAL-->", social_home_html())
    for pg, key in ((WTOS, "wtos"), (SIP, "sip"), (SWA, "swa")):
        pg["body"] = pg["body"].replace("<!--REVIEWS-->", reviews_division_html(reviews, key)).replace("<!--SOCIAL-->", social_division_html(key))
        pg["schema"] = list(pg["schema"]) + reviews_schema(reviews, key, 5)
    REVIEWS_PAGE = dict(slug="reviews.html", title="Sedona Wine Tour Reviews | Wine Tours of Sedona, SIP Sedona &amp; Sedona Wine Adventures",
        description="Real Google reviews of our three Sedona wine tour divisions, labeled by division and refreshed weekly: Wine Tours of Sedona (4.9★, 550+), SIP Sedona (5.0★) and Sedona Wine Adventures.",
        body=reviews_page_body(reviews), schema=[breadcrumbs([("Home", "index.html"), ("Guest reviews", "reviews.html")])] + reviews_schema(reviews, None, 10))
    pages.append(REVIEWS_PAGE)
    for p in pages + [THANKS]:
        html = cleanify(page(**p).replace('src="images/', 'src="/images/'))
        (OUT / p["slug"]).write_text(html)
    for f in ("htaccess.txt", "contact.php"):
        shutil.copy(HERE / f, OUT / (".htaccess" if f == "htaccess.txt" else f))
    # blog
    from blog import load_posts, post_body, index_body, post_schema, feed_xml, nice_date
    posts = load_posts()
    (OUT / "blog").mkdir(exist_ok=True)
    blog_index = dict(slug="blog/index.html", title="Arizona Travel &amp; Sedona Wine Country Blog | Sedona Wine Tours", description="Daily stories on Sedona, the Verde Valley wine trail and Arizona travel — hikes, wineries, towns, seasons and planning tips from guides who've worked here since 2004.", body=index_body(posts), schema=[breadcrumbs([("Home","index.html"),("Blog","blog/index.html")]), {"@context":"https://schema.org","@type":"Blog","name":"Sedona Wine Tours — Arizona travel blog","url":f"{SITE}/blog","publisher":{"@id":f"{SITE}/#org"}}])
    (OUT / "blog" / "index.html").write_text(cleanify(page(**blog_index).replace('src="images/', 'src="/images/')))
    for i, p in enumerate(posts):
        related = [r for r in posts if r["slug"] != p["slug"]]
        pg = dict(slug=f"blog/{p['slug']}.html", title=f"{p['title']} | Sedona Wine Tours Blog", description=p["description"], body=post_body(p, related), current="blog/index.html",
                  schema=[breadcrumbs([("Home","index.html"),("Blog","blog/index.html"),(p["title"], f"blog/{p['slug']}.html")]), post_schema(p)])
        (OUT / "blog" / f"{p['slug']}.html").write_text(cleanify(page(**pg).replace('src="images/', 'src="/images/')))
    (OUT / "blog" / "feed.xml").write_text(feed_xml(posts))
    # sitemap + robots
    today = __import__("datetime").date.today().isoformat()
    urls = "".join(f"<url><loc>{SITE}/blog/{p['slug']}</loc><lastmod>{p['updated']}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>" for p in posts)
    urls += f"<url><loc>{SITE}/blog</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>"
    urls += "".join(f"<url><loc>{SITE}{'/' if p['slug']=='index.html' else clean(p['slug'])}</loc><changefreq>monthly</changefreq><priority>{'1.0' if p['slug']=='index.html' else '0.8'}</priority></url>" for p in pages)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    (OUT / "404.html").write_text(cleanify(page(slug="404.html", title="Page not found | Sedona Wine Tours", description="That page isn't here — head back to Sedona Wine Tours.", body='<section><div class="wrap"><h1>That trail doesn\'t go anywhere.</h1><p class="lede">The page you were after has moved or never existed. Head back home, or call us at <a href="tel:+19285042445">(928) 504-2445</a> and we\'ll point you in the right direction.</p><p><a class="btn btn-primary" href="index.html">Back to Sedona Wine Tours</a></p></div></section>', schema=[], current="index.html")))
    build_preview(pages)
    print("built", [p["slug"] for p in pages])

def build_preview(pages):
    """Single-file hosted preview: all pages in one document with hash routing."""
    parts = []
    for p in pages:
        body = p["body"]
        # rewrite internal page links to hash routes
        for href, _ in NAV:
            body = body.replace(f'href="{href}#', f'href="#{href[:-5]}/').replace(f'href="{href}"', f'href="#{href[:-5]}"')
        hdr = header(p["slug"]).replace('href="index.html"', 'href="#index"')
        pid = p["slug"][:-5]
        bc = p.get("brand_class", "")
        parts.append(f'<div class="route {bc}" id="{pid}" hidden>{hdr}<main>{body}</main></div>')
    nav_fix = ""
    for href, _ in NAV:
        nav_fix += f'''document.querySelectorAll('a[href="{href}"]').forEach(a=>a.setAttribute('href','#{href[:-5]}'));'''
    preview = f'''<title>Sedona Wine Tours</title>
{FONTS}
<style>{CSS}
.preview-bar{{position:sticky;top:0;z-index:60;background:#6B4E00;color:#FFE08A;font:600 .8rem/1.4 var(--font-body);padding:.45rem 1rem;text-align:center;letter-spacing:.04em}}
.route .site-header{{top:32px}}
</style>
<div class="preview-bar">PREVIEW — hosted mock-up of www.sedonawinetours.group. Yellow “Confirm” badges mark facts to verify before launch.</div>
{"".join(parts)}
{FOOTER}
<script>
(function(){{
  {nav_fix}
  function route(){{
    var h=(location.hash||'#index').slice(1).split('/');var id=h[0]||'index';var anchor=h[1];
    var found=false;document.querySelectorAll('.route').forEach(function(r){{var on=r.id===id;r.hidden=!on;if(on)found=true;}});
    if(!found){{document.getElementById('index').hidden=false;}}
    document.querySelectorAll('nav.primary').forEach(function(n){{n.classList.remove('open')}});
    if(anchor){{var el=document.getElementById(anchor);if(el){{setTimeout(function(){{el.scrollIntoView({{behavior:'smooth'}})}},30);}}}} else {{window.scrollTo(0,0);}}
  }}
  window.addEventListener('hashchange',route);route();
}})();
</script>'''
    import base64, mimetypes
    def inline(m):
        p = OUT / m.group(1)
        mt = mimetypes.guess_type(str(p))[0] or "image/webp"
        if p.suffix == ".webp": mt = "image/webp"
        return 'src="data:%s;base64,%s"' % (mt, base64.b64encode(p.read_bytes()).decode())
    preview = re.sub(r'src="/?(images/[^"]+)"', inline, preview)
    Path("/tmp/claude-0/-home-claude/5f3b125d-44b7-5319-9e51-30759c1202f1/scratchpad").mkdir(parents=True, exist_ok=True)
    (Path("/tmp/claude-0/-home-claude/5f3b125d-44b7-5319-9e51-30759c1202f1/scratchpad") / "sedona-wine-tours-preview.html").write_text(preview)

if __name__ == "__main__":
    build()
