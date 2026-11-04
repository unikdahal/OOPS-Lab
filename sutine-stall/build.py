"""Builds the Sutine by Yojana pop-up stall print kit.

Usage:  python3 build.py
Needs:  pip install segno ; Playwright + Chromium (already installed in this env)
Output: print/*.pdf (print-ready, real size) and preview/*.png
Edit EVENT / LINKS below and re-run to update every piece.
"""
import io, pathlib, segno
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
import os, glob
CHROME = next(iter(glob.glob("/opt/pw-browsers/chromium*/chrome-linux*/chrome")), None) if os.path.isdir("/opt/pw-browsers") else None
EVENT = {
    "days": "Friday 6 &amp; Saturday 7 November",
    "venue": "",          # e.g. "Spitalfields Market, Stall 12"  (blank = write-in line)
    "hours": "",          # e.g. "10am – 6pm"
}
LINKS = {
    "instagram": ("https://www.instagram.com/sutine_by_yojana/", "@sutine_by_yojana"),
    "tiktok": ("https://www.tiktok.com/@sutine.by.yojana", "@sutine.by.yojana"),
    "website": ("https://sutine.com/?utm_source=popup&utm_medium=qr&utm_campaign=stall-nov26", "sutine.com"),
}

INK = "#292524"; ROSE = "#D4B0AB"; ROSE_D = "#BD8F89"; CREAM = "#FAF8F6"; BEIGE = "#F1EBE5"
TERRA = "#B5654A"; OLIVE = "#6E7a56"; TAUPE = "#78716C"


def qr(url, color=INK):
    buf = io.BytesIO()
    segno.make(url, error="q").save(buf, kind="svg", scale=10, border=0, dark=color, light=None,
                                    xmldecl=False, svgns=True, nl=False)
    svg = buf.getvalue().decode()
    import re
    w = re.search(r'width="([\d.]+)"', svg).group(1); h = re.search(r'height="([\d.]+)"', svg).group(1)
    svg = re.sub(r'\s(width|height)="[\d.]+"', "", svg, count=2)
    return svg.replace("<svg ", f'<svg class="qr" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid meet" ', 1)


# ---------- hand-drawn style line art (single colour, prints well on linen) ----------
def sprig(flip=False, color=INK):
    leaves = []
    for i, y in enumerate(range(40, 330, 34)):
        side = -1 if i % 2 else 1
        s = 1 - i * 0.055
        lx, ly = 50 + side * 4, y
        tip = (50 + side * 44 * s, y - 30 * s)
        leaves.append(
            f'<path d="M{lx} {ly} Q{lx + side * 30 * s} {ly - 2} {tip[0]} {tip[1]} '
            f'Q{lx + side * 8 * s} {ly - 30 * s} {lx} {ly} Z"/>'
            f'<path d="M{lx} {ly} Q{lx + side * 22 * s} {ly - 10 * s} {tip[0]} {tip[1]}" />')
    t = ' transform="scale(-1,1) translate(-100,0)"' if flip else ""
    return (f'<svg class="sprig" viewBox="0 0 100 360"><g{t} fill="none" stroke="{color}" '
            f'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M50 355 C48 260 54 150 50 18"/>{"".join(leaves)}'
            f'<circle cx="50" cy="12" r="5"/></g></svg>')


