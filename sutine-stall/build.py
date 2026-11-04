"""Sutine by Yojana: pop-up stall print kit (final).

Design idea: every piece is "dressed" like the clothes. It has a cream cotton ground,
a solid maroon or olive hem band (from the Lali skirt), and stitched Phulbari flower
appliques (from the patchwork skirt). No prices are printed anywhere.

Run:   pip install segno playwright pillow && python3 build.py
Out:   print/   print-ready PDFs at real size  (send these to the printer)
       digital/ PNGs for Instagram
       preview/ small PNG previews
Edit EVENT below to add the venue and hours, then run it again.
"""
import io, re, glob, pathlib, shutil, segno
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
CHROME = next(iter(glob.glob("/opt/pw-browsers/chromium*/chrome-linux*/chrome")), None)

EVENT = {
    "days": "Friday 6 &amp; Saturday 7 November",
    "venue": "",   # e.g. "Spitalfields Market · Stall 12"   (left blank = line is hidden)
    "hours": "",   # e.g. "10am – 6pm"
}
UTM = "utm_source=popup&utm_medium=qr&utm_campaign=stall-nov26"
IG = ("https://www.instagram.com/sutine_by_yojana/", "@sutine_by_yojana")
TT = ("https://www.tiktok.com/@sutine.by.yojana", "@sutine.by.yojana")
WEB = (f"https://sutine.com/?{UTM}", "sutine.com")

# palette: taken from sutine.com + the garments themselves
CREAM = "#F7F3EC"; PAPER = "#FBF8F3"; INK = "#2A2523"; TAUPE = "#7A716B"
MAROON = "#7A1F26"; OLIVE = "#5F6B3A"; ROSE = "#C99C95"; SAND = "#EDE5DA"

PRODUCTS = [  # id on sutine.com, display name, small line (from the product descriptions)
    (2, "Gunyo", "Traditional wrap top"), (7, "Rekha Top", "Striped sleeveless top"),
    (9, "Shanti", "Subtle mandala print"), (5, "Gurash", "Light &amp; softly structured"),
    (3, "Lali Skirt", "Soft, flowy, bordered hem"), (1, "Phulbari", "Hand-pieced patchwork skirt"),
    (6, "Sital Skirt", "Everyday cotton skirt"), (4, "Judi", "White cotton pants · petite"),
    (8, "Rekha Pants", "Relaxed cotton · petite"), (10, "Everyday Tote", "Made for every day"),
    (11, "Suti Thaili", "A modern Nepali thaili"),
]


# ------------------------------------------------------------------ motifs
def qr(url, color=INK):
    buf = io.BytesIO()
    segno.make(url, error="q").save(buf, kind="svg", scale=10, border=0, dark=color, light=None,
                                    xmldecl=False, svgns=True, nl=False)
    s = buf.getvalue().decode()
    w = re.search(r'width="([\d.]+)"', s).group(1); h = re.search(r'height="([\d.]+)"', s).group(1)
    s = re.sub(r'\s(width|height)="[\d.]+"', "", s, count=2)
    return s.replace("<svg ", f'<svg class="qr" viewBox="0 0 {w} {h}" ', 1)


def phul(color, stitch=CREAM, petals=7):
    """Phulbari flower: slim rounded petals, open centre and a running-stitch outline like applique."""
    g = []
    for k in range(petals):
        a = k * 360 / petals
        g.append(f'<g transform="rotate({a:.1f})">'
                 f'<path d="M0 -14 C-9 -20 -10 -44 0 -50 C10 -44 9 -20 0 -14 Z" fill="{color}"/>'
                 f'<path d="M0 -18 C-6 -23 -6.5 -41 0 -45.5 C6.5 -41 6 -23 0 -18 Z" fill="none" '
                 f'stroke="{stitch}" stroke-width="1.1" stroke-dasharray="2.6 2.2" opacity=".85"/></g>')
    g.append(f'<circle r="9.5" fill="{stitch}"/><circle r="9.5" fill="none" stroke="{color}" '
             f'stroke-width="1.2" stroke-dasharray="2.4 2"/>')
    return "".join(g)


def leaf(color, stitch=CREAM):
    return (f'<path d="M0 0 C14 -13 36 -13 52 0 C36 13 14 13 0 0 Z" fill="{color}"/>'
            f'<path d="M6 0 L46 0" stroke="{stitch}" stroke-width="1.1" stroke-dasharray="2.6 2.2"/>')


def garden(vb, items, cls="garden"):
    """items: (kind, x, y, scale, rotate, color)"""
    out = []
    for kind, x, y, s, r, c in items:
        body = phul(c) if kind == "f" else leaf(c)
        out.append(f'<g transform="translate({x} {y}) rotate({r}) scale({s})">{body}</g>')
    return f'<svg class="{cls}" viewBox="{vb}" preserveAspectRatio="xMidYMid meet">{"".join(out)}</svg>'


