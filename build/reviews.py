# -*- coding: utf-8 -*-
"""Google Business Profile reviews for all three divisions.

Source data: build/gmb_reviews_raw*.json — exports from the Google Business
Profile connector (Windsor.ai). The weekly refresh task re-pulls these files;
this module only curates and renders them.
"""
import json, re, html, datetime
from pathlib import Path

HERE = Path(__file__).parent
SITE = "https://www.sedonawinetours.group"

DIVISIONS = {
    "wtos": dict(name="Wine Tours of Sedona", short="Wine Tours of Sedona", slug="wine-tours-of-sedona.html",
                 account="Wine Tours of Sedona", site="https://www.winetoursofsedona.com",
                 maps="https://maps.google.com/maps?cid=15339961178440993728",
                 review_url="https://search.google.com/local/writereview?placeid=ChIJ", color="var(--syrah)"),
    "sip": dict(name="SIP Sedona", short="SIP Sedona", slug="sip-sedona.html", account="SIP Sedona",
                site="https://sipsedona.com", maps="https://maps.google.com/maps?cid=17983733618338021717",
                review_url="", color="var(--cathedral)"),
    "swa": dict(name="Sedona Wine Adventures", short="Sedona Wine Adventures", slug="sedona-wine-adventures.html",
                account="Sedona Wine Adventures", site="https://www.sedonawineadventures.com",
                maps="https://maps.google.com/maps?cid=8942728630006870401", review_url="", color="var(--verde)"),
}
ACCOUNT_TO_KEY = {v["account"]: k for k, v in DIVISIONS.items()}
STARS = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5}


def _clean(text):
    text = (text or "").replace("\r", "").strip()
    text = re.sub(r"\(Original\).*$", "", text, flags=re.S).replace("(Translated by Google)", "").strip()
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text


def load_reviews():
    rows = []
    for f in sorted(HERE.glob("gmb_reviews_raw*.json")):
        rows += json.load(open(f))["data"]
    seen, out, meta = set(), [], {}
    for r in rows:
        key = ACCOUNT_TO_KEY.get(r.get("account_name"))
        if not key or r["review_id"] in seen:
            continue
        seen.add(r["review_id"])
        m = meta.setdefault(key, {})
        if r.get("review_total_count"):
            m["count"] = int(r["review_total_count"])
        if r.get("review_average_rating_total"):
            m["avg"] = float(r["review_average_rating_total"])
        if r.get("location_metadata_new_review_uri"):
            m["review_url"] = r["location_metadata_new_review_uri"]
        text = _clean(r.get("review_comment"))
        out.append(dict(key=key, id=r["review_id"], name=(r.get("review_reviewer") or "Google user").strip(),
                        stars=STARS.get(r.get("review_star_rating"), 5), text=text,
                        date=r["review_create_time"][:10]))
    for k, m in meta.items():
        DIVISIONS[k].update({kk: vv for kk, vv in m.items()})
    out.sort(key=lambda x: x["date"], reverse=True)
    return out


def curated(reviews, key=None, n=None, min_len=100):
    sel = [r for r in reviews if r["stars"] == 5 and len(r["text"]) >= min_len and (key is None or r["key"] == key)]
    return sel[:n] if n else sel


def nice_date(d):
    y, m, dd = map(int, d.split("-"))
    return datetime.date(y, m, dd).strftime("%B %Y")


def _excerpt(text, limit=320):
    t = html.escape(text)
    if len(t) <= limit:
        return t.replace("\n", "<br>")
    cut = t[:limit].rsplit(" ", 1)[0].rstrip(",.;:—-")
    return cut.replace("\n", "<br>") + "…"


def review_card(r, show_division=True, limit=320):
    d = DIVISIONS[r["key"]]
    div = f' · <a href="{d["slug"]}">{d["short"]}</a>' if show_division else ""
    return (f'<div class="review" data-division="{r["key"]}">'
            f'<div class="stars" aria-label="Five stars">★★★★★</div>'
            f'<blockquote>“{_excerpt(r["text"], limit)}”</blockquote>'
            f'<cite>{html.escape(r["name"])} · Google review, {nice_date(r["date"])}{div}</cite></div>')


def aggregate_chips(keys=("wtos", "sip", "swa")):
    chips = ""
    for k in keys:
        d = DIVISIONS[k]
        if d.get("count"):
            chips += (f'<a class="agg" href="{d["maps"]}" rel="noopener" target="_blank">'
                      f'<span class="stars">★★★★★</span><span><strong>{d["avg"]:.1f}</strong> · {d["count"]} Google reviews</span>'
                      f'<small>{d["short"]}</small></a>')
    return f'<div class="agg-row">{chips}</div>'


def reviews_home_html(reviews):
    cards = "".join(review_card(r, limit=220) for k in ("wtos", "sip", "swa") for r in curated(reviews, k, 2))
    return f'''<section id="reviews"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Guest reviews</span><h2>What our guests say about all three divisions</h2></div><p>Pulled straight from our Google Business Profiles and refreshed weekly. Wine Tours of Sedona has been voted Readers' Choice Best of the Best two years running and holds TripAdvisor's Travelers' Choice award.</p></div>
  {aggregate_chips()}
  <div class="reviews">{cards}</div>
  <p style="margin-top:1.2rem"><a class="btn btn-ghost" href="reviews.html">Read more guest reviews</a></p>
</div></section>'''