def choli(color=INK, accent=TERRA):
    """Chaubandi-choli inspired wrap blouse on a hanger."""
    return f'''<svg class="choli" viewBox="0 0 220 230" fill="none" stroke="{color}" stroke-width="2.6"
 stroke-linecap="round" stroke-linejoin="round">
 <path d="M104 30 c0-12 16-12 16-1 c0 7-8 8-8 15"/>
 <path d="M112 44 L44 66 M112 44 L176 66"/>
 <path d="M70 60 L46 70 L20 128 L40 136 L56 100 L58 196 L162 196 L164 100 L180 136 L200 128 L174 70 L150 60
          Q110 82 70 60 Z" fill="{CREAM}"/>
 <path d="M70 60 L146 168"/>
 <path d="M150 60 L104 128"/>
 <path d="M146 168 q16 10 10 34 M146 168 q-6 16 -20 30"/>
 <circle cx="146" cy="168" r="4.5" fill="{color}"/>
 <path d="M84 130 q4 2 2 8 M90 112 q6 2 4 9" stroke-width="1.6"/>
 <g stroke="{accent}" stroke-width="2.2">
  <path d="M58 184 L162 184"/>
  <path d="M58 184 l8 8 l8 -8 l8 8 l8 -8 l8 8 l8 -8 l8 8 l8 -8 l8 8 l8 -8 l8 8 l8 -8 l8 8"/>
  <path d="M20 128 L40 136 M24 119 L43 127"/>
  <path d="M200 128 L180 136 M196 119 L177 127"/>
 </g>
</svg>'''


def dhaka(color=TERRA):
    """Repeating band inspired by Nepali dhaka weave."""
    return f'''<svg class="dhaka" viewBox="0 0 400 24" preserveAspectRatio="none">
 <defs><pattern id="dk" width="24" height="24" patternUnits="userSpaceOnUse">
  <path d="M12 2 L22 12 L12 22 L2 12 Z M12 7 L17 12 L12 17 L7 12 Z" fill="none" stroke="{color}" stroke-width="1.6"/>
  <circle cx="12" cy="12" r="1.6" fill="{color}"/></pattern></defs>
 <rect width="400" height="24" fill="url(#dk)"/></svg>'''


def wordmark(cls=""):
    return (f'<div class="wm {cls}"><div class="wm-main">SUT<i>ine</i></div>'
            f'<div class="wm-by">by Yojana</div></div>')


CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,500&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: {CREAM}; color: {INK}; font-family: 'Crimson Text', Georgia, serif;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; }}
.wm {{ text-align: center; line-height: .9; }}
.wm-main {{ font-family: 'Playfair Display', serif; font-weight: 400; letter-spacing: .02em; }}
.wm-main i {{ font-style: italic; font-weight: 500; letter-spacing: 0; }}
.wm-by {{ font-family: 'Playfair Display', serif; font-style: italic; color: {ROSE_D}; }}
.caps {{ text-transform: uppercase; letter-spacing: .28em; font-family: 'Crimson Text', serif; font-weight: 600; }}
.rule {{ background: {INK}; height: 1px; }}
.qr {{ display: block; width: 100%; height: 100%; }}
.dhaka {{ display: block; width: 100%; }}
.sprig, .choli {{ display: block; }}
"""


def page(w_mm, h_mm, body, extra_css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
@page {{ size: {w_mm}mm {h_mm}mm; margin: 0; }}
.page {{ width: {w_mm}mm; height: {h_mm}mm; }}
{extra_css}</style></head><body>{body}</body></html>"""


IG, TT, WEB = (LINKS[k] for k in ("instagram", "tiktok", "website"))

# 1. HANGING BANNER 80 x 180 cm  (fabric / linen, hang from frame like the reference)
banner = page(800, 1800, f"""
<div class="page">
  {dhaka()}
  <div class="top">
    {sprig()}{wordmark()}{sprig(True)}
  </div>
  <p class="caps sub">Handcrafted in Nepal</p>
  <div class="art">{choli()}</div>
  <p class="tag">Clothes that are light on your skin<br>and easy on your mind.</p>
  <div class="rule r"></div>
  <div class="social">
    <div class="q">{qr(IG[0])}</div>
    <div><p class="caps">Follow us</p><p class="h">{IG[1]}</p><p class="w">sutine.com</p></div>
  </div>
  <div style="flex:1"></div>
  {dhaka()}
</div>""", """
.dhaka { height: 40mm; }
.top { display: flex; align-items: center; justify-content: center; gap: 18mm; margin-top: 150mm; }
.top .sprig { width: 70mm; height: 300mm; flex-shrink: 0; }
.wm-main { font-size: 165mm; } .wm-by { font-size: 84mm; margin-top: 10mm; }
.sub { font-size: 40mm; margin-top: 70mm; }
.art .choli { width: 420mm; height: 440mm; margin-top: 70mm; }
.tag { font-style: italic; font-size: 52mm; text-align: center; line-height: 1.25; margin-top: 60mm; }
.r { width: 300mm; margin-top: 70mm; height: 2mm; }
.social { display: flex; align-items: center; gap: 40mm; margin-top: 80mm; }
.social .q { width: 190mm; height: 190mm; background: #FAF8F6; }
.social .caps { font-size: 30mm; } .social .h { font-size: 58mm; font-family: 'Playfair Display'; }
.social .w { font-size: 40mm; color: #78716C; }
""")

