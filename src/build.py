"""Static site generator for the Sanchari website.
Usage: python3 build.py <output dir>"""
import os, sys, shutil, html
sys.path.insert(0, os.path.dirname(__file__))
import images as IM
from data import DEST_IMG, ZONES, TOURS, CATS, POSTS, CREDITS

HERE = os.path.dirname(os.path.abspath(__file__))
import time
VER = time.strftime("%Y%m%d%H%M")
OUT = sys.argv[1]
LIVE = "https://darkorchid-pigeon-468832.hostingersite.com"
PHONE = "+91 73374 28436"; TEL = "+917337428436"; EMAIL = "info@sanchari.travel"
HOURS = "Mon – Fri: 08:00 – 20:00"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">'
E = html.escape

def inr(n): return "₹" + f"{n:,}".replace(",", "X").replace("X", ",") if n < 100000 else "₹" + _lakh(n)
def _lakh(n):
    s = str(n); last3 = s[-3:]; rest = s[:-3]; parts = []
    while len(rest) > 2: parts.insert(0, rest[-2:]); rest = rest[:-2]
    if rest: parts.insert(0, rest)
    return ",".join(parts + [last3])

# ------------------------------------------------------------ icons
P = {
 "temple": '<path d="M3 21h18M5 21V9l7-6 7 6v12M9 21v-6h6v6"/>',
 "map": '<path d="M9 20l-5.5-3V4L9 7m0 13l6-3m-6 3V7m6 10l5.5 3V7L15 4m0 13V4M9 7l6-3"/>',
 "pin": '<path d="M12 22s-8-7.6-8-13a8 8 0 0 1 16 0c0 5.4-8 13-8 13z"/><circle cx="12" cy="9" r="3"/>',
 "car": '<rect x="1" y="6" width="15" height="11" rx="2"/><path d="M16 9h4l3 3v5h-7"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
 "meal": '<path d="M3 11h18M5 11a7 7 0 0 1 14 0M12 4V2M4 15h16l-1 5H5z"/>',
 "boat": '<path d="M2 18c2 2 4 2 6 0 2 2 4 2 6 0 2 2 4 2 6 0M4 14l2-6h12l2 6M12 8V3l5 3"/>',
 "wave": '<path d="M2 12c2-3 4-3 6 0s4 3 6 0 4-3 6 0M2 18c2-3 4-3 6 0s4 3 6 0 4-3 6 0M2 6c2-3 4-3 6 0s4 3 6 0 4-3 6 0"/>',
 "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "peak": '<path d="m8 3 4 8 5-5 5 15H2L8 3z"/>',
 "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "user": '<circle cx="12" cy="7" r="4"/><path d="M5.5 21a6.5 6.5 0 0 1 13 0"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "cert": '<circle cx="12" cy="8" r="6"/><path d="M8.2 13.2 7 22l5-3 5 3-1.2-8.8"/>',
 "home": '<path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/>',
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 0 0 0-7.8z"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
 "chat": '<path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.2A8.4 8.4 0 0 1 12 3a8.4 8.4 0 0 1 9 8.5z"/>',
 "sliders": '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
 "smile": '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2M9 9h.01M15 9h.01"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
 "compass": '<circle cx="12" cy="12" r="10"/><path d="m16.2 7.8-2.1 6.3-6.3 2.1 2.1-6.3z"/>',
 "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
 "headset": '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1v-6h3zM3 19a2 2 0 0 0 2 2h1v-6H3z"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
 "access": '<circle cx="12" cy="4" r="2"/><path d="M19 13v-2c-1.5 0-3-.5-4-1.5l-1.3-1.4c-.4-.4-.9-.6-1.4-.6H11c-.5 0-1 .2-1.4.6L7 11v4h2l1-2.5V22M14 22v-5l-2-2"/>',
}
def ic(name, sw="2"): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}">{P[name]}</svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1l-.9 1.2c-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.4-1.5-.9-.8-1.5-1.8-1.6-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5v-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5 2.5 1 3 .8 3.6.8.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.7 17.9L0 24l6.3-1.7a11.8 11.8 0 0 0 5.7 1.4A11.8 11.8 0 0 0 20.4 3.6z"/></svg>'
def wa(msg): return "https://wa.me/" + TEL.lstrip("+") + "?text=" + msg.replace(" ", "%20").replace("’", "%27").replace("'", "%27").replace(",", "%2C")

def img(key, alt="", cls=""):
    real = IM.real_url(key)
    r = f' data-real="{real}"' if real else ""
    c = f' class="{cls}"' if cls else ""
    return f'<img src="assets/img/{key}.svg"{r} alt="{E(alt or IM.REG[key][0] or "Sanchari")}"{c}>'

# ------------------------------------------------------------ layout
NAV = [("Home", "index.html"), ("About Us", "about-us.html"), ("Temple", "temple-tours.html"),
       ("Adventure", "adventure-tours.html"), ("Wellness", "wellness-tours.html"), ("Blog", "blog.html"), ("Contact", "contact.html")]

def header(active):
    items = "".join(f'<li><a href="{h}"{" class=\"active\"" if n == active else ""}>{n}</a></li>' for n, h in NAV)
    mitems = "".join(f'<a href="{h}">{n}</a>' for n, h in NAV)
    return f'''
<div class="topbar"><div class="wrap">
  <div class="l"><a href="tel:{TEL}">{ic("phone")}{PHONE}</a><a href="mailto:{EMAIL}">{ic("mail")}{EMAIL}</a></div>
  <div class="r"><span>{ic("clock")}{HOURS}</span><span>Hyderabad, India</span></div>
</div></div>
<header class="site"><div class="wrap">
  <a href="index.html" class="logo" aria-label="Sanchari home"><img src="assets/img/logo-white.png" alt="Sanchari" class="logo-img" width="991" height="271"></a>
  <nav class="main" aria-label="Main"><ul>{items}</ul></nav>
  <div class="h-actions">
    <button type="button" class="login" data-auth="login" aria-haspopup="dialog">{ic("user")}Login</button>
    <a href="contact.html#enquire" class="btn btn-gold">Plan My Trip</a>
    <button class="menu-btn" aria-label="Open menu"><svg class="mb-open" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg><svg class="mb-close" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
  </div>
</div></header>
<div class="m-nav" id="mnav">{mitems}<button type="button" class="m-login" data-auth="login">Login / Sign Up</button><a href="contact.html#enquire" class="btn btn-gold">Plan My Trip</a></div>
'''

SOCIAL = '''<div class="social">
  <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8z"/></svg></a>
  <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a>
  <a href="#" aria-label="X"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.8 3h3.3l-7.2 8.2L22.4 21h-6.6l-5.2-6.8L4.6 21H1.3l7.7-8.8L.9 3h6.8l4.7 6.2L17.8 3zm-1.2 16h1.8L6.5 4.9H4.6L16.6 19z"/></svg></a>
  <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1c.4-1.6.5-3.2.5-4.8s-.1-3.2-.5-4.8zM9.7 15V9l5.8 3-5.8 3z"/></svg></a>
</div>'''

def footer(wa_msg="Hi Sanchari, I'd like to plan a trip."):
    return f'''
<section class="nl no-print" aria-labelledby="nlTitle">
  <div class="wrap nl-in">
    <div class="nl-copy">
      <span class="nl-ico">{ic("mail", "1.8")}</span>
      <div><h2 id="nlTitle">Subscribe to our newsletter</h2><p>New yatras, departure dates and travel tips — straight to your inbox.</p></div>
    </div>
    <form class="nl-form" id="nlForm" novalidate>
      <label for="nlEmail" class="sr-only">Email address</label>
      <input id="nlEmail" type="email" required autocomplete="email" placeholder="Enter your email address">
      <button class="btn btn-dark" type="submit">Subscribe {ic("arrow")}</button>
      <p class="nl-msg" id="nlMsg" role="status" aria-live="polite"></p>
    </form>
  </div>
</section>
<footer><div class="wrap">
  <div class="f-grid">
    <div>
      <a href="index.html" class="logo" aria-label="Sanchari home"><img src="assets/img/logo-white.png" alt="Sanchari" class="logo-img" width="991" height="271"></a>
      <p class="f-about">Hyderabad-based travel company crafting temple, adventure and wellness journeys — planned with care, delivered with comfort.</p>
      {SOCIAL}
    </div>
    <div><h4>Company</h4><ul><li><a href="about-us.html">About Us</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="account.html">My Account</a></li></ul></div>
    <div><h4>Policies</h4><ul><li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="terms-and-conditions.html">Terms &amp; Conditions</a></li><li><a href="cancellation-refund-policy.html">Cancellation &amp; Refund</a></li><li><a href="photo-credits.html">Photo Credits</a></li></ul></div>
    <div><h4>Contact</h4><ul><li>Hyderabad, Telangana, India</li><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{HOURS}</li></ul></div>
  </div>
  <div class="f-bottom"><span>© 2026 Sanchari Travel. All rights reserved.</span><div class="pay"><span>VISA</span><span>MASTERCARD</span><span>AMEX</span><span>JCB</span></div></div>
</div></footer>
<a class="wa" href="{wa(wa_msg)}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}</a>
'''


EYE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'
def _pw(id_, label, ac, ph="••••••••"):
    return (f'<div class="field"><label for="{id_}">{label}</label><div class="pw"><input id="{id_}" type="password" required minlength="8" autocomplete="{ac}" placeholder="{ph}">'
            f'<button type="button" class="pw-t" aria-label="Show password" data-pw="{id_}">{EYE}</button></div></div>')
AUTH = f'''
<div class="auth" id="auth" hidden>
  <div class="auth-bg" data-close></div>
  <div class="auth-box" role="dialog" aria-modal="true" aria-labelledby="authTitle">
    <button type="button" class="auth-x" data-close aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
    <div class="auth-side">
      <img src="assets/img/logo-white.png" alt="Sanchari" class="auth-logo">
      <div>
        <h2>Your journeys, all in one place</h2>
        <ul><li>{ic("cal")}Track bookings &amp; itineraries</li><li>{ic("heart")}Save tours to your wishlist</li><li>{ic("headset")}Faster support from our team</li></ul>
      </div>
      <small>See More. Feel Divine.</small>
    </div>
    <div class="auth-main">
      <h2 id="authTitle" class="sr">Account</h2>
      <div class="auth-tabs" role="tablist">
        <button type="button" role="tab" id="tab-login" aria-controls="pane-login" aria-selected="true" class="on" data-tab="login">Login</button>
        <button type="button" role="tab" id="tab-signup" aria-controls="pane-signup" aria-selected="false" data-tab="signup">Sign Up</button>
      </div>

      <form class="auth-pane" id="pane-login" role="tabpanel" aria-labelledby="tab-login" novalidate>
        <p class="auth-lead">Welcome back! Log in to manage your bookings.</p>
        <div class="field"><label for="lEmail">Email or phone</label><input id="lEmail" required autocomplete="username" placeholder="you@example.com"></div>
        {_pw("lPass", "Password", "current-password")}
        <div class="auth-row"><label class="chk"><input type="checkbox" id="lRem"><span>Remember me</span></label><button type="button" class="auth-link" data-forgot>Forgot password?</button></div>
        <p class="auth-err" role="alert"></p>
        <button class="btn btn-gold auth-submit" type="submit">Log In</button>
        <p class="auth-switch">New to Sanchari? <button type="button" class="auth-link" data-tab="signup">Create an account</button></p>
      </form>

      <form class="auth-pane" id="pane-signup" role="tabpanel" aria-labelledby="tab-signup" hidden novalidate>
        <p class="auth-lead">Create an account to book faster and save your favourite tours.</p>
        <div class="auth-2">
          <div class="field"><label for="sName">Full name</label><input id="sName" required autocomplete="name" placeholder="Your name"></div>
          <div class="field"><label for="sPhone">Phone</label><input id="sPhone" type="tel" required autocomplete="tel" placeholder="+91"></div>
        </div>
        <div class="field"><label for="sEmail">Email</label><input id="sEmail" type="email" required autocomplete="email" placeholder="you@example.com"></div>
        <div class="auth-2">{_pw("sPass", "Password", "new-password", "Min. 8 characters")}{_pw("sPass2", "Confirm password", "new-password", "Re-enter password")}</div>
        <label class="chk"><input type="checkbox" id="sTerms" required><span>I agree to the Terms &amp; Privacy Policy</span></label>
        <p class="auth-err" role="alert"></p>
        <button class="btn btn-gold auth-submit" type="submit">Create Account</button>
        <p class="auth-switch">Already have an account? <button type="button" class="auth-link" data-tab="login">Log in</button></p>
      </form>

      <div class="auth-pane auth-done" id="pane-done" hidden>
        <div class="auth-ok">{ic("shield")}</div>
        <h3 id="doneTitle">Welcome!</h3>
        <p id="doneText"></p>
        <div class="auth-done-acts"><a href="account.html" class="btn btn-gold" id="doneAcct">Go to My Account</a><button type="button" class="btn btn-line" data-close>Continue Browsing</button></div>
      </div>
    </div>
  </div>
</div>'''

def page(fname, title, desc, active, body, wa_msg=None):
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="assets/css/style.css?v={VER}">
</head>
<body class="pg-{fname[:-5]}">
{header(active)}
{body}
{footer(wa_msg) if wa_msg else footer()}
{AUTH}
<script src="assets/js/site.js?v={VER}"></script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(doc)

def hero(key, crumbs, eyebrow, h1, lead, extra="", cls="page-hero", real=None):
    cr = "".join((f'<a href="{h}">{n}</a><span>/</span>' if h else f'<span>{n}</span>') for n, h in crumbs)
    real = IM.real_url(key) or real
    rb = f' data-bg-real="{real}"' if real else ""
    return f'''
<section class="hero {cls}">
  <div class="hero-bg" style="background-image:url('assets/img/{key}.svg')"{rb} role="img" aria-label=""></div>
  <div class="wrap">
    <div class="crumbs">{cr}</div>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</section>'''

def sec_head(eyebrow, h2, p="", center=False):
    return f'<div class="sec-head{" center" if center else ""}"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{f"<p>{p}</p>" if p else ""}</div>'

# ------------------------------------------------------------ tour cards
def meta_spans(t):
    return (f'<span>{ic("cal")}{t["days"]} Days</span>'
            f'<span>{ic("pin")}{E(t["route"])}</span>')

def styles(t):
    return t.get("styles") or (["group"] if t["cat"] == "adventure" else ["individual", "group"])

def media_slider(t, n=5):
    """Swipeable photo slider used inside tour listing cards (reuses the [data-slider] JS)."""
    imgs = t["images"][:n]
    slides = "".join(f'<a class="ex-slide" href="{t["slug"]}.html" tabindex="-1" aria-label="{E(t["short"])} — photo {k+1} of {len(imgs)}">{img(key, t["short"])}</a>' for k, key in enumerate(imgs))
    dots = "".join(f'<button type="button" class="{"on" if k == 0 else ""}" aria-label="Show photo {k+1}"></button>' for k in range(len(imgs)))
    return (f'<div class="cslide" data-slider><div class="ex-track">{slides}</div>'
            f'<button type="button" class="ex-nav prev" aria-label="Previous photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>'
            f'<button type="button" class="ex-nav next" aria-label="Next photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button>'
            f'<span class="ex-count"><b>1</b> / {len(imgs)}</span><div class="ex-dots">{dots}</div></div>')

