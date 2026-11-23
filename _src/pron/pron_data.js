/* Luyện ngữ âm – 5 câu chính mỗi bài (từ mới lấy thẳng từ les.vocab) */
const PRON_SENT = {
  hsk1: {
    1: [["王老师，你好！","Wáng lǎoshī, nǐ hǎo!","Chào cô Vương!"],["大家好！","Dàjiā hǎo!","Chào cả lớp!"],["老师，您好！","Lǎoshī, nín hǎo!","Chào cô ạ!"],["谢谢！——不客气！","Xièxie! — Bú kèqi!","Cảm ơn! — Đừng khách sáo!"],["同学们，再见！","Tóngxuémen, zàijiàn!","Tạm biệt các em!"]],
    2: [["请问，你叫什么名字？","Qǐngwèn, nǐ jiào shénme míngzi?","Xin hỏi, bạn tên là gì?"],["我叫李文。","Wǒ jiào Lǐ Wén.","Mình tên là Lý Văn."],["我不是安妮，我是白家月。","Wǒ bú shì Ānnī, wǒ shì Bái Jiāyuè.","Mình không phải là Annie, mình là Bạch Gia Nguyệt."],["对不起！——没关系！","Duìbuqǐ! — Méi guānxi!","Xin lỗi! — Không sao đâu!"],["很高兴认识你。","Hěn gāoxìng rènshi nǐ.","Rất vui được làm quen với bạn."]],
    3: [["我是中国人。","Wǒ shì Zhōngguó rén.","Mình là người Trung Quốc."],["这是谁？","Zhè shì shéi?","Đây là ai vậy?"],["你女朋友是哪国人？","Nǐ nǚpéngyou shì nǎ guó rén?","Bạn gái của bạn là người nước nào?"],["你工作还忙吗？","Nǐ gōngzuò hái máng ma?","Công việc của em vẫn bận lắm à?"],["我不太忙。我们很想你。","Wǒ bú tài máng. Wǒmen hěn xiǎng nǐ.","Chị không bận lắm. Mọi người đều rất nhớ em."]],
    4: [["她有多少个学生？","Tā yǒu duōshao ge xuésheng?","Dì ấy có bao nhiêu học sinh?"],["你家有几口人？","Nǐ jiā yǒu jǐ kǒu rén?","Nhà em có mấy người?"],["我家有四口人，爸爸、妈妈、妹妹和我。","Wǒ jiā yǒu sì kǒu rén, bàba, māma, mèimei hé wǒ.","Nhà em có bốn người: bố, mẹ, em gái và em."],["我有两个孩子，一个儿子，一个女儿。","Wǒ yǒu liǎng ge háizi, yí ge érzi, yí ge nǚ'ér.","Chị có hai con, một con trai và một con gái."],["您女儿多大？","Nín nǚ'ér duō dà?","Con gái chị bao nhiêu tuổi?"]],
    5: [["今天几号？","Jīntiān jǐ hào?","Hôm nay ngày mấy?"],["今天9月8号，星期日。","Jīntiān jiǔ yuè bā hào, xīngqīrì.","Hôm nay là ngày 8 tháng 9, Chủ nhật."],["你会做饭吗？","Nǐ huì zuò fàn ma?","Em có biết nấu ăn không?"],["这是你的新电脑吗？","Zhè shì nǐ de xīn diànnǎo ma?","Đây là máy tính mới của em à?"],["我也很喜欢它。","Wǒ yě hěn xǐhuan tā.","Em cũng rất thích nó."]]
  },
  gt1: {
    1: [["你好！","Nǐ hǎo!","Chào bạn!"],["您好！","Nín hǎo!","Em chào thầy ạ!"],["你们好！","Nǐmen hǎo!","Chào các bạn!"],["老师好！","Lǎoshī hǎo!","Em chào thầy/cô ạ!"],["零、一、二、五、八","líng, yī, èr, wǔ, bā","không, một, hai, năm, tám"]],
    2: [["早上好！","Zǎoshang hǎo!","Chào buổi sáng!"],["你是哪国人？","Nǐ shì nǎ guó rén?","Bạn là người nước nào?"],["我是美国人。你呢？","Wǒ shì Měiguó rén. Nǐ ne?","Mình là người Mỹ. Còn bạn?"],["他是日本人。","Tā shì Rìběn rén.","Anh ấy là người Nhật Bản."],["我是越南人。","Wǒ shì Yuènán rén.","Tôi là người Việt Nam."]],
    3: [["请问，你叫什么名字？","Qǐngwèn, nǐ jiào shénme míngzi?","Xin hỏi bạn tên là gì?"],["我叫林娜。你呢？","Wǒ jiào Línnà. Nǐ ne?","Mình tên là Linna. Còn bạn?"],["认识你很高兴。","Rènshi nǐ hěn gāoxìng.","Rất vui được làm quen với bạn."],["老师，您贵姓？","Lǎoshī, nín guìxìng?","Thưa thầy, thầy họ gì ạ?"],["我姓李。","Wǒ xìng Lǐ.","Thầy họ Lý."]],
    4: [["林娜是法国留学生，她学习汉语。","Línnà shì Fǎguó liúxuéshēng, tā xuéxí Hànyǔ.","Linna là du học sinh người Pháp, cô ấy học tiếng Trung."],["他们一起上课，一起说汉语。","Tāmen yìqǐ shàngkè, yìqǐ shuō Hànyǔ.","Họ cùng lên lớp, cùng nói tiếng Trung."],["你学习法语吗？","Nǐ xuéxí Fǎyǔ ma?","Bạn có học tiếng Pháp không?"],["林娜，他是谁？","Línnà, tā shì shéi?","Linna, anh ấy là ai?"],["他是我同学。","Tā shì wǒ tóngxué.","Anh ấy là bạn cùng lớp của mình."]],
    5: [["你家有几口人？","Nǐ jiā yǒu jǐ kǒu rén?","Nhà bạn có mấy người?"],["我家有四口人：爸爸、妈妈、哥哥和我。","Wǒ jiā yǒu sì kǒu rén: bàba, māma, gēge hé wǒ.","Nhà tôi có bốn người: bố, mẹ, anh trai và tôi."],["你爸爸、妈妈做什么工作？","Nǐ bàba, māma zuò shénme gōngzuò?","Bố mẹ bạn làm nghề gì?"],["我爸爸是律师，妈妈是医生。","Wǒ bàba shì lǜshī, māma shì yīshēng.","Bố mình là luật sư, mẹ là bác sĩ."],["你们班有多少个学生？","Nǐmen bān yǒu duōshao ge xuésheng?","Lớp bạn có bao nhiêu học sinh?"]]
  }
};
const PRON_PRESETS = [
  "Phát âm chuẩn, rất tốt! 👍",
  "Câu đọc trôi chảy, ngữ điệu tự nhiên. Tốt lắm!",
  "Thanh điệu chưa đúng, em nghe lại audio mẫu rồi luyện thêm nhé.",
  "Chú ý thanh 3: hạ thấp giọng rồi mới lên. Em đọc lại nhé.",
  "Chú ý biến điệu: hai thanh 3 đi liền thì chữ đầu đọc thành thanh 2.",
  "Chú ý phân biệt zh / ch / sh với z / c / s.",
  "Chú ý âm cuối -n và -ng.",
  "Âm ü cần tròn môi hơn, em luyện thêm nhé.",
  "Đọc to và rõ hơn một chút nhé.",
  "Tốc độ hơi nhanh, em đọc chậm lại cho rõ từng âm.",
  "File ghi âm bị nhỏ/rè, cô nghe chưa rõ. Em ghi âm lại giúp cô nhé."
];
