"""Ghép _src/src.html + logo + ảnh đề thành index.html (trang Netlify).
Chạy:  python3 _src/build.py      (từ thư mục gốc của kho)
Tùy chọn: --artifact ĐƯỜNG_DẪN   ghi thêm bản không có <html>/<head> cho trang xem trước trên Claude."""
import base64, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
p = lambda *a: os.path.join(HERE, *a)
imgs = {}
for d in sorted(x for x in os.listdir(HERE) if x.startswith('ex') and os.path.isdir(p(x))):
    for f in sorted(os.listdir(p(d))):
        if f.endswith('.jpg'): imgs[f[:-4]] = 'data:image/jpeg;base64,' + base64.b64encode(open(p(d, f), 'rb').read()).decode()
s = open(p('src.html'), encoding='utf-8').read()
src = (s.replace('__LOGO__', open(p('logo.b64')).read().strip())
        .replace('__TEACHER_API__', open(p('teacher_api.txt')).read().strip())
        .replace('__EX_IMG__', 'const EX_IMG=' + json.dumps(imgs) + ';\n'))
head = '<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
k = src.index('<section id="scrWelcome"')
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(head + src[:k] + '</head>\n<body style="margin:0">\n' + src[k:] + '\n</body></html>')
if '--artifact' in sys.argv: open(sys.argv[sys.argv.index('--artifact') + 1], 'w', encoding='utf-8').write(src)
print('index.html', os.path.getsize(os.path.join(ROOT, 'index.html')), 'bytes')
