"""Thêm mục Văn hoá (3 game lễ tết) vào trang chủ học viên. Chạy lại được nhiều lần."""
import os, re
D = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(D, "..", "src.html")
s = open(SRC, encoding="utf-8").read(); rd = lambda f: open(os.path.join(D, f), encoding="utf-8").read()
s = re.sub(r"/\* CUL_CSS_BEGIN \*/.*?/\* CUL_CSS_END \*/\n", "", s, flags=re.S)
s = re.sub(r"/\* CUL_JS_BEGIN \*/.*?/\* CUL_JS_END \*/\n", "", s, flags=re.S)
i = s.index("</style>"); s = s[:i] + "/* CUL_CSS_BEGIN */\n" + rd("cul.css") + "/* CUL_CSS_END */\n" + s[i:]
a = "const RdAdmin = {"; s = s.replace(a, "/* CUL_JS_BEGIN */\n" + rd("cul.js") + "/* CUL_JS_END */\n" + a, 1)
def rep(old, new):
    global s
    if new in s: return
    assert s.count(old) == 1, old[:80]; s = s.replace(old, new)
rep('''        <button class="btn farm-btn" id="hiFarm">''', '''        <button class="btn cul-btn" id="hiCul">🏮 Văn hoá TQ</button>
        <button class="btn farm-btn" id="hiFarm">''')
rep('''  $("#hiFarm").onclick=()=>Farm.open();''', '''  $("#hiFarm").onclick=()=>Farm.open();
  $("#hiCul").onclick=()=>Culture.open();''')
rep('''<button class="btn farm-btn" data-mb="hiFarm">''', '''<button class="btn cul-btn" data-mb="hiCul">🏮<span> Văn hoá</span></button><button class="btn farm-btn" data-mb="hiFarm">''')
open(SRC, "w", encoding="utf-8").write(s); print("ok")