def choli(color=INK):
    """Line drawing of a chaubandi-choli-style wrap top on a hanger, with hem detail."""
    return f'''<svg class="choli" viewBox="0 0 220 220" fill="none" stroke="{color}" stroke-width="2.2"
 stroke-linecap="round" stroke-linejoin="round">
 <path d="M104 26 c0-12 16-12 16-1 c0 7-8 8-8 15"/>
 <path d="M112 40 L48 60 M112 40 L176 60"/>
 <path d="M72 56 L48 66 L24 120 L42 128 L58 94 L60 186 L164 186 L166 94 L182 128 L200 120 L176 66 L152 56
          Q112 78 72 56 Z" fill="{PAPER}"/>
 <path d="M72 56 L148 162"/><path d="M152 56 L106 124"/>
 <g stroke="{MAROON}"><path d="M148 162 q15 10 9 32 M148 162 q-6 15 -19 28"/></g>
 <circle cx="148" cy="162" r="4" fill="{MAROON}" stroke="{MAROON}"/>
 <path d="M60 174 L164 174" stroke="{OLIVE}" stroke-width="5"/>
 <path d="M24 120 L42 128" stroke="{OLIVE}" stroke-width="5"/><path d="M200 120 L182 128" stroke="{OLIVE}" stroke-width="5"/>
 <path d="M64 168 L160 168 M66 180 L158 180" stroke="{PAPER}" stroke-width=".9" stroke-dasharray="2.4 2"/>
</svg>'''


def wordmark(by=True):
    b = '<div class="wm-by">by Yojana</div>' if by else ""
    return f'<div class="wm"><div class="wm-main">SUT<i>ine</i></div>{b}</div>'


CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Karla:wght@400;500&display=swap');
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: {CREAM}; color: {INK}; font-family: 'Cormorant Garamond', Georgia, serif;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; background: {CREAM}; }}
.wm {{ text-align: center; line-height: .88; }}
.wm-main {{ font-family: 'Playfair Display', serif; font-weight: 400; letter-spacing: .015em; }}
.wm-main i {{ font-style: italic; font-weight: 400; letter-spacing: 0; }}
.wm-by {{ font-family: 'Playfair Display', serif; font-style: italic; color: {MAROON}; }}
.caps {{ font-family: 'Karla', sans-serif; text-transform: uppercase; letter-spacing: .32em; font-weight: 500; }}
.it {{ font-style: italic; }}
.qr {{ display: block; width: 100%; height: 100%; }}
.garden, .choli {{ display: block; }}
.hem {{ position: absolute; left: 0; right: 0; bottom: 0; background: {MAROON}; color: {CREAM};
  display: flex; align-items: center; justify-content: center; }}
.hem.olive {{ background: {OLIVE}; }}
.hem::before {{ content: ""; position: absolute; left: 0; right: 0; border-top: 1px dashed {CREAM}; opacity: .7; }}
.trim {{ position: absolute; left: 0; right: 0; background: {OLIVE}; }}
.page.sheet, .page.tsheet, .page.ssheet {{ align-items: stretch; justify-items: stretch; }}
"""


def page(w, h, body, css=""):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}'
            f'@page {{ size: {w}mm {h}mm; margin: 0; }} .page {{ width: {w}mm; height: {h}mm; }}{css}'
            f'</style></head><body>{body}</body></html>')


PX = 25.4 / 96  # 1 css px in mm, for the digital pieces

# ================================================================== BIG (fabric)
# A1 · Hanging banner 80 x 180 cm
A1 = page(800, 1800, f"""
<div class="page">
  <p class="caps top">Handcrafted in Nepal</p>
  {garden("-160 -60 320 120", [("l",-95,10,1,200,OLIVE),("f",-55,0,.62,10,MAROON),("f",0,-6,.9,0,OLIVE),
                               ("f",55,0,.62,-12,MAROON),("l",95,10,1,-20,OLIVE)], "crown")}
  {wordmark()}
  <div class="art">{choli()}</div>
  <p class="it tag">Clothes that are light on your skin<br>and easy on your mind.</p>
  <div class="social"><div class="q">{qr(IG[0])}</div>
    <div><p class="caps f">Follow along</p><p class="h">{IG[1]}</p></div></div>
  {garden("0 0 800 300", [("l",40,230,2.2,-40,OLIVE),("f",150,170,2.0,8,MAROON),("f",330,232,1.15,25,OLIVE),
                          ("l",420,250,1.6,-150,MAROON),("f",590,150,1.7,-10,OLIVE),("f",730,248,1.0,15,MAROON),
                          ("l",470,170,1.3,-60,OLIVE)], "bed")}
  <div class="trim" style="bottom:178mm;height:14mm"></div>
  <div class="hem" style="height:170mm"><p class="caps url">sutine.com</p></div>
