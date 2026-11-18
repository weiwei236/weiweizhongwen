/* ======================= BỘ THỦ 部首 – thẻ hình + trò chơi ghép chữ =======================
   Minh hoạ tự vẽ (SVG), chữ Khải lấy từ dữ liệu nét hanzi-writer-data (hz/d_bushou.js). */
const BS_LIST = [
 // id, chữ, biến thể, tên gọi, pinyin tên, nghĩa, màu nền, mẹo nhớ, ví dụ [chữ, pinyin, nghĩa]
 ["ren", "人", "亻", "单人旁", "dānrén páng", "người", "#CFE3EC", "Hai nét như hai chân người đang đứng. Khi đứng bên trái chữ, 人 viết gọn thành 亻.", [["你", "nǐ", "bạn"], ["他", "tā", "anh ấy"], ["休", "xiū", "nghỉ ngơi"]]],
 ["kou", "口", "", "口字旁", "kǒuzì páng", "miệng", "#F6D5CF", "Một cái miệng đang há to. Chữ có 口 thường liên quan đến ăn, nói, hỏi.", [["吃", "chī", "ăn"], ["喝", "hē", "uống"], ["叫", "jiào", "gọi"]]],
 ["mu", "木", "", "木字旁", "mùzì páng", "cây, gỗ", "#DCE8C8", "Một cái cây: nét ngang là cành, nét sổ là thân, hai nét xiên là rễ.", [["林", "lín", "rừng"], ["桌", "zhuō", "bàn"], ["椅", "yǐ", "ghế"]]],
 ["shui", "水", "氵", "三点水", "sān diǎn shuǐ", "nước", "#CDE7F5", "Dòng nước chảy. Đứng bên trái chữ thành ba giọt nước 氵.", [["河", "hé", "sông"], ["海", "hǎi", "biển"], ["洗", "xǐ", "rửa"]]],
 ["huo", "火", "灬", "火字旁", "huǒzì páng", "lửa", "#FCE2B8", "Ngọn lửa bốc lên với hai tia lửa hai bên. Nằm dưới chữ thành bốn chấm 灬.", [["灯", "dēng", "đèn"], ["热", "rè", "nóng"], ["点", "diǎn", "điểm, đốt"]]],
 ["tu", "土", "", "提土旁", "tí tǔ páng", "đất", "#EADBC6", "Một mầm cây nhô lên khỏi mặt đất.", [["地", "dì", "đất"], ["在", "zài", "ở"], ["坐", "zuò", "ngồi"]]],
 ["ri", "日", "", "日字旁", "rìzì páng", "mặt trời, ngày", "#FFE9A8", "Ông mặt trời hình vuông với một vạch ở giữa.", [["明", "míng", "sáng"], ["早", "zǎo", "sớm"], ["晚", "wǎn", "tối"]]],
 ["yue", "月", "", "月字旁", "yuèzì páng", "mặt trăng, thịt", "#D8D3EE", "Vầng trăng khuyết. Bên trái chữ, 月 còn mang nghĩa “thịt, cơ thể”.", [["朋", "péng", "bạn"], ["胖", "pàng", "mập"], ["脸", "liǎn", "mặt"]]],
 ["shan", "山", "", "山字旁", "shānzì páng", "núi", "#D3E6D6", "Ba đỉnh núi, đỉnh giữa cao nhất.", [["岁", "suì", "tuổi"], ["岛", "dǎo", "đảo"], ["出", "chū", "ra"]]],
 ["nv", "女", "", "女字旁", "nǚzì páng", "phụ nữ", "#F8D7E3", "Một người phụ nữ ngồi khoanh tay duyên dáng.", [["妈", "mā", "mẹ"], ["好", "hǎo", "tốt"], ["姐", "jiě", "chị"]]],
 ["zi", "子", "", "子字旁", "zǐzì páng", "con, trẻ em", "#FDE3C8", "Em bé quấn khăn, hai tay dang ra.", [["字", "zì", "chữ"], ["孩", "hái", "trẻ con"], ["学", "xué", "học"]]],
 ["xin", "心", "忄", "竖心旁", "shù xīn páng", "trái tim, tình cảm", "#FAD3D3", "Trái tim. Bên trái chữ thành 忄. Chữ có 心 thường nói về cảm xúc, suy nghĩ.", [["想", "xiǎng", "nghĩ, nhớ"], ["忙", "máng", "bận"], ["怕", "pà", "sợ"]]],
 ["shou", "手", "扌", "提手旁", "tí shǒu páng", "tay", "#F9E0CC", "Bàn tay xòe năm ngón. Bên trái chữ thành 扌, chữ có 扌 thường là hành động bằng tay.", [["打", "dǎ", "đánh, gọi"], ["找", "zhǎo", "tìm"], ["拿", "ná", "cầm"]]],
 ["mu2", "目", "", "目字旁", "mùzì páng", "mắt", "#D2EAE4", "Con mắt dựng đứng, hai nét ngang ở giữa là con ngươi.", [["看", "kàn", "nhìn"], ["睡", "shuì", "ngủ"], ["眼", "yǎn", "mắt"]]],
 ["tian", "田", "", "田字旁", "tiánzì páng", "ruộng", "#DDEBC2", "Thửa ruộng chia thành bốn ô.", [["男", "nán", "nam"], ["思", "sī", "nghĩ"], ["累", "lèi", "mệt"]]],
 ["men", "门", "", "门字框", "ménzì kuàng", "cửa", "#E8DCCB", "Cánh cửa: chấm bên trên là then cửa.", [["们", "men", "(số nhiều)"], ["问", "wèn", "hỏi"], ["间", "jiān", "gian, khoảng"]]],
 ["yu", "雨", "", "雨字头", "yǔzì tóu", "mưa", "#D5E3F1", "Đám mây với những hạt mưa rơi xuống.", [["雪", "xuě", "tuyết"], ["零", "líng", "số không"], ["雷", "léi", "sấm"]]],
 ["yan", "言", "讠", "言字旁", "yánzì páng", "lời nói", "#E6E1F4", "Lời nói thoát ra từ miệng 口. Bên trái chữ viết gọn thành 讠.", [["说", "shuō", "nói"], ["话", "huà", "lời"], ["语", "yǔ", "ngôn ngữ"]]],
 ["jin", "金", "钅", "金字旁", "jīnzì páng", "kim loại, vàng", "#FBEAB0", "Những thỏi vàng chôn dưới đất. Bên trái chữ thành 钅.", [["钱", "qián", "tiền"], ["银", "yín", "bạc"], ["错", "cuò", "sai"]]],
 ["shi", "食", "饣", "食字旁", "shízì páng", "ăn, đồ ăn", "#FDE0C5", "Bát cơm có nắp đậy. Bên trái chữ thành 饣.", [["饭", "fàn", "cơm"], ["饿", "è", "đói"], ["饺", "jiǎo", "sủi cảo"]]],
 ["zhu", "竹", "⺮", "竹字头", "zhúzì tóu", "tre, trúc", "#D6EBCB", "Hai cành trúc có lá rủ xuống. Trên đầu chữ thành ⺮.", [["笔", "bǐ", "bút"], ["笑", "xiào", "cười"], ["第", "dì", "thứ (số thứ tự)"]]],
 ["cao", "艹", "", "草字头", "cǎozì tóu", "cỏ, cây cỏ", "#DDF0C9", "Hai mầm cỏ non mọc cạnh nhau.", [["花", "huā", "hoa"], ["茶", "chá", "trà"], ["菜", "cài", "rau, món ăn"]]],
 ["mian", "宀", "", "宝盖头", "bǎogài tóu", "mái nhà", "#F1DFD0", "Mái nhà che phía trên. Chữ có 宀 thường liên quan đến nhà cửa.", [["家", "jiā", "nhà"], ["字", "zì", "chữ"], ["安", "ān", "an toàn"]]],
 ["ma", "马", "", "马字旁", "mǎzì páng", "ngựa", "#EBDCCB", "Con ngựa đang phi: có bờm, có chân.", [["妈", "mā", "mẹ"], ["吗", "ma", "(trợ từ hỏi)"], ["骑", "qí", "cưỡi"]]],
 ["yu2", "鱼", "", "鱼字旁", "yúzì páng", "cá", "#CFE8EE", "Con cá: đầu ở trên, thân ở giữa, đuôi ở dưới.", [["鲜", "xiān", "tươi"], ["鲸", "jīng", "cá voi"], ["鱿", "yóu", "mực"]]],
 ["niao", "鸟", "", "鸟字旁", "niǎozì páng", "chim", "#D9ECF6", "Con chim đậu: có mắt, cánh và đuôi.", [["鸡", "jī", "gà"], ["鸭", "yā", "vịt"], ["岛", "dǎo", "đảo"]]],
 ["quan", "犬", "犭", "反犬旁", "fǎn quǎn páng", "chó, thú", "#F2E2CC", "Chú chó vẫy đuôi. Bên trái chữ thành 犭, thường chỉ con vật.", [["狗", "gǒu", "chó"], ["猫", "māo", "mèo"], ["猴", "hóu", "khỉ"]]],
 ["che", "车", "", "车字旁", "chēzì páng", "xe", "#E4E7EF", "Chiếc xe nhìn từ trên xuống: trục và hai bánh.", [["辆", "liàng", "chiếc (xe)"], ["轮", "lún", "bánh xe"], ["较", "jiào", "khá, so"]]],
 ["bei", "贝", "", "贝字旁", "bèizì páng", "vỏ sò, tiền", "#F7E2D8", "Ngày xưa người ta dùng vỏ sò làm tiền, nên chữ có 贝 hay liên quan đến tiền bạc.", [["贵", "guì", "đắt"], ["买", "mǎi", "mua"], ["卖", "mài", "bán"]]],
 ["wang", "王", "", "王字旁", "wángzì páng", "vua, ngọc", "#F8EBC1", "Ba nét ngang là trời, người, đất; nét sổ nối liền – đó là vua. Bên trái chữ thường là “ngọc”.", [["玩", "wán", "chơi"], ["球", "qiú", "quả bóng"], ["班", "bān", "lớp"]]],
 ["shi2", "石", "", "石字旁", "shízì páng", "đá", "#DEDFE3", "Hòn đá lăn dưới vách núi.", [["码", "mǎ", "mã số"], ["破", "pò", "vỡ"], ["碗", "wǎn", "bát"]]],
 ["mi", "米", "", "米字旁", "mǐzì páng", "gạo", "#F7F0DC", "Những hạt gạo rơi ra từ bông lúa.", [["粉", "fěn", "bột, bún"], ["糖", "táng", "đường, kẹo"], ["精", "jīng", "tinh"]]],
 ["yi", "衣", "衤", "衣字旁", "yīzì páng", "áo, quần áo", "#E3DDF2", "Chiếc áo có cổ và hai vạt. Bên trái chữ thành 衤.", [["衬", "chèn", "áo sơ mi (衬衫)"], ["裤", "kù", "quần"], ["袜", "wà", "tất"]]],
 ["zu", "足", "⻊", "足字旁", "zúzì páng", "chân", "#F5DCCF", "Bàn chân với đầu gối ở trên. Bên trái chữ thành ⻊, chữ có ⻊ hay là hoạt động của chân.", [["跑", "pǎo", "chạy"], ["路", "lù", "đường"], ["跳", "tiào", "nhảy"]]],
 ["da", "大", "", "大字头", "dàzì tóu", "to, lớn", "#FCE0C2", "Một người dang rộng hai tay: “to thế này này!”", [["太", "tài", "quá"], ["天", "tiān", "trời"], ["夫", "fū", "chồng"]]],
 ["li", "力", "", "力字旁", "lìzì páng", "sức lực", "#F6D9C9", "Cánh tay gồng lên đầy sức mạnh.", [["男", "nán", "nam"], ["动", "dòng", "động"], ["加", "jiā", "thêm"]]],
 ["dao", "刀", "刂", "立刀旁", "lì dāo páng", "dao", "#DCE3EA", "Con dao có lưỡi cong. Bên phải chữ dựng đứng thành 刂.", [["到", "dào", "đến"], ["别", "bié", "đừng"], ["剪", "jiǎn", "cắt"]]],
 ["he", "禾", "", "禾木旁", "hémù páng", "lúa", "#EFE6B8", "Cây lúa trĩu bông ở trên ngọn.", [["秋", "qiū", "mùa thu"], ["和", "hé", "và"], ["种", "zhǒng", "loại, trồng"]]],
 ["er", "耳", "", "耳字旁", "ěrzì páng", "tai", "#F9DED3", "Cái tai nhìn nghiêng.", [["聊", "liáo", "tán gẫu"], ["取", "qǔ", "lấy"], ["聪", "cōng", "thông minh"]]],
 ["zou", "走", "", "走字旁", "zǒuzì páng", "đi, chạy", "#D8EBDA", "Người bước đi trên mặt đất: phía trên là đất 土, phía dưới là bàn chân.", [["起", "qǐ", "dậy"], ["超", "chāo", "siêu"], ["越", "yuè", "càng"]]]
];
/* Ghép chữ: [chữ, [thành phần], pinyin, nghĩa, id bộ thủ chính (nếu có)] */
const BS_COMBO = [
 ["好", ["女", "子"], "hǎo", "tốt (có con gái và con trai là tốt)", "nv"], ["林", ["木", "木"], "lín", "rừng (hai cây)", "mu"], ["森", ["木", "木", "木"], "sēn", "rừng rậm (ba cây)", "mu"],
 ["明", ["日", "月"], "míng", "sáng (mặt trời + mặt trăng)", "ri"], ["休", ["亻", "木"], "xiū", "nghỉ ngơi (người tựa gốc cây)", "ren"], ["从", ["人", "人"], "cóng", "theo (người đi theo người)", "ren"],
 ["众", ["人", "人", "人"], "zhòng", "đông người", "ren"], ["品", ["口", "口", "口"], "pǐn", "sản phẩm, phẩm chất", "kou"], ["朋", ["月", "月"], "péng", "bạn (bạn bè 朋友)", "yue"],
 ["男", ["田", "力"], "nán", "nam (người dùng sức làm ruộng)", "tian"], ["思", ["田", "心"], "sī", "nghĩ", "xin"], ["妈", ["女", "马"], "mā", "mẹ", "nv"],
 ["吗", ["口", "马"], "ma", "(trợ từ nghi vấn)", "kou"], ["安", ["宀", "女"], "ān", "bình an (người phụ nữ trong nhà)", "mian"], ["字", ["宀", "子"], "zì", "chữ", "mian"],
 ["炎", ["火", "火"], "yán", "nóng, viêm (hai ngọn lửa)", "huo"], ["尖", ["小", "大"], "jiān", "nhọn (trên nhỏ dưới to)", "da"], ["晴", ["日", "青"], "qíng", "trời nắng", "ri"],
 ["早", ["日", "十"], "zǎo", "sớm", "ri"], ["星", ["日", "生"], "xīng", "ngôi sao", "ri"], ["海", ["氵", "每"], "hǎi", "biển", "shui"],
 ["河", ["氵", "可"], "hé", "sông", "shui"], ["汉", ["氵", "又"], "hàn", "Hán (汉语 tiếng Hán)", "shui"], ["洗", ["氵", "先"], "xǐ", "rửa", "shui"],
 ["打", ["扌", "丁"], "dǎ", "đánh, gọi (điện)", "shou"], ["找", ["扌", "戈"], "zhǎo", "tìm", "shou"], ["说", ["讠", "兑"], "shuō", "nói", "yan"],
 ["话", ["讠", "舌"], "huà", "lời nói", "yan"], ["语", ["讠", "吾"], "yǔ", "ngôn ngữ", "yan"], ["请", ["讠", "青"], "qǐng", "mời, xin", "yan"],
 ["钱", ["钅", "戋"], "qián", "tiền", "jin"], ["饭", ["饣", "反"], "fàn", "cơm", "shi"], ["饿", ["饣", "我"], "è", "đói", "shi"],
 ["花", ["艹", "化"], "huā", "hoa", "cao"], ["草", ["艹", "早"], "cǎo", "cỏ", "cao"], ["笔", ["⺮", "毛"], "bǐ", "bút (lông gắn vào cán tre)", "zhu"],
 ["笑", ["⺮", "夭"], "xiào", "cười", "zhu"], ["猫", ["犭", "苗"], "māo", "con mèo", "quan"], ["狗", ["犭", "句"], "gǒu", "con chó", "quan"],
 ["鲜", ["鱼", "羊"], "xiān", "tươi (cá + dê đều tươi ngon)", "yu2"], ["鸡", ["又", "鸟"], "jī", "con gà", "niao"], ["跑", ["足", "包"], "pǎo", "chạy", "zu"],
 ["路", ["足", "各"], "lù", "đường", "zu"], ["起", ["走", "己"], "qǐ", "dậy, lên", "zou"], ["雪", ["雨", "彐"], "xuě", "tuyết", "yu"],
 ["灯", ["火", "丁"], "dēng", "đèn", "huo"], ["胖", ["月", "半"], "pàng", "mập", "yue"], ["你", ["亻", "尔"], "nǐ", "bạn", "ren"],
 ["他", ["亻", "也"], "tā", "anh ấy", "ren"], ["们", ["亻", "门"], "men", "(số nhiều: 我们, 你们)", "ren"], ["想", ["相", "心"], "xiǎng", "nghĩ, nhớ, muốn", "xin"],
 ["忙", ["忄", "亡"], "máng", "bận", "xin"], ["怕", ["忄", "白"], "pà", "sợ", "xin"], ["看", ["手", "目"], "kàn", "nhìn (lấy tay che mắt mà nhìn)", "mu2"],
 ["员", ["口", "贝"], "yuán", "nhân viên", "bei"], ["球", ["王", "求"], "qiú", "quả bóng", "wang"], ["秋", ["禾", "火"], "qiū", "mùa thu (lúa chín vàng như lửa)", "he"],
 ["到", ["至", "刂"], "dào", "đến", "dao"], ["聊", ["耳", "卯"], "liáo", "tán gẫu", "er"], ["码", ["石", "马"], "mǎ", "mã số", "shi2"], ["粉", ["米", "分"], "fěn", "bột", "mi"],
 ["家", ["宀", "豕"], "jiā", "nhà", "mian"], ["坐", ["人", "人", "土"], "zuò", "ngồi (hai người ngồi trên đất)", "tu"], ["动", ["云", "力"], "dòng", "động, cử động", "li"]
];

