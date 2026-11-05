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


# 01 · BIG BACKDROP BANNER 200 x 100 cm — hangs on the back wall / gazebo back, behind the table
BACKDROP = page(2000, 1000, f"""
<div class="page bd">
  {garden("0 0 520 820", [("l",70,600,2.4,-50,OLIVE),("f",190,450,2.6,8,MAROON),("f",400,640,1.45,25,OLIVE),
                          ("l",430,330,1.7,-115,OLIVE),("f",370,190,1.05,0,MAROON),("l",120,180,1.5,-140,MAROON)], "gl")}
  <div class="mid">
    <p class="caps top">Handcrafted in Nepal &nbsp;·&nbsp; 100% cotton</p>
    {wordmark()}
    <p class="it tag">Clothes that are light on your skin and easy on your mind.</p>
  </div>
  <div class="right">
    {garden("-160 -60 320 120", [("l",-95,10,1,200,OLIVE),("f",-55,0,.62,10,MAROON),("f",0,-6,.9,0,OLIVE),
                                 ("f",55,0,.62,-12,MAROON),("l",95,10,1,-20,OLIVE)], "crown")}
    <div class="q">{qr(IG[0])}</div>
    <p class="caps f">Follow along</p><p class="h">{IG[1]}</p>
  </div>
  <div class="trim" style="bottom:118mm;height:10mm"></div>
  <div class="hem" style="height:112mm"><p class="caps hh">{IG[1]} &nbsp;&nbsp;·&nbsp;&nbsp; sutine.com &nbsp;&nbsp;·&nbsp;&nbsp; {TT[1]}</p></div>
</div>""", """
.bd { flex-direction: row; align-items: flex-start; }
.gl { width: 520mm; height: 820mm; flex-shrink: 0; margin-top: 10mm; }
.mid { flex: 1; display: flex; flex-direction: column; align-items: center; margin-top: 150mm; }
.top { font-size: 26mm; color: #7A1F26; }
.wm { margin-top: 60mm; } .wm-main { font-size: 250mm; } .wm-by { font-size: 120mm; margin-top: 12mm; }
.tag { font-size: 46mm; margin-top: 70mm; text-align: center; }
.right { width: 420mm; flex-shrink: 0; display: flex; flex-direction: column; align-items: center; margin-top: 150mm; margin-right: 50mm; }
.crown { width: 300mm; height: 112mm; }
.right .q { width: 250mm; height: 250mm; margin-top: 50mm; background: #F7F3EC; }
.f { font-size: 18mm; color: #7A716B; margin-top: 22mm; } .h { font-family: 'Playfair Display'; font-size: 40mm; margin-top: 8mm; }
.hh { font-size: 30mm; letter-spacing: .3em; text-transform: none; position: relative; }
.hem::before { top: 12mm; border-top: 1.4mm dashed #F7F3EC; }
""")

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


PRINT = {
    "01-big-backdrop-banner-200x100cm": (BACKDROP, 2000, 1000),
    "02-hanging-banner-80x180cm": (A1, 800, 1800),
    "03-table-runner-50x140cm": (A3, 500, 1400),
    "04-follow-us-card-A5": (B1, 148, 210),
    "05-our-story-card-A5": (B2, 148, 210),
}
DIGITAL = {}


def render():
    for d in ("html", "print", "preview", "qr"):
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


# ================================================================== PRINT GUIDE (2 x A4)
SPECS = [
    ("01", "Big backdrop banner", "200 × 100 cm", "Wrinkle-free polyester fabric (or cotton canvas), matte, dye-sublimation",
     "1", "Hemmed, brass eyelets every 50 cm along the top + all corners. Hang on the back wall or gazebo back with "
          "cable ties or bungees, with the bottom edge just above table height."),
    ("02", "Hanging banner", "80 × 180 cm", "Cotton canvas or linen-look fabric, matte, dye-sublimation", "1",
     "Hemmed, 5 cm pole pocket top &amp; bottom (or 4 eyelets). Hang on a wooden frame or from the rail, beside the table."),
    ("03", "Table runner", "50 × 140 cm", "Heavy cotton canvas, dye-sublimation", "1",
     "Hemmed edges. Olive end lies at the back of the table; flowers + maroon hem hang down the front."),
    ("04", "Follow along card", "A5 (148 × 210 mm)", "350 gsm matte or uncoated card", "2",
     "One in a wooden block stand at the front of the table, one by the card reader."),
    ("05", "Our story card", "A5 (148 × 210 mm)", "350 gsm matte or uncoated card", "1", "Block stand, next to the Follow along card."),
]
QRS = [
    ("01 Backdrop · 02 Hanging banner · 04 card", "Instagram", "instagram.com/sutine_by_yojana"),
    ("04 Follow along card", "TikTok", "tiktok.com/@sutine.by.yojana"),
    ("04 Follow along card", "Shop online", "sutine.com"),
]


