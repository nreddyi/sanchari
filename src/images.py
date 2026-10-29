"""Dummy illustration generator. Every image on the site is a local SVG in the
brand palette; the real photo URL is stored alongside so the page can swap it
in when it loads."""

LIVE = "https://darkorchid-pigeon-468832.hostingersite.com/wp-content/uploads/"
DARK = "#53190A"
PEACH = "#F2B07A"
CREAM = "#FFD9BF"

# warm gradient pairs, cycled for variety
PAIRS = [("#C4471A", "#7A1F07"), ("#D0602A", "#8A2A0A"), ("#B23C12", "#5E1A06"),
         ("#C9522A", "#841F06"), ("#B8461A", "#6E1F08"), ("#C85A26", "#7A1F07")]


def _frame(w, h, c1, c2, inner, label):
    lab = ""
    if label:
        base = h * 0.86
        lab = (f'<rect y="{base:.1f}" width="{w}" height="{h-base:.1f}" fill="{DARK}"/>'
               f'<text x="{w/2}" y="{base+(h-base)*0.64:.1f}" text-anchor="middle" '
               f'font-family="Arial,Helvetica,sans-serif" font-weight="bold" font-size="{h*0.036:.1f}" '
               f'fill="{CREAM}" letter-spacing="3">{label.upper().replace("&","&amp;")}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/>'
            f'<stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#g)"/>{inner}{lab}</svg>')


def temple(w, h, c1, c2, label):
    cx = w / 2; base = h * 0.86; tw = w * 0.34; th = h * 0.07; y = base; tiers = ""
    for _ in range(7):
        top = tw * 0.86
        tiers += f'<path d="M{cx-tw/2:.1f} {y:.1f} L{cx-top/2:.1f} {y-th:.1f} L{cx+top/2:.1f} {y-th:.1f} L{cx+tw/2:.1f} {y:.1f} Z"/>'
        tiers += f'<rect x="{cx-tw*0.05:.1f}" y="{y-th*0.75:.1f}" width="{tw*0.1:.1f}" height="{th*0.5:.1f}" rx="3" fill="{c1}" opacity=".6"/>'
        y -= th; tw = top
    tiers += f'<path d="M{cx-tw/2:.1f} {y:.1f} Q{cx:.1f} {y-th*2.2:.1f} {cx+tw/2:.1f} {y:.1f} Z"/><rect x="{cx-3:.1f}" y="{y-th*2.6:.1f}" width="6" height="{th:.1f}" rx="3"/>'
    side = ""
    for sx in (w * 0.15, w * 0.85):
        side += (f'<path d="M{sx-w*.08:.1f} {base:.1f} L{sx-w*.062:.1f} {base-h*.12:.1f} L{sx+w*.062:.1f} {base-h*.12:.1f} L{sx+w*.08:.1f} {base:.1f} Z"/>'
                 f'<path d="M{sx-w*.062:.1f} {base-h*.12:.1f} Q{sx:.1f} {base-h*.22:.1f} {sx+w*.062:.1f} {base-h*.12:.1f} Z"/>')
    inner = (f'<circle cx="{cx}" cy="{h*.4:.1f}" r="{h*.3:.1f}" fill="{PEACH}" opacity=".3"/>'
             f'<circle cx="{cx}" cy="{h*.4:.1f}" r="{h*.19:.1f}" fill="{CREAM}" opacity=".35"/>'
             f'<g fill="{DARK}" opacity=".9">{side}{tiers}</g>')
    return _frame(w, h, c1, c2, inner, label)


def mountain(w, h, c1, c2, label):
    b = h * 0.86
    inner = (f'<circle cx="{w*.72:.1f}" cy="{h*.26:.1f}" r="{h*.11:.1f}" fill="{CREAM}" opacity=".55"/>'
             f'<path d="M0 {b:.1f} L{w*.18:.1f} {h*.5:.1f} L{w*.3:.1f} {h*.62:.1f} L{w*.5:.1f} {h*.2:.1f} L{w*.68:.1f} {h*.55:.1f} L{w*.8:.1f} {h*.42:.1f} L{w} {h*.66:.1f} L{w} {b:.1f} Z" fill="{DARK}" opacity=".85"/>'
             f'<path d="M{w*.44:.1f} {h*.32:.1f} L{w*.5:.1f} {h*.2:.1f} L{w*.56:.1f} {h*.31:.1f} L{w*.53:.1f} {h*.29:.1f} L{w*.5:.1f} {h*.33:.1f} L{w*.47:.1f} {h*.3:.1f} Z" fill="{CREAM}" opacity=".9"/>'
             f'<path d="M{w*.76:.1f} {h*.48:.1f} L{w*.8:.1f} {h*.42:.1f} L{w*.84:.1f} {h*.48:.1f} Z" fill="{CREAM}" opacity=".8"/>'
             f'<path d="M0 {b:.1f} L{w*.25:.1f} {h*.7:.1f} L{w*.45:.1f} {h*.78:.1f} L{w*.7:.1f} {h*.66:.1f} L{w} {h*.76:.1f} L{w} {b:.1f} Z" fill="{DARK}"/>')
    return _frame(w, h, c1, c2, inner, label)


