# -*- coding: utf-8 -*-
# Sinh dữ liệu 发展汉语·初级综合(II) bài 1–10 (lớp Giao tiếp sơ cấp 2) → scratchpad/gt/gb.js
# Phiên âm câu để trống ("") – trang web tự điền bằng pinyin-pro khi mở bài (gbFillPy).
import json, re, sys, random, importlib
sys.path.insert(0, '/home/claude/weiweizhongwen/_src/gt')
J = lambda o: json.dumps(o, ensure_ascii=False)
HAN = re.compile(r'[一-鿿〇]')
def han(s): return len(HAN.findall(s))
LT = "ABCDEFGHIJKL"

# ---------- DSL ----------
def V(src):  # 汉字|pinyin|pos|nghĩa[|câu ví dụ~nghĩa câu]
    out = []
    for ln in src.strip().split("\n"):
        f = [x.strip() for x in ln.split("|")]
        d = dict(h=f[0], p=f[1], pos=f[2], vi=f[3])
        if len(f) > 4 and f[4]: z, v = f[4].split("~"); d["ex"] = [z.strip(), "", v.strip()]
        out.append(d)
    return out
def T(src):  # [ai>]câu|nghĩa
    out = []
    for ln in src.strip().split("\n"):
        z, v = ln.split("|"); who = ""
        if ">" in z: who, z = z.split(">", 1)
        out.append(dict(who=who.strip(), zh=z.strip(), py="", vi=v.strip()))
    return out
def Q(src):  # câu hỏi|trả lời|nghĩa câu trả lời
    out = []
    for ln in src.strip().split("\n"):
        a, b, c = [x.strip() for x in ln.split("|")]
        out.append(dict(zh=a, py="", ans=b, vi=c))
    return out
def F(slots, ex, cap=None):
    # slots "S:Chủ ngữ|V:Động từ" ; ex [("他|闭|[着]|眼睛", "。", "nghĩa")]
    sl = [s.split(":", 1) for s in slots.split("|")]
    E = []
    for c, end, vi in ex:
        cells = c.split("|"); assert len(cells) == len(sl), (c, slots)
        E.append(dict(c=cells, end=end, vi=vi))
    d = dict(slots=sl, ex=E)
    if cap: d["cap"] = cap
    return d
def G(id, zh, vi, desc, forms=(), notes=(), prac=None):
    d = dict(id=id, zh=zh, vi=vi, desc=desc, forms=list(forms))
    if notes: d["notes"] = list(notes)
    if prac: d["practice"] = [dict(type="fill", items=[[l.split(":", 1) for l in it.split("\n")] for it in prac])]
    return d

# Bài tập: các hàm trả về "phần" (part) chưa đánh số
def pool(zh, vi, words, items, inline=True):  # items: câu có 【từ】
    return dict(k="pool", zh=zh, vi=vi, pool=words, items=items, inline=inline)
def match(zh, vi, defs, items):  # items [(từ, nghĩa)] ; defs = bên phải theo thứ tự sách
    return dict(k="match", zh=zh, vi=vi, pool=defs, items=items)
def pick(zh, vi, groups):  # groups [(["旧","老"], ["我和他是【老】朋友了。", ...])]
    return dict(k="pick", zh=zh, vi=vi, groups=groups)
def posq(zh, vi, items):  # items [("他A从来B都C吃D早饭。", "不", "C")]
    return dict(k="pos", zh=zh, vi=vi, items=items)
def tf(zh, vi, items, passage=None):  # items [("câu", True/False)]
    return dict(k="tf", zh=zh, vi=vi, items=items, passage=passage)
def opn(zh, vi, items, passage=None):  # items [("đề", "đáp án gợi ý")]
    return dict(k="open", zh=zh, vi=vi, items=items, passage=passage)

