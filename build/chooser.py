# -*- coding: utf-8 -*-
"""Tour Chooser: catalogue + quiz markup/JS for the homepage."""
import json

FH = "https://fareharbor.com/embeds/book/winetoursofsedona/items/{}/?full-items=yes"
SWA = "https://www.sedonawineadventures.com/reservations/"

# tags: party (couple, friends, group, solo) · style (allin, payg, social) · hours · drink (wine, mixed, beer, none, choc)
# want (food, vineyards, towns, activity, events, home)
TOURS = [
  dict(n="A Multi-Vineyard &amp; Winery Tasting Experience", d="wtos", p="$225", h=3, u=FH.format(214320), style="allin", drink=["wine"], want=["vineyards"], party=["couple","friends","group","solo"], desc="Two flights at Page Springs–area estate vineyards. Tastings included, private vehicle."),
  dict(n="Alcantara Estate Vineyard Tasting Experience", d="wtos", p="$225", h=3, u=FH.format(214307), style="allin", drink=["wine"], want=["vineyards","food"], party=["couple","friends","solo"], desc="VIP tasting and charcuterie at the riverside estate where Oak Creek meets the Verde."),
  dict(n="A Taste of “Old Town” Cottonwood", d="wtos", p="$225", h=3, u=FH.format(214346), style="allin", drink=["wine","mixed","beer"], want=["towns"], party=["couple","friends","group","solo"], desc="Two flights of wine, beer or spirits among Old Town's nine tasting rooms."),
  dict(n="The Flavors of Historic Jerome", d="wtos", p="$300", h=4, u=FH.format(214355), style="allin", drink=["wine"], want=["towns"], party=["couple","friends","group"], desc="Three flights in a copper-mining town on Cleopatra Hill."),
  dict(n="The Terroir of the Verde Valley Wine Trail", d="wtos", p="$375", h=5, u=FH.format(214370), style="allin", drink=["wine"], want=["vineyards"], party=["couple","friends","group"], desc="Four vineyard tastings chosen for your palate. Our wine lover's pick."),
  dict(n="Views of Vineyards", d="wtos", p="$375", h=5, u=FH.format(281356), style="allin", drink=["wine"], want=["vineyards","food"], party=["couple","friends"], desc="Alcantara and DA Ranch, two tastings and a charcuterie plate each."),
  dict(n="Sedona &amp; Verde Valley: Wine, Beer, Raw Chocolate &amp; Lunch", d="wtos", p="$444", h=5, u=FH.format(218228), style="allin", drink=["wine","mixed","beer","choc"], want=["food","towns","vineyards"], party=["couple","friends","group"], desc="Four flights, chocolate and lunch, anywhere in the Verde Valley. Our most popular tour."),
  dict(n="An Evening in Old Town", d="wtos", p="$444", h=4, u=FH.format(292881), style="allin", drink=["wine"], want=["food","towns"], party=["couple","friends"], desc="Three flights, dinner at Merkin and a bottle per couple."),
  dict(n="Date Night with Dinner", d="wtos", p="$777 / couple", h=5, u=FH.format(282128), style="allin", drink=["wine"], want=["food","vineyards"], party=["couple"], desc="DA Ranch tasting, chocolates and a full dinner at Up The Creek. Proposal-friendly."),
  dict(n="Rock Star Wine Tour", d="wtos", p="$555", h=5, u=FH.format(234412), style="allin", drink=["wine"], want=["food","towns"], party=["couple","friends","group"], desc="Merkin, Caduceus and Four Eight Wineworks, with lunch and handmade pasta."),
  dict(n="A Sedona Wine Lover's Experience", d="wtos", p="$525", h=7, u=FH.format(214374), style="allin", drink=["wine"], want=["vineyards","towns"], party=["couple","friends","group"], desc="Five flights anywhere in the Verde Valley — the full-day immersion."),
  dict(n="Sedona &amp; Wine Bachelorette Special Tour", d="wtos", p="$600", h=8, u=FH.format(214382), style="allin", drink=["wine","mixed","beer"], want=["food","towns","vineyards"], party=["friends","group"], desc="Six flights and lunch, eight hours, entirely on the group's schedule."),
  dict(n="Verde Valley Brewery Tour", d="wtos", p="$300", h=4, u="https://winetoursofsedona.com/scenic-micro-brewery-tours/", style="allin", drink=["beer"], want=["towns"], party=["couple","friends","group","solo"], desc="Two to four flights at every Verde Valley brewery."),
  dict(n="Sedona &amp; Raw Chocolate Charade", d="wtos", p="$225", h=3, u="https://winetoursofsedona.com/", style="allin", drink=["choc","none"], want=["activity"], party=["couple","friends","group","solo"], desc="Three raw chocolates and the red rocks. Kids 15 and under free."),
  dict(n="Sedona Magical Vortex Tour", d="wtos", p="$300", h=4, u="https://winetoursofsedona.com/", style="allin", drink=["none"], want=["activity","vineyards"], party=["couple","friends","group","solo"], desc="Airport, Bell, Boynton and Cathedral — no tastings, all scenery."),
  dict(n="Vines &amp; Vistas: Kayak and Wine Experience", d="wtos", p="$666", h=7, u="https://winetoursofsedona.com/tour-packages/", style="allin", drink=["wine"], want=["activity","vineyards","food"], party=["couple","friends"], desc="Kayak the Verde River, then wine, charcuterie and lunch."),
  dict(n="Palette &amp; Pour: Wine Tasting and Painting", d="wtos", p="$375", h=5, u="https://winetoursofsedona.com/tour-packages/", style="allin", drink=["wine"], want=["activity","food"], party=["couple","friends","group"], desc="Two flights, charcuterie, a bottle per couple and a painting class."),
  dict(n="The Sedona Cellar Experience (in-home tasting)", d="wtos", p="Call for pricing", h=2, u=FH.format(752593), style="allin", drink=["wine"], want=["home"], party=["couple","friends","group"], desc="Our guide brings the flight to your vacation rental or suite."),
  dict(n="3-Hour Tasting Adventure", d="sip", p="$90 + 18%", h=3, u="https://sipsedona.com/tours/3-hour-tasting-adventure/", style="social", drink=["wine"], want=["vineyards"], party=["couple","friends","solo"], desc="Oak Creek Vineyard and Cove Mesa on a small-group van; tastings paid as you go."),
  dict(n="4-Hour SIP &amp; Savor Tour", d="sip", p="$120 + 18%", h=4, u="https://sipsedona.com/tours/4-hour-sip-savor-tour/", style="social", drink=["wine"], want=["food","vineyards","towns"], party=["couple","friends","solo"], desc="Alcantara, Merkin's trattoria and Arizona Stronghold."),
  dict(n="5-Hour Wine, Beer &amp; Beyond Experience", d="sip", p="$150 + 18%", h=5, u="https://sipsedona.com/", style="social", drink=["wine","mixed","beer"], want=["towns","vineyards"], party=["couple","friends","group","solo"], desc="The wider valley loop; book the whole van private for $500."),
  dict(n="8-Hour SIP All Day Experience", d="sip", p="$240 + 18%", h=8, u="https://sipsedona.com/tours/8-hour-sip-all-day-experience/", style="social", drink=["wine"], want=["vineyards","towns"], party=["friends","group","solo"], desc="Seven stops from The Art of Wine to Arizona Stronghold."),
  dict(n="Wedding &amp; event shuttles (10–33 passengers)", d="sip", p="from $250 / hour", h=3, u="https://sipsedona.com/all-shuttles/", style="social", drink=["wine","mixed","beer","none"], want=["events"], party=["group","big"], desc="Coordinated pickups between hotels, ceremony and reception."),
  dict(n="A Sedona Quickie", d="swa", p="$95 + 18%", h=1.5, u=SWA, style="payg", drink=["wine"], want=["towns"], party=["couple","friends","solo"], desc="Ninety private minutes at The Art of Wine."),
  dict(n="Chapels, Where the Rivers Meet, &amp; Wine", d="swa", p="$150 + 18%", h=3, u=SWA, style="payg", drink=["wine"], want=["vineyards"], party=["couple","friends","solo"], desc="Alcantara at the river confluence, private and at your pace."),
  dict(n="Ranching Turned Into Wine: Perspectives of DA Ranch", d="swa", p="$250 + 18%", h=4, u=SWA, style="payg", drink=["wine"], want=["vineyards"], party=["couple","friends","group"], desc="A cattle ranch turned vineyard; vineyard tour or two glasses by season."),
  dict(n="Verde Valley Spirits", d="swa", p="$250 + 18%", h=5, u=SWA, style="payg", drink=["mixed"], want=["towns"], party=["couple","friends","group"], desc="Craft distilleries from Spirits &amp; Spice to Old Town's newest."),
  dict(n="Everybody's “ABT” — Adult Beverage Tour", d="swa", p="$300 + 18%", h=6, u=SWA, style="payg", drink=["mixed","beer","wine"], want=["towns","vineyards"], party=["friends","group"], desc="Wine, beer, spirits, cider and mead — for a group that can't agree."),
]