def wellness(w, h, c1, c2, label):
    b = h * 0.86; cx = w / 2
    petals = ""
    for ang in (-50, -25, 0, 25, 50):
        petals += f'<ellipse cx="{cx}" cy="{h*.6:.1f}" rx="{w*.04:.1f}" ry="{h*.14:.1f}" transform="rotate({ang} {cx} {h*.72:.1f})"/>'
    inner = (f'<circle cx="{cx}" cy="{h*.42:.1f}" r="{h*.26:.1f}" fill="{PEACH}" opacity=".35"/>'
             f'<path d="M0 {h*.74:.1f} Q{w*.25:.1f} {h*.62:.1f} {w*.5:.1f} {h*.72:.1f} T{w} {h*.7:.1f} L{w} {b:.1f} L0 {b:.1f} Z" fill="{DARK}" opacity=".55"/>'
             f'<g fill="{CREAM}" opacity=".9">{petals}</g>'
             f'<path d="M0 {h*.8:.1f} Q{w*.3:.1f} {h*.74:.1f} {w*.6:.1f} {h*.8:.1f} T{w} {h*.78:.1f} L{w} {b:.1f} L0 {b:.1f} Z" fill="{DARK}"/>')
    return _frame(w, h, c1, c2, inner, label)


def city(w, h, c1, c2, label):
    b = h * 0.86
    bars = ""
    xs = [0.06, 0.16, 0.24, 0.36, 0.46, 0.6, 0.7, 0.8, 0.9]
    hs = [0.3, 0.45, 0.25, 0.55, 0.35, 0.5, 0.28, 0.42, 0.32]
    for x, hh in zip(xs, hs):
        bars += f'<rect x="{w*x:.1f}" y="{b-h*hh:.1f}" width="{w*0.08:.1f}" height="{h*hh:.1f}"/>'
    inner = (f'<circle cx="{w*.3:.1f}" cy="{h*.28:.1f}" r="{h*.13:.1f}" fill="{CREAM}" opacity=".45"/>'
             f'<g fill="{DARK}" opacity=".85">{bars}</g>')
    return _frame(w, h, c1, c2, inner, label)


def person(w, h, c1, c2, label):
    cx = w / 2
    inner = (f'<circle cx="{cx}" cy="{h*.38:.1f}" r="{h*.16:.1f}" fill="{CREAM}" opacity=".85"/>'
             f'<path d="M{w*.2:.1f} {h} Q{w*.2:.1f} {h*.6:.1f} {cx} {h*.6:.1f} Q{w*.8:.1f} {h*.6:.1f} {w*.8:.1f} {h} Z" fill="{CREAM}" opacity=".85"/>')
    return _frame(w, h, c1, c2, inner, "")


KINDS = {"temple": temple, "mountain": mountain, "wellness": wellness, "city": city, "person": person}

# key: (label, kind, real path under LIVE or None, w, h)
REG = {}
_order = []


def add(key, label, kind, real=None, w=800, h=600):
    REG[key] = (label, kind, real, w, h)
    _order.append(key)


def svg_for(key):
    label, kind, real, w, h = REG[key]
    c1, c2 = PAIRS[_order.index(key) % len(PAIRS)]
    return KINDS[kind](w, h, c1, c2, label)


import os as _os, json as _json
_PMAP_FILE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "content", "photos.json")
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
def local_photo(url):
    """Local copy of a downloaded photo (assets/photos/...), or the URL itself if not downloaded."""
    if _os.environ.get("SANCHARI_NO_PHOTOS") or not url: return url
    global _PMAP
    try: _PMAP
    except NameError:
        _PMAP = _json.load(open(_PMAP_FILE)) if _os.path.exists(_PMAP_FILE) else {}
    p = _PMAP.get(url)
    return p if p and _os.path.exists(_os.path.join(_ROOT, p)) else url

def real_url(key):
    return local_photo(_real_url(key))

def _real_url(key):
    r = REG[key][2]
    if not r: return ""
    if r.startswith("http"): return r
    if r.startswith("assets/"): return r
    return LIVE + r