# 2. TABLE RUNNER 60 x 150 cm — top 60 cm lies on table, bottom 90 cm hangs at front. Art sits on the drop.
runner = page(600, 1500, f"""
<div class="page">
  <div class="ontable"><p class="caps fold">fold line — front edge of table</p></div>
  <div class="drop">
    {dhaka()}
    <div class="row">{sprig()}{wordmark()}{sprig(True)}</div>
    <p class="caps a">Handcrafted in Nepal</p>
    <p class="b">Culture &amp; comfort, made slowly by hand</p>
  </div>
</div>""", """
.ontable { height: 600mm; width: 100%; position: relative; }
.fold { position: absolute; bottom: 4mm; width: 100%; text-align: center; font-size: 6mm; color: #D4B0AB; }
.ontable::after { content: ""; position: absolute; bottom: 0; left: 0; right: 0; border-bottom: .6mm dashed #D4B0AB; }
.drop { width: 100%; display: flex; flex-direction: column; align-items: center; padding-top: 70mm; }
.drop .dhaka { height: 26mm; width: 480mm; }
.row { display: flex; align-items: center; gap: 22mm; margin-top: 90mm; }
.row .sprig { width: 50mm; height: 220mm; flex-shrink: 0; }
.wm-main { font-size: 112mm; } .wm-by { font-size: 56mm; margin-top: 6mm; }
.a { font-size: 24mm; margin-top: 60mm; } .b { font-style: italic; font-size: 30mm; margin-top: 16mm; color: #78716C; }
""")

# 3. FOLLOW US card A5 (148 x 210) — for the wooden block stand
follow = page(148, 210, f"""
<div class="page">
  <h1>Follow<br><span>us</span></h1>
  <div class="big">{qr(IG[0])}</div>
  <p class="h">Instagram · {IG[1]}</p>
  <div class="rule r"></div>
  <div class="pair">
    <div><div class="sm">{qr(TT[0])}</div><p>TikTok<br>{TT[1]}</p></div>
    <div><div class="sm">{qr(WEB[0])}</div><p>Shop online<br>sutine.com</p></div>
  </div>
  <div style="flex:1"></div>{dhaka()}
</div>""", """
.page { padding-top: 13mm; }
h1 { font-family: 'Playfair Display'; font-weight: 600; font-size: 21mm; line-height: .86; align-self: flex-start;
     margin-left: 14mm; text-transform: uppercase; letter-spacing: -.01em; }
h1 span { display: block; text-align: right; margin-right: 0; padding-left: 52mm; font-style: italic; text-transform: none; font-weight: 500; color: #BD8F89; }
.big { width: 62mm; height: 62mm; margin-top: 9mm; }
.h { font-size: 5mm; margin-top: 4mm; }
.r { width: 30mm; margin: 6mm 0 5mm; }
.pair { display: flex; gap: 18mm; text-align: center; }
.sm { width: 28mm; height: 28mm; margin: 0 auto 2.5mm; }
.pair p { font-size: 3.6mm; line-height: 1.25; }
.dhaka { height: 7mm; }
""")

