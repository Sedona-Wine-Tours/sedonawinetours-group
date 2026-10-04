# -*- coding: utf-8 -*-
"""Social profiles + latest Instagram posts (official embeds) for each division.

build/social_posts.json is refreshed by the weekly task from the Instagram
connector; only permalinks and captions are stored (Instagram image URLs
expire, so the official embed renders the picture in the visitor's browser).
"""
import json, html
from pathlib import Path

HERE = Path(__file__).parent

SOCIAL = {
    "wtos": dict(name="Wine Tours of Sedona", ig="sedonawineguide",
                 links=[("Instagram", "https://www.instagram.com/sedonawineguide/"),
                        ("Facebook", "https://www.facebook.com/482718061891694"),
                        ("LinkedIn", "https://www.linkedin.com/company/64734706/")]),
    "sip": dict(name="SIP Sedona", ig="sipsedona",
                links=[("Instagram", "https://www.instagram.com/sipsedona/"),
                       ("Facebook", "https://www.facebook.com/sipsedona/"),
                       ("LinkedIn", "https://www.linkedin.com/company/114324066/")]),
    "swa": dict(name="Sedona Wine Adventures", ig="sedonawineadventures",
                links=[("Instagram", "https://www.instagram.com/sedonawineadventures/"),
                       ("Facebook", "https://www.facebook.com/sedonawineadventuresWineTours/"),
                       ("LinkedIn", "https://www.linkedin.com/company/60235359/")]),
}
GROUP_LINKS = [("LinkedIn", "https://www.linkedin.com/company/114524044/")]


def same_as():
    urls = [u for d in SOCIAL.values() for _, u in d["links"]] + [u for _, u in GROUP_LINKS]
    return urls


def load_posts():
    return json.load(open(HERE / "social_posts.json"))


def _embed(post, label):
    cap = html.escape(post["caption"].split("\n")[0][:200])
    return (f'<figure class="ig-post"><blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="{post["permalink"]}?utm_source=ig_embed" data-instgrm-version="14">'
            f'<a href="{post["permalink"]}" rel="noopener" target="_blank">View this post on Instagram — {html.escape(label)}</a></blockquote>'
            f'<figcaption><strong>@{label}</strong> · {post["date"]}<br>{cap}</figcaption></figure>')


def follow_buttons(key=None):
    items = [(k, SOCIAL[k]) for k in (["wtos", "sip", "swa"] if key is None else [key])]
    out = ""
    for k, d in items:
        links = " ".join(f'<a class="btn btn-ghost btn-sm" href="{u}" rel="noopener" target="_blank">{n}</a>' for n, u in d["links"])
        out += f'<div class="follow-row"><strong>{d["name"]}</strong> {links}</div>'
    return f'<div class="follow">{out}</div>'


LOADER = '''<script>
(function(){var s=document.getElementById('social');if(!s)return;function load(){if(window.instgrm){window.instgrm.Embeds.process();return}var j=document.createElement('script');j.async=true;j.src='https://www.instagram.com/embed.js';document.body.appendChild(j)}
if('IntersectionObserver' in window){var o=new IntersectionObserver(function(e){if(e[0].isIntersecting){load();o.disconnect()}},{rootMargin:'600px'});o.observe(s)}else{load()}})();
</script>'''


def social_home_html():
    posts = load_posts()
    cards = "".join(_embed(posts[SOCIAL[k]["ig"]][0], SOCIAL[k]["ig"]) for k in ("wtos", "sip", "swa") if posts.get(SOCIAL[k]["ig"]))
    return f'''<section id="social"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Follow along</span><h2>Latest from our three divisions on Instagram</h2></div><p>Real days on the trail, posted by the guides. One feed per division, refreshed weekly — tap any post to see the full gallery, or follow the brand that fits your trip.</p></div>
  <div class="ig-grid">{cards}</div>
  {follow_buttons()}
</div></section>{LOADER}'''


def social_division_html(key, n=3):
    posts = load_posts()
    d = SOCIAL[key]
    cards = "".join(_embed(p, d["ig"]) for p in posts.get(d["ig"], [])[:n])
    return f'''<section id="social"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">@{d["ig"]} on Instagram</span><h2>Latest from {d["name"]}</h2></div><p>What this week looked like from the van. Follow for new stops, specials and the occasional very happy dog.</p></div>
  <div class="ig-grid">{cards}</div>
  {follow_buttons(key)}
</div></section>{LOADER}'''


SOCIAL_CSS = '''
/* Social */
.ig-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.25rem;align-items:start}
@media (max-width:900px){.ig-grid{grid-template-columns:1fr}}
.ig-post{margin:0;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.ig-post blockquote.instagram-media{margin:0!important;min-width:0!important;max-width:100%!important;width:100%!important;border:0!important;box-shadow:none!important;background:transparent!important;min-height:420px}
.ig-post blockquote a{display:block;padding:1.2rem;color:var(--ink-2)}
.ig-post figcaption{padding:.9rem 1.1rem;font-size:.9rem;color:var(--ink-2);border-top:1px solid var(--line)}
.follow{display:grid;gap:.6rem;margin-top:1.4rem}
.follow-row{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;font-size:.95rem}
.follow-row strong{min-width:200px}
.btn-sm{padding:.4rem .8rem;font-size:.85rem}
'''