/* ---------- chữ Khải từ dữ liệu nét ---------- */
function bsGlyph(c, x, y, s, col = "#2B2B33", op = 1, halo = "", sc = null){
  const d = HZ.d[c]; if(!d) return `<text x="${x + s / 2}" y="${y + s * .82}" font-size="${s * .9}" text-anchor="middle" font-family="KaiTi,STKaiti,serif" fill="${col}">${c}</text>`;
  const ps = d.s.map(p => `<path d="${p}"/>`).join("");
  return `<g transform="translate(${x} ${y}) scale(${s / 1024})" opacity="${op}"><g transform="scale(1,-1) translate(0,-900)">${halo ? `<g fill="${halo}" stroke="${halo}" stroke-width="56" stroke-linejoin="round">${ps}</g>` : ""}${sc ? d.s.map((p, i) => `<path d="${p}" fill="${sc[i] || col}"/>`).join("") : `<g fill="${col}">${ps}</g>`}</g></g>`;
}
/* ---------- minh hoạ: viewBox 0 0 200 200, chữ đặt ở khung G = [x, y, cỡ] ---------- */
/* Minh hoạ kiểu "hình lồng chữ": chữ Khải to ở giữa (x 28, y 34, cỡ 144), hình phẳng không viền ôm lấy các nét.
   Mỗi mục trả về { u: hình nằm dưới chữ, o: hình nằm trên chữ, c: màu chữ, sc: {số thứ tự nét: màu}, g: [x, y, cỡ], bg } */
