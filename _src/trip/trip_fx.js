/* ===== Khám phá TQ – phần mở rộng: HDV hoạt hình (Canva), bản đồ mới, hiệu ứng tranh,
   cảnh di chuyển giữa các điểm, vé máy bay, hộ chiếu & visa đóng dấu ===== */
const TRIP_GD = typeof TRIP_GD_DATA !== "undefined" ? TRIP_GD_DATA : {};

/* ---------- Hướng dẫn viên Tiểu Ngữ: thân + tay vẫy + miệng nói + chớp mắt ---------- */
function guideSVG(expr = "smile", cls = ""){
  if(!TRIP_GD.g_base) return "";
  const extra = expr === "think"
    ? `<g class="tg-q"><circle cx="372" cy="118" r="44" fill="#fff" stroke="#5B9BD5" stroke-width="7"/><text x="372" y="140" font-size="66" font-weight="800" fill="#5B9BD5" text-anchor="middle">?</text></g>`
    : expr === "happy" ? `<g class="tg-sp" fill="#F6C343"><path d="M370 92 l9 22 22 9 -22 9 -9 22 -9 -22 -22 -9 22 -9z"/><path d="M398 182 l5 12 12 5 -12 5 -5 12 -5 -12 -12 -5 12 -5z"/></g>` : "";
  return `<div class="tg tg-${expr} ${cls}" aria-hidden="true"><img class="tg-b" src="${TRIP_GD.g_base}" alt=""><img class="tg-a" src="${TRIP_GD.g_arm}" alt="">
    <svg class="tg-o" viewBox="0 0 450 600"><g class="tg-m"><ellipse cx="214" cy="259" rx="24" ry="18.5" fill="#FFDFC8"/><path d="M202 256 Q214 267 226 256" stroke="#B4544A" stroke-width="4.5" fill="none" stroke-linecap="round"/></g>
    <g class="tg-e"><ellipse cx="172" cy="223" rx="27" ry="26" fill="#FFDFC9"/><ellipse cx="263" cy="226" rx="27" ry="26" fill="#FFDFC9"/><path d="M149 228 Q172 241 195 228M240 231 Q263 244 286 231" stroke="#4A3328" stroke-width="5.5" fill="none" stroke-linecap="round"/></g>${extra}</svg></div>`;
}

/* ---------- Bản đồ mới (ảnh Canva 600×450, không có đường lưỡi bò) ---------- */
/* [x, y, lệch nhãn x, lệch nhãn y] theo hệ toạ độ 600×450 của ảnh bản đồ */
const TRIP_MAP = { bj: [400, 185, -96, -30], sh: [447, 263, 16, -26], hz: [437, 279, 18, 10], xa: [332, 247, -80, -46], cq: [309, 298, 14, -34],
  cd: [286, 286, -100, 30], sc: [272, 258, -112, -34], yn: [262, 335, -104, 26], gl: [344, 346, -86, 18], gz: [368, 372, 16, 14], gd: [382, 350, 18, -22] };
const TRIP_HOME = { x: 300, y: 446 };   /* xuất phát: Hà Nội (phía nam, ngoài khung) */
const TRIP_CODE = { bj: "PEK", sh: "PVG", cq: "CKG", yn: "KMG", hz: "HGH", xa: "XIY", gl: "KWL", sc: "JZH", cd: "CTU", gz: "CAN", gd: "SZX" };
function tripMapHTML(pinsSVG){
  return `<img class="tp-mapimg" src="${TRIP_GD.map}" alt="Bản đồ Trung Quốc"><svg class="tp-map-svg" viewBox="0 0 600 450" role="img" aria-label="Các trạm trên bản đồ">
    <path id="tpTrail" d="" fill="none" stroke="#E8453C" stroke-width="3.6" stroke-dasharray="4 8" stroke-linecap="round" opacity=".85"/>${pinsSVG}</svg>`;
}

/* ---------- Hiệu ứng động trong tranh ----------
   cloud:[y%] mây trôi · bird:y% chim bay · rip:[[x,y,rộng]] gợn nước · fish:[[x1,x2,y]] cá bơi
   fall:"autumn|green|petal|snow|dust" vật rơi/bay · steam:[[x,y]] hơi nóng · tw:[[x1,y1,x2,y2,số,màu]] lấp lánh · fount:[[x,y]] đài phun nước */