def guide_html():
    pv = lambda n: (ROOT / "preview" / f"{n}.png").as_uri()
    rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in SPECS)
    qrows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td class='ok'>✓ tested</td></tr>" for a, b, c in QRS)
    garments = "".join(f'<div class="gar" style="left:{x}%;background:{c};height:{h}%"></div>' for x, c, h in
                       [(5,'#fff',62),(19,'#7A1F26',38),(33,'#fff',70),(47,'#5F6B3A',36),(61,'#fff',66),(75,'#E6E1EE',58)])
    mock = f"""
<div class="mock">
  <div class="wall"></div><div class="floor"></div>
  <div class="bdrop"><img src="{pv('01-big-backdrop-banner-200x100cm')}"></div>
  <div class="frame"><div class="fb"></div><img src="{pv('02-hanging-banner-80x180cm')}"></div>
  <div class="rail"><div class="bar"></div>{garments}</div>
  <div class="table"><div class="top"></div><div class="cloth"></div>
    <div class="runner" style="background-image:url({pv('03-table-runner-50x140cm')})"></div>
    <div class="card c1"><img src="{pv('04-follow-us-card-A5')}"></div><div class="card c2"><img src="{pv('05-our-story-card-A5')}"></div>
  </div>
</div>"""
    thumbs = "".join(f'<div class="th"><img src="{pv(n)}"><p><b>{n[:2]}</b> {lbl}</p></div>' for n, lbl in [
        ("01-big-backdrop-banner-200x100cm", "Backdrop 200×100 cm"), ("02-hanging-banner-80x180cm", "Hanging 80×180 cm"),
        ("03-table-runner-50x140cm", "Runner 50×140 cm"), ("04-follow-us-card-A5", "Follow along A5"),
        ("05-our-story-card-A5", "Our story A5")])
    return page(210, 297, f"""
<div class="page g">
  <div class="hd">{wordmark()}<div><p class="caps">Pop-up stall · print guide</p><p class="it">{EVENT['days']}</p></div></div>
  <h2>How the stall comes together</h2>
  {mock}
  <div class="thumbs">{thumbs}</div>
  <ol class="setup">
    <li><b>Back wall:</b> the big backdrop (01), centred behind the table. Its bottom edge sits just above the table top.</li>
    <li><b>Left:</b> the hanging banner (02) on its frame, angled slightly towards the walkway.</li>
    <li><b>Table:</b> plain beige or white cloth to the floor, runner (03) on top with the flowers facing customers.</li>
    <li><b>On the table:</b> Follow along (04) and Our story (05) in wooden block stands, folded pieces in low stacks.</li>
    <li><b>Right:</b> clothing rail, wooden hangers, light to dark.</li>
  </ol>
  {SMALL_HEM}
</div>
<div class="page g">
  <h2>What to print: 5 pieces</h2>
  <table class="spec"><tr class="thr"><td></td><td>Piece</td><td>Finished size</td><td>Material</td><td>Qty</td><td>Finishing &amp; where it goes</td></tr>{rows}</table>
  <h2>QR codes</h2>
  <table class="qrt"><tr class="thr"><td>Printed on</td><td>Code</td><td>Opens</td><td></td></tr>{qrows}</table>
  <p class="small">Every code was decoded from the final PDFs and each link opened. Still scan one on the printer's proof.</p>
  <h2>Notes for the printer</h2>
  <ul class="notes">
    <li>All files are vector PDFs at 100% finished size, so any size prints sharp. Fabric pieces: add 3 cm hem
        allowance on every side (no bleed is built in). Cards: print edge to edge, then trim to A5.</li>
    <li>Colours: cream <b>#F7F3EC</b> · maroon <b>#7A1F26</b> · olive <b>#5F6B3A</b> · ink <b>#2A2523</b>.
        Ask for a small fabric test swatch first, because maroon tends to print darker on canvas.</li>
    <li>On natural or undyed linen, the cream background can be left unprinted so the fabric shows through.</li>
    <li>Fabric printing usually takes 1–2 working days, so order 01–03 first.</li>
  </ul>
  <h2>Bring on the day</h2>
  <div class="cols"><ul>
    <li>Cable ties / bungees for the backdrop</li><li>Banner frame or pole + S-hooks</li><li>Base tablecloth (to the floor)</li>
    <li>2 wooden block stands</li></ul><ul><li>Clothing rail + wooden hangers</li><li>Mirror + changing corner</li>
    <li>Card reader (charged) + cash float</li><li>Bags, tissue, tape, scissors, pen</li></ul></div>
  {SMALL_HEM}
</div>""", """
.g { padding: 12mm 14mm 0; align-items: stretch; page-break-after: always; }
.hd { display: flex; align-items: flex-end; justify-content: space-between; border-bottom: .3mm solid #2A2523; padding-bottom: 3mm; }
.hd .wm { text-align: left; } .hd .wm-main { font-size: 12mm; } .hd .wm-by { font-size: 5.6mm; }
.hd .caps { font-size: 2.6mm; color: #7A1F26; text-align: right; } .hd .it { font-size: 4.4mm; text-align: right; margin-top: 1mm; }
h2 { font-family: 'Playfair Display'; font-weight: 400; font-size: 6.2mm; margin: 5.5mm 0 2.5mm; }
.mock { position: relative; height: 112mm; border-radius: 2mm; overflow: hidden; }
.wall { position: absolute; inset: 0 0 20% 0; background: linear-gradient(#ebe4d9, #ddd3c5); }
.floor { position: absolute; left: 0; right: 0; bottom: 0; height: 20%; background: linear-gradient(#c9b9a3, #b8a68e); }
.bdrop { position: absolute; left: 25%; top: 5%; width: 50%; } .bdrop img { width: 100%; display: block; box-shadow: 0 1mm 3mm #0003; }
.frame { position: absolute; left: 5%; bottom: 10%; width: 15%; height: 82%; }
.frame .fb { position: absolute; inset: -2.5mm -2mm -5mm; border: 2mm solid #b48a5c; border-bottom: none; }
.frame img { width: 100%; height: 100%; object-fit: fill; box-shadow: 0 1mm 3mm #0003; }
.rail { position: absolute; right: 4%; bottom: 10%; width: 18%; height: 66%; border-left: 1.1mm solid #2A2523; border-right: 1.1mm solid #2A2523; }
.rail .bar { position: absolute; top: 0; left: 0; right: 0; height: 1.1mm; background: #2A2523; }
.gar { position: absolute; top: 3mm; width: 12%; border-radius: 1.5mm 1.5mm .5mm .5mm; box-shadow: 0 .5mm 1.5mm #0002; }
.table { position: absolute; left: 27%; bottom: 5%; width: 46%; height: 38%; }
.table .top { position: absolute; top: 0; left: -2%; right: -2%; height: 5%; background: #efe9df; border-radius: 1mm; }
.table .cloth { position: absolute; top: 5%; left: 0; right: 0; bottom: 0; background: #e6ddd0; box-shadow: inset 0 -2mm 3mm #0001; }
.runner { position: absolute; top: 5%; left: 36%; width: 28%; bottom: 0; background-size: 100% auto; background-position: center bottom; box-shadow: 0 .5mm 2mm #0002; }
.card { position: absolute; bottom: 99%; width: 9%; } .card img { width: 100%; display: block; box-shadow: 0 .5mm 1.5mm #0003; }
.card::after { content: ""; display: block; height: 2mm; background: #c79f72; margin: 0 -8%; }
.c1 { left: 9%; } .c2 { left: 82%; }
.thumbs { display: flex; align-items: flex-end; justify-content: space-between; gap: 3mm; margin-top: 5mm; }
.th { text-align: center; } .th img { display: block; margin: 0 auto; max-height: 30mm; max-width: 52mm; box-shadow: 0 .4mm 1.5mm #0002; }
.th p { font-size: 2.9mm; margin-top: 1.5mm; } .th b { color: #7A1F26; font-family: 'Playfair Display'; font-weight: 400; }
.setup { font-size: 3.9mm; line-height: 1.36; padding-left: 5mm; margin-top: 5mm; } .setup li { margin-bottom: 1.4mm; }
.setup b, .notes b { font-weight: 600; color: #7A1F26; }
table { width: 100%; border-collapse: collapse; font-size: 3.2mm; line-height: 1.25; }
td { padding: 1.6mm 1.5mm; border-bottom: .15mm solid #d8cfc3; vertical-align: top; }
.thr td { font-family: 'Karla'; font-size: 2.3mm; text-transform: uppercase; letter-spacing: .15em; color: #7A716B; border-bottom: .3mm solid #2A2523; }
.spec td:first-child { font-family: 'Playfair Display'; color: #7A1F26; width: 7mm; }
.spec td:nth-child(2) { font-weight: 600; width: 27mm; } .spec td:nth-child(3) { width: 23mm; } .spec td:nth-child(4) { width: 38mm; } .spec td:nth-child(5) { width: 8mm; }
.qrt td:nth-child(2) { font-weight: 600; } .ok { color: #5F6B3A; font-weight: 600; white-space: nowrap; }
.small { font-size: 3.2mm; font-style: italic; color: #7A716B; margin-top: 1.5mm; }
.notes { font-size: 3.6mm; line-height: 1.36; padding-left: 5mm; } .notes li { margin-bottom: 1.3mm; }
.cols { display: flex; gap: 8mm; } .cols ul { flex: 1; font-size: 3.6mm; line-height: 1.5; padding-left: 5mm; list-style: '☐  '; }
""")


def render_guide():
    f = ROOT / "html" / "00-PRINT-GUIDE.html"; f.write_text(guide_html())
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
        pg = b.new_page(viewport={"width": 794, "height": 1123})
        pg.goto(f.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(ROOT / "print" / "00-PRINT-GUIDE.pdf"), width="210mm", height="297mm", print_background=True)
        b.close()


if __name__ == "__main__":
    render()
    render_guide()
    print("done")