const SK = "#F9D2B5", HAIR = "#3B2A20";
const c_ = (x, y, r, f, o = "") => `<circle cx="${x}" cy="${y}" r="${r}" fill="${f}" ${o}/>`;
const e_ = (x, y, rx, ry, f, o = "") => `<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="${f}" ${o}/>`;
const r_ = (x, y, w, h, f, rx = 0, o = "") => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${f}" ${o}/>`;
const p_ = (d, f, o = "") => `<path d="${d}" fill="${f}" ${o}/>`;
const bsFace = (x, y, r, hair = HAIR) => c_(x, y, r, SK) + p_(`M${x - r} ${y} A${r} ${r} 0 0 1 ${x + r} ${y} Q${x} ${y - r * .35} ${x - r} ${y}Z`, hair) + c_(x - r * .38, y + r * .2, r * .11, "#2B2B33") + c_(x + r * .38, y + r * .2, r * .11, "#2B2B33") + e_(x - r * .55, y + r * .5, r * .16, r * .1, "#F4A0A0") + e_(x + r * .55, y + r * .5, r * .16, r * .1, "#F4A0A0");
const BS_OL = "#5A4034";
/* Mỗi mục: bản cũ trả về [hình, [x, y, cỡ], màu chữ, viền chữ]; bản mới trả về { u, o, c, sc, g, bg } */
const BS_ART = {
  ren: () => [`<circle cx="100" cy="40" r="13" fill="#E8695A" stroke="${BS_OL}" stroke-width="3"/><ellipse cx="62" cy="174" rx="12" ry="6" fill="#E57AA1"/><ellipse cx="146" cy="174" rx="12" ry="6" fill="#E57AA1"/>`, [38, 46, 124]],
  kou: () => ({ u: r_(44, 56, 124, 104, "#F06C8E", 44) + r_(60, 70, 92, 78, "#7A1F2B", 16) + r_(64, 73, 84, 13, "#fff", 5) + e_(106, 134, 32, 12, "#F48FA0"), c: "#2B2B33", g: [10, 20, 180] }),
  mu: () => ({ u: p_("M0 132 Q100 118 200 132 V200 H0Z", "#D9B48A") + c_(100, 56, 40, "#6DBE5A") + c_(64, 72, 30, "#6DBE5A") + c_(136, 70, 30, "#6DBE5A") + c_(84, 40, 22, "#82CC6E") + [[68, 62], [130, 50], [120, 80], [78, 84], [100, 30]].map(([x, y]) => c_(x, y, 5.5, "#E8453C")).join(""), c: "#3B2414" }),
  shui: () => ({ u: p_("M100 18 C122 58 168 82 168 120 A68 64 0 0 1 32 120 C32 82 78 58 100 18Z", "#7CC6E8") + p_("M46 146 q13 -8 27 0 t27 0 t27 0 t27 0", "none", 'stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".75"') + p_("M40 52 q7 11 0 16 q-7 -5 0 -16Z", "#7CC6E8") + p_("M164 44 q6 10 0 14 q-6 -4 0 -14Z", "#7CC6E8"), c: "#123A5A" }),
  huo: () => ({ u: p_("M100 20 C126 54 172 74 162 128 C156 166 128 180 100 180 C72 180 44 166 38 128 C32 88 62 74 74 44 C86 62 92 56 100 20Z", "#F7943D") + p_("M100 72 C120 98 136 118 128 146 C120 168 80 168 72 146 C66 122 88 106 100 72Z", "#FBD36A") + r_(56, 172, 88, 12, "#8E5A33", 6, 'transform="rotate(-8 100 178)"') + r_(56, 172, 88, 12, "#A0703F", 6, 'transform="rotate(8 100 178)"'), c: "#5A1E0E", sc: { 0: "#D9342B", 1: "#D9342B" } }),
  tu: () => ({ u: p_("M0 146 Q100 136 200 146 V200 H0Z", "#B98A5A") + [[30, 168], [80, 182], [140, 172], [176, 186]].map(([x, y]) => e_(x, y, 6, 3, "#9A6B3F")).join(""), c: "#3B2414", sc: { 1: "#3E8E41" } }),
  ri: () => [`<g stroke="#F6B11E" stroke-width="9" stroke-linecap="round">${[0,45,90,135,180,225,270,315].map(a=>{const r=a*Math.PI/180;return `<path d="M${100+Math.cos(r)*70} ${100+Math.sin(r)*70} L${100+Math.cos(r)*88} ${100+Math.sin(r)*88}"/>`}).join("")}</g><circle cx="100" cy="100" r="60" fill="#FFC93C" stroke="#F0A81C" stroke-width="5"/><ellipse cx="70" cy="118" rx="9" ry="6" fill="#F7907B" opacity=".7"/><ellipse cx="130" cy="118" rx="9" ry="6" fill="#F7907B" opacity=".7"/>`, [52, 52, 96], "#7A4A0E"],
  yue: () => [`<rect width="200" height="200" rx="22" fill="#3E3C7A"/><g fill="#FFF6C8"><circle cx="40" cy="40" r="2.5"/><circle cx="160" cy="30" r="2"/><circle cx="170" cy="150" r="2.5"/><circle cx="34" cy="160" r="2"/><path d="M150 70 l3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3z"/></g><path d="M118 22 A80 80 0 1 0 150 170 A64 64 0 1 1 118 22Z" fill="#FFE27A" stroke="#F2C94C" stroke-width="4"/>`, [34, 42, 112], "#6B4E0E", "rgba(255,240,180,.9)"],
  shan: () => ({ u: r_(0, 150, 200, 50, "#B9D59C") + p_("M10 150 L56 86 L100 150Z", "#8CC47A") + p_("M100 150 L142 74 L190 150Z", "#8CC47A") + p_("M46 150 L96 34 L148 150Z", "#6FAE5E") + p_("M84 62 L96 34 L108 62 Q96 70 84 62Z", "#fff") + p_("M48 98 L56 86 L64 98 Q56 102 48 98Z", "#fff") + p_("M134 88 L142 74 L150 88 Q142 92 134 88Z", "#fff") + c_(170, 34, 12, "#FFD45C"), c: "#1F3A1F", bg: "#D7ECF7" }),
  nv: () => ({ u: p_("M70 104 H130 L156 174 Q100 186 44 174Z", "#F4A3B5") + p_("M28 92 Q100 80 172 86 L176 112 Q150 116 132 108 L68 110 Q46 118 24 116Z", "#F48FA6") + r_(66, 100, 68, 10, "#D9465F", 5) + p_("M84 70 Q100 82 116 70 L112 92 H88Z", "#F4A3B5"), o: c_(96, 34, 15, SK) + p_("M80 32 Q80 14 96 14 Q114 14 112 32 Q104 22 96 24 Q86 24 80 32Z", HAIR) + c_(96, 9, 9, HAIR) + e_(80, 38, 4, 8, HAIR) + e_(112, 38, 4, 8, HAIR) + c_(90, 36, 1.8, "#2B2B33") + c_(102, 36, 1.8, "#2B2B33") + p_("M93 42 Q96 44 99 42", "none", 'stroke="#C2513A" stroke-width="1.8" stroke-linecap="round"'), c: "#4A2030", bg: "#F6EFE6" }),
  zi: () => ({ u: e_(90, 126, 38, 46, "#B9DFA2") + p_("M66 116 Q92 100 110 122 Q86 142 70 150", "none", 'stroke="#86C06C" stroke-width="4" stroke-linecap="round"') + p_("M40 100 Q100 88 162 96 L162 110 Q100 104 40 114Z", "#8EC5F0") + c_(94, 64, 26, SK) + c_(68, 68, 5, SK) + c_(120, 64, 5, SK) + p_("M74 50 Q94 30 116 46 Q102 40 92 46Z", "#A0703F") + c_(84, 68, 3, "#2B2B33") + c_(99, 68, 3, "#2B2B33") + e_(78, 77, 4, 2.5, "#F4A0A0") + c_(38, 107, 8, SK) + c_(164, 103, 8, SK), c: "#2B2B33", bg: "#F3EBD9" }),
  xin: () => [`<path d="M100 172 C40 132 20 96 32 64 C44 34 84 34 100 64 C116 34 156 34 168 64 C180 96 160 132 100 172Z" fill="#F48A97" stroke="#D9586A" stroke-width="4"/>`, [40, 42, 120], "#fff"],
  shou: () => [`<path d="M60 186 L56 104 Q52 86 60 80 Q70 78 72 96 L74 40 Q76 28 86 28 Q96 28 96 40 L96 30 Q98 18 108 18 Q118 18 118 30 L118 40 Q120 30 130 30 Q140 32 140 44 L140 70 Q142 60 152 62 Q162 66 158 84 L148 130 Q140 170 130 186Z" fill="#FCD9C0" stroke="#D99A7A" stroke-width="3"/>`, [40, 44, 120]],
  mu2: () => ({ u: p_("M100 30 Q172 104 100 178 Q28 104 100 30Z", "#fff") + c_(104, 104, 28, "#5BA4D9") + c_(104, 104, 12, "#1E2D4A") + c_(112, 96, 4, "#fff") + `<g stroke="#1E2D4A" stroke-width="3" stroke-linecap="round"><path d="M70 62 l-12 -6M60 80 l-14 -2M56 100 l-14 2"/></g>`, c: "#1E2D4A" }),
  tian: () => ({ u: r_(0, 150, 200, 50, "#B9D59C") + r_(68, 68, 30, 36, "#A8D672") + r_(98, 66, 48, 38, "#F2D06A") + r_(68, 104, 30, 40, "#F2D06A") + r_(98, 104, 48, 40, "#A8D672") + [[80, 82], [124, 78], [78, 118], [118, 120], [134, 128], [110, 90]].map(([x, y]) => p_(`M${x} ${y + 6} q-4 -8 -8 -8 M${x} ${y + 6} q4 -8 8 -8`, "none", 'stroke="#4E8F3A" stroke-width="2.5" stroke-linecap="round"')).join(""), c: "#3B2414", bg: "#D7ECF7" }),
  men: () => ({ u: r_(52, 58, 48, 108, "#C9925A", 4) + r_(102, 56, 50, 110, "#B97A45", 4) + c_(93, 114, 3.5, "#FFE27A") + c_(109, 114, 3.5, "#FFE27A") + r_(40, 166, 120, 8, "#9A6B3F", 3), c: "#3B2414", bg: "#EADBC6" }),
  yu: () => ({ u: Array.from({ length: 70 }, (_, i) => { const x = (i % 10) * 22 + ((i / 10 | 0) % 2) * 11 - 4, y = (i / 10 | 0) * 30 + 6; return `<path d="M${x} ${y} l7 14" stroke="#7DB9E4" stroke-width="4" stroke-linecap="round"/>`; }).join("") + c_(70, 52, 20, "#fff") + c_(102, 42, 26, "#fff") + c_(136, 52, 20, "#fff") + r_(52, 52, 104, 22, "#fff", 11), c: "#1C3F5E", sc: { 4: "#2F7CC4", 5: "#2F7CC4", 6: "#2F7CC4", 7: "#2F7CC4" }, bg: "#C9E6F7" }),
  yan: () => [`<path d="M30 40 Q30 22 50 22 H150 Q170 22 170 40 V140 Q170 158 150 158 H86 L58 184 L62 158 H50 Q30 158 30 140Z" fill="#fff" stroke="#A79BD6" stroke-width="5"/>`, [46, 30, 108]],
  jin: () => [`<path d="M30 170 L56 132 H144 L170 170Z" fill="#F6C343" stroke="#D49B12" stroke-width="3"/><path d="M60 132 L78 104 H122 L140 132Z" fill="#FBD86A" stroke="#D49B12" stroke-width="3"/><g fill="#fff" opacity=".8"><path d="M150 40 l4 10 10 4 -10 4 -4 10 -4 -10 -10 -4 10 -4z"/></g>`, [44, 30, 112]],
  shi: () => [`<path d="M36 112 H164 Q160 168 100 172 Q40 168 36 112Z" fill="#fff" stroke="#E8803C" stroke-width="5"/><path d="M48 112 Q100 70 152 112Z" fill="#fff" stroke="#E8D6B8" stroke-width="3"/><g fill="#F0E2C2"><circle cx="80" cy="100" r="5"/><circle cx="100" cy="94" r="5"/><circle cx="120" cy="100" r="5"/></g>`, [48, 20, 104]],
  zhu: () => ({ u: r_(64, 30, 16, 166, "#7CC264", 7) + r_(116, 24, 16, 172, "#7CC264", 7) + [70, 112, 154].map(y => r_(62, y, 20, 4, "#5A9E47", 2) + r_(114, y - 6, 20, 4, "#5A9E47", 2)).join("") + e_(150, 46, 22, 7, "#93D27A", 'transform="rotate(-25 150 46)"') + e_(44, 60, 22, 7, "#93D27A", 'transform="rotate(25 44 60)"') + e_(150, 70, 18, 6, "#93D27A", 'transform="rotate(15 150 70)"'), c: "#1F3A1F", sc: { 2: "#2E6B2F", 5: "#2E6B2F" }, bg: "#E6F2D8" }),
  cao: () => ({ u: r_(0, 122, 200, 78, "#B98A5A") + Array.from({ length: 22 }, (_, i) => { const x = 18 + i * 8, h = 50 + (i * 37 % 40); return p_(`M${x - 5} 124 Q${x} ${124 - h * .6} ${x + (i % 2 ? 6 : -6)} ${124 - h} Q${x + 2} ${124 - h * .5} ${x + 5} 124Z`, i % 3 ? "#6DBE5A" : "#86CF72"); }).join(""), c: "#1F3A1F", g: [16, 40, 168], bg: "#E8F4DC" }),
  mian: () => ({ u: r_(54, 132, 92, 56, "#FFF3E0") + r_(88, 150, 24, 38, "#C9925A", 3) + r_(62, 144, 18, 16, "#BFE6FA", 3) + r_(120, 144, 18, 16, "#BFE6FA", 3) + p_("M48 136 L56 118 H160 L162 136Z", "#E8695A") + r_(132, 92, 12, 26, "#B5523F") + r_(0, 186, 200, 14, "#B9D59C"), c: "#5A1E14", g: [10, 50, 180], bg: "#DCEFF8" }),
  ma: () => ({ u: e_(110, 128, 54, 28, "#D9A066") + p_("M58 124 L80 100 L72 62 L54 44 L36 54 L44 72 L52 110Z", "#D9A066") + p_("M56 46 Q76 50 82 70 L80 98 Q72 70 60 58Z", "#6B4226") + [70, 90, 128, 148].map(x => r_(x - 5, 140, 10, 46, "#B97A45", 5)).join("") + p_("M160 118 Q190 130 182 176 Q172 150 158 140Z", "#6B4226"), c: "#3B2414" }),
  yu2: () => [`<path d="M30 100 Q80 40 140 80 L182 54 L172 100 L182 146 L140 120 Q80 160 30 100Z" fill="#F7A55E" opacity=".6" stroke="#E07A1F" stroke-width="3"/><circle cx="56" cy="94" r="5" fill="${BS_OL}"/>`, [44, 40, 112]],
  niao: () => [`<path d="M40 90 Q50 40 100 44 Q150 46 156 96 Q170 120 186 128 Q150 138 120 150 Q60 156 40 90Z" fill="#8CCBEA" opacity=".6" stroke="#5B9BD5" stroke-width="3"/><path d="M40 72 L18 80 L40 86Z" fill="#F6B444"/><circle cx="58" cy="70" r="5" fill="${BS_OL}"/>`, [44, 40, 112]],
  quan: () => [`<path d="M150 150 Q190 130 182 96" stroke="#D9A066" stroke-width="12" stroke-linecap="round" fill="none"/><ellipse cx="104" cy="156" rx="56" ry="34" fill="#E8B77D" stroke="$${BS_OL}" stroke-width="3"/><circle cx="100" cy="86" r="52" fill="#F2C994" stroke="$${BS_OL}" stroke-width="3"/><path d="M52 60 Q34 74 40 120 Q56 112 62 84Z M148 60 Q166 74 160 120 Q144 112 138 84Z" fill="#B97A4A" stroke="$${BS_OL}" stroke-width="3"/><ellipse cx="100" cy="106" rx="22" ry="16" fill="#FFF1DC"/><ellipse cx="100" cy="98" rx="8" ry="6" fill="$${BS_OL}"/><circle cx="80" cy="80" r="5" fill="$${BS_OL}"/><circle cx="120" cy="80" r="5" fill="$${BS_OL}"/><path d="M96 116 Q100 132 108 118" fill="#F27C8A"/>`, [46, 42, 108], "#2B2B33", "rgba(255,255,255,.88)"],
  che: () => ({ u: [[48, 54], [140, 54], [28, 118], [158, 118]].map(([x, y]) => r_(x, y, 16, 34, "#3B3B46", 6)).join("") + r_(76, 44, 50, 128, "#E8695A", 16) + r_(82, 52, 38, 22, "#BFE6FA", 6) + r_(82, 142, 38, 18, "#BFE6FA", 6), c: "#2B2B33", bg: "#E4E7EF" }),
  bei: () => ({ u: e_(100, 108, 60, 74, "#F3D9B1") + [[72, 70], [128, 62], [62, 120], [138, 112], [80, 160], [124, 156], [100, 50]].map(([x, y]) => c_(x, y, 6, "#D9A66B")).join("") + p_("M100 44 Q90 76 104 108 Q90 140 100 172", "none", 'stroke="#7A4A22" stroke-width="7" stroke-linecap="round"') + [60, 80, 100, 120, 140, 160].map(y => p_(`M88 ${y} H112`, "none", 'stroke="#FFF6E6" stroke-width="3" stroke-linecap="round"')).join(""), c: "#4A2A12", bg: "#D5ECF5" }),
  wang: () => ({ u: p_("M64 66 H136 L154 168 H46Z", "#B39DDB") + p_("M46 66 L52 22 L76 46 L100 14 L124 46 L148 22 L154 66Z", "#F6C343") + c_(100, 40, 6, "#E8453C") + c_(70, 52, 4.5, "#5BA4D9") + c_(130, 52, 4.5, "#5BA4D9"), c: "#5A3A0A", bg: "#FFF3C8" }),
  shi2: () => ({ u: p_("M0 0 H200 V56 Q170 66 140 60 L64 66 Q30 70 0 84Z", "#8C8D99") + e_(108, 128, 46, 38, "#C9CAD2") + e_(96, 116, 14, 6, "#fff", 'opacity=".6"') + e_(30, 176, 14, 8, "#B5B6C0") + e_(176, 180, 10, 6, "#B5B6C0") + e_(150, 170, 8, 5, "#B5B6C0"), c: "#2B2B33", bg: "#ECEDF1" }),
  mi: () => [`<g fill="#fff" stroke="#E2D2A6" stroke-width="2">${[[40, 40], [160, 46], [36, 160], [164, 156], [100, 26], [100, 178], [24, 100], [176, 100]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="9" ry="6" transform="rotate(${(x + y) % 90} ${x} ${y})"/>`).join("")}</g>`, [40, 40, 120]],
  yi: () => ({ u: p_("M70 52 L100 68 L130 52 L176 84 L160 114 L144 104 V180 H56 V104 L40 114 L24 84Z", "#8EC5F0") + p_("M84 56 L100 86 L116 56", "none", 'stroke="#fff" stroke-width="6" stroke-linejoin="round"') + [118, 140, 162].map(y => c_(100, y, 3, "#fff")).join(""), c: "#1F3A5F", bg: "#E3DDF2" }),
  zu: () => ({ u: r_(80, 0, 40, 132, SK) + r_(78, 110, 44, 30, "#fff") + r_(78, 118, 44, 6, "#5BA4D9") + r_(78, 130, 44, 6, "#5BA4D9") + p_("M64 140 H134 Q176 140 178 164 Q178 178 162 178 H64 Q56 160 64 140Z", "#E8453C") + r_(62, 174, 118, 8, "#fff", 4), c: "#3B2414", bg: "#F5DCCF" }),
  da: () => [`<g stroke="#E8803C" stroke-width="18" stroke-linecap="round"><path d="M100 76 L22 66M100 76 L178 66"/></g><g stroke="#3E5C52" stroke-width="18" stroke-linecap="round"><path d="M100 120 L44 182M100 120 L156 182"/></g><path d="M80 64 H120 L124 124 H76Z" fill="#F7A43D" stroke="$${BS_OL}" stroke-width="3"/><circle cx="100" cy="36" r="24" fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"/><path d="M78 30 Q100 6 122 30 Q108 22 78 30Z" fill="#4A3020"/><circle cx="92" cy="38" r="3" fill="$${BS_OL}"/><circle cx="108" cy="38" r="3" fill="$${BS_OL}"/><path d="M92 46 Q100 54 108 46" stroke="$${BS_OL}" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="22" cy="66" r="9" fill="#FCE3D2"/><circle cx="178" cy="66" r="9" fill="#FCE3D2"/>`, [44, 50, 112], "#2B2B33", "rgba(255,255,255,.88)"],
  li: () => [`<path d="M24 186 L36 120 Q40 98 62 92 L74 64 Q72 44 84 36 Q100 28 108 44 L112 58 Q134 40 156 52 Q178 66 170 96 Q160 126 130 128 L106 126 L96 186Z" fill="#F7C6A5" stroke="#D9876A" stroke-width="5" stroke-linejoin="round"/><path d="M114 60 Q140 56 150 76" stroke="#E8A587" stroke-width="5" stroke-linecap="round" fill="none"/><g fill="#FFE27A"><path d="M160 22 l4 10 10 4 -10 4 -4 10 -4 -10 -10 -4 10 -4z"/><path d="M182 52 l3 6 6 3 -6 3 -3 6 -3 -6 -6 -3 6 -3z"/></g>`, [46, 50, 108], "#7A2E14", "rgba(255,255,255,.88)"],
  dao: () => ({ u: p_("M60 64 L146 58 V152 Q142 160 130 154 L58 144Z", "#F4F7FA") + p_("M60 140 L132 150", "none", 'stroke="#AEBBC9" stroke-width="5" stroke-linecap="round"') + c_(132, 72, 5, "#C9D6E3") + r_(14, 60, 50, 22, "#A0703F", 9) + c_(30, 71, 3, "#E8C9A0") + c_(48, 71, 3, "#E8C9A0"), c: "#2B2B33", bg: "#C9D6E3" }),
  he: () => [`<path d="M100 186 V40" stroke="#C9A43C" stroke-width="5"/><path d="M100 40 Q130 34 150 60 Q160 80 150 96" stroke="#E2B93B" stroke-width="10" stroke-linecap="round" fill="none"/><g fill="#F2D06A">${[0, 1, 2, 3].map(i => `<ellipse cx="${140 + i * 4}" cy="${56 + i * 12}" rx="6" ry="4"/>`).join("")}</g>`, [40, 46, 120]],
  er: () => ({ u: p_("M54 64 Q54 20 108 20 Q176 24 178 102 Q178 160 130 182 Q100 194 84 172 Q74 154 92 140 Q62 120 54 64Z", "#F9C8A8") + p_("M80 66 Q82 40 110 40 Q156 44 156 100 Q156 140 126 160 Q110 166 104 154", "none", 'stroke="#F4A08A" stroke-width="10" stroke-linecap="round"'), c: "#5A2E14", bg: "#FCEDE4" }),
  zou: () => [`<path d="M0 174 H200 V200 H0Z" fill="#B9D59C"/><g stroke="#9CC07A" stroke-width="4" stroke-linecap="round"><path d="M14 92 H44M8 112 H38M18 132 H46"/></g><circle cx="112" cy="40" r="20" fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"/><path d="M96 30 Q112 12 130 30 Q118 24 96 30Z" fill="#4A3020"/><g stroke="#3E7C6A" stroke-width="14" stroke-linecap="round" fill="none"><path d="M110 62 L100 110"/><path d="M106 72 L80 92 M106 72 L138 84"/></g><g stroke="#3E5C52" stroke-width="13" stroke-linecap="round" fill="none"><path d="M100 110 L70 140 L52 136"/><path d="M100 110 L128 142 L134 172"/></g>`, [44, 44, 112], "#2B2B33", "rgba(255,255,255,.88)"]
};
function bsCard(r, big){
  const [id, ch, , , , , bg0] = r; let a = BS_ART[id] ? BS_ART[id]() : {};
  if(Array.isArray(a)) a = { u: a[0], g: a[1], c: a[2], halo: a[3] };
  const [x, y, s] = a.g || [28, 34, 144];
  return `<svg class="bs-svg" viewBox="0 0 200 200" role="img" aria-label="${ch}"><defs><clipPath id="bsc_${id}"><rect width="200" height="200" rx="${big ? 18 : 22}"/></clipPath></defs><g clip-path="url(#bsc_${id})"><rect width="200" height="200" fill="${a.bg || bg0}"/>${a.u || ""}${bsGlyph(ch, x, y, s, a.c || "#2B2B33", 1, a.halo || "", a.sc)}${a.o || ""}</g></svg>`;
}

