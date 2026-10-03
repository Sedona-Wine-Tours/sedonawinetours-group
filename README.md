# sedonawinetours.group

Source for www.sedonawinetours.group (Sedona Wine Tours — Wine Tours of Sedona, SIP Sedona, Sedona Wine Adventures).

- `build/content.py` — every page's copy and prices (edit here)
- `build/specials.json` — homepage "This month" specials (weekly)
- `build/chooser.py` — Tour Chooser catalogue and quiz
- `build/build.py` — regenerates `site/` (`python3 build/build.py`)
- `site/` — the deployed static site (GoDaddy cPanel pulls this folder via `.cpanel.yml`)
