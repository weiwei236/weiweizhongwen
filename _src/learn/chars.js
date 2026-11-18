/* ======================= NHÂN VẬT CHÍNH · 主要人物 (Giáo trình HSK 3.0) =======================
   Sơ đồ quan hệ nhân vật: bấm vào nhân vật để xem giới thiệu Trung – Việt; bật/tắt phiên âm & tiếng Việt.
   Ảnh: _src/trip/gd/ch_*.webp (TRIP_GD.ch_*) */
const CH_PEOPLE = {
  xiaoyu: { zh: "AI小语", py: "AI Xiǎoyǔ", vi: "AI Tiểu Ngữ", role: "Trợ giảng AI",
    d: "新教程智慧导学助教。", dpy: "Xīn jiàochéng zhìhuì dǎoxué zhùjiào.", dvi: "Trợ giảng thông minh của “Giáo trình New HSK”." },
  yifei: { zh: "王一飞", py: "Wáng Yīfēi", vi: "Vương Nhất Phi", x: 235, y: 190, role: "Cô giáo",
    d: "女，北京人，30岁左右，中国派驻海外某国某高校的中文教师。", dpy: "Nǚ, Běijīng rén, sānshí suì zuǒyòu, Zhōngguó pàizhù hǎiwài mǒu guó mǒu gāoxiào de Zhōngwén jiàoshī.",
    dvi: "Nữ, người Bắc Kinh, khoảng 30 tuổi, giảng viên tiếng Trung Quốc của một trường đại học ở nước ngoài do Trung Quốc cử sang." },
  jiayue: { zh: "白家月", py: "Bái Jiāyuè", vi: "Bạch Gia Nguyệt", x: 95, y: 405, role: "Sinh viên",
    d: "女，法国人，20多岁，某国某高校大学生，在王一飞班里学中文。", dpy: "Nǚ, Fǎguó rén, èrshí duō suì, mǒu guó mǒu gāoxiào dàxuéshēng, zài Wáng Yīfēi bān li xué Zhōngwén.",
    dvi: "Nữ, người Pháp, hơn 20 tuổi, sinh viên của một trường đại học ở nước ngoài, học tiếng Trung Quốc trong lớp của Vương Nhất Phi." },
  anni: { zh: "安妮", py: "Ānnī", vi: "Annie", x: 235, y: 405, role: "Sinh viên",
    d: "女，加拿大人，20多岁，某国某高校大学生，在王一飞班里学中文。", dpy: "Nǚ, Jiānádà rén, èrshí duō suì, mǒu guó mǒu gāoxiào dàxuéshēng, zài Wáng Yīfēi bān li xué Zhōngwén.",
    dvi: "Nữ, người Canada, hơn 20 tuổi, sinh viên của một trường đại học ở nước ngoài, học tiếng Trung Quốc trong lớp của Vương Nhất Phi." },
  tianzhong: { zh: "陈天中", py: "Chén Tiānzhōng", vi: "Trần Thiên Trung", x: 375, y: 405, role: "Sinh viên",
    d: "男，泰国人，20多岁，某国某高校大学生，在王一飞班里学中文。", dpy: "Nán, Tàiguó rén, èrshí duō suì, mǒu guó mǒu gāoxiào dàxuéshēng, zài Wáng Yīfēi bān li xué Zhōngwén.",
    dvi: "Nam, người Thái Lan, hơn 20 tuổi, sinh viên của một trường đại học ở nước ngoài, học tiếng Trung Quốc trong lớp của Vương Nhất Phi." },
  liwen: { zh: "李文", py: "Lǐ Wén", vi: "Lý Văn", x: 235, y: 655, role: "Du học sinh ngành y",
    d: "男，北京人，20多岁，某国某高校中国留学生，学医。与白家月、安妮和陈天中在同一所学校，和他们是好朋友。",
    dpy: "Nán, Běijīng rén, èrshí duō suì, mǒu guó mǒu gāoxiào Zhōngguó liúxuéshēng, xué yī. Yǔ Bái Jiāyuè, Ānnī hé Chén Tiānzhōng zài tóng yì suǒ xuéxiào, hé tāmen shì hǎo péngyou.",
    dvi: "Nam, người Bắc Kinh, hơn 20 tuổi, là lưu học sinh Trung Quốc tại một trường đại học ở nước ngoài, chuyên ngành y học. Lý Văn học cùng trường và là bạn thân của Bạch Gia Nguyệt, Annie và Trần Thiên Trung." },
  yixue: { zh: "王一雪", py: "Wáng Yīxuě", vi: "Vương Nhất Tuyết", x: 625, y: 190, role: "Nhân viên văn phòng",
    d: "女，北京人，30多岁，某跨国公司北京分公司办公室工作人员，王一飞的堂姐。", dpy: "Nǚ, Běijīng rén, sānshí duō suì, mǒu kuàguó gōngsī Běijīng fēn gōngsī bàngōngshì gōngzuò rényuán, Wáng Yīfēi de tángjiě.",
    dvi: "Nữ, người Bắc Kinh, hơn 30 tuổi, nhân viên văn phòng tại chi nhánh Bắc Kinh của một công ty xuyên quốc gia, chị họ của Vương Nhất Phi." },
  liuming: { zh: "刘明", py: "Liú Míng", vi: "Lưu Minh", x: 855, y: 190, role: "Bác sĩ",
    d: "男，北京人，40岁左右，医生，王一雪的丈夫。", dpy: "Nán, Běijīng rén, sìshí suì zuǒyòu, yīshēng, Wáng Yīxuě de zhàngfu.",
    dvi: "Nam, người Bắc Kinh, khoảng 40 tuổi, bác sĩ, chồng của Vương Nhất Tuyết." },
  xiaoxue: { zh: "刘小雪", py: "Liú Xiǎoxuě", vi: "Lưu Tiểu Tuyết", x: 760, y: 405, role: "Học sinh tiểu học",
    d: "女，北京人，12岁，小学生，刘明和王一雪的女儿。", dpy: "Nǚ, Běijīng rén, shí'èr suì, xiǎoxuéshēng, Liú Míng hé Wáng Yīxuě de nǚ'ér.",
    dvi: "Nữ, người Bắc Kinh, 12 tuổi, học sinh tiểu học, con gái của Lưu Minh và Vương Nhất Tuyết." },
  xiaoming: { zh: "刘小明", py: "Liú Xiǎomíng", vi: "Lưu Tiểu Minh", x: 900, y: 405, role: "Học sinh mẫu giáo",
    d: "男，北京人，5岁，幼儿园学生，刘明和王一雪的儿子。", dpy: "Nán, Běijīng rén, wǔ suì, yòu'éryuán xuésheng, Liú Míng hé Wáng Yīxuě de érzi.",
    dvi: "Nam, người Bắc Kinh, 5 tuổi, học sinh mẫu giáo, con trai của Lưu Minh và Vương Nhất Tuyết." },
  tongle: { zh: "杨同乐", py: "Yáng Tónglè", vi: "Dương Đồng Lạc", x: 590, y: 560, role: "Nhân viên công ty",
    d: "男，上海人，30多岁，王一雪的同事。", dpy: "Nán, Shànghǎi rén, sānshí duō suì, Wáng Yīxuě de tóngshì.",
    dvi: "Nam, người Thượng Hải, hơn 30 tuổi, đồng nghiệp của Vương Nhất Tuyết." },
};
/* loại quan hệ: màu + tên trong chú giải */
const CH_KIND = {
  fam: ["#2E8B57", "家人", "jiārén", "Gia đình"], school: ["#2F6FD6", "师生", "shīshēng", "Cô giáo – học trò"],
  friend: ["#D9822B", "朋友", "péngyou", "Bạn bè"], love: ["#E0527A", "恋人", "liànrén", "Tình cảm"], work: ["#7A4FC4", "同事", "tóngshì", "Đồng nghiệp"],
};
/* quan hệ: [từ, đến, loại, chữ Hán, phiên âm, tiếng Việt, mô tả trong thẻ] */
const CH_LINKS = [
  ["yifei", "jiayue", "school", "", "", "", "Cô giáo dạy tiếng Trung của Bạch Gia Nguyệt"],
  ["yifei", "anni", "school", "师生", "shīshēng", "Cô – trò", "Cô giáo dạy tiếng Trung của Annie"],
  ["yifei", "tianzhong", "school", "", "", "", "Cô giáo dạy tiếng Trung của Trần Thiên Trung"],
  ["liwen", "jiayue", "love", "恋人", "liànrén", "Người yêu", "Bạch Gia Nguyệt và Lý Văn có mối quan hệ tình cảm"],
  ["liwen", "anni", "friend", "好朋友", "hǎo péngyou", "Bạn thân", "Lý Văn là bạn thân của Annie (học cùng trường)"],
  ["liwen", "tianzhong", "friend", "", "", "", "Lý Văn là bạn thân của Trần Thiên Trung (học cùng trường)"],
  ["jiayue", "anni", "friend", "同学", "tóngxué", "Bạn cùng lớp", "Bạch Gia Nguyệt và Annie học cùng lớp"],
  ["anni", "tianzhong", "friend", "同学", "tóngxué", "Bạn cùng lớp", "Annie và Trần Thiên Trung học cùng lớp"],
  ["yifei", "yixue", "fam", "堂姐妹", "tángjiěmèi", "Chị em họ thân thiết", "Vương Nhất Phi và Vương Nhất Tuyết là chị em họ thân thiết (Nhất Tuyết là chị)"],
  ["yixue", "liuming", "fam", "夫妻", "fūqī", "Vợ chồng", "Vương Nhất Tuyết và Lưu Minh là vợ chồng"],
  ["yixue", "tongle", "work", "同事", "tóngshì", "Đồng nghiệp", "Dương Đồng Lạc là đồng nghiệp của Vương Nhất Tuyết"],
];
const Chars = {
  sel: null,
  py: store.get("ww_ch_py", true), vi: store.get("ww_ch_vi", true),
  open(){ showScreen("scrChars"); this.sel = null; this.render(); window.scrollTo(0, 0); },
  img(k){ const G = typeof TRIP_GD !== "undefined" ? TRIP_GD : {}; return G["ch_" + k] || ""; },
  pill(x, y, zh, py, vi, col){
    const w = Math.max(zh.length * 15 + 16, this.vi ? vi.length * 6.4 + 14 : 0, this.py ? py.length * 6 + 14 : 0);
    const h = 22 + (this.py ? 13 : 0) + (this.vi ? 14 : 0); let ty = y - h / 2 + 17;
    let s = `<g class="ch-pill"><rect x="${x - w / 2}" y="${y - h / 2}" width="${w}" height="${h}" rx="10" fill="#fff" stroke="${col}" stroke-width="2"/>`;
    s += `<text x="${x}" y="${ty}" class="ch-lz" fill="${col}">${zh}</text>`;
    if(this.py){ ty += 13; s += `<text x="${x}" y="${ty}" class="ch-lp">${py}</text>`; }
    if(this.vi){ ty += 14; s += `<text x="${x}" y="${ty}" class="ch-lv">${esc(vi)}</text>`; }
    return s + "</g>";
  },
  node(k){
    const p = CH_PEOPLE[k], r = 46; let ty = p.y + r + 24;
    let s = `<g class="ch-node" data-k="${k}" tabindex="0" role="button" aria-label="${esc(p.vi)}">
      <circle cx="${p.x}" cy="${p.y}" r="${r + 6}" fill="#fff" class="ch-ring"/>
      <clipPath id="chc_${k}"><circle cx="${p.x}" cy="${p.y}" r="${r}"/></clipPath>
      <image href="${this.img(k)}" x="${p.x - r}" y="${p.y - r}" width="${r * 2}" height="${r * 2}" clip-path="url(#chc_${k})" preserveAspectRatio="xMidYMid slice"/>
      <circle cx="${p.x}" cy="${p.y}" r="${r + 3}" fill="none" stroke="#3E9B5A" stroke-width="6"/>
      <text x="${p.x}" y="${ty}" class="ch-nz">${p.zh}</text>`;
    if(this.py){ ty += 16; s += `<text x="${p.x}" y="${ty}" class="ch-np">${p.py}</text>`; }
    if(this.vi){ ty += 17; s += `<text x="${p.x}" y="${ty}" class="ch-nv">${esc(p.vi)}</text>`; }
    return s + "</g>";
  },
  svg(){
    const P = CH_PEOPLE, L = [];
    const line = (a, b, col, dash, w = 4) => `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="${col}" stroke-width="${w}" stroke-linecap="round" ${dash ? `stroke-dasharray="${dash}"` : ""}/>`;
    // khung hai bối cảnh
    L.push(`<rect x="8" y="58" width="452" height="742" rx="26" class="ch-zone"/><rect x="500" y="58" width="452" height="742" rx="26" class="ch-zone cn"/>`);
    L.push(`<text x="234" y="94" class="ch-zt">海外场景</text><text x="726" y="94" class="ch-zt">中国国内场景</text>`);
    if(this.vi) L.push(`<text x="234" y="116" class="ch-zv">Bối cảnh tại nước ngoài</text><text x="726" y="116" class="ch-zv">Bối cảnh tại Trung Quốc</text>`);
    // đường nối (nối từ dưới khối tên → đỉnh vòng tròn để không đè lên chữ)
    const K = CH_KIND, bot = k => ({ x: P[k].x, y: P[k].y + 52 + (this.py ? 16 : 0) + (this.vi ? 17 : 0) + 34 }), top = k => ({ x: P[k].x, y: P[k].y - 54 });
    const ybar = 345, yb = bot("yifei").y;
    L.push(`<path d="M${P.yifei.x} ${yb} V${ybar} M${P.jiayue.x} ${ybar} H${P.tianzhong.x} M${P.jiayue.x} ${ybar} V${top("jiayue").y} M${P.anni.x} ${ybar} V${top("anni").y} M${P.tianzhong.x} ${ybar} V${top("tianzhong").y}" stroke="${K.school[0]}" stroke-width="4" fill="none" stroke-linecap="round"/>`);
    L.push(line(P.jiayue, P.anni, K.friend[0], "3 9", 3), line(P.anni, P.tianzhong, K.friend[0], "3 9", 3));
    L.push(line(top("liwen"), bot("anni"), K.friend[0], "10 8"), line(top("liwen"), bot("tianzhong"), K.friend[0], "10 8"));
    L.push(line(top("liwen"), bot("jiayue"), K.love[0], "", 5));
    L.push(line(P.yifei, P.yixue, K.fam[0], "14 8", 5));
    L.push(line(P.yixue, P.liuming, K.fam[0], "", 5));
    L.push(line(bot("yixue"), top("tongle"), K.work[0], "10 8"));
    const mx = (P.yixue.x + P.liuming.x) / 2, by = 330;
    L.push(`<path d="M${mx} ${P.yixue.y} V${by} M${P.xiaoxue.x} ${by} H${P.xiaoming.x} M${P.xiaoxue.x} ${by} V${top("xiaoxue").y} M${P.xiaoming.x} ${by} V${top("xiaoming").y}" stroke="${K.fam[0]}" stroke-width="4" fill="none" stroke-linecap="round"/>`);
    Object.keys(P).filter(k => k !== "xiaoyu").forEach(k => L.push(this.node(k)));
    // nhãn quan hệ
    const mid = (a, b, t = .5) => [a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t];
    const lab = (a, b, t, kind, zh, py, vi) => { const [x, y] = mid(a, b, t); return this.pill(x, y, zh, py, vi, K[kind][0]); };
    L.push(this.pill(P.yifei.x, (yb + ybar) / 2 + 2, "师生", "shīshēng", "Cô giáo – học trò", K.school[0]));
    L.push(lab(bot("jiayue"), top("liwen"), .5, "love", "❤ 恋人", "liànrén", "Người yêu"));
    L.push(lab(bot("tianzhong"), top("liwen"), .5, "friend", "好朋友", "hǎo péngyou", "Bạn thân"));
    L.push(lab(P.yifei, P.yixue, .5, "fam", "堂姐妹", "tángjiěmèi", "Chị em họ thân thiết"));
    L.push(lab(P.yixue, P.liuming, .5, "fam", "夫妻", "fūqī", "Vợ chồng"));
    L.push(this.pill(mx, by - 2, "子女", "zǐnǚ", "Con gái · con trai", K.fam[0]));
    L.push(lab(bot("yixue"), top("tongle"), .5, "work", "同事", "tóngshì", "Đồng nghiệp"));
    // chú giải màu
    const lg = Object.values(K); let ly = 600;
    L.push(`<g class="ch-legend"><text x="720" y="${ly - 26}" class="ch-lgt">${this.vi ? "Chú giải" : "图例"}</text>`);
    lg.forEach(([c, zh, py, vi], i) => { const x = 720, y = ly + i * 30;
      L.push(`<line x1="${x}" y1="${y}" x2="${x + 34}" y2="${y}" stroke="${c}" stroke-width="5" stroke-linecap="round"/><text x="${x + 44}" y="${y + 5}" class="ch-lgi"><tspan class="han">${zh}</tspan>${this.vi ? ` · ${vi}` : this.py ? ` ${py}` : ""}</text>`); });
    L.push(`</g>`);
    return `<svg class="ch-svg" viewBox="0 48 960 762" role="img" aria-label="Sơ đồ quan hệ nhân vật">${L.join("")}</svg>`;
  },
  render(){
    const X = CH_PEOPLE.xiaoyu;
    const tg = (id, on, t) => `<button class="ch-tg ${on ? "on" : ""}" id="${id}" aria-pressed="${on}">${t}</button>`;
    let h = `<div class="ch-top"><div><h2><span class="han">主要人物</span> · Nhân vật chính</h2><p class="muted">Các nhân vật xuất hiện xuyên suốt Giáo trình HSK 3.0 – bấm vào từng người để xem giới thiệu.</p></div>
      <div class="ch-acts">${tg("chPy", this.py, "Phiên âm")}${tg("chVi", this.vi, "Tiếng Việt")}<button class="btn" id="chBack">${ICON.left}Về trang học</button></div></div>
      <button class="ch-guide" data-k="xiaoyu"><img src="${this.img("xiaoyu")}" alt=""><span><b class="han">${X.zh}</b>${this.py ? `<small>${X.py}</small>` : ""}${this.vi ? `<em>${X.vi} – ${X.role}</em>` : ""}
        <span class="han ch-gd">${X.d}</span>${this.py ? `<small>${X.dpy}</small>` : ""}${this.vi ? `<span class="ch-gv">${X.dvi}</span>` : ""}</span></button>
      <p class="ch-swipe">👉 Vuốt ngang để xem cả sơ đồ</p><div class="ch-wrap">${this.svg()}</div>`;
    if(this.sel) h += this.card(this.sel);
    $("#chBody").innerHTML = h; this.bind();
  },
  card(k){
    const p = CH_PEOPLE[k];
    const rel = CH_LINKS.filter(l => l[0] === k || l[1] === k).map(l => { const o = CH_PEOPLE[l[0] === k ? l[1] : l[0]], c = CH_KIND[l[2]][0];
      return `<li><i style="background:${c}"></i><b class="han">${o.zh}</b>${this.py ? ` <small>${o.py}</small>` : ""}${this.vi ? ` – ${esc(l[6])}` : ` – <span class="han">${CH_KIND[l[2]][1]}</span>`}</li>`; });
    if(k === "liuming" || k === "yixue") rel.push(`<li><i style="background:${CH_KIND.fam[0]}"></i><b class="han">刘小雪、刘小明</b>${this.vi ? " – con gái và con trai" : ""}</li>`);
    if(k === "xiaoxue" || k === "xiaoming") rel.push(`<li><i style="background:${CH_KIND.fam[0]}"></i><b class="han">刘明、王一雪</b>${this.vi ? " – bố và mẹ" : ""}</li>`, `<li><i style="background:${CH_KIND.fam[0]}"></i><b class="han">${k === "xiaoxue" ? "刘小明" : "刘小雪"}</b>${this.vi ? (k === "xiaoxue" ? " – em trai" : " – chị gái") : ""}</li>`);
    return `<div class="ch-ov" id="chOv"><div class="ch-card" role="dialog" aria-label="${esc(p.vi)}">
      <button class="ch-x" id="chX" aria-label="Đóng">✕</button>
      <div class="ch-ch"><img src="${this.img(k)}" alt=""><div><b class="han">${p.zh}</b> <button class="say" data-say="${p.zh}" aria-label="Nghe">${ICON.sound}</button>${this.py ? `<small>${p.py}</small>` : ""}${this.vi ? `<em>${esc(p.vi)} · ${esc(p.role)}</em>` : ""}</div></div>
      <div class="ch-intro"><p class="han">${p.d} <button class="say" data-say="${p.d}" aria-label="Nghe">${ICON.sound}</button></p>${this.py ? `<p class="ch-ipy">${p.dpy}</p>` : ""}${this.vi ? `<p class="ch-ivi">${esc(p.dvi)}</p>` : ""}</div>
      ${rel.length ? `<h4>${this.vi ? "Mối quan hệ" : "人物关系"}</h4><ul class="ch-rel">${rel.join("")}</ul>` : ""}
    </div></div>`;
  },
  bind(){
    const B = $("#chBody");
    $("#chBack").onclick = () => { showScreen("app"); renderHello(); };
    $("#chPy").onclick = () => { this.py = !this.py; store.set("ww_ch_py", this.py); this.render(); };
    $("#chVi").onclick = () => { this.vi = !this.vi; store.set("ww_ch_vi", this.vi); this.render(); };
    B.querySelectorAll("[data-k]").forEach(el => { const go = () => { this.sel = el.dataset.k; this.render(); speak(CH_PEOPLE[this.sel].zh.replace("AI", "")); };
      el.onclick = go; el.onkeydown = e => { if(e.key === "Enter" || e.key === " "){ e.preventDefault(); go(); } }; });
    B.querySelectorAll("[data-say]").forEach(el => el.onclick = e => { e.stopPropagation(); speak(el.dataset.say); });
    const close = () => { this.sel = null; this.render(); };
    if($("#chX")) $("#chX").onclick = close;
    if($("#chOv")) $("#chOv").onclick = e => { if(e.target.id === "chOv") close(); };
  },
};
