/* ======================= LUYỆN NGỮ ÂM =======================
   Học viên: nghe audio mẫu của cô → ghi âm → nộp. Cô nghe & nhận xét trong khu giáo viên (tab “Ngữ âm”).
   Dữ liệu lưu ở Google Sheet/Drive của giáo viên qua Apps Script (pronRef, pronSubmit, pronMine, pronSubs, pronComment…). */
/* chọn micro: tránh micro ảo (Teams, Zoom, Voicemod…) mà Chrome hay đặt làm mặc định – nó chỉ ra tín hiệu im lặng */
const MIC_BAD = /virtual|teams|zoom|voicemod|blackhole|loopback|soundflower|capcut|aggregate|krisp|nvidia broadcast|聚集|多输出|虚拟/i;
async function micList(){ try{ return (await navigator.mediaDevices.enumerateDevices()).filter(d => d.kind === "audioinput" && d.deviceId !== "communications"); }catch(e){ return []; } }
function micSaved(){ try{ return localStorage.getItem("ww_mic") || ""; }catch(e){ return ""; } }
async function pickMic(audio){
  const saved = micSaved(), open = id => navigator.mediaDevices.getUserMedia({ audio: id ? Object.assign({}, audio, { deviceId: { exact: id } }) : audio });
  let st = null;
  if(saved) try{ st = await open(saved); return st; }catch(e){ st = null; }
  st = await open("");
  const lab = (st.getAudioTracks()[0] || {}).label || "";
  if(MIC_BAD.test(lab)){
    const list = await micList();
    const good = list.find(d => /macbook|built-?in|内建|internal|内置/i.test(d.label) && !MIC_BAD.test(d.label)) || list.find(d => d.label && d.deviceId !== "default" && !MIC_BAD.test(d.label));
    if(good) try{ const s2 = await open(good.deviceId); st.getTracks().forEach(t => t.stop()); return s2; }catch(e){}
  }
  return st;
}
/* ô chọn micro (đặt trong trang) */
function micPicker(id){ return `<label class="pr-mic">🎙 Micro: <select id="${id}"><option value="">Tự động (tránh micro ảo)</option></select></label>`; }
async function micBind(id){
  const sel = document.getElementById(id); if(!sel) return;
  const list = await micList(), cur = micSaved();
  list.filter(d => d.deviceId !== "default").forEach((d, i) => { const o = document.createElement("option"); o.value = d.deviceId; o.textContent = (d.label || "Micro " + (i + 1)) + (MIC_BAD.test(d.label) ? " ⚠ ảo" : ""); sel.appendChild(o); });
  if(cur && [...sel.options].some(o => o.value === cur)) sel.value = cur;
  sel.onchange = () => { try{ sel.value ? localStorage.setItem("ww_mic", sel.value) : localStorage.removeItem("ww_mic"); }catch(e){} if(typeof MIC !== "undefined" && MIC && MIC.stream){ try{ MIC.stream.getTracks().forEach(t => t.stop()); }catch(e){} } };
}
const PronRec = {
  cur: null,
  mime(){ return ["audio/webm;codecs=opus", "audio/webm", "audio/mp4", "audio/ogg;codecs=opus"].find(m => window.MediaRecorder && MediaRecorder.isTypeSupported(m)) || ""; },
  ok(){ return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder); },
  /* bắt đầu ghi; trả về Promise<Blob|null> khi dừng (tự dừng sau maxSec giây) */
  async start(maxSec = 20, onTick){
    this.cancel();
    if(typeof stopAnyRecording === "function") stopAnyRecording();
    /* đo âm lượng trực tiếp từ micro (tạo AudioContext ngay trong lúc bấm để iPhone không chặn) */
    let ac = null; try{ ac = new (window.AudioContext || window.webkitAudioContext)(); if(ac.resume) ac.resume().catch(() => {}); }catch(e){ ac = null; }
    let stream;
    try{ stream = await pickMic({ echoCancellation: true, noiseSuppression: false, autoGainControl: true }); }
    catch(e){ if(ac) try{ ac.close(); }catch(x){} throw e; }
    const dev = ((stream.getAudioTracks()[0] || {}).label || "").trim();
    let an = null; const fb = new Float32Array(1024), lv = { peak: 0 };
    if(ac) try{ const src = ac.createMediaStreamSource(stream); an = ac.createAnalyser(); an.fftSize = 1024; src.connect(an); }catch(e){ an = null; }
    const mime = this.mime(); let mr;
    try{ mr = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined); }catch(e){ stream.getTracks().forEach(t => t.stop()); if(ac) try{ ac.close(); }catch(x){} throw e; }
    const chunks = []; mr.ondataavailable = e => { if(e.data && e.data.size) chunks.push(e.data); };
    const t0 = Date.now(); let keep = true;
    const done = new Promise(res => mr.onstop = () => {
      stream.getTracks().forEach(t => t.stop()); clearInterval(tk); this.cur = null;
      const metered = !!an && ac && ac.state === "running"; if(ac) try{ ac.close(); }catch(x){}
      if(!(keep && chunks.length)) return res(null);
      const b = new Blob(chunks, { type: mr.mimeType || mime || "audio/webm" }); b._peak = lv.peak; b._metered = metered; b._dev = dev; res(b); });
    const tk = setInterval(() => {
      let m = 0; if(an){ an.getFloatTimeDomainData(fb); for(let i = 0; i < fb.length; i++){ const v = Math.abs(fb[i]); if(v > m) m = v; } if(m > lv.peak) lv.peak = m; }
      const s = (Date.now() - t0) / 1000; if(onTick) onTick(s, m); if(s >= maxSec && mr.state === "recording") mr.stop(); }, 100);
    mr.start(); /* không chia nhỏ: Safari ghi mp4 theo từng mảnh sẽ giải mã ra im lặng */
    this.cur = { stop: (cancel) => { if(cancel) keep = false; if(mr.state === "recording") mr.stop(); }, done };
    return done;
  },
  stop(){ if(this.cur) this.cur.stop(false); },
  /* lời nhắc khi micro không thu được tiếng */
  silentMsg(r, who = "em"){
    const mac = /Mac/.test(navigator.platform || navigator.userAgent), win = /Win/.test(navigator.platform || "");
    const dev = r.dev ? `\n\nMicro trình duyệt đang dùng: “${r.dev}”.` : "";
    if(r.zero) return `Micro không thu được tiếng nào (tín hiệu bằng 0) – thường do máy tính đang chặn trình duyệt dùng micro.${dev}\n\n` +
      (mac ? "Cách sửa trên Mac: ⌘ Apple → Cài đặt hệ thống → Quyền riêng tư & Bảo mật → Micro → bật cho Google Chrome (hoặc Safari). Sau đó THOÁT HẲN trình duyệt (⌘Q) rồi mở lại trang."
        : win ? "Cách sửa trên Windows: Cài đặt → Quyền riêng tư & bảo mật → Micro → bật “Cho phép ứng dụng truy cập micro” và bật cho trình duyệt, rồi mở lại trình duyệt."
        : "Hãy kiểm tra quyền micro của trình duyệt trong cài đặt máy, rồi mở lại trình duyệt.");
    return `Micro thu được tiếng rất nhỏ, gần như im lặng.${dev}\n\nCó thể trình duyệt đang chọn nhầm micro (ví dụ tai nghe Bluetooth chưa kết nối hoặc micro ảo). Bấm biểu tượng 🎤 / 🔒 cạnh thanh địa chỉ → chọn đúng micro (micro tích hợp của máy), rồi ghi lại nhé.`;
  },
  cancel(){ if(this.cur) this.cur.stop(true); },
  /* cắt khoảng lặng đầu/cuối, chuẩn hoá âm lượng, đổi sang MP3 (nhẹ, máy nào cũng phát được) */
  async toMp3(blob){
    const quiet = blob._metered && blob._peak < 0.004, sil = { blob, silent: true, zero: blob._peak === 0, dev: blob._dev };
    try{
      let ctx; try{ ctx = new (window.AudioContext || window.webkitAudioContext)({ sampleRate: 24000 }); }catch(e){ ctx = new (window.AudioContext || window.webkitAudioContext)(); }
      const buf = await ctx.decodeAudioData(await blob.arrayBuffer()); try{ ctx.close(); }catch(e){}
      const rate = buf.sampleRate, n = buf.length, pcm = new Float32Array(n), chs = buf.numberOfChannels;
      for(let c = 0; c < chs; c++){ const d = buf.getChannelData(c); for(let k = 0; k < n; k++) pcm[k] += d[k] / chs; }
      let peak = 0; for(let k = 0; k < n; k++) peak = Math.max(peak, Math.abs(pcm[k]));
      /* giải mã ra im lặng nhưng micro có tiếng (lỗi giải mã của trình duyệt) → giữ nguyên file gốc */
      if(peak < 0.003) return blob._metered && blob._peak < 0.01 ? sil : { blob };
      const th = Math.max(0.015, peak * 0.06), pad = Math.round(rate * 0.25);
      let a = 0, b = n - 1; while(a < n && Math.abs(pcm[a]) < th) a++; while(b > a && Math.abs(pcm[b]) < th) b--;
      const seg = pcm.subarray(Math.max(0, a - pad), Math.min(n, b + pad));
      const g = Math.min(4, 0.9 / peak); for(let k = 0; k < seg.length; k++) seg[k] *= g;
      return { blob: await KTAudio.mp3(seg, rate), dur: seg.length / rate };
    }catch(e){ return quiet ? sil : { blob }; }
  }
};
function pronB64(blob){ return new Promise(r => { const fr = new FileReader(); fr.onload = () => r(String(fr.result).split(",")[1] || ""); fr.onerror = () => r(""); fr.readAsDataURL(blob); }); }
function pronBlob(r){ const bin = atob(r.data), u8 = new Uint8Array(bin.length); for(let i = 0; i < bin.length; i++) u8[i] = bin.charCodeAt(i); return new Blob([u8], { type: r.mime || "audio/mpeg" }); }
function pronTime(ms){ return ms ? new Date(ms).toLocaleString("vi-VN", { hour: "2-digit", minute: "2-digit", day: "2-digit", month: "2-digit" }) : ""; }
/* phát 1 file: url trực tiếp từ Drive, lỗi thì xin Apps Script gửi dữ liệu về */
const PronPlayer = {
  el: null, btn: null, loading: null, cache: {},
  stop(){ if(this.el){ this.el.pause(); this.el = null; } if(this.btn){ this.btn.classList.remove("on"); this.btn = null; } },
  /* src: link trực tiếp; fetchB64: hàm xin Apps Script gửi dữ liệu (dùng khi không có link / link lỗi); ck: khoá lưu tạm */
  async play(src, btn, fetchB64, ck){
    if(btn && this.loading === btn) return;               // đang tải: bấm thêm không huỷ
    const same = this.btn && this.btn === btn; this.stop(); if(same) return;
    if(typeof BGM !== "undefined" && BGM.dip) try{ BGM.dip(""); }catch(e){}
    if(!src && ck && this.cache[ck]) src = this.cache[ck];
    const el = new Audio(); this.el = el; this.btn = btn; if(btn) btn.classList.add("on");
    const end = () => { if(this.el === el) this.stop(); };
    const inline = url => { /* trình duyệt chặn tự phát → hiện trình phát để bấm */
      const row = btn && btn.closest(".pa-sub,.pr-row,.pa-ref"); if(!row) return end();
      let au = row.querySelector("audio.pp-inline"); if(!au){ au = document.createElement("audio"); au.className = "pp-inline"; au.controls = true; row.appendChild(au); }
      au.src = url; end(); };
    el.onended = end;
    let tried = false;
    el.onerror = async () => {
      if(tried || !fetchB64 || this.el !== el){ end(); return; } tried = true;
      this.loading = btn; if(btn){ btn.classList.add("loading"); btn.disabled = true; }
      let r; try{ r = await fetchB64(); }catch(e){ r = { ok: false, error: "network" }; }
      this.loading = null; if(btn){ btn.classList.remove("loading"); btn.disabled = false; }
      if(!r || !r.ok || !r.data){ end(); alert("Chưa tải được file ghi âm (" + ((r && r.error) || "lỗi mạng") + "). Thử bấm lại sau vài giây."); return; }
      const url = URL.createObjectURL(pronBlob(r)); if(ck) this.cache[ck] = url;
      if(this.el !== el) return;
      el.src = url; el.play().catch(() => inline(url));
    };
    if(src){ el.src = src; el.play().catch(err => { if(err && err.name === "NotAllowedError") inline(src); else if(el.onerror) el.onerror(); }); }
    else el.onerror();
  }
};

