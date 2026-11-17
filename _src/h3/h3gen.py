# -*- coding: utf-8 -*-
# Sinh dữ liệu HSK 3 (新HSK教程3 + 学练手册) → scratchpad/h3/h3.js
# Mỗi bài: _src/h3/h3_NN.py định nghĩa B[n] (dùng DSL của gt/gtb_gen.py) – phiên âm câu để trống, web tự điền (needPy).
import json, re, sys, types, importlib, random, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'gt'))
sys.modules['gtb_ex'] = types.SimpleNamespace(EX={}); sys.modules['gtb_tr'] = types.SimpleNamespace(TR={})
import gtb_gen as G0
J = lambda o: json.dumps(o, ensure_ascii=False)
ANS = json.load(open(os.path.join(HERE, 'answers.json'), encoding='utf-8'))
AUDIO_PAGE = "https://hoanguchinesestation.com/tai-lieu/audio/audio-sbt-hsk-3-0-3"
def C3(s): return [x.strip() for x in s.split("|")]

def dlg(s):  # "A：…\nB：…" → lines
    out = []
    for ln in s.strip().split("\n"):
        m = re.match(r'^([AB男女问])[：:](.*)$', ln.strip())
        out.append([m.group(1), m.group(2).strip()] if m else ["", ln.strip()])
    return out

def build_test(n, T):
    A = ANS[str(n)]; ex = {}
    gl = T.get("gl", {})
    def g(k, lines):
        if str(k) in gl: ex[str(k)] = gl[str(k)]
    L1 = dict(no=1, zh="第一部分", vi="Câu 1–3: Nghe hội thoại, chọn hình phù hợp nhất. Mỗi câu nghe hai lần.", type="poolpics",
              pool=[f"h3_l{n}_{k}" for k in "ABCD"],
              example=dict(lines=[["男", "喂，请问张经理在吗？"], ["女", "他正在开会，您半个小时以后再打，好吗？"]], gloss="A lô, xin hỏi giám đốc Trương có đó không? — Anh ấy đang họp, nửa tiếng nữa anh gọi lại được không?", ans="D"),
              qs=[dict(n=k) for k in (1, 2, 3)])
    L2 = dict(no=2, zh="第二部分", vi="Câu 4–6: Nghe hội thoại, chọn đáp án đúng. Mỗi câu nghe hai lần.", type="choice",
              example=dict(lines=[["女", "我需要搬一些椅子到楼上办公室，你能来帮忙吗？"], ["男", "没问题，我再叫几个人来帮你。"], ["问", "他们要把椅子搬到哪儿？"]], gloss="Tôi cần chuyển ít ghế lên văn phòng trên lầu, anh giúp được không? — Không vấn đề, tôi gọi thêm vài người đến giúp. — Hỏi: Họ chuyển ghế đi đâu?",
                           opts=[["教室", "phòng học"], ["办公室", "văn phòng"], ["体育馆", "nhà thi đấu"]], ans="B"),
              qs=[dict(n=4 + i, opts=C3(o)) for i, o in enumerate(T["l2"])])
    L3 = dict(no=3, zh="第三部分", vi="Câu 7–10: Nghe một đoạn, chọn đáp án đúng. Mỗi câu nghe hai lần.", type="choice",
              example=dict(lines=[["", "那个年轻人刚来公司不久，很有工作热情，人也很聪明。"], ["问", "关于那个年轻人，可以知道什么？"]], gloss="Chàng trai trẻ ấy mới vào công ty chưa lâu, làm việc rất nhiệt tình, người cũng rất thông minh. — Hỏi: Về chàng trai, biết được điều gì?",
                           opts=[["很聪明", "rất thông minh"], ["是留学生", "là du học sinh"], ["爱踢足球", "thích đá bóng"]], ans="A"),
              qs=[dict(n=7 + i, opts=C3(o)) for i, o in enumerate(T["l3"])])
    EX1 = ("你知道怎么去国家图书馆吗？", "E", "Bạn có biết đi Thư viện Quốc gia thế nào không? → E: Tất nhiên. Mình đi xe buýt trước rồi đổi tàu điện ngầm.")
    EX2 = ("中间那双（　　）是谁的？", "E", "Đôi giày ở giữa là của ai?")
    pool1, ex1, qs1 = T["r1"] if len(T["r1"]) == 3 else (T["r1"][0], EX1, T["r1"][1])
    R1 = dict(no=1, zh="第一部分", vi="Câu 11–15: Ghép câu (chọn câu trả lời / câu tiếp theo phù hợp).", type="pooltext", long=True, pool=pool1,
              example=dict(lines=[["", ex1[0]]], gloss=ex1[2], ans=ex1[1]),
              qs=[dict(n=11 + i, text=q) for i, q in enumerate(qs1)])
    pool2, ex2, qs2 = T["r2"] if len(T["r2"]) == 3 else (T["r2"][0], EX2, T["r2"][1])
    R2 = dict(no=2, zh="第二部分", vi="Câu 16–20: Chọn từ thích hợp điền vào chỗ trống.", type="pooltext", inline=True, pool=pool2,
              example=dict(lines=[["", ex2[0]]], gloss=ex2[2], ans=ex2[1]), qs=[])
    for i, q in enumerate(qs2):
        d = dict(n=16 + i)
        if "\n" in q: d["lines"] = dlg(q)
        else: d["text"] = q
        R2["qs"].append(d)
    R3 = dict(no=3, zh="第三部分", vi="Câu 21–24: Đọc đoạn văn, chọn đáp án đúng.", type="choice",
              example=dict(lines=[["", "您是来参加今天会议的吗？您来早了一点儿，现在才八点半。您先进来坐吧。"], ["★", "会议最可能几点开始？"]], gloss="Anh đến dự cuộc họp hôm nay phải không? Anh đến hơi sớm, bây giờ mới 8 giờ rưỡi. Mời anh vào ngồi trước. — Cuộc họp có thể bắt đầu lúc mấy giờ?",
                           opts=[["8:00", ""], ["8:30", ""], ["9:00", ""]], ans="C"), qs=[])
    p21, q21, o21 = T["r3"][0]; p22, q22, o22 = T["r3"][1]; p23, (q23, o23), (q24, o24) = T["r3"][2]
    R3["qs"] = [dict(n=21, lines=[["", p21], ["★", q21]], opts=C3(o21)), dict(n=22, lines=[["", p22], ["★", q22]], opts=C3(o22)),
                dict(n=23, lines=[["", p23], ["★", q23]], opts=C3(o23)), dict(n=24, lines=[["★", q24]], sub="Dựa vào đoạn văn của câu 23.", opts=C3(o24))]
    W1 = dict(no=1, zh="第一部分", vi="Câu 25–27: Viết chữ Hán theo phiên âm (gõ 1 chữ vào ô).", type="write",
              example=dict(text="咱们一会儿（dǎ）车回家吧。", ans="打", gloss="Lát nữa chúng ta bắt xe về nhà nhé."),
              qs=[dict(n=25 + i, text=q) for i, q in enumerate(T["w1"])])
    W2 = dict(no=2, zh="第二部分", vi="Câu 28–30: Nhìn hình, dùng từ cho sẵn để đặt câu (tự luận – so với đáp án gợi ý).", type="open",
              example=dict(img="h3_wex", lines=[["Dùng từ", "开心"], ["", "他开心得跳起来了。"]], gloss="Cậu ấy vui đến mức nhảy cẫng lên."),
              qs=[dict(n=28 + i, img=f"h3_l{n}_w{i + 1}", lines=[["Dùng từ", w]], ref=r) for i, (w, r) in enumerate(T["w2"])])
    answers = A + "***"
    assert len(answers) == 30 and "?" not in answers, (n, answers)
    for k, v in T.get("gl", {}).items(): ex[str(k)] = v
    return dict(answers=answers, pinyin=True,
                audio=dict(page=AUDIO_PAGE, track=str(n), label=f"SBT HSK 3 · Bài {n}", main=f"audio/hsk3/{n}.mp3", parts={"1": "", "2": "", "3": ""}),
                sections=[dict(zh="一、听力", vi="Nghe hiểu", audio=True, parts=[L1, L2, L3]),
                          dict(zh="二、阅读", vi="Đọc hiểu", parts=[R1, R2, R3]),
                          dict(zh="三、书写", vi="Viết", parts=[W1, W2])],
                explain=ex)

