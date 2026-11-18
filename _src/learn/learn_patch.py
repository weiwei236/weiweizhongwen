# Chèn "Ôn tập hằng ngày" (srs.js) và "Bộ thủ" (bushou.js) vào src.html. Chạy lại được nhiều lần.
import os
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, '..', 'src.html')
s = open(P, encoding='utf-8').read()
rd = lambda f: open(os.path.join(D, f), encoding='utf-8').read()
def put(s, b, e, body, anchor):
    if b not in s:
        i = s.index(anchor); s = s[:i] + b + '\n' + e + '\n' + s[i:]
    i = s.index(b) + len(b); j = s.index(e)
    return s[:i] + '\n' + body + s[j:]
def once(s, old, new, mark):
    if mark in s: return s
    assert s.count(old) == 1, ('không tìm thấy duy nhất', old[:70]); return s.replace(old, new, 1)
s = put(s, '/* LEARN_CSS_BEGIN */', '/* LEARN_CSS_END */', rd('learn.css'), '/* HZ_CSS_BEGIN */')
s = put(s, '/* LEARN_JS_BEGIN */', '/* LEARN_JS_END */', rd('srs.js') + '\n' + rd('bushou.js'), '/* HZ_JS_BEGIN */')
a = '<section id="scrTrip" class="screen trip-screen" hidden><div class="tp-wrap" id="tpBody"></div></section>'
s = once(s, a, a + '\n<section id="scrReview" class="screen" hidden><div class="rv-wrap" id="rvBody"></div></section>\n<section id="scrBushou" class="screen" hidden><div class="bs-wrap" id="bsBody"></div></section>', 'id="scrReview"')
s = once(s, '"scrFarm","scrTrip",', '"scrFarm","scrTrip","scrReview","scrBushou",', '"scrReview","scrBushou"')
s = once(s, '<div class="acts"><button class="btn farm-btn" id="hiFarm">',
         '<div class="acts"><button class="btn srs-btn" id="hiSrs">🔁 Ôn tập hôm nay${(n => n ? `<span class="n">${n}</span>` : " ✓")(SRS.count())}</button><button class="btn bs-btn" id="hiBs"><span class="han">部</span> Bộ thủ</button><button class="btn farm-btn" id="hiFarm">', 'id="hiSrs"')
s = once(s, '  $("#hiFarm").onclick=()=>Farm.open();', '  $("#hiSrs").onclick=()=>SRS.open(); $("#hiBs").onclick=()=>Bushou.open();\n  $("#hiFarm").onclick=()=>Farm.open();', 'SRS.open()')
s = once(s, 'const L=LEVELS[S.level], les=L.lessons[S.lesson]; gbFillPy(les);', 'const L=LEVELS[S.level], les=L.lessons[S.lesson]; gbFillPy(les); if(les) SRS.see(S.level,S.lesson);', 'SRS.see(S.level')
s = once(s, 'game: "Trò chơi", write: "Tập viết" };', 'game: "Trò chơi", write: "Tập viết", srs: "Ôn tập hằng ngày", bushou: "Bộ thủ" };', 'srs: "Ôn tập')
s = once(s, '      case "write": return `${d.done}/${d.total} chữ đã viết đúng`;', '      case "write": return `${d.done}/${d.total} chữ đã viết đúng`;\n      case "srs": return `Ôn ${d.n} từ, nhớ ${d.right}`;\n      case "bushou": return `${d.mode === "combo" ? "Ghép chữ" : "Tìm bộ thủ"}: ${d.right}/${d.total}`;', 'case "srs"')
open(P, 'w', encoding='utf-8').write(s); print('ok')
