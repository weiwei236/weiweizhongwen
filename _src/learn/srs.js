/* ======================= ÔN TẬP HẰNG NGÀY – lặp lại ngắt quãng (hộp Leitner) =======================
   Từ đi vào hàng ôn khi học viên đã mở bài chứa từ đó. Mỗi ngày tối đa SRS_NEW từ mới.
   Nhớ → lên hộp (giãn ngày ôn: 1, 2, 4, 7, 15, 30, 60 ngày); Khó → giữ hộp, ôn lại ngày mai; Quên → về hộp 1, ôn lại ngay trong buổi.
   Lưu ở ww_srs (tự đồng bộ theo tài khoản như các dữ liệu ww_ khác). */
const SRS_GAP = [0, 1, 2, 4, 7, 15, 30, 60], SRS_NEW = 10, SRS_MAX = 40;
const SRS = {
  today(){ const d = new Date(); return Math.floor((d.getTime() - d.getTimezoneOffset() * 6e4) / 864e5); },
  st(){ const s = store.get("ww_srs", null) || {}; s.c = s.c || {}; s.seen = s.seen || []; return s; },
  save(s){ store.set("ww_srs", s); },
  key(level, lesson, k){ return level + ":" + lesson + ":" + k; },
  word(key){ const [lv, ls, ...r] = key.split(":"), k = r.join(":"), les = LEVELS[lv] && LEVELS[lv].lessons[ls]; return les ? (les.vocab || []).find(w => w.k === k) : null; },
  /* ghi nhận bài đã mở */
  see(level, lesson){ try{ const s = this.st(), id = level + ":" + lesson; if(!s.seen.includes(id)){ s.seen.push(id); this.save(s); } }catch(e){} },
  seenList(){
    const s = this.st(), ids = [...s.seen];
    /* học viên cũ: bài nào đã có dữ liệu flashcard / tập viết cũng tính là đã học */
    try{ for(let i = 0; i < localStorage.length; i++){ const m = /^ww_(?:known|hz)_(.+)_(\d+)$/.exec(localStorage.key(i) || ""); if(m && LEVELS[m[1]] && LEVELS[m[1]].lessons[m[2]]){ const id = m[1] + ":" + m[2]; if(!ids.includes(id)) ids.push(id); } } }catch(e){}
    if(!ids.length && S.level && LEVELS[S.level]){ const f = Object.keys(LEVELS[S.level].lessons || {})[0]; if(f) ids.push(S.level + ":" + f); }
    return ids;
  },
  pool(){ const out = [], had = new Set();
    this.seenList().forEach(id => { const [lv, ls] = id.split(":"), les = LEVELS[lv] && LEVELS[lv].lessons[ls]; if(!les || !les.vocab) return;
      les.vocab.forEach(w => { if(!w.h || had.has(w.h)) return; had.add(w.h); out.push({ key: this.key(lv, ls, w.k), w, lv, ls }); }); });
    return out; },
  plan(){
    const s = this.st(), t = this.today(), pool = this.pool();
    const due = Object.entries(s.c).filter(([, v]) => v[1] <= t).sort((a, b) => a[1][1] - b[1][1]).map(([k]) => k).filter(k => this.word(k)).slice(0, SRS_MAX);
    const usedNew = s.nd === t ? (s.nn || 0) : 0, room = Math.max(0, SRS_NEW - usedNew);
    const known = new Set(); try{ for(let i = 0; i < localStorage.length; i++){ const m = /^ww_known_(.+)_(\d+)$/.exec(localStorage.key(i) || ""); if(m) (store.get(localStorage.key(i), []) || []).forEach(k => known.add(m[1] + ":" + m[2] + ":" + k)); } }catch(e){}
    const fresh = pool.filter(x => !s.c[x.key]).slice(0, room).map(x => x.key);
    return { due, fresh, known, total: Object.keys(s.c).length, pool: pool.length };
  },
  count(){ try{ const p = this.plan(); return p.due.length + p.fresh.length; }catch(e){ return 0; } },
  grade(key, g, isNew){
    const s = this.st(), t = this.today(); let [b] = s.c[key] || [isNew && this.q.known.has(key) ? 2 : 1, t];
    if(g === 0) b = 1; else if(g === 2) b = Math.min(7, b + 1);
    s.c[key] = [b, t + (g === 0 ? 0 : g === 1 ? 1 : SRS_GAP[b])];
    if(isNew){ if(s.nd !== t){ s.nd = t; s.nn = 0; } s.nn++; }
    this.save(s);
  },
  /* ---------- giao diện ---------- */
  open(){
    const p = this.plan(); this.q = { list: [...p.fresh.map(k => ({ k, n: 1 })), ...p.due.map(k => ({ k, n: 0 }))], i: 0, right: 0, done: 0, again: new Set(), known: p.known, fb: null };
    /* xen kẽ từ mới và từ ôn */
    const nw = this.q.list.filter(x => x.n), old = this.q.list.filter(x => !x.n), mix = []; while(nw.length || old.length){ if(old.length) mix.push(old.shift()); if(old.length) mix.push(old.shift()); if(nw.length) mix.push(nw.shift()); }
    this.q.list = mix; this.q.total = mix.length;
    showScreen("scrReview"); this.render();
  },
  mode(it){ const s = this.st(), b = (s.c[it.k] || [0])[0]; if(it.n || b <= 2 || it.retry) return "flip"; return (it.k.length + b) % 2 ? "mc" : "rev"; },
  opts(w, field){ const pool = this.pool().map(x => x.w).filter(x => x[field] !== w[field]); const pick = shuffle(pool).slice(0, 3).map(x => x[field]); return shuffle([w[field], ...pick]); },
  render(){
    const W = $("#rvBody"), Q = this.q, s = this.st();
    const head = `<div class="rv-top"><div><h2><span class="han">复习</span> · Ôn tập hôm nay</h2><p class="muted">Lặp lại ngắt quãng: từ nào nhớ chắc sẽ được ôn thưa dần, từ hay quên sẽ gặp lại sớm.</p></div><button class="btn" id="rvBack">${ICON.left}Về trang học</button></div>`;
    if(!Q.list.length){
      const t = this.today(), nxt = Object.values(s.c).filter(v => v[1] > t).sort((a, b) => a[1] - b[1])[0];
      W.innerHTML = head + `<div class="panel rv-empty"><span class="han">棒</span><h3>${Q.total ? "Hoàn thành buổi ôn hôm nay!" : "Hôm nay chưa có từ nào cần ôn"}</h3>
        ${Q.total ? `<p>Bạn ôn <b>${Q.total}</b> từ, nhớ ngay <b>${Q.right}</b> từ.</p>` : `<p>${this.st().seen.length || Object.keys(s.c).length ? "Bạn đã ôn hết từ đến hạn." : "Hãy mở một bài học (Flashcard, Tập viết…) để từ của bài đó vào hàng ôn tập."}</p>`}
        <p class="muted">Đang theo dõi <b>${Object.keys(s.c).length}</b> từ${nxt ? ` · lần ôn tiếp theo: <b>${nxt[1] - t === 1 ? "ngày mai" : "sau " + (nxt[1] - t) + " ngày"}</b>` : ""}.</p>
        ${this.boxes()}<button class="btn primary big" id="rvBack2">Về trang học</button></div>`;
      $("#rvBack").onclick = $("#rvBack2").onclick = () => { showScreen("app"); renderHello(); };
      if(Q.total && !Q.paid){ Q.paid = true; Track.log("srs", { n: Q.total, right: Q.right }, ""); if(typeof Farm !== "undefined" && Farm.load() && !(Farm.st.done || {})["srs:" + this.today()]) Farm.earn(Math.max(60, Q.right / Q.total * 100), `Ôn tập hằng ngày (${Q.total} từ)`, "srs:" + this.today()); }
      return;
    }
    const it = Q.list[0], w = this.word(it.k), md = this.mode(it), fb = Q.fb;
    if(!w){ Q.list.shift(); return this.render(); }
    const prog = `<div class="rv-prog"><div class="meter"><i style="width:${Q.done / Math.max(1, Q.total) * 100}%"></i></div><span>${Q.done}/${Q.total}</span>${it.n ? `<em class="rv-new">Từ mới</em>` : ""}</div>`;
    const back = `<div class="rv-back"><div class="rv-zh"><span class="han">${esc(w.h)}</span><button class="say" data-say="${esc(w.h)}" aria-label="Nghe">${ICON.sound}</button></div><div class="rv-py">${esc(w.p)}</div><div class="rv-vi">${esc(w.vi)}</div>
      ${w.ex && w.ex[0] ? `<div class="rv-ex"><span class="han">${esc(w.ex[0])}</span><small>${esc(w.ex[1] || "")}</small><small>${esc(w.ex[2] || "")}</small></div>` : ""}</div>`;
    let body = "";
    if(md === "flip"){
      body = fb ? back + `<p class="rv-ask">Bạn nhớ từ này thế nào?</p><div class="rv-grade"><button class="btn bad" data-g="0">Quên<small>ôn lại ngay</small></button><button class="btn" data-g="1">Khó<small>ngày mai</small></button><button class="btn good" data-g="2">Nhớ<small>${this.nextTxt(it)}</small></button></div>`
        : `<div class="rv-front"><span class="han">${esc(w.h)}</span><button class="say" data-say="${esc(w.h)}" aria-label="Nghe">${ICON.sound}</button></div><p class="rv-ask">Nhớ lại phiên âm và nghĩa, rồi lật thẻ.</p><button class="btn primary big" id="rvShow">Lật thẻ (Space)</button>`;
    } else {
      const field = md === "mc" ? "vi" : "h", opts = it.opts || (it.opts = this.opts(w, field));
      body = `${md === "mc" ? `<div class="rv-front"><span class="han">${esc(w.h)}</span><button class="say" data-say="${esc(w.h)}" aria-label="Nghe">${ICON.sound}</button></div><p class="rv-ask">Chọn nghĩa đúng</p>` : `<div class="rv-front vi"><b>${esc(w.vi)}</b></div><p class="rv-ask">Chọn chữ Hán đúng</p>`}
        <div class="rv-opts ${field === "h" ? "han" : ""}">${opts.map((o, j) => `<button class="rv-opt ${fb ? (o === w[field] ? "right" : it.sel === j ? "wrong" : "") : ""}" data-o="${j}" ${fb ? "disabled" : ""}>${esc(o)}</button>`).join("")}</div>
        ${fb ? back + `<button class="btn primary big" id="rvNext">Tiếp tục →</button>` : ""}`;
    }
    W.innerHTML = head + `<div class="panel rv-card">${prog}${body}</div>`;
    $("#rvBack").onclick = () => { showScreen("app"); renderHello(); };
    W.querySelectorAll("[data-say]").forEach(b => b.onclick = () => speak(b.dataset.say));
    const show = $("#rvShow"); if(show){ show.onclick = () => { Q.fb = true; this.render(); speak(w.h); }; }
    W.querySelectorAll("[data-g]").forEach(b => b.onclick = () => this.answer(+b.dataset.g));
    W.querySelectorAll("[data-o]").forEach(b => b.onclick = () => { const field = md === "mc" ? "vi" : "h"; it.sel = +b.dataset.o; const ok = it.opts[it.sel] === w[field]; it.ok = ok; Q.fb = true; this.render(); speak(w.h); });
    const nx = $("#rvNext"); if(nx) nx.onclick = () => this.answer(it.ok ? 2 : 0);
  },
  nextTxt(it){ const b = (this.st().c[it.k] || [it.n && this.q.known.has(it.k) ? 2 : 1])[0], g = SRS_GAP[Math.min(7, b + 1)]; return g === 1 ? "ngày mai" : g + " ngày nữa"; },
  answer(g){
    const Q = this.q, it = Q.list.shift();
    if(!it.retry){ this.grade(it.k, g, !!it.n); if(g === 2) Q.right++; Q.done++; }
    else if(g !== 0){ const s = this.st(); if(s.c[it.k]){ s.c[it.k][1] = this.today() + 1; this.save(s); } }
    if(g === 0 && !it.retry2){ Q.list.splice(Math.min(Q.list.length, 3), 0, { k: it.k, n: 0, retry: true, retry2: !!it.retry }); }
    Q.fb = null; this.render();
  },
  boxes(){ const s = this.st(), n = [0, 0, 0, 0, 0, 0, 0, 0]; Object.values(s.c).forEach(v => n[v[0]]++);
    const lab = ["", "Mới học", "1–2 ngày", "4 ngày", "1 tuần", "2 tuần", "1 tháng", "Nhớ chắc"];
    return `<div class="rv-boxes">${n.slice(1).map((x, i) => `<div><b>${x}</b><small>${lab[i + 1]}</small><i style="height:${Math.min(100, x * 4)}%"></i></div>`).join("")}</div>`; }
};
document.addEventListener("keydown", e => { if($("#scrReview") && !$("#scrReview").hidden && e.code === "Space" && $("#rvShow")){ e.preventDefault(); $("#rvShow").click(); } });
