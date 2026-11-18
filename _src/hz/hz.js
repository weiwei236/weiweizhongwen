/* ======================= TẬP VIẾT 写汉字 – thứ tự nét & luyện viết theo nét =======================
   Thư viện Hanzi Writer (MIT) + dữ liệu nét hanzi-writer-data (Arphic PL) để trong thư mục hz/,
   chỉ tải khi học viên mở phần Tập viết (hz/hw.js và hz/d_<cấp độ>.js). */
const HZ = {
  d: {}, p: {},
  add(o){ Object.assign(this.d, o); },
  script(src){ return new Promise((ok, no) => { const s = document.createElement("script"); s.src = src; s.onload = ok; s.onerror = no; document.head.appendChild(s); }); },
  lib(){ return this.p._lib || (this.p._lib = (window.HanziWriter ? Promise.resolve() : this.script("hz/hw.js")).catch(e => { delete this.p._lib; throw e; })); },
  level(lv){ return this.p[lv] || (this.p[lv] = this.script(`hz/d_${lv}.js`).catch(e => { delete this.p[lv]; throw e; })); },
  async get(c){
    if(!this.d[c]){ try{ await this.level(S.level); }catch(e){}
      for(const lv of Object.keys(LEVELS)) { if(this.d[c]) break; try{ await this.level(lv); }catch(e){} } }
    const x = this.d[c]; if(!x) throw new Error("no data: " + c);
    return { strokes: x.s, medians: x.m };
  },
  has(c){ return !!this.d[c]; },
  isHan: c => /[一-鿿]/.test(c)
};
/* Hình mỗi bước của thứ tự nét (dùng chung với bảng 笔顺) */
function hzStepsSVG(c, size = 46){
  const x = HZ.d[c]; if(!x) return "";
  return x.s.map((_, k) => `<figure class="hz-step"><svg viewBox="0 0 1024 1024" width="${size}" height="${size}" aria-hidden="true">${HZ_GRID_SVG}
    <g transform="scale(1,-1) translate(0,-900)">${x.s.map((p, i) => i <= k ? `<path d="${p}" fill="${i === k ? "#C2513A" : "#3B4F45"}"/>` : "").join("")}</g></svg><figcaption>${k + 1}</figcaption></figure>`).join("");
}
const HZ_GRID_SVG = `<g fill="none" stroke="#E7B3A8" stroke-width="8" stroke-dasharray="26 22"><path d="M0 512H1024M512 0V1024"/><path d="M0 0 1024 1024M1024 0 0 1024" opacity=".55"/></g><rect x="4" y="4" width="1016" height="1016" fill="none" stroke="#D9867A" stroke-width="10"/>`;

const Write = {
  mode: store.get("ww_hz_mode", "anim"), speed: store.get("ww_hz_speed", 1), wi: 0, ci: 0, writer: null, tok: 0, extra: null,
  MODES: [["anim", "Xem thứ tự nét"], ["step", "Từng nét"], ["trace", "Tập tô"], ["free", "Tự viết"]],
  mount(les){
    this.les = les; this.key = `ww_hz_${S.level}_${S.lesson}`; this.rec = store.get(this.key, {});
    this.words = les.vocab.map(w => ({ w, cs: [...w.h].filter(HZ.isHan) })).filter(x => x.cs.length);
    if(this.jumpTo){ const i = this.words.findIndex(x => x.w.k === this.jumpTo || x.w.h === this.jumpTo); if(i >= 0){ this.wi = i; this.ci = 0; } this.jumpTo = null; }
    if(this.wi >= this.words.length){ this.wi = 0; this.ci = 0; }
    this.extra = null; this.render();
  },
  jump(k){ this.jumpTo = k; this.wi = 0; this.ci = 0; S.section = "write"; store.set("ww_section", "write"); renderLesson(); window.scrollTo({ top: 0, behavior: "smooth" }); },
  allChars(){ return [...new Set(this.words.flatMap(x => x.cs))]; },
  cur(){ return this.extra || this.words[this.wi]; },
  ch(){ const c = this.cur(); return c ? c.cs[Math.min(this.ci, c.cs.length - 1)] : ""; },
  size(){ const w = ($("#hzBoard") || {}).clientWidth || 300; return Math.max(220, Math.min(340, w)); },
  render(){
    const W = $("#work"); if(!W) return;
    if(!this.words.length){ W.innerHTML = `<div class="empty"><span class="han">写</span><b>Bài này chưa có từ để tập viết.</b></div>`; return; }
    const all = this.allChars(), done = all.filter(c => this.rec[c] != null).length;
    W.innerHTML = `
    <div class="toolbar">
      <div class="seg hz-modes" role="group" aria-label="Chế độ">${this.MODES.map(([k, t]) => `<button data-m="${k}" aria-pressed="${this.mode === k}">${t}</button>`).join("")}</div>
      <div class="grp"><span class="hz-tl">Tốc độ</span><div class="seg" role="group" aria-label="Tốc độ">${[[0.5, "Chậm"], [1, "Vừa"], [1.8, "Nhanh"]].map(([v, t]) => `<button data-sp="${v}" aria-pressed="${this.speed === v}">${t}</button>`).join("")}</div></div>
    </div>
    <div class="fc-stage hz-stage">
      <div class="hz-main">
        <div class="hz-word" id="hzWord"></div>
        <div class="hz-boardwrap">
          <button class="btn hz-nav" id="hzPrev" aria-label="Chữ trước">${ICON.left}</button>
          <div class="hz-board" id="hzBoard"><svg class="hz-grid" viewBox="0 0 1024 1024" aria-hidden="true">${HZ_GRID_SVG}</svg><div id="hzW" class="hz-w"></div><div class="hz-load" id="hzLoad">Đang tải nét chữ…</div></div>
          <button class="btn hz-nav" id="hzNext" aria-label="Chữ sau">${ICON.right}</button>
        </div>
        <div class="hz-msg" id="hzMsg" aria-live="polite"></div>
        <div class="hz-ctrl" id="hzCtrl"></div>
        <div class="hz-steps-wrap"><h3><span class="han">笔顺</span> Thứ tự nét <span class="hz-cnt" id="hzCnt"></span></h3><div class="hz-steps" id="hzSteps"></div></div>
      </div>
      <aside class="side">
        <h3>Tiến độ tập viết</h3>
        <div class="meter"><i style="width:${all.length ? done / all.length * 100 : 0}%"></i></div>
        <div class="stat"><span>Chữ đã viết đúng</span><b>${done} / ${all.length}</b></div>
        <h3>Từ trong bài</h3>
        <div class="wordgrid hz-words">${this.words.map((x, i) => `<button data-wi="${i}" class="${!this.extra && i === this.wi ? "cur" : x.cs.every(c => this.rec[c] != null) ? "k" : ""}" title="${esc(x.w.vi)}">${esc(x.w.h)}</button>`).join("")}</div>
        <h3>Luyện chữ bất kỳ</h3>
        <form class="hz-free" id="hzFree"><input class="inp" id="hzIn" maxlength="8" placeholder="Gõ chữ Hán…" aria-label="Gõ chữ Hán muốn luyện" lang="zh"><button class="btn" type="submit">Viết</button></form>
        <ul class="hz-tips">
          <li><b>Xem thứ tự nét:</b> xem chữ được viết từng nét theo đúng thứ tự.</li>
          <li><b>Từng nét:</b> bấm “Nét tiếp” để xem lần lượt từng nét.</li>
          <li><b>Tập tô:</b> tô theo chữ mờ. Viết sai 2 lần, nét đúng sẽ nhấp nháy gợi ý.</li>
          <li><b>Tự viết:</b> viết không có chữ mờ, sai 3 lần mới có gợi ý.</li>
        </ul>
      </aside>
    </div>`;
    W.querySelectorAll("[data-m]").forEach(b => b.onclick = () => { this.mode = b.dataset.m; store.set("ww_hz_mode", this.mode); this.render(); });
    W.querySelectorAll("[data-sp]").forEach(b => b.onclick = () => { this.speed = +b.dataset.sp; store.set("ww_hz_speed", this.speed); W.querySelectorAll("[data-sp]").forEach(x => x.setAttribute("aria-pressed", x === b)); this.draw(); });
    W.querySelectorAll("[data-wi]").forEach(b => b.onclick = () => { this.extra = null; this.wi = +b.dataset.wi; this.ci = 0; this.render(); });
    $("#hzPrev").onclick = () => this.move(-1); $("#hzNext").onclick = () => this.move(1);
    $("#hzFree").onsubmit = e => { e.preventDefault(); const cs = [...$("#hzIn").value].filter(HZ.isHan); if(!cs.length) return; this.extra = { w: { h: cs.join(""), p: "", vi: "", k: "" }, cs, free: true }; this.ci = 0; this.render(); };
    this.draw();
  },
  move(d){
    const c = this.cur(); this.ci += d;
    if(this.ci >= c.cs.length){ if(this.extra){ this.ci = 0; } else { this.wi = (this.wi + 1) % this.words.length; this.ci = 0; } return this.render(); }
    if(this.ci < 0){ if(this.extra){ this.ci = c.cs.length - 1; } else { this.wi = (this.wi - 1 + this.words.length) % this.words.length; this.ci = this.words[this.wi].cs.length - 1; } return this.render(); }
    this.draw();
  },
  word(){
    const x = this.cur(), w = x.w, cur = this.ch();
    $("#hzWord").innerHTML = `<div class="hz-wh"><span class="han">${x.cs.map((c, i) => `<button class="hz-c ${i === this.ci ? "on" : ""} ${this.rec[c] != null ? "ok" : ""}" data-ci="${i}" aria-label="Chữ ${c}">${c}</button>`).join("")}</span>
      <button class="say-sm" id="hzSay" aria-label="Nghe phát âm">${ICON.sound}</button></div>
      ${w.p ? `<div class="hz-py">${esc(w.p)}</div>` : ""}${w.vi ? `<div class="hz-vi">${esc(w.vi)}</div>` : ""}`;
    $("#hzWord").querySelectorAll("[data-ci]").forEach(b => b.onclick = () => { this.ci = +b.dataset.ci; this.draw(); });
    $("#hzSay").onclick = () => speak(x.cs.length > 1 && !x.free ? w.h : cur);
  },
  msg(html, kind = ""){ const m = $("#hzMsg"); if(m){ m.className = "hz-msg " + kind; m.innerHTML = html; } },
  async draw(){
    const tok = ++this.tok, c = this.ch(); this.word(); this.msg(""); $("#hzCtrl").innerHTML = ""; $("#hzSteps").innerHTML = ""; $("#hzCnt").textContent = "";
    if(this.writer){ try{ this.writer.cancelQuiz(); this.writer.pauseAnimation(); }catch(e){} }
    $("#hzW").innerHTML = ""; this.writer = null; const ld = $("#hzLoad"); ld.hidden = false; ld.textContent = "Đang tải nét chữ…";
    try{ await HZ.lib(); await HZ.get(c); }
    catch(e){ if(tok !== this.tok) return; ld.textContent = window.HanziWriter ? `Chưa có dữ liệu nét cho chữ “${c}”.` : "Không tải được bộ nét chữ. Kiểm tra mạng rồi thử lại."; return; }
    if(tok !== this.tok || !$("#hzW")) return; ld.hidden = true;
    const n = HZ.d[c].s.length; $("#hzCnt").textContent = `· ${n} nét`; $("#hzSteps").innerHTML = hzStepsSVG(c);
    const sz = this.size(), quiz = this.mode === "trace" || this.mode === "free";
    this.writer = HanziWriter.create($("#hzW"), c, { width: sz, height: sz, padding: Math.round(sz * .06),
      charDataLoader: (ch, ok, no) => HZ.get(ch).then(ok, no),
      showOutline: this.mode !== "free", showCharacter: false, strokeColor: "#22352C", outlineColor: "#D7E3DB",
      highlightColor: "#E6A23C", drawingColor: "#21836A", drawingWidth: Math.max(14, sz / 18), radicalColor: null,
      strokeAnimationSpeed: this.speed, delayBetweenStrokes: Math.round(500 / this.speed), delayBetweenLoops: 1800,
      showHintAfterMisses: this.mode === "trace" ? 2 : 3, highlightOnComplete: true, highlightCompleteColor: "#2C9A58" });
    const C = $("#hzCtrl"), Wr = this.writer;
    if(this.mode === "anim"){
      C.innerHTML = `<button class="btn primary" id="hzPlay">${ICON.redo}Xem lại</button><button class="btn" id="hzLoop" aria-pressed="false">Lặp liên tục</button>`;
      const play = () => { this.tok === tok && Wr.hideCharacter(); Wr.animateCharacter(); };
      $("#hzPlay").onclick = () => { $("#hzLoop").setAttribute("aria-pressed", "false"); play(); };
      $("#hzLoop").onclick = e => { const on = e.currentTarget.getAttribute("aria-pressed") !== "true"; e.currentTarget.setAttribute("aria-pressed", on); if(on) Wr.loopCharacterAnimation(); else { Wr.pauseAnimation(); Wr.showCharacter(); } };
      play();
    } else if(this.mode === "step"){
      let k = 0;
      C.innerHTML = `<button class="btn" id="hzReset">${ICON.redo}Làm lại</button><span class="hz-k" id="hzK">0 / ${n}</span><button class="btn primary" id="hzStep">Nét tiếp ${ICON.right}</button>`;
      const upd = () => { $("#hzK").textContent = `${k} / ${n}`; $("#hzStep").disabled = k >= n; document.querySelectorAll(".hz-step").forEach((f, i) => f.classList.toggle("on", i === k - 1)); };
      Wr.hideCharacter(); upd();
      $("#hzStep").onclick = () => { if(k >= n) return; Wr.animateStroke(k); k++; upd(); if(k >= n) this.msg(`Đủ ${n} nét rồi! Chuyển sang <b>Tập tô</b> để tự viết thử nhé.`, "good"); };
      $("#hzReset").onclick = () => { k = 0; Wr.hideCharacter(); this.msg(""); upd(); };
    } else {
      C.innerHTML = `<button class="btn" id="hzAgain">${ICON.redo}Viết lại</button><button class="btn" id="hzHint">Gợi ý nét này</button>`;
      let cur = 0;
      const start = () => { this.msg(this.mode === "trace" ? "Dùng ngón tay hoặc chuột <b>tô theo chữ mờ</b>, viết lần lượt từng nét." : "Tự viết chữ vào ô, <b>đúng thứ tự nét</b>."); cur = 0;
        Wr.quiz({ onCorrectStroke: d => { cur = d.strokeNum + 1; this.msg(`Đúng rồi! Nét ${d.strokeNum + 1} / ${n}`, "good"); },
          onMistake: d => { this.msg(d.mistakesOnStroke >= (this.mode === "trace" ? 2 : 3) ? `Chưa đúng. Xem nét <b>nhấp nháy</b> rồi viết theo nhé.` : `Chưa đúng nét ${d.strokeNum + 1}, thử lại nhé. Chú ý <b>hướng viết và thứ tự nét</b>.`, "bad"); },
          onComplete: s => this.done(c, s.totalMistakes) }); };
      $("#hzAgain").onclick = () => { this.mode === "free" ? Wr.hideOutline() : null; start(); };
      $("#hzHint").onclick = () => { Wr.highlightStroke(cur); };
      start();
    }
  },
  done(c, m){
    const stars = m === 0 ? 3 : m <= 2 ? 2 : 1, prev = this.rec[c];
    if(prev == null || m < prev){ this.rec[c] = m; store.set(this.key, this.rec); }
    const last = !this.extra && this.wi === this.words.length - 1 && this.ci === this.cur().cs.length - 1;
    this.msg(`<span class="hz-stars" aria-label="${stars} sao">${"★".repeat(stars)}<i>${"★".repeat(3 - stars)}</i></span> Hoàn thành chữ <b class="han">${c}</b> · ${m ? m + " lần sai" : "không sai nét nào!"}
      ${last ? "" : `<button class="btn primary sm" id="hzGo">Chữ tiếp theo ${ICON.right}</button>`}`, "good");
    const go = $("#hzGo"); if(go) go.onclick = () => this.move(1);
    if(this.mode === "free" && this.writer) this.writer.showOutline();
    this.side(); if(this.extra) return;
    const all = this.allChars(), done = all.filter(x => this.rec[x] != null);
    Track.logLater("write" + this.key, "write", () => ({ done: done.length, total: all.length }));
    if(done.length === all.length){
      const sc = m => m === 0 ? 100 : m <= 2 ? 85 : m <= 4 ? 65 : 50, pct = all.reduce((a, x) => a + sc(this.rec[x]), 0) / all.length, key = `write:${S.level}-${S.lesson}`;
      if(typeof Farm !== "undefined" && Farm.load() && !(Farm.st.done || {})[key]) Farm.earn(pct, `Tập viết Bài ${S.lesson} (${all.length} chữ)`, key);
    }
  },
  side(){
    const all = this.allChars(), done = all.filter(c => this.rec[c] != null).length, W = $("#work"); if(!W) return;
    const mt = W.querySelector(".side .meter i"); if(mt) mt.style.width = (all.length ? done / all.length * 100 : 0) + "%";
    const st = W.querySelector(".side .stat b"); if(st) st.textContent = `${done} / ${all.length}`;
    W.querySelectorAll(".hz-words [data-wi]").forEach(b => { const x = this.words[+b.dataset.wi]; if(!b.classList.contains("cur")) b.classList.toggle("k", x.cs.every(c => this.rec[c] != null)); });
    const cb = W.querySelector(`.hz-c[data-ci="${this.ci}"]`); if(cb) cb.classList.add("ok");
  }
};
/* Nút "Cách viết" trên mặt sau flashcard → mở Tập viết đúng từ đó */
document.addEventListener("click", e => { const b = e.target.closest("[data-hzw]"); if(!b) return; e.stopPropagation(); e.preventDefault(); Write.jump(b.dataset.hzw); }, true);
let hzRz; window.addEventListener("resize", () => { clearTimeout(hzRz); hzRz = setTimeout(() => { if(Write.writer && $("#hzW") && S.section === "write"){ const s = Write.size(); try{ Write.writer.updateDimensions({ width: s, height: s, padding: Math.round(s * .06) }); }catch(e){} } }, 200); });
