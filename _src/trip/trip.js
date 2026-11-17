/* ===== Trò chơi "Khám phá Trung Quốc" – bản đồ, trạm, hướng dẫn viên, trả lời câu hỏi để mở khóa ===== */
const Trip = {
  st: null, view: "map", city: null, spot: null, qz: null, py: store.get("ww_trip_py", true), vi: store.get("ww_trip_vi", true), busy: false,
  key(){ const p = Profile.get(); if(!p) return null; if(!p.sid){ p.sid = Track.uid(); Profile.set(p); } return "ww_trip_" + p.sid; },
  load(){ const k = this.key(); if(!k) return null; this.st = store.get(k, null) || { done: {}, stamps: {} }; this.st.done = this.st.done || {}; this.st.stamps = this.st.stamps || {}; return this.st; },
  save(){ const k = this.key(); if(k && this.st) store.set(k, this.st); },
  C(id){ return TRIP.find(c => c.id === id); },
  S(id){ for(const c of TRIP){ const s = c.spots.find(x => x.id === id); if(s) return s; } return null; },
  cnt(c){ return c.spots.filter(s => this.st.done[s.id]).length; },
  z(t){ return this.py ? rubyHTML(t) : esc(t); },
  art(k, cls = ""){ return `<div class="tp-artbox ${cls}">${tripArt(k)}</div>`; },
  say(zh){ return `<button type="button" class="tp-say" data-say="${esc(zh)}" aria-label="Nghe">${ICON.sound}</button>`; },
  line([zh, vi]){ return `<div class="tp-line">${this.say(zh)}<div><div class="tp-zh han">${this.z(zh)}</div><div class="tp-vi">${esc(vi)}</div></div></div>`; },
  guide(expr, html){ return `<div class="tp-guide"><div class="tp-gd">${guideSVG(expr)}</div><div class="tp-bub">${html}</div></div>`; },
  open(){ if(!this.load()) return openWelcome(); this.view = "map"; showScreen("scrTrip"); this.render(); },

  render(){
    const p = Profile.get(), total = TRIP.reduce((a, c) => a + c.spots.length, 0), done = Object.keys(this.st.done).length;
    let h = `<div class="tp-top"><div><h2><span class="han">中国之旅</span> · Khám phá Trung Quốc</h2><p class="muted">Đã khám phá ${done}/${total} địa điểm · ${Object.keys(this.st.stamps).length}/${TRIP.length} con dấu</p></div>
      <div class="tp-acts"><button class="btn ${this.py ? "on" : ""}" id="tpPy" aria-pressed="${this.py}">Phiên âm</button><button class="btn ${this.vi ? "on" : ""}" id="tpVi" aria-pressed="${this.vi}">Tiếng Việt</button>
      ${this.view !== "map" ? `<button class="btn" id="tpMap">🗺 Bản đồ</button>` : ""}<button class="btn" id="tpBack">${ICON.left}Về trang học</button></div></div>`;
    if(this.view === "map") h += this.mapView();
    else if(this.view === "city") h += this.cityView();
    else if(this.view === "quiz") h += this.quizView();
    else if(this.view === "spot") h += this.spotView();
    $("#tpBody").innerHTML = h; $("#tpBody").classList.toggle("tp-novi", !this.vi); this.bind();
  },

  /* ---------- Bản đồ ---------- */
  mapView(){
    const pins = TRIP.map(c => { const n = this.cnt(c), full = n === c.spots.length, lx = c.x + c.lx, ly = c.y + c.ly, far = Math.hypot(c.lx + 30, c.ly) > 34;
      return `<g class="tp-pin" data-c="${c.id}" tabindex="0" role="button" aria-label="${c.vi}">
        ${far ? `<path d="M${c.x} ${c.y - 8} L${lx + (c.lx < 0 ? 60 : 0)} ${ly - 1}" stroke="${c.col}" stroke-width="1.4" stroke-dasharray="2 2"/>` : ""}
        <circle cx="${c.x}" cy="${c.y}" r="9" fill="${c.col}" opacity=".18"><animate attributeName="r" values="6;12;6" dur="2.4s" repeatCount="indefinite"/></circle>
        <path d="M${c.x} ${c.y + 1} C${c.x - 7} ${c.y - 7} ${c.x - 7} ${c.y - 17} ${c.x} ${c.y - 17} C${c.x + 7} ${c.y - 17} ${c.x + 7} ${c.y - 7} ${c.x} ${c.y + 1}Z" fill="${c.col}" stroke="#5A4034" stroke-width="1.4" stroke-linejoin="round"/>
        <circle cx="${c.x}" cy="${c.y - 11}" r="3.2" fill="#fff"/>
        <g transform="translate(${lx} ${ly})"><rect x="0" y="-10" width="60" height="19" rx="9.5" fill="#fff" stroke="${c.col}" stroke-width="2"/><text x="20" y="4" text-anchor="middle" font-size="11.5" font-family="KaiTi,STKaiti,serif" fill="#3A2A22">${c.zh}</text>${full ? `<circle cx="48" cy="-.5" r="5.6" fill="#2C9A58"/><path d="M45.2 -.5 l2 2 l3.6 -3.6" stroke="#fff" stroke-width="1.5" fill="none"/>` : `<text x="47" y="2.6" font-size="7.5" text-anchor="middle" fill="#8A7466">${n}/${c.spots.length}</text>`}</g></g>`; }).join("");
    const stamps = TRIP.map(c => { const ok = this.st.stamps[c.id];
      return `<div class="tp-stamp ${ok ? "ok" : ""}" style="--sc:${c.col}" title="${c.vi}"><span class="han">${c.zh}</span><small>${ok ? "已到" : "未到"}</small></div>`; }).join("");
    return this.guide("smile", `<b class="han">${this.z("你好！我是导游小语。")}</b><p>Chào ${esc(Profile.get().name)}! Mình là hướng dẫn viên Tiểu Ngữ. Chọn một trạm trên bản đồ để bắt đầu chuyến đi nhé. Ở mỗi trạm, bạn trả lời đúng ít nhất <b>2/3 câu hỏi</b> để “mua vé” vào xem danh lam hoặc nếm món ngon. Khám phá đủ 5 địa điểm của một thành phố sẽ được đóng <b>con dấu hộ chiếu</b>!</p>`)
      + `<div class="tp-maplay"><div class="tp-mapbox"><div class="tp-mapin">${chinaMapSVG().replace('<g id="tpPins"></g>', pins)}${this.meHTML()}</div><p class="tp-maphint">✈ Bấm vào một trạm để bay đến đó</p></div>
        <aside class="tp-pass"><h3>护照 · Hộ chiếu du lịch</h3><div class="tp-stamps">${stamps}</div>
        <div class="tp-clist">${TRIP.map(c => `<button class="tp-cbtn" data-c="${c.id}" style="--sc:${c.col}">${this.art(c.cover, "mini")}<span><b class="han">${c.zh}</b> <small>${c.py}</small><em>${c.vi} · ${this.cnt(c)}/${c.spots.length}</em></span></button>`).join("")}</div></aside></div>`;
  },

  pos(c){ return `left:${c.x / 4}%;top:${c.y / 3.2}%`; },
  head(){ const p = Profile.get(); try{ return avatarSVG({ ...(p.avatar || {}), expr: "laugh" }, { view: "head", label: p.name }); }catch(e){ return guideSVG("happy"); } },
  meHTML(){ const c = this.st.at && this.C(this.st.at); return `<div class="tp-me ${c ? "" : "off"}" id="tpMe" style="${c ? this.pos(c) : "left:96%;top:92%"}"><div class="tp-me-h">${this.head()}</div><i></i></div>`; },
  fly(id){
    const to = this.C(id), from = this.st.at && this.C(this.st.at);
    const done = () => { this.busy = false; this.st.at = id; this.save(); this.city = id; this.view = "city"; this.arrived = true; this.render(); window.scrollTo(0, 0); };
    const box = $("#tpBody .tp-mapin");
    if(!box || (from && from.id === id) || matchMedia("(prefers-reduced-motion: reduce)").matches) return done();
    this.busy = true;
    const A = from ? { x: from.x, y: from.y - 12 } : { x: 392, y: 300 }, B = { x: to.x, y: to.y - 12 };
    const d = Math.hypot(B.x - A.x, B.y - A.y) || 1, sg = (B.x - A.x) >= 0 ? -1 : 1, C = { x: (A.x + B.x) / 2 + sg * (B.y - A.y) / d * d * .35 * -1, y: (A.y + B.y) / 2 - Math.abs(B.x - A.x) / d * d * .35 - 12 };
    const pt = t => ({ x: (1 - t) * (1 - t) * A.x + 2 * (1 - t) * t * C.x + t * t * B.x, y: (1 - t) * (1 - t) * A.y + 2 * (1 - t) * t * C.y + t * t * B.y });
    const me = $("#tpMe"); if(me) me.classList.add("off");
    const plane = document.createElement("div"); plane.className = "tp-plane";
    plane.innerHTML = `<div class="tp-pl-r">${this.head()}</div><svg class="tp-pl-s" viewBox="0 0 64 40" aria-hidden="true"><path d="M6 20 Q10 14 22 14 L50 14 Q60 14 62 20 Q60 26 50 26 L22 26 Q10 26 6 20Z" fill="#fff" stroke="#5A4034" stroke-width="2"/><path d="M28 14 L40 2 H46 L40 14Z M28 26 L40 38 H46 L40 26Z M8 18 L2 8 H8 L14 16Z" fill="#7FB8E6" stroke="#5A4034" stroke-width="1.6" stroke-linejoin="round"/><g fill="#9FD0F0" stroke="#5A4034" stroke-width="1"><circle cx="30" cy="20" r="2.4"/><circle cx="37" cy="20" r="2.4"/><circle cx="44" cy="20" r="2.4"/></g><path d="M54 16 Q60 18 60 20" stroke="#5A4034" stroke-width="1.4" fill="none"/><path d="M14 22 H26" stroke="#E8453C" stroke-width="2"/></svg>`;
    box.appendChild(plane);
    const trail = $("#tpBody #tpTrail"), dur = Math.min(2600, 1300 + d * 6), t0 = performance.now();
    const step = now => {
      const t = Math.min(1, (now - t0) / dur), e = t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      const p = pt(e), q = pt(Math.min(1, e + .01)), ang = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI;
      plane.style.left = p.x / 4 + "%"; plane.style.top = p.y / 3.2 + "%";
      plane.querySelector(".tp-pl-s").style.transform = `rotate(${ang}deg) scale(${1 + Math.sin(e * Math.PI) * .35})`;
      if(trail){ let dd = `M${A.x} ${A.y}`; for(let k = 1; k <= 24; k++){ const r = pt(e * k / 24); dd += ` L${r.x.toFixed(1)} ${r.y.toFixed(1)}`; } trail.setAttribute("d", dd); }
      if(t < 1) requestAnimationFrame(step);
      else { plane.classList.add("land"); if(me){ me.style.cssText = this.pos(to); me.classList.remove("off"); me.classList.add("pop"); } setTimeout(done, 650); }
    };
    requestAnimationFrame(step);
  },

  /* ---------- Trạm thành phố ---------- */
  cityView(){
    const c = this.C(this.city);
    const arr = this.arrived; this.arrived = false;
    return `<div class="tp-banner ${arr ? "arrive" : ""}" style="--sc:${c.col}">${this.art(c.cover, "ban")}<div class="tp-bt"><span class="han">${c.zh}</span><small>${c.py}</small><b>${c.vi}</b><em>${this.cnt(c)}/${c.spots.length} địa điểm</em>${arr ? `<span class="tp-landed">✈ Đã hạ cánh!</span>` : ""}</div></div>`
      + this.guide("happy", c.intro.map(l => this.line(l)).join("") + `<button class="linkbtn tp-sayall" data-sayall="${esc(c.intro.map(l => l[0]).join(""))}">${ICON.sound} Nghe cả đoạn</button>`)
      + `<h3 class="tp-h">Bạn muốn khám phá gì?</h3><div class="tp-grid">${c.spots.map(s => { const ok = this.st.done[s.id];
        return `<button class="tp-card ${ok ? "ok" : "lock"}" data-s="${s.id}">${this.art(s.art)}<span class="tp-tag ${s.kind}">${s.kind === "jd" ? "景点 · Danh lam" : "美食 · Món ngon"}</span>
          <span class="tp-cn"><b class="han">${s.zh}</b><small>${s.py}</small><em>${esc(s.vi)}</em></span>
          ${ok ? `<span class="tp-ok">✓ Đã khám phá · ${ok.score}/3</span>` : `<span class="tp-lk">🔒 Trả lời 3 câu để vào</span>`}</button>`; }).join("")}</div>`;
  },

  /* ---------- Câu hỏi ---------- */
  startQuiz(id){
    const s = this.S(id), shuf = a => a.map(x => [Math.random(), x]).sort((p, q) => p[0] - q[0]).map(x => x[1]);
    this.qz = { id, i: 0, right: 0, fb: null, items: s.q.map(q => {
      if(q[0] === "s"){ const toks = q[1].split(" "); let sh; do { sh = shuf(toks.map((t, k) => ({ t, k }))); } while(toks.length > 2 && sh.every((x, k) => x.k === k)); return { t: "s", toks, pool: sh, pick: [], vi: q[2] }; }
      const opts = q[2].split("|").map((t, k) => ({ t, ok: k === q[3] }));
      return { t: q[0], text: q[1], opts: shuf(opts), why: q[4] }; }) };
    this.view = "quiz"; this.render();
  },
  quizView(){
    const s = this.S(this.qz.id), Q = this.qz, it = Q.items[Q.i], fb = Q.fb;
    const head = `<div class="tp-qhead">${this.art(s.art, "mini lock")}<div><small>${s.kind === "jd" ? "Vé vào cửa" : "Phiếu nếm thử"}</small><b class="han">${s.zh}</b> <span>${esc(s.vi)}</span></div><div class="tp-dots">${Q.items.map((x, k) => `<i class="${k < Q.i ? (x.res ? "r" : "w") : k === Q.i ? "now" : ""}"></i>`).join("")}</div></div>`;
    const ask = it.t === "c" ? "Chọn đáp án đúng nhé!" : it.t === "f" ? "Chọn từ thích hợp điền vào chỗ trống." : "Sắp xếp các từ thành câu đúng.";
    let body = "";
    if(it.t === "c"){
      body = `<div class="tp-qtext han">${this.z(it.text)}</div><div class="tp-opts">${it.opts.map((o, k) => `<button class="tp-opt ${fb ? (o.ok ? "right" : it.sel === k ? "wrong" : "") : ""}" data-o="${k}" ${fb ? "disabled" : ""}><b>${"ABC"[k]}</b> <span class="${/[一-鿿]/.test(o.t) ? "han" : ""}">${/[一-鿿]/.test(o.t) ? this.z(o.t) : esc(o.t)}</span></button>`).join("")}</div>`;
    } else if(it.t === "f"){
      const fill = it.sel != null ? it.opts[it.sel].t : "";
      const parts = it.text.split("（　）");
      body = `<div class="tp-qtext han">${this.z(parts[0])}<span class="tp-blank ${fb ? (it.res ? "right" : "wrong") : fill ? "filled" : ""}">${fill ? this.z(fill) : "&nbsp;"}</span>${this.z(parts[1] || "")}</div>
        <div class="tp-pool">${it.opts.map((o, k) => `<button class="tp-chip ${fb && o.ok ? "right" : ""} ${it.sel === k ? "used" : ""}" data-o="${k}" ${fb ? "disabled" : ""}>${this.z(o.t)}</button>`).join("")}</div>`;
    } else {
      body = `<div class="tp-vi-hint">“${esc(it.vi)}”</div><div class="tp-ans ${fb ? (it.res ? "right" : "wrong") : ""}">${it.pick.length ? it.pick.map((x, k) => `<button class="tp-chip in" data-back="${k}" ${fb ? "disabled" : ""}>${this.z(x.t)}</button>`).join("") : `<span class="muted">Bấm các từ bên dưới theo thứ tự…</span>`}</div>
        <div class="tp-pool">${it.pool.map((x, k) => it.pick.includes(x) ? `<span class="tp-chip ghost">${esc(x.t)}</span>` : `<button class="tp-chip" data-p="${k}" ${fb ? "disabled" : ""}>${this.z(x.t)}</button>`).join("")}</div>
        ${fb ? "" : `<div class="tp-row"><button class="btn" id="tpClr">Xóa</button><button class="btn primary" id="tpChk" ${it.pick.length === it.toks.length ? "" : "disabled"}>Kiểm tra</button></div>`}`;
    }
    let fbh = "";
    if(fb){
      const ans = it.t === "s" ? it.toks.join("") : it.opts.find(o => o.ok).t;
      fbh = this.guide(it.res ? "happy" : "think", `<b>${it.res ? `<span class="han">太棒了！</span> Chính xác!` : `<span class="han">没关系！</span> Chưa đúng rồi.`}</b>
        ${it.res ? "" : `<p>Đáp án: <b class="han">${this.z(ans)}</b></p>`}<p>${esc(it.t === "s" ? "Nghĩa: " + it.vi : it.why)}</p>
        <button class="btn primary" id="tpNext">${Q.i < Q.items.length - 1 ? "Câu tiếp theo →" : "Xem kết quả"}</button>`);
    }
    return head + (fb ? "" : this.guide("smile", `<b>Câu ${Q.i + 1}/${Q.items.length}</b> · ${ask}`)) + `<div class="tp-qbox panel">${body}</div>` + fbh;
  },
  check(){
    const Q = this.qz, it = Q.items[Q.i];
    it.res = it.t === "s" ? it.pick.map(x => x.t).join("") === it.toks.join("") : !!it.opts[it.sel].ok;
    if(it.res) Q.right++;
    Q.fb = true; this.render();
    if(it.res && it.t !== "c") speak(it.t === "s" ? it.toks.join("") : it.text.replace("（　）", it.opts[it.sel].t));
  },
  next(){
    const Q = this.qz;
    if(Q.i < Q.items.length - 1){ Q.i++; Q.fb = null; this.render(); return; }
    const s = this.S(Q.id), pass = Q.right >= 2;
    if(!pass){ this.view = "fail"; $("#tpBody").innerHTML = this.failView(); this.bind(); return; }
    const first = !this.st.done[s.id];
    this.st.done[s.id] = { score: Math.max(Q.right, (this.st.done[s.id] || {}).score || 0), t: Date.now() };
    const c = TRIP.find(c => c.spots.includes(s)); let newStamp = false;
    if(this.cnt(c) === c.spots.length && !this.st.stamps[c.id]){ this.st.stamps[c.id] = Date.now(); newStamp = true; }
    this.save();
    Track.log("trip", { spot: s.id, score: Q.right }, "");
    if(first && typeof Farm !== "undefined") Farm.earn(Q.right / 3 * 100, "Khám phá " + s.vi, "trip_" + s.id);
    this.spot = s.id; this.view = "spot"; this.newStamp = newStamp ? c.id : null; this.render();
  },
  failView(){
    const Q = this.qz, s = this.S(Q.id);
    return `<div class="tp-top"><div><h2><span class="han">中国之旅</span></h2></div><div class="tp-acts"><button class="btn" id="tpMap">🗺 Bản đồ</button></div></div>`
      + this.guide("think", `<b class="han">${this.z("再试一次吧！")}</b><p>Bạn trả lời đúng <b>${Q.right}/3</b> câu. Cần ít nhất 2 câu đúng để vào xem <b class="han">${s.zh}</b>. Thử lại nhé, câu hỏi sẽ được xáo lại!</p>
        <div class="tp-row"><button class="btn primary" data-retry="${s.id}">Thử lại</button><button class="btn" id="tpCity">Về trạm ${esc(this.C(this.city).vi)}</button></div>`);
  },

  /* ---------- Địa điểm đã mở ---------- */
  spotView(){
    const s = this.S(this.spot), c = this.C(this.city), idx = c.spots.indexOf(s), nx = c.spots.find((x, k) => k > idx && !this.st.done[x.id]) || c.spots.find(x => !this.st.done[x.id]);
    return (this.newStamp ? `<div class="tp-cele" style="--sc:${c.col}"><div class="tp-stamp big ok" style="--sc:${c.col}"><span class="han">${c.zh}</span><small>已到</small></div><div><b>Chúc mừng!</b> Bạn đã khám phá hết ${c.vi} và nhận con dấu hộ chiếu <span class="han">${c.zh}</span>!</div></div>` : "")
      + `<div class="tp-spot"><div class="tp-spot-art">${this.art(s.art, "big")}<div class="tp-spot-name"><span class="tp-tag ${s.kind}">${s.kind === "jd" ? "景点" : "美食"}</span><b class="han">${this.z(s.zh)}</b><small>${s.py}</small><em>${esc(s.vi)}</em></div></div>
        <div class="tp-spot-txt">${this.guide("happy", `<b>Hướng dẫn viên giới thiệu</b>` + s.lines.map(l => this.line(l)).join("") + `<button class="linkbtn tp-sayall" data-sayall="${esc(s.lines.map(l => l[0]).join(""))}">${ICON.sound} Nghe cả đoạn</button>`)}
        <div class="tp-words"><h4>Từ mới ở đây</h4>${s.words.map(([w, py, vi]) => `<button class="tp-word" data-say="${esc(w.replace(/……/g, ""))}"><b class="han">${esc(w)}</b><small>${esc(py)}</small><span>${esc(vi)}</span></button>`).join("")}</div>
        <div class="tp-row"><button class="btn" id="tpCity">← Về trạm ${esc(c.vi)}</button>${nx ? `<button class="btn primary" data-s="${nx.id}">Tiếp: ${esc(nx.zh)} →</button>` : `<button class="btn primary" id="tpMap2">Chọn thành phố khác 🗺</button>`}</div></div></div>`;
  },

  bind(){
    const B = $("#tpBody");
    const on = (sel, fn) => B.querySelectorAll(sel).forEach(el => el.onclick = e => fn(el, e));
    on("#tpBack", () => { stopSpeak(); showScreen("app"); renderHello(); });
    on("#tpMap, #tpMap2", () => { stopSpeak(); this.view = "map"; this.render(); });
    on("#tpCity", () => { stopSpeak(); this.view = "city"; this.render(); });
    on("#tpVi", () => { this.vi = !this.vi; store.set("ww_trip_vi", this.vi); const b = $("#tpVi"); b.classList.toggle("on", this.vi); b.setAttribute("aria-pressed", this.vi); $("#tpBody").classList.toggle("tp-novi", !this.vi); });
    on("#tpPy", () => { this.py = !this.py; store.set("ww_trip_py", this.py); if(this.view === "fail"){ $("#tpBody").innerHTML = this.failView(); this.bind(); } else this.render(); });
    const go = (id, fromList) => { if(this.busy) return; const m = B.querySelector(".tp-mapin"); if(fromList && m && m.getBoundingClientRect().top < 0){ m.scrollIntoView({ behavior: "smooth", block: "center" }); setTimeout(() => this.fly(id), 450); } else this.fly(id); };
    on(".tp-pin", el => go(el.dataset.c)); on(".tp-cbtn", el => go(el.dataset.c, true));
    B.querySelectorAll(".tp-pin").forEach(el => el.onkeydown = e => { if(e.key === "Enter" || e.key === " "){ e.preventDefault(); go(el.dataset.c); } });
    on(".tp-say, .tp-word", el => speak(el.dataset.say));
    on(".tp-sayall", el => speak(el.dataset.sayall));
    on("[data-s]", el => { stopSpeak(); const s = this.S(el.dataset.s); if(this.st.done[s.id]){ this.spot = s.id; this.newStamp = null; this.view = "spot"; this.render(); } else this.startQuiz(s.id); window.scrollTo(0, 0); });
    on("[data-retry]", el => this.startQuiz(el.dataset.retry));
    if(this.view === "quiz"){
      const it = this.qz.items[this.qz.i];
      on(".tp-opt[data-o], .tp-chip[data-o]", el => { if(this.qz.fb) return; it.sel = +el.dataset.o; this.check(); });
      on(".tp-chip[data-p]", el => { it.pick.push(it.pool[+el.dataset.p]); this.render(); });
      on(".tp-chip[data-back]", el => { it.pick.splice(+el.dataset.back, 1); this.render(); });
      on("#tpClr", () => { it.pick = []; this.render(); });
      on("#tpChk", () => this.check());
      on("#tpNext", () => this.next());
    }
  }
};