DIV = {"wtos": ("Wine Tours of Sedona", "brand-wtos", "/wine-tours-of-sedona"), "sip": ("SIP Sedona", "brand-sip", "/sip-sedona"), "swa": ("Sedona Wine Adventures", "brand-swa", "/sedona-wine-adventures")}

QUESTIONS = [
  ("party", "Who's coming?", [("couple","Just the two of us"),("friends","A few friends (3–5)"),("group","A group of 6–14"),("big","15 or more"),("solo","Just me")]),
  ("style", "How do you like to travel?", [("allin","All-inclusive — tastings paid, nothing to think about"),("payg","Private, but I'll pay tastings as I go"),("social","Social and budget-friendly — a small-group van is fine"),("any","Show me everything")]),
  ("hours", "How much of the day?", [("short","A quick taste (90 min – 3 hrs)"),("half","Most of an afternoon (4–5 hrs)"),("full","Make a day of it (6+ hrs)")]),
  ("drink", "What are you drinking?", [("wine","Wine, please"),("mixed","Wine, beer and spirits"),("beer","Craft beer"),("choc","Chocolate (and maybe wine)"),("none","Not drinking — scenery and stories")]),
  ("want", "The one thing it has to have", [("food","Food that matches the wine"),("vineyards","Vineyards and big views"),("towns","Historic towns — Cottonwood, Jerome"),("activity","An activity — kayak, paint, hike"),("events","Transportation for a wedding or event"),("home","A tasting at our rental — no driving")]),
]

