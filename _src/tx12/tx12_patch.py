"""Bài khoá HSK1–2 (giáo trình HSK 3.0): h1t.txt / h2t.txt → khối JS trong src.html.
Định dạng: '#L n|tên tiếng Việt', '#T 课文k|bối cảnh|bối cảnh vi' (hội thoại: 'người>câu|nghĩa'),
'#N 课文k|bối cảnh|bối cảnh vi' (đoạn văn: 'câu|nghĩa')."""
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(D, "..", "src.html")
def parse(fn):
    L = {}; cur = None; t = None
    for ln in open(os.path.join(D, fn), encoding="utf-8"):
        ln = ln.rstrip("\n").strip()
        if not ln: continue
        if ln.startswith("#L"):
            n, vi = ln[2:].strip().split("|", 1); cur = L.setdefault(int(n), {"vi": vi.strip(), "texts": []})
        elif ln.startswith("#T") or ln.startswith("#N"):
            p = ln[2:].strip().split("|"); t = {"t": p[0].strip(), "scene": p[1].strip() if len(p) > 1 else "", "scene_vi": p[2].strip() if len(p) > 2 else "", "lines": []}
            if ln.startswith("#N"): t["narr"] = True
            cur["texts"].append(t)
        else:
            who = ""
            if not t.get("narr") and ">" in ln: who, ln = ln.split(">", 1)
            zh, vi = (ln.split("|", 1) + [""])[:2]
            x = {"zh": zh.strip(), "py": "", "vi": vi.strip()}
            if who: x["who"] = who.strip()
            t["lines"].append(x)
    return L
data = {"hsk1": parse("h1t.txt"), "hsk2": parse("h2t.txt")}
js = ("/* HSK12_TX_BEGIN – bài khoá HSK1–2 (sinh bởi _src/tx12/tx12_patch.py) */\n"
      "const HSK12_TX = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
      "Object.entries(HSK12_TX).forEach(([lv, ls]) => Object.entries(ls).forEach(([n, x]) => { const l = LEVELS[lv] && LEVELS[lv].lessons[n]; if(!l) return; l.texts = x.texts; if(x.vi && !l.vi) l.vi = x.vi; }));\n"
      "/* HSK12_TX_END */\n")
s = open(SRC, encoding="utf-8").read()
s = re.sub(r"/\* HSK12_TX_BEGIN.*?/\* HSK12_TX_END \*/\n", "", s, flags=re.S)
anchor = "\n/* ======================= HELPERS ======================= */"
assert anchor in s
s = s.replace(anchor, "\n" + js + anchor, 1)
open(SRC, "w", encoding="utf-8").write(s)
print({k: {n: len(v["texts"]) for n, v in L.items()} for k, L in data.items()})