const TRIP_FX = {
  gugong: { cloud: [8, 20], bird: 22 }, changcheng: { cloud: [9, 22], bird: 30, fall: "autumn" }, tiantan: { cloud: [9, 24], bird: 32 },
  kaoya: { steam: [[42, 30], [55, 27]] }, tanghulu: { fall: "snow", tw: [[10, 5, 90, 90, 6, "#fff"]] },
  mingzhu: { tw: [[5, 3, 95, 38, 8, "#FFF6C8"]], rip: [[25, 88, 12], [52, 93, 12], [76, 87, 10]] }, waitan: { cloud: [9], bird: 24, rip: [[18, 82, 10], [45, 90, 14], [72, 86, 10]], steam: [[88, 72]] },
  yuyuan: { rip: [[28, 82, 10], [52, 90, 12], [78, 85, 10]], fish: [[18, 82, 86]], fall: "green" }, xiaolongbao: { steam: [[38, 28], [50, 24], [60, 28]] }, shengjian: { steam: [[40, 28], [55, 24]] },
  hongyadong: { tw: [[30, 12, 75, 70, 9, "#FFD27A"], [70, 2, 98, 35, 4, "#fff"]], rip: [[20, 92, 9], [42, 88, 12], [66, 93, 10]] },
  suodao: { cloud: [9], bird: 30, rip: [[45, 76, 10], [70, 72, 10], [30, 86, 9]] }, liziba: { cloud: [9], bird: 22, fall: "green" },
  huoguo: { steam: [[42, 33], [58, 33]] }, xiaomian: { steam: [[45, 24], [56, 20]] },
  shilin: { cloud: [7], bird: 18, rip: [[14, 84, 8], [30, 90, 9]], fish: [[6, 38, 88]] }, lijiang: { cloud: [7], rip: [[46, 64, 8], [55, 76, 10], [42, 90, 12]], fall: "petal" },
  yulong: { cloud: [10, 32], bird: 22 }, mixian: { steam: [[46, 12], [56, 9]] }, xianhuabing: { fall: "petal" },
  xihu: { cloud: [12], rip: [[30, 60, 12], [55, 70, 14], [75, 84, 10], [42, 82, 10]], fish: [[20, 70, 90]], fall: "green" },
  leifeng: { cloud: [8], bird: 30, rip: [[60, 80, 12], [76, 72, 10], [42, 92, 10]] }, duanqiao: { fall: "snow", rip: [[50, 92, 12], [24, 78, 8], [78, 82, 9]] },
  longjing: { steam: [[40, 34], [50, 30]], fall: "green" }, dongpo: { steam: [[38, 26], [50, 23]] },
  bingmayong: { fall: "dust" }, dayanta: { cloud: [8], fount: [[34, 80], [50, 82], [71, 80]] }, chengqiang: { cloud: [12], bird: 22 },
  roujiamo: { steam: [[45, 30], [56, 27]] }, paomo: { steam: [[45, 32], [56, 29]] },
  lijiangriver: { cloud: [14], bird: 24, rip: [[20, 72, 10], [50, 78, 12], [30, 92, 12], [80, 76, 10]], fish: [[8, 40, 90]] },
  xiangbishan: { cloud: [8], bird: 16, rip: [[20, 86, 10], [46, 93, 12], [80, 90, 10]] }, yangshuo: { cloud: [10], bird: 18, fall: "green" },
  guilinmifen: { steam: [[40, 30], [52, 28]] }, pijiuyu: { steam: [[40, 28], [52, 25]] },
  jiuzhaigou: { rip: [[46, 60, 12], [60, 48, 10], [40, 86, 14], [70, 80, 10]], fish: [[25, 75, 78]], fall: "autumn" },
  leshandafo: { bird: 14, rip: [[12, 80, 8], [30, 92, 10], [60, 96, 10]] }, emeishan: { cloud: [44, 60, 72], bird: 14, tw: [[58, 18, 72, 40, 4, "#FFF3B0"]] },
  mapodoufu: { steam: [[48, 30], [58, 27]] }, huiguorou: { steam: [[45, 35], [57, 32]] },
  pandajidi: { fall: "green" }, kuanzhai: { steam: [[38, 70], [86, 78]], fall: "green" }, bianlian: { tw: [[20, 10, 70, 80, 9, "#FFE27A"]] },
  dandanmian: { steam: [[44, 42], [54, 40]] }, bingfen: { tw: [[25, 15, 75, 70, 6, "#fff"]] },
  guangzhouta: { tw: [[0, 0, 100, 55, 10, "#fff"], [52, 10, 66, 70, 5, "#B9F3FF"]], rip: [[28, 86, 10], [58, 80, 12], [80, 90, 9]] },
  shamian: { fall: "green", bird: 14 }, chenjiaci: { cloud: [6], bird: 16 }, xiajiao: { steam: [[40, 30], [55, 28]] }, changfen: { steam: [[35, 32], [55, 27]] },
  danxia: { cloud: [7], bird: 15, rip: [[30, 74, 8], [55, 70, 8], [70, 56, 6]] }, diaolou: { cloud: [6], bird: 14 },
  gangzhuao: { cloud: [9], bird: 26, rip: [[20, 75, 10], [50, 88, 12], [76, 70, 10], [40, 62, 8]] }, shaoe: { steam: [[42, 24], [54, 21]] }, niurouwan: { steam: [[44, 38], [55, 35]] }
};
function tripRng(seed){ let h = 2166136261; for(const ch of seed) h = Math.imul(h ^ ch.charCodeAt(0), 16777619); return () => { h += 0x6D2B79F5; let t = h; t = Math.imul(t ^ t >>> 15, t | 1); t ^= t + Math.imul(t ^ t >>> 7, t | 61); return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const FX_FISH = c => `<svg viewBox="0 0 30 16"><path d="M2 8 Q10 0 20 5 L28 1 L26 8 L28 15 L20 11 Q10 16 2 8Z" fill="${c}" stroke="#A8502E" stroke-width="1.2"/><circle cx="8" cy="7" r="1.3" fill="#3A2A22"/></svg>`;
function tripFX(k){
  const f = TRIP_FX[k]; if(!f) return ""; const R = tripRng(k); let h = "";
  (f.cloud || []).forEach((y, i) => h += `<i class="fx-cloud" style="top:${y}%;--d:${46 + i * 13}s;animation-delay:-${(R() * 40).toFixed(1)}s"></i>`);
  if(f.bird != null) for(let i = 0; i < 2; i++) h += `<i class="fx-bird" style="top:${f.bird + i * 4}%;--d:${16 + i * 3}s;animation-delay:-${(i * 2.2 + R() * 3).toFixed(1)}s"><svg viewBox="0 0 40 16"><path d="M2 9 Q10 1 20 9 Q30 1 38 9" fill="none" stroke="#5A4A44" stroke-width="2.6" stroke-linecap="round"/></svg></i>`;
  (f.rip || []).forEach(([x, y, w]) => { for(let j = 0; j < 2; j++) h += `<i class="fx-rip" style="left:${x - w / 2}%;top:${y + j * 2}%;width:${w * (j ? .7 : 1)}%;animation-delay:-${(R() * 3.4).toFixed(2)}s"></i>`; });
  (f.fish || []).forEach(([a, b, y], i) => h += `<i class="fx-fishw" style="left:${a}%;width:${b - a}%;top:${y}%"><b class="fx-fish" style="--d:${9 + i * 3}s;animation-delay:-${(R() * 9).toFixed(1)}s">${FX_FISH(["#F28A3C", "#F25C4C", "#F6B444"][i % 3])}</b></i>`);
  if(f.fall){ const n = f.fall === "dust" ? 14 : f.fall === "snow" ? 16 : 9;
    for(let i = 0; i < n; i++) h += `<i class="fx-p fx-${f.fall}" style="left:${(R() * 100).toFixed(1)}%;--d:${(f.fall === "dust" ? 9 : 6) + R() * 6}s;--s:${(.6 + R() * .7).toFixed(2)};--h:${Math.round(R() * 60 - 30)}deg;animation-delay:-${(R() * 12).toFixed(1)}s"></i>`; }
  (f.steam || []).forEach(([x, y]) => h += `<i class="fx-steam" style="left:${x}%;top:${y}%"><b style="animation-delay:-${(R() * 3).toFixed(1)}s"></b><b style="animation-delay:-${(R() * 3).toFixed(1)}s"></b><b style="animation-delay:-${(R() * 3).toFixed(1)}s"></b></i>`);
  (f.tw || []).forEach(([x1, y1, x2, y2, n, c]) => { for(let i = 0; i < n; i++) h += `<i class="fx-tw" style="left:${(x1 + R() * (x2 - x1)).toFixed(1)}%;top:${(y1 + R() * (y2 - y1)).toFixed(1)}%;--c:${c};--s:${(.5 + R() * .8).toFixed(2)};animation-delay:-${(R() * 2.6).toFixed(1)}s"></i>`; });
  (f.fount || []).forEach(([x, y]) => { h += `<i class="fx-fount" style="left:${x}%;top:${y}%">`; for(let i = 0; i < 6; i++) h += `<b style="--x:${(i - 2.5) * 5}px;animation-delay:-${(i * .23).toFixed(2)}s"></b>`; h += `</i>`; });
  return `<div class="fx" aria-hidden="true">${h}</div>`;
}

/* ---------- Cảnh di chuyển giữa các điểm tham quan ---------- */
const TRIP_MV = { suodao: "cable", emeishan: "cable", liziba: "train", mingzhu: "train", guangzhouta: "train", gangzhuao: "bus",
  xihu: "boat", lijiangriver: "boat", xiangbishan: "boat", waitan: "boat", hongyadong: "boat", leshandafo: "boat", danxia: "boat", leifeng: "boat", yuyuan: "walk",
  chengqiang: "bike", yangshuo: "bike", duanqiao: "walk", lijiang: "walk", kuanzhai: "walk", shamian: "bike" };
const TRIP_MVTXT = { walk: ["走路去", "Đi bộ cùng Tiểu Ngữ đến"], bike: ["骑自行车去", "Đạp xe đến"], bus: ["坐大巴去", "Đi xe buýt du lịch đến"], train: ["坐地铁去", "Đi tàu điện đến"], boat: ["坐船去", "Đi thuyền đến"], cable: ["坐缆车去", "Đi cáp treo đến"] };
function tripMode(s){ return TRIP_MV[s.art] || (s.kind === "jd" ? "bus" : "walk"); }
const TV_SVG = {
  wheel: (x, y, r = 11) => `<g class="tv-wh" style="transform-origin:${x}px ${y}px"><circle cx="${x}" cy="${y}" r="${r}" fill="#3B3B46"/><circle cx="${x}" cy="${y}" r="${r * .45}" fill="#D9DCE6"/><path d="M${x - r * .45} ${y}H${x + r * .45}M${x} ${y - r * .45}V${y + r * .45}" stroke="#8A8FA0" stroke-width="2"/></g>`,
  hills: `<svg viewBox="0 0 400 60" preserveAspectRatio="none"><path d="M0 60 L0 34 Q40 6 80 30 Q120 2 170 28 Q210 8 250 30 Q300 4 340 26 Q372 12 400 34 L400 60Z" fill="#BFE0B0"/></svg>`,
  karst: `<svg viewBox="0 0 400 60" preserveAspectRatio="none"><path d="M0 60 V40 Q14 0 30 40 Q44 10 60 40 Q80 2 100 40 Q116 12 130 40 Q150 0 170 40 Q186 14 200 40 Q220 2 240 40 Q256 12 270 40 Q290 0 310 40 Q326 14 340 40 Q360 4 380 40 Q392 20 400 40 V60Z" fill="#A9D3A2"/></svg>`,
  city: `<svg viewBox="0 0 400 60" preserveAspectRatio="none"><g fill="#C9D4EA"><rect x="8" y="22" width="22" height="38"/><rect x="36" y="10" width="16" height="50"/><rect x="58" y="28" width="26" height="32"/><rect x="92" y="4" width="14" height="56"/><rect x="112" y="24" width="24" height="36"/><rect x="146" y="14" width="18" height="46"/><rect x="172" y="30" width="30" height="30"/><rect x="210" y="8" width="16" height="52"/><rect x="232" y="20" width="24" height="40"/><rect x="264" y="2" width="12" height="58"/><rect x="284" y="26" width="28" height="34"/><rect x="320" y="12" width="18" height="48"/><rect x="346" y="30" width="22" height="30"/><rect x="374" y="16" width="20" height="44"/></g></svg>`,
  trees: `<svg viewBox="0 0 400 50" preserveAspectRatio="none">${[20, 90, 150, 230, 300, 360].map(x => `<rect x="${x - 2}" y="28" width="4" height="22" fill="#8A6A4A"/><circle cx="${x}" cy="24" r="13" fill="#7CC264"/><circle cx="${x + 6}" cy="20" r="8" fill="#93D27A"/>`).join("")}</svg>`
};
const Travel = {
  face(){ return `<span class="tv-face" style="background-image:url(${TRIP_GD.g_full})"></span>`; },
  me(){ return `<span class="tv-me">${Trip.head()}</span>`; },
  walker(){ return `<div class="tv-walker"><div class="tv-gd">${guideSVG("smile", "walk")}</div><div class="tv-kid"><div class="tv-kh">${Trip.head()}</div><svg viewBox="0 0 40 46" class="tv-kb"><path d="M8 4 Q20 -2 32 4 L34 26 H6Z" fill="#F2B83A" stroke="#5A4034" stroke-width="2" stroke-linejoin="round"/><rect x="26" y="6" width="10" height="16" rx="4" fill="#E8453C" stroke="#5A4034" stroke-width="2"/><g class="tv-leg"><rect x="11" y="25" width="7" height="18" rx="3.5" fill="#3E5C52"/></g><g class="tv-leg b"><rect x="22" y="25" width="7" height="18" rx="3.5" fill="#3E5C52"/></g></svg></div></div>`; },
  actor(m){
    const W = TV_SVG.wheel;
    if(m === "walk") return this.walker();
    if(m === "bike") return `<div class="tv-veh tv-bike"><div class="tv-bk-h">${Trip.head()}</div><svg viewBox="0 0 120 70"><path d="M30 50 L52 26 L80 50 M52 26 L62 50 L30 50 M74 20 L80 50 M70 20 H82" stroke="#E8453C" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 22 L60 22" stroke="#5A4034" stroke-width="5" stroke-linecap="round"/><path d="M50 8 Q54 20 58 30" stroke="#3E5C52" stroke-width="8" stroke-linecap="round"/>${W(30, 50, 16)}${W(84, 50, 16)}</svg><div class="tv-gd small">${guideSVG("smile", "walk")}</div></div>`;
    if(m === "bus") return `<div class="tv-veh tv-bus"><svg viewBox="0 0 200 100"><rect x="10" y="14" width="180" height="66" rx="18" fill="#F6C343" stroke="#5A4034" stroke-width="3"/><rect x="10" y="58" width="180" height="10" fill="#E8453C"/><rect x="164" y="24" width="20" height="28" rx="6" fill="#BFE6FA" stroke="#5A4034" stroke-width="2.4"/><text x="100" y="78" font-size="10" fill="#fff" font-weight="700" text-anchor="middle">薇薇旅游 WEIWEI TOUR</text>${W(52, 84, 13)}${W(150, 84, 13)}</svg><div class="tv-win a">${this.face()}</div><div class="tv-win b">${this.me()}</div></div>`;
    if(m === "train") return `<div class="tv-veh tv-train"><svg viewBox="0 0 240 90"><path d="M10 20 Q10 10 22 10 H200 Q232 12 236 56 V72 H10Z" fill="#fff" stroke="#5A4034" stroke-width="3"/><rect x="10" y="54" width="226" height="8" fill="#21836A"/><path d="M206 18 Q226 24 228 50 H206Z" fill="#BFE6FA" stroke="#5A4034" stroke-width="2.4"/>${W(50, 76, 8)}${W(80, 76, 8)}${W(170, 76, 8)}${W(200, 76, 8)}</svg><div class="tv-win a">${this.face()}</div><div class="tv-win b">${this.me()}</div></div>`;
    if(m === "boat") return `<div class="tv-veh tv-boat"><div class="tv-gd">${guideSVG("smile")}</div><div class="tv-bme">${this.me()}</div><svg viewBox="0 0 220 70"><path d="M6 22 H214 Q200 64 160 66 H60 Q20 64 6 22Z" fill="#B97A4A" stroke="#5A4034" stroke-width="3"/><path d="M14 32 H206" stroke="#8E5A33" stroke-width="3"/><path d="M190 6 L196 40" stroke="#5A4034" stroke-width="3"/><path d="M196 8 L214 14 L198 20Z" fill="#E8453C"/></svg></div>`;
    return `<div class="tv-veh tv-cable"><svg viewBox="0 0 140 130"><path d="M70 0 V30" stroke="#5A4034" stroke-width="4"/><rect x="58" y="22" width="24" height="12" rx="4" fill="#8A8FA0"/><rect x="12" y="34" width="116" height="88" rx="20" fill="#E8453C" stroke="#5A4034" stroke-width="3"/><rect x="12" y="96" width="116" height="10" fill="#fff" opacity=".85"/></svg><div class="tv-win a">${this.face()}</div><div class="tv-win b">${this.me()}</div></div>`;
  },
  go(s, cb){
    if(matchMedia("(prefers-reduced-motion: reduce)").matches) return cb();
    const m = tripMode(s), c = TRIP.find(c => c.spots.includes(s)), far = m === "train" || m === "bus" && c && /sh|gz|cq/.test(c.id) ? TV_SVG.city : c && /gl/.test(c.id) ? TV_SVG.karst : TV_SVG.hills;
    const [zh, vi] = TRIP_MVTXT[m];
    const ov = document.createElement("div"); ov.className = `tv-ov tvm-${m}`; ov.setAttribute("role", "status");
    ov.innerHTML = `<div class="tv-card"><div class="tv-scene">${m === "cable" ? `<div class="tv-wire"></div>` : ""}<div class="tv-far">${far}${far}</div>${m === "boat" || m === "cable" ? `<div class="tv-water"></div>` : `<div class="tv-near">${TV_SVG.trees}${TV_SVG.trees}</div><div class="tv-road"></div>`}<div class="tv-act">${this.actor(m)}</div></div>
      <p class="tv-txt"><span class="han">${zh}${s.zh}</span><span>${vi} ${esc(s.vi)}…</span></p></div>`;
    document.body.appendChild(ov);
    let fin = false; const end = () => { if(fin) return; fin = true; ov.classList.add("out"); setTimeout(() => ov.remove(), 300); cb(); };
    ov.onclick = end; setTimeout(end, 2600);
  }
};

/* ---------- Vé máy bay ---------- */
const Ticket = {
  info(id){ const st = Trip.st, t = st.tix && st.tix[id]; if(t) return t;
    const R = tripRng(id + (Trip.key() || "")), d = new Date();
    return { no: "WW" + (100 + Math.floor(R() * 899)), seat: (1 + Math.floor(R() * 30)) + "ABCDEF"[Math.floor(R() * 6)], gate: "ABCD"[Math.floor(R() * 4)] + (1 + Math.floor(R() * 20)),
      time: String(7 + Math.floor(R() * 12)).padStart(2, "0") + ":" + ["00", "15", "30", "45"][Math.floor(R() * 4)], date: d.toLocaleDateString("vi-VN"), from: st.at || "han" }; },
  card(id, t, stamped){
    const c = Trip.C(id), f = t.from === "han" ? { zh: "河内", vi: "Hà Nội", code: "HAN" } : { ...Trip.C(t.from), code: TRIP_CODE[t.from] }, p = Profile.get();
    let bars = ""; const R = tripRng(t.no + id); for(let x = 0; x < 120; x += 2 + Math.floor(R() * 3)) bars += `<rect x="${x}" y="0" width="${1 + Math.floor(R() * 2)}" height="30"/>`;
    return `<div class="tk ${stamped ? "paid" : ""}" style="--sc:${c.col}">
      <div class="tk-l"><div class="tk-hd"><b>✈ 薇薇航空 <small>WEIWEI AIR</small></b><span>登机牌 · BOARDING PASS</span></div>
        <div class="tk-route"><div><b>${f.code}</b><span class="han">${f.zh}</span><small>${esc(f.vi)}</small></div><i>✈</i><div><b>${TRIP_CODE[id]}</b><span class="han">${c.zh}</span><small>${esc(c.vi)}</small></div></div>
        <div class="tk-grid"><div><small>乘客 · Hành khách</small><b>${esc(p.name || "")}</b></div><div><small>航班 · Chuyến bay</small><b>${t.no}</b></div><div><small>日期 · Ngày bay</small><b>${t.date}</b></div>
          <div><small>登机口 · Cửa</small><b>${t.gate}</b></div><div><small>座位 · Ghế</small><b>${t.seat}</b></div><div><small>登机 · Giờ lên</small><b>${t.time}</b></div></div></div>
      <div class="tk-r"><div class="tk-pic">${tripArt(c.cover)}</div><b>${TRIP_CODE[id]}</b><small>${t.seat} · ${t.no}</small><svg class="tk-bar" viewBox="0 0 120 30" preserveAspectRatio="none">${bars}</svg></div>
      <div class="tk-stamp"><span class="han">已出票</span><small>ĐÃ XUẤT VÉ</small></div></div>`;
  },
  open(id, onFly){
    const c = Trip.C(id), t = this.info(id), ov = document.createElement("div"); ov.className = "tk-ov";
    const paint = paid => { ov.innerHTML = `<div class="tk-box" role="dialog" aria-label="Mua vé máy bay đi ${esc(c.vi)}"><button class="tk-x" aria-label="Đóng">${ICON.x}</button>
      ${Trip.guide(paid ? "happy" : "smile", paid ? `<b class="han">${Trip.z("票买好了！我们出发吧！")}</b><p>Vé đã in xong! Mình cùng lên máy bay đi <b>${esc(c.vi)}</b> nhé.</p>` : `<b class="han">${Trip.z("我们坐飞机去" + c.zh + "吧！")}</b><p>Mình cùng bay đến <b>${esc(c.vi)}</b> nhé! Bấm <b>Mua vé</b> để in vé máy bay.</p>`)}
      <div class="tk-print">${this.card(id, t, paid)}</div>
      <div class="tp-row">${paid ? `<button class="btn primary big" id="tkFly">✈ Lên máy bay</button>` : `<span class="tk-price">Giá vé: <b>0 xu</b> · Tiểu Ngữ mời bạn!</span><button class="btn primary big" id="tkBuy">🎫 Mua vé</button>`}</div></div>`;
      ov.querySelector(".tk-x").onclick = () => { stopSpeak(); ov.remove(); };
      const say = ov.querySelector(".tp-say"); ov.querySelectorAll(".tp-say").forEach(b => b.onclick = () => Trip.talkSay(b.dataset.say, ov));
      if(paid){ ov.querySelector("#tkFly").onclick = () => { ov.classList.add("out"); setTimeout(() => { ov.remove(); onFly(); }, 250); }; }
      else ov.querySelector("#tkBuy").onclick = () => {
        Trip.st.tix = Trip.st.tix || {}; Trip.st.tix[id] = t; if(!Trip.st.visa) Trip.st.visa = Date.now(); Trip.save();
        paint(true); ov.querySelector(".tk-print").classList.add("printing"); Trip.talkSay("票买好了！我们出发吧！", ov); };
      Trip.talk(ov, 1600);
    };
    paint(!!(Trip.st.tix && Trip.st.tix[id]));
    document.body.appendChild(ov);
  }
};

/* ---------- Hộ chiếu & visa ---------- */
const Passport = {
  pg: 0,
  pages(){ const st = Trip.st, P = ["cover", "info", "visa"]; for(let i = 0; i < Math.ceil(TRIP.length / 4); i++) P.push("st" + i);
    const nt = Object.keys(st.tix || {}).length; for(let i = 0; i < Math.max(1, Math.ceil(nt / 3)); i++) P.push("tk" + i); return P; },
  no(){ const p = Profile.get() || {}; return "VW" + String(Math.abs([...((p.sid || p.name || "x"))].reduce((a, ch) => a * 31 + ch.charCodeAt(0) | 0, 7)) % 10000000).padStart(7, "0"); },
  stamp(c, t, fresh){
    const R = tripRng(c.id), rot = Math.round(R() * 30 - 15), d = new Date(t), ds = `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, "0")}.${String(d.getDate()).padStart(2, "0")}`;
    return `<div class="pp-stamp ${fresh ? "fresh" : ""}" style="--sc:${c.col};--r:${rot}deg"><svg viewBox="0 0 120 120"><defs><filter id="ink${c.id}"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="${Math.floor(R() * 99)}"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -.9 1.45"/><feComposite in="SourceGraphic" operator="in"/></filter></defs>
      <g filter="url(#ink${c.id})" fill="none" stroke="${c.col}"><circle cx="60" cy="60" r="54" stroke-width="4"/><circle cx="60" cy="60" r="46" stroke-width="1.6"/>
      <text x="60" y="58" font-size="28" fill="${c.col}" stroke="none" text-anchor="middle" font-family="KaiTi,STKaiti,serif" font-weight="700">${c.zh}</text>
      <text x="60" y="76" font-size="9.5" fill="${c.col}" stroke="none" text-anchor="middle" letter-spacing="1">${c.py.toUpperCase()}</text>
      <text x="60" y="92" font-size="9" fill="${c.col}" stroke="none" text-anchor="middle">${ds}</text>
      <text x="60" y="30" font-size="11" fill="${c.col}" stroke="none" text-anchor="middle">✈ 入境 ENTRY</text></g></svg></div>`;
  },
  page(k){
    const st = Trip.st, p = Profile.get() || {}, head = Trip.head();
    if(k === "cover") return `<div class="pp-cover"><div class="pp-emb"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="none" stroke="#F2D27A" stroke-width="3"/><path d="M10 50 H90 M50 10 Q28 50 50 90 Q72 50 50 10" fill="none" stroke="#F2D27A" stroke-width="2.4"/><text x="50" y="60" font-size="28" text-anchor="middle" fill="#F2D27A" font-family="KaiTi,STKaiti,serif">薇</text></svg></div>
      <b class="han">旅行护照</b><span>TRAVEL PASSPORT</span><small>薇薇中文 · Khám phá Trung Quốc</small><em>Hộ chiếu giả lập – dùng trong trò chơi</em></div>`;
    if(k === "info") return `<div class="pp-in"><h4>个人资料 · Thông tin cá nhân</h4><div class="pp-id"><div class="pp-photo">${head}</div><dl>
      <dt>Họ tên · 姓名</dt><dd>${esc(p.name || "")}</dd><dt>Số hộ chiếu · 护照号</dt><dd>${this.no()}</dd><dt>Quốc tịch · 国籍</dt><dd>Việt Nam · 越南</dd>
      <dt>Ngày cấp · 签发日期</dt><dd>${new Date(st.visa || Date.now()).toLocaleDateString("vi-VN")}</dd></dl></div>
      <p class="pp-mrz">P&lt;VNM${esc((p.name || "").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/gi, "D").toUpperCase().replace(/[^A-Z]+/g, "<"))}&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;<br>${this.no()}&lt;VNM&lt;&lt;WEIWEI&lt;ZHONGWEN&lt;&lt;&lt;</p></div>`;
    if(k === "visa") return `<div class="pp-in"><h4>签证 · Thị thực (Visa)</h4>${st.visa ? `<div class="pp-visa"><div class="pp-vh"><b class="han">中国 旅游签证</b><span>CHINA · TOURIST VISA (L)</span></div>
      <div class="pp-id"><div class="pp-photo">${head}</div><dl><dt>Họ tên</dt><dd>${esc(p.name || "")}</dd><dt>Loại · 种类</dt><dd>L · Du lịch 旅游</dd><dt>Số lần nhập cảnh</dt><dd>Nhiều lần · 多次</dd><dt>Cấp ngày</dt><dd>${new Date(st.visa).toLocaleDateString("vi-VN")}</dd></dl></div>
      <p class="pp-mrz">V&lt;CHN${this.no()}&lt;&lt;WEIWEI&lt;TRAVEL&lt;&lt;&lt;</p></div>` : `<div class="pp-empty">Visa sẽ được dán khi bạn mua vé máy bay đầu tiên ✈</div>`}</div>`;
    if(k.startsWith("st")){ const i = +k.slice(2), cs = TRIP.slice(i * 4, i * 4 + 4);
      return `<div class="pp-in"><h4>入境章 · Dấu nhập cảnh <small>${i + 1}/${Math.ceil(TRIP.length / 4)}</small></h4><div class="pp-slots">${cs.map(c => `<div class="pp-slot" data-c="${c.id}">${st.stamps[c.id] ? this.stamp(c, st.stamps[c.id], this.fresh === c.id) : `<span class="han">${c.zh}</span><small>${c.vi}<br>${Trip.cnt(c)}/${c.spots.length}</small>`}</div>`).join("")}</div></div>`; }
    const ids = Object.keys(st.tix || {}), i = +k.slice(2), part = ids.slice(i * 3, i * 3 + 3);
    return `<div class="pp-in"><h4>机票 · Vé máy bay đã mua</h4>${part.length ? `<div class="pp-tix">${part.map(id => `<div class="pp-tk">${Ticket.card(id, st.tix[id], true)}</div>`).join("")}</div>` : `<div class="pp-empty">Chưa có vé nào. Chọn một trạm trên bản đồ để mua vé nhé!</div>`}</div>`;
  },
  open(at, fresh){
    stopSpeak(); const P = this.pages(); this.fresh = fresh || null;
    this.pg = typeof at === "number" ? at : at ? Math.max(0, P.indexOf(at)) : 0;
    let ov = document.querySelector(".pp-ov"); if(!ov){ ov = document.createElement("div"); ov.className = "pp-ov"; document.body.appendChild(ov); }
    const paint = () => { const P = this.pages(), k = P[this.pg];
      ov.innerHTML = `<div class="pp-box" role="dialog" aria-label="Hộ chiếu du lịch"><button class="tk-x" aria-label="Đóng">${ICON.x}</button>
        <div class="pp-book ${k === "cover" ? "is-cover" : ""}"><div class="pp-page" key="${k}">${this.page(k)}</div>${this.fresh && k.startsWith("st") ? `<div class="pp-tool" aria-hidden="true"><svg viewBox="0 0 60 90"><rect x="22" y="0" width="16" height="44" rx="8" fill="#8E5A33" stroke="#5A4034" stroke-width="2.4"/><rect x="6" y="44" width="48" height="16" rx="5" fill="#C9A27A" stroke="#5A4034" stroke-width="2.4"/><rect x="4" y="60" width="52" height="10" rx="3" fill="var(--sc,#D9483B)"/></svg></div>` : ""}</div>
        <div class="pp-nav"><button class="btn" id="ppPrev" ${this.pg ? "" : "disabled"} aria-label="Trang trước">${ICON.left}</button><span>${P.map((_, j) => `<i class="${j === this.pg ? "on" : ""}"></i>`).join("")}</span><button class="btn" id="ppNext" ${this.pg < P.length - 1 ? "" : "disabled"} aria-label="Trang sau">${ICON.right}</button></div></div>`;
      ov.querySelector(".tk-x").onclick = () => { ov.remove(); this.fresh = null; };
      ov.onclick = e => { if(e.target === ov){ ov.remove(); this.fresh = null; } };
      ov.querySelector("#ppPrev").onclick = () => { this.pg--; this.fresh = null; paint(); };
      ov.querySelector("#ppNext").onclick = () => { this.pg++; this.fresh = null; paint(); };
      const tool = ov.querySelector(".pp-tool"), slot = this.fresh && ov.querySelector(`.pp-slot[data-c="${this.fresh}"]`);
      if(tool && slot){ const b = ov.querySelector(".pp-book").getBoundingClientRect(), r = slot.getBoundingClientRect(); tool.style.left = (r.left - b.left + r.width / 2) + "px"; tool.style.top = (r.top - b.top + r.height / 2) + "px"; tool.style.setProperty("--sc", Trip.C(this.fresh).col); }
    };
    paint();
  }
};
