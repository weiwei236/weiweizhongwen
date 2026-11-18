# Chèn phần "Tập viết" (hz.js, hz.css) vào src.html. Chạy lại được nhiều lần.
import os
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, '..', 'src.html')
s = open(P, encoding='utf-8').read()
rd = lambda f: open(os.path.join(D, f), encoding='utf-8').read()
def put(s, b, e, body, anchor):
    if b not in s:
        i = s.index(anchor); s = s[:i] + b + '\n' + e + '\n' + s[i:]
    i = s.index(b) + len(b); j = s.index(e)
    return s[:i] + '\n' + body + s[j:]
def once(s, old, new, mark):
    if mark in s: return s
    assert s.count(old) == 1, ('không tìm thấy duy nhất', old[:60]); return s.replace(old, new, 1)
s = put(s, '/* HZ_CSS_BEGIN */', '/* HZ_CSS_END */', rd('hz.css'), '/* TRIP_CSS_BEGIN */')
s = put(s, '/* HZ_JS_BEGIN */', '/* HZ_JS_END */', rd('hz.js'), '/* TRIP_JS_BEGIN */')
# biểu tượng bút
s = once(s, "  copy:'<svg", """  pen:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>',
  copy:'<svg""", "  pen:'<svg")
# tab Tập viết trong bài học (ngay sau Flashcard)
s = once(s, """<button role="tab" data-s="flash" aria-selected="${S.section==="flash"}">${ICON.cards}Flashcard</button>""",
         """<button role="tab" data-s="flash" aria-selected="${S.section==="flash"}">${ICON.cards}Flashcard</button>
      <button role="tab" data-s="write" aria-selected="${S.section==="write"}">${ICON.pen}Tập viết</button>""", 'data-s="write"')
s = once(s, 'else if(S.section==="gram") Grammar.mount(les); else Speak.mount(les);',
         'else if(S.section==="gram") Grammar.mount(les); else if(S.section==="write") Write.mount(les); else Speak.mount(les);', 'Write.mount(les)')
# nút "Cách viết" trên mặt sau flashcard
s = once(s, """<div class="mean">${esc(w.vi)}</div>
              <div class="ex">""", """<div class="mean">${esc(w.vi)}</div>
              <div class="ex">""".replace('<div class="ex">', '<button class="btn hz-fc" data-hzw="${esc(w.k)}">${ICON.pen}Xem cách viết</button>\n              <div class="ex">'), 'data-hzw=')
# nhật ký học tập cho giáo viên
s = once(s, 'exam: "Bài tập HSK", game: "Trò chơi" };', 'exam: "Bài tập HSK", game: "Trò chơi", write: "Tập viết" };', 'write: "Tập viết"')
s = once(s, '      case "quiz": return `${d.right}/${d.total} câu đúng`;', '      case "quiz": return `${d.right}/${d.total} câu đúng`;\n      case "write": return `${d.done}/${d.total} chữ đã viết đúng`;', 'case "write"')
open(P, 'w', encoding='utf-8').write(s); print('ok')
