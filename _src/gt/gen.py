import json, random, re, sys
sys.path.insert(0, '/home/claude/weiweizhongwen/_src/gt')
import gtdata2
from gtdata import L
from gtex import EX as GEX
J = lambda o: json.dumps(o, ensure_ascii=False)
HAN = re.compile(r'[一-鿿〇]')
PUN = re.compile(r'[，。？！、：；“”（）()\s…·,.?!]')
def han(s): return len(HAN.findall(s))

def sents(n):  # (zh, py, vi, kind)
    out = []
    for t in L[n]['texts']:
        for who, zh, py, vi in t['lines']: out.append((zh, py, vi, 'line'))
        for q in t.get('q', []): out += [(q[0], q[1], '', 'q'), (q[2], '', q[3], 'a')]
    for b in L[n].get('bank', []): out.append((b[0], b[1], b[2], 'bank'))
    return out

DICT = set()
EXTRA_WORDS = "我们 你们 他们 什么 名字 老师 同学 中国 美国 哪国 留学生 一个 两个 一共 多少 早上 下午 晚上 上午 每天 图书馆 教学 一楼 怎么样 星期 几号 一起 一下 一点儿 哪儿 那儿 这儿 不是 没有 电子词典 学习 认识 高兴 法国 泰国 韩国 日本 汉语 英语 法语 九月 十月 十号 二十八 号 块 毛 斤 个 口 人 的 了 吗 呢 吧 也 很 都 不 和 在 有 是 去 买 要 叫 姓 说 看 喝 吃 请 想 做 对 好 太".split()
def dict_upto(n):
    d = set(EXTRA_WORDS)
    for k in L:
        if k <= n:
            for v in L[k]['vocab']: d.add(v[0])
            for t in L[k]['texts']:
                for who, *_ in t['lines']:
                    if who: d.add(who)
    return d
def seg(s, d):
    s = PUN.sub('', s); out = []; i = 0
    while i < len(s):
        for l in range(min(6, len(s) - i), 0, -1):
            w = s[i:i+l]
            if l == 1 or w in d: out.append(w); i += l; break
    # gộp số đếm liên tiếp kiểu 二十八 / 七百八十
    return out

EXS={"马丁":("马丁是美国人。","Mǎdīng shì Měiguó rén.","Martin là người Mỹ."),"林娜":("林娜是法国人。","Línnà shì Fǎguó rén.","Linna là người Pháp."),
 "李一民":("李一民是老师。","Lǐ Yīmín shì lǎoshī.","Lý Nhất Dân là giáo viên."),"阿明":("阿明是泰国人。","Āmíng shì Tàiguó rén.","A Minh là người Thái Lan."),
 "崔浩":("崔浩是韩国人。","Cuī Hào shì Hánguó rén.","Thôi Hạo là người Hàn Quốc."),"营业员":("她是营业员。","Tā shì yíngyèyuán.","Cô ấy là nhân viên bán hàng."),
 "教学楼":("这是教学楼。","Zhè shì jiàoxuélóu.","Đây là tòa giảng đường."),"星期一":("今天星期一。","Jīntiān xīngqīyī.","Hôm nay thứ Hai."),
 "星期三":("明天星期三。","Míngtiān xīngqīsān.","Ngày mai thứ Tư."),"星期四":("星期四我有课。","Xīngqīsì wǒ yǒu kè.","Thứ Năm tôi có tiết học."),
 "星期六":("星期六我不上课。","Xīngqīliù wǒ bú shàng kè.","Thứ Bảy tôi không đi học."),"没有":("我没有电脑。","Wǒ méiyǒu diànnǎo.","Tôi không có máy tính.")}
