/* ======================= VĂN HOÁ TRUNG QUỐC – game dẫn vào bài đọc ======================= */
/* bật/tắt mục Văn hoá TQ trên trang chủ (true = hiện) */
const CUL_ON = false;
const CUL_GAMES = [
  { id: "chunjie",   zh: "过年啦！",     py: "Guònián la!",       vi: "Tết Nguyên đán – đón năm mới cùng gia đình", tag: "春节" },
  { id: "zhongqiu",  zh: "月亮上的嫦娥", py: "Yuèliang shang de Cháng'é", vi: "Tết Trung thu – câu chuyện Hằng Nga", tag: "中秋节" },
  { id: "shengxiao", zh: "十二生肖",     py: "Shí'èr shēngxiào",  vi: "12 con giáp – cuộc đua qua sông", tag: "生肖" }
];
const Culture = {
  open(){
    this.close();
    const M = document.createElement("div"); M.className = "cul-modal"; M.id = "culModal";
    M.innerHTML = `<div class="cul-box" role="dialog" aria-modal="true" aria-label="Văn hoá Trung Quốc">
      <div class="cul-head"><div><h2><span class="han">中国文化</span> Văn hoá Trung Quốc</h2><p class="muted">Chơi game để tìm hiểu ngày lễ, phong tục của người Trung Quốc. Nhớ bật loa 🔊</p></div>
        <button class="btn sm" id="culX" aria-label="Đóng">✕</button></div>
      <div class="cul-grid">${CUL_GAMES.map(g => `<button class="cul-card" data-g="${g.id}">
        <img src="games/${g.id}.webp" alt="" loading="lazy"><span class="cul-tag han">${g.tag}</span>
        <b class="han">${g.zh}</b><small>${g.py}</small><span>${g.vi}</span><i>▶ Chơi</i></button>`).join("")}</div></div>`;
    document.body.appendChild(M);
    M.onclick = e => { if(e.target === M) this.close(); };
    M.querySelector("#culX").onclick = () => this.close();
    M.querySelectorAll("[data-g]").forEach(b => b.onclick = () => this.play(b.dataset.g));
    this.esc = e => { if(e.key === "Escape"){ if(document.getElementById("culPlay")) this.stop(); else this.close(); } };
    document.addEventListener("keydown", this.esc);
    try{ Track.log("culture_open", {}, ""); }catch(e){}
  },
  close(){ this.stop(); const M = document.getElementById("culModal"); if(M) M.remove(); if(this.esc) document.removeEventListener("keydown", this.esc); },
  play(id){
    const g = CUL_GAMES.find(x => x.id === id); if(!g) return;
    this.stop();
    if(typeof BGM !== "undefined"){ this.bgmHeld = BGM.held; BGM.held = true; try{ BGM.apply(.2); }catch(e){} }
    try{ if(window.speechSynthesis) speechSynthesis.cancel(); }catch(e){}
    const P = document.createElement("div"); P.className = "cul-play"; P.id = "culPlay";
    P.oncontextmenu = e => e.preventDefault();
    P.innerHTML = `<div class="cul-bar"><button class="btn sm" id="culBack">← Danh sách</button><b class="han">${g.zh}</b>
      ${document.fullscreenEnabled || document.webkitFullscreenEnabled ? `<button class="btn sm" id="culFs">⛶ Toàn màn hình</button>` : ""}</div>
      <div class="cul-rot">📱↻ Xoay ngang điện thoại để chơi to hơn</div>
      <iframe src="games/${g.id}.html" title="${g.zh}" allow="autoplay; fullscreen" allowfullscreen></iframe>`;
    document.body.appendChild(P);
    P.querySelector("#culBack").onclick = () => { if(document.fullscreenElement || document.webkitFullscreenElement){ try{ (document.exitFullscreen || document.webkitExitFullscreen).call(document); }catch(e){} } this.stop(); };
    const fs = P.querySelector("#culFs"); if(fs) fs.onclick = () => { const on = document.fullscreenElement || document.webkitFullscreenElement;
      try{ on ? (document.exitFullscreen || document.webkitExitFullscreen).call(document) : (P.requestFullscreen || P.webkitRequestFullscreen).call(P); }catch(e){} };
    try{ Track.log("culture_play", { game: id }, ""); }catch(e){}
  },
  stop(){
    const P = document.getElementById("culPlay"); if(!P) return;
    const f = P.querySelector("iframe"); if(f) f.src = "about:blank";
    P.remove();
    if(typeof BGM !== "undefined"){ BGM.held = !!this.bgmHeld; try{ BGM.apply(.4); }catch(e){} }
  }
};