BL = re.compile(r'【([^】]*)】')
def build_test(parts):
    secs = []; ans = []; explain = {}; n = 0; no = 0
    for P in parts:
        no += 1; k = P["k"]; start = n + 1; p = dict(no=no, zh=P["zh"], vi=P["vi"])
        if P.get("passage"): p["passage"] = P["passage"]
        qs = []
        if k == "pool":
            p.update(type="pooltext", pool=P["pool"]);
            if P["inline"] and max(len(w) for w in P["pool"]) <= 6: p["inline"] = True
            else: p["long"] = True
            for it in P["items"]:
                ws = BL.findall(it); nums = list(range(n + 1, n + 1 + len(ws)))
                txt = it; full = BL.sub(lambda m: m.group(1), it)
                for j, w in enumerate(ws):
                    txt = txt.replace(f"【{w}】", "（　　）" if len(ws) == 1 else f"（ {nums[j]} ）", 1)
                for j, w in enumerate(ws):
                    n += 1; assert w in P["pool"], (w, P["pool"])
                    q = dict(n=n, text=txt if j == 0 else "")
                    if j: q["sub"] = f"Ô ({n}) trong câu {nums[0]} ở trên"
                    qs.append(q); ans.append(LT[P["pool"].index(w)]); explain[str(n)] = f"Đáp án: {w} → {full}"
        elif k == "match":
            p.update(type="pooltext", pool=P["pool"], long=True)
            for w, d in P["items"]:
                n += 1; qs.append(dict(n=n, text=w)); ans.append(LT[P["pool"].index(d)]); explain[str(n)] = f"{w} — {d}"
        elif k == "pick":
            p.update(type="choice")
            for opts, items in P["groups"]:
                for it in items:
                    w = BL.findall(it)[0]; n += 1
                    qs.append(dict(n=n, text=BL.sub("（　　）", it), opts=opts)); ans.append("ABC"[opts.index(w)])
                    explain[str(n)] = f"Đáp án: {w} → {BL.sub(lambda m: m.group(1), it)}"
        elif k == "pos":
            p.update(type="letters", letters="ABCD")
            for t, w, L in P["items"]:
                n += 1; qs.append(dict(n=n, text=f"{t}（{w}）")); ans.append(L)
                i = t.index(L); fixed = re.sub(r'[ABCD]', '', t[:i] + w + t[i + 1:])
                explain[str(n)] = f"“{w}” đặt ở vị trí {L}: {fixed}"
        elif k == "tf":
            p.update(type="tf")
            for t, ok in P["items"]:
                n += 1; qs.append(dict(n=n, text=t)); ans.append("A" if ok else "B"); explain[str(n)] = ("Đúng (对)." if ok else "Sai (错).") + (" " + P.get("why", {}).get(t, "") if P.get("why") else "")
        elif k == "open":
            p.update(type="open")
            for t, ref in P["items"]:
                n += 1; qs.append(dict(n=n, text=t, ref=ref)); ans.append("*")
        p["qs"] = qs
        p["vi"] = (f"Câu {start}–{n}: " if n > start else f"Câu {start}: ") + P["vi"]
        secs.append(p)
    return dict(answers="".join(ans), pinyin=True, gt=True, book=2,
                sections=[dict(zh="综合练习", vi="Bài tập tổng hợp", parts=secs)], explain=explain)

def build(n, D):
    texts = []
    for t in D["texts"]:
        texts.append(dict(t=t["t"], scene=t.get("scene", ""), scene_vi=t.get("scene_vi", ""), narr=t.get("narr", True), lines=t["lines"], q=t.get("q", [])))
    sents = [(l["zh"], l["vi"]) for t in texts for l in t["lines"]]
    gsents = []
    for g in D["grammar"]:
        for f in g.get("forms", []):
            for e in f["ex"]: gsents.append(("".join(c.replace("[", "").replace("]", "") for c in e["c"]) + e.get("end", ""), e["vi"]))
    vocab = []
    for v in D["vocab"]:
        if "ex" not in v:
            c = [s for s in sents + gsents if v["h"].split("（")[0].split("……")[0] in s[0]]
            c.sort(key=lambda s: (han(s[0]) > 28, han(s[0])))
            v["ex"] = [c[0][0], "", c[0][1]] if c else [v["h"], v["p"], v["vi"]]
        vocab.append(v)
    zhvi = [dict(zh=z, py="", vi=v) for z, v in sents if 4 <= han(z) <= 30][:14]
    speak = [dict(h=z, p="", vi=v) for z, v in sents + gsents if 4 <= han(z) <= 18][:14]
    vizh = []
    for z, v in gsents + sents:
        if not (4 <= han(z) <= 16): continue
        tok = seg(z)
        if 3 <= len(tok) <= 9 and z not in [x.get("_z") for x in vizh]:
            vizh.append(dict(vi=v, ans=tok, extra=[], alt=[], py="", _z=z))
        if len(vizh) >= 10: break
    for x in vizh: x.pop("_z")
    test = build_test(D["ex"])
    return vocab, zhvi, vizh, speak, texts, test

