# Lấy danh sách chữ Hán trong từ vựng của từng cấp độ từ index.html đã build → chars.json
#   python3 _src/build.py && python3 _src/hz/hz_chars.py
import json, os
from playwright.sync_api import sync_playwright
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(D, '..', '..'))
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
    pg.goto('file://' + os.path.join(ROOT, 'index.html')); pg.wait_for_timeout(1500)
    r = pg.evaluate("""(()=>{const o={};for(const [k,L] of Object.entries(LEVELS)){const s=new Set();const ls=L.lessons||{};
      for(const n in ls){const les=ls[n];if(!les||!les.vocab)continue;for(const w of les.vocab)for(const c of (w.h||''))if(/[\\u4e00-\\u9fff]/.test(c))s.add(c);}
      o[k]={name:L.name,n:Object.keys(ls).length,chars:[...s].join('')};}return o;})()""")
    json.dump(r, open(os.path.join(D, 'chars.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    for k, v in r.items(): print(k, v['name'], len(v['chars']), 'chữ')
