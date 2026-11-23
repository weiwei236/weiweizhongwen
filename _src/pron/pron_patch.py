"""Chèn phần Luyện ngữ âm (pron_data.js + pron.js + pron.css) vào src.html và nối tab / khu giáo viên. Chạy lại được nhiều lần."""
import os, re
D = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(D, "..", "src.html")
s = open(SRC, encoding="utf-8").read()
rd = lambda f: open(os.path.join(D, f), encoding="utf-8").read()
s = re.sub(r"/\* PRON_CSS_BEGIN \*/.*?/\* PRON_CSS_END \*/\n", "", s, flags=re.S)
s = re.sub(r"/\* PRON_JS_BEGIN \*/.*?/\* PRON_JS_END \*/\n", "", s, flags=re.S)
i = s.index("</style>"); s = s[:i] + "/* PRON_CSS_BEGIN */\n" + rd("pron.css") + "/* PRON_CSS_END */\n" + s[i:]
a = "const RdAdmin = {"; assert a in s
s = s.replace(a, "/* PRON_JS_BEGIN */\n" + rd("pron_data.js") + rd("pron.js") + "/* PRON_JS_END */\n" + a, 1)
def rep(old, new):
    global s
    if new in s: return
    assert s.count(old) == 1, old[:80]; s = s.replace(old, new)
# tab học viên
rep('''      <button role="tab" data-s="speak" aria-selected="${S.section==="speak"}">${ICON.mic}Phát âm</button>''',
    '''      ${Pron.has(S.level,S.lesson)?`<button role="tab" data-s="pron" aria-selected="${S.section==="pron"}">${ICON.mic}Luyện ngữ âm</button>`:""}
      <button role="tab" data-s="speak" aria-selected="${S.section==="speak"}">${ICON.mic}Phát âm</button>''')
rep('''  if(S.section==="text"&&!les.texts) S.section="flash";''',
    '''  if(S.section==="text"&&!les.texts) S.section="flash";
  if(S.section==="pron"&&!Pron.has(S.level,S.lesson)) S.section="flash"; Pron.stop();''')
rep('''  if(S.section==="text") TextView.mount(les); else''', '''  if(S.section==="pron") Pron.mount(les); else if(S.section==="text") TextView.mount(les); else''')
rep('''const SEC_NAME={text:"Bài khóa",''', '''const SEC_NAME={pron:"Luyện ngữ âm",text:"Bài khóa",''')
rep('''function stopAnyRecording(){ if(REC&&REC.stop) REC.stop(true); }''', '''function stopAnyRecording(){ if(REC&&REC.stop) REC.stop(true); if(typeof PronRec!=="undefined"&&PronRec.cur) PronRec.cancel(); }''')
# khu giáo viên
rep('''[["hv", "Học viên"], ["read", "Bài đọc"], ["kt", "Kiểm tra"]]''', '''[["hv", "Học viên"], ["read", "Bài đọc"], ["kt", "Kiểm tra"]].concat(PRON_ON ? [["na", "Ngữ âm"]] : [])''')
rep('''if(this.view === "read"){ RdAdmin.draft = null; RdAdmin.render(); } else if(this.view === "kt"){''', '''if(this.view === "read"){ RdAdmin.draft = null; RdAdmin.render(); } else if(this.view === "na"){ PronAdmin.subs = null; PronAdmin.refs = {}; PronAdmin.render(); } else if(this.view === "kt"){''')
rep('''this.view = b.dataset.tv; this.view === "read" ? RdAdmin.render() :''', '''this.view = b.dataset.tv; PronAdmin.stopRec(); PronPlayer.stop(); this.view === "read" ? RdAdmin.render() : this.view === "na" ? PronAdmin.render() :''')
rep('''    if(this.view === "read") return RdAdmin.render();\n    if(this.view === "kt") return KTA.render();''', '''    if(this.view === "read") return RdAdmin.render();\n    if(this.view === "na" && !PRON_ON) this.view = "hv";\n    if(this.view === "na") return PronAdmin.render();\n    if(this.view === "kt") return KTA.render();''')
rep("    const stream=await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:true,noiseSuppression:true}});", "    const stream=await pickMic({echoCancellation:true,noiseSuppression:true});")
rep("  async mp3(f32, rate){", "  async mp3(f32, rate, kbps){")
rep("new lamejs.Mp3Encoder(1, rate, 96)", "new lamejs.Mp3Encoder(1, rate, kbps || 96)")
open(SRC, "w", encoding="utf-8").write(s); print("ok")