DICT = set()
PUN = re.compile(r'[，。？！、：；“”‘’"（）()\s…·,.?!—]')
def seg(s):
    s = PUN.sub('', s); out = []; i = 0
    while i < len(s):
        for l in range(min(5, len(s) - i), 0, -1):
            w = s[i:i + l]
            if l == 1 or w in DICT: out.append(w); i += l; break
    return out

def main():
    from gtdata import L as L1
    import gtdata2  # noqa: nạp bài 11–20 vào L1
    for k in L1:
        for v in L1[k]["vocab"]: DICT.add(v[0])
    DICT.update("我们 你们 他们 她们 什么 怎么 为什么 已经 现在 以后 以前 时候 一个 一些 这么 那么 可是 但是 所以 因为 虽然 如果 要是 喜欢 知道 觉得 告诉 朋友 中国 学校 同学 老师 晚上 早上 每天 今天 明天 昨天 东西 地方 问题 事情 自己 大家 一起 一定 应该 可以 没有 不是 还是 或者 这样 那样 生活 习惯 工作 学习 汉语 电脑 衣服 房间 宿舍 妈妈 爸爸 儿子 女儿 孩子 一点儿 有点儿 起来 出来 回来 进来 过来 下去 上去 出去 回去".split())
    B = {}
    for mod in ("gtb1", "gtb2", "gtb3", "gtb4", "gtb5"):
        try: m = importlib.import_module(mod)
        except ModuleNotFoundError: continue
        B.update(m.B)
    for k in B:
        for v in B[k]["vocab"]: DICT.add(v["h"])
    out = []; gram = {}
    for n in sorted(B):
        vocab, zhvi, vizh, speak, texts, test = build(n, B[n])
        out.append(f"const GB{n}_VOCAB={J(vocab)};\nconst GB{n}_ZHVI={J(zhvi)};\nconst GB{n}_VIZH={J(vizh)};\nconst GB{n}_SPEAK={J(speak)};\nconst GB{n}_TEXT={J(texts)};\nconst GB{n}_TEST={J(test)};")
        gram[n] = B[n]["grammar"]
        print(n, len(vocab), len(zhvi), len(vizh), len(speak), len(test["answers"]), test["answers"], file=sys.stderr)
    les = ",\n".join(f'   {n}:{{title:"Bài {n}",theme:"",zh:{J(B[n]["zh"])},vi:{J(B[n]["vi"])},intro:{J(B[n].get("intro", ""))},vocab:GB{n}_VOCAB,zhvi:GB{n}_ZHVI,vizh:GB{n}_VIZH,sentences:GB{n}_SPEAK,texts:GB{n}_TEXT,test:GB{n}_TEST,needPy:true}}' for n in sorted(B))
    js = "/* ===== 发展汉语·初级综合(II) Bài 1–10 – lớp Giao tiếp sơ cấp 2 (sinh từ _src/gt/gtb_gen.py) ===== */\n" + "\n".join(out) + f"\nconst GB_LESSONS1={{\n{les}\n}};\nconst GB_GRAMMAR1={J(gram)};\n"
    open('/tmp/claude-0/-home-claude/c42ce2af-05ed-5ab0-9ae7-40fe1ca5a6a5/scratchpad/gt/gb.js', 'w', encoding='utf-8').write(js)
    print("bytes", len(js.encode()), file=sys.stderr)

if __name__ == "__main__": main()
