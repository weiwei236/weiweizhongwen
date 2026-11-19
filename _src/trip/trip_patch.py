# Chèn trò chơi Khám phá Trung Quốc (trip/*.js, trip.css) vào src.html. Chạy lại được nhiều lần.
import os, re
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, '..', 'src.html')
s = open(P, encoding='utf-8').read()
import base64, json
def img_js():
    d = os.path.join(D, 'img'); m = {}
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith('.webp'): m[f[:-5]] = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(d, f), 'rb').read()).decode()
    g = {}; gd = os.path.join(D, 'gd')
    if os.path.isdir(gd):
        for f in sorted(os.listdir(gd)):
            if f.endswith('.webp'): g[f[:-5]] = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(gd, f), 'rb').read()).decode()
    return 'const TRIP_IMG_DATA=' + json.dumps(m) + ';\nconst TRIP_GD_DATA=' + json.dumps(g) + ';\n'
rd = lambda f: open(os.path.join(D, f), encoding='utf-8').read()
def put(s, b, e, body, anchor, before=True):
    if b not in s:
        i = s.index(anchor) if before else s.index(anchor) + len(anchor)
        s = s[:i] + b + '\n' + e + '\n' + s[i:]
    i = s.index(b) + len(b); j = s.index(e)
    return s[:i] + '\n' + body + s[j:]
s = put(s, '/* TRIP_CSS_BEGIN */', '/* TRIP_CSS_END */', rd('trip.css'), '</style>')
s = put(s, '/* TRIP_JS_BEGIN */', '/* TRIP_JS_END */', img_js() + rd('trip_art.js') + '\n' + rd('trip_art2.js') + '\n' + rd('trip_data.js') + '\n' + rd('trip_data2.js') + '\n' + rd('trip_data3.js') + '\n' + rd('trip_data4.js') + '\n' + rd('trip_fx.js') + '\n' + rd('trip.js'), 'function xiaoyuSVG(')
if 'id="scrTrip"' not in s:
    a = '<section id="scrFarm" class="screen farm-screen" hidden><div class="fm-wrap" id="fmBody"></div></section>'
    s = s.replace(a, a + '\n<section id="scrTrip" class="screen trip-screen" hidden><div class="tp-wrap" id="tpBody"></div></section>', 1)
if '"scrFarm","scrTrip"' not in s:
    s = s.replace('"scrFarm","scrGrammar"', '"scrFarm","scrTrip","scrGrammar"', 1)
if 'id="hiTrip"' not in s:
    a = '<b class="coin-count">${Farm.coins()}</b></button>'
    assert a in s
    s = s.replace(a, a + '<button class="btn trip-btn" id="hiTrip"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/></svg>Khám phá TQ</button>', 1)
    s = s.replace('  $("#hiFarm").onclick=()=>Farm.open();', '  $("#hiFarm").onclick=()=>Farm.open();\n  $("#hiTrip").onclick=()=>Trip.open();', 1)
open(P, 'w', encoding='utf-8').write(s); print('ok')
