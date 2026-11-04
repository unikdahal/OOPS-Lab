# Sutíne by Yojana — Pop-up Stall Kit (Fri 6 & Sat 7 Nov)

Brand: cream `#FAF8F6`, dusty rose `#D4B0AB`/`#BD8F89`, charcoal `#292524`, lali maroon `#7B1E22` + olive `#6B7340` (taken from the garment borders).
Fonts: Playfair Display + Crimson Text (the same ones sutine.com uses).

## Files (`print/` = send these to the printer)
| # | Piece | Size | How to print |
|---|-------|------|--------------|
| 01 | Hanging banner | 80 × 180 cm | Print on natural linen/canvas fabric; hem the top for a pole or tie it to a wooden frame |
| 02 | Table runner | 60 × 150 cm | Fabric. Top 60 cm lies on the table; artwork sits on the 90 cm front drop (the fold line is marked) |
| 03 | Follow Us card | A5 | 300gsm matte card, then clip it into a wooden block stand |
| 04 | Brand story card | A5 | 300gsm matte card, displayed next to Follow Us |
| 05 | Sets, offer, sizing & payment cards | 4 × A6 on one A4 sheet | Cut along the dashed lines, fill in with a fine black pen, hang from the rail with clips |
| 06 | Thank-you / QR cards | 10 × 85×55 mm on A4 | 350gsm. Print about 10 sheets (100 cards) and put one in every bag |
| 07 | "This weekend" poster | A4 | Post it on socials Thu & Fri, and use it on the venue board |
| 08 | Price board (real sutine.com prices) | A4 | Frame it or stand it on an easel |
| 09 | Hang tags, one per product, each with a QR code to that product's page | 12 × 50×90 mm on A4 | 350gsm. Punch the circle and tie on with twine. The 12th tag is blank. Print 3–4 sheets |
| 10 | Lookbook (photos + prices + shop QR) | A4 | Put it on the table, and post it on IG |

Products and prices were pulled from the sutine.com catalogue (`assets/products.json`, photos in `assets/products/`).
If a price changes, edit `products.json` and re-run the build.

`qr/` holds the standalone QR codes (SVG + PNG):
- Instagram → https://www.instagram.com/sutine_by_yojana/
- TikTok → https://www.tiktok.com/@sutine.by.yojana
- Website → https://sutine.com/?utm_source=popup&utm_medium=qr&utm_campaign=stall-nov26 (stall scans show up separately in your analytics)

Before printing, scan every QR with a phone.

## Editing
Open `build.py` and set `EVENT["venue"]` / `EVENT["hours"]`. The poster shows a write-in line while these are blank.
Then run `pip install segno playwright && python3 build.py`.

## Stall checklist
- [ ] Wooden frame or pole for the banner, plus ties or clips
- [ ] Base tablecloth (warm beige or olive green under the cream runner looks great)
- [ ] Clothing rail, wooden hangers, S-hooks and bulldog clips for the price cards
- [ ] 2 wooden block stands for the A5 cards
- [ ] Mirror, and a curtain or try-on corner
- [ ] Card reader (charged), cash float, and the "Sales Receipt" Google Form open on a phone
- [ ] Paper bags, tissue, thank-you cards
- [ ] Phone charger and power bank, tape, scissors, a pen and a marker
- [ ] Notebook or sign-up sheet for emails (new-arrival list)
- [ ] Post on IG / TikTok Thursday night, Friday morning and Saturday morning; share Stories from the stall