def card_h(t, order):
    badge = E(t["badge"]) if t.get("badge") else ("Featured" if t.get("featured") else "")
    pts = "".join(f"<li>{E(p)}</li>" for p in t["card"][:2])
    return f'''
      <article class="card t-card" data-styles="{' '.join(styles(t))}" data-circuits="{circuits_of(t["slug"])}" data-region="{t["rkey"]}" data-zone="{t.get("zone","")}" data-price="{t["price"]}" data-days="{t["days"]}" data-order="{order}">
        <div class="t-img">{media_slider(t)}
          {f'<span class="badge">{badge}</span>' if badge else ""}
          <span class="t-dur">{ic("cal")}{t["days"]} Days · {t["nights"]} Nights</span>
        </div>
        <div class="t-body">
          <div class="t-top"><span class="region">{E(t["region"])}</span><span class="t-route">{ic("pin")}{E(t["route"])}</span></div>
          <h3><a href="{t["slug"]}.html">{E(t["short"])}</a></h3>
          <ul class="incl">{pts}</ul>
          <div class="t-styles">{"".join(f'<span>{ic("user" if x == "individual" else "users")}{"Individual" if x == "individual" else "Group"}</span>' for x in styles(t))}</div>
          <div class="t-foot">
            <div class="price"><small>From</small><b>{inr(t["price"])} <span>/ person</span></b></div>
            <a class="t-go" href="{t["slug"]}.html" aria-label="View {E(t["short"])}">{ic("arrow")}</a>
          </div>
        </div>
      </article>'''


def card_adventure(t, order):
    """Dark expedition-style card, used for every category (Temple, Adventure, Wellness)."""
    cat = t["cat"]; st = styles(t)
    stat = lambda key: next((v for i, v, l in t["stats"] if i == key), "")
    if cat == "adventure":
        badge = E(t["badge"]) if t.get("badge") else ""
        label = (ic("users"), "Group")
        stats = [(ic("peak"), E(stat("peak")), "Max altitude"), (ic("cal"), f'{t["days"]} days', f'{t["nights"]} nights'),
                 (ic("compass"), E(t["region"]), "Destination")]
        cta = "View Expedition"
    elif cat == "temple":
        badge = E(t["badge"]) if t.get("badge") else ("Featured" if t.get("featured") else "")
        label = (ic("user") if st == ["individual"] else ic("users"), "Individual & Group" if len(st) > 1 else ("Group" if st == ["group"] else "Individual"))
        stats = [(ic("temple"), E(stat("temple") or "—"), "Temples"), (ic("cal"), f'{t["days"]} days', f'{t["nights"]} nights'),
                 (ic("compass"), E(t["region"]), "State")]
        cta = "View Journey"
    else:
        badge = E(t["badge"]) if t.get("badge") else ""
        label = (ic("users"), "Individual or group")
        stats = [(ic("cal"), f'{t["days"]} days', f'{t["nights"]} nights'), (ic("compass"), E(t["region"]), "Destination"),
                 (ic("meal"), "All meals", "Included")]
        cta = "View Journey"
    sts = "".join(f"<div>{i}<b>{b}</b><span>{l}</span></div>" for i, b, l in stats)
    return f"""
      <article class="card a-card a-{cat}" data-styles="{' '.join(st)}" data-circuits="{circuits_of(t["slug"])}" data-region="{t["rkey"]}" data-zone="{t.get("zone","")}" data-price="{t["price"]}" data-days="{t["days"]}" data-order="{order}">
        <div class="a-media">{media_slider(t)}
          <div class="a-top">{f'<span class="badge">{badge}</span>' if badge else '<span></span>'}<span class="a-group">{label[0]}{label[1]}</span></div>
          <div class="a-cap"><span class="a-region">{ic("pin")}{E(t["region"])} · {E(t["route"])}</span><h3><a href="{t["slug"]}.html">{E(t["short"])}</a></h3></div>
        </div>
        <div class="a-stats">{sts}</div>
        <div class="a-foot">
          <div class="price"><small>From</small><b>{inr(t["price"])} <span>/ person</span></b></div>
          <a class="btn btn-gold" href="{t["slug"]}.html">{cta} {ic("arrow")}</a>
        </div>
      </article>"""

def card_wellness(t, order):
    tags = "".join(f'<span>{ic("spark")}{E(p)}</span>' for p in t["card"][:2])
    intro = t["overview"][0]
    return f"""
      <article class="card w-card" data-styles="{' '.join(styles(t))}" data-circuits="{circuits_of(t["slug"])}" data-region="{t["rkey"]}" data-zone="{t.get("zone","")}" data-price="{t["price"]}" data-days="{t["days"]}" data-order="{order}">
        <div class="w-media">{media_slider(t)}<span class="w-dur">{t["days"]} Days · {t["nights"]} Nights</span></div>
        <div class="w-body">
          <span class="w-eyebrow">{ic("heart")}Wellness journey · {E(t["region"])}</span>
          <h3><a href="{t["slug"]}.html">{E(t["short"])}</a></h3>
          <p class="w-text">{E(intro)}</p>
          <div class="w-tags">{tags}</div>
          <div class="w-meta"><span>{ic("pin")}{E(t["route"])}</span><span>{ic("users")}Individual or group</span><span>{ic("meal")}All meals included</span></div>
          <div class="w-foot">
            <div class="price"><small>From</small><b>{inr(t["price"])} <span>/ person</span></b></div>
            <a class="btn btn-line" href="{t["slug"]}.html">Explore Journey {ic("arrow")}</a>
          </div>
        </div>
      </article>"""

def card_for(t, order):
    return card_adventure(t, order)  # one card design across Temple, Adventure and Wellness pages

def card_v(t):
    badge = f'<span class="badge">{E(t["badge"])}</span>' if t.get("badge") else ""
    return f'''
      <a class="r-card" href="{t["slug"]}.html">
        <div class="r-img">{img(t["images"][0], t["short"])}{badge}</div>
        <div class="r-body"><span class="region">{E(t["region"])} · {t["days"]} Days</span><h3>{E(t["short"])}</h3><p>{E(t["route"])}</p>
        <div class="r-foot"><b>{inr(t["price"])}</b><span>View tour →</span></div></div>
      </a>'''

def card_ex(t, n):
    """Home: Adventure Journeys card with an image slider."""
    imgs = t["images"][:5]
    slides = "".join(f'<div class="ex-slide" role="group" aria-roledescription="slide" aria-label="{k+1} of {len(imgs)}">{img(key, f"{t['short']} — photo {k+1}")}</div>' for k, key in enumerate(imgs))
    dots = "".join(f'<button type="button" class="{"on" if k == 0 else ""}" aria-label="Show photo {k+1}"></button>' for k in range(len(imgs)))
    summit = next((v for k, v, l in t["stats"] if k == "peak"), "")
    where = next((v for k, v, l in t["stats"] if k == "pin"), t["region"])
    hl = "".join(f"<li>{ic('peak','1.8')}<span><b>{E(b)}</b>{E(d)}</span></li>" for b, d in t["highlights"][:2])
    return f"""
      <article class="ex-card">
        <div class="ex-slider" data-slider>
          <div class="ex-track">{slides}</div>
          <button type="button" class="ex-nav prev" aria-label="Previous photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>
          <button type="button" class="ex-nav next" aria-label="Next photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button>
          <span class="ex-alt">{ic("peak")}{summit}</span>
          <span class="ex-count"><b>1</b> / {len(imgs)}</span>
          <div class="ex-dots">{dots}</div>
        </div>
        <div class="ex-body">
          <div class="ex-meta"><span>{ic("pin")}{E(where)}</span><span>{ic("cal")}{t["days"]} Days</span></div>
          <h3><a href="{t["slug"]}.html">{E(t["short"])}</a></h3>
          <p class="ex-route">{E(t["route"])}</p>
          <ul class="ex-hl">{hl}</ul>
          <div class="ex-foot">
            <div class="ex-price"><small>From / person</small><b>{inr(t["price"])}</b></div>
            <a class="ex-btn" href="{t["slug"]}.html">View Expedition {ic("arrow")}</a>
          </div>
        </div>
      </article>"""

# ------------------------------------------------------------ shared blocks
def enquiry(*_args, **_kw):
    """The single 'Plan Your Journey' section used on every page."""
    groups = [("Temple Tours", [t["short"] for t in TOURS if t["cat"] == "temple"]),
              ("Adventure Tours", [t["short"] for t in TOURS if t["cat"] == "adventure"]),
              ("Wellness Tours", [t["short"] for t in TOURS if t["cat"] == "wellness"])]
    opts = "".join(f'<optgroup label="{g}">' + "".join(f"<option>{E(o)}</option>" for o in os_) + "</optgroup>" for g, os_ in groups)
    types = [("temple", "Temple"), ("adventure", "Adventure"), ("wellness", "Wellness"), ("custom", "Custom"), ("general", "General enquiry")]
    ty = "".join(f'<label><input type="radio" name="pjType" value="{v}"{" checked" if i == 0 else ""}><span>{ic({"temple":"temple","adventure":"peak","wellness":"heart","custom":"sliders","general":"chat"}[v], "1.8")}{n}</span></label>' for i, (v, n) in enumerate(types))
    bg = IM.real_url("hero-wellness")
    return f"""
<section class="pj" id="enquire">
  <div class="pj-bg" style="background-image:url('assets/img/hero-wellness.svg')" data-bg-real="{bg}"></div>
  <div class="wrap pj-grid">
    <div class="pj-intro">
      <span class="eyebrow">Plan Your Journey</span>
      <h2>Tell us your dream trip. <em>We’ll plan the rest.</em></h2>
      <p>Share a few details and a Sanchari travel expert will send you a tailored itinerary and quote.</p>
      <ul class="pj-points">
        <li>{ic("shield", "1.8")}No obligation — just a conversation</li>
        <li>{ic("clock", "1.8")}We usually reply within one business day</li>
        <li>{ic("users", "1.8")}Individuals, families &amp; groups</li>
      </ul>
      <div class="pj-contact">
        <a href="tel:{TEL}"><span>{ic("phone", "1.8")}</span><div><small>Call us</small><b>{PHONE}</b></div></a>
        <a href="{wa("Hi Sanchari, I'd like to plan a trip.")}" target="_blank" rel="noopener"><span class="wa-i">{WA_SVG}</span><div><small>WhatsApp</small><b>Chat with us</b></div></a>
        <a href="mailto:{EMAIL}"><span>{ic("mail", "1.8")}</span><div><small>Email</small><b>{EMAIL}</b></div></a>
      </div>
      <p class="pj-hours">{ic("clock")}{HOURS}</p>
    </div>
    <form class="pj-form" data-ok="pj-ok">
      <div class="pj-head"><h3 id="pjTitle" data-trip="Plan your journey" data-gen="Send us a message">Plan your journey</h3><span>Takes less than a minute</span></div>
      <fieldset class="pj-types"><legend>What can we help with?</legend>{ty}</fieldset>
      <div class="pj-row">
        <div class="field"><label for="pjName">Full name *</label><input id="pjName" required autocomplete="name" placeholder="Your name"></div>
        <div class="field"><label for="pjPhone">Phone *</label><input id="pjPhone" type="tel" required autocomplete="tel" placeholder="+91"></div>
      </div>
      <div class="field"><label for="pjEmail">Email<span class="pj-gen-only"> *</span></label><input id="pjEmail" type="email" autocomplete="email" placeholder="you@example.com"></div>
      <div class="pj-row pj-trip">
        <div class="field"><label for="pjTour">Tour of interest</label><select id="pjTour"><option>Not sure yet</option>{opts}<option>Custom itinerary</option></select></div>
        <div class="field"><label for="pjWhen">When</label><input id="pjWhen" type="month"></div>
      </div>
      <div class="pj-row pj-trip">
        <div class="field"><label for="pjPax">Travellers</label><select id="pjPax"><option>1–2</option><option>3–5</option><option>6–10</option><option>10+ (group)</option></select></div>
        <div class="field"><label for="pjBudget">Budget per person</label><select id="pjBudget"><option>Flexible</option><option>Under ₹10,000</option><option>₹10,000 – ₹25,000</option><option>₹25,000 – ₹1,00,000</option><option>Above ₹1,00,000</option></select></div>
      </div>
      <div class="field"><label for="pjMsg"><span class="pj-trip-only">Anything else?</span><span class="pj-gen-only">Message *</span></label><textarea id="pjMsg" rows="3" placeholder="Places you’d like to include, special requirements…" data-ph-gen="How can we help? Ask us anything — tours, dates, payments, bookings…"></textarea></div>
      <div class="form-ok" id="pj-ok"><span class="pj-trip-only">Thank you — our travel expert will get back to you shortly.</span><span class="pj-gen-only">Thank you — we’ve received your message and will reply shortly.</span></div>
      <button class="btn btn-gold pj-submit" type="submit"><span class="pj-trip-only">Send My Request</span><span class="pj-gen-only">Send Message</span> {ic("arrow")}</button>
      <p class="pj-note"><span class="pj-trip-only">By sending this you agree to be contacted about your trip.</span><span class="pj-gen-only">By sending this you agree to be contacted about your enquiry.</span></p>
    </form>
  </div>
</section>"""

