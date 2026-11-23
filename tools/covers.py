"""Generate one SVG cover per game (640x400). Pure code, no assets."""
import math
import os
import random
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "covers"
os.makedirs(OUT, exist_ok=True)
W, H = 640, 400


def svg(defs, body, title, sub, fg, sub_fg, serif=True):
    font = "Georgia, 'Iowan Old Style', 'Times New Roman', serif" if serif else "'Courier New', ui-monospace, monospace"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">
<defs>{defs}
<linearGradient id="shade" x1="0" y1="0" x2="0" y2="1"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.55"/></linearGradient>
</defs>
{body}
<rect width="{W}" height="{H}" fill="url(#shade)"/>
<text x="36" y="{H-58}" font-family="{font}" font-size="{40 if len(title) <= 18 else 32}" font-weight="700" fill="{fg}">{title}</text>
<text x="38" y="{H-28}" font-family="'Courier New', ui-monospace, monospace" font-size="15" letter-spacing="2" fill="{sub_fg}">{sub}</text>
</svg>"""


def rnd(seed):
    r = random.Random(seed)
    return r


def marginalia():
    r = rnd(1)
    body = '<rect width="640" height="400" fill="#f1e6cf"/>'
    # text lines as platforms
    for i, y in enumerate(range(60, 300, 26)):
        x = 60 + r.randint(0, 40)
        while x < 580:
            w = r.randint(20, 70)
            body += f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2" fill="#3b3226" opacity="{0.35 + r.random()*0.3:.2f}"/>'
            x += w + r.randint(6, 12)
    # margin line
    body += '<line x1="40" y1="30" x2="40" y2="320" stroke="#b5452f" stroke-width="1.5" opacity="0.6"/>'
    # pencil figure walking on a line
    body += '<g transform="translate(300 200)" stroke="#2a241c" stroke-width="3" fill="none" stroke-linecap="round">' \
            '<circle cx="0" cy="-34" r="8"/><path d="M0 -26 L0 -6 M0 -18 L-10 -10 M0 -18 L10 -12 M0 -6 L-8 8 M0 -6 L8 8"/></g>'
    # refuso blot
    body += '<g fill="#b5452f" opacity="0.8"><circle cx="470" cy="128" r="11"/><circle cx="482" cy="120" r="5"/><circle cx="460" cy="140" r="4"/></g>'
    return svg("", body, "Marginalia", "PLATFORM NARRATIVO · LIBRI", "#fff8ea", "#f1e6cf")


def brumafonda():
    r = rnd(2)
    defs = '<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#ffd98a" stop-opacity="0.95"/><stop offset="0.35" stop-color="#ffb347" stop-opacity="0.45"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient>' \
           '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3d5a6c"/><stop offset="1" stop-color="#1f3a34"/></linearGradient>'
    body = '<rect width="640" height="400" fill="url(#bg)"/>'
    for i in range(5):
        body += f'<ellipse cx="{r.randint(0,640)}" cy="{r.randint(80,260)}" rx="{r.randint(120,240)}" ry="{r.randint(20,40)}" fill="#cfe3e0" opacity="0.10"/>'
    # hills/trees
    body += '<path d="M0 300 Q120 240 240 290 T480 270 T640 280 V400 H0Z" fill="#2c4f3e"/>'
    for x in range(20, 640, 46):
        h = r.randint(40, 80)
        body += f'<path d="M{x} {300-h+20} l18 {h} h-36z" fill="#1c372c" opacity="0.9"/>'
    body += '<circle cx="420" cy="170" r="110" fill="url(#glow)"/>'
    body += '<g transform="translate(420 170)"><rect x="-14" y="-22" width="28" height="40" rx="6" fill="#ffe7a8" stroke="#5a3c1c" stroke-width="3"/><path d="M-10 -22 Q0 -40 10 -22" stroke="#5a3c1c" stroke-width="3" fill="none"/></g>'
    for i in range(14):
        body += f'<circle cx="{r.randint(60,620)}" cy="{r.randint(40,280)}" r="{r.choice([1.5,2,2.5])}" fill="#fff2b0" opacity="{0.5+r.random()*0.5:.2f}"/>'
    return svg(defs, body, "La Lanterna di Brumafonda", "AVVENTURA · ACQUERELLO", "#fff4d8", "#d8ece6")


def pentimento():
    r = rnd(3)
    defs = '<radialGradient id="uv" cx="0.62" cy="0.42" r="0.45"><stop offset="0" stop-color="#b98cff" stop-opacity="0.55"/><stop offset="1" stop-color="#b98cff" stop-opacity="0"/></radialGradient>'
    body = '<rect width="640" height="400" fill="#121a33"/>'
    # swirls
    for i in range(9):
        cx, cy, rad = r.randint(40, 600), r.randint(40, 260), r.randint(18, 55)
        pts = []
        for k in range(60):
            a = k / 60 * 4 * math.pi
            rr = rad * k / 60
            pts.append(f"{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}")
        body += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{r.choice(["#3e5aa8","#5b7fd0","#e3c14a"])}" stroke-width="3" opacity="0.6" stroke-linecap="round"/>'
    body += '<rect width="640" height="400" fill="url(#uv)"/>'
    # frame
    body += '<rect x="14" y="14" width="612" height="372" fill="none" stroke="#b08a3e" stroke-width="6"/>'
    # hidden signature
    body += '<text x="470" y="250" font-family="Georgia, serif" font-style="italic" font-size="28" fill="#e9dcff" opacity="0.8">A.</text>'
    return svg(defs, body, "Pentimento", "THRILLER SULL'ARTE · GO + EBITENGINE", "#f3ecff", "#c9bbf0")


def ottavio():
    body = '<rect width="640" height="400" fill="#e9c79a"/>'
    body += '<circle cx="520" cy="80" r="40" fill="#f6dfb6"/>'
    # colosseum silhouette
    body += '<path d="M90 300 V150 Q300 110 520 150 V300Z" fill="#c58a5a"/>'
    for row, (y, h) in enumerate([(165, 40), (215, 40), (262, 34)]):
        for x in range(105, 510, 34):
            body += f'<path d="M{x} {y+h} V{y+12} a12 12 0 0 1 24 0 V{y+h}Z" fill="#8a5434" opacity="0.85"/>'
    body += '<rect x="0" y="300" width="640" height="100" fill="#b77b4f"/>'
    # cat
    body += '<g transform="translate(330 300)" fill="#3a2a1f"><ellipse cx="0" cy="-22" rx="34" ry="20"/><circle cx="34" cy="-42" r="15"/><path d="M26 -54 l4 -14 l8 12z M38 -55 l8 -12 l2 14z"/><path d="M-32 -26 q-28 -10 -18 -44" stroke="#3a2a1f" stroke-width="7" fill="none" stroke-linecap="round"/></g>'
    return svg("", body, "Er Gatto de Roma", "ESPLORAZIONE · ROMA ANTICA 1:1", "#fff7ea", "#ffe8cc")


def dolce():
    body = '<rect width="640" height="400" fill="#f6dcd6"/>'
    body += '<circle cx="120" cy="90" r="70" fill="#f9e9c7" opacity="0.8"/><circle cx="540" cy="120" r="90" fill="#e8c4d8" opacity="0.6"/>'
    # bowl
    body += '<path d="M190 200 Q320 330 450 200Z" fill="#7fa7b8"/><ellipse cx="320" cy="200" rx="130" ry="22" fill="#a9c8d3"/><ellipse cx="320" cy="200" rx="112" ry="15" fill="#f4e3c3"/>'
    # stirring spiral
    pts = []
    for k in range(80):
        a = k / 80 * 5 * math.pi
        rr = 4 + 70 * k / 80
        pts.append(f"{320 + rr*math.cos(a):.1f},{200 + rr*0.18*math.sin(a):.1f}")
    body += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#d6b07a" stroke-width="2.5"/>'
    # spoon
    body += '<path d="M360 196 L470 90" stroke="#9c6b3f" stroke-width="9" stroke-linecap="round"/>'
    for (x, y, c) in [(150, 260, "#e05a6c"), (500, 270, "#f0b44c"), (560, 220, "#8cbf7a")]:
        body += f'<circle cx="{x}" cy="{y}" r="16" fill="{c}" opacity="0.75"/>'
    return svg("", body, "Dolce Stil Novo", "ZEN · DOLCI D'ITALIA", "#fff7f4", "#fff0ea")


def legami():
    r = rnd(6)
    body = '<rect width="640" height="400" fill="#2d2a4a"/>'
    pairs = [((110, 90), (300, 210), "#f4a6c1"), ((200, 260), (430, 80), "#9fd6c9"), ((480, 250), (560, 120), "#f7d488"), ((380, 290), (140, 180), "#b9a8f0")]
    for (a, b, c) in pairs:
        mx, my = (a[0]+b[0])/2 + r.randint(-60, 60), (a[1]+b[1])/2 + r.randint(-60, 60)
        body += f'<path d="M{a[0]} {a[1]} Q{mx} {my} {b[0]} {b[1]}" stroke="{c}" stroke-width="4" fill="none" opacity="0.8" stroke-linecap="round"/>'
        for p in (a, b):
            body += f'<circle cx="{p[0]}" cy="{p[1]}" r="18" fill="{c}"/><circle cx="{p[0]}" cy="{p[1]}" r="28" fill="{c}" opacity="0.15"/>'
    return svg("", body, "Legàmi", "ZEN · PUZZLE INFINITI", "#ffffff", "#d9d3f5")


def garden():
    r = rnd(7)
    body = '<rect width="640" height="400" fill="#1b2420"/>'
    for y in range(20, 400, 14):
        amp = 6
        d = f"M0 {y} " + " ".join(f"Q{x+40} {y + (amp if (x//80)%2 else -amp)} {x+80} {y}" for x in range(0, 640, 80))
        body += f'<path d="{d}" stroke="#a8b59a" stroke-width="1.2" fill="none" opacity="0.18"/>'
    body += '<ellipse cx="150" cy="150" rx="60" ry="34" fill="#4b5a50"/><ellipse cx="150" cy="140" rx="50" ry="24" fill="#66766a"/>'
    for i, (x, rot) in enumerate([(330, -8), (400, 4), (470, 12)]):
        body += f'<g transform="translate({x} 150) rotate({rot})"><rect x="-36" y="-52" width="72" height="104" rx="8" fill="#efe6d2" stroke="#c8b98f" stroke-width="2"/>'
        if i == 0:
            body += '<circle cx="0" cy="-30" r="10" fill="none" stroke="#7d8f6a" stroke-width="2.5"/>'
        body += '<rect x="-22" y="0" width="44" height="5" rx="2" fill="#8b8270"/><rect x="-16" y="12" width="32" height="5" rx="2" fill="#8b8270"/></g>'
    for i in range(16):
        body += f'<circle cx="{r.randint(20,620)}" cy="{r.randint(20,300)}" r="2.2" fill="#f2f0a0" opacity="{0.4+r.random()*0.6:.2f}"/>'
    return svg("", body, "The Associations Garden", "ZEN · SOLITARIO DI PAROLE", "#f6f1e2", "#c6d3c0")


def bitforge():
    r = rnd(8)
    body = '<rect width="640" height="400" fill="#0f2a33"/>'
    s = 16
    # pixel water shimmer
    for i in range(60):
        body += f'<rect x="{r.randint(0,39)*s}" y="{r.randint(0,24)*s}" width="{s}" height="4" fill="#1d4a57"/>'
    # islands
    for (cx, cy, rad) in [(9, 9, 5), (26, 7, 4), (31, 15, 3)]:
        for gx in range(cx - rad, cx + rad + 1):
            for gy in range(cy - rad, cy + rad + 1):
                if (gx-cx)**2 + (gy-cy)**2 <= rad*rad:
                    edge = (gx-cx)**2 + (gy-cy)**2 > (rad-1)**2
                    col = "#d9c27a" if edge else r.choice(["#4f9a4a", "#5aab52", "#46893f"])
                    body += f'<rect x="{gx*s}" y="{gy*s}" width="{s}" height="{s}" fill="{col}"/>'
    # chip
    body += '<g transform="translate(144 128)"><rect x="-22" y="-22" width="44" height="44" fill="#22262b" stroke="#9aa3ad" stroke-width="2"/>' + \
            "".join(f'<rect x="{-20+i*10}" y="-30" width="4" height="8" fill="#c9b26a"/><rect x="{-20+i*10}" y="22" width="4" height="8" fill="#c9b26a"/>' for i in range(5)) + \
            '<rect x="-8" y="-8" width="16" height="16" fill="#38e0a0"/></g>'
    return svg("", body, "BITFORGE", "CRAFTING · L'ARCIPELAGO DEL SILICIO", "#eafff4", "#9fe6c6", serif=False)


def ladder():
    body = '<rect width="640" height="400" fill="#161a2e"/>'
    # building
    body += '<rect x="120" y="30" width="400" height="300" fill="#252b4a"/>'
    for f, y in enumerate(range(50, 320, 38)):
        body += f'<rect x="120" y="{y+30}" width="400" height="4" fill="#3c4573"/>'
        for x in range(140, 510, 40):
            lit = (x * 7 + f * 13) % 5 < 2
            body += f'<rect x="{x}" y="{y}" width="24" height="18" fill="{"#ffd35c" if lit else "#323a63"}" opacity="0.9"/>'
    # ladder
    body += '<g stroke="#ff5c8a" stroke-width="5"><line x1="420" y1="40" x2="420" y2="330"/><line x1="460" y1="40" x2="460" y2="330"/></g>'
    for y in range(50, 330, 22):
        body += f'<line x1="420" y1="{y}" x2="460" y2="{y}" stroke="#ff5c8a" stroke-width="4"/>'
    # tiny hero
    body += '<g transform="translate(440 150)"><rect x="-7" y="-20" width="14" height="14" fill="#ffe0b8"/><rect x="-8" y="-6" width="16" height="18" fill="#4cc9f0"/><rect x="-6" y="-20" width="12" height="4" fill="#3a2a1f"/></g>'
    return svg("", body, "BIG COMPANY", "ARCADE · LADDER CLIMBING", "#ffffff", "#ffb3c8", serif=False)


def chillrider():
    defs = '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5b4b8a"/><stop offset="0.5" stop-color="#f08a7e"/><stop offset="1" stop-color="#ffcf9e"/></linearGradient>'
    body = '<rect width="640" height="400" fill="url(#sky)"/>'
    body += '<circle cx="320" cy="250" r="90" fill="#ffe2a8" opacity="0.95"/>'
    for i, y in enumerate([215, 235, 252, 266]):
        body += f'<rect x="200" y="{y}" width="240" height="{4+i}" fill="#f4a38c" opacity="0.8"/>'
    body += '<path d="M0 270 Q160 240 320 270 T640 262 V400 H0Z" fill="#a8607a"/>'
    body += '<path d="M290 400 L316 270 L324 270 L350 400Z" fill="#6e3f5f"/>'
    # bike
    body += '<g transform="translate(470 300)" stroke="#2c1e33" stroke-width="4" fill="none" stroke-linecap="round"><circle cx="-26" cy="0" r="18"/><circle cx="26" cy="0" r="18"/><path d="M-26 0 L-6 -24 L18 -24 L26 0 M-6 -24 L2 0 L-26 0 M14 -30 L20 -30"/></g>'
    return svg(defs, body, "Chill Rider 3D", "ZEN · BICI AL TRAMONTO · LO-FI", "#fffaf2", "#ffe9d6")


COVERS = {
    "marginalia": marginalia, "brumafonda": brumafonda, "pentimento": pentimento,
    "ottavio": ottavio, "dolce-stil-novo": dolce, "legami": legami,
    "the-associations-garden": garden, "bitforge": bitforge,
    "ladder-climbing": ladder, "chill-rider-3d": chillrider,
}

for slug, fn in COVERS.items():
    with open(os.path.join(OUT, f"{slug}.svg"), "w", encoding="utf-8") as f:
        f.write(fn())
print("ok", len(COVERS))