def main():
    src = open(os.path.join(HERE, '..', 'gt', 'gtb_gen.py'), encoding='utf-8').read()
    for s in re.findall(r'DICT\.update\("([^"]+)"\.split\(\)\)', src): G0.DICT.update(s.split())
    B = {}
    for f in sorted(os.listdir(HERE)):
        if re.match(r'h3_\d\d\.py$', f): B.update(importlib.import_module(f[:-3]).B)
    for k in B:
        for v in B[k]["vocab"]: G0.DICT.add(v["h"])
    out = []; gram = {}
    for n in sorted(B):
        D = dict(B[n]); D["ex"] = []; D["vex"] = True
        vocab, zhvi, vizh, speak, texts, _t, trsort, trtype = G0.build(n + 300, D)
        for v in vocab:
            if not v.get("ex") or v["ex"][0] == v["h"]: print("  thiếu câu ví dụ:", n, v["h"], file=sys.stderr)
        test = build_test(n, D["test"])
        P = "H3L"
        out.append(f"const {P}{n}_VOCAB={J(vocab)};\nconst {P}{n}_ZHVI={J(zhvi)};\nconst {P}{n}_VIZH={J(vizh)};\nconst {P}{n}_SPEAK={J(speak)};\nconst {P}{n}_TEXT={J(texts)};\nconst {P}{n}_TEST={J(test)};\nconst {P}{n}_TR={J(dict(sort=trsort, type=trtype))};")
        ROLES = set("kw S V O A T P N D Nu M X kw2 B C Q O1 O2 S2 V1 V2".split())
        for g in B[n]["grammar"]:
            for f in g["forms"]:
                for r in f["slots"]: assert r[0] in ROLES, (n, g["id"], r)
        gram[n] = B[n]["grammar"]
        print(n, "vocab", len(vocab), "zhvi", len(zhvi), "vizh", len(vizh), "speak", len(speak), "sort", len(trsort), "type", len(trtype), file=sys.stderr)
    les = ",\n".join(f'   {n}:{{title:"Bài {n}",theme:"",zh:{J(B[n]["zh"])},vi:{J(B[n]["vi"])},intro:{J(B[n].get("intro", ""))},vocab:H3L{n}_VOCAB,zhvi:H3L{n}_ZHVI,vizh:H3L{n}_VIZH,sentences:H3L{n}_SPEAK,texts:H3L{n}_TEXT,test:H3L{n}_TEST,tr:H3L{n}_TR,needPy:true}}' for n in sorted(B))
    js = "/* ===== HSK 3 – 新HSK教程3 (sinh từ _src/h3/h3gen.py) ===== */\n" + "\n".join(out) + f"\nconst H3_LESSONS={{\n{les}\n}};\nconst H3_GRAMMAR={J(gram)};\n"
    open('/tmp/claude-0/-home-claude/c42ce2af-05ed-5ab0-9ae7-40fe1ca5a6a5/scratchpad/h3/h3.js', 'w', encoding='utf-8').write(js)
    print("bytes", len(js.encode()), "lessons", sorted(B), file=sys.stderr)
if __name__ == "__main__": main()
