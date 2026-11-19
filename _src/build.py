"""Ghép _src/src.html + logo + ảnh đề thành index.html (trang Netlify).
Chạy:  python3 _src/build.py      (từ thư mục gốc của kho)
Tùy chọn: --artifact ĐƯỜNG_DẪN   ghi thêm bản không có <html>/<head> cho trang xem trước trên Claude."""
import base64, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
p = lambda *a: os.path.join(HERE, *a)
import shutil
imgs = {}; imgs2 = {}
os.makedirs(os.path.join(ROOT, 'img', 'hsk2'), exist_ok=True); os.makedirs(os.path.join(ROOT, 'img', 'hsk1'), exist_ok=True); os.makedirs(os.path.join(ROOT, 'img', 'hsk3'), exist_ok=True); os.makedirs(os.path.join(ROOT, 'img', 'hsk4'), exist_ok=True)
for d in sorted(x for x in os.listdir(HERE) if x.startswith('ex') and os.path.isdir(p(x))):
    for f in sorted(os.listdir(p(d))):
        if not f.endswith('.jpg'): continue
        uri = 'data:image/jpeg;base64,' + base64.b64encode(open(p(d, f), 'rb').read()).decode()
        if d.startswith('ex4_'):   # ảnh 看图造句 HSK 4 → img/hsk4
            imgs2[f[:-4]] = uri; shutil.copyfile(p(d, f), os.path.join(ROOT, 'img', 'hsk4', f))
        elif d.startswith('ex3_'):   # ảnh sách bài tập HSK 3 → img/hsk3
            imgs2[f[:-4]] = uri; shutil.copyfile(p(d, f), os.path.join(ROOT, 'img', 'hsk3', f))
        elif d.startswith('ex2_') or d.startswith('exs1_'):   # ảnh sách bài tập: để thành file riêng img/hsk2, img/hsk1 cho trang nhẹ
            imgs2[f[:-4]] = uri; shutil.copyfile(p(d, f), os.path.join(ROOT, 'img', 'hsk2' if d.startswith('ex2_') else 'hsk1', f))
        else: imgs[f[:-4]] = uri
s = open(p('src.html'), encoding='utf-8').read()
src = (s.replace('__LOGO__', open(p('logo.b64')).read().strip())
        .replace('__TEACHER_API__', open(p('teacher_api.txt')).read().strip())
        )
art = src.replace('__EX_IMG__', 'const EX_IMG=' + json.dumps({**imgs, **imgs2}) + ';\n')
# index.html (GitHub Pages): ảnh để thành file riêng cho trang nhẹ; bản xem trước (--artifact) vẫn nhúng ảnh
os.makedirs(os.path.join(ROOT, 'img', 'ex'), exist_ok=True)
exmap = {}
for d in sorted(x for x in os.listdir(HERE) if x.startswith('ex') and os.path.isdir(p(x)) and not (x.startswith('ex2_') or x.startswith('ex3_') or x.startswith('ex4_') or x.startswith('exs1_'))):
    for f in sorted(os.listdir(p(d))):
        if f.endswith('.jpg'): shutil.copyfile(p(d, f), os.path.join(ROOT, 'img', 'ex', f)); exmap[f[:-4]] = 'img/ex/' + f
src = src.replace('__EX_IMG__', 'const EX_IMG=' + json.dumps(exmap) + ';\n')
import re
def files_js(var, sub):
    global src
    d = os.path.join(HERE, 'trip', sub); out = os.path.join(ROOT, 'trip', sub); os.makedirs(out, exist_ok=True); m = {}
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith('.webp'): shutil.copyfile(os.path.join(d, f), os.path.join(out, f)); m[f[:-5]] = 'trip/' + sub + '/' + f
    global art
    for nm in ('src', 'art'):
        t = globals()[nm]; i = t.find('const ' + var + '=')
        if i >= 0: j = t.index(';\n', i); globals()[nm] = t[:i] + 'const ' + var + '=' + json.dumps(m) + t[j:]
files_js('TRIP_IMG_DATA', 'img'); files_js('TRIP_GD_DATA', 'gd')
head = '<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
k = src.index('<section id="scrWelcome"')
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(head + src[:k] + '</head>\n<body style="margin:0">\n' + src[k:] + '\n</body></html>')
if '--artifact' in sys.argv: open(sys.argv[sys.argv.index('--artifact') + 1], 'w', encoding='utf-8').write(art)
print('index.html', os.path.getsize(os.path.join(ROOT, 'index.html')), 'bytes')