def chooser_html():
    qs = ""
    for i, (key, label, opts) in enumerate(QUESTIONS):
        btns = "".join(f'<button type="button" class="opt" data-k="{key}" data-v="{v}">{t}</button>' for v, t in opts)
        qs += f'<fieldset class="q" data-step="{i}" {"" if i == 0 else "hidden"}><legend><span class="step">{i+1} of {len(QUESTIONS)}</span>{label}</legend><div class="opts">{btns}</div></fieldset>'
    data = json.dumps([dict(t, div=DIV[t["d"]][0], cls=DIV[t["d"]][1], page=DIV[t["d"]][2]) for t in TOURS], ensure_ascii=False)
    return f'''
<section id="chooser" class="chooser-wrap"><div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Tour Chooser</span><h2>Not sure which Sedona wine tour to book? Answer five questions.</h2></div><p>There are more than thirty ways to taste the Verde Valley with us. Tell us who's coming and what you love, and we'll point you to the three best fits — with booking links.</p></div>
  <div class="chooser" id="tour-chooser">
    <form onsubmit="return false">{qs}</form>
    <div class="chooser-nav"><button type="button" class="btn btn-ghost" id="ch-back" hidden>← Back</button><button type="button" class="btn btn-ghost" id="ch-reset" hidden>Start over</button></div>
    <div id="ch-results" hidden></div>
  </div>
</div></section>
<script>
(function(){{
  var T={data};
  var A={{}};var step=0;var root=document.getElementById('tour-chooser');if(!root)return;
  var qs=root.querySelectorAll('.q');var back=document.getElementById('ch-back');var reset=document.getElementById('ch-reset');var res=document.getElementById('ch-results');
  function show(i){{qs.forEach(function(q,j){{q.hidden=j!==i;}});step=i;back.hidden=i===0;reset.hidden=false;res.hidden=true;if(i===0)reset.hidden=true;}}
  root.querySelectorAll('.opt').forEach(function(b){{b.addEventListener('click',function(){{
    var k=b.dataset.k,v=b.dataset.v;A[k]=v;
    b.parentNode.querySelectorAll('.opt').forEach(function(o){{o.classList.toggle('on',o===b)}});
    if(step<qs.length-1){{show(step+1);}} else {{render();}}
  }});}});
  back.addEventListener('click',function(){{if(step>0)show(step-1);}});
  reset.addEventListener('click',function(){{A={{}};root.querySelectorAll('.opt.on').forEach(function(o){{o.classList.remove('on')}});show(0);}});
  function score(t){{
    var s=0;
    if(A.party==='big')return t.want.indexOf('events')>-1?50:-1;
    if(t.party.indexOf(A.party)>-1)s+=3;else s-=4;
    if(A.style!=='any'){{if(t.style===A.style)s+=5;else s-=3;}}
    var h=t.h;var band=h<=3?'short':(h<=5?'half':'full');if(band===A.hours)s+=4;else if((band==='half'&&A.hours!=='full')||(band==='short'&&A.hours==='half'))s+=1;else s-=2;
    if(t.drink.indexOf(A.drink)>-1)s+=5;else if(A.drink==='wine'&&t.drink.indexOf('mixed')>-1)s+=1;else if(A.drink==='none')s-=12;else s-=5;
    if(t.want.indexOf(A.want)>-1)s+=6;else if(A.want==='events'||A.want==='home')s-=8;
    if(A.want==='home'&&t.want.indexOf('home')>-1)s+=20;
    return s;
  }}
  function esc(s){{return s;}}
  function render(){{
    qs.forEach(function(q){{q.hidden=true;}});back.hidden=false;reset.hidden=false;
    var ranked=T.map(function(t){{return [score(t),t]}}).filter(function(x){{return x[0]>-1}}).sort(function(a,b){{return b[0]-a[0]}}).slice(0,3);
    var html='';
    if(A.party==='big'){{
      html+='<div class="ch-note"><h3>Fifteen or more? Let\\'s talk.</h3><p>We seat up to 33 in one coach and run multiple vehicles for larger parties, with a 20% group rate and step-on guide options. One call sorts it in five minutes.</p><p><a class="btn btn-primary" href="tel:+19285042445">Call (928) 504-2445</a> <a class="btn btn-ghost" href="/groups-corporate-weddings">Group tours &amp; weddings</a></p></div>';
    }}
    if(ranked.length){{
      html+='<h3 class="ch-title">Your best fits</h3><div class="tours">'+ranked.map(function(x){{var t=x[1];return '<article class="tour '+t.cls+'"><div class="meta"><span>'+(t.h<2?'90 min':t.h+' hours')+'</span><span>'+t.div+'</span></div><h3>'+t.n+'</h3><div class="price num">'+t.p+'</div><p>'+t.desc+'</p><div class="actions"><a class="btn btn-primary" href="'+t.u+'" rel="noopener">'+(t.u.indexOf('fareharbor')>-1?'Book now':'See &amp; book')+'</a> <a class="btn btn-ghost" href="'+t.page+'">About '+t.div+'</a></div></article>';}}).join('')+'</div>';
      html+='<p class="ch-foot">Not quite right? <a href="#" id="ch-again">Change an answer</a>, browse <a href="#packages">every package</a>, or call <a href="tel:+19285042445">(928) 504-2445</a> and a human will match you in two minutes.</p>';
    }} else if(A.party!=='big'){{
      html+='<div class="ch-note"><h3>That\\'s a custom day — and we love those.</h3><p>Call <a href="tel:+19285042445">(928) 504-2445</a> and we\\'ll build it.</p></div>';
    }}
    res.innerHTML=html;res.hidden=false;
    var ag=document.getElementById('ch-again');if(ag)ag.addEventListener('click',function(e){{e.preventDefault();show(0);}});
    res.scrollIntoView({{behavior:'smooth',block:'start'}});
  }}
}})();
</script>
'''

