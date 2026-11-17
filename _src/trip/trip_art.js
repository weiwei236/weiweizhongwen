/* ===== Tranh chibi cho trò chơi "Khám phá Trung Quốc" (viewBox 0 0 200 150) ===== */
const TA = {
  OL: "#5A4034",
  sky(id, a, b){ return `<defs><linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${a}"/><stop offset="1" stop-color="${b}"/></linearGradient></defs><rect width="200" height="150" fill="url(#${id})"/>`; },
  face(x, y, s = 1, mood = "smile", ink = "#4A3328"){
    const e = mood === "happy"
      ? `<path d="M${x - 6 * s} ${y} q${2.2 * s} ${-2.6 * s} ${4.4 * s} 0 M${x + 1.6 * s} ${y} q${2.2 * s} ${-2.6 * s} ${4.4 * s} 0" stroke="${ink}" stroke-width="${1.4 * s}" fill="none" stroke-linecap="round"/>`
      : `<ellipse cx="${x - 3.8 * s}" cy="${y}" rx="${1.3 * s}" ry="${1.6 * s}" fill="${ink}"/><ellipse cx="${x + 3.8 * s}" cy="${y}" rx="${1.3 * s}" ry="${1.6 * s}" fill="${ink}"/><circle cx="${x - 3.4 * s}" cy="${y - 0.6 * s}" r="${0.45 * s}" fill="#fff"/><circle cx="${x + 4.2 * s}" cy="${y - 0.6 * s}" r="${0.45 * s}" fill="#fff"/>`;
    return `<g stroke="none">${e}<ellipse cx="${x - 6.4 * s}" cy="${y + 2.8 * s}" rx="${2 * s}" ry="${1.2 * s}" fill="#F48B8B" opacity=".55"/><ellipse cx="${x + 6.4 * s}" cy="${y + 2.8 * s}" rx="${2 * s}" ry="${1.2 * s}" fill="#F48B8B" opacity=".55"/><path d="M${x - 1.6 * s} ${y + 2.4 * s} q${1.6 * s} ${1.6 * s} ${3.2 * s} 0" stroke="${ink}" stroke-width="${1.1 * s}" fill="none" stroke-linecap="round"/></g>`;
  },
  cloud(x, y, s = 1, face = true){
    return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-22 7 Q-25 -5 -12 -6 Q-8 -17 4 -14 Q15 -19 18 -8 Q29 -7 25 5 Q24 10 17 10 L-15 10 Q-22 10 -22 7Z" fill="#fff" stroke="#E3EEF7" stroke-width="1.5"/>${face ? TA.face(1, 1, .7, "happy", "#8AA0B8") : ""}</g>`;
  },
  sun(x, y, r = 13){
    let rays = ""; for(let i = 0; i < 8; i++){ const a = i * Math.PI / 4, c = Math.cos(a), s = Math.sin(a); rays += `<path d="M${x + c * (r + 4)} ${y + s * (r + 4)} L${x + c * (r + 9)} ${y + s * (r + 9)}"/>`; }
    return `<g stroke="#F5B53A" stroke-width="3" stroke-linecap="round">${rays}</g><circle cx="${x}" cy="${y}" r="${r}" fill="#FFD45C" stroke="#F2A93B" stroke-width="2"/>${TA.face(x, y + 1, r / 11, "happy")}`;
  },
  steam(x, y, s = 1){ return `<g fill="none" stroke="#fff" stroke-width="${3 * s}" stroke-linecap="round" opacity=".9"><path d="M${x} ${y} q${-5 * s} ${-7 * s} 0 ${-14 * s} q${5 * s} ${-7 * s} 0 ${-14 * s}"/><path d="M${x + 12 * s} ${y + 2} q${-5 * s} ${-7 * s} 0 ${-14 * s} q${5 * s} ${-6 * s} 0 ${-12 * s}"/></g>`; },
  flakes(n, seed, col = "#fff"){ let h = "", r = seed; for(let i = 0; i < n; i++){ r = (r * 9301 + 49297) % 233280; const x = r / 233280 * 200; r = (r * 9301 + 49297) % 233280; const y = r / 233280 * 110; h += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(1.2 + (i % 3) * .6).toFixed(1)}" fill="${col}" opacity=".9"/>`; } return h; },
  stars(n, seed){ let h = "", r = seed; for(let i = 0; i < n; i++){ r = (r * 9301 + 49297) % 233280; const x = r / 233280 * 200; r = (r * 9301 + 49297) % 233280; const y = r / 233280 * 60; h += `<path d="M${x.toFixed(1)} ${(y - 2.4).toFixed(1)} L${(x + .7).toFixed(1)} ${(y - .7).toFixed(1)} L${(x + 2.4).toFixed(1)} ${y.toFixed(1)} L${(x + .7).toFixed(1)} ${(y + .7).toFixed(1)} L${x.toFixed(1)} ${(y + 2.4).toFixed(1)} L${(x - .7).toFixed(1)} ${(y + .7).toFixed(1)} L${(x - 2.4).toFixed(1)} ${y.toFixed(1)} L${(x - .7).toFixed(1)} ${(y - .7).toFixed(1)}Z" fill="#FFF3B0"/>`; } return h; },
  lantern(x, y, s = 1){ return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M0 -6 V-2" stroke="#5A4034" stroke-width="1.2"/><ellipse cx="0" cy="4" rx="5" ry="6" fill="#E8453C" stroke="#A8302A" stroke-width="1.2"/><rect x="-2.5" y="-2.5" width="5" height="1.8" rx=".8" fill="#F2B83A"/><rect x="-2.5" y="9.2" width="5" height="1.8" rx=".8" fill="#F2B83A"/><path d="M0 11 V15" stroke="#F2B83A" stroke-width="1.2"/></g>`; },
  willow(x, y, s = 1, flip = false){
    let br = ""; for(let i = 0; i < 9; i++){ const bx = 6 + i * 6, len = 34 + (i % 3) * 10; br += `<path d="M${bx} 4 Q${bx + 4} ${len * .5} ${bx - 2} ${len}" fill="none" stroke="#7CB85A" stroke-width="2.2" stroke-linecap="round"/>`; }
    return `<g transform="translate(${x} ${y}) scale(${flip ? -s : s} ${s})"><path d="M-6 80 Q0 40 -4 0" stroke="#7A5638" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M-4 2 Q20 -10 60 4" stroke="#7A5638" stroke-width="3.5" fill="none" stroke-linecap="round"/>${br}</g>`;
  },
  roof(x1, x2, y, h, fill, ol = "#4A3E3A", curl = 7){
    /* mái cong kiểu Trung Hoa: đáy y, cao h, hai đầu vểnh lên */
    return `<path d="M${x1 - curl} ${y - curl * .9} Q${x1 - 1} ${y + 2} ${x1 + 10} ${y} L${x2 - 10} ${y} Q${x2 + 1} ${y + 2} ${x2 + curl} ${y - curl * .9} Q${x2 - 4} ${y - 2} ${x2 - 14} ${y - h} L${x1 + 14} ${y - h} Q${x1 + 4} ${y - 2} ${x1 - curl} ${y - curl * .9}Z" fill="${fill}" stroke="${ol}" stroke-width="2" stroke-linejoin="round"/>`;
  },
  wrap(key, inner, label){ return `<svg class="tp-art" viewBox="0 0 200 150" role="img" aria-label="${label || ""}"><g stroke-linejoin="round" stroke-linecap="round">${inner}</g></svg>`; }
};

const ART = {
  /* ---------------- BẮC KINH ---------------- */
  gugong(){
    let cols = ""; for(let x = 54; x <= 146; x += 13) cols += `<rect x="${x}" y="68" width="5" height="32" rx="1.5" fill="#B8352B"/>`;
    let tiles = ""; for(let x = 58; x <= 142; x += 7) tiles += `<path d="M${x} 61 L${x - 2} 73" stroke="#E09A2A" stroke-width="1.2"/>`;
    return TA.sky("ggS", "#BFE4FF", "#EEF8FF") + TA.cloud(34, 26, .9) + TA.cloud(160, 20, .75) + TA.sun(178, 44, 10)
      + `<rect y="116" width="200" height="34" fill="#EAD7AE"/><path d="M0 128 H200 M0 140 H200" stroke="#D9C291" stroke-width="1.5"/>
      <path d="M18 116 L182 116 L172 101 L28 101Z" fill="#F5F2EA" stroke="${TA.OL}" stroke-width="2"/>
      <path d="M30 107 H170" stroke="#CFC8B8" stroke-width="2" stroke-dasharray="2 4"/>
      <path d="M86 116 L114 116 L110 101 L90 101Z" fill="#E6E0D2" stroke="${TA.OL}" stroke-width="1.6"/>
      <rect x="46" y="68" width="108" height="34" rx="2" fill="#D9483B" stroke="${TA.OL}" stroke-width="2"/>${cols}
      <path d="M90 102 V84 Q100 76 110 84 V102Z" fill="#8E2A22" stroke="${TA.OL}" stroke-width="1.6"/>
      <g fill="#F2C14E" stroke="none"><circle cx="95" cy="90" r="1"/><circle cx="105" cy="90" r="1"/><circle cx="95" cy="96" r="1"/><circle cx="105" cy="96" r="1"/></g>`
      + TA.roof(46, 154, 72, 14, "#F2B33D", TA.OL, 9) + tiles
      + `<rect x="66" y="44" width="68" height="18" rx="2" fill="#D9483B" stroke="${TA.OL}" stroke-width="2"/>
      <rect x="91" y="47" width="18" height="10" rx="1.5" fill="#2F5FA8" stroke="#F2C14E" stroke-width="1.4"/>`
      + TA.roof(62, 138, 48, 13, "#F6C04A", TA.OL, 8)
      + `<path d="M74 35 Q100 31 126 35" stroke="${TA.OL}" stroke-width="3" fill="none"/><circle cx="73" cy="33" r="2.4" fill="#F2B33D" stroke="${TA.OL}" stroke-width="1.3"/><circle cx="127" cy="33" r="2.4" fill="#F2B33D" stroke="${TA.OL}" stroke-width="1.3"/>`
      + TA.lantern(40, 76, 1) + TA.lantern(160, 76, 1);
  },
  changcheng(){
    const wall = "M-6 98 Q28 64 58 82 Q88 100 114 78 Q140 58 168 70 Q188 78 206 74";
    let trees = ""; [[24, 124, "#F08A3C"], [46, 132, "#E25B45"], [150, 128, "#F2B33D"], [176, 120, "#E25B45"], [118, 138, "#F08A3C"]].forEach(([x, y, c]) => trees += `<circle cx="${x}" cy="${y}" r="9" fill="${c}" stroke="${TA.OL}" stroke-width="1.6"/><path d="M${x} ${y + 8} V${y + 15}" stroke="${TA.OL}" stroke-width="2"/>`);
    const tower = (x, y) => `<g transform="translate(${x} ${y})"><rect x="-11" y="-24" width="22" height="24" rx="2" fill="#EBD3A6" stroke="${TA.OL}" stroke-width="2"/><path d="M-12 -24 h5 v-4 h4 v4 h6 v-4 h4 v4 h5" fill="#EBD3A6" stroke="${TA.OL}" stroke-width="1.8"/><path d="M-4 0 V-8 Q0 -13 4 -8 V0Z" fill="#6D4B36"/><rect x="-7" y="-19" width="4" height="5" rx="1" fill="#6D4B36"/><rect x="3" y="-19" width="4" height="5" rx="1" fill="#6D4B36"/></g>`;
    return TA.sky("ccS", "#FFE0BD", "#D7EEFF") + TA.sun(30, 30, 11) + TA.cloud(150, 24, .8)
      + `<path d="M0 96 Q24 58 52 76 Q80 44 112 70 Q140 48 172 64 Q190 72 200 68 L200 150 L0 150Z" fill="#B7DC9F" stroke="#8FBF78" stroke-width="2"/>
      <path d="M0 122 Q50 96 100 112 Q150 126 200 102 L200 150 L0 150Z" fill="#86C273" stroke="#6BA95C" stroke-width="2"/>
      <path d="${wall}" fill="none" stroke="#7A5A40" stroke-width="15"/><path d="${wall}" fill="none" stroke="#EBD3A6" stroke-width="10.5"/>
      <g transform="translate(0 -6)"><path d="${wall}" fill="none" stroke="#7A5A40" stroke-width="6" stroke-dasharray="4 3.5"/><path d="${wall}" fill="none" stroke="#EBD3A6" stroke-width="3.4" stroke-dasharray="4 3.5"/></g>`
      + tower(58, 84) + tower(140, 63) + trees;
  },
  tiantan(){
    const tier = (y, rx, h) => `<path d="M${100 - rx} ${y} V${y + h} Q100 ${y + h + 9} ${100 + rx} ${y + h} V${y}" fill="#ECE8DF" stroke="${TA.OL}" stroke-width="1.8"/><ellipse cx="100" cy="${y}" rx="${rx}" ry="7" fill="#F8F6F1" stroke="${TA.OL}" stroke-width="1.8"/><path d="M${100 - rx + 6} ${y + 1} Q100 ${y + 9} ${100 + rx - 6} ${y + 1}" fill="none" stroke="#CFC8B8" stroke-width="1.5" stroke-dasharray="1.5 3"/>`;
    const body = (y, w, h) => `<path d="M${100 - w} ${y} V${y + h} Q100 ${y + h + 5} ${100 + w} ${y + h} V${y}Z" fill="#D9483B" stroke="${TA.OL}" stroke-width="1.8"/>` + Array.from({ length: 5 }, (_, i) => `<path d="M${100 - w + 6 + i * (2 * w - 12) / 4} ${y + 1} V${y + h + 1}" stroke="#B4352C" stroke-width="2"/>`).join("");
    const cone = (y, w, h) => `<path d="M${100 - w} ${y} Q100 ${y - h - 6} ${100 + w} ${y} Q100 ${y + 7} ${100 - w} ${y}Z" fill="#3A6FC4" stroke="${TA.OL}" stroke-width="1.8"/><path d="M${100 - w + 3} ${y + 1} Q100 ${y + 6} ${100 + w - 3} ${y + 1}" fill="none" stroke="#F2B83A" stroke-width="2"/><path d="M${100 - w * .45} ${y - h * .45} Q100 ${y - h * .7} ${100 + w * .2} ${y - h * .55}" fill="none" stroke="#7FA8E6" stroke-width="2"/>`;
    let trees = ""; [[16, 112], [184, 112], [30, 104], [170, 104]].forEach(([x, y]) => trees += `<circle cx="${x}" cy="${y}" r="10" fill="#7EC06C" stroke="${TA.OL}" stroke-width="1.6"/>`);
    return TA.sky("ttS", "#C9E7FF", "#F2FAFF") + TA.cloud(30, 24, .8) + TA.cloud(168, 30, .7)
      + `<rect y="126" width="200" height="24" fill="#BFE0A8"/>` + trees
      + tier(118, 84, 9) + tier(108, 68, 9) + tier(98, 54, 9)
      + body(80, 32, 16) + cone(82, 46, 14) + body(64, 24, 13) + cone(66, 36, 12) + body(50, 17, 11) + cone(51, 27, 11)
      + `<path d="M100 38 V30" stroke="${TA.OL}" stroke-width="2"/><circle cx="100" cy="27" r="4" fill="#F2B83A" stroke="${TA.OL}" stroke-width="1.6"/>`;
  },
  kaoya(){
    return TA.sky("kyS", "#FFF2DF", "#FFE0C2")
      + `<g opacity=".35"><path d="M0 120 H200 M0 136 H200 M20 112 V150 M60 112 V150 M100 112 V150 M140 112 V150 M180 112 V150" stroke="#E7A07A" stroke-width="6"/></g>
      <ellipse cx="96" cy="104" rx="80" ry="28" fill="#fff" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="96" cy="102" rx="66" ry="21" fill="#F7F1E7" stroke="#E2D7C6" stroke-width="1.5"/>
      <path d="M50 98 Q44 72 74 64 Q104 56 126 72 Q138 82 130 98 Q110 110 78 108 Q56 106 50 98Z" fill="#C4612C" stroke="${TA.OL}" stroke-width="2"/>
      <path d="M62 82 Q76 66 102 68" fill="none" stroke="#E98E4E" stroke-width="5" opacity=".9"/><ellipse cx="84" cy="74" rx="9" ry="3.5" fill="#fff" opacity=".55" transform="rotate(-12 84 74)"/>
      <path d="M118 92 Q138 88 140 100 Q134 108 120 104" fill="#B5582A" stroke="${TA.OL}" stroke-width="1.8"/>
      <g stroke="${TA.OL}" stroke-width="1.5"><ellipse cx="150" cy="104" rx="13" ry="6" fill="#D47A44" transform="rotate(-14 150 104)"/><path d="M139 106 Q150 99 162 101" stroke="#FBEFE0" stroke-width="2.5" fill="none"/><ellipse cx="158" cy="112" rx="13" ry="6" fill="#D47A44" transform="rotate(-8 158 112)"/><path d="M147 114 Q158 108 170 110" stroke="#FBEFE0" stroke-width="2.5" fill="none"/></g>
      <g stroke="${TA.OL}" stroke-width="1.5"><ellipse cx="36" cy="128" rx="24" ry="8" fill="#FBEFD7"/><ellipse cx="36" cy="124" rx="24" ry="8" fill="#FDF4E2"/><ellipse cx="36" cy="120" rx="24" ry="8" fill="#FFF8EC"/></g>
      <g stroke="#4E8B3A" stroke-width="1.2"><rect x="62" y="112" width="22" height="5" rx="2.5" fill="#8CCB6A" transform="rotate(-8 73 114)"/><rect x="64" y="118" width="22" height="5" rx="2.5" fill="#A8D985" transform="rotate(-4 75 120)"/><path d="M90 116 L112 112" stroke="#7DBB55" stroke-width="2.5"/></g>
      <path d="M160 126 Q160 142 178 142 Q196 142 196 126Z" fill="#fff" stroke="${TA.OL}" stroke-width="1.8"/><ellipse cx="178" cy="126" rx="18" ry="5" fill="#5B2E22" stroke="${TA.OL}" stroke-width="1.6"/>` + TA.face(178, 134, .7)
      + TA.steam(88, 54, .8);
  },
  tanghulu(){
    const ball = (x, y, mood) => `<circle cx="${x}" cy="${y}" r="13" fill="#E2383F" stroke="#9E2128" stroke-width="2"/><path d="M${x - 9} ${y - 4} Q${x - 6} ${y - 11} ${x + 1} ${y - 11}" fill="none" stroke="#fff" stroke-width="2.6" opacity=".8"/><path d="M${x + 6} ${y + 10} q1 4 -1 6" stroke="#FFD9D2" stroke-width="2" fill="none" opacity=".8"/>` + TA.face(x, y + 1, .8, mood, "#5A1515");
    return TA.sky("thS", "#FFE3EC", "#FFF6E9") + TA.flakes(22, 7, "#fff") + TA.cloud(160, 24, .8)
      + `<path d="M70 146 L78 30" stroke="#B98552" stroke-width="4"/><g transform="rotate(4 74 80)">${ball(77, 42, "happy")}${ball(76, 68, "smile")}${ball(75, 94, "happy")}${ball(74, 120, "smile")}</g>
      <g opacity=".95"><path d="M126 148 L138 46" stroke="#B98552" stroke-width="4"/><g transform="rotate(7 132 96)">${ball(137, 58, "smile")}${ball(135, 84, "happy")}${ball(133, 110, "smile")}</g></g>
      <g fill="#FFF7D6" stroke="#E7C76E" stroke-width="1"><circle cx="100" cy="60" r="2"/><circle cx="108" cy="80" r="1.6"/><circle cx="96" cy="104" r="1.8"/></g>`;
  },
  /* ---------------- THƯỢNG HẢI ---------------- */
  mingzhu(){
    let bld = ""; [[6, 70, 22, "#A9BDE0"], [30, 56, 18, "#B9C9EA"], [150, 48, 20, "#A9BDE0"], [172, 62, 22, "#B9C9EA"], [126, 76, 18, "#C5D3EE"], [52, 82, 16, "#C5D3EE"]].forEach(([x, y, w, c]) => { bld += `<rect x="${x}" y="${y}" width="${w}" height="${122 - y}" rx="3" fill="${c}" stroke="#7F93BF" stroke-width="1.5"/>`; for(let yy = y + 6; yy < 116; yy += 9) bld += `<path d="M${x + 4} ${yy} H${x + w - 4}" stroke="#FFF2B8" stroke-width="2" stroke-dasharray="2 3"/>`; });
    return TA.sky("mzS", "#8FA9E8", "#FFD3C1") + TA.stars(10, 3) + bld
      + `<rect y="120" width="200" height="30" fill="#5E8FD0"/><path d="M10 130 q8 -4 16 0 t16 0 M120 138 q8 -4 16 0 t16 0 M60 144 q8 -4 16 0 t16 0" stroke="#A9C8F0" stroke-width="2" fill="none"/>
      <g stroke="${TA.OL}" stroke-width="1.8"><path d="M80 122 L93 96" stroke-width="7"/><path d="M120 122 L107 96" stroke-width="7"/><path d="M80 122 L93 96 M120 122 L107 96" stroke="#E6E9F2" stroke-width="4"/>
      <rect x="93" y="30" width="5" height="64" fill="#E6E9F2"/><rect x="102" y="30" width="5" height="64" fill="#E6E9F2"/></g>
      <circle cx="100" cy="94" r="19" fill="#EC5F8E" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="93" cy="86" rx="6" ry="4" fill="#fff" opacity=".45"/>` + TA.face(100, 96, 1.1, "happy", "#6B1C3A")
      + `<g stroke="${TA.OL}" stroke-width="1.6"><circle cx="100" cy="71" r="3.4" fill="#F28FB0"/><circle cx="100" cy="64" r="3.4" fill="#F28FB0"/></g>
      <circle cx="100" cy="50" r="12" fill="#EC5F8E" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="95" cy="45" rx="4" ry="2.6" fill="#fff" opacity=".45"/>
      <rect x="98" y="26" width="4" height="12" fill="#E6E9F2" stroke="${TA.OL}" stroke-width="1.5"/><circle cx="100" cy="25" r="4.5" fill="#F28FB0" stroke="${TA.OL}" stroke-width="1.6"/><path d="M100 20 V6" stroke="${TA.OL}" stroke-width="2.2"/>
      <g fill="#FFF2B8"><circle cx="86" cy="100" r="1.3"/><circle cx="114" cy="100" r="1.3"/><circle cx="100" cy="112" r="1.3"/><circle cx="91" cy="54" r="1.1"/><circle cx="109" cy="54" r="1.1"/></g>`;
  },
  waitan(){
    const b = (x, w, h, c, extra = "") => { let s = `<rect x="${x}" y="${108 - h}" width="${w}" height="${h}" rx="2" fill="${c}" stroke="${TA.OL}" stroke-width="1.8"/>`; for(let xx = x + 5; xx < x + w - 3; xx += 6) s += `<rect x="${xx}" y="${108 - h + 8}" width="3" height="${h - 14}" rx="1" fill="#fff" opacity=".55"/>`; return s + extra; };
    return TA.sky("wtS", "#FFD9B5", "#CFE6FF") + TA.cloud(160, 22, .8) + TA.sun(36, 30, 9)
      + b(4, 30, 46, "#EBD7B5") + b(36, 26, 40, "#DCC7A4", `<path d="M36 68 Q49 54 62 68Z" fill="#7FA9A0" stroke="${TA.OL}" stroke-width="1.6"/>`)
      + `<rect x="66" y="40" width="24" height="68" rx="2" fill="#F1E2C4" stroke="${TA.OL}" stroke-width="1.8"/><path d="M64 42 L78 22 L92 42Z" fill="#9FBFAE" stroke="${TA.OL}" stroke-width="1.8"/><circle cx="78" cy="52" r="7" fill="#fff" stroke="${TA.OL}" stroke-width="1.6"/><path d="M78 47 V52 L82 54" stroke="${TA.OL}" stroke-width="1.4" fill="none"/>`
      + b(92, 30, 52, "#E3CFAE", `<path d="M96 56 Q107 40 118 56Z" fill="#8DB5A8" stroke="${TA.OL}" stroke-width="1.6"/>`) + b(124, 26, 44, "#EFE0C2") + b(152, 44, 38, "#DCC7A4")
      + `<rect y="108" width="200" height="12" fill="#BFA98A" stroke="${TA.OL}" stroke-width="1.5"/><path d="M0 104 H200" stroke="${TA.OL}" stroke-width="2"/><path d="M4 104 V110 M14 104 V110 M24 104 V110 M34 104 V110 M44 104 V110 M54 104 V110 M64 104 V110 M74 104 V110 M84 104 V110 M94 104 V110 M104 104 V110 M114 104 V110 M124 104 V110 M134 104 V110 M144 104 V110 M154 104 V110 M164 104 V110 M174 104 V110 M184 104 V110 M194 104 V110" stroke="${TA.OL}" stroke-width="1.2"/>
      <rect y="120" width="200" height="30" fill="#7FB0DC"/><path d="M14 132 q8 -4 16 0 t16 0 M110 140 q8 -4 16 0 t16 0" stroke="#C3DCF2" stroke-width="2" fill="none"/>
      <g stroke="${TA.OL}" stroke-width="1.6"><path d="M40 104 V84" /><circle cx="40" cy="82" r="3.5" fill="#FFE27A"/><path d="M150 104 V84"/><circle cx="150" cy="82" r="3.5" fill="#FFE27A"/></g>
      <path d="M150 138 L176 138 L170 146 L156 146Z" fill="#fff" stroke="${TA.OL}" stroke-width="1.6"/><path d="M162 138 V126 L172 134Z" fill="#F28B5B" stroke="${TA.OL}" stroke-width="1.4"/>`;
  },
  yuyuan(){
    let lot = ""; [[30, 132], [60, 140], [168, 136], [146, 142]].forEach(([x, y]) => lot += `<ellipse cx="${x}" cy="${y}" rx="11" ry="4.5" fill="#6DB36A" stroke="#3F7F45" stroke-width="1.4"/>`);
    return TA.sky("yyS", "#D6EEFF", "#F4FBFF") + TA.cloud(56, 22, .8) + TA.willow(8, 4, 1)
      + `<rect y="88" width="200" height="62" fill="#8CCBD6"/><path d="M0 88 H200" stroke="#5FA7B6" stroke-width="2"/>` + lot
      + `<circle cx="34" cy="128" r="4" fill="#F59BB5" stroke="#C25B7C" stroke-width="1.2"/>
      <path d="M-4 140 L46 122 L34 110 L84 98 L74 90 L120 86" fill="none" stroke="#7A5A40" stroke-width="11"/><path d="M-4 140 L46 122 L34 110 L84 98 L74 90 L120 86" fill="none" stroke="#EADCC2" stroke-width="7"/>
      <path d="M-4 134 L46 116 L34 104 L84 92 L74 84 L120 80" fill="none" stroke="#B5463A" stroke-width="2"/>
      <rect x="128" y="64" width="54" height="24" rx="2" fill="#F3E6CC" stroke="${TA.OL}" stroke-width="1.8"/>
      <g fill="#C9483B" stroke="${TA.OL}" stroke-width="1.2"><rect x="132" y="64" width="4" height="24"/><rect x="152" y="64" width="4" height="24"/><rect x="174" y="64" width="4" height="24"/></g>
      <rect x="140" y="70" width="10" height="10" rx="1.5" fill="#9AC7D8" stroke="${TA.OL}" stroke-width="1.2"/><rect x="160" y="70" width="10" height="10" rx="1.5" fill="#9AC7D8" stroke="${TA.OL}" stroke-width="1.2"/>`
      + TA.roof(126, 184, 66, 12, "#646C78", TA.OL, 11)
      + `<rect x="140" y="44" width="30" height="12" rx="2" fill="#F3E6CC" stroke="${TA.OL}" stroke-width="1.6"/>` + TA.roof(136, 174, 46, 11, "#646C78", TA.OL, 10)
      + `<circle cx="155" cy="32" r="2.6" fill="#F2B83A" stroke="${TA.OL}" stroke-width="1.2"/>` + TA.lantern(130, 72, .8) + TA.lantern(180, 72, .8);
  },
  xiaolongbao(){
    const bao = (x, y, mood) => `<path d="M${x - 17} ${y + 4} Q${x - 20} ${y - 12} ${x} ${y - 18} Q${x + 20} ${y - 12} ${x + 17} ${y + 4} Q${x} ${y + 11} ${x - 17} ${y + 4}Z" fill="#FFFBF2" stroke="${TA.OL}" stroke-width="1.8"/><g stroke="#D9CBB2" stroke-width="1.4" fill="none"><path d="M${x} ${y - 18} Q${x - 10} ${y - 10} ${x - 13} ${y}"/><path d="M${x} ${y - 18} Q${x - 4} ${y - 8} ${x - 5} ${y + 2}"/><path d="M${x} ${y - 18} Q${x + 4} ${y - 8} ${x + 5} ${y + 2}"/><path d="M${x} ${y - 18} Q${x + 10} ${y - 10} ${x + 13} ${y}"/></g><circle cx="${x}" cy="${y - 18}" r="2.4" fill="#FFFBF2" stroke="${TA.OL}" stroke-width="1.4"/>` + TA.face(x, y - 2, .75, mood);
    let lines = ""; for(let x = 30; x <= 170; x += 10) lines += `<path d="M${x} ${100 + Math.abs(x - 100) * -.05} V${118 + (1 - Math.abs(x - 100) / 80) * 10}" stroke="#B88A4E" stroke-width="1.2"/>`;
    return TA.sky("xlS", "#FFF4E0", "#FCE4C2")
      + `<path d="M20 96 V116 Q100 150 180 116 V96" fill="#D9AE6A" stroke="${TA.OL}" stroke-width="2"/>${lines}<ellipse cx="100" cy="96" rx="80" ry="28" fill="#E9C78B" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="100" cy="96" rx="70" ry="22" fill="#F6E7C3" stroke="#C9A066" stroke-width="1.5"/>`
      + bao(64, 98, "smile") + bao(100, 92, "happy") + bao(136, 98, "smile") + bao(84, 112, "happy") + bao(118, 112, "smile")
      + TA.steam(80, 64) + TA.steam(118, 60)
      + `<path d="M150 30 L196 62" stroke="#8A5A36" stroke-width="4"/><path d="M158 24 L198 54" stroke="#8A5A36" stroke-width="4"/>`;
  },
  shengjian(){
    const bun = (x, y, mood) => `<ellipse cx="${x}" cy="${y + 7}" rx="17" ry="7" fill="#D99A3C" stroke="${TA.OL}" stroke-width="1.6"/><path d="M${x - 17} ${y + 6} Q${x - 18} ${y - 12} ${x} ${y - 14} Q${x + 18} ${y - 12} ${x + 17} ${y + 6}Z" fill="#FFF8EA" stroke="${TA.OL}" stroke-width="1.8"/><g fill="#3D3530"><circle cx="${x - 5}" cy="${y - 9}" r=".9"/><circle cx="${x + 3}" cy="${y - 11}" r=".9"/><circle cx="${x + 8}" cy="${y - 7}" r=".9"/></g><g fill="#fff" stroke="#C9BBA0" stroke-width=".5"><ellipse cx="${x - 1}" cy="${y - 7}" rx="1.2" ry=".7"/><ellipse cx="${x + 6}" cy="${y - 12}" rx="1.2" ry=".7"/></g><g fill="#6DBA4F"><rect x="${x - 9}" y="${y - 12}" width="3.5" height="2" rx="1"/><rect x="${x + 1}" y="${y - 6}" width="3.5" height="2" rx="1"/></g>` + (mood ? TA.face(x, y, .7, mood) : "");
    return TA.sky("sjS", "#FFF1DE", "#FFE6CC")
      + `<path d="M176 90 L198 74" stroke="#3A3A42" stroke-width="9"/><path d="M178 89 L198 75" stroke="#55555F" stroke-width="5"/>
      <ellipse cx="96" cy="100" rx="84" ry="36" fill="#3C3C46" stroke="#222" stroke-width="2"/><ellipse cx="96" cy="98" rx="74" ry="29" fill="#55555F"/>`
      + bun(62, 92, "smile") + bun(98, 86, "") + bun(134, 92, "happy") + bun(78, 112, "happy") + bun(116, 112, "")
      + TA.steam(86, 60) + TA.steam(124, 62, .8);
  },
  /* ---------------- TRÙNG KHÁNH ---------------- */
  hongyadong(){
    let h = ""; const rows = [[118, 14, 172], [100, 22, 160], [82, 32, 150], [64, 42, 138], [46, 52, 126], [30, 62, 112]];
    rows.forEach(([y, x1, x2], r) => {
      h += `<rect x="${x1}" y="${y}" width="${x2 - x1}" height="16" fill="${r % 2 ? "#6E4330" : "#7D4D36"}" stroke="#3B2418" stroke-width="1.4"/>`;
      for(let x = x1 + 5; x < x2 - 6; x += 9) h += `<rect x="${x}" y="${y + 4}" width="5" height="7" rx="1" fill="#FFD66B"/>`;
      h += `<path d="M${x1 - 5} ${y + 1} Q${x1} ${y - 1} ${x1 + 6} ${y - 4} L${x2 - 6} ${y - 4} Q${x2} ${y - 1} ${x2 + 5} ${y + 1}Z" fill="#3A2C2A" stroke="#1F1512" stroke-width="1.2"/>`;
      for(let x = x1 + 10; x < x2; x += 26) h += TA.lantern(x, y + 3, .55);
    });
    return TA.sky("hyS", "#1F3164", "#4D5C9A") + TA.stars(16, 11)
      + `<circle cx="172" cy="24" r="10" fill="#FFF3B0" stroke="#E9CF6C" stroke-width="1.5"/>` + TA.face(172, 25, .8, "happy", "#9A7A2A")
      + `<path d="M0 134 L0 60 Q20 50 40 70 L60 134Z" fill="#2A3B5A"/><path d="M200 134 L200 40 Q182 34 170 60 L160 134Z" fill="#2A3B5A"/>` + h
      + `<path d="M64 26 V18" stroke="#1F1512" stroke-width="2"/><rect y="134" width="200" height="16" fill="#243E70"/><g stroke="#FFD66B" stroke-width="2" opacity=".7"><path d="M30 140 H50 M70 144 H96 M110 140 H140 M150 146 H170"/></g>`;
  },
  suodao(){
    return TA.sky("sdS", "#BFE2FF", "#EAF6FF") + TA.cloud(40, 22, .8) + TA.cloud(130, 18, .65)
      + `<path d="M0 70 Q20 58 40 66 L56 116 L0 116Z" fill="#8CC27A" stroke="#5F9A55" stroke-width="2"/>
      <g stroke="${TA.OL}" stroke-width="1.5"><rect x="4" y="62" width="14" height="40" rx="2" fill="#F2DDBB"/><rect x="20" y="70" width="16" height="34" rx="2" fill="#E7CFA8"/><rect x="150" y="34" width="18" height="78" rx="2" fill="#D8E3F2"/><rect x="170" y="48" width="24" height="64" rx="2" fill="#C9D7EC"/><rect x="132" y="62" width="16" height="50" rx="2" fill="#E3EBF6"/></g>
      <g stroke="#FFF" stroke-width="2" stroke-dasharray="2 4" opacity=".8"><path d="M155 42 V108 M162 42 V108 M176 56 V108 M186 56 V108"/></g>
      <rect y="112" width="200" height="38" fill="#D9A866"/><path d="M0 116 Q50 110 100 118 T200 114 V150 H0Z" fill="#C49456"/><path d="M20 130 q8 -3 16 0 t16 0 M120 140 q8 -3 16 0 t16 0" stroke="#E8C792" stroke-width="2" fill="none"/>
      <path d="M0 44 L200 92" stroke="#555" stroke-width="1.8"/><path d="M0 50 L200 98" stroke="#555" stroke-width="1.4"/>
      <g transform="rotate(13 100 86)"><path d="M100 66 V76" stroke="#555" stroke-width="3"/><circle cx="100" cy="66" r="3" fill="#888" stroke="#444" stroke-width="1"/>
      <rect x="78" y="76" width="44" height="30" rx="9" fill="#E8453C" stroke="${TA.OL}" stroke-width="2"/><rect x="84" y="81" width="32" height="11" rx="4" fill="#CFEAFF" stroke="${TA.OL}" stroke-width="1.4"/><path d="M78 98 H122" stroke="#B8302A" stroke-width="2"/></g>` + TA.face(100, 101, .9, "happy", "#fff");
  },
  liziba(){
    let win = ""; for(let y = 24; y < 134; y += 12) for(let x = 70; x < 146; x += 13){ if(y > 62 && y < 98) continue; win += `<rect x="${x}" y="${y}" width="8" height="7" rx="1.5" fill="#BFDDF2" stroke="#8E7A66" stroke-width="1"/>`; }
    return TA.sky("lzS", "#C8E6FF", "#F0F8FF") + TA.cloud(30, 22, .75) + TA.cloud(176, 30, .7)
      + `<rect y="132" width="200" height="18" fill="#9FD18A"/>
      <rect x="62" y="16" width="90" height="120" rx="4" fill="#F2DAB8" stroke="${TA.OL}" stroke-width="2"/>${win}
      <rect x="62" y="64" width="90" height="34" fill="#5B4C48" stroke="${TA.OL}" stroke-width="1.6"/>
      <rect y="96" width="200" height="6" fill="#B9B9C2" stroke="${TA.OL}" stroke-width="1.4"/><g fill="#C9C9D2" stroke="${TA.OL}" stroke-width="1.4"><rect x="16" y="102" width="8" height="30"/><rect x="40" y="102" width="8" height="30"/><rect x="170" y="102" width="8" height="30"/></g>
      <path d="M150 70 H196 Q202 70 202 76 V96 H150Z" fill="#fff" stroke="${TA.OL}" stroke-width="2"/><rect x="150" y="86" width="52" height="5" fill="#E8453C"/><g fill="#9FD0F0" stroke="${TA.OL}" stroke-width="1"><rect x="156" y="74" width="10" height="8" rx="2"/><rect x="170" y="74" width="10" height="8" rx="2"/><rect x="184" y="74" width="10" height="8" rx="2"/></g>
      <path d="M64 70 H22 Q8 70 6 84 L6 96 H64Z" fill="#fff" stroke="${TA.OL}" stroke-width="2"/><rect x="6" y="86" width="58" height="5" fill="#E8453C"/><path d="M10 74 Q14 72 24 72 L24 82 L8 82Z" fill="#9FD0F0" stroke="${TA.OL}" stroke-width="1"/><g fill="#9FD0F0" stroke="${TA.OL}" stroke-width="1"><rect x="30" y="74" width="10" height="8" rx="2"/><rect x="44" y="74" width="10" height="8" rx="2"/></g>` + TA.face(16, 90, .6, "happy")
      + `<g fill="#FFD66B" stroke="${TA.OL}" stroke-width="1"><circle cx="8" cy="92" r="1.6"/></g>`;
  },
  huoguo(){
    let chili = ""; [[66, 80], [80, 96], [58, 98], [92, 84], [72, 110]].forEach(([x, y], i) => chili += `<path d="M${x} ${y} q6 -2 9 3 q-5 3 -9 -3z" fill="#C61F1F" stroke="#7A1010" stroke-width="1" transform="rotate(${i * 40} ${x} ${y})"/>`);
    let pep = ""; [[70, 90], [86, 104], [62, 86], [96, 96]].forEach(([x, y]) => pep += `<circle cx="${x}" cy="${y}" r="1.6" fill="#5A2A1A"/>`);
    return TA.sky("hgS", "#FFE9D8", "#FFD9C2")
      + `<ellipse cx="100" cy="98" rx="84" ry="38" fill="#C9CDD6" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="100" cy="96" rx="74" ry="31" fill="#E44B2F"/>
      <path d="M100 65 Q130 78 100 96 Q70 112 104 127 Q160 122 174 96 Q166 72 100 65Z" fill="#F6EAD7"/><path d="M100 65 Q130 78 100 96 Q70 112 104 127" fill="none" stroke="#B9BEC9" stroke-width="4"/>`
      + chili + pep
      + `<g stroke="${TA.OL}" stroke-width="1.2"><circle cx="134" cy="88" r="5" fill="#E9D3B0"/><circle cx="148" cy="100" r="4" fill="#F2DDB8"/><circle cx="128" cy="106" r="2.5" fill="#E2453B"/><circle cx="140" cy="112" r="2.5" fill="#E2453B"/><path d="M152 84 q6 2 4 8" stroke="#6DBA4F" stroke-width="3" fill="none"/></g>
      <g fill="#fff" opacity=".7"><circle cx="76" cy="102" r="2"/><circle cx="90" cy="76" r="1.6"/><circle cx="64" cy="94" r="1.4"/></g>`
      + TA.face(80, 92, 1, "happy", "#7A1010") + TA.face(140, 98, .9, "smile")
      + TA.steam(80, 54) + TA.steam(126, 52)
      + `<path d="M150 30 L196 46" stroke="#8A5A36" stroke-width="4"/><path d="M152 22 L198 38" stroke="#8A5A36" stroke-width="4"/><path d="M178 34 q8 -6 14 2 q-6 8 -14 -2z" fill="#F4B9A6" stroke="${TA.OL}" stroke-width="1.2"/>`;
  },
  xiaomian(){
    let nd = ""; for(let i = 0; i < 6; i++) nd += `<path d="M${50 + i * 4} ${70 + i * 2} q12 -8 24 0 t24 0 t24 0" fill="none" stroke="#F4D27A" stroke-width="3"/>`;
    return TA.sky("xmS", "#FFF1E4", "#FFE2CF")
      + `<path d="M24 78 Q28 136 100 140 Q172 136 176 78Z" fill="#fff" stroke="${TA.OL}" stroke-width="2"/><path d="M30 98 Q100 112 170 98" fill="none" stroke="#5B8ED6" stroke-width="5"/><path d="M36 112 Q100 124 164 112" fill="none" stroke="#5B8ED6" stroke-width="2" stroke-dasharray="4 4"/>
      <ellipse cx="100" cy="78" rx="76" ry="18" fill="#D8452A" stroke="${TA.OL}" stroke-width="2"/>${nd}
      <path d="M128 70 q10 -10 22 -2 q-4 10 -22 2z" fill="#6DBA4F" stroke="#3F7F2F" stroke-width="1.2"/><path d="M118 76 q12 -6 20 4 q-10 6 -20 -4z" fill="#8FD068" stroke="#3F7F2F" stroke-width="1.2"/>
      <g fill="#E3B979" stroke="#9A6E3A" stroke-width=".8"><ellipse cx="64" cy="76" rx="3" ry="2"/><ellipse cx="72" cy="82" rx="3" ry="2"/><ellipse cx="58" cy="84" rx="3" ry="2"/><ellipse cx="96" cy="86" rx="3" ry="2"/></g>
      <g fill="#7FC95A"><circle cx="86" cy="74" r="1.6"/><circle cx="108" cy="82" r="1.6"/><circle cx="80" cy="86" r="1.6"/></g>`
      + TA.face(100, 120, 1.1, "happy") + TA.steam(78, 52) + TA.steam(112, 50, .8)
      + `<path d="M120 20 L70 70" stroke="#8A5A36" stroke-width="4"/><path d="M130 22 L82 72" stroke="#8A5A36" stroke-width="4"/>`;
  },
  /* ---------------- VÂN NAM ---------------- */
  shilin(){
    const st = (d, c) => `<path d="${d}" fill="${c}" stroke="#55556A" stroke-width="2"/>`;
    return TA.sky("slS", "#C6E6FF", "#F1F9FF") + TA.cloud(160, 24, .85) + TA.sun(32, 28, 10)
      + `<rect y="118" width="200" height="32" fill="#9BCF7E"/><ellipse cx="44" cy="138" rx="34" ry="8" fill="#8CCBDC" stroke="#5FA7B6" stroke-width="1.6"/>`
      + st("M8 124 L12 74 Q16 58 22 72 L26 66 Q30 60 32 70 L36 124Z", "#A3A3B8")
      + st("M36 124 L40 46 Q46 30 52 48 L58 124Z", "#B4B4C8")
      + st("M58 124 L64 64 Q70 52 74 66 L80 58 Q84 52 86 62 L90 124Z", "#9C9CB2")
      + st("M92 124 L98 34 Q106 18 112 36 L118 124Z", "#B8B8CC")
      + st("M120 124 L124 70 Q130 56 136 72 L140 124Z", "#A3A3B8")
      + st("M140 124 L146 50 Q152 38 158 52 L162 60 Q166 54 170 64 L174 124Z", "#ADADC2")
      + st("M174 124 L180 82 Q186 70 190 84 L196 124Z", "#9C9CB2")
      + `<g stroke="#7E7E96" stroke-width="1.4" fill="none"><path d="M46 60 L44 100 M104 48 L102 96 M152 66 L150 104 M70 80 L72 110"/></g>`
      + TA.face(105, 62, .95) + `<g fill="#6FB15A" stroke="#3F7F2F" stroke-width="1"><path d="M60 126 q4 -8 8 0z"/><path d="M128 128 q4 -8 8 0z"/><path d="M176 128 q4 -8 8 0z"/></g>`;
  },
  lijiang(){
    const house = (x, w, y, c) => `<rect x="${x}" y="${y}" width="${w}" height="${110 - y}" fill="${c}" stroke="${TA.OL}" stroke-width="1.6"/><rect x="${x + w / 2 - 5}" y="${y + 8}" width="10" height="9" rx="1.5" fill="#F9E3B4" stroke="${TA.OL}" stroke-width="1.2"/>` + TA.roof(x - 2, x + w + 2, y + 2, 10, "#5D6470", TA.OL, 8);
    let spokes = ""; for(let i = 0; i < 8; i++){ const a = i * Math.PI / 4; spokes += `<path d="M44 92 L${(44 + Math.cos(a) * 24).toFixed(1)} ${(92 + Math.sin(a) * 24).toFixed(1)}"/>`; }
    let pad = ""; for(let i = 0; i < 12; i++){ const a = i * Math.PI / 6; pad += `<rect x="${(44 + Math.cos(a) * 26 - 3).toFixed(1)}" y="${(92 + Math.sin(a) * 26 - 3).toFixed(1)}" width="6" height="6" rx="1" fill="#A97B4F" stroke="${TA.OL}" stroke-width="1" transform="rotate(${i * 30} ${(44 + Math.cos(a) * 26).toFixed(1)} ${(92 + Math.sin(a) * 26).toFixed(1)})"/>`; }
    return TA.sky("ljS", "#BCE0FF", "#F2FAFF")
      + `<path d="M70 70 L96 30 L106 42 L120 22 L136 48 L150 38 L176 70Z" fill="#C9D4E6" stroke="#8E9DB6" stroke-width="1.6"/><path d="M96 30 L102 40 L108 36 L106 42 L112 36 L120 22 L126 34 L132 40 L136 48 L128 44 L120 50 L112 44 L104 50 L98 42 L90 46Z" fill="#fff"/>`
      + house(74, 34, 70, "#C69A6A") + house(110, 40, 64, "#B88A5C") + house(152, 44, 72, "#C69A6A")
      + TA.lantern(92, 82, .7) + TA.lantern(130, 78, .7) + TA.lantern(174, 84, .7)
      + `<rect y="110" width="200" height="14" fill="#C9C1B4" stroke="${TA.OL}" stroke-width="1.4"/><path d="M8 117 h8 M24 117 h8 M40 117 h8 M120 117 h8 M136 117 h8 M152 117 h8 M168 117 h8" stroke="#ABA293" stroke-width="2"/>
      <rect y="124" width="200" height="26" fill="#86C3D6"/><path d="M80 134 q8 -4 16 0 t16 0 M140 142 q8 -4 16 0 t16 0" stroke="#C7E6EF" stroke-width="2" fill="none"/>
      <circle cx="44" cy="92" r="24" fill="none" stroke="#8B6340" stroke-width="4"/><g stroke="#8B6340" stroke-width="3">${spokes}</g>${pad}<circle cx="44" cy="92" r="5" fill="#A97B4F" stroke="${TA.OL}" stroke-width="1.4"/>`
      + TA.willow(196, 6, .8, true);
  },
  yulong(){
    return TA.sky("ylS", "#7FB8F0", "#DDF0FF") + TA.cloud(40, 30, .8) + TA.cloud(170, 46, .7)
      + `<path d="M0 116 L28 72 L42 84 L66 40 L80 56 L100 22 L116 50 L130 40 L148 68 L166 52 L200 96 L200 150 L0 150Z" fill="#8797B4" stroke="#5E6E8E" stroke-width="2"/>
      <path d="M66 40 L72 54 L78 50 L80 56 L86 46 L94 52 L100 22 L106 38 L112 44 L116 50 L122 44 L130 40 L136 52 L130 58 L120 54 L112 62 L104 52 L96 60 L88 56 L80 64 L74 58 L64 62Z" fill="#fff" stroke="#C6D2E6" stroke-width="1.2"/>
      <path d="M28 72 L34 82 L42 84 L36 88Z M148 68 L156 62 L166 52 L172 64 L160 70Z" fill="#fff"/>
      <path d="M0 122 Q60 104 120 120 Q160 130 200 114 L200 150 L0 150Z" fill="#8CCB6E" stroke="#5FA557" stroke-width="2"/>
      <g stroke="${TA.OL}" stroke-width="1"><circle cx="30" cy="136" r="3" fill="#F7D35C"/><circle cx="58" cy="130" r="3" fill="#F59BB5"/><circle cx="150" cy="138" r="3" fill="#F7D35C"/><circle cx="178" cy="128" r="3" fill="#FFFFFF"/><circle cx="110" cy="140" r="3" fill="#F59BB5"/></g>`
      + `<g transform="translate(120 112)"><ellipse cx="0" cy="8" rx="16" ry="10" fill="#4C3A30" stroke="${TA.OL}" stroke-width="1.6"/><circle cx="-14" cy="4" r="7" fill="#4C3A30" stroke="${TA.OL}" stroke-width="1.6"/><path d="M-19 -1 q-4 -4 -2 -7 M-10 -1 q3 -4 6 -4" stroke="#EADBC4" stroke-width="2" fill="none"/><path d="M-10 17 V21 M8 17 V21" stroke="${TA.OL}" stroke-width="3"/>${TA.face(-14, 5, .55, "happy", "#fff")}</g>`;
  },
  mixian(){
    return TA.sky("mxS", "#FFF6E3", "#FFE9C9")
      + `<path d="M30 70 Q34 130 100 134 Q166 130 170 70Z" fill="#fff" stroke="${TA.OL}" stroke-width="2"/><path d="M60 110 Q100 84 140 110" fill="none" stroke="#5B8ED6" stroke-width="3"/><path d="M64 110 V116 M80 101 V116 M100 97 V116 M120 101 V116 M136 110 V116" stroke="#5B8ED6" stroke-width="2"/>
      <ellipse cx="100" cy="70" rx="70" ry="16" fill="#F6CF6B" stroke="${TA.OL}" stroke-width="2"/><g fill="#FFE59A" opacity=".9"><ellipse cx="78" cy="68" rx="9" ry="3"/><ellipse cx="116" cy="72" rx="7" ry="2.5"/><ellipse cx="102" cy="64" rx="5" ry="2"/></g>`
      + TA.face(100, 120, 1)
      + `<g stroke="${TA.OL}" stroke-width="1.6"><ellipse cx="22" cy="132" rx="18" ry="7" fill="#fff"/><path d="M10 130 q6 -6 12 0 t12 0" stroke="#F4F0E4" stroke-width="3" fill="none"/>
      <ellipse cx="178" cy="132" rx="18" ry="7" fill="#fff"/><ellipse cx="172" cy="130" rx="6" ry="3" fill="#F7A3A3" stroke-width="1"/><ellipse cx="182" cy="128" rx="6" ry="3" fill="#F7B5B5" stroke-width="1"/>
      <ellipse cx="22" cy="40" rx="16" ry="6" fill="#fff"/><circle cx="18" cy="38" r="3" fill="#FFF7E6"/><circle cx="26" cy="38" r="3" fill="#FFF7E6"/>
      <ellipse cx="178" cy="40" rx="16" ry="6" fill="#fff"/><path d="M168 38 h18" stroke="#6DBA4F" stroke-width="3"/></g>`
      + TA.steam(86, 50) + TA.steam(118, 48, .8);
  },
  xianhuabing(){
    const rose = (x, y, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})"><circle r="8" fill="#F06A8E" stroke="#B53A5E" stroke-width="1.4"/><path d="M-4 -1 Q0 -6 4 -1 Q2 4 -2 2 Q-1 -1 1 0" fill="none" stroke="#B53A5E" stroke-width="1.3"/><path d="M-8 6 q-6 2 -8 -3 q6 -2 8 3z" fill="#6DBA4F" stroke="#3F7F2F" stroke-width="1"/></g>`;
    const cake = (x, y, mood) => `<ellipse cx="${x}" cy="${y + 6}" rx="24" ry="10" fill="#E9C27E" stroke="${TA.OL}" stroke-width="1.8"/><ellipse cx="${x}" cy="${y}" rx="24" ry="10" fill="#FFF3D8" stroke="${TA.OL}" stroke-width="1.8"/><path d="M${x - 16} ${y - 2} Q${x} ${y + 4} ${x + 16} ${y - 2}" fill="none" stroke="#EBD8B0" stroke-width="1.5"/><circle cx="${x}" cy="${y - 3}" r="3.4" fill="#E2453B"/>` + (mood ? TA.face(x, y + 2, .6, mood) : "");
    return TA.sky("xhS", "#FDE6F0", "#FFF4E6")
      + `<ellipse cx="100" cy="112" rx="88" ry="26" fill="#C99A68" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="100" cy="110" rx="80" ry="21" fill="#DDB383"/>`
      + cake(62, 98, "smile") + cake(110, 92, "") + cake(86, 116, "happy")
      + `<path d="M130 112 Q134 100 150 100 Q166 102 168 114 Q150 126 130 112Z" fill="#FFF3D8" stroke="${TA.OL}" stroke-width="1.8"/><path d="M140 110 Q150 104 160 112 Q150 118 140 110Z" fill="#E3557A" stroke="#B53A5E" stroke-width="1.2"/>`
      + rose(32, 36, 1.2) + rose(170, 30, 1) + rose(178, 74, .8) + rose(20, 82, .8)
      + `<g fill="#F59BB5" stroke="#C25B7C" stroke-width=".8"><ellipse cx="70" cy="40" rx="4" ry="2.4" transform="rotate(30 70 40)"/><ellipse cx="128" cy="50" rx="4" ry="2.4" transform="rotate(-20 128 50)"/><ellipse cx="100" cy="30" rx="4" ry="2.4"/><ellipse cx="150" cy="140" rx="4" ry="2.4"/></g>`;
  },
  /* ---------------- HÀNG CHÂU ---------------- */
  xihu(){
    let lot = ""; [[150, 128], [176, 136], [130, 140]].forEach(([x, y]) => lot += `<ellipse cx="${x}" cy="${y}" rx="11" ry="4" fill="#6DB36A" stroke="#3F7F45" stroke-width="1.3"/>`);
    return TA.sky("xhuS", "#CBE8FF", "#F5FBFF") + TA.cloud(80, 22, .8) + TA.sun(160, 26, 9)
      + `<path d="M0 82 Q30 56 60 72 Q90 50 124 70 Q150 58 176 70 Q190 76 200 72 L200 92 L0 92Z" fill="#A9CFB8" stroke="#86B29A" stroke-width="1.6"/>
      <path d="M40 92 Q70 70 104 86 Q140 74 200 88 L200 94 L40 94Z" fill="#89BFA0"/>
      <path d="M132 70 L132 56 M128 70 L136 70 M129 64 L135 64 M130 60 L134 60" stroke="#6E8A7C" stroke-width="2"/>
      <rect y="92" width="200" height="58" fill="#9BD3E2"/><path d="M0 92 H200" stroke="#6FB0C2" stroke-width="2"/>
      <g fill="#5F7C86" stroke="#3F5A64" stroke-width="1"><path d="M96 104 l3 -7 l3 7z"/><path d="M110 108 l3 -7 l3 7z"/><path d="M124 104 l3 -7 l3 7z"/></g>` + lot
      + `<circle cx="164" cy="132" r="4" fill="#F59BB5" stroke="#C25B7C" stroke-width="1.2"/>
      <path d="M58 122 Q84 132 112 122 L106 132 Q84 138 64 132Z" fill="#8B5E3C" stroke="${TA.OL}" stroke-width="1.8"/><path d="M70 122 Q84 108 100 122" fill="#3E3A44" stroke="${TA.OL}" stroke-width="1.6"/><path d="M112 122 L126 112" stroke="${TA.OL}" stroke-width="2"/>
      <path d="M40 140 q8 -4 16 0 t16 0 M120 120 q8 -4 16 0" stroke="#D2EEF5" stroke-width="2" fill="none"/>` + TA.willow(8, 2, 1.05);
  },
  leifeng(){
    let tiers = ""; const T = [[118, 40, 14], [102, 34, 13], [87, 28, 12], [73, 23, 11], [60, 18, 10]];
    T.forEach(([y, w, h]) => { tiers += `<rect x="${100 - w + 6}" y="${y - h}" width="${(w - 6) * 2}" height="${h}" fill="#D98B3A" stroke="${TA.OL}" stroke-width="1.6"/>`; for(let x = 100 - w + 12; x < 100 + w - 8; x += 8) tiers += `<rect x="${x}" y="${y - h + 3}" width="3" height="${h - 5}" rx="1" fill="#A85E22"/>`; tiers += TA.roof(100 - w, 100 + w, y - h + 2, 6, "#6B4A3A", TA.OL, 7); });
    return TA.sky("lfS", "#FFB98A", "#FFE6C8") + `<circle cx="150" cy="70" r="20" fill="#FFD45C" stroke="#F2A93B" stroke-width="2"/>` + TA.face(150, 72, 1.5, "happy") + TA.cloud(40, 26, .8)
      + `<path d="M30 128 Q60 108 100 112 Q140 108 170 128Z" fill="#5F8F58" stroke="#476F42" stroke-width="2"/>` + tiers
      + `<path d="M100 47 V30" stroke="${TA.OL}" stroke-width="2.4"/><circle cx="100" cy="36" r="3" fill="#F2B83A"/><circle cx="100" cy="29" r="2.2" fill="#F2B83A"/>
      <rect y="126" width="200" height="24" fill="#F6B88E"/><path d="M0 126 H200" stroke="#E79A6C" stroke-width="2"/><g opacity=".55"><rect x="90" y="128" width="20" height="3" rx="1.5" fill="#D98B3A"/><rect x="94" y="134" width="12" height="3" rx="1.5" fill="#D98B3A"/><rect x="140" y="130" width="22" height="3" rx="1.5" fill="#FFD45C"/></g>`;
  },
  duanqiao(){
    return TA.sky("dqS", "#D9E6F2", "#F6FAFD") + TA.flakes(30, 19, "#fff")
      + `<path d="M0 76 Q40 60 80 72 Q120 58 160 70 Q182 76 200 72 L200 88 L0 88Z" fill="#C7D6DE" stroke="#AFC1CB" stroke-width="1.5"/><path d="M0 76 Q40 60 80 72 Q120 58 160 70" fill="none" stroke="#fff" stroke-width="3"/>
      <rect y="88" width="200" height="62" fill="#A9CFDD"/>
      <path d="M8 112 Q100 52 192 112 L192 120 L170 120 Q100 74 30 120 L8 120Z" fill="#CFC6B8" stroke="${TA.OL}" stroke-width="2"/>
      <path d="M30 120 Q100 74 170 120" fill="#87B6C8" stroke="${TA.OL}" stroke-width="1.6"/><path d="M40 120 Q100 136 160 120" fill="none" stroke="#C9E1EA" stroke-width="2"/>
      <path d="M10 110 Q36 90 64 79" fill="none" stroke="#fff" stroke-width="5"/><path d="M136 79 Q164 90 190 110" fill="none" stroke="#fff" stroke-width="5"/>
      <g transform="translate(100 64)"><path d="M0 -14 Q-12 -14 -14 -4 Q0 -8 14 -4 Q12 -14 0 -14Z" fill="#E8453C" stroke="${TA.OL}" stroke-width="1.4"/><path d="M0 -14 V6" stroke="${TA.OL}" stroke-width="1.4"/><circle cx="-4" cy="2" r="4" fill="#FCE3D2" stroke="${TA.OL}" stroke-width="1.2"/><path d="M-9 14 Q-4 4 1 14Z" fill="#fff" stroke="${TA.OL}" stroke-width="1.2"/><circle cx="6" cy="3" r="4" fill="#FCE3D2" stroke="${TA.OL}" stroke-width="1.2"/><path d="M1 14 Q6 4 11 14Z" fill="#7FB8E6" stroke="${TA.OL}" stroke-width="1.2"/></g>`
      + TA.willow(198, 0, .9, true) + `<path d="M150 12 Q170 6 192 14" stroke="#fff" stroke-width="3" fill="none"/>`;
  },
  longjing(){
    let rows = ""; for(let i = 0; i < 5; i++) rows += `<path d="M-10 ${60 + i * 16} Q50 ${46 + i * 16} 100 ${58 + i * 16} T210 ${54 + i * 16}" fill="none" stroke="${i % 2 ? "#6FB55C" : "#86C773"}" stroke-width="12"/>`;
    let leaves = ""; [[86, 96, -20], [96, 88, 6], [106, 100, 18], [112, 86, -8], [92, 110, 10], [102, 112, -14]].forEach(([x, y, r]) => leaves += `<ellipse cx="${x}" cy="${y}" rx="3" ry="9" fill="#7CC264" stroke="#3F7F2F" stroke-width="1" transform="rotate(${r} ${x} ${y})"/>`);
    return TA.sky("lgS", "#D8F0FF", "#F3FBEF") + TA.cloud(40, 22, .8) + rows
      + `<path d="M68 64 L74 136 Q100 144 126 136 L132 64" fill="#E9F7FF" fill-opacity=".85" stroke="#7FA8C2" stroke-width="2"/><path d="M71 84 L75 134 Q100 142 125 134 L129 84Z" fill="#D9EF9F" opacity=".85"/>${leaves}
      <ellipse cx="100" cy="64" rx="32" ry="7" fill="#F3FBFF" stroke="#7FA8C2" stroke-width="2"/><path d="M76 74 L78 122" stroke="#fff" stroke-width="3" opacity=".8"/>`
      + TA.face(100, 124, .9, "happy", "#3F6F2F") + TA.steam(92, 52, .8)
      + `<g transform="translate(160 118)"><ellipse cx="0" cy="0" rx="9" ry="16" fill="#86C773" stroke="#3F7F2F" stroke-width="1.6" transform="rotate(30)"/><path d="M-6 12 L6 -12" stroke="#3F7F2F" stroke-width="1.4" transform="rotate(0)"/>${TA.face(0, 0, .55, "smile", "#2F5F22")}</g>`;
  },
  dongpo(){
    const cube = (x, y, mood) => `<path d="M${x - 15} ${y - 10} Q${x - 16} ${y - 18} ${x - 6} ${y - 18} L${x + 10} ${y - 18} Q${x + 17} ${y - 18} ${x + 16} ${y - 10} L${x + 16} ${y + 8} Q${x + 16} ${y + 14} ${x + 8} ${y + 14} L${x - 8} ${y + 14} Q${x - 15} ${y + 14} ${x - 15} ${y + 8}Z" fill="#B4482E" stroke="${TA.OL}" stroke-width="1.8"/><path d="M${x - 15} ${y - 4} H${x + 16} M${x - 15} ${y + 3} H${x + 16}" stroke="#F3D4B8" stroke-width="2.4"/><path d="M${x - 15} ${y - 4} H${x + 16}" stroke="#E89A72" stroke-width="1"/><path d="M${x - 2} ${y - 18} V${y + 14} M${x - 15} ${y - 12} H${x + 16}" stroke="#D9C49E" stroke-width="1.6"/><ellipse cx="${x - 6}" cy="${y - 14}" rx="5" ry="1.6" fill="#fff" opacity=".5"/>` + TA.face(x, y + 8, .55, mood, "#fff");
    return TA.sky("dpS", "#FFF0E0", "#FFDFC6")
      + `<path d="M30 84 Q32 138 100 140 Q168 138 170 84Z" fill="#9C5B3A" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="100" cy="84" rx="70" ry="18" fill="#7A3A22" stroke="${TA.OL}" stroke-width="2"/><ellipse cx="100" cy="84" rx="62" ry="13" fill="#8E3E22"/>`
      + cube(78, 82, "happy") + cube(118, 80, "smile") + cube(98, 96, "happy")
      + `<path d="M138 98 q14 -12 26 -2 q-8 12 -26 2z" fill="#6DBA4F" stroke="#3F7F2F" stroke-width="1.2"/><path d="M40 98 q-10 -14 6 -18 q8 10 -6 18z" fill="#8FD068" stroke="#3F7F2F" stroke-width="1.2"/>
      <path d="M140 30 Q168 22 186 40 L176 56 Q158 46 140 48Z" fill="#9C5B3A" stroke="${TA.OL}" stroke-width="1.8"/><circle cx="164" cy="36" r="4" fill="#7A3A22" stroke="${TA.OL}" stroke-width="1.2"/>`
      + TA.steam(86, 56) + TA.steam(116, 54, .8);
  }
};

/* Hướng dẫn viên chibi 小语导游 – expr: smile | happy | think */
function guideSVG(expr = "smile", cls = ""){
  const eyes = expr === "happy"
    ? `<path d="M46 72 q5 -6 10 0 M70 72 q5 -6 10 0" stroke="#2E2321" stroke-width="2.6" fill="none" stroke-linecap="round"/>`
    : `<ellipse cx="51" cy="72" rx="5.4" ry="6.6" fill="#2E2321"/><ellipse cx="75" cy="72" rx="5.4" ry="6.6" fill="#2E2321"/><circle cx="53" cy="69.5" r="2" fill="#fff"/><circle cx="77" cy="69.5" r="2" fill="#fff"/><circle cx="49.5" cy="75" r="1" fill="#fff"/><circle cx="73.5" cy="75" r="1" fill="#fff"/>`;
  const mouth = expr === "happy" ? `<path d="M56 84 Q63 94 70 84 Z" fill="#C2524A" stroke="#8E3530" stroke-width="1.4" stroke-linejoin="round"/>`
    : expr === "think" ? `<path d="M58 87 q5 -3 10 0" stroke="#8E3530" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M92 48 q5 8 0 11 q-5 -3 0 -11z" fill="#9FD3F5" stroke="#5D9CC8" stroke-width="1.2"/>`
    : `<path d="M57 85 Q63 90 69 85" stroke="#8E3530" stroke-width="2.2" fill="none" stroke-linecap="round"/>`;
  const arm = expr === "think"
    ? `<path d="M84 116 Q96 108 90 94" stroke="#2F9E8F" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="89" cy="92" r="5" fill="#FCE3D2" stroke="#5A4034" stroke-width="1.2"/>`
    : `<path d="M86 114 Q100 104 104 90" stroke="#2F9E8F" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="104" cy="88" r="5" fill="#FCE3D2" stroke="#5A4034" stroke-width="1.2"/><path d="M106 92 L112 34" stroke="#8A5A36" stroke-width="3" stroke-linecap="round"/><path d="M112 34 L134 42 L111 52Z" fill="#E8453C" stroke="#A8302A" stroke-width="1.6" stroke-linejoin="round"/><text x="119" y="46" font-size="7.5" fill="#FFE27A" font-weight="700" text-anchor="middle">游</text>`;
  return `<svg class="tp-guide-svg ${cls}" viewBox="0 0 140 170" aria-hidden="true">
    <ellipse cx="64" cy="164" rx="34" ry="5" fill="#000" opacity=".08"/>
    <path d="M24 74 Q18 108 30 118 L38 104Z M102 74 Q108 108 96 118 L88 104Z" fill="#4A3020"/>
    <path d="M40 112 Q40 100 63 98 Q86 100 86 112 L90 148 L36 148Z" fill="#fff" stroke="#5A4034" stroke-width="1.6" stroke-linejoin="round"/>
    <path d="M40 112 Q40 100 52 99 L56 148 L36 148Z M86 112 Q86 100 74 99 L70 148 L90 148Z" fill="#2F9E8F" stroke="#5A4034" stroke-width="1.6" stroke-linejoin="round"/>
    <path d="M56 100 L63 120 L70 100" fill="none" stroke="#E8453C" stroke-width="2"/><rect x="58" y="120" width="10" height="13" rx="2" fill="#FFE27A" stroke="#5A4034" stroke-width="1.2"/>
    <rect x="44" y="146" width="14" height="12" rx="4" fill="#3E5C52"/><rect x="68" y="146" width="14" height="12" rx="4" fill="#3E5C52"/>
    <path d="M40 116 Q28 126 32 140" stroke="#2F9E8F" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="32" cy="141" r="5" fill="#FCE3D2" stroke="#5A4034" stroke-width="1.2"/>
    ${arm}
    <ellipse cx="63" cy="70" rx="36" ry="33" fill="#FCE3D2" stroke="#5A4034" stroke-width="1.6"/>
    <path d="M27 70 Q26 44 46 38 Q63 50 80 40 Q100 46 99 70 Q94 56 82 52 Q70 60 56 56 Q40 58 27 70Z" fill="#4A3020"/>
    <path d="M22 46 Q26 22 63 20 Q100 22 104 46 Q63 38 22 46Z" fill="#F2B83A" stroke="#5A4034" stroke-width="1.6" stroke-linejoin="round"/>
    <path d="M18 48 Q63 36 108 48 Q112 54 104 54 Q63 44 22 54 Q14 54 18 48Z" fill="#F7CE5B" stroke="#5A4034" stroke-width="1.6" stroke-linejoin="round"/>
    <circle cx="63" cy="30" r="6" fill="#E8453C" stroke="#5A4034" stroke-width="1.2"/><text x="63" y="33" font-size="7" fill="#fff" font-weight="700" text-anchor="middle">导</text>
    ${eyes}
    <ellipse cx="42" cy="82" rx="6" ry="3.4" fill="#F6A9A9" opacity=".75"/><ellipse cx="84" cy="82" rx="6" ry="3.4" fill="#F6A9A9" opacity=".75"/>
    ${mouth}
  </svg>`;
}

/* Bản đồ Trung Quốc chibi (viewBox 0 0 400 320) */
function chinaMapSVG(){
  const P = "394,58 369,98 340,108 326,122 313,118 307,130 289,130 285,138 295,146 317,146 301,158 307,186 313,202 301,226 289,246 270,262 245,274 232,269 220,262 190,266 176,270 165,250 162,218 128,218 103,222 78,214 54,198 48,182 42,158 19,142 13,126 22,118 53,102 69,82 84,66 96,50 115,62 146,90 177,102 208,110 239,102 252,86 277,78 295,62 298,46 307,18 326,18 338,34 351,46 369,62";
  let mts = ""; [[70, 170], [96, 186], [120, 176], [60, 140], [150, 200]].forEach(([x, y]) => mts += `<path d="M${x - 12} ${y + 8} L${x} ${y - 8} L${x + 12} ${y + 8}Z" fill="#B9D7A8" stroke="#8FB57E" stroke-width="1.6" stroke-linejoin="round"/><path d="M${x - 4} ${y - 2} L${x} ${y - 8} L${x + 4} ${y - 2}Z" fill="#fff"/>`);
  let waves = ""; [[352, 170], [366, 220], [340, 270], [372, 140]].forEach(([x, y]) => waves += `<path d="M${x} ${y} q6 -5 12 0 t12 0" fill="none" stroke="#A9D4EE" stroke-width="2.4" stroke-linecap="round"/>`);
  return `<svg class="tp-map-svg" viewBox="0 0 400 320" role="img" aria-label="Bản đồ Trung Quốc">
    <defs><linearGradient id="tpSea" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E6F5FF"/><stop offset="1" stop-color="#CFEAFB"/></linearGradient></defs>
    <rect width="400" height="320" rx="22" fill="url(#tpSea)"/>${waves}
    <polygon points="${P}" transform="translate(4 6)" fill="#9CC79A" opacity=".45"/>
    <polygon points="${P}" fill="#E5F4D6" stroke="#9CC79A" stroke-width="7" stroke-linejoin="round"/>
    <polygon points="${P}" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="1 7" stroke-linecap="round" opacity=".9"/>
    <ellipse cx="245" cy="290" rx="9" ry="6" fill="#E5F4D6" stroke="#9CC79A" stroke-width="4"/><ellipse cx="310" cy="252" rx="5" ry="11" fill="#E5F4D6" stroke="#9CC79A" stroke-width="4"/>
    ${mts}
    <path d="M60 230 Q70 222 82 230" stroke="#C9B48A" stroke-width="2" fill="none"/>
    <g transform="translate(150 150)"><circle r="11" fill="#fff" stroke="#3B3B3B" stroke-width="1.6"/><circle cx="-8" cy="-8" r="4.5" fill="#3B3B3B"/><circle cx="8" cy="-8" r="4.5" fill="#3B3B3B"/><ellipse cx="-4" cy="0" rx="3" ry="3.6" fill="#3B3B3B"/><ellipse cx="4" cy="0" rx="3" ry="3.6" fill="#3B3B3B"/><circle cx="-3.4" cy="-.6" r="1" fill="#fff"/><circle cx="4.6" cy="-.6" r="1" fill="#fff"/><ellipse cx="0" cy="5" rx="1.8" ry="1.2" fill="#3B3B3B"/></g>
    <path d="M279 123 Q330 140 311 192 Q300 200 303 200 Q250 190 218 205 Q200 222 194 242" fill="none" stroke="#E8453C" stroke-width="2.4" stroke-dasharray="2 6" stroke-linecap="round" opacity=".75"/>
    <g transform="translate(240 160) rotate(-20)"><path d="M-12 0 L10 0 Q16 0 16 3 Q16 5 10 5 L-12 5Z" fill="#fff" stroke="#5A4034" stroke-width="1.4"/><path d="M-2 0 L4 -10 L8 -10 L6 0Z M-2 5 L4 13 L8 13 L6 5Z M-12 0 L-15 -6 L-11 -6 L-8 0Z" fill="#7FB8E6" stroke="#5A4034" stroke-width="1.2" stroke-linejoin="round"/></g>
    <g id="tpPins"></g>
  </svg>`;
}
