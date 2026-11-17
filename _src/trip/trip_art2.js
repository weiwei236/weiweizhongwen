/* ===== Tranh bổ sung: chi tiết thêm cho tranh cũ + 6 trạm mới (Tây An, Quế Lâm, Tứ Xuyên, Thành Đô, Quảng Châu, Quảng Đông) ===== */
Object.assign(TA, {
  grad(id, a, b, vertical = true){ return `<defs><linearGradient id="${id}" x1="0" y1="0" x2="${vertical ? 0 : 1}" y2="${vertical ? 1 : 0}"><stop offset="0" stop-color="${a}"/><stop offset="1" stop-color="${b}"/></linearGradient></defs>`; },
  light(k){ return `<defs><radialGradient id="lt_${k}" cx=".25" cy=".1" r=".9"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></radialGradient></defs><rect width="200" height="150" fill="url(#lt_${k})" pointer-events="none"/>`; },
  shadow(cx, cy, rx, ry = 3){ return `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="#000" opacity=".12"/>`; },
  rnd(seed){ let r = seed; return () => (r = (r * 9301 + 49297) % 233280) / 233280; },
  grass(y1, y2, n, seed, col = "#5E9E4A"){ const R = TA.rnd(seed); let h = ""; for(let i = 0; i < n; i++){ const x = R() * 196 + 2, y = y1 + R() * (y2 - y1); h += `<path d="M${x.toFixed(1)} ${y.toFixed(1)} q-1 -4 -3 -5 M${x.toFixed(1)} ${y.toFixed(1)} q0 -5 1 -7 M${x.toFixed(1)} ${y.toFixed(1)} q1 -4 4 -4" stroke="${col}" stroke-width="1.2" fill="none" stroke-linecap="round"/>`; } return h; },
  flowers(y1, y2, n, seed){ const R = TA.rnd(seed), C = ["#FFFFFF", "#F7D35C", "#F59BB5", "#BFA5F2"]; let h = ""; for(let i = 0; i < n; i++){ const x = R() * 190 + 5, y = y1 + R() * (y2 - y1), c = C[i % 4]; h += `<g transform="translate(${x.toFixed(1)} ${y.toFixed(1)})"><circle cx="-1.6" r="1.5" fill="${c}"/><circle cx="1.6" r="1.5" fill="${c}"/><circle cy="-1.6" r="1.5" fill="${c}"/><circle cy="1.6" r="1.5" fill="${c}"/><circle r="1.1" fill="#F2B83A"/></g>`; } return h; },
  birds(list){ return list.map(([x, y, s = 1]) => `<path d="M${x - 5 * s} ${y} q${2.5 * s} ${-3 * s} ${5 * s} 0 q${2.5 * s} ${-3 * s} ${5 * s} 0" stroke="#5A6A80" stroke-width="1.3" fill="none" stroke-linecap="round"/>`).join(""); },
  /* du khách chibi nhỏ: x,y = chân; s tỉ lệ; c màu áo; o: {hat, cam, flag, back} */
  person(x, y, s = 1, c = "#E8803C", o = {}){
    const sk = "#FCE3D2", ol = "#5A4034", hair = o.hair || "#3A2A22";
    return `<g transform="translate(${x} ${y}) scale(${s})">${TA.shadow(0, 0, 6, 1.6)}
      <rect x="-4" y="-8" width="3.2" height="8" rx="1.5" fill="#4A5A78" stroke="${ol}" stroke-width=".8"/><rect x=".8" y="-8" width="3.2" height="8" rx="1.5" fill="#4A5A78" stroke="${ol}" stroke-width=".8"/>
      <path d="M-6 -7 Q-6 -18 0 -18 Q6 -18 6 -7Z" fill="${c}" stroke="${ol}" stroke-width=".9"/>
      ${o.back ? `<rect x="${o.back === "l" ? -9 : 4}" y="-17" width="5" height="8" rx="2" fill="#7FA9D6" stroke="${ol}" stroke-width=".8"/>` : ""}
      <circle cx="0" cy="-24" r="7" fill="${sk}" stroke="${ol}" stroke-width=".9"/>
      <path d="M-7 -25 Q-6 -32 0 -32 Q6 -32 7 -25 Q3 -28 -1 -27 Q-5 -27 -7 -25Z" fill="${hair}"/>
      ${o.hat ? `<path d="M-9 -28 Q0 -31 9 -28 Q6 -36 0 -36 Q-6 -36 -9 -28Z" fill="${o.hat}" stroke="${ol}" stroke-width=".8"/>` : ""}
      <circle cx="-2.4" cy="-23.5" r=".9" fill="${ol}"/><circle cx="2.4" cy="-23.5" r=".9" fill="${ol}"/><ellipse cx="-4.2" cy="-21.6" rx="1.3" ry=".7" fill="#F48B8B" opacity=".6"/><ellipse cx="4.2" cy="-21.6" rx="1.3" ry=".7" fill="#F48B8B" opacity=".6"/>
      ${o.cam ? `<rect x="-3.5" y="-16" width="7" height="5" rx="1" fill="#3A3A42"/><circle cx="0" cy="-13.5" r="1.4" fill="#9FD0F0"/>` : ""}
      ${o.flag ? `<path d="M6 -12 L8 -34" stroke="#8A5A36" stroke-width="1"/><path d="M8 -34 L15 -31 L7.6 -28Z" fill="#E8453C"/>` : ""}
    </g>`;
  },
  table(){ return `<g opacity=".32"><path d="M0 122 H200 M0 138 H200 M24 110 V150 M64 110 V150 M104 110 V150 M144 110 V150 M184 110 V150" stroke="#D98A60" stroke-width="6"/></g>`; },
  cup(x, y, s = 1, tea = "#C9A24E"){ return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-8 -8 Q-8 4 0 4 Q8 4 8 -8Z" fill="#fff" stroke="#5A4034" stroke-width="1.3"/><ellipse cx="0" cy="-8" rx="8" ry="2.4" fill="${tea}" stroke="#5A4034" stroke-width="1.1"/><path d="M-5 -3 Q0 0 5 -3" stroke="#5B8ED6" stroke-width="1" fill="none"/></g>`; },
  chop(x1, y1, x2, y2){ return `<path d="M${x1} ${y1} L${x2} ${y2}" stroke="#8A5A36" stroke-width="3.6" stroke-linecap="round"/><path d="M${x1 + 8} ${y1 - 4} L${x2 + 6} ${y2 - 5}" stroke="#A0703F" stroke-width="3.6" stroke-linecap="round"/>`; },
  karst(x, base, w, h, c1 = "#7DB88A", c2 = "#5C9C6E"){ return `<path d="M${x - w} ${base} Q${x - w * .9} ${base - h * .55} ${x - w * .45} ${base - h * .85} Q${x - w * .2} ${base - h * 1.05} ${x} ${base - h} Q${x + w * .25} ${base - h * .98} ${x + w * .45} ${base - h * .8} Q${x + w * .9} ${base - h * .5} ${x + w} ${base}Z" fill="${c1}" stroke="${c2}" stroke-width="1.6"/><path d="M${x - w * .3} ${base - h * .7} Q${x - w * .1} ${base - h * .4} ${x - w * .25} ${base - h * .1}" stroke="${c2}" stroke-width="1.2" fill="none" opacity=".7"/>`; },
  bamboo(x, y, h, s = 1){ let l = ""; for(let i = 0; i < 4; i++) l += `<path d="M${x} ${y - i * h / 4} q${(i % 2 ? 8 : -8) * s} ${-4 * s} ${(i % 2 ? 14 : -14) * s} ${-2 * s}" stroke="#5FA34A" stroke-width="${2.4 * s}" fill="none" stroke-linecap="round"/>`; return `<path d="M${x} ${y} V${y - h}" stroke="#7CC264" stroke-width="${3 * s}"/><path d="M${x - 1.5 * s} ${y - h * .33} h${3 * s} M${x - 1.5 * s} ${y - h * .66} h${3 * s}" stroke="#4E8F3A" stroke-width="1.2"/>${l}`; },
  panda(x, y, s = 1, mood = "smile"){ return `<g transform="translate(${x} ${y}) scale(${s})">${TA.shadow(0, 14, 16, 3)}<ellipse cx="0" cy="4" rx="15" ry="12" fill="#fff" stroke="#3B3B3B" stroke-width="1.5"/><ellipse cx="-11" cy="10" rx="5" ry="6" fill="#2E2E33"/><ellipse cx="11" cy="10" rx="5" ry="6" fill="#2E2E33"/><path d="M-14 -2 Q0 4 14 -2 L14 4 Q0 9 -14 4Z" fill="#2E2E33"/><circle cx="0" cy="-12" r="12" fill="#fff" stroke="#3B3B3B" stroke-width="1.5"/><circle cx="-9" cy="-21" r="4.6" fill="#2E2E33"/><circle cx="9" cy="-21" r="4.6" fill="#2E2E33"/><ellipse cx="-4.5" cy="-12" rx="3.4" ry="4.2" fill="#2E2E33" transform="rotate(-20 -4.5 -12)"/><ellipse cx="4.5" cy="-12" rx="3.4" ry="4.2" fill="#2E2E33" transform="rotate(20 4.5 -12)"/>${mood === "happy" ? `<path d="M-6 -12 q1.5 -2 3 0 M3 -12 q1.5 -2 3 0" stroke="#fff" stroke-width="1.1" fill="none"/>` : `<circle cx="-4" cy="-12.5" r="1.3" fill="#fff"/><circle cx="5" cy="-12.5" r="1.3" fill="#fff"/>`}<ellipse cx="0" cy="-7" rx="2" ry="1.3" fill="#2E2E33"/><path d="M-2 -5 q2 2 4 0" stroke="#2E2E33" stroke-width="1" fill="none"/><ellipse cx="-8" cy="-6" rx="2" ry="1.1" fill="#F6A9A9" opacity=".7"/><ellipse cx="8" cy="-6" rx="2" ry="1.1" fill="#F6A9A9" opacity=".7"/></g>`; }
});

/* Lớp chi tiết vẽ thêm lên các tranh cũ */
const ART_X = {
  gugong: () => TA.birds([[60, 22], [72, 16, .8], [140, 30, .7]]) + `<g stroke="#D9C291" stroke-width="1" opacity=".8"><path d="M20 122 L10 150 M60 122 L56 150 M140 122 L144 150 M180 122 L190 150"/></g>` + TA.person(30, 140, .9, "#5B8ED6", { cam: 1 }) + TA.person(166, 142, .9, "#E8803C", { hat: "#F2B83A" }) + TA.person(180, 138, .75, "#7CC264", { flag: 1 }) + `<path d="M58 66 Q100 62 142 66" stroke="#FFE39A" stroke-width="1.6" fill="none"/>`,
  changcheng: () => `<path d="M0 86 Q30 70 60 80 Q100 60 140 74 Q170 66 200 74" fill="none" stroke="#fff" stroke-width="10" opacity=".25"/>` + TA.birds([[100, 26], [112, 20, .8], [92, 30, .7]]) + TA.person(96, 92, .55, "#E8453C", { back: "r" }) + TA.person(108, 86, .5, "#5B8ED6", { hat: "#F2B83A" }) + TA.grass(126, 148, 16, 5, "#4E8F3A") + TA.flowers(128, 146, 8, 9),
  tiantan: () => TA.birds([[50, 40], [60, 34, .8]]) + TA.person(26, 146, .8, "#E8453C", { hat: "#fff" }) + TA.person(40, 144, .75, "#5B8ED6") + TA.person(176, 146, .8, "#7CC264", { cam: 1 }) + TA.grass(130, 148, 12, 3),
  tanghulu: () => `<path d="M0 130 Q100 120 200 132 V150 H0Z" fill="#fff" opacity=".85"/><rect x="150" y="96" width="44" height="22" rx="6" fill="#E8453C" stroke="#9E2128" stroke-width="1.6"/><text x="172" y="111" text-anchor="middle" font-size="10" fill="#FFE27A" font-family="KaiTi,STKaiti,serif">糖葫芦</text>`,
  mingzhu: () => `<g opacity=".55"><rect x="96" y="124" width="8" height="22" fill="#EC5F8E"/><rect x="98" y="126" width="4" height="2" fill="#fff"/></g><path d="M140 134 L176 134 L170 142 L146 142Z" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><rect x="150" y="126" width="18" height="8" rx="2" fill="#FFE27A" stroke="#5A4034" stroke-width="1.2"/><g fill="#FFE27A"><circle cx="153" cy="130" r="1"/><circle cx="159" cy="130" r="1"/><circle cx="165" cy="130" r="1"/></g>`,
  waitan: () => TA.person(60, 104, .7, "#E8453C", { cam: 1 }) + TA.person(72, 104, .7, "#5B8ED6") + TA.person(126, 104, .65, "#7CC264", { hat: "#F2B83A" }) + TA.birds([[120, 18], [130, 14, .8]]) + `<g fill="#FFE27A" opacity=".35"><circle cx="40" cy="82" r="8"/><circle cx="150" cy="82" r="8"/></g>`,
  yuyuan: () => `<g><path d="M110 120 q6 -4 12 0 q-6 4 -12 0z" fill="#F28B3C" stroke="#B85A1E" stroke-width="1"/><path d="M110 120 l-4 -3 v6z" fill="#F28B3C"/><path d="M150 112 q6 -4 12 0 q-6 4 -12 0z" fill="#fff" stroke="#E8453C" stroke-width="1"/><path d="M150 112 l-4 -3 v6z" fill="#E8453C"/></g>` + TA.person(58, 112, .55, "#E8453C") + TA.person(90, 92, .5, "#5B8ED6", { hat: "#F2B83A" }),
  xiaolongbao: () => `<ellipse cx="34" cy="132" rx="20" ry="7" fill="#fff" stroke="#5A4034" stroke-width="1.5"/><ellipse cx="34" cy="131" rx="15" ry="4.5" fill="#5B2E22"/><g stroke="#E8B34A" stroke-width="1.6"><path d="M28 130 l6 -1 M32 132 l6 -1"/></g>` + TA.cup(178, 136, 1.2),
  shengjian: () => TA.table() + `<ellipse cx="30" cy="134" rx="18" ry="6" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><g fill="#6DBA4F"><circle cx="24" cy="132" r="1.6"/><circle cx="30" cy="134" r="1.6"/><circle cx="36" cy="131" r="1.6"/></g>`,
  hongyadong: () => `<path d="M150 140 L180 140 L174 146 L156 146Z" fill="#E8453C" stroke="#1F1512" stroke-width="1.2"/><rect x="158" y="134" width="14" height="6" rx="1.5" fill="#FFD66B"/>` + TA.birds([[30, 30, .7]]),
  suodao: () => `<path d="M30 132 L56 132 L50 138 L36 138Z" fill="#fff" stroke="#5A4034" stroke-width="1.3"/><path d="M130 142 L160 142 L154 148 L136 148Z" fill="#E8803C" stroke="#5A4034" stroke-width="1.3"/>` + TA.birds([[90, 30], [100, 24, .8], [80, 36, .6]]),
  liziba: () => TA.person(84, 146, .75, "#E8453C", { cam: 1 }) + TA.person(100, 146, .75, "#5B8ED6", { cam: 1 }) + TA.person(116, 146, .7, "#7CC264", { hat: "#F2B83A" }) + TA.person(130, 146, .7, "#BFA5F2") + TA.flowers(136, 148, 6, 4),
  huoguo: () => `<ellipse cx="26" cy="136" rx="22" ry="8" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><g fill="#F4B9A6" stroke="#C97A62" stroke-width=".8"><ellipse cx="18" cy="134" rx="7" ry="3"/><ellipse cx="28" cy="132" rx="7" ry="3"/><ellipse cx="34" cy="136" rx="7" ry="3"/></g><ellipse cx="176" cy="138" rx="20" ry="7" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><g fill="#7DC264" stroke="#3F7F2F" stroke-width=".8"><ellipse cx="170" cy="136" rx="6" ry="3"/><ellipse cx="180" cy="134" rx="6" ry="3"/></g>`,
  xiaomian: () => TA.cup(178, 136, 1.2, "#D6B26A") + `<ellipse cx="26" cy="138" rx="16" ry="5" fill="#fff" stroke="#5A4034" stroke-width="1.3"/><g fill="#E3B979"><ellipse cx="22" cy="136" rx="2.6" ry="1.6"/><ellipse cx="28" cy="137" rx="2.6" ry="1.6"/></g>`,
  shilin: () => TA.person(66, 144, .7, "#E8453C", { cam: 1 }) + TA.person(80, 144, .7, "#2F9E8F", { flag: 1 }) + TA.person(130, 146, .7, "#5B8ED6", { hat: "#fff" }) + TA.flowers(126, 148, 10, 2) + TA.birds([[60, 20], [70, 14, .8]]),
  lijiang: () => `<path d="M100 138 q4 -3 8 0 q-4 3 -8 0z" fill="#F28B3C"/><path d="M130 144 q4 -3 8 0 q-4 3 -8 0z" fill="#F7D35C"/>` + TA.person(96, 112, .6, "#E8453C", { hat: "#F2B83A" }) + TA.person(140, 112, .6, "#5B8ED6", { cam: 1 }) + TA.birds([[150, 14], [160, 10, .7]]),
  mixian: () => TA.table(),
  xianhuabing: () => `<rect x="150" y="40" width="40" height="30" rx="4" fill="#F7C7D6" stroke="#B53A5E" stroke-width="1.5"/><path d="M150 52 H190 M170 40 V70" stroke="#E8453C" stroke-width="2.5"/><text x="170" y="66" text-anchor="middle" font-size="7" fill="#B53A5E" font-family="KaiTi,STKaiti,serif">鲜花饼</text>`,
  xihu: () => TA.birds([[110, 30], [120, 24, .8], [100, 36, .6]]) + `<g transform="translate(80 120)"><circle cx="2" cy="-8" r="3" fill="#FCE3D2" stroke="#5A4034" stroke-width=".8"/><path d="M-2 -10 Q2 -16 6 -10Z" fill="#F2B83A"/></g>` + `<ellipse cx="190" cy="132" rx="9" ry="3.5" fill="#6DB36A" stroke="#3F7F45" stroke-width="1.2"/><circle cx="188" cy="128" r="3" fill="#F59BB5" stroke="#C25B7C" stroke-width="1"/>`,
  leifeng: () => TA.birds([[50, 52], [60, 46, .8], [40, 58, .6]]) + `<path d="M30 140 L52 140 L48 145 L34 145Z" fill="#6B4A3A"/><path d="M40 140 V132 L48 138Z" fill="#fff" stroke="#6B4A3A" stroke-width=".8"/>`,
  duanqiao: () => `<path d="M0 140 Q50 132 100 142 Q150 134 200 140 V150 H0Z" fill="#fff" opacity=".8"/>`,
  longjing: () => `<g transform="translate(36 132)">${TA.person(0, 0, .9, "#2F9E8F", { hat: "#E9C27E" })}<path d="M6 -14 Q14 -14 14 -6 Q14 2 6 2" fill="#C99A68" stroke="#5A4034" stroke-width="1"/></g>`,
  dongpo: () => TA.chop(150, 128, 196, 112) + `<path d="M14 120 Q14 140 34 140 Q54 140 54 120Z" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><ellipse cx="34" cy="120" rx="20" ry="5" fill="#FAF6EE" stroke="#5A4034" stroke-width="1.2"/>` + TA.face(34, 130, .6, "happy")
};

Object.assign(ART, {
  /* ---------------- TÂY AN ---------------- */
  bingmayong(){
    const soldier = (x, y, s, c = "#B98A62") => `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-7" y="-4" width="14" height="6" rx="1" fill="#9C7352"/><path d="M-8 -4 L-7 -22 Q0 -26 7 -22 L8 -4Z" fill="${c}" stroke="#6E4E36" stroke-width="1.2"/><path d="M-7 -14 H7 M-7 -10 H7" stroke="#8E6748" stroke-width="1"/><circle cx="0" cy="-30" r="6.5" fill="${c}" stroke="#6E4E36" stroke-width="1.2"/><path d="M-6 -33 Q0 -40 6 -33 Q3 -36 0 -35 Q-3 -36 -6 -33Z" fill="#8E6748"/><circle cx="3" cy="-38" r="2.4" fill="#8E6748"/><path d="M-2.5 -30 h1.6 M1 -30 h1.6" stroke="#5A3E2B" stroke-width="1"/><path d="M-1.5 -26.5 q1.5 1 3 0" stroke="#5A3E2B" stroke-width=".9" fill="none"/></g>`;
    let rows = "";
    [[78, .7], [100, .85], [126, 1.05]].forEach(([y, s], r) => { for(let x = 18 + r * 6; x < 196; x += 26 - r * 2) rows += soldier(x + (r % 2 ? 8 : 0), y, s); });
    return TA.grad("bmW", "#E9C99E", "#C9A273") + `<rect width="200" height="150" fill="url(#bmW)"/>
      <path d="M0 0 H200 V30 H0Z" fill="#8E6A4A"/><path d="M0 30 H200" stroke="#6E4E36" stroke-width="2"/><g stroke="#7A5A40" stroke-width="2"><path d="M0 8 H200 M0 18 H200"/></g>
      <path d="M0 58 H200 M0 82 H200 M0 108 H200" stroke="#B48A62" stroke-width="5"/>${rows}
      <rect x="0" y="134" width="200" height="16" fill="#D9B98E"/><path d="M0 134 H200" stroke="#9C7352" stroke-width="2"/>`
      + TA.person(40, 150, .8, "#E8453C", { cam: 1 }) + TA.person(160, 150, .8, "#5B8ED6", { flag: 1 });
  },
  dayanta(){
    let t = ""; const T = [[118, 34], [102, 30], [88, 27], [75, 24], [63, 21], [52, 18], [42, 15]];
    T.forEach(([y, w], i) => { const h = i ? 13 - i * .6 : 18; t += `<rect x="${100 - w}" y="${y - h}" width="${w * 2}" height="${h}" fill="#D7B486" stroke="#6E4E36" stroke-width="1.4"/><path d="M${100 - 3} ${y - h + 3} v${h - 5} h6 v${-(h - 5)}Z" fill="#6E4E36"/><path d="M${100 - w - 3} ${y - h} h${w * 2 + 6} l-3 -2.6 h${-(w * 2)}Z" fill="#A98058" stroke="#6E4E36" stroke-width="1.2"/>`; });
    return TA.sky("dyS", "#BDE2FF", "#FFF2DE") + TA.cloud(40, 26, .8) + TA.cloud(166, 34, .7) + TA.birds([[140, 20], [150, 14, .8]])
      + `<rect y="118" width="200" height="32" fill="#E7D2AE"/><path d="M0 128 H200" stroke="#D4BB92" stroke-width="1.5"/>` + t
      + `<path d="M100 26 V16" stroke="#6E4E36" stroke-width="2.4"/><circle cx="100" cy="15" r="3" fill="#F2B83A" stroke="#6E4E36" stroke-width="1"/>
      <g><circle cx="30" cy="110" r="14" fill="#7EC06C" stroke="#4E8F3A" stroke-width="1.5"/><circle cx="170" cy="110" r="14" fill="#7EC06C" stroke="#4E8F3A" stroke-width="1.5"/></g>`
      + TA.person(60, 142, .85, "#E8453C", { cam: 1 }) + TA.person(140, 144, .85, "#2F9E8F", { hat: "#F2B83A" });
  },
  chengqiang(){
    let cren = ""; for(let x = 0; x < 200; x += 10) cren += `<rect x="${x}" y="80" width="6" height="7" fill="#B9A07E" stroke="#6E4E36" stroke-width="1"/>`;
    return TA.sky("cqS", "#FFD1A3", "#FFF0DA") + TA.sun(36, 30, 10) + TA.birds([[150, 20], [160, 14, .8]])
      + `<rect y="86" width="200" height="40" fill="#B9A07E" stroke="#6E4E36" stroke-width="1.8"/>${cren}
      <g stroke="#9E8566" stroke-width="1" opacity=".8"><path d="M0 96 H200 M0 106 H200 M0 116 H200"/><path d="M10 86 V96 M30 96 V106 M50 86 V96 M70 106 V116 M110 96 V106 M150 86 V96 M170 106 V116 M190 96 V106"/></g>
      <path d="M86 126 V106 Q100 92 114 106 V126Z" fill="#5A3E2B" stroke="#6E4E36" stroke-width="1.6"/>
      <rect x="62" y="58" width="76" height="22" fill="#D9483B" stroke="#6E4E36" stroke-width="1.6"/><g fill="#B8352B"><rect x="68" y="58" width="4" height="22"/><rect x="88" y="58" width="4" height="22"/><rect x="108" y="58" width="4" height="22"/><rect x="128" y="58" width="4" height="22"/></g>`
      + TA.roof(60, 140, 62, 12, "#4A4E58", "#2E2A28", 10) + `<rect x="72" y="38" width="56" height="12" fill="#D9483B" stroke="#6E4E36" stroke-width="1.4"/>` + TA.roof(68, 132, 41, 10, "#4A4E58", "#2E2A28", 9)
      + TA.lantern(70, 64, .8) + TA.lantern(130, 64, .8)
      + `<rect y="126" width="200" height="24" fill="#E7D2AE"/>`
      + `<g transform="translate(150 130)"><circle cx="-8" cy="8" r="6" fill="none" stroke="#5A4034" stroke-width="1.6"/><circle cx="8" cy="8" r="6" fill="none" stroke="#5A4034" stroke-width="1.6"/><path d="M-8 8 L0 0 L8 8 M0 0 L-3 -4" stroke="#E8453C" stroke-width="1.8" fill="none"/></g>` + TA.person(152, 130, .6, "#5B8ED6", { hat: "#F2B83A" }) + TA.person(40, 146, .8, "#E8803C", { cam: 1 });
  },
  roujiamo(){
    return TA.sky("rjS", "#FFF1DE", "#FFE0C0") + TA.table()
      + `<ellipse cx="100" cy="122" rx="78" ry="18" fill="#fff" stroke="#5A4034" stroke-width="1.8"/>
      <path d="M44 104 Q46 70 100 66 Q154 70 156 104Z" fill="#F2D29B" stroke="#5A4034" stroke-width="2"/><path d="M60 92 Q100 72 140 92" stroke="#E2B66E" stroke-width="2" fill="none"/><circle cx="100" cy="86" r="6" fill="none" stroke="#E2B66E" stroke-width="1.6"/>
      <path d="M46 104 Q100 92 154 104 Q150 112 100 112 Q50 112 46 104Z" fill="#8E4A2A" stroke="#5A4034" stroke-width="1.6"/><g fill="#6DBA4F"><circle cx="70" cy="104" r="2"/><circle cx="96" cy="100" r="2"/><circle cx="124" cy="104" r="2"/></g><g fill="#B5643A"><circle cx="82" cy="106" r="2.4"/><circle cx="112" cy="106" r="2.4"/></g>
      <path d="M48 106 Q50 124 100 126 Q150 124 152 106 Q100 116 48 106Z" fill="#E9C27E" stroke="#5A4034" stroke-width="2"/>` + TA.face(100, 118, .9, "happy")
      + TA.steam(86, 60) + TA.steam(116, 58, .8) + TA.cup(178, 128, 1.1);
  },
  paomo(){
    let bread = ""; const R = TA.rnd(8); for(let i = 0; i < 14; i++){ const x = 60 + R() * 80, y = 70 + R() * 14; bread += `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="7" height="5" rx="1.6" fill="#F6E2B8" stroke="#C9A066" stroke-width=".8" transform="rotate(${(R() * 60 - 30).toFixed(0)} ${x.toFixed(1)} ${y.toFixed(1)})"/>`; }
    return TA.sky("pmS", "#FFF3E2", "#FFE6CC") + TA.table()
      + `<path d="M24 76 Q28 136 100 140 Q172 136 176 76Z" fill="#2F64B5" stroke="#5A4034" stroke-width="2"/><path d="M40 100 Q100 116 160 100" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 4"/>
      <ellipse cx="100" cy="76" rx="76" ry="18" fill="#F3E3C6" stroke="#5A4034" stroke-width="2"/>${bread}
      <g fill="#F4B9A6" stroke="#C97A62" stroke-width=".8"><ellipse cx="80" cy="74" rx="9" ry="3.5"/><ellipse cx="118" cy="78" rx="9" ry="3.5"/><ellipse cx="100" cy="70" rx="8" ry="3"/></g>
      <g fill="#6DBA4F"><circle cx="70" cy="80" r="1.6"/><circle cx="130" cy="72" r="1.6"/><circle cx="108" cy="84" r="1.6"/></g>
      <path d="M134 70 q6 -6 12 -2 q-4 6 -12 2z" fill="#8FD068" stroke="#3F7F2F" stroke-width="1"/>` + TA.face(100, 122, 1, "happy", "#fff")
      + TA.steam(84, 54) + TA.steam(116, 52, .8)
      + `<g transform="translate(176 128)"><ellipse rx="16" ry="5" fill="#fff" stroke="#5A4034" stroke-width="1.3"/><path d="M-8 -2 q4 -6 8 0 q4 -6 8 0" fill="#F7E7C3" stroke="#C9A066" stroke-width="1"/></g>`;
  },
  /* ---------------- QUẾ LÂM ---------------- */
  lijiangriver(){
    return TA.sky("lgS", "#BFE6F2", "#F2FAFC") + TA.birds([[90, 20], [100, 14, .8]])
      + TA.karst(30, 96, 30, 60, "#A9CFB8", "#86B29A") + TA.karst(80, 96, 26, 74, "#B6D8C2", "#8FB9A2") + TA.karst(130, 96, 28, 58, "#A9CFB8", "#86B29A") + TA.karst(176, 96, 30, 70, "#B6D8C2", "#8FB9A2")
      + TA.karst(56, 100, 22, 44, "#7DB88A", "#5C9C6E") + TA.karst(150, 100, 24, 40, "#7DB88A", "#5C9C6E")
      + `<rect y="98" width="200" height="52" fill="#8FCFC8"/><g opacity=".35"><path d="M40 104 Q56 118 72 104Z M126 104 Q150 120 174 104Z" fill="#5C9C6E"/></g>
      <path d="M0 98 H200" stroke="#6FB0A8" stroke-width="1.6"/><path d="M20 112 q8 -3 16 0 M140 136 q8 -3 16 0 M70 142 q8 -3 16 0" stroke="#D2EEEA" stroke-width="2" fill="none"/>
      <g transform="translate(96 124)"><path d="M-36 0 H36 L32 6 H-32Z" fill="#C9A266" stroke="#6E4E36" stroke-width="1.4"/><path d="M-30 0 V6 M-20 0 V6 M-10 0 V6 M0 0 V6 M10 0 V6 M20 0 V6 M30 0 V6" stroke="#A07E48" stroke-width="1"/>
      <path d="M-20 0 L-20 -16" stroke="#6E4E36" stroke-width="1.4"/><circle cx="-26" cy="-6" r="3.6" fill="#3A3A42"/><path d="M-26 -9 q2 -5 5 -3" stroke="#3A3A42" stroke-width="2" fill="none"/></g>`
      + TA.person(-2 + 96 + 10, 124, .7, "#5B8ED6", { hat: "#E9C27E" }) + `<path d="M120 124 L132 92" stroke="#8A5A36" stroke-width="1.6"/>`;
  },
  xiangbishan(){
    return TA.sky("xbS", "#C7E6FF", "#F3FAFF") + TA.cloud(160, 22, .8) + TA.sun(36, 28, 9)
      + TA.karst(176, 100, 26, 50, "#A9CFB8", "#86B29A")
      + `<path d="M20 102 Q22 50 70 44 Q120 40 132 70 Q140 92 136 120 L118 120 Q120 92 104 80 Q88 72 78 92 Q74 104 76 120 L62 120 Q60 106 52 104 Q30 104 20 102Z" fill="#8CBE8A" stroke="#5C8F5C" stroke-width="2"/>
      <path d="M40 64 Q60 52 84 54" stroke="#6FA56C" stroke-width="2" fill="none"/><circle cx="56" cy="66" r="2.6" fill="#3B3B3B"/><path d="M48 74 q6 3 12 0" stroke="#5C8F5C" stroke-width="1.4" fill="none"/>
      <g fill="#6DAA6A"><circle cx="70" cy="44" r="5"/><circle cx="84" cy="42" r="5"/><circle cx="96" cy="46" r="5"/></g><path d="M86 30 V44 M82 34 h8 M83 38 h6" stroke="#6E6A60" stroke-width="2"/>
      <rect y="112" width="200" height="38" fill="#8FCFDB"/><path d="M76 120 Q96 96 118 120" fill="#6DB6C6"/><g opacity=".3"><path d="M20 112 Q70 140 136 112Z" fill="#5C8F5C"/></g>
      <path d="M150 132 L176 132 L172 138 L154 138Z" fill="#C9A266" stroke="#6E4E36" stroke-width="1.2"/>` + TA.person(162, 132, .55, "#E8453C", { hat: "#E9C27E" }) + TA.birds([[110, 30], [120, 24, .7]]);
  },
  yangshuo(){
    let fields = ""; for(let i = 0; i < 5; i++) fields += `<path d="M0 ${104 + i * 10} Q100 ${98 + i * 10} 200 ${106 + i * 10}" fill="none" stroke="${i % 2 ? "#B9DE7E" : "#A6D46C"}" stroke-width="10"/>`;
    return TA.sky("ysS", "#CFEAFF", "#F6FBFF") + TA.cloud(100, 20, .8) + TA.birds([[40, 30], [50, 24, .8]])
      + TA.karst(24, 100, 26, 64, "#A9CFB8", "#86B29A") + TA.karst(70, 100, 22, 52, "#B6D8C2", "#8FB9A2") + TA.karst(120, 100, 30, 70, "#A9CFB8", "#86B29A") + TA.karst(174, 100, 28, 56, "#B6D8C2", "#8FB9A2")
      + fields + `<path d="M0 136 Q100 126 200 138" stroke="#E7D2AE" stroke-width="8" fill="none"/>
      <g transform="translate(70 132)"><circle cx="-8" cy="4" r="5.5" fill="none" stroke="#5A4034" stroke-width="1.6"/><circle cx="8" cy="4" r="5.5" fill="none" stroke="#5A4034" stroke-width="1.6"/><path d="M-8 4 L0 -3 L8 4 M0 -3 L-2 -7" stroke="#E8453C" stroke-width="1.8" fill="none"/></g>` + TA.person(70, 130, .55, "#5B8ED6", { hat: "#F2B83A" })
      + `<g transform="translate(120 136)"><circle cx="-8" cy="4" r="5.5" fill="none" stroke="#5A4034" stroke-width="1.6"/><circle cx="8" cy="4" r="5.5" fill="none" stroke="#5A4034" stroke-width="1.6"/><path d="M-8 4 L0 -3 L8 4 M0 -3 L-2 -7" stroke="#2F9E8F" stroke-width="1.8" fill="none"/></g>` + TA.person(120, 134, .55, "#E8453C");
  },
  guilinmifen(){
    let nd = ""; for(let i = 0; i < 7; i++) nd += `<path d="M${46 + i * 4} ${72 + i * 1.6} q14 -6 28 0 t28 0 t28 0" fill="none" stroke="#FFF8EA" stroke-width="3"/>`;
    return TA.sky("gmS", "#FFF3E2", "#FFE6CC") + TA.table()
      + `<path d="M24 76 Q28 136 100 140 Q172 136 176 76Z" fill="#fff" stroke="#5A4034" stroke-width="2"/><path d="M34 100 Q100 114 166 100" fill="none" stroke="#3FA27A" stroke-width="4"/><path d="M40 112 Q100 124 160 112" fill="none" stroke="#3FA27A" stroke-width="1.6" stroke-dasharray="3 3"/>
      <ellipse cx="100" cy="76" rx="76" ry="18" fill="#B9733E" stroke="#5A4034" stroke-width="2"/>${nd}
      <g fill="#8E4A2A" stroke="#5A2E1A" stroke-width=".8"><ellipse cx="72" cy="74" rx="9" ry="3"/><ellipse cx="128" cy="78" rx="9" ry="3"/></g>
      <g fill="#E3B979" stroke="#9A6E3A" stroke-width=".7"><ellipse cx="90" cy="82" rx="2.6" ry="1.8"/><ellipse cx="110" cy="70" rx="2.6" ry="1.8"/><ellipse cx="100" cy="84" rx="2.6" ry="1.8"/></g>
      <g fill="#6DBA4F"><circle cx="84" cy="70" r="1.8"/><circle cx="118" cy="84" r="1.8"/><circle cx="140" cy="72" r="1.8"/></g><g fill="#E2453B"><circle cx="64" cy="82" r="1.8"/><circle cx="104" cy="76" r="1.8"/></g>`
      + TA.face(100, 124, 1.1, "happy") + TA.steam(80, 54) + TA.steam(114, 52, .8) + TA.chop(130, 22, 82, 70);
  },
  pijiuyu(){
    return TA.sky("pyS", "#FFF0DE", "#FFDFC4") + TA.table()
      + `<path d="M184 96 L200 86" stroke="#3A3A42" stroke-width="8"/><ellipse cx="96" cy="100" rx="86" ry="36" fill="#3C3C46" stroke="#222" stroke-width="2"/><ellipse cx="96" cy="98" rx="76" ry="29" fill="#C9662E"/>
      <path d="M40 98 Q70 72 120 82 Q150 86 158 98 Q150 110 120 114 Q70 124 40 98Z" fill="#E9A15A" stroke="#7A3A1A" stroke-width="2"/><path d="M158 98 L178 84 L176 112Z" fill="#E9A15A" stroke="#7A3A1A" stroke-width="2"/>
      <g stroke="#B5643A" stroke-width="1.6" fill="none"><path d="M70 88 q4 10 0 20 M86 84 q4 12 0 26 M102 84 q4 12 0 26 M118 86 q4 10 0 22"/></g>
      <circle cx="54" cy="94" r="4.4" fill="#fff" stroke="#5A4034" stroke-width="1.2"/><circle cx="55" cy="94" r="2" fill="#3A2A22"/>
      <g fill="#E2453B"><circle cx="76" cy="112" r="3.6"/><circle cx="110" cy="76" r="3.6"/><circle cx="132" cy="110" r="3.6"/></g><g fill="#6DBA4F"><rect x="88" y="100" width="6" height="2.4" rx="1"/><rect x="124" y="94" width="6" height="2.4" rx="1"/></g>`
      + TA.steam(80, 58) + TA.steam(116, 56, .8)
      + `<g transform="translate(176 40)"><path d="M-9 -16 H9 L7 18 Q0 22 -7 18Z" fill="#F7C35C" stroke="#5A4034" stroke-width="1.4"/><path d="M-9 -16 Q-6 -24 0 -20 Q6 -26 9 -16Z" fill="#fff" stroke="#5A4034" stroke-width="1.2"/>${TA.face(0, 4, .7, "happy")}</g>`;
  },
  /* ---------------- TỨ XUYÊN ---------------- */
  jiuzhaigou(){
    let trees = ""; [[16, 74, "#F2B33D"], [34, 70, "#E25B45"], [150, 66, "#7EC06C"], [168, 72, "#F08A3C"], [186, 68, "#E25B45"], [56, 76, "#7EC06C"]].forEach(([x, y, c]) => trees += `<path d="M${x} ${y - 14} L${x + 8} ${y + 4} H${x - 8}Z" fill="${c}" stroke="#5A4034" stroke-width="1.2"/><path d="M${x} ${y + 4} V${y + 9}" stroke="#5A4034" stroke-width="1.6"/>`);
    return TA.sky("jzS", "#BCE2FF", "#F2FAFF") + TA.cloud(110, 20, .8)
      + `<path d="M0 70 Q40 30 80 54 Q110 24 150 48 Q180 30 200 50 V90 H0Z" fill="#8FB49A" stroke="#6E9A7E" stroke-width="1.6"/><path d="M0 80 Q60 60 120 76 Q170 66 200 74 V96 H0Z" fill="#6FA57E"/>` + trees
      + TA.grad("jzW", "#3FD0D6", "#1F8FB8") + `<path d="M0 92 Q100 82 200 94 V150 H0Z" fill="url(#jzW)"/>
      <path d="M86 94 L82 112 M96 94 L94 116 M106 94 L106 114 M116 94 L118 112" stroke="#fff" stroke-width="4" opacity=".9"/><path d="M80 112 Q100 120 122 112" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>
      <g opacity=".55"><path d="M20 124 h30 M130 132 h40 M60 140 h30" stroke="#BFF3F5" stroke-width="2"/></g>
      <g opacity=".5"><path d="M16 96 L24 92 L32 96Z M150 98 L160 92 L170 98Z" fill="#E25B45"/></g>`
      + TA.birds([[40, 30], [50, 24, .7]]);
  },
  leshandafo(){
    return TA.sky("lsS", "#CFE8F5", "#F5FAF5") + TA.cloud(160, 18, .7)
      + `<path d="M0 30 Q30 18 60 26 L64 150 L0 150Z M140 26 Q170 18 200 30 L200 150 L136 150Z" fill="#B48A62" stroke="#7A5A40" stroke-width="1.6"/><g fill="#6FA56C"><circle cx="20" cy="26" r="9"/><circle cx="40" cy="22" r="8"/><circle cx="160" cy="22" r="8"/><circle cx="182" cy="26" r="9"/></g>
      <rect x="60" y="20" width="80" height="130" fill="#C9A27A" stroke="#7A5A40" stroke-width="1.6"/>
      <g stroke="#7A5A40" stroke-width="1.6"><path d="M64 132 Q66 80 100 76 Q134 80 136 132Z" fill="#D9B48A"/><path d="M76 90 Q100 110 124 90" fill="none"/><path d="M70 112 Q100 128 130 112" fill="none"/>
      <ellipse cx="100" cy="52" rx="22" ry="26" fill="#DDBB92"/><path d="M78 44 Q80 22 100 22 Q120 22 122 44 Q112 34 100 34 Q88 34 78 44Z" fill="#6E5A48"/><g fill="#6E5A48"><circle cx="86" cy="28" r="2.4"/><circle cx="94" cy="26" r="2.4"/><circle cx="102" cy="25" r="2.4"/><circle cx="110" cy="26" r="2.4"/></g>
      <ellipse cx="76" cy="56" rx="4" ry="10" fill="#DDBB92"/><ellipse cx="124" cy="56" rx="4" ry="10" fill="#DDBB92"/></g>
      <path d="M88 54 q4 -3 8 0 M104 54 q4 -3 8 0" stroke="#5A4034" stroke-width="1.6" fill="none"/><path d="M94 66 q6 4 12 0" stroke="#5A4034" stroke-width="1.6" fill="none"/>
      <g fill="#D9B48A" stroke="#7A5A40" stroke-width="1.4"><rect x="80" y="132" width="16" height="10" rx="4"/><rect x="104" y="132" width="16" height="10" rx="4"/></g>
      <rect y="140" width="200" height="10" fill="#C99A5A"/><path d="M0 143 q8 -3 16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0" stroke="#E8C792" stroke-width="1.4" fill="none"/>`
      + TA.person(88, 132, .4, "#E8453C") + TA.person(112, 132, .4, "#5B8ED6");
  },
  emeishan(){
    return TA.sky("emS", "#FFD7A8", "#FFF3DE") + `<circle cx="160" cy="36" r="14" fill="#FFE27A" opacity=".85"/>` + TA.face(160, 37, 1.2, "happy")
      + `<path d="M30 88 L70 34 L90 50 L110 24 L150 88Z" fill="#8E9DB6" stroke="#5E6E8E" stroke-width="1.6"/>
      <g transform="translate(110 24)"><rect x="-14" y="-12" width="28" height="12" fill="#F2C14E" stroke="#8A5A1E" stroke-width="1.2"/>${TA.roof(-16, 16, -10, 8, "#E6A42A", "#8A5A1E", 6)}</g>
      <g fill="#fff"><ellipse cx="40" cy="92" rx="40" ry="12"/><ellipse cx="100" cy="96" rx="50" ry="14"/><ellipse cx="166" cy="92" rx="40" ry="12"/><ellipse cx="70" cy="104" rx="60" ry="12"/><ellipse cx="150" cy="106" rx="56" ry="12"/></g>
      <path d="M0 150 L0 112 Q60 104 120 116 Q160 122 200 112 V150Z" fill="#7DA06E" stroke="#5E8550" stroke-width="1.6"/>
      <g transform="translate(60 128)">${TA.shadow(0, 14, 12)}<ellipse cx="0" cy="4" rx="11" ry="10" fill="#A97E5A" stroke="#5A4034" stroke-width="1.4"/><circle cx="0" cy="-8" r="9" fill="#A97E5A" stroke="#5A4034" stroke-width="1.4"/><ellipse cx="0" cy="-6" rx="6" ry="5" fill="#F2C9A8"/><circle cx="-8" cy="-10" r="3" fill="#F2C9A8" stroke="#5A4034" stroke-width="1"/><circle cx="8" cy="-10" r="3" fill="#F2C9A8" stroke="#5A4034" stroke-width="1"/>${TA.face(0, -7, .55, "happy")}<path d="M10 6 Q22 4 20 -8" stroke="#A97E5A" stroke-width="3" fill="none"/><circle cx="20" cy="-10" r="3" fill="#F2B83A" stroke="#5A4034" stroke-width="1"/></g>`
      + TA.person(140, 140, .8, "#E8453C", { cam: 1 }) + TA.birds([[50, 30], [60, 24, .8]]);
  },
  mapodoufu(){
    let tofu = ""; [[72, 84], [92, 80], [112, 84], [132, 82], [82, 96], [104, 96], [124, 96], [96, 72], [116, 72]].forEach(([x, y]) => tofu += `<rect x="${x - 6}" y="${y - 5}" width="12" height="10" rx="2.4" fill="#FFF6E0" stroke="#C9A066" stroke-width="1"/><rect x="${x - 4}" y="${y - 3.6}" width="5" height="2" rx="1" fill="#fff" opacity=".9"/>`);
    return TA.sky("mpS", "#FFEEDD", "#FFDCC4") + TA.table()
      + `<ellipse cx="100" cy="100" rx="84" ry="32" fill="#fff" stroke="#5A4034" stroke-width="2"/><ellipse cx="100" cy="96" rx="70" ry="24" fill="#D8452A" stroke="#A8302A" stroke-width="1.4"/>${tofu}
      <g fill="#8E3A22"><circle cx="66" cy="92" r="2"/><circle cx="140" cy="90" r="2"/><circle cx="100" cy="106" r="2"/><circle cx="120" cy="78" r="2"/></g><g fill="#6DBA4F"><circle cx="78" cy="78" r="1.8"/><circle cx="108" cy="88" r="1.8"/><circle cx="130" cy="102" r="1.8"/><circle cx="90" cy="104" r="1.8"/></g>
      <g fill="#FF9A6A" opacity=".55"><ellipse cx="60" cy="100" rx="6" ry="2"/><ellipse cx="146" cy="96" rx="5" ry="2"/></g>`
      + TA.face(104, 89, .7, "happy") + TA.steam(84, 56) + TA.steam(118, 54, .8)
      + `<path d="M22 132 Q22 148 40 148 Q58 148 58 132Z" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><ellipse cx="40" cy="132" rx="18" ry="5" fill="#FAF6EE" stroke="#5A4034" stroke-width="1.2"/>` + TA.cup(178, 138, 1.1);
  },
  huiguorou(){
    let slices = ""; [[66, 88, -10], [86, 80, 6], [108, 86, -4], [128, 80, 10], [80, 100, 4], [104, 102, -8], [126, 98, 4]].forEach(([x, y, r]) => slices += `<g transform="rotate(${r} ${x} ${y})"><rect x="${x - 12}" y="${y - 5}" width="24" height="10" rx="4" fill="#F4C9A6" stroke="#9A4A2A" stroke-width="1.2"/><rect x="${x - 12}" y="${y - 5}" width="24" height="4" rx="2" fill="#C4612C"/></g>`);
    return TA.sky("hgrS", "#FFEFDF", "#FFDCC4") + TA.table()
      + `<ellipse cx="100" cy="100" rx="84" ry="30" fill="#fff" stroke="#5A4034" stroke-width="2"/><ellipse cx="100" cy="96" rx="70" ry="22" fill="#F3E9DA" stroke="#E2D7C6" stroke-width="1.2"/>${slices}
      <g stroke="#3F7F2F" stroke-width="1"><path d="M60 100 q10 -8 18 0 q-8 6 -18 0z" fill="#7DC264"/><path d="M134 90 q10 -8 18 0 q-8 6 -18 0z" fill="#7DC264"/><path d="M96 110 q10 -8 18 0 q-8 6 -18 0z" fill="#8FD068"/></g>
      <g fill="#D8452A"><rect x="70" y="76" width="7" height="2.6" rx="1"/><rect x="116" y="104" width="7" height="2.6" rx="1"/></g>`
      + TA.face(100, 92, .7, "happy") + TA.steam(84, 58) + TA.steam(116, 56, .8) + TA.chop(150, 30, 196, 52);
  },
  /* ---------------- THÀNH ĐÔ ---------------- */
  pandajidi(){
    return TA.sky("pdS", "#CFEFD8", "#F2FBF0") + TA.bamboo(20, 140, 120) + TA.bamboo(34, 140, 96, .8) + TA.bamboo(176, 140, 120) + TA.bamboo(190, 140, 100, .8)
      + `<path d="M40 112 H160 L150 122 H50Z" fill="#B98552" stroke="#6E4E36" stroke-width="1.6"/><path d="M60 122 V146 M140 122 V146" stroke="#8A5A36" stroke-width="5"/><path d="M0 140 H200 V150 H0Z" fill="#8FC87A"/>`
      + TA.panda(76, 96, 1, "happy") + `<g transform="translate(76 96)"><path d="M10 0 L22 -26" stroke="#7CC264" stroke-width="3"/><path d="M20 -22 q6 -2 8 2 M16 -14 q6 -2 8 2" stroke="#5FA34A" stroke-width="2" fill="none"/></g>`
      + TA.panda(128, 104, .75) + `<g transform="translate(150 60)">${TA.panda(0, 0, .55, "happy")}</g><path d="M128 62 Q150 58 172 64" stroke="#8A5A36" stroke-width="4" fill="none"/>`
      + TA.grass(140, 150, 10, 6, "#4E8F3A");
  },
  kuanzhai(){
    return TA.sky("kzS", "#D7ECFF", "#F6FBFF") + TA.birds([[100, 18], [110, 12, .7]])
      + `<path d="M0 46 L56 60 V140 H0Z" fill="#9A9AA6" stroke="#5A5A66" stroke-width="1.6"/><path d="M200 46 L144 60 V140 H200Z" fill="#9A9AA6" stroke="#5A5A66" stroke-width="1.6"/>
      <g stroke="#7E7E8A" stroke-width="1" opacity=".8"><path d="M0 70 L56 76 M0 90 L56 94 M0 110 L56 112 M200 70 L144 76 M200 90 L144 94 M200 110 L144 112"/></g>
      <path d="M-4 44 L60 58 L56 50 L0 36Z M204 44 L140 58 L144 50 L200 36Z" fill="#4A4E58" stroke="#2E2A28" stroke-width="1.4"/>
      <path d="M14 140 V96 Q28 84 42 96 V140Z" fill="#8E3A2A" stroke="#5A2E1A" stroke-width="1.6"/><circle cx="24" cy="118" r="1.8" fill="#F2B83A"/><circle cx="32" cy="118" r="1.8" fill="#F2B83A"/>
      <path d="M158 140 V96 Q172 84 186 96 V140Z" fill="#8E3A2A" stroke="#5A2E1A" stroke-width="1.6"/>
      <path d="M56 140 L80 92 H120 L144 140Z" fill="#CBB79A"/><g stroke="#B5A182" stroke-width="1"><path d="M70 120 H130 M64 132 H136 M76 106 H124"/></g>
      <rect x="80" y="66" width="40" height="26" fill="#E9D7B8" stroke="#6E4E36" stroke-width="1.4"/>` + TA.roof(78, 122, 68, 9, "#4A4E58", "#2E2A28", 8)
      + `<rect x="92" y="74" width="16" height="10" rx="1.5" fill="#F6E1A8" stroke="#6E4E36" stroke-width="1"/><text x="100" y="82" text-anchor="middle" font-size="6.5" fill="#8E3A2A" font-family="KaiTi,STKaiti,serif">茶馆</text>`
      + TA.lantern(52, 66, .8) + TA.lantern(148, 66, .8) + TA.lantern(70, 72, .6) + TA.lantern(130, 72, .6)
      + TA.person(90, 140, .7, "#E8453C", { cam: 1 }) + TA.person(112, 134, .6, "#5B8ED6", { hat: "#F2B83A" }) + TA.person(128, 140, .7, "#7CC264")
      + `<path d="M178 60 q6 -14 0 -26" stroke="#7CC264" stroke-width="2" fill="none"/><path d="M182 50 q8 -2 10 -8 M176 44 q-8 -2 -10 -8" stroke="#7CC264" stroke-width="2" fill="none"/>`;
  },
  bianlian(){
    const mask = (x, y, s, c1, c2, mood) => `<g transform="translate(${x} ${y}) scale(${s})"><ellipse rx="16" ry="19" fill="${c1}" stroke="#3A2A22" stroke-width="1.4"/><path d="M-16 -4 Q-8 -12 0 -6 Q8 -12 16 -4 Q10 6 0 2 Q-10 6 -16 -4Z" fill="${c2}"/><path d="M-12 -9 q4 -4 8 0 M4 -9 q4 -4 8 0" stroke="#3A2A22" stroke-width="2" fill="none"/>${TA.face(0, -3, .9, mood, "#3A2A22")}<path d="M-6 10 Q0 14 6 10" stroke="#3A2A22" stroke-width="1.6" fill="none"/></g>`;
    return TA.grad("blB", "#7A1E2A", "#3A0E16") + `<rect width="200" height="150" fill="url(#blB)"/><path d="M0 0 Q30 30 20 150 H0Z M200 0 Q170 30 180 150 H200Z" fill="#C2272E" stroke="#8E1A20" stroke-width="2"/><path d="M0 0 H200 V14 Q100 26 0 14Z" fill="#E2453B" stroke="#8E1A20" stroke-width="1.6"/><g fill="#F2B83A"><circle cx="40" cy="14" r="3"/><circle cx="80" cy="18" r="3"/><circle cx="120" cy="18" r="3"/><circle cx="160" cy="14" r="3"/></g>
      <g opacity=".35"><path d="M100 26 L50 150 H150Z" fill="#FFE9A8"/></g>
      <path d="M70 150 Q70 104 100 98 Q130 104 130 150Z" fill="#E8453C" stroke="#3A2A22" stroke-width="1.6"/><path d="M84 104 L100 150 L116 104" fill="#F2B83A" stroke="#3A2A22" stroke-width="1.4"/>
      <path d="M70 112 Q50 96 52 76" stroke="#E8453C" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M50 82 L42 60 L60 70Z" fill="#2F64B5" stroke="#3A2A22" stroke-width="1.2"/>
      <path d="M76 58 Q100 36 124 58" fill="#2E2E33"/><path d="M80 50 L100 34 L120 50" fill="#F2B83A" stroke="#3A2A22" stroke-width="1.2"/><circle cx="100" cy="34" r="4" fill="#E2453B"/>`
      + mask(100, 74, 1, "#E8453C", "#2E2E33", "smile") + mask(40, 120, .55, "#2F64B5", "#fff", "happy") + mask(162, 116, .55, "#3FA27A", "#F2B83A", "smile") + mask(160, 60, .45, "#F2B83A", "#E8453C", "happy");
  },
  dandanmian(){
    let nd = ""; for(let i = 0; i < 6; i++) nd += `<path d="M${50 + i * 4} ${72 + i * 2} q12 -8 24 0 t24 0 t24 0" fill="none" stroke="#F4D27A" stroke-width="3"/>`;
    return TA.sky("ddS", "#FFF1E4", "#FFE2CF") + TA.table()
      + `<path d="M34 80 Q38 132 100 136 Q162 132 166 80Z" fill="#fff" stroke="#5A4034" stroke-width="2"/><path d="M40 98 Q100 110 160 98" fill="none" stroke="#E8453C" stroke-width="3"/><path d="M44 108 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4 l6 -4 l6 4" fill="none" stroke="#E8453C" stroke-width="1.4"/>
      <ellipse cx="100" cy="80" rx="66" ry="16" fill="#C9502E" stroke="#5A4034" stroke-width="2"/>${nd}
      <path d="M86 70 Q100 62 114 70 Q110 78 100 78 Q90 78 86 70Z" fill="#8E4A2A" stroke="#5A2E1A" stroke-width="1"/><g fill="#E3B979"><circle cx="96" cy="68" r="1.6"/><circle cx="104" cy="72" r="1.6"/></g>
      <g fill="#6DBA4F"><circle cx="76" cy="76" r="1.8"/><circle cx="122" cy="82" r="1.8"/><circle cx="112" cy="70" r="1.8"/></g><path d="M126 74 q10 -8 20 0 q-10 6 -20 0z" fill="#7DC264" stroke="#3F7F2F" stroke-width="1"/>`
      + TA.face(100, 120, 1, "happy") + TA.steam(82, 56) + TA.steam(114, 54, .8) + TA.chop(126, 20, 86, 72);
  },
  bingfen(){
    return TA.sky("bfS", "#E6F6FF", "#FFF4F0")
      + `<ellipse cx="100" cy="126" rx="70" ry="12" fill="#fff" stroke="#5A4034" stroke-width="1.6"/>
      <path d="M40 76 Q44 128 100 130 Q156 128 160 76Z" fill="#E9F6FF" fill-opacity=".9" stroke="#7FA8C2" stroke-width="2"/><path d="M46 84 Q50 124 100 126 Q150 124 154 84Z" fill="#D9F1FF" opacity=".9"/>
      <ellipse cx="100" cy="76" rx="60" ry="14" fill="#F3FBFF" stroke="#7FA8C2" stroke-width="2"/><ellipse cx="100" cy="78" rx="52" ry="10" fill="#E7C27E" opacity=".55"/>
      <g fill="#FF8FAE" stroke="#C25B7C" stroke-width=".8"><circle cx="78" cy="74" r="4"/><circle cx="118" cy="78" r="4"/></g><g fill="#F7D35C" stroke="#C9A02E" stroke-width=".8"><rect x="92" y="70" width="6" height="6" rx="1.5"/><rect x="132" y="72" width="6" height="6" rx="1.5"/></g>
      <g fill="#fff" stroke="#C9C1B4" stroke-width=".6"><circle cx="70" cy="80" r="2.4"/><circle cx="106" cy="82" r="2.4"/><circle cx="140" cy="78" r="2.4"/></g><g fill="#8E4A2A"><circle cx="100" cy="76" r="1.6"/><circle cx="84" cy="80" r="1.6"/><circle cx="126" cy="74" r="1.6"/></g>
      <g fill="#BFE6FF" stroke="#7FA8C2" stroke-width="1" opacity=".9"><rect x="58" y="96" width="12" height="12" rx="3"/><rect x="86" y="104" width="12" height="12" rx="3"/><rect x="118" y="98" width="12" height="12" rx="3"/></g>`
      + TA.face(100, 114, 1, "happy", "#4E7FA6") + `<path d="M150 60 L176 30" stroke="#C9C1B4" stroke-width="3"/><ellipse cx="148" cy="64" rx="6" ry="4" fill="#E9E4DA" stroke="#9A9A9A" stroke-width="1" transform="rotate(-50 148 64)"/>`
      + `<g transform="translate(36 40)"><circle r="10" fill="#FF8FAE" stroke="#C25B7C" stroke-width="1.2"/><path d="M-2 -10 q2 -6 6 -6" stroke="#3F7F2F" stroke-width="1.6" fill="none"/>${TA.face(0, 1, .6, "happy")}</g>`;
  },
  /* ---------------- QUẢNG CHÂU ---------------- */
  guangzhouta(){
    let rings = ""; for(let i = 0; i < 14; i++){ const y = 24 + i * 7, w = 10 + Math.abs(i - 7) * 1.6; rings += `<path d="M${100 - w} ${y} Q100 ${y + 3} ${100 + w} ${y}" stroke="${["#FF6FA8", "#7FD3FF", "#B58CFF", "#FFD45C"][i % 4]}" stroke-width="2" fill="none"/>`; }
    return TA.sky("gzS", "#232F66", "#6E5AA8") + TA.stars(16, 21)
      + `<g fill="#3E4A86" stroke="#2A3366" stroke-width="1"><rect x="10" y="80" width="20" height="44"/><rect x="34" y="70" width="16" height="54"/><rect x="146" y="74" width="18" height="50"/><rect x="168" y="86" width="22" height="38"/></g>
      <g fill="#FFE27A" opacity=".8"><rect x="14" y="86" width="3" height="3"/><rect x="22" y="96" width="3" height="3"/><rect x="38" y="80" width="3" height="3"/><rect x="150" y="84" width="3" height="3"/><rect x="172" y="96" width="3" height="3"/><rect x="156" y="100" width="3" height="3"/></g>
      <path d="M86 124 Q94 74 88 22 L112 22 Q106 74 114 124Z" fill="#5B6BB0" stroke="#2A3366" stroke-width="1.6"/>${rings}
      <path d="M96 22 L98 6 H102 L104 22Z" fill="#9AA6D8" stroke="#2A3366" stroke-width="1.2"/><circle cx="100" cy="5" r="2.4" fill="#FF6FA8"/>
      <rect y="122" width="200" height="28" fill="#2A3E7A"/><g opacity=".7"><rect x="96" y="124" width="8" height="24" fill="#B58CFF"/><path d="M90 130 h20 M92 138 h16" stroke="#FF6FA8" stroke-width="2"/></g>
      <path d="M20 140 L58 140 L52 146 L26 146Z" fill="#fff" stroke="#2A3366" stroke-width="1.2"/><rect x="28" y="132" width="22" height="8" rx="2" fill="#FFD45C" stroke="#2A3366" stroke-width="1"/>
      <circle cx="170" cy="26" r="9" fill="#FFF3B0"/>${""}` + TA.face(170, 27, .75, "happy", "#9A7A2A");
  },
  shamian(){
    let tree = (x, y) => `<path d="M${x} ${y} V${y - 26}" stroke="#7A5638" stroke-width="5"/><path d="M${x - 4} ${y - 14} q-4 6 -2 14 M${x + 4} ${y - 18} q4 8 2 16" stroke="#7A5638" stroke-width="1.4" fill="none"/><circle cx="${x - 14}" cy="${y - 34}" r="14" fill="#6DAA5A" stroke="#4E8F3A" stroke-width="1.4"/><circle cx="${x + 12}" cy="${y - 36}" r="15" fill="#7EC06C" stroke="#4E8F3A" stroke-width="1.4"/><circle cx="${x}" cy="${y - 46}" r="14" fill="#7EC06C" stroke="#4E8F3A" stroke-width="1.4"/>`;
    return TA.sky("smS", "#CBE8FF", "#F6FBFF") + TA.cloud(100, 18, .7)
      + `<rect x="40" y="40" width="120" height="84" fill="#F3E2C6" stroke="#6E4E36" stroke-width="1.8"/><path d="M36 42 L100 22 L164 42Z" fill="#E8B48E" stroke="#6E4E36" stroke-width="1.8"/><circle cx="100" cy="34" r="5" fill="#fff" stroke="#6E4E36" stroke-width="1.2"/>
      <g fill="#fff" stroke="#6E4E36" stroke-width="1.2">${[50, 72, 94, 116, 138].map(x => `<rect x="${x}" y="52" width="12" height="16" rx="6"/><rect x="${x}" y="80" width="12" height="16" rx="6"/>`).join("")}</g>
      <g fill="#E9D3B0" stroke="#6E4E36" stroke-width="1"><rect x="44" y="100" width="6" height="24"/><rect x="150" y="100" width="6" height="24"/><rect x="86" y="100" width="6" height="24"/><rect x="108" y="100" width="6" height="24"/></g>
      <rect y="124" width="200" height="26" fill="#D9CCB4"/><path d="M0 124 H200" stroke="#B5A182" stroke-width="2"/>` + tree(24, 128) + tree(180, 130)
      + TA.person(70, 144, .8, "#E8453C", { cam: 1 }) + TA.person(98, 146, .75, "#fff", { hat: "#F59BB5" }) + TA.person(130, 144, .8, "#5B8ED6");
  },
  chenjiaci(){
    return TA.sky("cjS", "#C9E6FF", "#F4FAFF") + TA.cloud(40, 20, .7) + TA.birds([[150, 22], [160, 16, .7]])
      + `<rect y="116" width="200" height="34" fill="#D9CCB4"/><path d="M0 128 H200" stroke="#C2B49A" stroke-width="1.5"/>
      <rect x="20" y="64" width="160" height="52" fill="#9A9AA6" stroke="#5A5A66" stroke-width="1.8"/>
      <path d="M86 116 V86 H114 V116Z" fill="#4A3020" stroke="#2E2A28" stroke-width="1.6"/><path d="M100 86 V116" stroke="#2E2A28" stroke-width="1.2"/><g fill="#F2B83A"><circle cx="96" cy="100" r="1.6"/><circle cx="104" cy="100" r="1.6"/></g>
      <rect x="84" y="72" width="32" height="10" rx="1.5" fill="#1F2A3A" stroke="#F2B83A" stroke-width="1"/><text x="100" y="80" text-anchor="middle" font-size="7" fill="#F2B83A" font-family="KaiTi,STKaiti,serif">陈氏书院</text>
      <g fill="#C9B79A" stroke="#6E4E36" stroke-width="1"><rect x="30" y="76" width="40" height="20" rx="2"/><rect x="130" y="76" width="40" height="20" rx="2"/></g><g stroke="#8E6748" stroke-width="1.2" fill="none"><path d="M34 90 q6 -10 12 0 q6 -10 12 0 q6 -10 10 0 M134 90 q6 -10 12 0 q6 -10 12 0 q6 -10 10 0"/></g>`
      + TA.roof(14, 186, 66, 14, "#4A6A68", "#2E2A28", 10)
      + `<g fill="#3FA27A" stroke="#2E2A28" stroke-width="1"><path d="M30 52 q6 -10 14 -6 q-2 8 -14 6z"/><path d="M170 52 q-6 -10 -14 -6 q2 8 14 6z"/></g><g fill="#E8453C" stroke="#2E2A28" stroke-width="1"><circle cx="64" cy="50" r="3"/><circle cx="136" cy="50" r="3"/></g><g fill="#F2B83A" stroke="#2E2A28" stroke-width="1"><path d="M90 50 l4 -6 l4 6 l4 -6 l4 6 l4 -6"/></g>
      <path d="M44 52 Q100 44 156 52" stroke="#E9C27E" stroke-width="2" fill="none"/>`
      + TA.lantern(60, 70, .8) + TA.lantern(140, 70, .8) + TA.person(56, 142, .8, "#E8453C", { cam: 1 }) + TA.person(146, 142, .8, "#2F9E8F", { flag: 1 });
  },
  xiajiao(){
    const xj = (x, y, mood) => `<path d="M${x - 17} ${y + 4} Q${x - 18} ${y - 14} ${x} ${y - 16} Q${x + 18} ${y - 14} ${x + 17} ${y + 4} Q${x} ${y + 10} ${x - 17} ${y + 4}Z" fill="#FCEFF0" fill-opacity=".92" stroke="#5A4034" stroke-width="1.6"/><path d="M${x - 10} ${y - 4} Q${x} ${y - 12} ${x + 10} ${y - 4}" fill="#F6A07E" opacity=".75"/><g stroke="#E6CFCB" stroke-width="1.2" fill="none"><path d="M${x - 12} ${y - 10} l3 4 M${x - 6} ${y - 14} l2 5 M${x} ${y - 16} l0 5 M${x + 6} ${y - 14} l-2 5 M${x + 12} ${y - 10} l-3 4"/></g>` + TA.face(x, y, .7, mood);
    let lines = ""; for(let x = 30; x <= 170; x += 10) lines += `<path d="M${x} 98 V${116 + (1 - Math.abs(x - 100) / 80) * 10}" stroke="#B88A4E" stroke-width="1.2"/>`;
    return TA.sky("xjS", "#FFF4E3", "#FCE6C8")
      + `<path d="M20 96 V116 Q100 150 180 116 V96" fill="#D9AE6A" stroke="#5A4034" stroke-width="2"/>${lines}<ellipse cx="100" cy="96" rx="80" ry="28" fill="#E9C78B" stroke="#5A4034" stroke-width="2"/><ellipse cx="100" cy="96" rx="70" ry="22" fill="#F6E7C3" stroke="#C9A066" stroke-width="1.5"/>`
      + xj(66, 96, "smile") + xj(100, 90, "happy") + xj(134, 96, "smile") + xj(84, 110, "happy") + xj(118, 110, "smile")
      + TA.steam(84, 62) + TA.steam(120, 60, .8)
      + `<g transform="translate(170 40)"><path d="M-16 -10 Q-16 12 0 12 Q16 12 16 -10Z" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><path d="M16 -6 q8 0 8 6 q0 6 -8 6" fill="none" stroke="#5A4034" stroke-width="1.4"/><ellipse cx="0" cy="-10" rx="16" ry="4" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><path d="M-6 -16 L0 -22 L6 -16" fill="#5B8ED6" stroke="#5A4034" stroke-width="1"/><path d="M-10 2 Q0 6 10 2" stroke="#5B8ED6" stroke-width="1.2" fill="none"/></g>` + TA.cup(30, 46, 1.1);
  },
  changfen(){
    return TA.sky("cfS", "#FFF3E2", "#FFE5CB") + TA.table()
      + `<ellipse cx="100" cy="106" rx="84" ry="28" fill="#fff" stroke="#5A4034" stroke-width="2"/><ellipse cx="100" cy="104" rx="72" ry="22" fill="#F3EAD8"/>
      <ellipse cx="100" cy="104" rx="64" ry="16" fill="#D99B5A" opacity=".7"/>
      <g stroke="#5A4034" stroke-width="1.6"><path d="M42 96 Q46 84 62 86 L138 86 Q154 84 158 96 Q154 104 138 104 L62 104 Q46 104 42 96Z" fill="#FFF9F0" fill-opacity=".92"/><path d="M50 112 Q54 102 68 104 L132 104 Q146 102 150 112 Q146 120 132 120 L68 120 Q54 120 50 112Z" fill="#FFF9F0" fill-opacity=".92"/></g>
      <g fill="#F6A07E" opacity=".75"><ellipse cx="80" cy="95" rx="6" ry="3"/><ellipse cx="110" cy="95" rx="6" ry="3"/><ellipse cx="94" cy="112" rx="6" ry="3"/><ellipse cx="124" cy="112" rx="6" ry="3"/></g>
      <g fill="#6DBA4F"><circle cx="66" cy="94" r="1.8"/><circle cx="130" cy="92" r="1.8"/><circle cx="74" cy="112" r="1.8"/><circle cx="140" cy="110" r="1.8"/></g>`
      + TA.face(100, 96, .8, "happy") + TA.steam(86, 66) + TA.steam(116, 64, .8) + TA.cup(178, 136, 1.1) + TA.chop(18, 34, 64, 60);
  },
  /* ---------------- QUẢNG ĐÔNG ---------------- */
  danxia(){
    return TA.sky("dxS", "#CDE8FF", "#FFF2E6") + TA.cloud(160, 20, .7) + TA.birds([[60, 24], [70, 18, .7]])
      + `<path d="M0 100 Q10 50 40 48 Q60 46 66 70 L70 100Z" fill="#D9744A" stroke="#9E4A2A" stroke-width="1.8"/><path d="M60 100 Q62 34 100 30 Q136 30 140 60 L146 100Z" fill="#E28356" stroke="#9E4A2A" stroke-width="1.8"/><path d="M140 100 Q146 56 172 56 Q196 58 200 76 V100Z" fill="#D9744A" stroke="#9E4A2A" stroke-width="1.8"/>
      <g stroke="#B85A34" stroke-width="1.2" opacity=".7" fill="none"><path d="M76 50 Q100 44 130 52 M70 66 Q100 60 136 68 M66 82 Q100 76 140 84 M12 66 Q36 60 60 66 M150 72 Q172 66 196 74"/></g>
      <g fill="#6DAA5A"><ellipse cx="100" cy="30" rx="26" ry="6"/><ellipse cx="38" cy="48" rx="18" ry="5"/><ellipse cx="172" cy="56" rx="18" ry="5"/></g>
      <path d="M0 100 H200 V150 H0Z" fill="#7FBFCF"/><g opacity=".35"><path d="M60 100 Q100 140 146 100Z" fill="#E28356"/></g><path d="M20 120 q8 -3 16 0 M150 134 q8 -3 16 0" stroke="#D2EEF5" stroke-width="2" fill="none"/>
      <path d="M70 130 L100 130 L94 138 L76 138Z" fill="#C9A266" stroke="#6E4E36" stroke-width="1.2"/>` + TA.person(86, 130, .55, "#E8453C", { hat: "#F2B83A" }) + TA.grass(100, 104, 0, 1);
  },
  diaolou(){
    const tower = (x, w, h, c) => `<rect x="${x - w / 2}" y="${118 - h}" width="${w}" height="${h}" fill="${c}" stroke="#6E4E36" stroke-width="1.6"/>${Array.from({ length: Math.floor(h / 16) }, (_, i) => `<rect x="${x - 3}" y="${118 - h + 22 + i * 16}" width="6" height="7" rx="1" fill="#5A4034"/>`).join("")}<path d="M${x - w / 2 - 4} ${118 - h} h${w + 8} v-5 h-${w + 8}Z" fill="#E9D7B8" stroke="#6E4E36" stroke-width="1.2"/><path d="M${x - w / 2 - 2} ${118 - h - 5} Q${x} ${118 - h - 22} ${x + w / 2 + 2} ${118 - h - 5}" fill="${c}" stroke="#6E4E36" stroke-width="1.4"/><g fill="#6E4E36"><rect x="${x - w / 2 - 2}" y="${118 - h - 9}" width="3" height="4"/><rect x="${x + w / 2 - 1}" y="${118 - h - 9}" width="3" height="4"/></g>`;
    let rice = ""; for(let i = 0; i < 4; i++) rice += `<path d="M0 ${120 + i * 8} Q100 ${116 + i * 8} 200 ${122 + i * 8}" stroke="${i % 2 ? "#B9DE7E" : "#9FCF60"}" stroke-width="8" fill="none"/>`;
    return TA.sky("dlS", "#CFEAFF", "#F6FBF0") + TA.cloud(40, 22, .7) + TA.cloud(170, 18, .6)
      + `<path d="M0 108 Q50 92 100 104 Q150 94 200 106 V120 H0Z" fill="#9CC79A"/>`
      + tower(50, 22, 60, "#EFE3CC") + tower(104, 26, 80, "#F3E9D8") + tower(156, 22, 54, "#E9DCC4")
      + `<g><circle cx="76" cy="108" r="10" fill="#6DAA5A" stroke="#4E8F3A" stroke-width="1.2"/><circle cx="132" cy="110" r="9" fill="#7EC06C" stroke="#4E8F3A" stroke-width="1.2"/><circle cx="182" cy="108" r="8" fill="#6DAA5A" stroke="#4E8F3A" stroke-width="1.2"/></g>` + rice
      + TA.person(30, 146, .75, "#2F9E8F", { hat: "#E9C27E" }) + TA.birds([[100, 24], [110, 18, .7]]);
  },
  gangzhuao(){
    let cables = ""; [52, 140].forEach(x => { for(let i = -4; i <= 4; i++) if(i) cables += `<path d="M${x} 52 L${x + i * 9} 96" stroke="#fff" stroke-width=".9"/>`; });
    return TA.sky("gzaS", "#8FC9F2", "#E6F5FF") + TA.cloud(30, 22, .7) + TA.cloud(170, 26, .6) + TA.birds([[96, 30], [106, 24, .7]])
      + `<rect y="94" width="200" height="56" fill="#4F9FD0"/><g opacity=".5"><path d="M10 116 q8 -3 16 0 M90 128 q8 -3 16 0 M150 112 q8 -3 16 0 M40 140 q8 -3 16 0" stroke="#CFEAFB" stroke-width="2" fill="none"/></g>
      <path d="M0 98 Q100 86 200 96" stroke="#5A4034" stroke-width="7" fill="none"/><path d="M0 98 Q100 86 200 96" stroke="#E9E4DA" stroke-width="4" fill="none"/>
      <g fill="#E9E4DA" stroke="#5A4034" stroke-width="1.2"><rect x="20" y="96" width="3" height="10"/><rect x="80" y="92" width="3" height="10"/><rect x="120" y="92" width="3" height="10"/><rect x="180" y="96" width="3" height="10"/></g>
      ${cables}<g fill="#fff" stroke="#5A4034" stroke-width="1.4"><path d="M49 94 L51 52 L53 52 L55 94Z"/><path d="M137 92 L139 52 L141 52 L143 92Z"/></g>
      <g fill="#E8453C"><rect x="70" y="86" width="10" height="4" rx="1.5"/><rect x="108" y="84" width="10" height="4" rx="1.5"/></g><g fill="#F2B83A"><rect x="150" y="88" width="10" height="4" rx="1.5"/></g>
      <path d="M150 130 L180 130 L174 138 L156 138Z" fill="#fff" stroke="#5A4034" stroke-width="1.3"/><path d="M164 130 V118 L174 126Z" fill="#F2B83A" stroke="#5A4034" stroke-width="1.2"/>`;
  },
  shaoe(){
    return TA.sky("seS", "#FFF0DE", "#FFDDC2") + TA.table()
      + `<ellipse cx="100" cy="108" rx="84" ry="26" fill="#fff" stroke="#5A4034" stroke-width="2"/><ellipse cx="100" cy="106" rx="72" ry="19" fill="#F7F1E7"/>
      <path d="M34 104 Q30 72 70 66 Q112 60 134 80 Q142 92 132 104 Q100 114 60 112 Q38 110 34 104Z" fill="#A9461C" stroke="#5A4034" stroke-width="2"/><path d="M48 84 Q66 70 98 72" fill="none" stroke="#D2713A" stroke-width="5"/><ellipse cx="72" cy="78" rx="10" ry="3.4" fill="#fff" opacity=".55" transform="rotate(-10 72 78)"/>
      <path d="M128 96 Q144 92 146 102 Q140 108 128 106" fill="#9A3E18" stroke="#5A4034" stroke-width="1.6"/>
      <g stroke="#5A4034" stroke-width="1.4">${[0, 1, 2, 3].map(i => `<g transform="translate(${148 + i * 6} ${96 + i * 5}) rotate(-20)"><rect x="-12" y="-4" width="24" height="8" rx="3" fill="#B5502A"/><rect x="-12" y="1" width="24" height="3" rx="1.5" fill="#FBEFE0"/></g>`).join("")}</g>
      <path d="M20 128 Q20 144 38 144 Q56 144 56 128Z" fill="#fff" stroke="#5A4034" stroke-width="1.6"/><ellipse cx="38" cy="128" rx="18" ry="5" fill="#E9B04A" stroke="#5A4034" stroke-width="1.3"/>` + TA.face(38, 136, .6)
      + TA.steam(80, 52) + TA.steam(112, 50, .8)
      ;
  },
  niurouwan(){
    const ball = (x, y, mood) => `<circle cx="${x}" cy="${y}" r="11" fill="#B9886A" stroke="#6E4E36" stroke-width="1.6"/><ellipse cx="${x - 4}" cy="${y - 4}" rx="4" ry="2.4" fill="#fff" opacity=".45"/><g fill="#8E6448"><circle cx="${x + 4}" cy="${y + 4}" r=".9"/><circle cx="${x - 2}" cy="${y + 5}" r=".9"/></g>` + TA.face(x, y + 1, .65, mood);
    return TA.sky("nrS", "#FFF2E4", "#FFE2CC") + TA.table()
      + `<path d="M28 82 Q32 134 100 138 Q168 134 172 82Z" fill="#fff" stroke="#5A4034" stroke-width="2"/><path d="M36 104 Q100 118 164 104" fill="none" stroke="#5B8ED6" stroke-width="3"/>
      <ellipse cx="100" cy="82" rx="72" ry="17" fill="#F6E6C4" stroke="#5A4034" stroke-width="2"/>`
      + ball(72, 80, "happy") + ball(98, 76, "smile") + ball(124, 80, "happy") + ball(86, 90, "smile") + ball(112, 90, "happy")
      + `<g fill="#6DBA4F"><circle cx="60" cy="86" r="1.8"/><circle cx="138" cy="84" r="1.8"/><circle cx="100" cy="94" r="1.8"/></g><path d="M140 74 q10 -8 20 0 q-10 6 -20 0z" fill="#8FD068" stroke="#3F7F2F" stroke-width="1"/>`
      + TA.steam(84, 56) + TA.steam(116, 54, .8)
      + `<g transform="translate(36 40)">${ball(0, 0, "happy")}<path d="M-14 -16 l4 4 M14 -16 l-4 4 M0 -20 v5" stroke="#F2B83A" stroke-width="2"/></g>`
      + `<path d="M176 140 Q176 128 186 124 L192 140Z" fill="#fff" stroke="#5A4034" stroke-width="1.2"/><ellipse cx="180" cy="140" rx="14" ry="4" fill="#E8453C" stroke="#5A4034" stroke-width="1.2"/>`;
  }
});

/* Tranh dùng ảnh (do giáo viên cung cấp) – ưu tiên hơn tranh vẽ */
const TRIP_IMG = typeof TRIP_IMG_DATA !== "undefined" ? TRIP_IMG_DATA : {};
function tripArt(k){
  if(TRIP_IMG[k]) return `<img class="tp-art tp-img" src="${TRIP_IMG[k]}" alt="" loading="lazy">`;
  return TA.wrap(k, ART[k]() + (ART_X[k] ? ART_X[k]() : "") + TA.light(k), "");
}