const Bushou = {
  view: "list", sel: null, g: null,
  async open(view = "list"){
    showScreen("scrBushou"); this.view = view; $("#bsBody").innerHTML = `<p class="muted" style="text-align:center;padding:40px">Đang tải bộ thủ…</p>`;
    try{ await HZ.script("hz/d_bushou.js"); }catch(e){}
    this.render();
  },
  top(){ return `<div class="bs-top"><div><h2><span class="han">部首</span> · Bộ thủ</h2><p class="muted">${BS_LIST.length} bộ thủ thường gặp – học bằng hình, rồi chơi ghép chữ nhé!</p></div>
    <div class="bs-acts"><div class="seg" role="group"><button data-v="list" aria-pressed="${this.view === "list" || this.view === "card"}">Thẻ bộ thủ</button><button data-v="combo" aria-pressed="${this.view === "combo"}">Ghép chữ</button><button data-v="find" aria-pressed="${this.view === "find"}">Tìm bộ thủ</button></div>
    <button class="btn" id="bsBack">${ICON.left}Về trang học</button></div></div>`; },
  render(){
    let h = this.top();
    if(this.view === "list") h += `<div class="bs-grid">${BS_LIST.map((r, i) => `<button class="bs-tile" data-i="${i}">${bsCard(r)}<b>${r[2] ? `${r[1]} <span>${r[2]}</span>` : r[1]}</b><small>${esc(r[5])}</small></button>`).join("")}</div>`;
    else if(this.view === "card") h += this.cardView();
    else h += this.gameView();
    $("#bsBody").innerHTML = h; this.bind();
  },
  cardView(){
    const r = BS_LIST[this.sel], [id, ch, vr, nm, nmpy, vi, , tip, ex] = r, combos = BS_COMBO.filter(c => c[4] === id);
    return `<div class="bs-detail"><div class="bs-big">${bsCard(r, true)}</div><div class="bs-info">
      <div class="bs-name"><span class="han">${ch}</span>${vr ? `<span class="han bs-var">${vr}</span>` : ""}<button class="say" data-say="${ch}" aria-label="Nghe">${ICON.sound}</button></div>
      <p class="bs-nm"><b class="han">${nm}</b> <small>${nmpy}</small> · <b>${esc(vi)}</b></p><p class="bs-tip">💡 ${esc(tip)}</p>
      <h4>Chữ thường gặp</h4><div class="bs-ex">${ex.map(([c, p, v]) => `<button data-say="${c}"><b class="han">${c}</b><small>${p}</small><span>${esc(v)}</span></button>`).join("")}</div>
      ${combos.length ? `<h4>Ghép chữ</h4><div class="bs-cmb">${combos.map(c => `<button data-say="${c[0]}"><span class="han">${c[1].join(" + ")} = <b>${c[0]}</b></span><small>${c[2]} · ${esc(c[3])}</small></button>`).join("")}</div>` : ""}
      <div class="tp-row"><button class="btn" data-mv="-1">${ICON.left}Bộ trước</button><button class="btn" id="bsList">Tất cả bộ thủ</button><button class="btn" data-mv="1">Bộ sau ${ICON.right}</button></div></div></div>`;
  },
  /* ---------- trò chơi ---------- */
  newGame(mode){
    const pool = shuffle(BS_COMBO.filter(c => mode === "combo" || BS_LIST.some(r => r[0] === c[4]))).slice(0, 10);
    this.g = { mode, items: pool, i: 0, right: 0, pick: [], fb: null };
    pool.forEach(it => { if(mode === "combo"){ const parts = it[1], others = shuffle([...new Set(BS_COMBO.flatMap(c => c[1]).filter(x => !parts.includes(x)))]).slice(0, Math.max(3, 7 - parts.length)); it.tiles = shuffle([...parts, ...others]); }
      else { const right = BS_LIST.find(r => r[0] === it[4]); it.opts = shuffle([right, ...shuffle(BS_LIST.filter(r => r !== right)).slice(0, 3)]); } });
  },
  gameView(){
    const G = this.g; if(!G || G.mode !== this.view) this.newGame(this.view);
    const g = this.g;
    if(g.i >= g.items.length){
      const pct = g.right / g.items.length * 100, key = "bushou:" + this.view + ":" + SRS.today();
      if(!g.paid){ g.paid = true; Track.log("bushou", { mode: this.view, right: g.right, total: g.items.length }, ""); if(typeof Farm !== "undefined" && Farm.load() && !(Farm.st.done || {})[key]) Farm.earn(pct, (this.view === "combo" ? "Ghép chữ" : "Tìm bộ thủ") + ` (${g.right}/${g.items.length})`, key); }
      return `<div class="panel bs-end"><span class="han">${pct >= 80 ? "棒" : "加油"}</span><h3>Bạn đúng ${g.right}/${g.items.length} câu</h3><p class="muted">Mỗi ngày chơi lần đầu được cộng xu nông trại.</p><button class="btn primary big" id="bsAgain">Chơi lại</button></div>`;
    }
    const it = g.items[g.i], dots = `<div class="tp-dots">${g.items.map((x, k) => `<i class="${k < g.i ? (x.res ? "r" : "w") : k === g.i ? "now" : ""}"></i>`).join("")}</div>`;
    if(this.view === "combo"){
      const n = it[1].length, done = g.fb;
      return `<div class="panel bs-game">${dots}<p class="bs-q">Ghép các bộ phận thành chữ có nghĩa <b>“${esc(it[3])}”</b> · <span class="bs-py">${it[2]}</span> <button class="say" data-say="${it[0]}" aria-label="Nghe">${ICON.sound}</button></p>
        <div class="bs-slots">${Array.from({ length: n }, (_, k) => { const t = g.pick[k]; return `<button class="bs-slot ${t != null ? "on" : ""}" data-back="${k}" ${done ? "disabled" : ""}>${t != null ? `<svg viewBox="0 0 100 100">${bsGlyph(it.tiles[t], 8, 8, 84)}</svg>` : ""}</button>`; }).join(`<span class="bs-plus">+</span>`)}
          <span class="bs-plus">=</span><div class="bs-res ${done ? (it.res ? "right" : "wrong") : ""}">${done ? `<svg viewBox="0 0 100 100">${bsGlyph(it[0], 6, 6, 88, it.res ? "#2C9A58" : "#C2513A")}</svg>` : "?"}</div></div>
        <div class="bs-tiles">${it.tiles.map((t, k) => `<button class="bs-tile2" data-t="${k}" ${done || g.pick.includes(k) ? "disabled" : ""}><svg viewBox="0 0 100 100">${bsGlyph(t, 10, 10, 80)}</svg></button>`).join("")}</div>
        ${done ? `<p class="bs-fb ${it.res ? "good" : "bad"}">${it.res ? "Chính xác! " : "Chưa đúng. "}<b class="han">${it[1].join(" + ")} = ${it[0]}</b> (${it[2]}) – ${esc(it[3])}</p><button class="btn primary big" id="bsNext">${g.i < g.items.length - 1 ? "Câu tiếp →" : "Xem kết quả"}</button>`
          : `<div class="tp-row"><button class="btn" id="bsClr">Xoá</button><button class="btn primary" id="bsChk" ${g.pick.length === n ? "" : "disabled"}>Kiểm tra</button></div>`}</div>`;
    }
    const done = g.fb, right = BS_LIST.find(r => r[0] === it[4]);
    return `<div class="panel bs-game">${dots}<p class="bs-q">Chữ này có bộ thủ nào? <button class="say" data-say="${it[0]}" aria-label="Nghe">${ICON.sound}</button></p>
      <div class="bs-target"><svg viewBox="0 0 100 100">${bsGlyph(it[0], 4, 4, 92)}</svg><small>${it[2]} · ${esc(it[3])}</small></div>
      <div class="bs-opts">${it.opts.map((r, k) => `<button class="bs-opt ${done ? (r === right ? "right" : it.sel === k ? "wrong" : "") : ""}" data-o="${k}" ${done ? "disabled" : ""}>${bsCard(r)}<b>${r[1]}${r[2] ? " " + r[2] : ""}</b><small>${esc(r[5])}</small></button>`).join("")}</div>
      ${done ? `<p class="bs-fb ${it.res ? "good" : "bad"}">${it.res ? "Đúng rồi! " : "Chưa đúng. "}<b class="han">${it[0]}</b> có bộ <b class="han">${right[1]}${right[2] ? " (" + right[2] + ")" : ""}</b> – ${esc(right[5])}.</p><button class="btn primary big" id="bsNext">${g.i < g.items.length - 1 ? "Câu tiếp →" : "Xem kết quả"}</button>` : ""}</div>`;
  },
  bind(){
    const B = $("#bsBody"), on = (s, f) => B.querySelectorAll(s).forEach(el => el.onclick = () => f(el));
    on("#bsBack", () => { showScreen("app"); renderHello(); });
    on("[data-v]", el => { this.view = el.dataset.v; this.g = null; this.render(); });
    on(".bs-tile", el => { this.sel = +el.dataset.i; this.view = "card"; this.render(); window.scrollTo(0, 0); speak(BS_LIST[this.sel][1]); });
    on("#bsList", () => { this.view = "list"; this.render(); });
    on("[data-mv]", el => { this.sel = (this.sel + +el.dataset.mv + BS_LIST.length) % BS_LIST.length; this.render(); speak(BS_LIST[this.sel][1]); });
    on("[data-say]", el => speak(el.dataset.say));
    const g = this.g; if(!g) return; const it = g.items[g.i];
    on("[data-t]", el => { if(g.pick.length < it[1].length){ g.pick.push(+el.dataset.t); this.render(); } });
    on("[data-back]", el => { g.pick.splice(+el.dataset.back, 1); this.render(); });
    on("#bsClr", () => { g.pick = []; this.render(); });
    on("#bsChk", () => { const a = g.pick.map(k => it.tiles[k]).sort().join(), b = [...it[1]].sort().join(); it.res = a === b; if(it.res) g.right++; g.fb = true; this.render(); speak(it[0]); });
    on("[data-o]", el => { it.sel = +el.dataset.o; it.res = it.opts[it.sel][0] === it[4]; if(it.res) g.right++; g.fb = true; this.render(); speak(it[0]); });
    on("#bsNext", () => { g.i++; g.pick = []; g.fb = null; this.render(); });
    on("#bsAgain", () => { this.g = null; this.render(); });
  }
};
