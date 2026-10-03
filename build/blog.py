# -*- coding: utf-8 -*-
"""Blog: renders build/posts/*.md (YAML front matter) into site/blog/."""
import re, json, datetime
from pathlib import Path
import markdown, yaml

HERE = Path(__file__).parent
POSTS = HERE / "posts"
SITE = "https://www.sedonawinetours.group"

CTA = '''<aside class="post-cta">
  <span class="eyebrow">Plan the trip</span>
  <h3>Make wine country part of your Sedona visit</h3>
  <p>We've guided Sedona wine tours since 2004 — private all-inclusive, small-group van, or pay-as-you-go. Five questions and we'll match you to the right one.</p>
  <p><a class="btn btn-primary" href="/#chooser">Try the Tour Chooser</a> <a class="btn btn-ghost" href="/sedona-wineries-and-vineyards">Wineries near Sedona</a></p>
</aside>'''

def load_posts():
    posts = []
    for f in sorted(POSTS.glob("*.md")):
        raw = f.read_text()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            continue
        meta = yaml.safe_load(m.group(1)) or {}
        body_md = m.group(2).strip()
        if meta.get("draft"):
            continue
        slug = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f.stem)
        html = markdown.markdown(body_md, extensions=["extra", "toc", "smarty"])
        # open external links in new tab; keep internal relative
        html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener" target="_blank"', html)
        words = len(re.sub(r"<[^>]+>", " ", html).split())
        date = meta.get("date")
        if isinstance(date, (datetime.date, datetime.datetime)):
            date = date.isoformat()[:10]
        posts.append(dict(slug=slug, title=meta["title"], description=meta.get("description", ""), date=str(date),
                          updated=str(meta.get("updated", date)), author=meta.get("author", "Jim Reich"),
                          keywords=meta.get("keywords", []), category=meta.get("category", "Arizona travel"),
                          image=meta.get("image"), image_alt=meta.get("image_alt", ""), html=html, words=words,
                          sources=meta.get("sources", [])))
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts

def nice_date(d):
    y, m, dd = map(int, d.split("-"))
    return datetime.date(y, m, dd).strftime("%B %-d, %Y")

def post_schema(p):
    return {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
            "datePublished": p["date"], "dateModified": p["updated"], "author": {"@type": "Person", "name": p["author"], "url": SITE},
            "publisher": {"@type": "Organization", "name": "Sedona Wine Tours", "url": SITE, "logo": {"@type": "ImageObject", "url": f"{SITE}/images/swt-emblem.webp"}},
            "mainEntityOfPage": f"{SITE}/blog/{p['slug']}", "keywords": ", ".join(p["keywords"]), "wordCount": p["words"],
            **({"image": p["image"] if p["image"].startswith("http") else SITE + p["image"]} if p.get("image") else {})}

def post_body(p, related):
    img = f'<figure class="post-hero"><img src="{p["image"]}" alt="{p["image_alt"]}" loading="eager"></figure>' if p.get("image") else ""
    rel = "".join(f'<li><a href="/blog/{r["slug"]}">{r["title"]}</a><span>{nice_date(r["date"])}</span></li>' for r in related[:4])
    srcs = "".join(f'<li><a href="{s["url"]}" rel="noopener" target="_blank">{s["title"]}</a></li>' for s in p["sources"]) if p["sources"] else ""
    return f'''
<article class="post"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/blog">Arizona travel blog</a> › <span>{p["category"]}</span></nav>
  <header class="post-head">
    <span class="eyebrow">{p["category"]}</span>
    <h1>{p["title"]}</h1>
    <p class="lede">{p["description"]}</p>
    <p class="byline">By {p["author"]} · {nice_date(p["date"])} · {max(1, round(p["words"]/220))} min read</p>
  </header>
  {img}
  <div class="post-grid">
    <div class="post-body">{p["html"]}
      {"<h2>Sources &amp; further reading</h2><ul class='sources'>" + srcs + "</ul>" if srcs else ""}
    </div>
    <div class="post-side">
      {CTA}
      {"<div class='related'><span class='eyebrow'>More from the blog</span><ul>" + rel + "</ul></div>" if rel else ""}
    </div>
  </div>
</div></article>'''

