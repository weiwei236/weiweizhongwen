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
function bsGlyph(c, x, y, s, col = "#2B2B33", op = 1, halo = ""){
  const d = HZ.d[c]; if(!d) return `<text x="${x + s / 2}" y="${y + s * .82}" font-size="${s * .9}" text-anchor="middle" font-family="KaiTi,STKaiti,serif" fill="${col}">${c}</text>`;
  const ps = d.s.map(p => `<path d="${p}"/>`).join("");
  return `<g transform="translate(${x} ${y}) scale(${s / 1024})" opacity="${op}"><g transform="scale(1,-1) translate(0,-900)">${halo ? `<g fill="${halo}" stroke="${halo}" stroke-width="56" stroke-linejoin="round">${ps}</g>` : ""}<g fill="${col}">${ps}</g></g></g>`;
}
/* ---------- minh hoạ: viewBox 0 0 200 200, chữ đặt ở khung G = [x, y, cỡ] ---------- */
const BS_OL = "#5A4034";
const BS_ART = {
  ren: () => [`<circle cx="100" cy="40" r="13" fill="#E8695A" stroke="${BS_OL}" stroke-width="3"/><ellipse cx="62" cy="174" rx="12" ry="6" fill="#E57AA1"/><ellipse cx="146" cy="174" rx="12" ry="6" fill="#E57AA1"/>`, [38, 46, 124]],
  kou: () => [`<rect x="38" y="44" width="124" height="112" rx="30" fill="#C2413A" stroke="${BS_OL}" stroke-width="4"/><path d="M52 58 Q100 50 148 58 L148 66 Q100 60 52 66Z" fill="#fff"/><path d="M52 142 Q100 150 148 142 L148 134 Q100 140 52 134Z" fill="#fff"/><ellipse cx="100" cy="122" rx="34" ry="16" fill="#F06C6C"/>`, [46, 44, 108], "#FFF4E8"],
  mu: () => [`<ellipse cx="100" cy="74" rx="66" ry="54" fill="#7CC264" stroke="${BS_OL}" stroke-width="3"/><circle cx="58" cy="96" r="26" fill="#8FD07A"/><circle cx="146" cy="92" r="28" fill="#8FD07A"/><rect x="92" y="120" width="16" height="50" rx="6" fill="#A0703F"/>`, [40, 36, 120]],
  shui: () => [`<path d="M20 70 Q45 52 70 70 T120 70 T170 70 T200 70 V200 H0 V70Z" fill="#7CC6E8" opacity=".6"/><path d="M0 120 Q30 104 60 120 T120 120 T180 120 T220 120 V200 H0Z" fill="#59B3DF" opacity=".7"/><path d="M150 30 q12 18 0 26 q-12 -8 0 -26Z" fill="#59B3DF"/>`, [40, 40, 120]],
  huo: () => [`<path d="M100 18 C130 52 168 70 160 118 C154 156 128 176 100 176 C72 176 46 156 40 118 C34 82 66 70 72 40 C86 58 88 70 100 18Z" fill="#F7A43D" stroke="#E07A1F" stroke-width="4"/><path d="M100 70 C118 92 132 110 124 138 C118 156 82 156 76 138 C70 116 88 104 100 70Z" fill="#FBD36A"/>`, [42, 52, 116]],
  tu: () => [`<path d="M10 170 Q100 120 190 170 V200 H10Z" fill="#B98A5A"/><path d="M100 130 Q90 108 70 104 Q86 96 100 112 Q112 94 132 98 Q114 106 100 130Z" fill="#7CC264"/>`, [40, 34, 120]],
  ri: () => [`<g stroke="#F6B11E" stroke-width="9" stroke-linecap="round">${[0,45,90,135,180,225,270,315].map(a=>{const r=a*Math.PI/180;return `<path d="M${100+Math.cos(r)*70} ${100+Math.sin(r)*70} L${100+Math.cos(r)*88} ${100+Math.sin(r)*88}"/>`}).join("")}</g><circle cx="100" cy="100" r="60" fill="#FFC93C" stroke="#F0A81C" stroke-width="5"/><ellipse cx="70" cy="118" rx="9" ry="6" fill="#F7907B" opacity=".7"/><ellipse cx="130" cy="118" rx="9" ry="6" fill="#F7907B" opacity=".7"/>`, [52, 52, 96], "#7A4A0E"],
  yue: () => [`<rect width="200" height="200" rx="22" fill="#3E3C7A"/><g fill="#FFF6C8"><circle cx="40" cy="40" r="2.5"/><circle cx="160" cy="30" r="2"/><circle cx="170" cy="150" r="2.5"/><circle cx="34" cy="160" r="2"/><path d="M150 70 l3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3z"/></g><path d="M118 22 A80 80 0 1 0 150 170 A64 64 0 1 1 118 22Z" fill="#FFE27A" stroke="#F2C94C" stroke-width="4"/>`, [34, 42, 112], "#6B4E0E", "rgba(255,240,180,.9)"],
  shan: () => [`<path d="M10 170 L58 70 L84 110 L106 40 L138 104 L156 80 L196 170Z" fill="#8DBF7B" stroke="${BS_OL}" stroke-width="3" stroke-linejoin="round"/><path d="M94 66 L106 40 L118 64 Q106 72 94 66Z" fill="#fff"/>`, [40, 56, 116]],
  nv: () => [`<path d="M100 56 Q150 60 158 130 L170 186 H30 L42 130 Q50 60 100 56Z" fill="#F7A8C0" stroke="#E07A98" stroke-width="4"/><circle cx="100" cy="44" r="28" fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"/><path d="M70 50 Q66 12 100 12 Q134 12 130 50 Q128 30 100 28 Q74 30 70 50Z" fill="#4A3020"/><path d="M70 50 Q64 70 72 82 L80 60Z M130 50 Q136 70 128 82 L120 60Z" fill="#4A3020"/><path d="M122 14 l14 -10 l2 16z M122 14 l14 10 l-14 2z" fill="#F06C8E"/><circle cx="90" cy="46" r="3" fill="$${BS_OL}"/><circle cx="110" cy="46" r="3" fill="$${BS_OL}"/><path d="M93 56 Q100 62 107 56" stroke="$${BS_OL}" stroke-width="2.5" fill="none" stroke-linecap="round"/>`, [46, 72, 108], "#7A1F3F", "rgba(255,255,255,.88)"],
  zi: () => [`<path d="M48 82 Q100 66 152 82 Q156 140 136 178 Q100 194 64 178 Q44 140 48 82Z" fill="#9FD0F0" stroke="#5B9BD5" stroke-width="4"/><g stroke="#5B9BD5" stroke-width="3" fill="none" opacity=".6"><path d="M60 120 Q100 136 140 120M62 150 Q100 166 138 150"/></g><circle cx="100" cy="52" r="32" fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"/><path d="M84 26 Q100 14 112 24 Q102 22 98 30Z" fill="#4A3020"/><circle cx="88" cy="54" r="4" fill="$${BS_OL}"/><circle cx="112" cy="54" r="4" fill="$${BS_OL}"/><ellipse cx="80" cy="64" rx="6" ry="4" fill="#F6A9A9"/><ellipse cx="120" cy="64" rx="6" ry="4" fill="#F6A9A9"/><path d="M94 68 Q100 74 106 68" stroke="$${BS_OL}" stroke-width="2.5" fill="none" stroke-linecap="round"/><g fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"><circle cx="30" cy="92" r="12"/><circle cx="170" cy="92" r="12"/></g><g stroke="#9FD0F0" stroke-width="16" stroke-linecap="round"><path d="M38 96 L60 106M162 96 L140 106"/></g>`, [50, 80, 100], "#1F4E79", "rgba(255,255,255,.88)"],
  xin: () => [`<path d="M100 172 C40 132 20 96 32 64 C44 34 84 34 100 64 C116 34 156 34 168 64 C180 96 160 132 100 172Z" fill="#F48A97" stroke="#D9586A" stroke-width="4"/>`, [40, 42, 120], "#fff"],
  shou: () => [`<path d="M60 186 L56 104 Q52 86 60 80 Q70 78 72 96 L74 40 Q76 28 86 28 Q96 28 96 40 L96 30 Q98 18 108 18 Q118 18 118 30 L118 40 Q120 30 130 30 Q140 32 140 44 L140 70 Q142 60 152 62 Q162 66 158 84 L148 130 Q140 170 130 186Z" fill="#FCD9C0" stroke="#D99A7A" stroke-width="3"/>`, [40, 44, 120]],
  mu2: () => [`<path d="M100 20 Q172 100 100 180 Q28 100 100 20Z" fill="#fff" stroke="${BS_OL}" stroke-width="4"/><circle cx="100" cy="100" r="34" fill="#7CC6E8" opacity=".55"/>`, [44, 40, 112]],
  tian: () => [`<rect x="24" y="28" width="152" height="146" rx="14" fill="#B5DB8E"/><g stroke="#8CBF64" stroke-width="2"><path d="M40 60h40M40 80h40M120 60h40M120 80h40M40 130h40M40 150h40M120 130h40M120 150h40"/></g>`, [36, 36, 128]],
  men: () => [`<rect x="34" y="22" width="132" height="160" rx="8" fill="#D0A570" stroke="${BS_OL}" stroke-width="4"/><path d="M100 22 V182" stroke="${BS_OL}" stroke-width="3"/><circle cx="92" cy="104" r="4" fill="#FFE27A"/><circle cx="108" cy="104" r="4" fill="#FFE27A"/>`, [40, 36, 120]],
  yu: () => [`<path d="M40 70 Q40 34 82 40 Q96 16 126 28 Q166 26 162 66 Q178 80 160 92 H48 Q24 88 40 70Z" fill="#fff" stroke="#9DBBD8" stroke-width="4"/><g fill="#59B3DF"><path d="M54 130 q6 10 0 16 q-6 -6 0 -16Z"/><path d="M146 150 q6 10 0 16 q-6 -6 0 -16Z"/><path d="M100 172 q6 10 0 16 q-6 -6 0 -16Z"/></g>`, [44, 38, 112]],
  yan: () => [`<path d="M30 40 Q30 22 50 22 H150 Q170 22 170 40 V140 Q170 158 150 158 H86 L58 184 L62 158 H50 Q30 158 30 140Z" fill="#fff" stroke="#A79BD6" stroke-width="5"/>`, [46, 30, 108]],
  jin: () => [`<path d="M30 170 L56 132 H144 L170 170Z" fill="#F6C343" stroke="#D49B12" stroke-width="3"/><path d="M60 132 L78 104 H122 L140 132Z" fill="#FBD86A" stroke="#D49B12" stroke-width="3"/><g fill="#fff" opacity=".8"><path d="M150 40 l4 10 10 4 -10 4 -4 10 -4 -10 -10 -4 10 -4z"/></g>`, [44, 30, 112]],
  shi: () => [`<path d="M36 112 H164 Q160 168 100 172 Q40 168 36 112Z" fill="#fff" stroke="#E8803C" stroke-width="5"/><path d="M48 112 Q100 70 152 112Z" fill="#fff" stroke="#E8D6B8" stroke-width="3"/><g fill="#F0E2C2"><circle cx="80" cy="100" r="5"/><circle cx="100" cy="94" r="5"/><circle cx="120" cy="100" r="5"/></g>`, [48, 20, 104]],
  zhu: () => [`<g fill="#7CC264" stroke="#5A9E47" stroke-width="2"><rect x="48" y="20" width="16" height="170" rx="6"/><rect x="134" y="20" width="16" height="170" rx="6"/></g><g fill="#93D27A"><path d="M64 60 q30 -10 44 6 q-28 6 -44 -6z"/><path d="M134 90 q-30 -10 -44 6 q28 6 44 -6z"/><path d="M64 130 q24 -4 34 10 q-22 2 -34 -10z"/></g>`, [40, 40, 120]],
  cao: () => [`<path d="M0 176 H200 V200 H0Z" fill="#9BCF7A"/><g fill="#7CC264"><path d="M40 176 Q44 120 64 96 Q56 140 60 176Z"/><path d="M80 176 Q90 110 116 86 Q100 136 98 176Z"/><path d="M130 176 Q140 120 166 104 Q150 146 150 176Z"/></g>`, [40, 26, 120]],
  mian: () => [`<path d="M14 92 L100 22 L186 92 L170 104 L100 48 L30 104Z" fill="#E8695A" stroke="${BS_OL}" stroke-width="3" stroke-linejoin="round"/><rect x="44" y="96" width="112" height="84" rx="6" fill="#FFF6E6" stroke="${BS_OL}" stroke-width="3"/>`, [44, 50, 112], "#7A2E24"],
  ma: () => [`<path d="M160 120 Q190 130 186 168 Q176 146 160 140Z" fill="#6B4226"/><g stroke="#8E5A33" stroke-width="12" stroke-linecap="round"><path d="M74 140 L68 186M96 144 L98 188M138 140 L134 186M158 134 L166 184"/></g><ellipse cx="116" cy="118" rx="58" ry="34" fill="#C48A55" stroke="$${BS_OL}" stroke-width="3"/><path d="M66 110 Q52 70 36 52 Q30 40 42 34 Q60 30 76 46 Q90 66 92 100Z" fill="#C48A55" stroke="$${BS_OL}" stroke-width="3"/><path d="M40 34 Q34 22 44 18 L50 30Z" fill="#C48A55" stroke="$${BS_OL}" stroke-width="2"/><path d="M50 32 Q70 30 84 54 Q94 74 94 96 Q80 70 66 54Z" fill="#6B4226"/><circle cx="46" cy="46" r="3.5" fill="$${BS_OL}"/><ellipse cx="34" cy="56" rx="5" ry="4" fill="#A86C3C"/>`, [62, 58, 104], "#fff", "rgba(107,66,38,.85)"],
  yu2: () => [`<path d="M30 100 Q80 40 140 80 L182 54 L172 100 L182 146 L140 120 Q80 160 30 100Z" fill="#F7A55E" opacity=".6" stroke="#E07A1F" stroke-width="3"/><circle cx="56" cy="94" r="5" fill="${BS_OL}"/>`, [44, 40, 112]],
  niao: () => [`<path d="M40 90 Q50 40 100 44 Q150 46 156 96 Q170 120 186 128 Q150 138 120 150 Q60 156 40 90Z" fill="#8CCBEA" opacity=".6" stroke="#5B9BD5" stroke-width="3"/><path d="M40 72 L18 80 L40 86Z" fill="#F6B444"/><circle cx="58" cy="70" r="5" fill="${BS_OL}"/>`, [44, 40, 112]],
  quan: () => [`<path d="M150 150 Q190 130 182 96" stroke="#D9A066" stroke-width="12" stroke-linecap="round" fill="none"/><ellipse cx="104" cy="156" rx="56" ry="34" fill="#E8B77D" stroke="$${BS_OL}" stroke-width="3"/><circle cx="100" cy="86" r="52" fill="#F2C994" stroke="$${BS_OL}" stroke-width="3"/><path d="M52 60 Q34 74 40 120 Q56 112 62 84Z M148 60 Q166 74 160 120 Q144 112 138 84Z" fill="#B97A4A" stroke="$${BS_OL}" stroke-width="3"/><ellipse cx="100" cy="106" rx="22" ry="16" fill="#FFF1DC"/><ellipse cx="100" cy="98" rx="8" ry="6" fill="$${BS_OL}"/><circle cx="80" cy="80" r="5" fill="$${BS_OL}"/><circle cx="120" cy="80" r="5" fill="$${BS_OL}"/><path d="M96 116 Q100 132 108 118" fill="#F27C8A"/>`, [46, 42, 108], "#2B2B33", "rgba(255,255,255,.88)"],
  che: () => [`<rect x="20" y="70" width="160" height="60" rx="20" fill="#9CC8F0" opacity=".55"/><circle cx="56" cy="160" r="20" fill="#3B3B46"/><circle cx="56" cy="160" r="8" fill="#D9DCE6"/><circle cx="144" cy="160" r="20" fill="#3B3B46"/><circle cx="144" cy="160" r="8" fill="#D9DCE6"/>`, [40, 26, 120]],
  bei: () => [`<path d="M100 22 C160 26 186 100 160 160 Q100 190 40 160 C14 100 40 26 100 22Z" fill="#FBE3D6" stroke="#E8A98A" stroke-width="4"/><g stroke="#E8A98A" stroke-width="3" fill="none"><path d="M100 28 V176M70 36 Q60 110 64 170M130 36 Q140 110 136 170"/></g>`, [44, 38, 112]],
  wang: () => [`<path d="M30 70 L50 30 L76 58 L100 20 L124 58 L150 30 L170 70 Z" fill="#F6C343" stroke="#D49B12" stroke-width="3" stroke-linejoin="round"/><circle cx="100" cy="150" r="22" fill="#7CC6A0" opacity=".6"/>`, [40, 54, 120]],
  shi2: () => [`<path d="M0 0 H200 V40 Q150 60 120 50 L80 66 Q40 60 0 70Z" fill="#8C8D99"/><path d="M0 70 Q40 60 80 66 L60 92 Q30 96 0 92Z" fill="#A9AAB5"/><path d="M40 182 Q30 120 80 98 Q130 84 160 112 Q186 140 170 176 Q150 190 100 190 Q56 190 40 182Z" fill="#C9CAD2" stroke="#7D7E8A" stroke-width="4"/><path d="M70 120 Q90 108 112 112" stroke="#fff" stroke-width="5" stroke-linecap="round" fill="none" opacity=".8"/><ellipse cx="22" cy="186" rx="12" ry="7" fill="#B5B6C0"/><ellipse cx="184" cy="188" rx="10" ry="6" fill="#B5B6C0"/>`, [40, 36, 120], "#2B2B33", "rgba(255,255,255,.88)"],
  mi: () => [`<g fill="#fff" stroke="#E2D2A6" stroke-width="2">${[[40, 40], [160, 46], [36, 160], [164, 156], [100, 26], [100, 178], [24, 100], [176, 100]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="9" ry="6" transform="rotate(${(x + y) % 90} ${x} ${y})"/>`).join("")}</g>`, [40, 40, 120]],
  yi: () => [`<path d="M66 24 L100 40 L134 24 L176 52 L160 86 L144 78 V180 H56 V78 L40 86 L24 52Z" fill="#B5A7E6" opacity=".6" stroke="#8C7CC8" stroke-width="3" stroke-linejoin="round"/>`, [40, 40, 120]],
  zu: () => [`<path d="M78 20 Q96 20 98 50 L104 120 Q140 128 162 150 Q168 170 140 172 H68 Q54 170 58 150 L62 50 Q62 20 78 20Z" fill="#FCD9C0" stroke="#D99A7A" stroke-width="3" opacity=".8"/>`, [44, 36, 112]],
  da: () => [`<g stroke="#E8803C" stroke-width="18" stroke-linecap="round"><path d="M100 76 L22 66M100 76 L178 66"/></g><g stroke="#3E5C52" stroke-width="18" stroke-linecap="round"><path d="M100 120 L44 182M100 120 L156 182"/></g><path d="M80 64 H120 L124 124 H76Z" fill="#F7A43D" stroke="$${BS_OL}" stroke-width="3"/><circle cx="100" cy="36" r="24" fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"/><path d="M78 30 Q100 6 122 30 Q108 22 78 30Z" fill="#4A3020"/><circle cx="92" cy="38" r="3" fill="$${BS_OL}"/><circle cx="108" cy="38" r="3" fill="$${BS_OL}"/><path d="M92 46 Q100 54 108 46" stroke="$${BS_OL}" stroke-width="2.5" fill="none" stroke-linecap="round"/><circle cx="22" cy="66" r="9" fill="#FCE3D2"/><circle cx="178" cy="66" r="9" fill="#FCE3D2"/>`, [44, 50, 112], "#2B2B33", "rgba(255,255,255,.88)"],
  li: () => [`<path d="M24 186 L36 120 Q40 98 62 92 L74 64 Q72 44 84 36 Q100 28 108 44 L112 58 Q134 40 156 52 Q178 66 170 96 Q160 126 130 128 L106 126 L96 186Z" fill="#F7C6A5" stroke="#D9876A" stroke-width="5" stroke-linejoin="round"/><path d="M114 60 Q140 56 150 76" stroke="#E8A587" stroke-width="5" stroke-linecap="round" fill="none"/><g fill="#FFE27A"><path d="M160 22 l4 10 10 4 -10 4 -4 10 -4 -10 -10 -4 10 -4z"/><path d="M182 52 l3 6 6 3 -6 3 -3 6 -3 -6 -6 -3 6 -3z"/></g>`, [46, 50, 108], "#7A2E14", "rgba(255,255,255,.88)"],
  dao: () => [`<path d="M30 60 H150 Q178 62 184 96 Q186 116 168 118 H30Z" fill="#E4E9EF" stroke="#7D8A99" stroke-width="5"/><path d="M40 72 H150" stroke="#fff" stroke-width="5" stroke-linecap="round"/><rect x="2" y="78" width="44" height="26" rx="10" fill="#A0703F" stroke="$${BS_OL}" stroke-width="3"/><g fill="#E8C9A0"><circle cx="16" cy="91" r="3.5"/><circle cx="32" cy="91" r="3.5"/></g>`, [56, 40, 108], "#2B2B33"],
  he: () => [`<path d="M100 186 V40" stroke="#C9A43C" stroke-width="5"/><path d="M100 40 Q130 34 150 60 Q160 80 150 96" stroke="#E2B93B" stroke-width="10" stroke-linecap="round" fill="none"/><g fill="#F2D06A">${[0, 1, 2, 3].map(i => `<ellipse cx="${140 + i * 4}" cy="${56 + i * 12}" rx="6" ry="4"/>`).join("")}</g>`, [40, 46, 120]],
  er: () => [`<path d="M78 22 Q156 14 168 86 Q174 140 132 168 Q108 184 92 172 Q78 158 92 140 Q112 124 120 104 Q128 74 106 62 Q84 54 70 74 Q58 50 78 22Z" fill="#FCD0B4" stroke="#D9876A" stroke-width="5"/><path d="M98 40 Q144 40 148 90 Q150 120 124 142" stroke="#E8A587" stroke-width="7" stroke-linecap="round" fill="none"/>`, [44, 40, 112], "#2B2B33", "rgba(255,255,255,.88)"],
  zou: () => [`<path d="M0 174 H200 V200 H0Z" fill="#B9D59C"/><g stroke="#9CC07A" stroke-width="4" stroke-linecap="round"><path d="M14 92 H44M8 112 H38M18 132 H46"/></g><circle cx="112" cy="40" r="20" fill="#FCE3D2" stroke="$${BS_OL}" stroke-width="3"/><path d="M96 30 Q112 12 130 30 Q118 24 96 30Z" fill="#4A3020"/><g stroke="#3E7C6A" stroke-width="14" stroke-linecap="round" fill="none"><path d="M110 62 L100 110"/><path d="M106 72 L80 92 M106 72 L138 84"/></g><g stroke="#3E5C52" stroke-width="13" stroke-linecap="round" fill="none"><path d="M100 110 L70 140 L52 136"/><path d="M100 110 L128 142 L134 172"/></g>`, [44, 44, 112], "#2B2B33", "rgba(255,255,255,.88)"]
};
function bsCard(r, big){
  const [id, ch, , , , , bg] = r, a = BS_ART[id] ? BS_ART[id]() : ["", [40, 40, 120]], [x, y, s] = a[1], col = a[2] || "#2B2B33", halo = a[3] || "";
  return `<svg class="bs-svg" viewBox="0 0 200 200" role="img" aria-label="${ch}"><rect width="200" height="200" rx="${big ? 18 : 22}" fill="${bg}"/>${a[0]}${bsGlyph(ch, x, y, s, col, 1, halo)}</svg>`;
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