CHOOSER_CSS = '''
/* Tour Chooser */
.chooser-wrap{background:var(--ground-2)}
.chooser{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:clamp(1.4rem,3vw,2.4rem);box-shadow:var(--shadow)}
.chooser fieldset{border:0;margin:0;padding:0}
.chooser legend{font-family:var(--font-display);font-size:1.5rem;font-weight:600;margin-bottom:1.1rem;padding:0}
.chooser legend .step{display:block;font-family:var(--font-body);font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-ink);font-weight:700;margin-bottom:.3rem}
.chooser .opts{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.7rem}
.chooser .opt{font:inherit;font-weight:500;text-align:left;padding:.95rem 1.1rem;border:1.5px solid var(--line);border-radius:12px;background:var(--ground);color:var(--ink);cursor:pointer;transition:border-color .15s,transform .15s}
.chooser .opt:hover{border-color:var(--accent);transform:translateY(-1px)}
.chooser .opt.on{border-color:var(--accent);background:var(--accent-soft);color:var(--accent-ink)}
.chooser-nav{display:flex;gap:.6rem;margin-top:1.2rem}
.ch-title{font-size:1.5rem;margin:.4rem 0 1rem}
.ch-note{background:var(--accent-soft);border-radius:12px;padding:1.3rem 1.5rem;margin-bottom:1.2rem}
.ch-note h3{margin-bottom:.4rem}
.ch-foot{margin-top:1.2rem;color:var(--ink-2);font-size:.95rem}
'''
