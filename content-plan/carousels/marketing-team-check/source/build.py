"""Builds slides.html for the "Is your marketing team doing a good job?" carousel.

Run:  python3 build.py && node render.mjs
Colours follow brand/brand-guide.md.
"""
from pathlib import Path

NAVY9, NAVY7, NAVY5, TEAL, WHITE = "#0a1a30", "#16304e", "#2a517f", "#6896a3", "#ffffff"
GREY = "rgba(10,26,48,.4)"       # "bad sign" line art (navy at 40%)
GREY_TXT = "rgba(10,26,48,.65)"  # small text on the bad side, still readable
TOTAL = 10

# ---------- small SVG helpers ----------
def arrow_right(color, w=34):
    return (f'<svg width="{w}" height="18" viewBox="0 0 34 18" fill="none" stroke="{color}" '
            f'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M2 9H31M24 2L31 9L24 16"/></svg>')

def check(color, size=22, sw=3.4):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5L9.5 18L20 6.5"/></svg>')

def cross(color, size=20, sw=3.2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"><path d="M5 5L19 19M19 5L5 19"/></svg>')

BOOKMARK = ('<svg width="18" height="22" viewBox="0 0 18 22" fill="none" stroke="currentColor" stroke-width="2.4" '
            'stroke-linejoin="round"><path d="M2 2H16V20L9 15L2 20Z"/></svg>')

def svg(body, color):
    return (f'<svg width="360" height="340" viewBox="0 0 360 340" fill="none" stroke="{color}" stroke-width="5" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')

def bubble(x, y, w=64, h=42, dots=True):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/><path d="M{x+14} {y+h} L{x+10} {y+h+14} L{x+28} {y+h}"/>'
    if dots:
        cy = y + h / 2
        s += "".join(f'<circle cx="{x + w/2 + d}" cy="{cy}" r="1.5" stroke-width="5"/>' for d in (-14, 0, 14))
    return s

def calendar_tick(x, y):
    return (f'<rect x="{x}" y="{y}" width="60" height="56" rx="8"/><path d="M{x} {y+18}H{x+60}"/>'
            f'<path d="M{x+16} {y-8}V{y+6}M{x+44} {y-8}V{y+6}"/>'
            f'<path d="M{x+16} {y+37}L{x+26} {y+46}L{x+44} {y+28}" stroke-width="5"/>')

def person(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="13"/><path d="M{x} {y+20}V{y+66}"/>'
            f'<path d="M{x} {y+66}L{x-14} {y+100}M{x} {y+66}L{x+16} {y+98}"/>'
            f'<path d="M{x-18} {y+46}L{x} {y+32}L{x+20} {y+44}"/>')

def phone(x, y):
    return f'<rect x="{x}" y="{y}" width="50" height="84" rx="10"/><path d="M{x+19} {y+72}H{x+31}"/>'

# ---------- illustrations (360 x 340) ----------
ILL = {}

# 1 Cost per customer
ILL[1] = (
    svg('<path d="M60 110H220L290 175L220 240H60Z"/><circle cx="238" cy="175" r="10"/>'
        '<path d="M248 168C280 130 300 100 330 78"/>'
        f'<text x="140" y="208" font-size="96" font-weight="800" fill="{GREY}" stroke="none" text-anchor="middle">?</text>', GREY),
    svg('<path d="M50 60V270M14 232L50 270L86 232"/>'
        f'<text x="112" y="140" font-size="42" font-weight="700" fill="{GREY}" stroke="none">AED 200</text>'
        '<path d="M108 126H296" stroke-width="4"/>'
        f'<text x="112" y="232" font-size="56" font-weight="800" fill="{NAVY5}" stroke="none">AED 160</text>', TEAL),
)

# 2 Enquiries -> customers
_funnel = '<path d="M40 70H320L215 185V238H145V185Z"/>'
ILL[2] = (
    svg(_funnel + bubble(70, 8) + bubble(150, 0) + bubble(232, 10) + bubble(118, 92, 56, 36) + bubble(190, 96, 56, 36)
        + '<path d="M180 262V300" stroke-dasharray="2 14"/>'
        f'<text x="180" y="336" font-size="26" font-weight="700" fill="{GREY_TXT}" stroke="none" text-anchor="middle">0 out</text>', GREY),
    svg('<path d="M40 40H320L215 140V180H145V140Z"/>' + bubble(100, 62, 56, 34) + bubble(196, 62, 56, 34)
        + '<path d="M165 186C150 220 110 225 92 240M180 186V236M195 186C210 220 250 225 268 240"/>'
        + calendar_tick(62, 262) + calendar_tick(150, 262) + calendar_tick(238, 262), TEAL),
)

# 3 Reply time
ILL[3] = (
    svg('<circle cx="140" cy="150" r="108"/><path d="M140 150V78M140 150H200"/>'
        '<path d="M140 50V60M240 150H230M140 250V240M40 150H50" stroke-width="6"/>'
        + bubble(236, 14, 116, 56, dots=False)
        + f'<text x="294" y="51" font-size="26" font-weight="700" fill="{GREY_TXT}" stroke="none" text-anchor="middle">Seen</text>'
        + f'<text x="140" y="318" font-size="30" font-weight="800" fill="{GREY_TXT}" stroke="none" text-anchor="middle">3 hours</text>', GREY),
    svg('<circle cx="160" cy="185" r="115"/><path d="M142 48H178M160 48V70"/>'
        '<path d="M160 115A70 70 0 0 1 219 147" stroke-width="10"/>'
        f'<text x="160" y="212" font-size="56" font-weight="800" fill="{NAVY5}" stroke="none" text-anchor="middle">2 min</text>'
        '<circle cx="300" cy="62" r="34"/><path d="M285 63L296 74L316 51"/>', TEAL),
)

# 4 Repeat customers
ILL[4] = (
    svg('<path d="M40 50H150V300H40Z" stroke-width="4"/><path d="M150 50L196 72V318L150 300Z"/>'
        + person(225, 110) + person(282, 118) + person(335, 126)
        + '<path d="M215 300H335M318 286L335 300L318 314"/>', GREY),
    svg('<path d="M30 60H130V300H30Z"/>'
        + '<path d="M255 70A95 95 0 1 1 164 200"/><path d="M181 216L161 197L149 222"/>'
        + person(232, 118) + person(282, 118), TEAL),
)

# 5 Shares, not likes
ILL[5] = (
    svg('<path d="M170 280C50 200 50 90 120 86C150 84 170 112 170 112C170 112 190 84 220 86C290 90 290 200 170 280Z"/>'
        f'<text x="300" y="100" font-size="52" font-weight="800" fill="{GREY}" stroke="none" text-anchor="middle">+1</text>', GREY),
    svg('<path d="M20 175L160 115L118 232L100 190Z"/><path d="M100 190L160 115"/>'
        '<path d="M170 120C210 80 240 60 270 58M172 140C220 150 250 165 282 168M150 175C190 240 230 270 270 272" '
        'stroke-dasharray="3 13" stroke-width="4.5"/>'
        + phone(280, 14) + phone(292, 126) + phone(280, 238), TEAL),
)

# 6 Reports in AED
def _doc(x, w):
    return f'<rect x="{x}" y="22" width="{w}" height="296" rx="16"/><path d="M{x+30} 64H{x+120}" stroke-width="8"/>'

ILL[6] = (
    svg(_doc(70, 220)
        + f'<text x="100" y="150" font-size="36" font-weight="700" fill="{GREY_TXT}" stroke="none">Views ↑</text>'
        + f'<text x="100" y="220" font-size="36" font-weight="700" fill="{GREY_TXT}" stroke="none">Likes ↑</text>'
        + '<path d="M100 262H240" stroke-dasharray="2 14"/>', GREY),
    svg(_doc(40, 280)
        + "".join(f'<text x="70" y="{y}" font-size="32" font-weight="800" fill="{NAVY5}" stroke="none">{t}</text>'
                  f'<path d="M262 {y-20}L272 {y-10}L292 {y-32}"/>'
                  for t, y in (("Customers", 140), ("Revenue", 208), ("Cost", 276))), TEAL),
)

# ---------- slide chrome ----------
def chrome(n, theme):
    navy = theme == "navy"
    count_col = TEAL if navy else NAVY5
    dots = "".join(f'<span class="dot{" on" if i == n else ""}"></span>' for i in range(1, TOTAL + 1))
    return (f'<div class="handle">@nextdigitalgrowth</div>'
            f'<div class="count" style="color:{count_col}">{n}/{TOTAL} {arrow_right(count_col)}</div>'
            f'<div class="dots">{dots}</div>'
            f'<div class="save">{BOOKMARK}<span>Save for later</span></div>')

def slide(n, theme, inner):
    return f'<section class="slide {theme}" id="s{n}">{inner}{chrome(n, theme)}</section>'

def t(word):
    return f'<span class="teal">{word}</span>'

# ---------- slides ----------
S = []

# 1 Cover
S.append(slide(1, "navy", f"""
<div class="glow" style="background:radial-gradient(circle at 900px 900px, rgba(104,150,163,.30), transparent 420px)"></div>
<h1 class="cover">Every<br>business<br>needs to {t('know')}</h1>
<svg class="abs" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none">
  <circle cx="84" cy="1050" r="11" fill="#fff"/>
  <path d="M84 1050C430 1050 640 890 1080 890" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
</svg>"""))

# 2 Map
branches = ["Cost per customer", "Enquiries → customers", "Reply time",
            "Repeat customers", "Shares, not likes", "Reports in AED"]
ys = [620, 722, 824, 926, 1028, 1130]
paths = "".join(f'<path d="M230 890C330 890 340 {y} 440 {y}"/>' for y in ys)
dots2 = "".join(f'<circle cx="452" cy="{y}" r="12" fill="{TEAL}" stroke="none"/>' for y in ys)
labels = "".join(f'<div class="branch" style="top:{y-24}px"><span class="teal">#{i}</span> {b}</div>'
                 for i, (b, y) in enumerate(zip(branches, ys), 1))
S.append(slide(2, "navy", f"""
<h1 class="map">…if their marketing team is doing a {t('good job.')}</h1>
<svg class="abs" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round">
  <path d="M0 890H230"/>{paths}{dots2}
</svg>{labels}"""))

# 3-8 White "sign" slides
SIGNS = [
    ("Cost per customer",
     "A good team knows this number, and it goes down. <b>If nobody can tell you the number, that’s your answer.</b>",
     "Nobody knows the number", "Known, and going down", "Example figures."),
    ("Enquiries → customers",
     "Messages are nice. <b>Paying customers are the job.</b>",
     "Lots of messages, no bookings", "Messages turn into bookings", None),
    ("Reply time",
     "People message 3–4 businesses at once. <b>The fastest reply usually wins.</b>",
     "Left on “Seen” for 3 hours", "Replied in 2 minutes", "Example times."),
    ("Repeat customers",
     "Winning a customer is expensive. <b>Keeping one is cheap.</b>",
     "They buy once and leave", "They keep coming back", None),
    ("Shares, not likes",
     "A like is a nod. <b>A share is a recommendation.</b>",
     "A like: +1, then forgotten", "A share: sent to 3 friends", None),
    ("Reports in AED",
     "Followers and views are clues, <b>not results.</b>",
     "Looks busy, says nothing", "Shows what you earned", None),
]
for i, (title, body, bad_cap, good_cap, note) in enumerate(SIGNS, 1):
    bad, good = ILL[i]
    foot = f'<div class="note">{note}</div>' if note else ""
    S.append(slide(i + 2, "light", f"""
<div class="tagrow"><span class="tag">#{i}</span><span class="title">{title}</span></div>
<p class="body">{body}</p>
<div class="cards">
  <div class="card bad"><div class="label">{cross(GREY_TXT)}<span>Bad sign</span></div>{bad}<div class="cap">{bad_cap}</div></div>
  <div class="card good"><div class="label">{check(NAVY5)}<span>Good sign</span></div>{good}<div class="cap">{good_cap}</div></div>
</div>
<svg class="abs" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none">
  <path d="M0 1196H1080" stroke="{TEAL}" stroke-width="4"/>
</svg>{foot}"""))

# 9 Scorecard
QS = ["What does each new customer cost us?",
      "How many enquiries became customers?",
      "How fast do we reply to messages?",
      "How many customers came back?",
      "How many people shared our posts?",
      "What did we make this month, in AED?"]
rows = "".join(f'<li><span class="tick">{check(TEAL, 28, 3.2)}</span><span>{q}</span></li>' for q in QS)
S.append(slide(9, "navy", f"""
<h1 class="score">Your team is doing a good job if they can answer {t('these:')}</h1>
<ul class="qs">{rows}</ul>
<div class="closer">Can’t answer? That’s the problem.</div>"""))

# 10 CTA
S.append(slide(10, "navy", f"""
<h1 class="cta">Not sure what your {t('numbers')} are?</h1>
<p class="sub">DM us one word. We’ll look at them with you.</p>
<div class="glow" style="background:radial-gradient(ellipse 460px 300px at 590px 965px, rgba(104,150,163,.35), transparent 100%)"></div>
<svg class="abs" width="1080" height="1350" viewBox="0 0 1080 1350" fill="none">
  <path d="M0 1150C140 1150 110 965 222 965" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
  <circle cx="226" cy="965" r="11" fill="#fff"/>
</svg>
<div class="button">DM “AUDIT”</div>"""))

CSS = f"""
@font-face{{font-family:Inter;src:url(fonts/Inter-400.ttf);font-weight:400}}
@font-face{{font-family:Inter;src:url(fonts/Inter-600.ttf);font-weight:500 600}}
@font-face{{font-family:Inter;src:url(fonts/Inter-700.ttf);font-weight:700}}
@font-face{{font-family:Inter;src:url(fonts/Inter-800.ttf);font-weight:800 900}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#555;font-family:Inter,sans-serif}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 auto 40px}}
.navy{{background:linear-gradient(160deg,{NAVY9} 0%,{NAVY7} 55%,{NAVY5} 100%);color:{WHITE}}}
.light{{background:linear-gradient(180deg,#ffffff 0%,#e8eff1 100%);color:{NAVY9}}}
.abs,.glow{{position:absolute;inset:0}}
.teal{{color:{TEAL}}}
.handle{{position:absolute;left:72px;top:64px;font-size:28px;font-weight:600;letter-spacing:-.2px}}
.count{{position:absolute;right:72px;top:64px;font-size:28px;font-weight:700;display:flex;align-items:center;gap:12px}}
.dots{{position:absolute;left:50%;transform:translateX(-50%);top:1272px;display:flex;gap:12px}}
.dot{{width:12px;height:12px;border-radius:6px;background:rgba(255,255,255,.3)}}
.dot.on{{width:36px;background:#fff}}
.light .dot{{background:rgba(10,26,48,.18)}} .light .dot.on{{background:{NAVY9}}}
.save{{position:absolute;right:72px;top:1250px;height:56px;padding:0 26px;border-radius:28px;display:flex;align-items:center;
  gap:10px;font-size:22px;font-weight:700;background:#fff;color:{NAVY9}}}
.light .save{{background:{NAVY9};color:#fff}}
.note{{position:absolute;left:72px;top:1262px;font-size:22px;font-weight:600;color:{GREY_TXT}}}
h1{{font-weight:800;letter-spacing:-2px;position:absolute;left:72px;right:72px}}
h1.cover{{top:300px;font-size:140px;line-height:1.0;letter-spacing:-4.5px}}
h1.map{{top:190px;font-size:80px;line-height:1.08}}
h1.score{{top:190px;font-size:66px;line-height:1.1}}
h1.cta{{top:300px;font-size:108px;line-height:1.02;letter-spacing:-3.5px}}
.branch{{position:absolute;left:492px;font-size:40px;font-weight:700;line-height:48px;letter-spacing:-.5px}}
.tagrow{{position:absolute;left:72px;top:176px;display:flex;align-items:center;gap:28px}}
.tag{{background:{NAVY9};color:#fff;font-size:48px;font-weight:800;padding:8px 22px;border-radius:6px;letter-spacing:-1px}}
.title{{font-size:56px;font-weight:800;letter-spacing:-1.5px}}
.body{{position:absolute;left:72px;right:72px;top:318px;font-size:44px;line-height:1.28;font-weight:400;letter-spacing:-.6px}}
.body b{{font-weight:800}}
.cards{{position:absolute;left:72px;right:72px;top:594px;height:552px;display:flex;gap:24px}}
.card{{flex:1;background:#fff;border-radius:28px;padding:28px 24px 0;display:flex;flex-direction:column;align-items:center;
  border:2px solid rgba(10,26,48,.08)}}
.card.good{{border:3px solid {TEAL}}}
.label{{align-self:flex-start;display:flex;align-items:center;gap:10px;font-size:22px;font-weight:800;text-transform:uppercase;
  letter-spacing:2px;margin-bottom:22px}}
.bad .label,.bad .cap{{color:{GREY_TXT}}}
.good .label,.good .cap{{color:{NAVY5}}}
.cap{{margin-top:22px;font-size:27px;font-weight:700;text-align:center;letter-spacing:-.3px}}
.qs{{position:absolute;left:72px;right:72px;top:470px;list-style:none}}
.qs li{{display:flex;align-items:center;gap:26px;height:92px;font-size:38px;font-weight:600;letter-spacing:-.5px;
  border-bottom:1px solid rgba(255,255,255,.14)}}
.tick{{flex:none;width:56px;height:56px;border-radius:50%;border:3px solid {TEAL};display:flex;align-items:center;justify-content:center}}
.closer{{position:absolute;left:72px;right:72px;top:1072px;padding:30px 36px;border-radius:24px;background:rgba(10,26,48,.6);
  color:{TEAL};font-size:50px;font-weight:800;letter-spacing:-1px}}
.sub{{position:absolute;left:72px;right:72px;top:690px;font-size:40px;line-height:1.3;color:rgba(255,255,255,.88)}}
.button{{position:absolute;left:260px;top:890px;width:660px;height:150px;border-radius:75px;
  background:linear-gradient(135deg,{NAVY5} 0%,{TEAL} 60%);color:{NAVY9};font-size:66px;font-weight:800;letter-spacing:-1.5px;
  display:flex;align-items:center;justify-content:center;box-shadow:0 20px 60px rgba(10,26,48,.45)}}
"""

html = f'<!doctype html><html><head><meta charset="utf-8"><title>Marketing team check carousel</title><style>{CSS}</style></head><body>{"".join(S)}</body></html>'
Path(__file__).with_name("slides.html").write_text(html, encoding="utf-8")
print("wrote slides.html")
