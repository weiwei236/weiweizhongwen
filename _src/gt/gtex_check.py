import sys, re; sys.path.insert(0, '/home/claude/weiweizhongwen/_src/gt')
import gtdata2
from gtdata import L
from gtex import EX
HAN = re.compile(r'[一-鿿]')
WL = set("阮明")
def allowed(n):
    s = set(WL)
    for k in L:
        if k <= n:
            for v in L[k]['vocab']: s |= set(HAN.findall(v[0]))
            for t in L[k]['texts']:
                for l in t['lines']: s |= set(HAN.findall(l[1]))
    return s
bad = 0
for n in sorted(EX):
    A = allowed(n); need = [v[0] for v in L[n]['vocab'] if len(v) < 5 and v[2] != 'rieng']
    miss = [w for w in need if w not in EX[n]]
    if miss: print(n, 'MISSING', miss)
    for w, (z, p, v) in EX[n].items():
        if w not in z and w not in ('打（电话）',): print(n, w, 'NOT IN SENTENCE', z)
        x = [c for c in HAN.findall(z) if c not in A]
        if x: bad += 1; print(n, w, z, 'NEW:', ''.join(x))
print('bad', bad)