def reviews_division_html(reviews, key, n=3):
    d = DIVISIONS[key]
    cards = "".join(review_card(r, show_division=False) for r in curated(reviews, key, n))
    leave = f' <a class="btn btn-ghost" href="{d["review_url"]}" rel="noopener" target="_blank">Leave a review</a>' if d.get("review_url") else ""
    return f'''<section id="reviews"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Google reviews</span><h2>What guests say about {d["name"]}</h2></div><p>{d.get("avg", 5):.1f} stars across {d.get("count", 0)} Google reviews. These are the most recent, word for word.</p></div>
  <div class="reviews">{cards}</div>
  <p style="margin-top:1.2rem"><a class="btn btn-primary" href="{d["maps"]}" rel="noopener" target="_blank">Read all {d.get("count", "")} reviews on Google</a>{leave} <a class="btn btn-ghost" href="reviews.html#{key}">All divisions</a></p>
</div></section>'''


def reviews_page_body(reviews, per_division=24):
    sections = ""
    for k in ("wtos", "sip", "swa"):
        d = DIVISIONS[k]
        cards = "".join(review_card(r, show_division=False, limit=600) for r in curated(reviews, k, per_division))
        leave = f' <a class="btn btn-ghost" href="{d["review_url"]}" rel="noopener" target="_blank">Leave a review for {d["short"]}</a>' if d.get("review_url") else ""
        sections += f'''<section id="{k}" class="review-group" data-division="{k}"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">{d["name"]}</span><h2>{d["name"]} reviews</h2></div><p>{d.get("avg", 5):.1f}★ · {d.get("count", 0)} Google reviews · <a href="{d["slug"]}">About this division</a></p></div>
  <div class="reviews">{cards}</div>
  <p style="margin-top:1.2rem"><a class="btn btn-primary" href="{d["maps"]}" rel="noopener" target="_blank">Read all on Google</a>{leave}</p>
</div></section>'''
    total = sum(DIVISIONS[k].get("count", 0) for k in DIVISIONS)
    return f'''<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">Guest reviews · all three divisions</span>
    <h1>Sedona wine tour reviews from {total:,} Google guests</h1>
    <p class="lede">Every review below is a real Google review of one of our three divisions — Wine Tours of Sedona, SIP Sedona and Sedona Wine Adventures — shown word for word and refreshed weekly. We've labeled each one with the division it describes, because the formats are different and the right fit depends on how you like to travel.</p>
    <div class="actions"><a class="btn btn-primary" href="index.html#chooser">Find the right tour for me</a><a class="btn btn-ghost" href="index.html#divisions">Compare the divisions</a></div>
  </div>
  <div class="facts">
    <div><span>Google rating</span><strong class="num">{DIVISIONS["wtos"].get("avg", 4.9):.1f}★</strong></div>
    <div><span>Reviews</span><strong class="num">{total:,}</strong></div>
    <div><span>Guiding since</span><strong>2004</strong></div>
    <div><span>Divisions</span><strong>3</strong></div>
  </div>
</div></section>
<section><div class="wrap">
  {aggregate_chips()}
  <div class="filter-row" role="tablist" aria-label="Filter reviews by division">
    <button class="chip on" data-filter="all" aria-pressed="true">All divisions</button>
    <button class="chip" data-filter="wtos" aria-pressed="false">Wine Tours of Sedona</button>
    <button class="chip" data-filter="sip" aria-pressed="false">SIP Sedona</button>
    <button class="chip" data-filter="swa" aria-pressed="false">Sedona Wine Adventures</button>
  </div>
</div></section>
{sections}
<script>
(function(){{var b=document.querySelectorAll('.filter-row .chip'),g=document.querySelectorAll('.review-group');
b.forEach(function(x){{x.addEventListener('click',function(){{b.forEach(function(y){{y.classList.remove('on');y.setAttribute('aria-pressed','false')}});x.classList.add('on');x.setAttribute('aria-pressed','true');var f=x.dataset.filter;g.forEach(function(s){{s.style.display=(f==='all'||s.dataset.division===f)?'':'none'}})}})}});
if(location.hash){{var t=document.querySelector('.chip[data-filter="'+location.hash.slice(1)+'"]');if(t)t.click()}}}})();
</script>'''


def reviews_schema(reviews, key=None, n=10):
    """AggregateRating + a handful of Review items for a division (or all)."""
    keys = [key] if key else list(DIVISIONS)
    out = []
    for k in keys:
        d = DIVISIONS[k]
        if not d.get("count"):
            continue
        out.append({"@context": "https://schema.org", "@type": "TouristTrip", "name": f"{d['name']} wine tours",
                    "provider": {"@type": "Organization", "name": d["name"], "url": d["site"]},
                    "url": f"{SITE}/{d['slug'][:-5]}",
                    "aggregateRating": {"@type": "AggregateRating", "ratingValue": d["avg"], "reviewCount": d["count"], "bestRating": 5},
                    "review": [{"@type": "Review", "author": {"@type": "Person", "name": r["name"]}, "datePublished": r["date"],
                                "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5}, "reviewBody": r["text"][:500]}
                               for r in curated(reviews, k, n)]})
    return out


REVIEWS_CSS = '''
/* Review aggregates & filters */
.agg-row{display:flex;flex-wrap:wrap;gap:.8rem;margin:0 0 1.4rem}
.agg{display:flex;flex-direction:column;gap:.1rem;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:.8rem 1.1rem;text-decoration:none;color:var(--ink);font-size:.95rem;min-width:200px}
.agg strong{font-size:1.15rem}
.agg small{color:var(--ink-3);font-size:.8rem}
.agg .stars{font-size:.8rem}
.filter-row{display:flex;flex-wrap:wrap;gap:.5rem;margin:.4rem 0 .5rem}
.chip{border:1px solid var(--line);background:var(--card);color:var(--ink-2);border-radius:999px;padding:.45rem .95rem;font:inherit;font-size:.9rem;cursor:pointer}
.chip.on{background:var(--ink);color:var(--ground);border-color:var(--ink)}
.review-group{padding-top:1rem}
.review cite a{color:var(--ink-2)}
'''