# 4. BRAND STORY card A5
story = page(148, 210, f"""
<div class="page">
  {wordmark()}
  <div class="rule r"></div>
  <p class="lead">Sutíne didn't come from a perfect plan. It came from wanting back the softness —
  that <i>ghar jasto</i> feel.</p>
  <p>As a Nepali woman, Yojana grew up around soft cotton, light fabrics and clothes made for comfort.
  So she stopped searching and started creating.</p>
  <p>Every piece is made slowly, by hand, by a small team of skilled women in Nepal. Simple, but intentional.
  Nothing is rushed.</p>
  <p>Our first collection blends culture and comfort — inspired by the traditional <i>chaubandi choli</i>,
  with a modern touch.</p>
  <div style="flex:1"></div>
  <div class="art">{choli()}</div>
  <p class="caps foot">Handcrafted with love in Nepal</p>
  {dhaka()}
</div>""", """
.page { padding: 16mm 15mm 0; }
.wm-main { font-size: 17mm; } .wm-by { font-size: 8.5mm; margin-top: 1mm; }
.r { width: 24mm; margin: 7mm 0; }
p { font-size: 4.3mm; line-height: 1.45; text-align: center; margin-bottom: 3.2mm; }
.lead { font-size: 5.4mm; font-style: italic; line-height: 1.35; margin-bottom: 5mm; }
.art .choli { width: 30mm; height: 32mm; }
.foot { font-size: 3mm; margin: 3mm 0 7mm; }
.page > .dhaka { height: 6mm; width: 148mm; }
""")

# 5. PRICE CARDS — 4 x A6 on A4, write-in (use chalk pen / fine liner), with clip space at top
def price_card(title, rows):
    lines = "".join(f'<div class="ln"><span>{r}</span><b></b></div>' for r in rows)
    return f'<div class="card"><div class="clip"></div><p class="caps t">{title}</p>{lines}' \
           f'<p class="ft">SUT<i>ine</i> · by Yojana</p></div>'


prices = page(210, 297, f"""
<div class="page grid">
  {price_card("Price list", ["Lali Set", "Choli top", "Trousers", "Scarf", "", ""])}
  {price_card("Pop-up offer", ["", "", "", ""])}
  {price_card("Sizing", ["Relaxed, artisanal fit", "Between sizes? Size up", "Try-on welcome", "Just ask us ♡"])}
  {price_card("We accept", ["Card &amp; contactless", "Cash", "", ""])}
</div>""", """
.grid { display: grid; grid-template-columns: 105mm 105mm; grid-template-rows: 148.5mm 148.5mm; }
.card { border: .2mm dashed #D4B0AB; padding: 14mm 11mm 8mm; display: flex; flex-direction: column; }
.clip { height: 6mm; }
.t { font-size: 5mm; text-align: center; margin-bottom: 8mm; letter-spacing: .3em; }
.ln { display: flex; align-items: flex-end; gap: 3mm; height: 11mm; font-size: 5mm; }
.ln span { white-space: nowrap; } .ln b { flex: 1; border-bottom: .3mm solid #292524; height: 1px; margin-bottom: 1.6mm; }
.ft { margin-top: auto; text-align: center; font-family: 'Playfair Display'; font-size: 4mm; color: #BD8F89; }
""")

# 6. BUSINESS / THANK-YOU CARDS 85 x 55, 10-up on A4 (put one in every bag)
card = f"""<div class="bc"><div class="l">{wordmark()}<p class="caps">Handcrafted in Nepal</p>
<p class="s">{IG[1]}<br>sutine.com</p></div><div class="r"><div class="q">{qr(WEB[0])}</div>
<p>Thank you ♡<br>shop &amp; follow</p></div></div>"""
cards = page(210, 297, f'<div class="page sheet">{card * 10}</div>', """
.sheet { display: grid; grid-template-columns: 85mm 85mm; grid-auto-rows: 55mm; gap: 0; padding: 11mm 20mm; align-content: start; justify-content: center; }
.bc { border: .15mm dashed #D4B0AB; display: flex; align-items: center; padding: 5mm 6mm; gap: 4mm; }
.bc .l { flex: 1; text-align: center; } .wm-main { font-size: 9.5mm; } .wm-by { font-size: 4.6mm; }
.bc .caps { font-size: 1.9mm; margin-top: 2.5mm; } .bc .s { font-size: 2.8mm; margin-top: 2mm; color: #78716C; line-height: 1.3; }
.bc .r { width: 25mm; text-align: center; } .bc .q { width: 22mm; height: 22mm; margin: 0 auto 1.5mm; }
.bc .r p { font-size: 2.6mm; line-height: 1.2; font-style: italic; }
""")