def build(n):
    D = L[n]; rnd = random.Random(n * 7)
    allS = sents(n); prevS = [s for k in L if k < n for s in sents(k)]
    vocab = []; miss = []
    for v in D['vocab']:
        h, p, pos, vi = v[:4]; ex = GEX.get(n, {}).get(h) or (v[4] if len(v) > 4 else None)
        if not ex and h in EXS: ex = EXS[h]
        if not ex:
            cand = [s for s in allS + prevS if h in s[0] and s[1] and s[2]]
            cand.sort(key=lambda s: (s[3] != 'line', han(s[0])))
            if cand: ex = cand[0][:3]
        if not ex: miss.append(h); ex = (h, p, vi)
        vocab.append(dict(h=h, p=p, pos=pos, vi=vi, ex=list(ex)))
    good = [s for s in allS if s[1] and s[2] and han(s[0]) >= 3 and s[3] in ('line', 'bank')]
    seen = set(); uniq = []
    for s in good:
        if s[0] not in seen: seen.add(s[0]); uniq.append(s)
    zhvi = [dict(zh=s[0], py=s[1], vi=s[2]) for s in uniq[:12]]
    d = dict_upto(n); vizh = []
    words = [v['h'] for v in vocab if v['pos'] != 'rieng']
    for s in uniq:
        tok = seg(s[0], d)
        if not (2 <= len(tok) <= 9): continue
        ex2 = [w for w in rnd.sample(words, min(len(words), 6)) if w not in tok][:2]
        vizh.append(dict(vi=s[2], ans=tok, extra=ex2, alt=[], py=s[1]))
        if len(vizh) >= 10: break
    speak = [dict(h=s[0], p=s[1], vi=s[2]) for s in uniq if han(s[0]) <= 16][:12]
    # ---- bài tập ----
    secs = []; answers = []; explain = {}; num = 0
    # P1: chọn từ điền chỗ trống
    pool = []; qs1 = []
    cands = [v for v in vocab if v['pos'] not in ('rieng',) and len(v['h']) >= 1]
    rnd.shuffle(cands)
    used = set(); usedS = set()
    for v in cands:
        if len(pool) >= 5: break
        h = v['h']
        if any(h in u or u in h for u in used): continue
        ss = [s for s in uniq + [x for x in allS if x[3] == 'bank'] if h in s[0] and s[0].count(h) == 1 and han(s[0]) - len(h) >= 2]
        ss = [s for s in ss if not any(o['h'] != h and h in o['h'] and o['h'] in s[0] for o in vocab)]
        ss = [s for s in ss if s[0] not in usedS and not any(u in s[0] for u in used)]
        if not ss: continue
        s = rnd.choice(ss); usedS.add(s[0]); used.add(h); pool.append(h); qs1.append((s[0].replace(h, '（　　）'), h, s[2]))
    if len(pool) >= 3:
        order = pool[:]; rnd.shuffle(order); qs = []
        for t, h, vi in qs1:
            num += 1; qs.append(dict(n=num, text=t)); answers.append('ABCDE'[order.index(h)]); explain[str(num)] = f"Điền “{h}”: {vi}"
        secs.append(dict(no=1, zh="一、选词填空", vi=f"Câu 1–{num}: Chọn từ thích hợp điền vào chỗ trống.", type="pooltext", inline=True, pool=order, qs=qs))
    # P2: chọn câu trả lời phù hợp
    pairs = []
    for t in D['texts']:
        ln = t['lines']
        for i in range(len(ln) - 1):
            a, b = ln[i], ln[i + 1]
            if a[0] and b[0] and a[0] != b[0] and a[1].endswith('？'): pairs.append((a[1], b[1], a[3], b[3]))
    for q in [q for t in D['texts'] for q in t.get('q', [])]:
        pairs.append((q[0], q[2], q[3], q[3]))
    seenA = set(); P = []
    for p in pairs:
        if p[1] in seenA or p[0] in [x[0] for x in P]: continue
        seenA.add(p[1]); P.append(p)
    rnd.shuffle(P); P = P[:5]
    if len(P) >= 3:
        start = num + 1; order = [p[1] for p in P]; rnd.shuffle(order); qs = []
        for p in P:
            num += 1; qs.append(dict(n=num, text=p[0])); answers.append('ABCDE'[order.index(p[1])]); explain[str(num)] = f"“{p[0]}” → “{p[1]}” ({p[3]})"
        secs.append(dict(no=2, zh="二、选择合适的回答", vi=f"Câu {start}–{num}: Chọn câu trả lời phù hợp với mỗi câu hỏi.", type="pooltext", long=True, pool=order, qs=qs))
    # P3: đọc hiểu bài khóa
    start = num + 1; qs = []
    for q, py, opts, ok in D['quiz']:
        o = opts[:]; rnd.shuffle(o); num += 1
        qs.append(dict(n=num, text=q, opts=o)); answers.append('ABC'[o.index(opts[ok])]); explain[str(num)] = f"Theo bài khóa: {opts[ok]}"
    secs.append(dict(no=3, zh="三、根据课文选择正确答案", vi=f"Câu {start}–{num}: Dựa vào bài khóa, chọn đáp án đúng.", type="choice", qs=qs))
    test = dict(answers=''.join(answers), pinyin=True, gt=True, sections=[dict(zh="综合练习", vi="Bài tập tổng hợp", parts=secs)], explain=explain)
    texts = [dict(t=t['t'], scene=t.get('scene', ''), scene_vi=t.get('scene_vi', ''), narr=t.get('narr', False),
                  lines=[dict(who=w, zh=z, py=p, vi=v) for w, z, p, v in t['lines']],
                  q=[dict(zh=a, py=b, ans=c, vi=d) for a, b, c, d in t.get('q', [])]) for t in D['texts']]
    return vocab, zhvi, vizh, speak, texts, test, miss

out = []; gram = {}
for n in sorted(L):
    vocab, zhvi, vizh, speak, texts, test, miss = build(n)
    if miss: print('MISS', n, miss, file=sys.stderr)
    out.append(f"const GT{n}_VOCAB={J(vocab)};\nconst GT{n}_ZHVI={J(zhvi)};\nconst GT{n}_VIZH={J(vizh)};\nconst GT{n}_SPEAK={J(speak)};\nconst GT{n}_TEXT={J(texts)};\nconst GT{n}_TEST={J(test)};")
    gram[n] = L[n]['grammar']
    print(n, len(vocab), len(zhvi), len(vizh), len(speak), test['answers'], file=sys.stderr)
def les(ns): return ",\n".join(f'   {n}:{{title:"Bài {n}",theme:"",zh:{J(L[n]["zh"])},vi:{J(L[n]["vi"])},vocab:GT{n}_VOCAB,zhvi:GT{n}_ZHVI,vizh:GT{n}_VIZH,sentences:GT{n}_SPEAK,texts:GT{n}_TEXT,test:GT{n}_TEST}}' for n in ns)
A=[n for n in sorted(L) if n<=10]; B=[n for n in sorted(L) if 11<=n<=20]
js = "/* ===== 发展汉语·初级综合(I) – lớp Giao tiếp ===== */\n" + "\n".join(out) + f"\nconst GT_LESSONS1={{\n{les(A)}\n}};\nconst GT_GRAMMAR1={J({n:gram[n] for n in A})};\nconst GT_LESSONS2={{\n{les(B)}\n}};\nconst GT_GRAMMAR2={J({n:gram[n] for n in B})};\n"
open('/tmp/claude-0/-home-claude/c42ce2af-05ed-5ab0-9ae7-40fe1ca5a6a5/scratchpad/gt/gt.js', 'w', encoding='utf-8').write(js)
print(len(js), file=sys.stderr)
for n in (1, 12):
    v, z, vz, sp, tx, te, _ = build(n)
    print(n, [x['ans'] for x in vz][:6], file=sys.stderr)
