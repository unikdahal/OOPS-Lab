"""FINAL two print pieces for the Sutine pop-up stall.

  1. Table runner 80 x 180 cm (lies across a standard 6 ft table, front end hangs down)
  2. "Follow us" QR card, A5 (for a wooden block stand / clip)

Run:  python3 final.py      ->  final/*.pdf (print-ready, real size) + final/*-preview.png
Shared motifs, colours and QR helper come from build.py.
"""
from build import (ROOT, CHROME, IG, TT, WEB, CREAM, INK, MAROON, OLIVE, TAUPE, PX,
                   page, wordmark, garden, phul, leaf, qr)
from playwright.sync_api import sync_playwright

OUT = ROOT / "final"


def spray(flip=False):
    """Tall applique flower stem, like the botanical sprigs either side of the EAN runner."""
    stems = (f'<g fill="none" stroke="{OLIVE}" stroke-width="4" stroke-linecap="round">'
             f'<path d="M80 515 C70 420 92 310 80 150"/><path d="M82 340 C112 312 126 285 122 250"/>'
             f'<path d="M78 410 C52 388 40 362 44 330"/></g>'
             f'<g fill="none" stroke="{CREAM}" stroke-width="1.1" stroke-dasharray="2.6 2.2">'
             f'<path d="M80 505 C71 420 91 310 80 160"/></g>')
    items = [("f", 80, 112, 1.0, 0, MAROON), ("f", 124, 236, .55, 15, OLIVE), ("f", 44, 318, .42, -10, MAROON),
             ("l", 82, 200, .9, -150, OLIVE), ("l", 80, 260, .9, -35, OLIVE), ("l", 80, 450, 1.0, -150, OLIVE),
             ("l", 82, 380, .85, -30, OLIVE)]
    body = "".join(f'<g transform="translate({x} {y}) rotate({r}) scale({s})">{phul(c) if k == "f" else leaf(c)}</g>'
                   for k, x, y, s, r, c in items)
    t = ' transform="translate(160 0) scale(-1 1)"' if flip else ""
    return f'<svg class="spray" viewBox="0 0 160 520"><g{t}>{stems}{body}</g></svg>'


# 1 · TABLE RUNNER 80 x 180 cm
# On a 6 ft (183 x 76 cm) table: ~30 cm hangs at the back, 76 cm across the top, ~74 cm drops at the front.
# The artwork sits on the front drop so it is upright and readable to customers.
RUNNER = page(800, 1800, f"""
<div class="page">
  <div class="trim" style="top:28mm;height:6mm"></div>
  <div class="hem olive" style="top:0;bottom:auto;height:24mm"></div>
  <div class="art">
    {spray()}
    <div class="mid">
      {wordmark()}
      <p class="caps l1">Handcrafted in Nepal</p>
    </div>
    {spray(True)}
  </div>
  <div class="trim" style="bottom:66mm;height:7mm"></div>
  <div class="hem" style="height:60mm"></div>
</div>""", """
.art { position: absolute; left: 0; right: 0; bottom: 115mm; display: flex; align-items: center; justify-content: center; gap: 6mm; }
.spray { width: 165mm; height: 536mm; flex-shrink: 0; }
.mid { display: flex; flex-direction: column; align-items: center; }
.wm-main { font-size: 124mm; } .wm-by { font-size: 62mm; margin-top: 6mm; }
.l1 { font-size: 18mm; margin-top: 46mm; letter-spacing: .28em; white-space: nowrap; }
.l2 { font-size: 14mm; margin-top: 12mm; color: #7A716B; letter-spacing: .2em; white-space: nowrap; }
.url { font-size: 18mm; letter-spacing: .5em; position: relative; }
.hem::before { top: 7mm; border-top: 1mm dashed #F7F3EC; }
""")

# 2 · FOLLOW US card A5 (148 x 210 mm)
CARD = page(148, 210, f"""
<div class="page">
  {garden("-60 -60 120 120", [("f", 0, 0, 1, 0, MAROON)], "fl")}
  {garden("-60 -60 120 120", [("f", 0, 0, 1, 0, OLIVE)], "fl2")}
  <h1>FOLLOW<br><span>us</span></h1>
  <div class="big">{qr(IG[0])}</div>
  <p class="h">{IG[1]}</p>
  <p class="it lede">New pieces, behind the seams &amp; stories from Nepal</p>
  <div class="rule"></div>
  <div class="pair">
    <div class="p"><div class="sm">{qr(TT[0])}</div><div><p class="caps lab">TikTok</p><p class="s">{TT[1]}</p></div></div>
    <div class="p"><div class="sm">{qr(WEB[0])}</div><div><p class="caps lab">Shop online</p><p class="s">sutine.com</p></div></div>
  </div>
  <div class="trim" style="bottom:9mm;height:1.4mm"></div><div class="hem" style="height:7.5mm"></div>
</div>""", """
.fl { position: absolute; top: -13mm; right: -13mm; width: 46mm; height: 46mm; }
.fl2 { position: absolute; top: 20mm; right: 22mm; width: 14mm; height: 14mm; }
h1 { align-self: flex-start; margin: 15mm 0 0 14mm; font-family: 'Playfair Display'; font-weight: 600; font-size: 21mm;
     line-height: .82; letter-spacing: -.005em; }
h1 span { display: block; text-align: right; font-style: italic; font-weight: 400; color: #7A1F26; font-size: 23mm; }
.big { width: 60mm; height: 60mm; margin-top: 9mm; }
.h { font-family: 'Playfair Display'; font-size: 6mm; margin-top: 4mm; }
.lede { font-size: 4.2mm; color: #7A716B; margin-top: 1mm; }
.rule { width: 22mm; height: .3mm; background: #7A1F26; margin: 6mm 0 5.5mm; }
.pair { display: flex; gap: 10mm; }
.p { display: flex; align-items: center; gap: 3mm; } .sm { width: 19mm; height: 19mm; flex-shrink: 0; }
.lab { font-size: 2.3mm; color: #7A716B; } .s { font-size: 3.9mm; margin-top: .8mm; }
""")

PIECES = {"1-table-runner-80x180cm": (RUNNER, 800, 1800), "2-follow-us-QR-card-A5": (CARD, 148, 210)}

if __name__ == "__main__":
    import shutil
    shutil.rmtree(OUT, ignore_errors=True); OUT.mkdir()
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
        for name, (html, w, h) in PIECES.items():
            f = OUT / f"{name}.html"; f.write_text(html)
            pg = b.new_page(viewport={"width": round(w / PX), "height": round(h / PX)})
            pg.goto(f.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready")
            pg.pdf(path=str(OUT / f"{name}.pdf"), width=f"{w}mm", height=f"{h}mm", print_background=True)
            png = OUT / f"{name}-preview.png"; pg.screenshot(path=str(png)); pg.close()
            im = Image.open(png); im.thumbnail((1600, 1600)); im.save(png)
            f.unlink()
        b.close()
    print("done")