</div>""", """
.top { font-size: 26mm; margin-top: 120mm; color: #7A1F26; }
.crown { width: 380mm; height: 140mm; margin-top: 55mm; }
.wm { margin-top: 20mm; } .wm-main { font-size: 168mm; } .wm-by { font-size: 82mm; margin-top: 8mm; }
.art .choli { width: 330mm; height: 330mm; margin-top: 70mm; }
.tag { font-size: 54mm; text-align: center; line-height: 1.22; margin-top: 45mm; }
.social { display: flex; align-items: center; gap: 30mm; margin-top: 60mm; }
.social .q { width: 150mm; height: 150mm; }
.social .f { font-size: 20mm; color: #7A716B; } .social .h { font-family: 'Playfair Display'; font-size: 46mm; margin-top: 6mm; }
.bed { position: absolute; left: 0; bottom: 150mm; width: 800mm; height: 300mm; }
.url { font-size: 40mm; letter-spacing: .5em; position: relative; }
.hem::before { top: 14mm; border-top: 1.6mm dashed #F7F3EC; }
""")

# A2 · Table-front / tent header banner 150 x 50 cm (landscape)
A2 = page(1500, 500, f"""
<div class="page row">
  {garden("0 0 340 420", [("l",60,330,1.8,-60,OLIVE),("f",120,220,1.85,10,MAROON),("f",255,330,1.05,20,OLIVE),
                          ("l",280,150,1.2,-110,OLIVE),("f",250,95,.7,0,MAROON)], "gl")}
  <div class="mid">{wordmark()}<p class="caps sub">Handcrafted in Nepal &nbsp;·&nbsp; 100% cotton</p></div>
  {garden("0 0 340 420", [("l",280,330,1.8,-120,OLIVE),("f",220,220,1.85,-10,OLIVE),("f",85,330,1.05,-20,MAROON),
                          ("l",60,150,1.2,-70,OLIVE),("f",90,95,.7,0,MAROON)], "gr")}
  <div class="trim" style="bottom:66mm;height:6mm"></div>
  <div class="hem" style="height:62mm"><p class="caps h">{IG[1]} &nbsp;·&nbsp; sutine.com</p></div>
</div>""", """
.row { flex-direction: row; align-items: flex-start; justify-content: space-between; }
.gl, .gr { width: 340mm; height: 420mm; margin-top: 0; }
.mid { display: flex; flex-direction: column; align-items: center; margin-top: 70mm; }
.wm-main { font-size: 150mm; } .wm-by { font-size: 72mm; margin-top: 6mm; }
.sub { font-size: 18mm; margin-top: 32mm; color: #7A1F26; }
.h { font-size: 20mm; letter-spacing: .3em; text-transform: none; position: relative; }
.hem::before { top: 7mm; border-top: 1mm dashed #F7F3EC; }
""")

# A3 · Table runner 50 x 140 cm: back 60 cm lies on the table, front 80 cm hangs down
A3 = page(500, 1400, f"""
<div class="page">
  <div class="hem olive" style="top:0;bottom:auto;height:40mm"></div>
  <div style="height:640mm"></div>
  {wordmark()}
  <p class="caps sub">Handcrafted in Nepal</p>
  {garden("0 0 500 300", [("l",50,240,1.7,-40,OLIVE),("f",140,170,1.55,8,MAROON),("f",290,235,1.0,25,OLIVE),
                          ("l",350,120,1.2,-100,MAROON),("f",420,170,1.25,-12,OLIVE)], "bed")}
  <div class="trim" style="bottom:108mm;height:8mm"></div>
  <div class="hem" style="height:100mm"></div>
</div>""", """
.wm-main { font-size: 105mm; } .wm-by { font-size: 52mm; margin-top: 5mm; }
.sub { font-size: 15mm; margin-top: 40mm; color: #7A1F26; }
.bed { position: absolute; left: 0; bottom: 92mm; width: 500mm; height: 300mm; }
.hem::before { top: 9mm; border-top: 1mm dashed #F7F3EC; }
""")

# ================================================================== SMALL (card)
SMALL_HEM = '<div class="trim" style="bottom:9mm;height:1.4mm"></div><div class="hem" style="height:7.5mm"></div>'

# B1 · Follow us card A5
B1 = page(148, 210, f"""
<div class="page">
  {garden("-60 -60 120 120", [("f",0,0,1,0,MAROON)], "fl")}
  <h1>Follow <i>along</i></h1>
  <p class="it lede">New pieces, behind the seams &amp; stories from Nepal</p>
  <div class="big">{qr(IG[0])}</div>
  <p class="caps lab">Instagram</p><p class="h">{IG[1]}</p>
  <div class="pair">
    <div><div class="sm">{qr(TT[0])}</div><p class="caps lab">TikTok</p><p class="s">{TT[1]}</p></div>
    <div><div class="sm">{qr(WEB[0])}</div><p class="caps lab">Shop online</p><p class="s">sutine.com</p></div>
  </div>
  {SMALL_HEM}
</div>""", """
.fl { position: absolute; top: -12mm; right: -12mm; width: 44mm; height: 44mm; }
h1 { font-family: 'Playfair Display'; font-weight: 400; font-size: 15mm; margin-top: 17mm; }
h1 i { color: #7A1F26; }
.lede { font-size: 4.6mm; color: #7A716B; margin-top: 1mm; }
.big { width: 56mm; height: 56mm; margin-top: 8mm; }
.lab { font-size: 2.4mm; color: #7A716B; margin-top: 3.5mm; }
.h { font-family: 'Playfair Display'; font-size: 5.4mm; margin-top: 1mm; }
.pair { display: flex; gap: 22mm; margin-top: 9mm; text-align: center; }
.sm { width: 23mm; height: 23mm; margin: 0 auto; } .pair .s { font-size: 3.8mm; margin-top: .6mm; }
""")

# B2 · Our story card A5
B2 = page(148, 210, f"""
<div class="page">
  {garden("-150 -55 300 110", [("l",-90,8,.8,200,OLIVE),("f",-45,0,.5,10,MAROON),("f",0,-4,.7,0,OLIVE),
                               ("f",45,0,.5,-12,MAROON),("l",90,8,.8,-20,OLIVE)], "crown")}
  {wordmark()}
  <p class="caps k">Our story</p>
  <p class="lead it">“I wanted to bring back that softness, that <span>ghar jasto</span> feel.”</p>
  <p>As a Nepali woman, Yojana grew up around soft cotton, light fabrics and clothes made for comfort.
  So she stopped searching and started creating.</p>
  <p>Every piece is made slowly, by hand, by a small team of skilled women in Nepal.
  Simple, but intentional. Nothing is rushed.</p>
  <p>Our first collection blends culture and comfort, inspired by the traditional <i>chaubandi choli</i>
  with a quiet, modern touch.</p>
  <p class="sig it">With love, Yojana</p>
  {SMALL_HEM}
</div>""", """
.page { padding: 0 16mm; }
.crown { width: 64mm; height: 24mm; margin-top: 13mm; }
.wm { margin-top: 3mm; } .wm-main { font-size: 15mm; } .wm-by { font-size: 7.4mm; margin-top: 1mm; }
.k { font-size: 2.6mm; color: #7A1F26; margin: 8mm 0 5mm; }
p { font-size: 4.5mm; line-height: 1.42; text-align: center; margin-bottom: 3.2mm; }
.lead { font-family: 'Playfair Display'; font-size: 5.6mm; line-height: 1.32; margin-bottom: 5mm; }
.lead span { color: #7A1F26; }
.sig { font-family: 'Playfair Display'; font-size: 5.4mm; color: #7A1F26; margin-top: 3mm; }
""")

# B3 · Four small table signs A6 (on one A4 sheet)
def sign(kicker, title, line, flower_color):
    return (f'<div class="sg">{garden("-60 -60 120 120", [("f",0,0,1,0,flower_color)], "sf")}'
            f'<p class="caps kk">{kicker}</p><p class="tt">{title}</p><p class="it ll">{line}</p>'
            f'<div class="tr"></div><div class="hm"></div></div>')
B3 = page(210, 297, '<div class="page sheet">' + "".join([
    sign("Please", "Try&nbsp;it <i>on</i>", "Our mirror &amp; changing corner are all yours.", MAROON),
    sign("The fabric", "100% <i>suti</i>", "Soft, breathable cotton, made to be lived in.", OLIVE),
    sign("Made by hand", "Handcrafted <i>in Nepal</i>", "Each piece is made slowly, with love and patience.", OLIVE),
    sign("Easy checkout", "Card &amp; <i>cash</i>", "Contactless welcome. Shop anytime at sutine.com", MAROON),
]) + "</div>", """
.sheet { display: grid; grid-template-columns: 105mm 105mm; grid-template-rows: 148.5mm 148.5mm; }
.sg { position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center;
      text-align: center; padding: 0 12mm 10mm; outline: .15mm dashed #C99C95; }
.sf { width: 30mm; height: 30mm; margin-bottom: 8mm; }
.kk { font-size: 2.6mm; color: #7A716B; } .tt { font-family: 'Playfair Display'; font-size: 11mm; line-height: 1.05; margin-top: 3mm; }
.tt i { color: #7A1F26; } .ll { font-size: 4.6mm; margin-top: 5mm; line-height: 1.35; color: #4a4340; }
.tr { position: absolute; left: 0; right: 0; bottom: 8mm; height: 1.2mm; background: #5F6B3A; }
.hm { position: absolute; left: 0; right: 0; bottom: 0; height: 6.5mm; background: #7A1F26; }
""")

# B4 · Hang tags 50 x 90 mm, 12 per A4 (no prices; the QR opens the product page)
def tag(pid=None, name="", line=""):
    q = (f'<div class="q">{qr(f"https://sutine.com/product/{pid}?{UTM}")}</div>'
         f'<p class="sc">scan for sizes &amp; details</p>') if pid else '<div class="q"></div><p class="sc">&nbsp;</p>'
    return (f'<div class="tg"><div class="hole"></div>{wordmark(False)}<div class="rl"></div>'
            f'<p class="n">{name or "&nbsp;"}</p><p class="d it">{line or "&nbsp;"}</p>{q}'
            f'<p class="caps m">100% cotton · Nepal</p><div class="hm"></div></div>')
B4 = page(210, 297, '<div class="page tsheet">' + "".join(tag(*p) for p in PRODUCTS) + tag() + "</div>", """
.tsheet { display: grid; grid-template-columns: repeat(4, 50mm); grid-template-rows: repeat(3, 90mm);
          justify-content: center; align-content: center; height: 297mm; }
.tg { position: relative; overflow: hidden; display: flex; flex-direction: column; align-items: center; padding: 4mm 4mm 0; outline: .15mm dashed #C99C95; }
.hole { width: 4.5mm; height: 4.5mm; border: .3mm solid #7A716B; border-radius: 50%; }
.tg .wm { margin-top: 5mm; } .tg .wm-main { font-size: 8.4mm; }
.rl { width: 8mm; height: .3mm; background: #7A1F26; margin: 4mm 0; }
.n { font-family: 'Playfair Display'; font-size: 5.4mm; text-align: center; line-height: 1.1; }
.d { font-size: 3.4mm; color: #7A716B; text-align: center; margin-top: 1mm; }
.q { width: 20mm; height: 20mm; margin-top: 6mm; } .sc { font-size: 2.6mm; font-style: italic; margin-top: 1.2mm; }
.m { font-size: 1.9mm; position: absolute; bottom: 8mm; }
.hm { position: absolute; left: 0; right: 0; bottom: 0; height: 5mm; background: #7A1F26; }
""")

# B5 · Thank-you cards 85 x 55 mm, 10 per A4
card = f"""<div class="bc"><div class="l">{garden("-60 -60 120 120", [("f",0,0,1,0,CREAM)], "cf")}
<p class="caps">Thank you</p></div><div class="r">{wordmark()}<p class="it t">Thank you for choosing slow,<br>handmade clothing.</p>
<div class="b"><div class="q">{qr(IG[0])}</div><p>Tag us in your look<br><b>{IG[1]}</b></p></div></div></div>"""
B5 = page(210, 297, f'<div class="page sheet">{card * 10}</div>', f"""
.sheet {{ display: grid; grid-template-columns: 85mm 85mm; grid-auto-rows: 55mm; padding: 11mm 20mm; align-content: start; justify-content: center; }}
.bc {{ display: flex; outline: .15mm dashed {ROSE}; overflow: hidden; }}
.l {{ width: 26mm; background: {MAROON}; color: {CREAM}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4mm; }}
.l .cf {{ width: 15mm; height: 15mm; }} .l .caps {{ font-size: 1.9mm; letter-spacing: .25em; }}
.r {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 3mm; }}
.r .wm-main {{ font-size: 7.6mm; }} .r .wm-by {{ font-size: 3.6mm; }}
.t {{ font-size: 3.2mm; text-align: center; line-height: 1.25; margin-top: 2.2mm; }}
.b {{ display: flex; align-items: center; gap: 2.5mm; margin-top: 2.6mm; }}
.b .q {{ width: 12mm; height: 12mm; }} .b p {{ font-size: 2.5mm; line-height: 1.3; }}
""")

# B6 · Round stickers 50 mm, 15 per A4 (seal tissue paper / bags)
def sticker(i, bg, fg, fl):
    return f"""<div class="st" style="background:{bg};color:{fg}"><svg viewBox="0 0 100 100" class="arc">
<defs><path id="c{i}" d="M50 50 m-38 0 a38 38 0 1 1 76 0 a38 38 0 1 1 -76 0"/></defs>
<text font-family="Karla" font-size="6.4" letter-spacing="2.6" fill="{fg}" font-weight="500">
<textPath href="#c{i}" startOffset="2%">HANDCRAFTED IN NEPAL · 100% COTTON ·</textPath></text></svg>
<div class="in">{garden("-60 -60 120 120", [("f",0,0,1,0,fl)], "sf")}<div class="wm-main">SUT<i>ine</i></div></div></div>"""
B6 = page(210, 297, '<div class="page ssheet">' +
          "".join(sticker(i, *((CREAM, MAROON, OLIVE) if i % 2 else (MAROON, CREAM, CREAM))) for i in range(15)) + "</div>", """
.ssheet { display: grid; grid-template-columns: repeat(3, 50mm); grid-auto-rows: 50mm; gap: 6mm 12mm; justify-content: center; align-content: center; height: 297mm; }
.st { position: relative; border-radius: 50%; outline: .15mm dashed #C99C95; }
.arc { position: absolute; inset: 0; width: 100%; height: 100%; }
.in { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.st .sf { width: 11mm; height: 11mm; margin-bottom: 1.5mm; } .st .wm-main { font-size: 7.4mm; }
""")

# ================================================================== EVENT poster + digital
def event_body():
    v = f'<p class="v">{EVENT["venue"]}</p>' if EVENT["venue"] else ""
    h = f'<p class="v">{EVENT["hours"]}</p>' if EVENT["hours"] else ""
    return f"""<div class="page">
  {garden("-160 -60 320 120", [("l",-95,10,1,200,OLIVE),("f",-55,0,.62,10,MAROON),("f",0,-6,.9,0,OLIVE),
                               ("f",55,0,.62,-12,MAROON),("l",95,10,1,-20,OLIVE)], "crown")}
  <p class="caps k">Pop-up stall</p>
  {wordmark()}
  <div class="art">{choli()}</div>
  <p class="caps k2">Come say hello</p>
  <p class="d">{EVENT['days']}</p>{v}{h}
  <p class="it x">Try on the first collection, handcrafted in Nepal</p>
  <div style="flex:1"></div>
  <p class="caps hd">{IG[1]}</p>
  {garden("0 0 800 300", [("l",40,230,2.2,-40,OLIVE),("f",150,170,2.0,8,MAROON),("f",330,232,1.15,25,OLIVE),
                          ("l",420,250,1.6,-150,MAROON),("f",590,150,1.7,-10,OLIVE),("f",730,248,1.0,15,MAROON),
                          ("l",470,170,1.3,-60,OLIVE)], "bed")}
  <div class="trim" style="bottom:calc(var(--u)*11);height:calc(var(--u)*1.4)"></div>
  <div class="hem" style="height:calc(var(--u)*9.5)"></div>
</div>"""
EV_CSS = """
.page { --u: VAR; }
.crown { width: calc(var(--u)*80); height: calc(var(--u)*30); margin-top: calc(var(--u)*14); }
.k { font-size: calc(var(--u)*3.6); margin-top: calc(var(--u)*5); color: #7A1F26; }
.wm { margin-top: calc(var(--u)*5); } .wm-main { font-size: calc(var(--u)*28); } .wm-by { font-size: calc(var(--u)*13.5); margin-top: calc(var(--u)*1.5); }
.art .choli { width: calc(var(--u)*56); height: calc(var(--u)*56); margin-top: calc(var(--u)*8); }
.k2 { font-size: calc(var(--u)*3.6); margin-top: calc(var(--u)*6); color: #7A716B; }
.d { font-family: 'Playfair Display'; font-size: calc(var(--u)*10); margin-top: calc(var(--u)*3); text-align: center; }
.v { font-size: calc(var(--u)*6.5); margin-top: calc(var(--u)*1.5); }
.x { font-size: calc(var(--u)*5.4); margin-top: calc(var(--u)*5); color: #4a4340; }
.hd { font-size: calc(var(--u)*3.6); letter-spacing: .2em; text-transform: none; margin-bottom: calc(var(--u)*62); }
.bed { position: absolute; left: 0; width: 100%; bottom: calc(var(--u)*8); height: calc(var(--u)*79); }
.hem::before { top: calc(var(--u)*1.6); }
"""
C1 = page(210, 297, event_body(), EV_CSS.replace("VAR", "1mm"))                       # A4 poster
C2 = page(1080 * PX, 1350 * PX, event_body(), EV_CSS.replace("VAR", "1.24mm") +        # IG post 4:5
          ".crown{margin-top:calc(var(--u)*9)} .art .choli{width:calc(var(--u)*44);height:calc(var(--u)*44)}")
C3 = page(1080 * PX, 1920 * PX, event_body(), EV_CSS.replace("VAR", "1.36mm") +        # IG story 9:16
          ".crown{margin-top:calc(var(--u)*40)} .art .choli{width:calc(var(--u)*70);height:calc(var(--u)*70)} .hd{margin-bottom:calc(var(--u)*90)}")

PRINT = {
    "A1-hanging-banner-80x180cm": (A1, 800, 1800),
    "A2-table-front-banner-150x50cm": (A2, 1500, 500),
    "A3-table-runner-50x140cm": (A3, 500, 1400),
    "B1-follow-us-card-A5": (B1, 148, 210),
    "B2-our-story-card-A5": (B2, 148, 210),
    "B3-table-signs-4xA6-on-A4": (B3, 210, 297),
    "B4-hang-tags-12up-A4": (B4, 210, 297),
    "B5-thank-you-cards-10up-A4": (B5, 210, 297),
    "B6-stickers-50mm-15up-A4": (B6, 210, 297),
    "C1-weekend-poster-A4": (C1, 210, 297),
}
DIGITAL = {"C2-instagram-post-1080x1350": (C2, 1080, 1350), "C3-instagram-story-1080x1920": (C3, 1080, 1920)}


def render():
    for d in ("html", "print", "preview", "digital", "qr"):
        shutil.rmtree(ROOT / d, ignore_errors=True); (ROOT / d).mkdir()
    for key, (url, _) in {"instagram": IG, "tiktok": TT, "website": WEB}.items():
        segno.make(url, error="q").save(ROOT / "qr" / f"{key}.svg", scale=10, border=2, dark=INK)
        segno.make(url, error="q").save(ROOT / "qr" / f"{key}.png", scale=30, border=2, dark=INK)
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
        for name, (html, w, h) in {**PRINT, **DIGITAL}.items():
            f = ROOT / "html" / f"{name}.html"; f.write_text(html)
            digital = name in DIGITAL
            vw, vh = (w, h) if digital else (round(w / PX), round(h / PX))
            pg = b.new_page(viewport={"width": vw, "height": vh})
            pg.goto(f.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
            if digital:
                pg.screenshot(path=str(ROOT / "digital" / f"{name}.png"))
            else:
                pg.pdf(path=str(ROOT / "print" / f"{name}.pdf"), width=f"{w}mm", height=f"{h}mm", print_background=True)
            pg.screenshot(path=str(ROOT / "preview" / f"{name}.png"))
            pg.close()
        b.close()
    for png in (ROOT / "preview").glob("*.png"):
        im = Image.open(png); im.thumbnail((1400, 1400)); im.save(png)


if __name__ == "__main__":
    render()
    print("done")


# ================================================================== PRINT GUIDE (2 x A4) — rendered after the pieces
SPECS = [
    ("BIG · fabric", None),
    ("A1", "Hanging banner", "80 × 180 cm", "Cotton canvas or linen-look polyester, matte, dye-sublimation", "1",
     "Hemmed edges + 5 cm pole pocket top &amp; bottom (or 4 brass eyelets). Hang on a wooden frame or a clothing rail"),
    ("A2", "Table-front / tent header banner", "150 × 50 cm", "Same fabric as A1", "1",
     "Eyelets in the 4 corners. Clip it to the front table edge or the gazebo valance"),
    ("A3", "Table runner", "50 × 140 cm", "Heavy cotton canvas, dye-sublimation", "1",
     "Hemmed. Olive end lies at the back of the table, flowers + maroon hem hang down the front"),
    ("SMALL · card &amp; paper", None),
    ("B1", "Follow us card", "A5", "350 gsm uncoated / matte card", "2",
     "One in a wooden block stand at the front of the table, one by the till"),
    ("B2", "Our story card", "A5", "350 gsm uncoated / matte card", "1", "Next to the Follow us card"),
    ("B3", "Table signs (try-on, suti, handcrafted, card &amp; cash)", "4 × A6 on A4", "350 gsm matte card", "1 sheet",
     "Cut on the dashed lines. Clip to the rail, mirror and till"),
    ("B4", "Hang tags (one per product, QR to its page)", "50 × 90 mm, 12 on A4", "400 gsm uncoated card", "3–4 sheets",
     "Punch the circle (5 mm), tie on with jute twine. The blank 12th tag is for anything new"),
    ("B5", "Thank-you cards", "85 × 55 mm, 10 on A4", "350 gsm matte card", "10 sheets (100)",
     "One in every bag. The QR goes to your Instagram"),
    ("B6", "Round stickers", "Ø 50 mm, 15 on A4", "Matte paper sticker sheet, kiss-cut", "4 sheets (60)",
     "Seal tissue paper and kraft bags"),
    ("C1", "This-weekend poster", "A4", "170 gsm silk paper", "2", "Venue board or a shop window nearby"),
    ("DIGITAL · Instagram", None),
    ("C2", "Feed post", "1080 × 1350 px", "PNG", "—", "Post Thursday evening"),
    ("C3", "Story", "1080 × 1920 px", "PNG", "—", "Thursday night, Friday morning, Saturday morning. Add a link sticker to sutine.com"),
]


def guide_html():
    pv = lambda n: (ROOT / "preview" / f"{n}.png").as_uri()
    rows = ""
    for r in SPECS:
        if r[1] is None:
            rows += f'<tr class="sec"><td colspan="6">{r[0]}</td></tr>'
        else:
            rows += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    mock = f"""
<div class="mock">
  <div class="wall"></div><div class="floor"></div>
  <div class="frame"><div class="fb"></div><img src="{pv('A1-hanging-banner-80x180cm')}"></div>
  <div class="rail"><div class="bar"></div>
    {''.join(f'<div class="gar" style="left:{x}%;background:{c};height:{h}%"></div>' for x, c, h in
             [(6,'#fff',62),(18,'#7A1F26',38),(30,'#fff',70),(42,'#5F6B3A',36),(54,'#fff',66),(66,'#E9E4F0',58),(78,'#efe9df',64)])}
  </div>
  <div class="table"><div class="top"></div><div class="cloth"></div>
    <div class="runner" style="background-image:url({pv('A3-table-runner-50x140cm')})"></div>
    <div class="card c1"><img src="{pv('B1-follow-us-card-A5')}"></div><div class="card c2"><img src="{pv('B2-our-story-card-A5')}"></div>
    <div class="fold"></div>
  </div>
</div>"""
    return page(210, 297, f"""
<div class="page g">
  <div class="hd">{wordmark()}<div><p class="caps">Pop-up stall · print guide</p><p class="it">{EVENT['days']}</p></div></div>
  <h2>How the stall comes together</h2>
  {mock}
  <ol class="setup">
    <li><b>Back left:</b> A1 banner on its frame, slightly angled so it can be seen from the walkway.</li>
    <li><b>Table:</b> plain beige or white base cloth to the floor, A3 runner on top, flowers facing the customer.
        Use the A2 banner instead of the runner if the table is wider than 1.5 m.</li>
    <li><b>On the table:</b> B1 Follow us + B2 Our story in wooden block stands, folded pieces in low stacks, Totes &amp; Thailis in a basket.</li>
    <li><b>Rail:</b> on the right, wooden hangers, light to dark. B4 tag on every piece, B3 "Try it on" sign clipped to the end.</li>
    <li><b>Bags:</b> kraft bag, cream tissue sealed with a B6 sticker, and a B5 thank-you card inside.</li>
  </ol>
  {SMALL_HEM}
</div>
<div class="page g">
  <h2>What to print</h2>
  <table><tr class="th"><td></td><td>Piece</td><td>Finished size</td><td>Material</td><td>Qty</td><td>Finishing &amp; where it goes</td></tr>{rows}</table>
  <h2>Notes for the printer</h2>
  <ul class="notes">
    <li>Files are vector PDFs at 100% finished size. Fabric: add 3 cm hem allowance on every side (no bleed is built in).
        Card: print edge to edge, then trim on the dashed guides.</li>
    <li>Colours: cream <b>#F7F3EC</b>, maroon <b>#7A1F26</b>, olive <b>#5F6B3A</b>, ink <b>#2A2523</b>. Ask for a small
        test swatch of the fabric. Maroon goes darker on canvas.</li>
    <li>If you print on natural or undyed linen, the cream background can be left unprinted so the fabric shows through.</li>
    <li>Scan every QR code on the proof before the full run.</li>
  </ul>
  <h2>Bring on the day</h2>
  <div class="cols"><ul>
    <li>Banner frame or pole, cable ties, S-hooks</li><li>Clothing rail + wooden hangers</li><li>Base tablecloth (to the floor)</li>
    <li>2 wooden block stands, bulldog clips</li><li>Mirror + changing curtain</li><li>Basket for totes &amp; thailis</li></ul><ul>
    <li>Card reader (charged) + cash float</li><li>Kraft bags, cream tissue, twine</li><li>Sales Receipt form open on a phone</li>
    <li>Power bank, tape, scissors, pens</li><li>Email sign-up sheet for new arrivals</li><li>Water &amp; snacks ♡</li></ul></div>
  {SMALL_HEM}
</div>""", """
.g { padding: 12mm 14mm 0; align-items: stretch; page-break-after: always; }
.hd { display: flex; align-items: flex-end; justify-content: space-between; border-bottom: .3mm solid #2A2523; padding-bottom: 3mm; }
.hd .wm { text-align: left; } .hd .wm-main { font-size: 12mm; } .hd .wm-by { font-size: 5.6mm; }
.hd .caps { font-size: 2.6mm; color: #7A1F26; text-align: right; } .hd .it { font-size: 4.4mm; text-align: right; margin-top: 1mm; }
h2 { font-family: 'Playfair Display'; font-weight: 400; font-size: 6.2mm; margin: 5mm 0 2.5mm; }
.mock { position: relative; height: 120mm; border-radius: 2mm; overflow: hidden; }
.wall { position: absolute; inset: 0 0 22% 0; background: linear-gradient(#e9e2d7, #ddd3c5); }
.floor { position: absolute; left: 0; right: 0; bottom: 0; height: 22%; background: linear-gradient(#c9b9a3, #b8a68e); }
.frame { position: absolute; left: 6%; bottom: 12%; width: 17%; height: 83%; }
.frame .fb { position: absolute; inset: -2.5mm -2mm -5mm; border: 2mm solid #b48a5c; border-bottom: none; }
.frame img { width: 100%; height: 100%; object-fit: fill; box-shadow: 0 1mm 3mm #0003; }
.rail { position: absolute; right: 5%; bottom: 12%; width: 30%; height: 72%; border-left: 1.2mm solid #2A2523; border-right: 1.2mm solid #2A2523; }
.rail .bar { position: absolute; top: 0; left: 0; right: 0; height: 1.2mm; background: #2A2523; }
.gar { position: absolute; top: 3mm; width: 10%; border-radius: 1.5mm 1.5mm .5mm .5mm; box-shadow: 0 .5mm 1.5mm #0002; }
.table { position: absolute; left: 27%; bottom: 6%; width: 40%; height: 44%; }
.table .top { position: absolute; top: 0; left: -2%; right: -2%; height: 5%; background: #efe9df; border-radius: 1mm; }
.table .cloth { position: absolute; top: 5%; left: 0; right: 0; bottom: 0; background: #e8dfd2; box-shadow: inset 0 -2mm 3mm #0001; }
.runner { position: absolute; top: 5%; left: 33%; width: 34%; bottom: 0; background-size: 100% auto; background-position: center bottom; box-shadow: 0 .5mm 2mm #0002; }
.card { position: absolute; bottom: 99%; width: 11%; } .card img { width: 100%; display: block; box-shadow: 0 .5mm 1.5mm #0003; }
.card::after { content: ""; display: block; height: 2.2mm; background: #c79f72; margin: 0 -8%; }
.c1 { left: 8%; } .c2 { left: 79%; }
.setup { font-size: 4.1mm; line-height: 1.38; padding-left: 5mm; margin-top: 5mm; } .setup li { margin-bottom: 1.8mm; }
.setup b, .notes b { font-weight: 600; color: #7A1F26; }
table { width: 100%; border-collapse: collapse; font-size: 3.05mm; line-height: 1.2; }
td { padding: 1.1mm 1.4mm; border-bottom: .15mm solid #d8cfc3; vertical-align: top; }
.th td { font-family: 'Karla'; font-size: 2.3mm; text-transform: uppercase; letter-spacing: .15em; color: #7A716B; border-bottom: .3mm solid #2A2523; }
.sec td { font-family: 'Karla'; font-size: 2.4mm; letter-spacing: .2em; text-transform: uppercase; color: #7A1F26; padding-top: 3.5mm; border-bottom: none; }
td:first-child { font-family: 'Playfair Display'; color: #7A1F26; width: 7mm; }
td:nth-child(2) { font-weight: 600; width: 32mm; } td:nth-child(3) { width: 24mm; } td:nth-child(4) { width: 36mm; } td:nth-child(5) { width: 15mm; }
.notes { font-size: 3.5mm; line-height: 1.32; padding-left: 5mm; } .notes li { margin-bottom: 1.4mm; }
.cols { display: flex; gap: 8mm; } .cols ul { flex: 1; font-size: 3.4mm; line-height: 1.42; padding-left: 5mm; list-style: '☐  '; }
""")


def render_guide():
    f = ROOT / "html" / "00-PRINT-GUIDE.html"; f.write_text(guide_html())
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
        pg = b.new_page(viewport={"width": 794, "height": 1123})
        pg.goto(f.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(ROOT / "print" / "00-PRINT-GUIDE.pdf"), width="210mm", height="297mm", print_background=True)
        pg.screenshot(path=str(ROOT / "preview" / "00-print-guide-p1.png"))
        b.close()


if __name__ == "__main__":
    render_guide()