def faq_block(eyebrow, h2, items, lead=True):
    det = "".join(f'<details{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(items))
    lp = f'<p>Can’t find what you’re looking for? Call or WhatsApp us on <a href="tel:{TEL}" style="color:var(--gold);font-weight:600">{PHONE}</a>.</p>' if lead else ""
    return f'''
<section class="sec faq">
  <div class="wrap faq-wrap">
    <div class="sec-head" style="margin-bottom:0"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{lp}</div>
    <div>{det}</div>
  </div>
</section>'''

def why_grid(items):
    return '<div class="why-grid">' + "".join(
        f'<div class="why"><div class="ico">{ic(i, "1.8")}</div><h3>{E(h)}</h3><p>{E(p)}</p></div>' for i, h, p in items) + "</div>"

PROCESS = f'''
<section class="sec process">
  <div class="wrap">
    {sec_head("How It Works", "From enquiry to journey in four steps", "A simple, guided booking process with a dedicated travel coordinator.")}
    <div class="steps">
      <div class="step"><h3>Choose a Tour</h3><p>Pick a featured journey or tell us where you’d like to go.</p></div>
      <div class="step"><h3>Personalise</h3><p>Adjust dates, hotels and pace for individuals, families or groups.</p></div>
      <div class="step"><h3>Confirm &amp; Pay</h3><p>Secure your booking with all major cards accepted.</p></div>
      <div class="step"><h3>Travel in Peace</h3><p>Our team stays in touch throughout your journey, from pickup to drop.</p></div>
    </div>
  </div>
</section>'''

# ------------------------------------------------------------ category pages
WHY = {
 "temple": [("map", "Curated Itineraries", "Routes sequenced around temple timings, festivals and travel distances for a well-paced trip."),
            ("users", "Knowledgeable Guides", "Local experts who share the history, legends and rituals behind every shrine you visit."),
            ("home", "Comfortable Stays", "Hand-picked, clean accommodation located close to the temples on your route."),
            ("shield", "Transparent Pricing", "Clear per-person pricing with inclusions listed upfront — no surprises on the road.")],
 "adventure": [("peak", "Expert Leadership", "Expeditions run with Anmish Adventures, led by a record-holding mountaineer."),
               ("compass", "Acclimatisation Built In", "Rest days and buffer days planned into every itinerary for a safer climb."),
               ("shield", "Safety First", "First aid, emergency oxygen, communication devices and insurance on every trip."),
               ("users", "Experienced Crews", "Guides, porters and support staff who know these mountains well.")],
 "wellness": [("heart", "Unhurried Pace", "Fewer early starts and more time to rest, reflect and enjoy each place."),
              ("wave", "Nature & Sea", "Forests, hills and quiet beaches woven into every journey."),
              ("home", "Comfortable Stays", "Hand-picked accommodation chosen for comfort and calm."),
              ("headset", "Support Throughout", "A single point of contact before and during your journey.")],
}
CAT_FAQ = {
 "temple": [("Where do the tours start from?", "Each tour has its own starting point — Hyderabad, Coimbatore or Vijayawada. Pickup and drop details are listed on each tour page, and we can arrange connections from other cities."),
            ("Is the price per person?", "Yes, listed prices are per-person starting rates. The final price depends on group size, hotel category and travel dates."),
            ("Can I customise an itinerary?", "Absolutely. You can add or remove temples, change hotels or extend your stay. Share your preferences and our team will send a revised plan."),
            ("Are these tours suitable for senior citizens?", "Yes. Let us know about any mobility needs and we’ll plan a comfortable pace, suitable rooms and assisted access wherever possible."),
            ("What payment methods do you accept?", "We accept Visa, Mastercard, American Express and JCB cards.")],
 "adventure": [("How fit do I need to be?", "Good cardiovascular fitness is essential. We recommend 8–12 weeks of training with long walks, stair climbs and cardio before departure."),
               ("Are flights included?", "It varies by expedition — the Everest trek includes flights from Hyderabad, while Kilimanjaro and Elbrus do not. Check the inclusions on each tour page."),
               ("What happens if the weather turns?", "Every itinerary includes buffer or reserve days. Final decisions on summit attempts are made by the expedition leaders for everyone’s safety."),
               ("Can I rent equipment?", "Yes. A detailed gear list is shared on booking, and personal trekking and mountaineering gear can be rented on request."),
               ("Is insurance included?", "High-altitude, medical and evacuation cover is included where stated on each tour page. We’ll confirm exactly what is covered when you book.")],
 "wellness": [("What makes a journey a wellness tour?", "A slower pace, time in nature and room to rest — combined with meaningful places to visit."),
              ("Can I add Ayurveda or yoga sessions?", "Yes. Tell us what you’re looking for and we’ll suggest additions to your itinerary."),
              ("Is the price per person?", "Yes, listed prices are per-person starting rates. The final price depends on group size, hotel category and dates."),
              ("Can I customise the itinerary?", "Absolutely. Share your preferences and our team will send a tailored plan.")],
}

CIRCUITS = [
    ("char-dham", "Char Dham Yatra", "uk-kedarnath", "Yamunotri, Gangotri, Kedarnath &amp; Badrinath — the four Himalayan dhams.",
     ["tour-char-dham-yatra"]),
    ("jyotirlinga", "Jyotirlinga Darshan", "mp-mahakal", "Kedarnath, Kashi Vishwanath, Mahakaleshwar, Omkareshwar, Somnath &amp; Nageshwar.",
     ["tour-char-dham-yatra", "tour-kashi-prayagraj-ayodhya", "tour-jyotirlinga-ujjain-omkareshwar", "tour-dwarka-somnath"]),
    ("shakti-peeth", "Shakti Peeth Yatra", "pb-vaishno", "Mata Vaishno Devi, Harsiddhi in Ujjain and Kamakshi Amman in Kanchipuram.",
     ["tour-golden-temple-vaishno-devi", "tour-jyotirlinga-ujjain-omkareshwar", "tour-tamil-nadu-temple-journey"]),
]
def circuits_of(slug):
    return " ".join(k for k, _n, _i, _d, slugs in CIRCUITS if slug in slugs)

def circuits_sec(home=False):
    by = {t["slug"]: t for t in TOURS}
    cards = ""
    for k, n, im, d, slugs in CIRCUITS:
        ts = [by[x] for x in slugs if x in by]
        cnt = len(ts)
        frm = min(t["price"] for t in ts)
        href = f"temple-tours.html?circuit={k}#tours" if home else "#tours"
        cards += (f'<a class="yc" href="{href}" data-c="{k}" data-name="{n}">'
                  f'<span class="yc-img">{img(im, n)}</span>'
                  f'<span class="yc-top"><em>{cnt:02d} {"Tour" if cnt == 1 else "Tours"}</em><span>From {inr(frm)}</span></span>'
                  f'<span class="yc-body"><small>Sacred circuit</small><b>{n}</b><span class="yc-d">{d}</span>'
                  f'<span class="yc-go">View tours <i>{ic("arrow")}</i></span></span></a>')
    return f"""
<section class="yc-sec{' yc-home bg-white' if home else ''}" aria-label="Popular yatras">
  <div class="wrap">
    <div class="yc-head"><div><span class="eyebrow">Popular Yatras</span><h2>Choose your sacred circuit</h2></div>{'<a href="temple-tours.html#tours" class="btn btn-line">View all temple tours</a>' if home else ''}</div>
    <div class="yc-grid">{cards}</div>
  </div>
</section>"""

def category_page(cat):
    c = CATS[cat]; tours = [t for t in TOURS if t["cat"] == cat]
    regions = []
    for t in tours:
        if (t["rkey"], t["region"]) not in regions: regions.append((t["rkey"], t["region"]))
    lo = min(t["price"] for t in tours)
    dmin, dmax = min(t["days"] for t in tours), max(t["days"] for t in tours)
    stats = f'''<div class="hero-stats"><div><b>{len(tours)}</b><span>{"Journeys" if len(tours) > 1 else "Journey"} available</span></div>
      <div><b>{dmin}{"–" + str(dmax) if dmax != dmin else ""}</b><span>Day itineraries</span></div>
      <div><b>{inr(lo)}</b><span>Packages from</span></div></div>'''
    ctas = f'<div class="hero-ctas"><a href="#tours" class="btn btn-gold">Explore Tours {ic("arrow")}</a><a href="#enquire" class="btn btn-outline">Request a Custom Itinerary</a></div>'
    body = hero(c["hero"], [("Home", "index.html"), (c["name"], None)], c["eyebrow"], c["h1"], c["lead"], "",
                cls="page-hero compact", real=IM.real_url(tours[0]["images"][0]))
    dest_opts = "".join(f'<option value="{k}">{E(n)}</option>' for k, n in regions)
    if cat == "temple":
        zs = [z for z in ZONES if any(t.get("zone") == z for t in tours)]
        dest_opts = "".join(f'<optgroup label="{ZONES[z]}"><option value="{z}">All of {ZONES[z]}</option>' + "".join(
            f'<option value="{k}">{E(n)}</option>' for k, n in regions if any(t["rkey"] == k and t.get("zone") == z for t in tours)) + "</optgroup>" for z in zs)
    if cat == "adventure":
        dur = '<option value="all">Any duration</option><option value="1-9">Up to 9 days</option><option value="10-30">10+ days</option>'
        bud = '<option value="all">Any budget</option><option value="125000">Under ₹1,25,000</option><option value="150000">Under ₹1,50,000</option>'
    else:
        dur = '<option value="all">Any duration</option><option value="1-5">Up to 5 days</option><option value="6-7">6–7 days</option><option value="8-30">8+ days</option>'
        bud = '<option value="all">Any budget</option><option value="10000">Under ₹10,000</option><option value="15000">Under ₹15,000</option><option value="20000">Under ₹20,000</option>'
    body += f'''
<div class="search-panel"><div class="wrap">
  <form class="search-card" id="searchForm">
    <div class="field"><label for="sDest">Destination</label><select id="sDest"><option value="all">All destinations</option>{dest_opts}</select></div>
    <div class="field"><label for="sDur">Duration</label><select id="sDur">{dur}</select></div>
    <div class="field"><label for="sType">Travel style</label><select id="sType"><option value="all">All travel styles</option><option value="individual">Individual / Family</option><option value="group">Group departure</option></select></div>
    <div class="field"><label for="sBudget">Budget</label><select id="sBudget">{bud}</select></div>
    <button class="btn btn-dark" type="submit">{ic("search")}Search</button>
  </form>
</div></div>'''
    if cat == "temple":
        body += circuits_sec()
    chips = ""
    zones = [z for z in ZONES if any(t.get("zone") == z for t in tours)]
    if cat == "temple" and len(zones) > 1:
        zn = {z: sum(t.get("zone") == z for t in tours) for z in zones}
        chips = '<div class="chips"><button class="chip on" data-f="all">All Tours</button>' + "".join(
            f'<button class="chip" data-f="{z}">{ZONES[z]} <small>{zn[z]}</small></button>' for z in zones) + "</div>"
        regions = [(z, ZONES[z]) for z in zones] + regions
    elif len(regions) > 1:
        chips = '<div class="chips"><button class="chip on" data-f="all">All Tours</button>' + "".join(
            f'<button class="chip" data-f="{k}">{E(n)}</button>' for k, n in regions) + "</div>"
    else:
        chips = '<div class="chips"><button class="chip on" data-f="all">All Tours</button></div>'
    # travel style as tabs (no label), same on every category page
    style_ctrl = f'''<div class="seg" role="group" aria-label="Travel style">
        <button type="button" class="seg-b on" data-s="all">{ic("compass")}All</button><button type="button" class="seg-b" data-s="individual">{ic("user")}Individual</button><button type="button" class="seg-b" data-s="group">{ic("users")}Group</button></div>'''
    cards = "".join(card_for(t, i + 1) for i, t in enumerate(tours))
    if len(tours) < 2:
        cards += f'''
      <div class="grid-note"><div class="gn-text"><span class="eyebrow">More coming soon</span><h3>Looking for a different kind of retreat?</h3>
        <p>Ayurveda stays, yoga retreats and nature escapes can be planned around your dates. Tell us what you have in mind.</p></div>
        <a href="#enquire" class="btn btn-gold">Plan a Wellness Trip</a></div>'''
    body += f'''
<section class="sec tours" id="tours">
  <div class="wrap">
    {sec_head(c["name"], c["sec_h"], c["sec_p"])}
    <div class="toolbar">{chips}
      <div class="tb-right">
      {style_ctrl}
      </div>
    </div>
    <p class="count"><b id="cnt">{len(tours)}</b> {"tours" if len(tours) != 1 else "tour"} available</p>
    <div class="yc-bar" id="ycBar" hidden><span>Showing <b id="ycName"></b></span><button type="button" id="ycClear">Show all tours ×</button></div>
    <div class="grid grid-{cat}" id="grid">{cards}</div>
    <div class="empty" id="empty">No tours match these filters. <a href="#" onclick="resetFilters();return false" style="color:var(--gold);font-weight:600">Clear filters</a> or <a href="#enquire" style="color:var(--gold);font-weight:600">ask us for a custom plan</a>.</div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    {sec_head("Why Sanchari", {"temple": "A pilgrimage without the planning burden", "adventure": "Adventure, planned around safety", "wellness": "Travel that leaves you restored"}[cat], "We handle the logistics end to end, so every day of your journey is about the experience.", True)}
    {why_grid(WHY[cat])}
  </div>
</section>
{PROCESS}'''
    if cat == "temple":
        body += f'''
<section class="sec">
  <div class="wrap split">
    <div class="split-img">{img("tn-brihad", "Group temple tour")}
      <div class="float-card"><div class="ico" style="margin:0;width:44px;height:44px">{ic("users", "1.8")}</div><div><b>Group departures</b><span>Families, communities &amp; corporates</span></div></div>
    </div>
    <div>
      <span class="eyebrow">Individual &amp; Group Tours</span>
      <h2 style="font-size:clamp(24px,2.7vw,36px);margin:12px 0 16px">Travelling with family, a community or your team?</h2>
      <p class="lead-sm">Every package can be run as a private tour or a group departure. We’ll tailor the itinerary, vehicles and accommodation to your group’s size and needs.</p>
      <ul class="check-list"><li>Private vehicles sized to your group</li><li>Flexible dates and custom temple selection</li><li>Single point of contact before and during travel</li><li>Add-ons: flights, hotels and travel insurance</li></ul>
      <a href="#enquire" class="btn btn-gold">Get a Group Quote</a>
    </div>
  </div>
</section>'''
    if cat == "adventure":
        body += f'''
<section class="sec"><div class="wrap">{leader_block()}</div></section>'''
    body += faq_block("FAQs", "Questions before you travel", CAT_FAQ[cat])
    body += enquiry()
    page(c["file"], f'{c["name"]} | Sanchari Travel', c["blurb"], c["nav"], body,
         f"Hi Sanchari, I'd like to know more about your {c['name'].lower()}.")

def leader_block():
    return f'''
<div class="leader">
  <div class="leader-img">{img("anmish", "Uhuru Peak, Kilimanjaro")}</div>
  <div>
    <span class="eyebrow">Elite Adventure Leadership</span>
    <h2>Led by mountaineer Anmish Varma</h2>
    <p>Our adventure journeys are led by Mr. Anmish Varma, a mountaineer and Guinness World Record holder for the fastest ascent of the Seven Volcanic Summits.</p>
    <p>His experience shapes every expedition we run — from acclimatisation schedules to safety protocols on summit day.</p>
    <a href="adventure-tours.html" class="btn btn-light">View Expeditions</a>
  </div>
</div>'''

# ------------------------------------------------------------ tour detail
def tour_page(t):
    cat = CATS[t["cat"]]
    imgs = t["images"]
    gal_top = imgs[:5] if len(imgs) >= 5 else (imgs * 5)[:5]
    stats = "".join(f'<div><div class="f-ico">{ic(i, "1.8")}</div><b>{E(v)}</b><span>{E(l)}</span></div>' for i, v, l in t["stats"])
    hls = "".join(f'<div class="hl"><b>{E(b)}</b><span>{E(s)}</span></div>' for b, s in t["highlights"])
    stops = '<i>→</i>'.join(f"<span>{E(s)}</span>" for s in t["stops"])
    days = ""
    for n, (title, sub, intro, slots, draft) in enumerate(t["itinerary"], 1):
        sl = "".join(f'<li><time>{E(tm)}</time><div><b>{E(b)}</b>{E(d)}</div></li>' for tm, b, d in slots)
        dc = "<!-- DRAFT: not on the current site; confirm with operations -->" if draft else ""
        days += f'''{dc}
          <details class="day"{" open" if n == 1 else ""}>
            <summary><span class="d-num">Day<b>{n:02d}</b></span><span class="d-t"><b>{E(title)}</b><small>{E(sub)}</small></span></summary>
            <div class="d-body">{f"<p>{E(intro)}</p>" if intro else ""}<ul class="slots">{sl}</ul></div>
          </details>'''
    incl = "".join(f"<li>{E(x)}</li>" for x in t["incl"])
    excl = "".join(f"<li>{E(x)}</li>" for x in t["excl"])
    gal = "".join(f'<figure{" class=\"wide\"" if (i == len(imgs) - 1 and len(imgs) % 3 == 1) else ""}>{img(k)}<figcaption>{E(IM.REG[k][0])}</figcaption></figure>' for i, k in enumerate(imgs))
    know = "".join(f"<div><h3>{E(h)}</h3><p>{E(p)}</p></div>" for h, p in t["know"])
    faqs = "".join(f'<details{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(t["faq"]))
    adv = t["cat"] == "adventure"
    if adv:
        pax = f'''<div class="pax"><div><b>Participants</b><small>18+ years</small></div>
            <div class="stepper"><button type="button" data-pax="a" data-d="-1" aria-label="Fewer participants">−</button><span id="pa">1</span><button type="button" data-pax="a" data-d="1" aria-label="More participants">+</button></div></div>'''
        note = "Final price and departure dates are confirmed by our expedition team."
    else:
        pax = f'''<div class="pax"><div><b>Adults</b><small>12+ years</small></div>
            <div class="stepper"><button type="button" data-pax="a" data-d="-1" aria-label="Fewer adults">−</button><span id="pa">2</span><button type="button" data-pax="a" data-d="1" aria-label="More adults">+</button></div></div>
          <div class="pax"><div><b>Children</b><small>5–11 years</small></div>
            <div class="stepper"><button type="button" data-pax="c" data-d="-1" aria-label="Fewer children">−</button><span id="pc">0</span><button type="button" data-pax="c" data-d="1" aria-label="More children">+</button></div></div>'''
        note = "Child pricing and final total are confirmed by our team."
    st = styles(t)
    if len(st) > 1:
        style_pick = f'''<div class="field"><label>Travel style</label>
          <div class="b-style" role="radiogroup" aria-label="Travel style">
            <label><input type="radio" name="bStyle" value="individual" checked><span>{ic("user")}<b>Individual</b><small>Private / family</small></span></label>
            <label><input type="radio" name="bStyle" value="group"><span>{ic("users")}<b>Group</b><small>Group departure</small></span></label>
          </div></div>'''
    else:
        if st == ["individual"]:
            style_pick = f'<div class="b-fixed">{ic("user")}<span><b>Individual / family</b><small>A private tour for you and your family</small></span></div><input type="hidden" name="bStyleFixed" value="individual">'
        else:
            msg = "This expedition runs as a guided team" if t["cat"] == "adventure" else "Travel with a small group on fixed departure dates"
            style_pick = f'<div class="b-fixed">{ic("users")}<span><b>Group departure</b><small>{msg}</small></span></div><input type="hidden" name="bStyleFixed" value="group">'
    related = [x for x in TOURS if x["cat"] == t["cat"] and x is not t]
    related += [x for x in TOURS if x["cat"] != t["cat"]]
    rel = "".join(card_v(x) for x in related[:3])
    tag = f'<span class="tag">{E(t["badge"])}</span>' if t.get("badge") else '<span class="tag">Featured</span>'
    wmsg = f"Hi Sanchari, I'm interested in the {t['short']} ({t['days']} days)."
    body = f'''
<section class="d-top">
  <div class="wrap">
    <div class="crumbs d-crumbs"><a href="index.html">Home</a><span>/</span><a href="{cat["file"]}">{cat["name"]}</a><span>/</span><span>{E(t["short"])}</span></div>
    <div class="d-titlebar">
      <div>
        <span class="eyebrow">{E(t["region"])} · {cat["name"][:-1]}</span>
        <h1>{E(t["title"])}</h1>
        <div class="d-sub"><span>{ic("pin")}{E(t["route"])}</span><span>{ic("cal")}{t["days"]} Days / {t["nights"]} Nights</span>{tag}</div>
      </div>
      <div class="d-share">
        <button class="icon-btn" id="shareBtn" aria-label="Share"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/></svg></button>
        <button class="icon-btn" id="wishBtn" data-slug="{t["slug"]}" aria-label="Save to wishlist" aria-pressed="false">{ic("heart")}</button>
      </div>
    </div>
    <div class="gallery">
      <div class="g-main">{img(gal_top[0])}</div><div>{img(gal_top[1])}</div><div>{img(gal_top[2])}</div><div>{img(gal_top[3])}</div>
      <div class="g-more">{img(gal_top[4])}<a href="#gallery" class="g-count"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>View all {len(imgs)} photos</a></div>
    </div>
    <div class="facts">{stats}</div>
  </div>
</section>
<nav class="d-tabs" aria-label="Tour sections"><div class="wrap">
  <a href="#overview" class="on">Overview</a><a href="#itinerary">Itinerary</a><a href="#inclusions">Inclusions</a><a href="#gallery">Gallery</a><a href="#know">Good to Know</a><a href="#faq">FAQs</a>
</div></nav>
<section class="d-main">
  <div class="wrap d-layout">
    <div class="d-content">
      <div class="block" id="overview"><h2>Tour overview</h2>{"".join(f"<p>{E(p)}</p>" for p in t["overview"])}<div class="hl-grid">{hls}</div></div>
      <div class="block" id="itinerary">
        <div class="block-head"><h2>Day-by-day itinerary</h2><button class="link-btn" id="toggleDays">Expand all</button></div>
        <div class="route">{stops}</div>
        <div class="days">{days}</div>
      </div>
      <div class="block" id="inclusions"><h2>What’s included</h2>
        <div class="ie"><div class="ie-col yes"><h3>Included</h3><ul>{incl}</ul></div><div class="ie-col no"><h3>Not included</h3><ul>{excl}</ul></div></div>
      </div>
      <div class="block" id="gallery"><h2>Gallery</h2><div class="g-grid">{gal}</div></div>
      <div class="block" id="know"><h2>Good to know</h2><div class="know-grid">{know}</div></div>
      <div class="block" id="faq"><h2>Frequently asked questions</h2>{faqs}</div>
    </div>
    <aside class="d-aside" id="book">
      <div class="book">
        <div class="book-top"><small>Starting from</small><div class="b-price">{inr(t["price"])} <span>/ person</span></div></div>
        <form class="book-body" id="bookForm" data-price="{t["price"]}" data-slug="{t["slug"]}">
          {style_pick}
          <div class="field"><label for="bDate">Preferred travel date</label><input type="date" id="bDate" required></div>
          <div class="field"><label for="bName">Lead traveller name</label><input type="text" id="bName" autocomplete="name" placeholder="Full name" required></div>
          <div class="b-two">
            <div class="field"><label for="bPhone">Phone</label><input type="tel" id="bPhone" autocomplete="tel" placeholder="+91" required></div>
            <div class="field"><label for="bEmail">Email</label><input type="email" id="bEmail" autocomplete="email" placeholder="you@example.com"></div>
          </div>
          {pax}
          <div class="b-total"><span>Estimated total</span><b id="tot">{inr(t["price"])}</b></div>
          <p class="b-note">{note}</p>
          <button class="btn btn-gold b-full" type="submit">Book This Tour</button>
          <a class="btn b-wa b-full" target="_blank" rel="noopener" href="{wa(wmsg)}"><span style="width:18px;height:18px;display:inline-flex">{WA_SVG}</span>Enquire on WhatsApp</a>
          <div class="form-ok" id="bok">Thank you! Our team will call you to confirm availability.</div>
        </form>
      </div>
      <div class="help"><div class="ico">{ic("phone", "1.8")}</div><div><b>Need help planning?</b><a href="tel:{TEL}">{PHONE}</a><small>{HOURS}</small></div></div>
    </aside>
  </div>
</section>
<section class="sec related">
  <div class="wrap">
    <div class="block-head" style="margin-bottom:32px">
      <div><span class="eyebrow">You may also like</span><h2 style="font-size:clamp(22px,2.4vw,30px);margin-top:10px">More journeys</h2></div>
      <a href="{cat["file"]}" class="btn btn-dark">View all {cat["name"].lower()}</a>
    </div>
    <div class="r-grid">{rel}</div>
  </div>
</section>
<div class="m-book"><div><small>From</small><b>{inr(t["price"])}</b><span>/ person</span></div><a href="#book" class="btn btn-gold">Book Now</a></div>'''
    page(t["slug"] + ".html", f'{t["short"]} – {t["days"]}-Day Tour | Sanchari Travel',
         f'{t["days"]}-day guided journey, {t["route"]}. From {inr(t["price"])} per person.', cat["nav"], body, wmsg)


POPULAR = ["tour-sacred-kerala", "tour-tamil-nadu-temple-journey", "tour-everest-base-camp", "tour-char-dham-yatra",
           "tour-kashi-prayagraj-ayodhya", "tour-sacred-karnataka", "tour-kilimanjaro-expedition", "tour-mount-elbrus-expedition"]
# Popular journeys: these cards play a short 9:16 clip instead of a photo.
# The clips in assets/video/ are generated placeholder animations - replace each
# file with real footage under the same name (keep it short, muted, under ~3 MB).
# Popular journeys: these cards stream a real clip from Wikimedia Commons (credited on photo-credits.html).
# The card shows the tour photo first and fades into the video once it plays; if the clip can't load,
# the photo card simply stays. Each clip plays an 8-second window from `start` seconds.
# To use your own footage: put a short muted 9:16 MP4 in assets/video/ and set the value to that path.
from urllib.parse import quote as _vq
def _cv(name): return "https://commons.wikimedia.org/wiki/Special:FilePath/" + _vq(name)
REEL_VIDEO = {}  # Commons clips removed; add {"tour-slug": ("assets/video/file.mp4", 0)} to give a card a video
REEL_TAG = {"temple": "Temple Journey", "adventure": "Expedition", "wellness": "Wellness Escape"}

def reel_card(t, i):
    cat = t["cat"]
    v = REEL_VIDEO.get(t["slug"])
    if v:
        src, start = v
        media = (img(t["images"][0], t["short"]) +
                 f'<video muted playsinline preload="none" data-src="{src}#t={start}" data-start="{start}" data-len="8" aria-label="Video: {E(t["short"])}"></video>')
        kind = f'<span class="reel-kind" title="Video"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13l11-6.5z"/></svg></span>'
    else:
        media = img(t["images"][0], t["short"])
        kind = f'<span class="reel-kind" title="Photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="2"/><path d="m21 15-5-5L5 21"/></svg></span>'
    return f"""
      <article class="reel{" has-video" if v else ""}" data-cat="{cat}">
        <a class="reel-link" href="{t["slug"]}.html" aria-label="View {E(t["short"])}"></a>
        <div class="reel-media">{media}</div>
        <div class="reel-shade"></div>
        <div class="reel-bar"><span></span></div>
        <div class="reel-head">
          <span class="reel-av"><img src="assets/img/favicon.png" alt=""></span>
          <div><b>sanchari.travel</b><small>{ic("pin")}{E(t["region"])}</small></div>
          {kind}
        </div>
        <div class="reel-side">
          <button type="button" class="reel-btn reel-like" data-slug="{t["slug"]}" aria-label="Save to wishlist" aria-pressed="false">{ic("heart")}<small>Save</small></button>
          <button type="button" class="reel-btn reel-share" aria-label="Share {E(t["short"])}" data-url="{t["slug"]}.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/></svg><small>Share</small></button>
          <a class="reel-btn" href="{wa(f"Hi Sanchari, I'd like to know more about the {t['short']}.")}" target="_blank" rel="noopener" aria-label="Ask on WhatsApp">{ic("chat")}<small>Ask</small></a>
        </div>
        <div class="reel-foot">
          <span class="reel-tag">{REEL_TAG[cat]}</span>
          <div class="reel-meta"><span>{ic("cal")}{t["days"]} Days</span><span>{ic("map")}{E(t["route"])}</span></div>
          <h3>{E(t["short"])}</h3>
          <div class="reel-cta"><div><small>From</small><b>{inr(t["price"])}</b></div><span class="reel-go">View Journey {ic("arrow")}</span></div>
        </div>
      </article>"""

def trending_ranked():
    """Home: alternative 'Trending Now' layout - featured #1 journey + ranked list."""
    by = {t["slug"]: t for t in TOURS}
    tl = [by[s_] for s_ in POPULAR if s_ in by][:6]
    f, rest = tl[0], tl[1:]
    fhl = "".join(f"<li>{ic('check' if 'check' in P else 'star','2')}{E(b)}</li>" for b, _ in f["highlights"][:3])
    rows = "".join(f"""
        <a class="tr-row" href="{t["slug"]}.html">
          <span class="tr-rank">{k+2:02d}</span>
          <span class="tr-thumb">{img(t["images"][0], t["short"])}</span>
          <span class="tr-info"><small>{E(t["region"])} · {REEL_TAG[t["cat"]]}</small><b>{E(t["short"])}</b>
            <em>{ic("cal")}{t["days"]} Days<i></i><span>{E(t["route"])}</span></em></span>
          <span class="tr-price"><small>From</small>{inr(t["price"])}</span>
          <span class="tr-go" aria-hidden="true">{ic("arrow")}</span>
        </a>""" for k, t in enumerate(rest))
    return f"""
<section class="sec tr-sec">
  <div class="wrap">
    <div class="tr-head">
      {sec_head("Trending Now", "Top picks for this season", "Six journeys our team recommends right now — from the Himalayan dhams to the Kerala backwaters.")}
      <a href="contact.html#enquire" class="btn btn-line">Ask about availability {ic("arrow")}</a>
    </div>
    <div class="tr-grid">
      <a class="tr-feature" href="{f["slug"]}.html">
        <span class="tr-fimg">{img(f["images"][0], f["short"])}</span>
        <span class="tr-badge"><b>01</b> Top pick</span>
        <span class="tr-fbody">
          <small>{ic("pin")}{E(f["region"])} · {E(f["route"])}</small>
          <b class="tr-ftitle">{E(f["short"])}</b>
          <ul>{fhl}</ul>
          <span class="tr-ffoot"><span class="tr-fprice"><small>From / person</small>{inr(f["price"])}</span>
            <span class="tr-fdays">{ic("cal")}{f["days"]} Days · {f["nights"]} Nights</span>
            <span class="tr-fbtn">View Journey {ic("arrow")}</span></span>
        </span>
      </a>
      <div class="tr-list">{rows}
      </div>
    </div>
  </div>
</section>"""

def trending_tickets():
    """Home: 'Trending Now' option 3 - boarding-pass style journey tickets."""
    by = {t["slug"]: t for t in TOURS}
    tl = [by[s_] for s_ in POPULAR if s_ in by][:6]
    def ends(t):
        parts = [p.strip() for p in t["route"].split("→")]
        return (parts[0], parts[-1]) if len(parts) > 1 else (t["route"], t["region"])
    tix = ""
    for k, t in enumerate(tl):
        a, b = ends(t)
        tix += f"""
      <a class="tk" href="{t["slug"]}.html">
        <span class="tk-img">{img(t["images"][0], t["short"])}<span class="tk-tag">{REEL_TAG[t["cat"]]}</span></span>
        <span class="tk-main">
          <span class="tk-top"><small>Journey pass</small><small>No. {k+1:02d}</small></span>
          <b class="tk-title">{E(t["short"])}</b>
          <span class="tk-route">
            <span><small>From</small><b>{E(a)}</b></span>
            <span class="tk-line" aria-hidden="true"><i></i>{ic("compass","1.8")}<i></i></span>
            <span class="tk-to"><small>To</small><b>{E(b)}</b></span>
          </span>
          <span class="tk-meta"><span><small>Duration</small><b>{t["days"]}D / {t["nights"]}N</b></span><span><small>Region</small><b>{E(t["region"])}</b></span></span>
        </span>
        <span class="tk-stub">
          <small>From</small><b>{inr(t["price"])}</b><em>per person</em>
          <span class="tk-cta">View {ic("arrow")}</span>
          <span class="tk-bars" aria-hidden="true"></span>
        </span>
      </a>"""
    return f"""
<section class="sec tk-sec">
  <div class="wrap">
    {sec_head("Journey Passes", "Your next journey pass", "Pick a ticket and start planning — six journeys travellers love, at a glance.", True)}
    <div class="tk-grid">{tix}
    </div>
  </div>
</section>"""

def dest_carousel():
    """Home: popular destinations carousel (square photo cards with tour count), modelled on the live site."""
    order = ["uttarakhand", "uttarpradesh", "karnataka", "kerala", "tamilnadu", "telangana", "andhra", "punjab-jk",
             "gujarat", "odisha", "madhyapradesh"]
    by = {}
    for t in TOURS: by.setdefault(t["rkey"], []).append(t)
    keys = [k for k in order if k in by] + [k for k in by if k not in order]
    cards = ""
    for k in keys:
        ts = by[k]; t0 = ts[0]; n = len(ts)
        key = DEST_IMG.get(k, t0["images"][0])
        cards += f"""
      <a class="dx" href="{CATS[t0["cat"]]["file"]}?region={k}#tours" aria-label="{E(t0["region"])}: {n} {'tour' if n == 1 else 'tours'}">
        <span class="dx-img">{img(key, t0["region"])}</span>
        <span class="dx-info"><b>{E(t0["region"])}</b><span class="dx-count"><em>{n:02d}</em> {'Tour' if n == 1 else 'Tours'}</span></span>
      </a>"""
    return f"""
<section class="sec dx-sec">
  <div class="wrap">
    <div class="dx-head">
      <div><span class="dx-eyebrow">Travel. Explore. Experience.</span>
        <h2>Popular destinations worth exploring</h2>
        <p>Discover India’s temples, adventures, wellness retreats, heritage and culture — and the great summits beyond.</p></div>
      <div class="dx-nav"><button type="button" class="dx-arrow" data-d="-1" aria-label="Previous destinations"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>
        <button type="button" class="dx-arrow" data-d="1" aria-label="Next destinations"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button></div>
    </div>
    <div class="dx-track" id="dxTrack" tabindex="0" aria-label="Popular destinations">{cards}
    </div>
  </div>
</section>"""

def reels_section():
    by = {t["slug"]: t for t in TOURS}
    cards = "".join(reel_card(by[s], i) for i, s in enumerate(POPULAR) if s in by)
    return f"""
<section class="sec reels-sec">
  <div class="wrap">
    <div class="sec-top">
      <div class="sec-head"><span class="eyebrow">Trending Now</span><h2>Popular journeys</h2><p>Swipe through the trips our travellers love most.</p></div>
      <div class="reel-nav"><button type="button" class="reel-arrow" data-dir="-1" aria-label="Previous journeys"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></button>
        <button type="button" class="reel-arrow" data-dir="1" aria-label="Next journeys">{ic("arrow")}</button></div>
    </div>
  </div>
  <div class="reel-track" id="reelTrack" tabindex="0" aria-label="Popular journeys">{cards}</div>
  <div class="wrap"><div class="reel-dots" id="reelDots"></div></div>
</section>"""


def temple_showcase(temples):
    f, rest = temples[0], temples[1:4]
    hl = "".join(f'<li>{ic("temple", "1.8")}{E(b)}</li>' for b, _ in f["highlights"][:3])
    big = f"""
      <a class="ts-feature" href="{f["slug"]}.html">
        <div class="ts-media">{img(f["images"][0], f["short"])}</div>
        <div class="ts-overlay">
          <span class="ts-badge">{ic("star")}Most loved</span>
          <span class="ts-region">{ic("pin")}{E(f["region"])} · {E(f["route"])}</span>
          <h3>{E(f["title"])}</h3>
          <ul class="ts-hl">{hl}</ul>
          <div class="ts-bottom">
            <div class="ts-facts"><span><b>{f["days"]}</b>Days</span><span><b>{f["stats"][0][1]}</b>Temples</span><span><b>{inr(f["price"])}</b>From / person</span></div>
            <span class="ts-btn">View Journey {ic("arrow")}</span>
          </div>
        </div>
      </a>"""
    items = "".join(f"""
        <a class="ts-item" href="{t["slug"]}.html">
          <div class="ts-thumb">{img(t["images"][0], t["short"])}<span>{t["days"]}D</span></div>
          <div class="ts-info">
            <span class="region">{E(t["region"])}</span>
            <h4>{E(t["short"])}</h4>
            <p>{ic("pin")}{E(t["route"])}</p>
            <div class="ts-row"><b>{inr(t["price"])}<small> / person</small></b><span class="ts-go">{ic("arrow")}</span></div>
          </div>
        </a>""" for t in rest)
    return f'<div class="ts">{big}<div class="ts-list">{items}</div></div>'


# Custom tour packages video. Put your file at assets/video/custom-tours.mp4,
# or set a YouTube link here (e.g. "https://www.youtube.com/watch?v=XXXX").
CUSTOM_VIDEO = "https://upload.wikimedia.org/wikipedia/commons/transcoded/5/59/Ganga_Aarti_at_Rishikesh.webm/Ganga_Aarti_at_Rishikesh.webm.1080p.vp9.webm"
CUSTOM_VIDEO_SD = "https://upload.wikimedia.org/wikipedia/commons/transcoded/5/59/Ganga_Aarti_at_Rishikesh.webm/Ganga_Aarti_at_Rishikesh.webm.480p.vp9.webm"
CUSTOM_VIDEO_POSTER = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Ganga_Aarti_at_Rishikesh.webm/960px--Ganga_Aarti_at_Rishikesh.webm.jpg"

def custom_section():
    steps = [("chat", "Share your idea", "Tell us where, when and who’s travelling."),
             ("map", "We design it", "Our experts build a tailored itinerary."),
             ("sliders", "Fine-tune together", "Change stays, pace or temples until it’s right."),
             ("spark", "Travel stress-free", "One coordinator with you from start to finish.")]
    st = "".join(f'<li><span class="cs-n">{i:02d}</span><span class="cs-i">{ic(icn, "1.8")}</span><div><b>{h}</b><small>{p}</small></div></li>' for i, (icn, h, p) in enumerate(steps, 1))
    feats = [("user", "Personalised", "Built around your interests"), ("sliders", "Flexible", "Your dates, your pace"),
             ("home", "Comfortable", "Hand-picked stays"), ("shield", "Worry-free", "Support throughout")]
    ft = "".join(f'<div class="cs-f"><span>{ic(i, "1.8")}</span><div><b>{h}</b><small>{p}</small></div></div>' for i, h, p in feats)
    return f"""
<section class="sec cs" id="custom">
  <div class="cs-deco" aria-hidden="true"></div>
  <div class="wrap">
    <div class="cs-grid">
      <div class="cs-video">
        <div class="cs-player">
          {img("custom", "Ganga Aarti at Triveni Ghat, Rishikesh")}
          <video class="cs-vid" autoplay muted loop playsinline preload="auto" poster="{CUSTOM_VIDEO_POSTER}" aria-label="Video: Ganga Aarti at Triveni Ghat, Rishikesh">
            <source src="{CUSTOM_VIDEO}" type="video/webm">
            <source src="{CUSTOM_VIDEO_SD}" type="video/webm">
          </video>
          <span class="cs-shade"></span>
          <button type="button" class="cs-pp" aria-label="Pause video" aria-pressed="false"><svg class="ic-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg><svg class="ic-play" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg></button>
          <button type="button" class="cs-sound" aria-label="Turn sound on" aria-pressed="false"><svg class="ic-off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path d="m23 9-6 6M17 9l6 6"/></svg><svg class="ic-on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/></svg></button>
          <span class="cs-vlabel"><b>Ganga Aarti at Triveni Ghat, Rishikesh</b><small>{ic("pin")}Experience it on our Char Dham Yatra</small></span>
        </div>
        <div class="cs-chip">{ic("headset", "1.8")}<div><b>Personal trip planning</b><small>Talk to a travel expert</small></div></div>
      </div>
      <div class="cs-copy">
        <span class="eyebrow">Custom Tour Packages</span>
        <h2>Travel your way, <em>made just for you</em></h2>
        <p>Journeys designed around your interests, pace, family needs, comfort and budget — from the first call to your return home.</p>
        <ol class="cs-steps">{st}</ol>
        <div class="cs-ctas">
          <a href="contact.html#enquire" class="btn btn-light">Design My Journey {ic("arrow")}</a>
          <a href="{wa("Hi Sanchari, I'd like to plan a custom trip.")}" target="_blank" rel="noopener" class="btn btn-outline"><span style="width:18px;height:18px;display:inline-flex">{WA_SVG}</span>Chat with an Expert</a>
        </div>
      </div>
    </div>
    <div class="cs-feats">{ft}</div>
  </div>
</section>
<div class="vmodal" id="vmodal" hidden>
  <div class="vm-bg" data-vclose></div>
  <div class="vm-box" role="dialog" aria-modal="true" aria-label="Video">
    <button type="button" class="vm-x" data-vclose aria-label="Close video"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
    <div class="vm-frame" id="vmFrame"></div>
  </div>
</div>"""


def temple_accordion(temples):
    panels = ""
    for i, t in enumerate(temples):
        hl = "".join(f"<li>{ic('temple', '1.8')}{E(b)}</li>" for b, _ in t["highlights"][:3])
        temples_n = next((v for k, v, l in t["stats"] if k == "temple"), "")
        panels += f"""
      <article class="ta-panel{' on' if i == 0 else ''}" tabindex="0" aria-expanded="{'true' if i == 0 else 'false'}" aria-label="{E(t['short'])}">
        <div class="ta-media">{img(t["images"][0], t["short"])}</div>
        <div class="ta-shade"></div>
        <div class="ta-closed"><span class="ta-num">0{i+1}</span><span class="ta-name">{E(t["region"])}</span><span class="ta-plus">+</span></div>
        <div class="ta-open">
          <div class="ta-top"><span class="ta-num">0{i+1}</span><span class="ta-chip">{ic("cal")}{t["days"]} Days · {t["nights"]} Nights</span></div>
          <div class="ta-body">
            <span class="ta-region">{ic("pin")}{E(t["region"])} · {E(t["route"])}</span>
            <h3>{E(t["short"])}</h3>
            <p>{E(t["overview"][0].split(" — ")[0].rstrip(".") + ".")}</p>
            <ul>{hl}</ul>
            <div class="ta-foot">
              <div class="ta-stats"><span><b>{temples_n}</b>Temples</span><span><b>{inr(t["price"])}</b>From / person</span></div>
              <a class="ta-btn" href="{t["slug"]}.html">Explore Journey {ic("arrow")}</a>
            </div>
          </div>
        </div>
      </article>"""
    return f'<div class="ta" id="templeAcc">{panels}</div>'


HERO_SLIDES = [
    dict(img="hero-s1", tag="Temple Tours", h="Sacred Journeys to India’s Great Temples",
         p="From the Himalayan Char Dham to the living temples of the south — pilgrimages with darshan schedules, comfortable stays and local guides.",
         link="temple-tours.html", cta="Explore Temple Tours"),
    dict(img="hero-s2", tag="Adventure Tours", h="Climb Higher. Reach the World’s Great Summits",
         p="Everest Base Camp, Kilimanjaro and Mount Elbrus — expeditions led by experienced mountaineers, with acclimatisation and safety built in.",
         link="adventure-tours.html", cta="Explore Adventure Tours"),
    dict(img="hero-s3", tag="Wellness Tours", h="Slow Down, Breathe and Restore",
         p="Unhurried journeys through sacred places, nature and quiet coastlines — designed to leave you rested, renewed and balanced.",
         link="wellness-tours.html", cta="Explore Wellness Tours"),
]

def hero_slider():
    """Home hero: full-width fade slider with Ken Burns zoom, centred text, arrows and dots
    (modelled on the live Sanchari site's Elementor slider)."""
    slides = "".join(f'''
    <div class="hv-slide{" on" if i == 0 else ""}" role="group" aria-roledescription="slide" aria-label="{i+1} of {len(HERO_SLIDES)}" aria-hidden="{"false" if i == 0 else "true"}">
      <div class="hv-bg" style="background-image:url('assets/img/{d["img"]}.svg')" data-bg-real="{IM.real_url(d["img"])}"></div>
      <div class="hv-overlay"></div>
      <div class="hv-inner">
        <span class="hv-tag">{d["tag"]}</span>
        {"<h1" if i == 0 else "<h2"} class="hv-title">{d["h"]}{"</h1>" if i == 0 else "</h2>"}
        <p class="hv-text">{d["p"]}</p>
        <div class="hv-ctas"><a href="{d["link"]}" class="hv-btn"{"" if i == 0 else ' tabindex="-1"'}>{d["cta"]}</a><a href="contact.html?type=custom#enquire" class="hv-btn hv-btn-2"{"" if i == 0 else ' tabindex="-1"'}>Create Your Own Journey</a></div>
      </div>
    </div>''' for i, d in enumerate(HERO_SLIDES))
    dots = "".join(f'<button type="button" class="{"on" if i == 0 else ""}" aria-label="Go to slide {i+1}"></button>' for i in range(len(HERO_SLIDES)))
    return f'''
<section class="hv" id="heroSlider" aria-roledescription="carousel" aria-label="Featured journeys">
  {slides}
  <button type="button" class="hv-arrow prev" aria-label="Previous slide"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M15 4l-8 8 8 8"/></svg></button>
  <button type="button" class="hv-arrow next" aria-label="Next slide"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 4l8 8-8 8"/></svg></button>
  <div class="hv-dots">{dots}</div>
</section>'''

def _mp(lon, lat):  # simple projection for the stylised South India map (viewBox 0 0 420 518)
    return round((lon - 72) * 30, 1), round((21 - lat) * 37, 1)

MAP_PINS = {"telangana": (78.5, 17.4, "Hyderabad"), "andhra": (80.6, 16.5, "Vijayawada"),
            "tamilnadu": (79.1, 10.8, "Thanjavur"), "kerala": (76.2, 10.5, "Thrissur")}

def temple_map(temples):
    outline = [(72.8,21),(72.9,19),(73.4,17),(73.8,15.5),(74.6,13),(75.4,11.8),(76.2,10),(76.6,8.9),(77.5,8.1),
               (78.2,8.9),(79.2,9.3),(79.8,10.3),(79.85,11.8),(80.3,13.1),(80.1,14.5),(80.3,15.8),(81.3,16.4),
               (82.3,16.9),(83.3,17.7),(84.5,18.8),(85.8,19.8),(86.9,21)]
    pts = " ".join(f"{x},{y}" for x, y in (_mp(*p) for p in outline))
    geo = ["telangana", "andhra", "tamilnadu", "kerala"]
    order = sorted([t for t in temples if t["rkey"] in MAP_PINS], key=lambda t: geo.index(t["rkey"]))
    route = [_mp(*MAP_PINS[k][:2]) for k in ["telangana", "andhra", "tamilnadu", "kerala"] if any(t["rkey"] == k for t in order)]
    path = "M" + " L".join(f"{x},{y}" for x, y in route)
    # labels for neighbouring states (decorative)
    labels = [("KARNATAKA", 75.2, 14.2), ("MAHARASHTRA", 75.5, 19.6), ("ODISHA", 84.2, 20.4)]
    lab = "".join(f'<text x="{_mp(lo,la)[0]}" y="{_mp(lo,la)[1]}" class="tm-lbl">{n}</text>' for n, lo, la in labels)
    pins, cards, tabs = "", "", ""
    for i, t in enumerate(order):
        lon, lat, city = MAP_PINS[t["rkey"]]
        x, y = _mp(lon, lat)
        on = " on" if i == 0 else ""
        pins += f'''<button type="button" class="tm-pin{on}" data-i="{i}" style="left:{x/420*100:.2f}%;top:{y/518*100:.2f}%" aria-label="{E(t["region"])}: {E(t["short"])}">
          <span class="tm-dot"><b>{i+1}</b></span><span class="tm-tip">{E(t["region"])}<small>{city}</small></span></button>'''
        temples_n = next((v for k, v, l in t["stats"] if k == "temple"), "")
        hl = "".join(f"<li>{ic('temple','1.8')}{E(b)}</li>" for b, _ in t["highlights"][:3])
        cards += f'''
        <article class="tm-card{on}" data-i="{i}" aria-hidden="{"false" if i == 0 else "true"}">
          <a class="tm-photo" href="{t["slug"]}.html" tabindex="{0 if i == 0 else -1}">{img(t["images"][0], t["short"])}
            <span class="tm-badge">0{i+1} · {E(t["region"])}</span><span class="tm-days">{ic("cal")}{t["days"]} Days</span></a>
          <div class="tm-body">
            <span class="tm-route">{ic("pin")}{E(t["route"])}</span>
            <h3>{E(t["short"])}</h3>
            <p>{E(t["overview"][0].split(" — ")[0].rstrip(".") + ".")}</p>
            <ul>{hl}</ul>
            <div class="tm-foot">
              <div class="tm-stats"><span><b>{temples_n}</b>Temples</span><span><b>{t["nights"]}</b>Nights</span><span><b>{inr(t["price"])}</b>From / person</span></div>
              <a class="btn btn-gold" href="{t["slug"]}.html" tabindex="{0 if i == 0 else -1}">Explore {ic("arrow")}</a>
            </div>
          </div>
        </article>'''
        tabs += f'''<button type="button" class="tm-tab{on}" data-i="{i}"><small>0{i+1}</small><b>{E(t["region"])}</b><span>{t["days"]} days · {inr(t["price"])}</span></button>'''
    svg = f'''<svg class="tm-svg" viewBox="0 0 420 518" aria-hidden="true">
        <defs><pattern id="tmGrid" width="22" height="22" patternUnits="userSpaceOnUse"><path d="M22 0H0V22" fill="none" stroke="#ead6ca" stroke-width=".6"/></pattern></defs>
        <rect width="420" height="518" fill="url(#tmGrid)"/>
        <polygon points="{pts}" class="tm-land-edge"/>
        {lab}
        <text x="370" y="420" class="tm-sea">BAY OF<tspan x="370" dy="14">BENGAL</tspan></text>
        <text x="40" y="440" class="tm-sea">ARABIAN<tspan x="40" dy="14">SEA</tspan></text>
        <path d="{path}" class="tm-path"/>
      </svg>'''
    return f'''
    <div class="tm" id="templeMap">
      <div class="tm-map">{svg}{pins}<div class="tm-legend"><span class="tm-ld"></span>Our temple circuit</div></div>
      <div class="tm-cards">{cards}</div>
    </div>
    <div class="tm-tabs" role="tablist">{tabs}</div>'''

def temple_stack(temples):
    """Home: Temple Journeys - sticky intro on the left, journey cards that stack on scroll."""
    alln = len(temples)
    states = len({t["region"] for t in temples})
    zones = [z for z in ZONES if any(t.get("zone") == z for t in temples)]
    pick = ["tour-char-dham-yatra", "tour-kashi-prayagraj-ayodhya", "tour-dwarka-somnath", "tour-puri-konark-bhubaneswar", "tour-tamil-nadu-temple-journey"]
    allt = temples
    temples = [t for s_ in pick for t in allt if t["slug"] == s_] or allt[:5]
    n = len(temples)
    total_t = sum(int(next((v for k, v, l in t["stats"] if k == "temple"), "0").rstrip("+") or 0) for t in temples)
    low = min(t["price"] for t in allt)
    cards = ""
    for i, t in enumerate(temples):
        temples_n = next((v for k, v, l in t["stats"] if k == "temple"), "")
        chips = "".join(f"<li>{ic('temple','1.8')}{E(b)}</li>" for b, _ in t["highlights"][:3])
        thumbs = "".join(f'<span class="tj-thumb">{img(k, t["short"])}</span>' for k in t["images"][1:3])
        cards += f"""
      <article class="tj-card" style="--i:{i}">
        <a class="tj-media" href="{t["slug"]}.html" tabindex="-1" aria-hidden="true">
          {img(t["images"][0], t["short"])}
          <span class="tj-region">{ic("pin")}{E(t["region"])} · {ZONES.get(t.get("zone"), "")}</span>
          <div class="tj-thumbs">{thumbs}</div>
        </a>
        <div class="tj-body">
          <div class="tj-top"><span class="tj-num">0{i+1}<small>/0{n}</small></span><span class="tj-days">{ic("cal")}{t["days"]} Days · {t["nights"]} Nights</span></div>
          <h3><a href="{t["slug"]}.html">{E(t["short"])}</a></h3>
          <p class="tj-route">{ic("map")}{E(t["route"])}</p>
          <ul class="tj-chips">{chips}</ul>
          <div class="tj-foot">
            <div class="tj-facts"><span><b>{temples_n}</b>Temples</span><span><b>{inr(t["price"])}</b>From / person</span></div>
            <a class="tj-btn" href="{t["slug"]}.html">View Journey {ic("arrow")}</a>
          </div>
        </div>
      </article>"""
    return f"""
<section class="sec tj-sec">
  <div class="wrap tj">
    <aside class="tj-intro">
      <span class="eyebrow">Temple Journeys</span>
      <h2>Journeys to India’s sacred temples</h2>
      <p>From the Himalayan dhams to the shore temples of the south, carefully paced pilgrimages across India — with darshan timings, comfortable stays and local guides arranged for you.</p>
      <div class="tj-kpis">
        <div><b>{alln}</b><span>Temple circuits</span></div>
        <div><b>{states}</b><span>States covered</span></div>
        <div><b>{inr(low)}</b><span>Starting price</span></div>
      </div>
      <div class="tj-acts"><a href="temple-tours.html" class="btn btn-gold">View all temple tours {ic("arrow")}</a></div>
      <ol class="tj-index">{"".join(f'<li><a href="temple-tours.html?region={z}#tours"><span>{sum(t.get("zone") == z for t in allt)}</span>{ZONES[z]}</a></li>' for z in zones)}</ol>
    </aside>
    <div class="tj-stack">{cards}
    </div>
  </div>
</section>"""

def temple_bento(temples):
    """Home: Temple Journeys - zone filter pills + bento mosaic of every temple tour."""
    big, wide = "tour-char-dham-yatra", "tour-kashi-prayagraj-ayodhya"
    order = sorted(temples, key=lambda t: (t["slug"] != big, t["slug"] != wide))
    zones = [z for z in ZONES if any(t.get("zone") == z for t in temples)]
    pills = '<button type="button" class="tb-pill on" data-z="all">All <small>' + str(len(temples)) + '</small></button>' + "".join(
        f'<button type="button" class="tb-pill" data-z="{z}">{ZONES[z]} <small>{sum(t.get("zone") == z for t in temples)}</small></button>' for z in zones)
    tiles = ""
    for t in order:
        size = " tb-big" if t["slug"] == big else (" tb-wide" if t["slug"] == wide else "")
        hl = "".join(f"<li>{E(b)}</li>" for b, _ in t["highlights"][:4]) if size else ""
        tiles += f"""
      <a class="tb-tile{size}" href="{t["slug"]}.html" data-zone="{t.get("zone","")}">
        {img(t["images"][0], t["short"])}
        <span class="tb-top"><span class="tb-chip">{ic("pin")}{E(t["region"])}</span><span class="tb-days">{t["days"]}D / {t["nights"]}N</span></span>
        <span class="tb-body">
          <small class="tb-zone">{ZONES.get(t.get("zone"), "")}</small>
          <b class="tb-title">{E(t["short"])}</b>
          {f'<ul class="tb-hl">{hl}</ul>' if hl else ""}
          <span class="tb-foot"><span class="tb-price"><small>From</small>{inr(t["price"])}</span><span class="tb-go" aria-hidden="true">{ic("arrow")}</span></span>
        </span>
      </a>"""
    tiles += f"""
      <a class="tb-tile tb-cta" href="contact.html#enquire" data-zone="all">
        <span class="tb-cta-ico">{ic("compass", "1.8")}</span>
        <b>Don’t see your temple?</b>
        <span>Tell us the shrines you wish to visit and we’ll plan a custom pilgrimage anywhere in India.</span>
        <span class="tb-cta-btn">Plan a custom pilgrimage {ic("arrow")}</span>
      </a>"""
    return f"""
<section class="sec tb-sec">
  <div class="wrap">
    <div class="tb-head">
      {sec_head("Temple Journeys", "Sacred journeys across every corner of India", "From the Himalayan dhams to the shore temples of the south — pick a region to explore.")}
      <a href="temple-tours.html" class="btn btn-line">View all temple tours {ic("arrow")}</a>
    </div>
    <div class="tb-pills" role="group" aria-label="Filter temple journeys by region">{pills}</div>
    <div class="tb-grid" id="templeBento">{tiles}
    </div>
  </div>
</section>"""

# ------------------------------------------------------------ home
def home():
    slides = [("Discover. Experience. Connect.", "Discover the <em>soul of India</em>",
               "From the Himalayan dhams to the great temples of the south, experience India’s sacred places, rich traditions and breathtaking landscapes.", "temple-tours.html"),
              ("Temple Journeys", "Explore the heart of <em>ancient temples</em>",
               "Centuries-old temples, sacred traditions, timeless architecture and the stories behind them — thoughtfully planned.", "temple-tours.html"),
              ("Wellness & Adventure", "Refresh your mind, <em>reach new heights</em>",
               "Restorative wellness journeys and expertly led expeditions to the world’s great summits.", "wellness-tours.html")]
    sl = "".join(f'''<div class="slide{" on" if i == 0 else ""}"><span class="eyebrow">{e}</span><h1>{h}</h1><p class="lead">{p}</p>
      <div class="hero-ctas"><a href="{l}" class="btn btn-gold">Explore More {ic("arrow")}</a><a href="contact.html#enquire" class="btn btn-outline">Plan a Custom Trip</a></div></div>''' for i, (e, h, p, l) in enumerate(slides))
    dots = "".join(f'<button class="{"on" if i == 0 else ""}" aria-label="Slide {i+1}"></button>' for i in range(3))
    regions = []
    for t in TOURS:
        if t["rkey"] not in [r[0] for r in regions]: regions.append((t["rkey"], t["region"], t["cat"]))
    # destinations per activity for the home search (Activity -> Destination)
    import json as _json
    _dest = {}
    for cat_ in ("temple", "adventure", "wellness"):
        ts = [t for t in TOURS if t["cat"] == cat_]
        groups = []
        if cat_ == "temple":
            for z in ZONES:
                zs = [t for t in ts if t.get("zone") == z]
                if zs:
                    opts = [[z, f"All of {ZONES[z]} ({len(zs)})"]] + [[t["rkey"], t["region"]] for t in zs]
                    groups.append([ZONES[z], opts])
        else:
            groups.append(["", [[t["rkey"], t["region"]] for t in ts]])
        _dest[cat_] = dict(all=f"All {CATS[cat_]['name'].lower()} ({len(ts)})", groups=groups)
    dopts = ""
    hs_data = _json.dumps(_dest, ensure_ascii=False).replace("</", "<\\/")
    temples = [t for t in TOURS if t["cat"] == "temple"]
    advs = [t for t in TOURS if t["cat"] == "adventure"]
    wells = [t for t in TOURS if t["cat"] == "wellness"]
    def cat_tile(cat, count):
        c = CATS[cat]
        return f'''<a class="cat" href="{c["file"]}">{img(c["tile"], c["name"])}<div class="cat-body"><span>{count} {"journeys" if count > 1 else "journey"}</span><h3>{c["name"]}</h3><p>{c["blurb"]}</p><b>Explore Packages {ic("arrow")}</b></div></a>'''
    sindia = [t for t in TOURS if t["cat"] in ("temple", "wellness")]
    # destinations: one card per state, grouped by zone (North → South)
    zord = list(ZONES)
    dmap = {}
    for t in sindia:
        dmap.setdefault(t["rkey"], []).append(t)
    dlist = sorted(dmap.values(), key=lambda ts: zord.index(ts[0].get("zone", "south")))
    def dcard(ts):
        t0 = ts[0]; n = len(ts); z = ZONES.get(t0.get("zone", "south"))
        names = " · ".join(E(x["short"]) for x in ts)
        return (f'<a class="dc" href="{CATS[t0["cat"]]["file"]}?region={t0["rkey"]}#tours">'
                f'<span class="dc-img">{img(t0["images"][0], t0["region"])}</span>'
                f'<span class="dc-txt"><small>{z}</small><b>{E(t0["region"])}</b><em>{names}</em>'
                f'<span class="dc-meta">{n} {"journey" if n == 1 else "journeys"} · from {inr(min(x["price"] for x in ts))}</span></span>'
                f'<span class="dc-go" aria-hidden="true">{ic("arrow")}</span></a>')
    dest = "".join(dcard(ts) for ts in dlist) + (
        f'<a class="dc dc-cta" href="contact.html#enquire"><span class="dc-img dc-ico">{ic("compass", "1.8")}</span>'
        f'<span class="dc-txt"><small>Anywhere in India</small><b>Plan a custom trip</b><em>Tell us where you want to go</em>'
        f'<span class="dc-meta">Get a tailored itinerary &amp; quote</span></span><span class="dc-go" aria-hidden="true">{ic("arrow")}</span></a>')
    dest_n = len(dlist)
    posts = "".join(blog_card(p) for p in POSTS)
    body = f'''
{hero_slider()}
<div class="search-panel bg-sand"><div class="wrap">
  <form class="search-card home-search" id="homeSearch">
    <div class="field"><label for="hAct">Activity</label><select id="hAct"><option value="" selected>Select activity</option><option value="temple">Temple Tours</option><option value="adventure">Adventure Tours</option><option value="wellness">Wellness Tours</option></select></div>
    <div class="field"><label for="hDest">Destination</label><select id="hDest" disabled><option value="all">Select an activity first</option></select></div>
    <div class="field"><label for="hDate">When</label><input type="month" id="hDate"></div>
    <button class="btn btn-dark" type="submit">{ic("search")}Find Tours</button>
    <p class="hs-err" id="hsErr" role="alert"></p>
  </form>
  <script type="application/json" id="hsData">{hs_data}</script>
</div></div>
<section class="trust-sec bg-sand">
  <div class="wrap">
    <div class="trust">
      <div class="trust-i"><span class="trust-n">01</span><div class="trust-ico">{ic("compass", "1.8")}</div><h3>Handpicked Journeys</h3><p>Every itinerary is researched and planned by people who know these places.</p></div>
      <div class="trust-i"><span class="trust-n">02</span><div class="trust-ico">{ic("tag", "1.8")}</div><h3>Transparent Pricing</h3><p>Clear per-person prices with inclusions listed upfront — no surprises.</p></div>
      <div class="trust-i"><span class="trust-n">03</span><div class="trust-ico">{ic("headset", "1.8")}</div><h3>Support Throughout</h3><p>One team coordinating routes, stays and schedules from start to finish.</p></div>
    </div>
  </div>
</section>
<section class="sec bg-white">
  <div class="wrap">
    {sec_head("Discover. Experience. Connect.", "Explore experiences that inspire every journey", "Spiritual journeys, adventures and wellness — across India and beyond.", True)}
    <div class="cats">{cat_tile("temple", len(temples))}{cat_tile("adventure", len(advs))}{cat_tile("wellness", len(wells))}</div>
  </div>
</section>
{dest_carousel()}
{circuits_sec(home=True)}
{enquiry()}
<section class="sec bg-white">
  <div class="wrap">
    <div class="sec-top">{sec_head("Adventure Journeys", "Journeys made for every adventurer", "Expeditions run with Anmish Adventures.")}<a href="adventure-tours.html" class="btn btn-line">View all expeditions</a></div>
    <div class="ex-grid">{"".join(card_ex(t, i) for i, t in enumerate(advs))}</div>
  </div>
</section>
<section class="sec bg-sand">
  <div class="wrap">
    {sec_head("Travel Better. Experience More.", "Every journey, thoughtfully planned", "", True)}
    <div class="pillars">
      <div class="pillar"><small>01</small><h3>Curated with context</h3><p>Destinations chosen for their history, traditions and culture — with the stories that bring them to life.</p><a href="about-us.html">About us →</a></div>
      <div class="pillar"><small>02</small><h3>Planned around people</h3><p>Journeys shaped around age, interests, pace, family needs and comfort.</p><a href="contact.html#enquire">Plan a trip →</a></div>
      <div class="pillar"><small>03</small><h3>Supported throughout</h3><p>Routes, stays, temple schedules and travel coordinated by one partner.</p><a href="contact.html">Contact us →</a></div>
    </div>
    <div class="stats-band" style="margin-top:48px">
      <div><b>{len(TOURS)}</b><span>Curated journeys</span></div>
      <div><b>{len({t["region"] for t in TOURS if t["cat"] != "adventure"})}</b><span>Indian states</span></div>
      <div><b>{len([t for t in TOURS if t["cat"] == "adventure"])}</b><span>International summits</span></div>
      <div><b>{len(ZONES)}</b><span>Regions of India</span></div>
    </div>
  </div>
</section>
<section class="sec bg-white">
  <div class="wrap">
    <div class="sec-top">{sec_head("From the Blog", "Travel tips and advice")}<a href="blog.html" class="btn btn-line">View all articles</a></div>
    <div class="b-grid">{posts}</div>
  </div>
</section>
{custom_section()}'''
    page("index.html", "Sanchari Travel | Temple, Adventure & Wellness Journeys",
         "Discover the soul of India with curated temple tours, expert-led adventure expeditions and restorative wellness journeys.", "Home", body)

# ------------------------------------------------------------ about
def about():
    team = [("team1", "Mr. Dil Raju", "Investor & Visionary"), ("team2", "Mr. Pranay Nistala", "Founder"),
            ("team3", "Mrs. Vygha Reddy", "Founder"), ("team4", "Ganesh Reddy", "Founding Member"), ("team5", "Karthik", "Founding Member")]
    tm = "".join(f'<div class="member"><div class="member-img">{img(k, n)}</div><b>{n}</b><span>{r}</span></div>' for k, n, r in team)
    body = hero("hero-about", [("Home", "index.html"), ("About Us", None)], "Est. 2026", "The bridge to <em>every corner of India</em>",
                "Sanchari makes travel across India welcoming and effortless — removing the barriers of language, logistics and distance.", cls="page-hero compact no-overlap")
    body += f'''
<section class="sec">
  <div class="wrap about-split">
    <div class="about-img">{img("about-main", "Sanchari")}<span class="est">EST. 2026</span></div>
    <div>
      <span class="eyebrow">The Sanchari Mission</span>
      <h2 style="font-size:clamp(24px,2.7vw,36px);margin:12px 0 16px">India’s diversity is its greatest strength</h2>
      <p class="lead-sm">Yet its sheer size can keep travellers from exploring beyond familiar regions — even though its spiritual centres, heritage sites and landscapes are all within reach.</p>
      <p class="lead-sm" style="margin-top:14px">Sanchari exists to bridge that gap, making travel across India welcoming and effortless.</p>
      <div class="quote">“We are the bridge that connects the diverse corners of India.”</div>
      <a href="contact.html#enquire" class="btn btn-gold">Plan a Journey With Us</a>
    </div>
  </div>
</section>
<section class="sec sec-alt">
  <div class="wrap">
    {sec_head("Experience Bharat", "Three pillars of travel", "Immersive journeys beyond standard itineraries — connecting you with heritage, spirituality and nature, supported by local experts and dependable infrastructure.", True)}
    <div class="pillars">
      <div class="pillar"><small>The Soul Within</small><h3>Temple Tourism</h3><p>Curated pilgrimages to sacred sites with comfortable stays and well-planned darshans.</p><a href="temple-tours.html">Temple tours →</a></div>
      <div class="pillar"><small>The Energy</small><h3>Adventure Experiences</h3><p>Trekking, expeditions and the outdoors — led by expert teams.</p><a href="adventure-tours.html">Adventure tours →</a></div>
      <div class="pillar"><small>The Renewal</small><h3>Wellness &amp; Activities</h3><p>Ayurveda, guided yoga, mindful activities and nature stays.</p><a href="wellness-tours.html">Wellness tours →</a></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap">
    {sec_head("Why Sanchari", "Built on trust and reliability", "Transparent, secure and carefully planned experiences — from departure to return.", True)}
    {why_grid([("access", "The Companion Model", "On-ground help for senior and differently-abled travellers — at heritage sites, during transfers and wherever mobility needs arise."),
               ("headset", "24/7 Journey Support", "Round-the-clock help with itinerary changes, local guidance and unexpected needs."),
               ("shield", "Safety, Security & Care", "Verified accommodation, trusted transport, experienced guides and sound safety practices."),
               ("map", "End-to-End Support", "Coordination from departure to return, including flights, transfers, stays and activities.")])}
  </div>
</section>
<section class="sec sec-alt"><div class="wrap">{leader_block()}</div></section>
<section class="sec">
  <div class="wrap">
    {sec_head("Our Team", "The people behind Sanchari", "", True)}
    <div class="team">{tm}</div>
  </div>
</section>
{enquiry()}'''
    page("about-us.html", "About Us | Sanchari Travel", "Sanchari makes travel across India welcoming and effortless — temple, adventure and wellness journeys from Hyderabad.", "About Us", body)

# ------------------------------------------------------------ contact
def contact():
    body = hero("hero-contact", [("Home", "index.html"), ("Contact", None)], "Get in Touch", "Let’s plan your <em>next journey</em>",
                "Our travel experts are here to help with bookings, package details and support — Monday to Friday, 08:00 to 20:00.", cls="page-hero compact")
    body += f'''
<section style="padding-bottom:40px"><div class="wrap">
  <div class="c-cards">
    <div class="c-card"><div class="ico">{ic("pin", "1.8")}</div><small>Our office</small><b>Hyderabad, India</b><p>Telangana</p></div>
    <div class="c-card"><div class="ico">{ic("phone", "1.8")}</div><small>Call our experts</small><a class="v" href="tel:{TEL}">{PHONE}</a><p>{HOURS}</p></div>
    <div class="c-card"><div class="ico">{ic("mail", "1.8")}</div><small>Email us</small><a class="v" href="mailto:{EMAIL}">{EMAIL}</a><p>We reply within one business day</p></div>
    <div class="c-card"><div class="ico">{ic("chat", "1.8")}</div><small>Chat with us</small><a class="v" href="{wa("Hi Sanchari, I have a question.")}" target="_blank" rel="noopener">WhatsApp</a><p>{HOURS}</p></div>
  </div>
</div></section>
{enquiry()}
{faq_block("FAQs", "Before you get in touch", [
  ("How soon will you respond?", "We usually respond within one business day. For urgent queries, call or WhatsApp us during working hours."),
  ("Can you plan a trip that isn’t listed?", "Yes. Our team designs custom itineraries around your destination, dates, pace and budget."),
  ("Do you arrange group tours?", "Yes — for families, communities and corporate groups, with vehicles and stays sized to your group."),
  ("How do I pay?", "We accept Visa, Mastercard, American Express and JCB cards. Payment details are shared once your itinerary is confirmed.")], lead=False)}'''
    page("contact.html", "Contact Us | Sanchari Travel", "Get in touch with Sanchari’s travel experts in Hyderabad — call, email or WhatsApp.", "Contact", body)

# ------------------------------------------------------------ blog
def blog_card(p):
    return f'''<a class="b-card" href="{p["slug"]}.html"><div class="b-img">{img(p["img"], p["title"])}</div>
      <div class="b-body"><div class="b-meta"><span class="region">{E(p["cat"])}</span><span>{p["date"]}</span></div>
      <h3>{E(p["title"])}</h3><p>{E(p["excerpt"])}</p><span class="more">Read article →</span></div></a>'''

def blog():
    body = hero("hero-blog", [("Home", "index.html"), ("Blog", None)], "Travel Tips &amp; Advice", "Stories and advice for <em>better journeys</em>",
                "Practical guidance for temple tours, high-altitude treks and travelling with family.", cls="page-hero compact no-overlap")
    body += f'''
<section class="sec"><div class="wrap"><div class="b-grid">{"".join(blog_card(p) for p in POSTS)}</div></div></section>'''
    page("blog.html", "Blog | Sanchari Travel", "Travel tips and advice from Sanchari — temple etiquette, trek preparation and family travel.", "Blog", body)
    for i, p in enumerate(POSTS):
        content = ""
        for kind, v in p["body"]:
            if kind == "p": content += f"<p>{E(v)}</p>"
            elif kind == "h2": content += f"<h2>{E(v)}</h2>"
            elif kind == "ul": content += "<ul>" + "".join(f"<li>{E(x)}</li>" for x in v) + "</ul>"
        others = [x for x in POSTS if x is not p]
        b = f'''
<section class="d-top bp-top">
  <div class="wrap"><div class="article">
    <div class="crumbs d-crumbs"><a href="index.html">Home</a><span>/</span><a href="blog.html">Blog</a><span>/</span><span>Article</span></div>
    <span class="eyebrow">{E(p["cat"])}</span>
    <h1>{E(p["title"])}</h1>
    <div class="b-meta"><span>By Sanchari Team</span><span>·</span><span>{p["date"]}</span><span>·</span><span>{p["read"]}</span></div>
  </div></div>
</section>
<section class="sec bp-body">
  <div class="wrap"><div class="article">
    <div class="article-img">{img(p["img"], p["title"])}</div>
    <div class="prose">{content}</div>
    <div class="article-cta"><div><h3>Ready to plan your journey?</h3><p>Talk to our team about tours and custom itineraries.</p></div><a href="contact.html#enquire" class="btn btn-gold">Get in Touch</a></div>
  </div></div>
</section>
<section class="sec related"><div class="wrap">
  <div class="block-head" style="margin-bottom:32px"><div><span class="eyebrow">Keep reading</span><h2 style="font-size:clamp(22px,2.4vw,30px);margin-top:10px">More articles</h2></div><a href="blog.html" class="btn btn-dark">All articles</a></div>
  <div class="b-grid" style="grid-template-columns:repeat(2,1fr)">{"".join(blog_card(x) for x in others)}</div>
</div></section>'''
        page(p["slug"] + ".html", f'{p["title"]} | Sanchari Travel', p["excerpt"], "Blog", b)


# ------------------------------------------------------------ invoice
# Business details printed on the invoice. Fill these in before going live.
BIZ = dict(name="Sanchari Travel", address="Hyderabad, Telangana, India", gstin="", pan="",
           bank="", account="", ifsc="", upi="")
TAX = dict(label="GST", rate=0.05)   # confirm the applicable GST rate with your accountant

def invoice():
    import json
    tours = {t["slug"]: dict(title=t["title"], short=t["short"], route=t["route"], days=t["days"], nights=t["nights"],
                             price=t["price"], cat=CATS[t["cat"]]["name"], region=t["region"], incl=t["incl"][:6])
             for t in TOURS}
    data = json.dumps(dict(tours=tours, tax=TAX), ensure_ascii=False).replace("</", "<\\/")
    def row(k, v): return f'<div><small>{k}</small><b>{v}</b></div>'
    missing = '<em class="iv-todo">To be added</em>'
    body = f"""
<section class="iv-wrap">
  <div class="wrap">
    <div class="iv-bar no-print">
      <div><span class="eyebrow">Booking received</span><h1 class="iv-h">Your booking invoice</h1>
        <p id="ivIntro">Thank you for booking with Sanchari. Our team will call you to confirm availability and payment.</p></div>
      <div class="iv-actions">
        <button type="button" class="btn btn-gold" id="ivPrint">{ic("arrow")}Download / Print PDF</button>
        <a class="btn btn-line" href="index.html">Back to Home</a>
      </div>
    </div>

    <article class="iv" id="invoice" aria-label="Invoice">
      <header class="iv-head">
        <div class="iv-brand">
          <img src="assets/img/logo.png" alt="Sanchari" width="991" height="271">
          <p>{BIZ["address"]}<br>{PHONE} · {EMAIL}</p>
          <p class="iv-ids">GSTIN: {BIZ["gstin"] or missing}{f' · PAN: {BIZ["pan"]}' if BIZ["pan"] else ""}</p>
        </div>
        <div class="iv-title">
          <h2>Invoice</h2>
          <span class="iv-status" id="ivStatus">Payment pending</span>
          <dl>
            <dt>Invoice no.</dt><dd id="ivNo">—</dd>
            <dt>Invoice date</dt><dd id="ivDate">—</dd>
            <dt>Booking ref.</dt><dd id="ivRef">—</dd>
          </dl>
        </div>
      </header>

      <div class="iv-parties">
        <div><h3>Billed to</h3><p><b id="ivName">—</b><br><span id="ivPhone">—</span><br><span id="ivEmail"></span></p></div>
        <div><h3>Tour</h3><p><b id="ivTour">—</b><br><span id="ivRoute">—</span><br><span id="ivCat"></span></p></div>
        <div><h3>Travel</h3><p><span id="ivDates">—</span><br><span id="ivStyle">—</span><br><span id="ivPax">—</span></p></div>
      </div>

      <table class="iv-table">
        <thead><tr><th>Description</th><th class="num">Qty</th><th class="num">Rate</th><th class="num">Amount</th></tr></thead>
        <tbody id="ivRows"></tbody>
      </table>

      <div class="iv-sum">
        <div class="iv-incl"><h3>Package includes</h3><ul id="ivIncl"></ul></div>
        <dl class="iv-totals">
          <dt>Subtotal</dt><dd id="ivSub">—</dd>
          <dt id="ivTaxL">GST</dt><dd id="ivTax">—</dd>
          <dt class="iv-grand">Total</dt><dd class="iv-grand" id="ivTotal">—</dd>
          <dt>Amount paid</dt><dd id="ivPaid">₹0</dd>
          <dt class="iv-due">Balance due</dt><dd class="iv-due" id="ivDue">—</dd>
        </dl>
      </div>
      <p class="iv-words" id="ivWords"></p>

      <div class="iv-foot">
        <div><h3>Payment details</h3>
          <p>Bank: {BIZ["bank"] or missing}<br>A/c no.: {BIZ["account"] or missing}<br>IFSC: {BIZ["ifsc"] or missing}<br>UPI: {BIZ["upi"] or missing}</p></div>
        <div><h3>Notes</h3>
          <ul>
            <li>This booking is provisional until our team confirms availability and dates.</li>
            <li>Child pricing and the final total may be revised on confirmation.</li>
            <li>Entry fees, special darshan tickets and personal expenses are not included unless listed.</li>
          </ul></div>
        <div class="iv-sign"><div class="iv-line"></div><small>Authorised signatory<br>{BIZ["name"]}</small></div>
      </div>
      <p class="iv-thanks">Thank you for travelling with Sanchari.</p>
    </article>
  </div>
</section>
<script type="application/json" id="ivData">{data}</script>"""
    page("invoice.html", "Booking Invoice | Sanchari Travel", "Your Sanchari booking invoice.", "", body)

# ------------------------------------------------------------ my account
def account():
    import json
    tours = {t["slug"]: dict(short=t["short"], title=t["title"], route=t["route"], days=t["days"], nights=t["nights"],
                             price=t["price"], cat=CATS[t["cat"]]["name"], region=t["region"],
                             img="assets/img/" + t["images"][0] + ".svg", real=IM.real_url(t["images"][0]))
             for t in TOURS}
    data = json.dumps(dict(tours=tours, tax=TAX, wa=TEL.lstrip("+")), ensure_ascii=False).replace("</", "<\\/")
    nav = [("dashboard", "home", "Dashboard"), ("bookings", "cal", "My Bookings"), ("wishlist", "heart", "Wishlist"), ("profile", "user", "Profile")]
    side = "".join(f'<a href="#{k}" class="ac-link" data-pane="{k}">{ic(i)}<span>{n}</span><b class="ac-badge" data-count="{k}"></b></a>' for k, i, n in nav)
    body = f"""
<section class="ac-wrap">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a><span>/</span><span>My Account</span></div>

    <div class="ac-guest" id="acGuest" hidden>
      <div class="ac-guest-ico">{ic("user","1.8")}</div>
      <h1>Your Sanchari account</h1>
      <p>Log in or create an account to see your bookings, download invoices and keep a wishlist of tours.</p>
      <div class="ac-guest-acts"><button type="button" class="btn btn-gold" data-auth="login">Log In</button><button type="button" class="btn btn-line" data-auth="signup">Create Account</button></div>
    </div>

    <div class="ac" id="acApp" hidden>
      <aside class="ac-side">
        <div class="ac-user"><span class="ac-av" id="acAv">S</span><div><b id="acName">Traveller</b><small id="acMail"></small></div></div>
        <nav class="ac-nav" aria-label="Account">{side}
          <button type="button" class="ac-link ac-out" id="acLogout">{ic("arrow")}<span>Log out</span></button>
        </nav>
        <div class="ac-help"><b>Need help with a booking?</b><a href="tel:{TEL}">{PHONE}</a><small>{HOURS}</small></div>
      </aside>

      <div class="ac-main">
        <section class="ac-pane" id="pane-dashboard" data-pane="dashboard">
          <div class="ac-hello"><div><span class="eyebrow">My Account</span><h1>Namaste, <span id="acFirst">Traveller</span></h1>
            <p>Manage your bookings, invoices and saved tours in one place.</p></div>
            <a href="temple-tours.html" class="btn btn-gold">Book a new journey {ic("arrow")}</a></div>
          <div class="ac-stats">
            <div><span>{ic("cal")}</span><b data-stat="bookings">0</b><small>Bookings</small></div>
            <div><span>{ic("map")}</span><b data-stat="upcoming">0</b><small>Upcoming trips</small></div>
            <div><span>{ic("heart")}</span><b data-stat="wishlist">0</b><small>Saved tours</small></div>
          </div>
          <div class="ac-card"><div class="ac-card-h"><h2>Next journey</h2><a href="#bookings" data-go="bookings">All bookings</a></div><div id="acNext"></div></div>
          <div class="ac-card"><div class="ac-card-h"><h2>Saved tours</h2><a href="#wishlist" data-go="wishlist">View wishlist</a></div><div class="ac-mini" id="acMiniWish"></div></div>
        </section>

        <section class="ac-pane" id="pane-bookings" data-pane="bookings" hidden>
          <div class="ac-ph"><h1>My Bookings</h1><p>Every booking you make while logged in appears here, with its invoice.</p></div>
          <div class="ac-filter" role="tablist"><button class="on" data-bf="all">All</button><button data-bf="upcoming">Upcoming</button><button data-bf="past">Past</button></div>
          <div id="acBookings" class="ac-blist"></div>
        </section>

        <section class="ac-pane" id="pane-wishlist" data-pane="wishlist" hidden>
          <div class="ac-ph"><h1>Wishlist</h1><p>Tap the heart on any tour to save it here.</p></div>
          <div id="acWish" class="ac-wgrid"></div>
        </section>

        <section class="ac-pane" id="pane-profile" data-pane="profile" hidden>
          <div class="ac-ph"><h1>Profile</h1><p>These details are used to fill in your bookings and invoices.</p></div>
          <form class="ac-card ac-form" id="acProfile" novalidate>
            <div class="ac-2"><div class="field"><label for="pName">Full name</label><input id="pName" autocomplete="name" required></div>
              <div class="field"><label for="pPhone">Phone</label><input id="pPhone" type="tel" autocomplete="tel"></div></div>
            <div class="ac-2"><div class="field"><label for="pEmail">Email</label><input id="pEmail" type="email" autocomplete="email"></div>
              <div class="field"><label for="pCity">City</label><input id="pCity" autocomplete="address-level2" placeholder="e.g. Hyderabad"></div></div>
            <div class="field"><label for="pNotes">Travel preferences</label><textarea id="pNotes" rows="3" placeholder="Dietary needs, mobility support, preferred hotels…"></textarea></div>
            <div class="ac-form-foot"><button class="btn btn-gold" type="submit">Save changes</button><span class="ac-saved" id="pSaved" role="status"></span></div>
          </form>
          <p class="ac-privacy">{ic("shield")}Your account details and bookings are stored on this device only. To change a confirmed booking, please contact our team.</p>
        </section>
      </div>
    </div>
  </div>
</section>
<script type="application/json" id="acData">{data}</script>"""
    page("account.html", "My Account | Sanchari Travel", "Manage your Sanchari bookings, invoices and saved tours.", "", body)

def credits():
    rows = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{E(c)}</a><span>Wikimedia Commons</span></li>' for c, u in CREDITS)
    body = hero("hero-blog", [("Home", "index.html"), ("Photo credits", None)], "Photo Credits", "Photo credits",
                "Some photos on this site come from Wikimedia Commons and are used under their free licences. Follow each link for the photographer and licence.", cls="page-hero compact no-overlap")
    body += f'''<section class="sec"><div class="wrap"><ul class="credits">{rows}</ul>
      <p class="lead-sm" style="margin-top:24px">Tour photos are Sanchari’s own.</p></div></section>'''
    page("photo-credits.html", "Photo Credits | Sanchari Travel", "Photo credits for images used on the Sanchari website.", "", body)


UPDATED = "29 October 2026"
LEGAL = {
 "privacy-policy.html": ("Privacy Policy", "How Sanchari Travel collects, uses and protects your personal information.", [
  ("Who we are", ["Sanchari Travel is a travel company based in Hyderabad, Telangana, India. This policy explains what personal information we collect when you use this website or book a journey with us, and how we use it."]),
  ("Information we collect", ["Details you give us: your name, phone number, email address, travel dates, number of travellers, budget and any requirements you share in enquiry, booking or newsletter forms.",
                              "Booking details needed to arrange your trip, such as traveller names, ages and ID details where a hotel, permit or yatra registration requires them.",
                              "Basic technical data such as browser type and pages visited, used to keep the site working well."]),
  ("How we use it", ["To answer your enquiries and prepare itineraries and quotes.", "To arrange and confirm bookings with hotels, transport and guides.", "To send booking updates, invoices and, if you subscribe, our newsletter. You can unsubscribe at any time."]),
  ("Sharing", ["We share only what is needed with the hotels, transport operators, guides and registration authorities that deliver your journey. We do not sell your personal information."]),
  ("Storage and security", ["We keep your information only as long as needed for your trip, our accounts and legal requirements, and we take reasonable steps to protect it."]),
  ("Your choices", ["You can ask us to see, correct or delete your personal information, or to stop sending you marketing emails, by writing to us at the email address below."]),
 ]),
 "terms-and-conditions.html": ("Terms & Conditions", "The terms that apply when you book a journey with Sanchari Travel.", [
  ("Bookings", ["A booking is confirmed once we receive the required advance payment and send you a written confirmation.", "Itineraries, prices and inclusions are those shown in your confirmation. Prices on the website are per person and may change until a booking is confirmed."]),
  ("Payments", ["The balance is due before departure on the date given in your confirmation. Prices include GST where stated on your invoice."]),
  ("Changes to your trip", ["We will try to accommodate changes you request, subject to availability and any extra costs from hotels or transport.", "Weather, road closures, temple schedules, permits or government advisories can sometimes force changes. We will offer the closest possible alternative."]),
  ("Health and fitness", ["Some journeys involve high altitude, long walks or treks. Please read the fitness notes for your tour and tell us about any medical needs before booking."]),
  ("Documents", ["Travellers are responsible for carrying valid ID and, for international expeditions, a passport, visas and travel insurance."]),
  ("Liability", ["We work with carefully chosen partners but are not liable for delays, losses or injuries caused by events outside our reasonable control."]),
 ]),
 "cancellation-refund-policy.html": ("Cancellation & Refund Policy", "What happens if you need to cancel a Sanchari journey.", [
  ("Cancelling a booking", ["Please tell us in writing (email or WhatsApp) if you need to cancel. The cancellation date is the day we receive your message."]),
  ("Cancellation charges", ["The exact charges for your journey are stated in your booking confirmation. As a guide:",
                            "More than 30 days before departure: advance amount is refundable, less non-refundable costs already paid to hotels, airlines or permit offices.",
                            "15–30 days before departure: 50% of the tour cost is charged.",
                            "Less than 15 days before departure, or no-show: no refund."]),
  ("If we cancel", ["If we have to cancel a departure, you can choose another date or receive a full refund of the amount paid to us."]),
  ("Refunds", ["Approved refunds are made to the original payment method within 7–10 working days."]),
 ]),
}

def legal_pages():
    for fn, (title, intro, secs) in LEGAL.items():
        body = hero("hero-blog", [("Home", "index.html"), (title, None)], "Policies", E(title), intro, cls="page-hero compact no-overlap")
        toc = "".join(f'<li><a href="#s{i}">{E(h)}</a></li>' for i, (h, _p) in enumerate(secs, 1))
        sec = "".join(f'<section id="s{i}"><h2>{E(h)}</h2>' + "".join(f"<p>{E(p)}</p>" for p in ps) + "</section>" for i, (h, ps) in enumerate(secs, 1))
        others = "".join(f'<li><a href="{f}">{E(t)}</a></li>' for f, (t, _i, _s) in LEGAL.items() if f != fn)
        body += f'''<section class="sec"><div class="wrap legal">
  <aside class="legal-side"><b>On this page</b><ol>{toc}</ol><b>Other policies</b><ul>{others}</ul></aside>
  <article class="legal-body"><p class="legal-upd">Last updated: {UPDATED}</p>{sec}
    <section><h2>Contact us</h2><p>Questions about this policy? Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call <a href="tel:{TEL}">{PHONE}</a> ({HOURS}).</p></section>
  </article></div></section>'''
        page(fn, f"{title} | Sanchari Travel", intro, "", body)

# ------------------------------------------------------------ run
if os.path.exists(OUT): shutil.rmtree(OUT)
for d in ["assets/css", "assets/js", "assets/img"]: os.makedirs(os.path.join(OUT, d))
css = open(os.path.join(HERE, "base.css")).read() + open(os.path.join(HERE, "extra.css")).read()
open(os.path.join(OUT, "assets/css/style.css"), "w").write(css)
shutil.copy(os.path.join(HERE, "site.js"), os.path.join(OUT, "assets/js/site.js"))
for f in ["logo.png", "logo-white.png", "favicon.png", "apple-touch-icon.png"]: shutil.copy(os.path.join(HERE, f), os.path.join(OUT, "assets/img", f))
if os.path.isdir(os.path.join(HERE, "video")): shutil.copytree(os.path.join(HERE, "video"), os.path.join(OUT, "assets/video"))
for k in IM.REG: open(os.path.join(OUT, f"assets/img/{k}.svg"), "w").write(IM.svg_for(k))
home(); about(); contact(); blog(); credits(); invoice(); account(); legal_pages()
for c in CATS: category_page(c)
for t in TOURS: tour_page(t)
print("pages:", len([f for f in os.listdir(OUT) if f.endswith(".html")]), "images:", len(IM.REG))
