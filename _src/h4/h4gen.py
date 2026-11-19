# -*- coding: utf-8 -*-
# Sinh dữ liệu HSK 4上 (新HSK教程4上) → scratchpad/h4/h4.js
# Mỗi bài: _src/h4/h4_NN.py định nghĩa B[n] (DSL của gt/gtb_gen.py). Bài tập lấy từ 综合练习 của sách (ex=[...]).
import json, re, sys, types, importlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'gt'))
sys.modules['gtb_ex'] = types.SimpleNamespace(EX={}); sys.modules['gtb_tr'] = types.SimpleNamespace(TR={})
import gtb_gen as G0
J = lambda o: json.dumps(o, ensure_ascii=False)
OUT = '/tmp/claude-0/-home-claude/c42ce2af-05ed-5ab0-9ae7-40fe1ca5a6a5/scratchpad/h4/h4.js'

def main():
    src = open(os.path.join(HERE, '..', 'gt', 'gtb_gen.py'), encoding='utf-8').read()
    for s in re.findall(r'DICT\.update\("([^"]+)"\.split\(\)\)', src): G0.DICT.update(s.split())
    # thêm từ vựng HSK3 để tách câu tốt hơn
    for v in re.findall(r'^([^|\n]{1,5})\|[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü ]+\|', open(os.path.join(HERE, '..', 'h3', 'h3_01.py'), encoding='utf-8').read(), re.M): G0.DICT.add(v)
    B = {}
    for f in sorted(os.listdir(HERE)):
        if re.match(r'h4_\d\d\.py$', f): B.update(importlib.import_module(f[:-3]).B)
    import h4_prac, h4b_prac; h4_prac.attach(B)
    for k in B:
        for v in B[k]["vocab"]: G0.DICT.add(v["h"])
    out = []; gram = {}
    ROLES = set("kw S V O A T P N D Nu M X kw2 B C Q O1 O2 S2 V1 V2".split())
    for n in sorted(B):
        D = dict(B[n]); D["vex"] = True
        vocab, zhvi, vizh, speak, texts, test, trsort, trtype = G0.build(n + 400, D)
        test.pop("book", None)
        # HSK4 câu dài: bổ sung Việt→Trung từ câu ví dụ từ vựng + câu ngữ pháp ngắn
        have = set("".join(x["ans"]) for x in vizh)
        cand = [(v["ex"][0], v["ex"][2]) for v in vocab if v.get("ex")]
        for g in B[n]["grammar"]:
            for f in g["forms"]:
                for e in f["ex"]: cand.append(("".join(c.replace("[", "").replace("]", "") for c in e["c"]) + e.get("end", ""), e["vi"]))
        for z, v in cand:
            if len(vizh) >= 12: break
            hz = len(re.findall(r'[\u4e00-\u9fff]', z)); tok = G0.merge(G0.seg(z))
            if 5 <= hz <= 16 and 3 <= len(tok) <= 9 and G0.PUN.sub("", z) not in have:
                vizh.append(dict(vi=v, ans=tok, extra=[], alt=[], py="")); have.add(G0.PUN.sub("", z))
        for v in vocab:
            if not v.get("ex") or v["ex"][0] == v["h"]: print("  thiếu câu ví dụ:", n, v["h"], file=sys.stderr)
        P = "H4L"
        out.append(f"const {P}{n}_VOCAB={J(vocab)};\nconst {P}{n}_ZHVI={J(zhvi)};\nconst {P}{n}_VIZH={J(vizh)};\nconst {P}{n}_SPEAK={J(speak)};\nconst {P}{n}_TEXT={J(texts)};\nconst {P}{n}_TEST={J(test)};\nconst {P}{n}_TR={J(dict(sort=trsort, type=trtype))};")
        for g in B[n]["grammar"]:
            for f in g["forms"]:
                for r in f["slots"]: assert r[0] in ROLES, (n, g["id"], r)
        gram[n] = B[n]["grammar"]
        print(n, "vocab", len(vocab), "zhvi", len(zhvi), "vizh", len(vizh), "speak", len(speak), "sort", len(trsort), "type", len(trtype), "bt", len(test["answers"]), file=sys.stderr)
    les = ",\n".join(f'   {n}:{{title:"Bài {n}",theme:"",zh:{J(B[n]["zh"])},vi:{J(B[n]["vi"])},intro:{J(B[n].get("intro", ""))},vocab:H4L{n}_VOCAB,zhvi:H4L{n}_ZHVI,vizh:H4L{n}_VIZH,sentences:H4L{n}_SPEAK,texts:H4L{n}_TEXT,test:H4L{n}_TEST,tr:H4L{n}_TR,needPy:true}}' for n in sorted(B))
    js = "/* ===== HSK 4上 – 新HSK教程4上 (sinh từ _src/h4/h4gen.py) ===== */\n" + "\n".join(out) + f"\nconst H4_LESSONS={{\n{les}\n}};\nconst H4_GRAMMAR={J(gram)};\n"
    open(OUT, 'w', encoding='utf-8').write(js)
    print("bytes", len(js.encode()), "lessons", sorted(B), file=sys.stderr)
if __name__ == "__main__": main()