const Pron = {
  refs: {}, mine: {}, local: {}, busy: {}, les: null, lv: "", n: 0,
  has(lv, n){ return !!(PRON_SENT[lv] && PRON_SENT[lv][n]); },
  items(lv, n){
    const L = LEVELS[lv], les = L && L.lessons[n]; if(!les) return [];
    const seen = new Set(), out = [];
    (les.vocab || []).forEach(w => { if(!w.h || seen.has(w.h)) return; seen.add(w.h); out.push({ k: "w:" + w.h, zh: w.h, py: w.p || "", pos: POS[w.pos] || "", vi: w.vi || "" }); });
    (PRON_SENT[lv][n] || []).forEach(s => out.push({ k: "s:" + s[0], zh: s[0], py: s[1], vi: s[2], sent: true }));
    return out;
  },
  user(){ const a = Auth.get(); return a && a.u && a.token ? a : null; },
  key(){ return this.lv + ":" + this.n; },
  stat(lv, n, k){ const t = PRON_STATIC[lv] && PRON_STATIC[lv][n]; return t && t[k] || ""; },
  async load(force){
    const k = this.key(), lv = this.lv, n = this.n;
    if(!Track.on()) return;
    const jobs = [];
    if(force || !this.refs[k]) jobs.push(Auth.call("pronRef", { level: lv, lesson: n }, 30000).then(r => { if(r.ok) this.refs[k] = r.refs || {}; }));
    const a = this.user();
    if(a && (force || !this.mine[k])) jobs.push(Auth.call("pronMine", { u: a.u, token: a.token, level: lv, lesson: n }, 30000).then(r => { if(r.ok) this.mine[k] = r.mine || {}; }));
    await Promise.all(jobs);
    const m = this.mine[k] || {};
    if(a && Object.values(m).some(x => x.comment && x.cAt > (x.seen || 0))) Auth.call("pronSeen", { u: a.u, token: a.token, level: lv, lesson: n });
  },
  mount(les){
    this.les = les; this.lv = S.level; this.n = S.lesson;
    this.render();
    this.load().then(() => { if(this.lv === S.level && this.n === S.lesson && S.section === "pron") this.render(); });
  },
  render(){
    const W = $("#work"); if(!W) return;
    const k = this.key(), refs = this.refs[k] || {}, mine = this.mine[k] || {}, loc = this.local[k] || {}, a = this.user();
    const items = this.items(this.lv, this.n), words = items.filter(x => !x.sent), sents = items.filter(x => x.sent);
    const unsent = Object.keys(loc).length, newC = Object.values(mine).filter(x => x.comment && x.cAt > (x.seen || 0)).length;
    const row = x => {
      const m = mine[x.k], l = loc[x.k], busy = this.busy[x.k];
      return `<div class="pr-row${x.sent ? " sent" : ""}" data-k="${esc(x.k)}">
        <div class="pr-main"><span class="pr-zh han">${esc(x.zh)}</span>${x.pos ? `<span class="pr-pos">${esc(x.pos)}</span>` : ""}<span class="pr-py">${esc(x.py)}</span><span class="pr-vi">${esc(x.vi)}</span></div>
        <div class="pr-acts">
          ${this.refBtns(x.k, refs)}
          <button class="btn sm pr-rec" data-a="rec" ${PronRec.ok() ? "" : "disabled"}>${ICON.mic}<span>${l || m ? "Ghi lại" : "Ghi âm"}</span></button>
          ${l || m ? `<button class="btn sm" data-a="me">${ICON.play}Nghe giọng em</button>` : ""}
          ${l ? `<button class="btn sm primary" data-a="send" ${busy ? "disabled" : ""}>${busy ? "Đang nộp…" : "Nộp cho cô"}</button>` : ""}
        </div>
        <div class="pr-st">${l ? `<span class="pr-tag warn">Chưa nộp bản mới</span>` : m ? `<span class="pr-tag ok">✓ Đã nộp ${pronTime(m.at)}</span>` : ""}${m && !m.comment && !l ? `<span class="pr-tag">Chờ cô nhận xét</span>` : ""}</div>
        ${m && m.comment ? `<div class="pr-cmt${m.cAt > (m.seen || 0) ? " new" : ""}"><b>💬 Cô nhận xét</b>${m.cAt > (m.seen || 0) ? `<span class="pr-new">Mới</span>` : ""}<p>${esc(m.comment)}</p></div>` : ""}
      </div>`;
    };
    W.innerHTML = `<div class="pr">
      <div class="pr-head"><div><h2 class="han">语音练习 <small>Luyện ngữ âm – phát âm</small></h2>
        <p class="muted">Bấm <b>Giọng nam / Giọng nữ</b> để nghe mẫu → <b>Ghi âm</b> (bấm lần nữa để dừng) → <b>Nghe giọng em</b> để tự so sánh → <b>Nộp cho cô</b>. Cô sẽ nghe và nhận xét từng từ, từng câu.</p></div>
        <div class="pr-tools">${micPicker("prMic")}${this.sending ? `<button class="btn primary" id="prAll" disabled>Đang nộp ${this.sending.i}/${this.sending.n}… (đừng tắt trang)</button>` : unsent && a ? `<button class="btn primary" id="prAll">Nộp tất cả (${unsent})</button>` : ""}</div></div>
      ${!Track.on() ? `<div class="fm-note">Trang chưa nối với Google Sheet của giáo viên nên chưa nộp bài được. Em vẫn có thể tự ghi âm và nghe lại.</div>`
        : !a ? `<div class="fm-note">Em đang dùng bản học thử. <b>Đăng ký / đăng nhập</b> tài khoản để nộp bài ghi âm cho cô và xem cô nhận xét.</div>` : ""}
      ${newC ? `<div class="fm-note pr-note">💬 Cô vừa nhận xét ${newC} mục – xem các khung màu vàng bên dưới.</div>` : ""}
      ${!PronRec.ok() ? `<div class="fm-note">Trình duyệt này chưa hỗ trợ ghi âm. Em mở trang bằng Chrome hoặc Safari bản mới nhé.</div>` : ""}
      <h3 class="pr-h">Từ mới <small>${words.length} từ</small></h3><div class="pr-list">${words.map(row).join("")}</div>
      <h3 class="pr-h">Câu chính <small>${sents.length} câu</small></h3><div class="pr-list">${sents.map(row).join("")}</div>
    </div>`;
    W.querySelectorAll(".pr-row [data-a]").forEach(b => b.onclick = () => this.act(b.closest(".pr-row").dataset.k, b.dataset.a, b));
    const all = $("#prAll"); if(all && !this.sending) all.onclick = () => this.sendAll(all);
    micBind("prMic");
  },
  item(k){ return this.items(this.lv, this.n).find(x => x.k === k); },
  /* nút nghe mẫu: giọng nam / giọng nữ (file có sẵn), giọng cô (cô ghi trong khu giáo viên), hoặc giọng máy */
  refBtns(k, refs){
    const st = this.stat(this.lv, this.n, k), b = (v, l, t) => `<button class="btn sm pr-ref" data-a="ref" data-v="${v}" title="${t}">${ICON.sound}${l}</button>`;
    let h = "";
    if(st && st.m) h += b("m", "Giọng nam", "Nghe giọng nam đọc mẫu");
    if(st && st.f) h += b("f", "Giọng nữ", "Nghe giọng nữ đọc mẫu");
    if(refs[k]) h += b("c", "Giọng cô", "Nghe audio cô ghi âm");
    return h || b("tts", "Nghe (giọng máy)", "Chưa có audio mẫu – tạm nghe giọng máy");
  },
  async act(k, a, btn){
    const K = this.key(), x = this.item(k); if(!x) return;
    if(a === "ref"){
      const v = btn.dataset.v, id = (this.refs[K] || {})[k], st = this.stat(this.lv, this.n, k);
      if(v === "c" && id) return PronPlayer.play(audioSrc({ id }), btn, () => Auth.call("audio", { id }, 60000));
      if(st && st[v]) return PronPlayer.play(st[v], btn);
      PronPlayer.stop(); return speak(x.zh);
    }
    if(a === "me"){
      const l = (this.local[K] || {})[k];
      if(l) return PronPlayer.play(l.url, btn);
      const u = this.user(); if(!u) return;
      return PronPlayer.play("", btn, () => Auth.call("pronMyAudio", { u: u.u, token: u.token, level: this.lv, lesson: this.n, item: k }, 90000), "me|" + this.lv + this.n + k + "|" + ((this.mine[K] || {})[k] || {}).at);
    }
    if(a === "rec"){
      if(PronRec.cur && btn.classList.contains("rec")){ PronRec.stop(); return; }
      PronPlayer.stop();
      document.querySelectorAll(".pr-rec.rec").forEach(b => b.classList.remove("rec"));
      const lab = btn.querySelector("span"); btn.classList.add("rec"); lab.textContent = "Dừng (0s)";
      let blob;
      try{ blob = await PronRec.start(x.sent ? 20 : 8, (s, m) => { lab.textContent = `Dừng (${Math.floor(s)}s)`; btn.style.setProperty("--lv", Math.min(1, m * 3).toFixed(2)); }); }
      catch(e){ btn.classList.remove("rec"); lab.textContent = "Ghi âm"; return alert("Chưa ghi âm được: em cần cho phép trang dùng micro (bấm biểu tượng 🔒 cạnh thanh địa chỉ → Micro → Cho phép)."); }
      btn.classList.remove("rec"); lab.textContent = "Đang xử lý…";
      if(!blob){ this.render(); return; }
      const r = await PronRec.toMp3(blob);
      if(r.silent){ this.render(); return alert(PronRec.silentMsg(r)); }
      const loc = this.local[K] = this.local[K] || {};
      if(loc[k]) URL.revokeObjectURL(loc[k].url);
      loc[k] = { blob: r.blob, url: URL.createObjectURL(r.blob) };
      this.render();
      const me = document.querySelector(`.pr-row[data-k="${CSS.escape(k)}"] [data-a="me"]`); if(me) PronPlayer.play(loc[k].url, me);
      return;
    }
    if(a === "send") return this.send(k);
  },
  async send(k, quiet){
    const K = this.key(), lv = this.lv, n = this.n, loc = this.local[K] || {}, l = loc[k], u = this.user(), x = this.item(k);
    if(!l || !u || this.busy[k]) return false;
    if(!Track.on()){ alert("Trang chưa nối với Google Sheet của giáo viên."); return false; }
    this.busy[k] = true; if(!quiet) this.render();
    const data = await pronB64(l.blob);
    const body = { u: u.u, token: u.token, level: lv, lesson: n, item: k, text: x ? x.zh : "", mime: l.blob.type || "audio/mpeg", data };
    let r = await Auth.call("pronSubmit", body, 120000);
    if(!r.ok && !quiet && r.error !== "auth" && r.error !== "too_large"){ await new Promise(z => setTimeout(z, 2000)); r = await Auth.call("pronSubmit", body, 120000); }
    delete this.busy[k];
    if(r.ok){
      URL.revokeObjectURL(l.url); delete loc[k];
      const m = this.mine[K] = this.mine[K] || {}; m[k] = { id: r.id, at: r.at || Date.now(), comment: "", cAt: 0, seen: 0 };
      try{ Track.log("pron", { item: x ? x.zh : k }, `${lv}-${n}`); }catch(e){}
    } else if(!quiet) alert(r.error === "auth" ? "Phiên đăng nhập đã hết hạn. Em đăng nhập lại rồi nộp nhé." : r.error === "too_large" ? "Bản ghi quá dài. Em ghi ngắn lại nhé." : "Chưa nộp được (" + (r.error || "lỗi mạng") + "). Em thử lại nhé.");
    if(this.lv === lv && this.n === n && S.section === "pron") this.render();
    return !!r.ok;
  },
  async sendAll(btn){
    const ks = Object.keys(this.local[this.key()] || {}); if(!ks.length) return;
    let ok = 0; this.sending = { i: 0, n: ks.length };
    for(let i = 0; i < ks.length; i++){ this.sending.i = i + 1; const b = $("#prAll"); if(b){ b.disabled = true; b.textContent = `Đang nộp ${i + 1}/${ks.length}… (đừng tắt trang)`; }
      let done = false; for(let t = 0; t < 3 && !done; t++){ if(t) await new Promise(r => setTimeout(r, 2000 * t)); done = await this.send(ks[i], true); }
      if(done) ok++; }
    this.sending = null; this.render();
    alert(ok === ks.length ? `✓ Đã nộp xong ${ok}/${ks.length} bản ghi cho cô.` : `Đã nộp ${ok}/${ks.length}. Các mục còn “Chưa nộp bản mới” em bấm “Nộp tất cả” lần nữa nhé.`);
  },
  stop(){ PronRec.cancel(); PronPlayer.stop(); }
};