# 7. THIS WEEKEND poster A4 (for socials / shop window / venue board)
venue = EVENT["venue"] or '<span class="blank"></span>'
hours = EVENT["hours"] or '<span class="blank short"></span>'
poster = page(210, 297, f"""
<div class="page">
  {dhaka()}
  <p class="caps k">Pop-up stall</p>
  {wordmark()}
  <div class="art">{choli()}</div>
  <p class="caps k2">Find us this weekend</p>
  <p class="d">{EVENT['days']}</p>
  <p class="v">{venue}</p>
  <p class="v hrs">{hours}</p>
  <div style="flex:1"></div>
  <div class="foot"><div class="q">{qr(IG[0])}</div><p>Follow along<br><b>{IG[1]}</b></p></div>
  {dhaka()}
</div>""", """
.dhaka { height: 9mm; }
.k { font-size: 4.2mm; margin: 16mm 0 6mm; }
.wm-main { font-size: 30mm; } .wm-by { font-size: 14mm; margin-top: 1.5mm; }
.art .choli { width: 62mm; height: 65mm; margin-top: 8mm; }
.k2 { font-size: 4.2mm; margin-top: 8mm; color: #BD8F89; }
.d { font-family: 'Playfair Display'; font-size: 10.5mm; margin-top: 3mm; text-align: center; }
.v { font-size: 6.5mm; margin-top: 3mm; font-style: italic; min-height: 8mm; }
.blank { display: inline-block; width: 110mm; border-bottom: .3mm solid #292524; height: 7mm; }
.blank.short { width: 55mm; }
.foot { display: flex; align-items: center; gap: 6mm; margin-bottom: 10mm; }
.foot .q { width: 26mm; height: 26mm; } .foot p { font-size: 4.6mm; line-height: 1.3; }
""")


PIECES = {
    "01-hanging-banner-80x180cm": (banner, 800, 1800),
    "02-table-runner-60x150cm": (runner, 600, 1500),
    "03-follow-us-card-A5": (follow, 148, 210),
    "04-brand-story-card-A5": (story, 148, 210),
    "05-price-cards-4xA6-on-A4": (prices, 210, 297),
    "06-thankyou-cards-10up-A4": (cards, 210, 297),
    "07-this-weekend-poster-A4": (poster, 210, 297),
}

if __name__ == "__main__":
    for d in ("html", "print", "preview", "qr"):
        (ROOT / d).mkdir(exist_ok=True)
    for key, (url, _) in LINKS.items():
        segno.make(url, error="q").save(ROOT / "qr" / f"{key}.svg", scale=10, border=2, dark=INK)
        segno.make(url, error="q").save(ROOT / "qr" / f"{key}.png", scale=30, border=2, dark=INK)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
        for name, (html, w, h) in PIECES.items():
            f = ROOT / "html" / f"{name}.html"
            f.write_text(html)
            pg = b.new_page()
            pg.goto(f.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
            pg.pdf(path=str(ROOT / "print" / f"{name}.pdf"), width=f"{w}mm", height=f"{h}mm", print_background=True)
            pg.set_viewport_size({"width": int(w * 3.7795) + 1, "height": int(h * 3.7795) + 1})
            pg.screenshot(path=str(ROOT / "preview" / f"{name}.png"), full_page=False, scale="css")
            pg.close()
        b.close()
    from PIL import Image
    for png in (ROOT / "preview").glob("*.png"):
        im = Image.open(png); im.thumbnail((1400, 1400)); im.save(png)
    print("done")
