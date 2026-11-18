# Tạo dữ liệu nét chữ cho phần "Tập viết" (Hanzi Writer).
#   python3 _src/hz/hz_build.py ĐƯỜNG_DẪN/hanzi-writer-data/data
# Đọc danh sách chữ theo cấp độ trong chars.json (lấy từ từ vựng các bài học) và ghi:
#   hz/hw.js            thư viện Hanzi Writer (MIT) đã build sẵn
#   hz/d_<cấp độ>.js     dữ liệu nét cho các chữ của cấp độ đó (HZ.add({...}))
# Dữ liệu nét: hanzi-writer-data (Arphic Public License, xem ARPHICPL.TXT).
# Khi thêm bài mới có chữ chưa có dữ liệu: cập nhật chars.json (chạy hz_chars.py) rồi chạy lại file này.
import json, os, re, sys, shutil
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '..', '..'))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(D, 'data')
OUT = os.path.join(ROOT, 'hz'); os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(D, 'hanzi-writer.min.js'), os.path.join(OUT, 'hw.js'))
for f in ('LICENSE-hanzi-writer.txt', 'ARPHICPL.TXT'): shutil.copyfile(os.path.join(D, f), os.path.join(OUT, f))
levels = json.load(open(os.path.join(D, 'chars.json'), encoding='utf-8'))
def comp(c):
    p = os.path.join(SRC, c + '.json')
    if not os.path.exists(p): return None
    d = json.load(open(p, encoding='utf-8'))
    return {'s': [re.sub(r' ?([MLQCZ]) ?', r'\1', x) for x in d['strokes']], 'm': d['medians']}
for lv, v in levels.items():
    chars = v['chars']
    if not chars: continue
    m = {c: comp(c) for c in chars}; miss = [c for c, x in m.items() if x is None]
    body = json.dumps({c: x for c, x in m.items() if x}, ensure_ascii=False, separators=(',', ':'))
    open(os.path.join(OUT, f'd_{lv}.js'), 'w', encoding='utf-8').write('HZ.add(' + body + ');\n')
    print(lv, len(chars), 'chữ', os.path.getsize(os.path.join(OUT, f'd_{lv}.js')) // 1024, 'KB', ('thiếu: ' + ''.join(miss)) if miss else '')
# Bộ thủ: mọi chữ xuất hiện trong _src/learn/bushou.js → hz/d_bushou.js
import re as _re
_s = open(os.path.join(D, '..', 'learn', 'bushou.js'), encoding='utf-8').read()
_cs = sorted(set(_re.findall(r'[⺀-⿟㐀-鿿]', _s)))
_m = {c: comp(c) for c in _cs}
open(os.path.join(OUT, 'd_bushou.js'), 'w', encoding='utf-8').write('HZ.add(' + json.dumps({c: x for c, x in _m.items() if x}, ensure_ascii=False, separators=(',', ':')) + ');\n')
print('bushou', len(_cs), 'chữ', 'thiếu: ' + ''.join(c for c, x in _m.items() if not x))