/* ---------- Khu giáo viên: tab “Ngữ âm” ---------- */
const PronAdmin = {
  tab: "subs", subs: null, msg: "", lv: "", n: 1, refs: {}, rec: null, f: { lv: "all", n: "all", st: "todo", q: "" }, open: {},
  levels(){ return Object.keys(PRON_SENT).filter(lv => LEVELS[lv]); },
  presets(){ let c = []; try{ c = JSON.parse(localStorage.getItem("ww_t_presets") || "[]"); }catch(e){} return { base: PRON_PRESETS, custom: Array.isArray(c) ? c : [] }; },
  savePresets(c){ try{ localStorage.setItem("ww_t_presets", JSON.stringify(c.slice(0, 40))); }catch(e){} },
  label(lv, n){ const L = LEVELS[lv]; return `${L ? L.name.replace(/\s*·.*$/, "") : lv} · Bài ${n}`; },
  lvName(lv){ return lv === "hsk1" ? "HSK 1" : lv === "gt1" ? "Giao tiếp sơ cấp 1" : (LEVELS[lv] && LEVELS[lv].full) || lv; },
  async render(){
    if(!this.lv) this.lv = this.levels()[0] || "hsk1";
    const B = $("#tBody");
    const seg = `<div class="seg pa-seg" role="group"><button data-pt="subs" aria-pressed="${this.tab === "subs"}">Bài nộp của học viên</button><button data-pt="ref" aria-pressed="${this.tab === "ref"}">Audio mẫu của cô</button></div>`;
    B.innerHTML = Teacher.topbar("Luyện ngữ âm", "Đang tải…") + `<div class="panel">${seg}<p class="muted">Đang tải…</p></div>`; Teacher.bindTop();
    if(this.tab === "ref") return this.renderRef();
    if(!this.subs){ const r = await Auth.call("pronSubs", { key: Teacher.key }, 60000); this.subs = r.ok ? r.subs || [] : []; if(!r.ok) this.msg = "Chưa tải được bài nộp (" + (r.error || "lỗi mạng") + "). Nếu vừa cập nhật Apps Script, nhớ Triển khai → Quản lý bản triển khai → Phiên bản mới."; }
    this.renderSubs();
  },
  bindSeg(){ document.querySelectorAll("#tBody [data-pt]").forEach(b => b.onclick = () => { if(this.tab === b.dataset.pt) return; this.stopRec(); PronPlayer.stop(); this.tab = b.dataset.pt; this.render(); }); },
  head(sub){ return Teacher.topbar("Luyện ngữ âm", sub) + (this.msg ? `<div class="fm-note">${esc(this.msg)}</div>` : ""); },
  /* ----- bài nộp ----- */
  renderSubs(){
    const B = $("#tBody"), f = this.f, all = this.subs || [], q = f.q.trim().toLowerCase();
    const todo = all.filter(s => !s.comment).length;
    const list = all.filter(s => (f.lv === "all" || s.level === f.lv) && (f.n === "all" || s.lesson === +f.n) && (f.st === "all" || (f.st === "todo" ? !s.comment : !!s.comment))
      && (!q || [s.name, s.u].some(v => (v || "").toLowerCase().includes(q)))).sort((a, b) => b.at - a.at);
    const groups = new Map(); list.forEach(s => { const g = s.u + "|" + s.level + "|" + s.lesson; if(!groups.has(g)) groups.set(g, []); groups.get(g).push(s); });
    const P = this.presets();
    const chip = (t, i, custom) => `<span class="pa-chip"><button type="button" data-ps="${esc(t)}">${esc(t)}</button>${custom ? `<button type="button" class="pa-chipx" data-pdel="${i}" title="Xoá mẫu này">×</button>` : ""}</span>`;
    const opt = (v, l, cur) => `<option value="${v}" ${String(cur) === String(v) ? "selected" : ""}>${esc(l)}</option>`;
    B.innerHTML = this.head(`${all.length} bài ghi âm · <b>${todo}</b> bài chưa nhận xét`) + `
      <div class="panel pa">
        <div class="pa-bar"><div class="seg pa-seg" role="group"><button data-pt="subs" aria-pressed="true">Bài nộp của học viên</button><button data-pt="ref" aria-pressed="false">Audio mẫu của cô</button></div></div>
        <div class="pa-filter">
          <select class="inp" id="paLv">${opt("all", "Tất cả lớp", f.lv)}${this.levels().map(lv => opt(lv, this.lvName(lv), f.lv)).join("")}</select>
          <select class="inp" id="paN">${opt("all", "Tất cả bài", f.n)}${[1, 2, 3, 4, 5].map(n => opt(n, "Bài " + n, f.n)).join("")}</select>
          <select class="inp" id="paSt">${opt("todo", "Chưa nhận xét", f.st)}${opt("done", "Đã nhận xét", f.st)}${opt("all", "Tất cả", f.st)}</select>
          <input class="inp" id="paQ" placeholder="Tìm học viên…" value="${esc(f.q)}">
          <button class="btn" id="paRe">${ICON.redo}Tải lại</button>
        </div>
        <details class="pa-pre"><summary>Câu nhận xét mẫu (${P.base.length + P.custom.length}) – bấm vào câu mẫu trong từng bài để chèn</summary>
          <div class="pa-chips">${P.base.map(t => chip(t)).join("")}${P.custom.map((t, i) => chip(t, i, true)).join("")}</div>
          <div class="pa-addp"><input class="inp" id="paNewP" placeholder="Soạn câu mẫu mới của cô…"><button class="btn" id="paAddP">＋ Thêm câu mẫu</button></div></details>
        ${groups.size ? [...groups.values()].map(g => { const s0 = g[0];
          return `<div class="pa-grp"><div class="pa-gh"><b>${esc(s0.name || s0.u)}</b><small>@${esc(s0.u)} · ${esc(this.label(s0.level, s0.lesson))} · ${g.length} mục</small></div>
          ${g.map(s => `<div class="pa-sub${s.comment ? " done" : ""}" data-k="${esc(s.k)}">
            <div class="pa-s1"><button class="btn sm pa-play" data-play>${ICON.play}Nghe</button>
              <div class="pa-txt"><span class="han">${esc(s.text || s.item.slice(2))}</span><small>${s.item.startsWith("s:") ? "Câu" : "Từ"} · nộp ${pronTime(s.at)}${s.comment ? ` · đã nhận xét ${pronTime(s.cAt)}${s.seen ? " · HV đã xem" : ""}` : ""}</small></div>
              ${this.refBtn(s)}</div>
            <div class="pa-c">
              <div class="pa-chips sm">${P.base.concat(P.custom).map(t => `<button type="button" data-ins="${esc(t)}">${esc(t.length > 38 ? t.slice(0, 36) + "…" : t)}</button>`).join("")}</div>
              <textarea class="inp pa-ta" rows="2" placeholder="Nhận xét của cô (bấm câu mẫu ở trên để chèn, hoặc tự soạn)…">${esc(s.comment)}</textarea>
              <div class="pa-cacts"><span class="pa-ok"></span><button class="btn sm" data-keep title="Lưu câu đang soạn thành câu mẫu để dùng lại">☆ Lưu làm câu mẫu</button><button class="btn sm primary" data-save>Lưu nhận xét</button></div>
            </div></div>`).join("")}</div>`; }).join("")
          : `<p class="t-dim" style="padding:20px 4px">${all.length ? "Không có bài nộp nào khớp bộ lọc." : "Chưa có học viên nào nộp bài ghi âm."}</p>`}
      </div>`;
    this.msg = ""; Teacher.bindTop(); this.bindSeg();
    const re = () => this.renderSubs();
    $("#paLv").onchange = e => { f.lv = e.target.value; re(); };
    $("#paN").onchange = e => { f.n = e.target.value; re(); };
    $("#paSt").onchange = e => { f.st = e.target.value; re(); };
    $("#paQ").oninput = e => { f.q = e.target.value; clearTimeout(this.qt); this.qt = setTimeout(() => { re(); const i = $("#paQ"); i.focus(); i.setSelectionRange(i.value.length, i.value.length); }, 350); };
    $("#paRe").onclick = () => { this.subs = null; this.render(); };
    $("#paAddP").onclick = () => { const v = $("#paNewP").value.trim(); if(!v) return; const c = this.presets().custom; if(!c.includes(v)) c.push(v); this.savePresets(c); re(); };
    B.querySelectorAll("[data-pdel]").forEach(b => b.onclick = () => { const c = this.presets().custom; c.splice(+b.dataset.pdel, 1); this.savePresets(c); re(); });
    B.querySelectorAll(".pa-pre [data-ps]").forEach(b => b.onclick = () => { navigator.clipboard && navigator.clipboard.writeText(b.dataset.ps).catch(() => {}); b.classList.add("on"); setTimeout(() => b.classList.remove("on"), 600); });
    B.querySelectorAll(".pa-sub").forEach(el => {
      const k = el.dataset.k, s = all.find(x => x.k === k), ta = el.querySelector(".pa-ta"), ok = el.querySelector(".pa-ok");
      el.querySelector("[data-play]").onclick = e => PronPlayer.play("", e.currentTarget, () => Auth.call("pronAudio", { key: Teacher.key, k }, 90000), "t|" + k + "|" + s.at);
      const rb = el.querySelector("[data-ref]"); if(rb) rb.onclick = e => { const id = rb.dataset.ref; PronPlayer.play(audioSrc({ id }), e.currentTarget, () => Auth.call("audio", { id }, 60000)); };
      const sbt = el.querySelector("[data-st]"); if(sbt) sbt.onclick = e => PronPlayer.play(sbt.dataset.st, e.currentTarget);
      el.querySelectorAll("[data-ins]").forEach(b => b.onclick = () => { const t = b.dataset.ins, v = ta.value.trim(); ta.value = v ? (v.includes(t) ? v : v + " " + t) : t; ta.focus(); });
      el.querySelector("[data-keep]").onclick = () => { const v = ta.value.trim(); if(!v) return; const c = this.presets().custom; if(!c.includes(v)){ c.push(v); this.savePresets(c); } ok.textContent = "Đã lưu làm câu mẫu"; };
      el.querySelector("[data-save]").onclick = async e => {
        const b = e.currentTarget; b.disabled = true; ok.textContent = "Đang lưu…";
        const r = await Auth.call("pronComment", { key: Teacher.key, k, comment: ta.value.trim() }, 30000);
        b.disabled = false;
        if(!r.ok){ ok.textContent = "Chưa lưu được: " + (r.error || "lỗi mạng"); return; }
        s.comment = ta.value.trim(); s.cAt = r.cAt || 0; s.seen = 0; ok.textContent = "✓ Đã lưu – học viên sẽ thấy trong bài"; el.classList.toggle("done", !!s.comment);
      };
    });
    this.loadRefsFor(list);
  },
  refBtn(s){ const id = (this.refs[s.level + ":" + s.lesson] || {})[s.item], st = Pron.stat(s.level, s.lesson, s.item); if(!id && st && (st.f || st.m)) return `<button class="btn sm ghost" data-st="${esc(st.f || st.m)}" title="Nghe audio mẫu">${ICON.sound}Mẫu</button>`; return id ? `<button class="btn sm ghost" data-ref="${esc(id)}" title="Nghe audio mẫu của cô">${ICON.sound}Mẫu</button>` : ""; },
  async loadRefsFor(list){
    const need = [...new Set(list.map(s => s.level + ":" + s.lesson))].filter(k => !this.refs[k]); if(!need.length) return;
    await Promise.all(need.map(k => { const [lv, n] = k.split(":"); return Auth.call("pronRef", { level: lv, lesson: +n }, 30000).then(r => { this.refs[k] = r.ok ? r.refs || {} : {}; }); }));
    if(Teacher.view === "na" && this.tab === "subs") document.querySelectorAll(".pa-sub").forEach(el => { const s = (this.subs || []).find(x => x.k === el.dataset.k); if(!s || el.querySelector("[data-ref]") || !(this.refs[s.level + ":" + s.lesson] || {})[s.item]) return; const old = el.querySelector("[data-st]"); if(old) old.remove();
      const h = this.refBtn(s); if(h){ el.querySelector(".pa-s1").insertAdjacentHTML("beforeend", h); const rb = el.querySelector("[data-ref]"); if(rb) rb.onclick = e => { const id = rb.dataset.ref; PronPlayer.play(audioSrc({ id }), e.currentTarget, () => Auth.call("audio", { id }, 60000)); }; } });
  },
  /* ----- audio mẫu ----- */
  async renderRef(force){
    const B = $("#tBody"), K = this.lv + ":" + this.n;
    if(force || !this.refs[K]){ const r = await Auth.call("pronRef", { level: this.lv, lesson: this.n }, 30000); this.refs[K] = r.ok ? r.refs || {} : {}; if(!r.ok) this.msg = "Chưa tải được audio mẫu (" + (r.error || "lỗi mạng") + ")."; }
    const refs = this.refs[K], items = Pron.items(this.lv, this.n), have = items.filter(x => refs[x.k] || Pron.stat(this.lv, this.n, x.k)).length;
    const opt = (v, l, cur) => `<option value="${v}" ${String(cur) === String(v) ? "selected" : ""}>${esc(l)}</option>`;
    const row = x => `<div class="pa-ref${refs[x.k] ? " has" : ""}" data-k="${esc(x.k)}">
        <div class="pa-txt"><span class="han">${esc(x.zh)}</span><small>${esc(x.py)}${x.pos ? " · " + esc(x.pos) : ""} · ${esc(x.vi)}</small></div>
        <div class="pa-racts">${refs[x.k] ? `<span class="pr-tag ok">✓ Cô đã ghi</span><button class="btn sm" data-a="play">${ICON.play}Giọng cô</button>` : Pron.stat(this.lv, this.n, x.k) ? `<span class="pr-tag ok">✓ File có sẵn</span>` : `<span class="pr-tag">Chưa có</span>`}${["m", "f"].filter(v => (Pron.stat(this.lv, this.n, x.k) || {})[v]).map(v => `<button class="btn sm" data-a="stat" data-v="${v}">${ICON.play}${v === "m" ? "Giọng nam" : "Giọng nữ"}</button>`).join("")}
          <button class="btn sm pa-rec" data-a="rec">${ICON.mic}<span>${refs[x.k] ? "Ghi lại" : "Ghi âm"}</span></button>
          <label class="btn sm pa-up">📁 Tải file<input type="file" accept="audio/*" hidden></label>
          ${refs[x.k] ? `<button class="btn sm ghost" data-a="del" title="Xoá audio mẫu">🗑</button>` : ""}</div>
        <div class="pa-prev"></div></div>`;
    B.innerHTML = this.head(`Audio mẫu: học viên nghe các file này khi bấm Giọng nam / Giọng nữ / Giọng cô`) + `
      <div class="panel pa">
        <div class="pa-bar"><div class="seg pa-seg" role="group"><button data-pt="subs" aria-pressed="false">Bài nộp của học viên</button><button data-pt="ref" aria-pressed="true">Audio mẫu của cô</button></div></div>
        <div class="pa-filter"><select class="inp" id="paRLv">${this.levels().map(lv => opt(lv, this.lvName(lv), this.lv)).join("")}</select>
          <select class="inp" id="paRN">${[1, 2, 3, 4, 5].map(n => opt(n, "Bài " + n + " – " + ((LEVELS[this.lv].lessons[n] || {}).zh || ""), this.n)).join("")}</select>
          <span class="muted">Đã ghi <b>${have}/${items.length}</b> mục</span>${micPicker("paMic")}</div>
        <p class="muted pa-tip">Bấm <b>Ghi âm</b>, đọc từ/câu, bấm lần nữa để dừng → nghe thử → <b>Lưu</b>. Trang tự cắt khoảng lặng đầu/cuối và đổi sang MP3. Cũng có thể tải lên file có sẵn (mp3, m4a…).</p>
        <h3 class="pr-h">Từ mới</h3>${items.filter(x => !x.sent).map(row).join("")}
        <h3 class="pr-h">Câu chính</h3>${items.filter(x => x.sent).map(row).join("")}
      </div>`;
    this.msg = ""; Teacher.bindTop(); this.bindSeg();
    micBind("paMic");
    $("#paRLv").onchange = e => { this.stopRec(); this.lv = e.target.value; this.renderRef(); };
    $("#paRN").onchange = e => { this.stopRec(); this.n = +e.target.value; this.renderRef(); };
    B.querySelectorAll(".pa-ref").forEach(el => {
      const k = el.dataset.k, prev = el.querySelector(".pa-prev");
      const pb = el.querySelector('[data-a="play"]'); if(pb) pb.onclick = e => { const id = refs[k]; PronPlayer.play(audioSrc({ id }), e.currentTarget, () => Auth.call("audio", { id }, 60000)); };
      el.querySelectorAll('[data-a="stat"]').forEach(sb => sb.onclick = e => PronPlayer.play(Pron.stat(this.lv, this.n, k)[sb.dataset.v], e.currentTarget));
      const db = el.querySelector('[data-a="del"]'); if(db) db.onclick = async () => { if(!confirm("Xoá audio mẫu của mục này?")) return; db.disabled = true; const r = await Auth.call("pronRefDel", { key: Teacher.key, level: this.lv, lesson: this.n, item: k }, 30000); if(r.ok) delete refs[k]; else alert("Chưa xoá được: " + (r.error || "lỗi mạng")); this.renderRef(); };
      const show = (blob, ext) => { const url = URL.createObjectURL(blob);
        prev.innerHTML = `<audio controls src="${url}"></audio><button class="btn sm primary" data-save>Lưu làm audio mẫu</button><button class="btn sm" data-cancel>Huỷ</button><span class="pa-ok"></span>`;
        prev.querySelector("audio").play().catch(() => {});
        prev.querySelector("[data-cancel]").onclick = () => { URL.revokeObjectURL(url); prev.innerHTML = ""; };
        prev.querySelector("[data-save]").onclick = async e => { const b = e.currentTarget, okEl = prev.querySelector(".pa-ok"); b.disabled = true; okEl.textContent = "Đang lưu…";
          const r = await Auth.call("pronRefSet", { key: Teacher.key, level: this.lv, lesson: this.n, item: k, mime: blob.type || "audio/mpeg", ext, data: await pronB64(blob) }, 120000);
          if(!r.ok){ b.disabled = false; okEl.textContent = "Chưa lưu được: " + (r.error || "lỗi mạng"); return; }
          refs[k] = r.id; URL.revokeObjectURL(url); this.renderRef(); }; };
      const rb = el.querySelector('[data-a="rec"]');
      rb.onclick = async () => {
        if(rb.classList.contains("rec")){ PronRec.stop(); return; }
        this.stopRec(); PronPlayer.stop();
        const lab = rb.querySelector("span"); rb.classList.add("rec"); lab.textContent = "Dừng (0s)"; this.rec = rb;
        let blob; try{ blob = await PronRec.start(25, (s, m) => { lab.textContent = `Dừng (${Math.floor(s)}s)`; rb.style.setProperty("--lv", Math.min(1, m * 3).toFixed(2)); }); }
        catch(e){ rb.classList.remove("rec"); lab.textContent = "Ghi âm"; return alert("Chưa ghi âm được: cần cho phép trang dùng micro."); }
        rb.classList.remove("rec"); this.rec = null;
        if(!blob){ lab.textContent = "Ghi âm"; return; }
        lab.textContent = "Đang xử lý…"; const r = await PronRec.toMp3(blob); lab.textContent = "Ghi lại";
        if(r.silent) return alert(PronRec.silentMsg(r, "cô"));
        show(r.blob, r.blob.type === "audio/mpeg" ? "mp3" : r.blob.type === "audio/wav" ? "wav" : "");
      };
      el.querySelector(".pa-up input").onchange = e => { const file = e.target.files[0]; if(!file) return;
        if(file.size > 1800000) return alert("File lớn quá (tối đa khoảng 1,8 MB). Cô cắt ngắn hoặc đổi sang MP3 nhé.");
        show(file, (file.name.match(/\.(\w+)$/) || [, ""])[1]); };
    });
  },
  stopRec(){ if(this.rec){ PronRec.cancel(); this.rec = null; } }
};