def index_body(posts):
    cards = "".join(f'''<article class="post-card">
  <span class="eyebrow">{p["category"]}</span>
  <h2><a href="/blog/{p["slug"]}">{p["title"]}</a></h2>
  <p>{p["description"]}</p>
  <p class="byline">{nice_date(p["date"])} · {max(1, round(p["words"]/220))} min read</p>
</article>''' for p in posts)
    return f'''
<section class="hero-band"><div class="wrap">
  <div>
    <span class="eyebrow">The Sedona Wine Tours blog</span>
    <h1>Arizona travel, wine country and the Verde Valley — from the guides who drive it daily</h1>
    <p class="lede">A new story every day: where to taste, hike, eat and stay across Sedona and Arizona, written by people who've guided here since 2004. No fluff, real hours, real prices, and the stops we'd send our own families to.</p>
    <p><a class="btn btn-primary" href="/#chooser">Find your wine tour</a> <a class="btn btn-ghost" href="/blog/feed.xml">RSS feed</a></p>
  </div>
  <div class="facts">
    <div><span>Posts</span><strong class="num">{len(posts)}</strong></div>
    <div><span>Cadence</span><strong>Daily</strong></div>
    <div><span>Written by</span><strong>Local guides</strong></div>
    <div><span>Since</span><strong>2004</strong></div>
  </div>
</div></section>
<section><div class="wrap"><div class="post-list">{cards}</div></div></section>'''

def feed_xml(posts):
    items = "".join(f'''<item><title>{esc(p["title"])}</title><link>{SITE}/blog/{p["slug"]}</link><guid>{SITE}/blog/{p["slug"]}</guid><pubDate>{rfc(p["date"])}</pubDate><description>{esc(p["description"])}</description></item>''' for p in posts[:30])
    return f'''<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Sedona Wine Tours — Arizona travel blog</title><link>{SITE}/blog</link><description>Daily stories on Sedona, Arizona wine country and Arizona travel from local guides.</description>{items}</channel></rss>'''

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def rfc(d):
    y, m, dd = map(int, d.split("-"))
    return datetime.datetime(y, m, dd, 14, 0, 0).strftime("%a, %d %b %Y %H:%M:%S +0000")

BLOG_CSS = '''
/* Blog */
.crumbs{font-size:.85rem;color:var(--ink-3);margin-bottom:1.2rem}
.crumbs a{color:var(--ink-2)}
.post{padding:clamp(2rem,5vw,4rem) 0}
.post-head{max-width:76ch;margin-bottom:2rem}
.post-head h1{font-size:clamp(2rem,4.2vw,3.2rem)}
.byline{color:var(--ink-3);font-size:.9rem}
.post-hero{margin:0 0 2rem}
.post-hero img{border-radius:var(--radius);width:100%;aspect-ratio:16/9;object-fit:cover}
.post-grid{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:3rem;align-items:start}
@media (max-width:960px){.post-grid{grid-template-columns:1fr}}
.post-body{max-width:72ch;font-size:1.06rem}
.post-body h2{font-size:1.65rem;margin:2.2rem 0 .7rem}
.post-body h3{font-size:1.25rem;margin:1.6rem 0 .5rem}
.post-body p,.post-body li{line-height:1.7}
.post-body ul,.post-body ol{padding-left:1.3rem}
.post-body blockquote{border-left:4px solid var(--accent);margin:1.4rem 0;padding:.4rem 1.2rem;color:var(--ink-2);font-family:var(--font-display);font-style:italic;font-size:1.15rem}
.post-body table{border-collapse:collapse;width:100%;font-size:.95rem;margin:1.2rem 0}
.post-body th,.post-body td{border-bottom:1px solid var(--line);padding:.6rem .7rem;text-align:left}
.post-body img{border-radius:12px;margin:1rem 0}
.post-body .sources{font-size:.92rem;color:var(--ink-2)}
.post-side{position:sticky;top:90px;display:grid;gap:1.2rem}
.post-cta{background:var(--card);border:1px solid var(--line);border-top:5px solid var(--accent);border-radius:var(--radius);padding:1.4rem}
.post-cta h3{font-size:1.2rem;margin:.2rem 0 .5rem}
.post-cta p{font-size:.93rem;color:var(--ink-2)}
.related ul{list-style:none;padding:0;margin:.5rem 0 0;display:grid;gap:.6rem}
.related li a{display:block;font-weight:600;font-size:.95rem}
.related li span{font-size:.8rem;color:var(--ink-3)}
.post-list{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
@media (max-width:900px){.post-list{grid-template-columns:1fr}}
.post-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:1.4rem;display:flex;flex-direction:column;gap:.5rem}
.post-card h2{font-size:1.25rem}
.post-card h2 a{color:var(--ink);text-decoration:none}
.post-card h2 a:hover{color:var(--accent-ink)}
.post-card p{color:var(--ink-2);font-size:.95rem;margin:0}
'''
