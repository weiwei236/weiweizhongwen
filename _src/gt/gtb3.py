# -*- coding: utf-8 -*-
# 发展汉语·初级综合(II) – Bài 5, 6
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[5] = dict(zh="为什么我一个人站着吃", en="Why Do I Stand by Myself While Eating", vi="Tại sao chỉ mình tôi đứng ăn",
intro="Cả nhà Tiểu Vương đều quý cô con dâu ngoại quốc Debby. Bố mẹ chồng ngày nào cũng nấu món ngon cho cô, Tiểu Vương ngày nào cũng đưa cô đi tham quan khắp nơi. Thế mà một hôm, đang ăn cơm Debby lại nổi giận. Vì sao vậy?",
vocab=V("""
娶|qǔ|dong|lấy (vợ), cưới (vợ)
洋|yáng|tt|tây, ngoại quốc
媳妇|xífù|dt|con dâu; vợ
饭菜|fàncài|dt|cơm canh, bữa ăn
游览|yóulǎn|dong|du ngoạn, tham quan
皇帝|huángdì|dt|hoàng đế
妻子|qīzi|dt|vợ
开玩笑|kāi wánxiào|cum|đùa, nói đùa
选中|xuǎn zhòng|cum|chọn trúng, chọn được
尊重|zūnzhòng|dong|tôn trọng
妇女|fùnǚ|dt|phụ nữ
改|gǎi|dong|đổi, sửa
式|shì|dt|kiểu
早餐|zǎocān|dt|bữa sáng
豆浆|dòujiāng|dt|sữa đậu nành
油条|yóutiáo|dt|quẩy (bánh quẩy)
不得了|bù déliǎo|cum|vô cùng, cực kỳ
噎|yē|dong|nghẹn
指|zhǐ|dong|chỉ (tay)
蘸|zhàn|dong|chấm (vào nước chấm)
吃惊|chī jīng|dong|ngạc nhiên, giật mình
婆婆|pópo|dt|mẹ chồng
公公|gōnggong|dt|bố chồng
骗人|piàn rén|dong|lừa người, nói dối
黛比|Dàibǐ|rieng|Debby (tên người)
"""),
texts=[dict(t="为什么我一个人站着吃", narr=True, lines=T("""
小王娶了一个漂亮的美国姑娘，名字叫黛比。|Tiểu Vương cưới một cô gái Mỹ xinh đẹp, tên là Debby.
今年春节，小王带着她回到了北京。|Tết năm nay, Tiểu Vương đưa cô về Bắc Kinh.
小王的父母特别喜欢这个“洋媳妇”，每天都给她做好吃的饭菜。|Bố mẹ Tiểu Vương đặc biệt quý cô “con dâu Tây” này, ngày nào cũng nấu món ngon cho cô.
小王每天陪着黛比到处参观。|Ngày nào Tiểu Vương cũng đưa Debby đi tham quan khắp nơi.
游览故宫的时候，黛比说：“中国的皇帝真奇怪，娶那么多的妻子，多麻烦！”|Khi thăm Cố Cung, Debby nói: “Hoàng đế Trung Quốc lạ thật, lấy nhiều vợ như thế, phiền biết bao!”
小王开玩笑说：“要是一百年前你来到中国，中国的皇帝选中了你，你不愿意，怎么办？”|Tiểu Vương đùa: “Nếu một trăm năm trước em đến Trung Quốc, hoàng đế chọn trúng em mà em không muốn thì làm sao?”
黛比笑着说：“那好办。要是我不愿意，就回美国去。”|Debby cười nói: “Dễ thôi. Nếu em không muốn thì về Mỹ.”
“那你可就回不去了，这个大院子里的女人是没有自由的。|“Thế thì em không về được đâu, phụ nữ trong cái sân lớn này không có tự do.
不过，现在你什么也不用怕，中国很尊重妇女，女人结婚以后都不用改姓。”|Nhưng bây giờ em chẳng phải sợ gì cả, Trung Quốc rất tôn trọng phụ nữ, phụ nữ lấy chồng rồi cũng không phải đổi họ.”
第二天早晨，小王全家吃中国式早餐——豆浆、油条。|Sáng hôm sau, cả nhà Tiểu Vương ăn bữa sáng kiểu Trung Quốc – sữa đậu nành, bánh quẩy.
黛比第一次吃油条，喜欢得不得了，拿起油条大口大口地吃起来。|Lần đầu Debby ăn quẩy, thích vô cùng, cầm quẩy lên ăn từng miếng to.
小王怕她噎着，就指着豆浆碗说：“蘸着吃。”|Tiểu Vương sợ cô bị nghẹn, liền chỉ vào bát sữa đậu nành nói: “Chấm mà ăn.”
黛比吃惊地看着小王，不懂他说的是什么意思。|Debby ngạc nhiên nhìn Tiểu Vương, không hiểu anh nói gì.
婆婆也笑着说：“蘸着吃。”|Mẹ chồng cũng cười nói: “Chấm mà ăn.”
公公也说：“对，蘸着吃。”|Bố chồng cũng nói: “Đúng, chấm mà ăn.”
小王的弟弟也说：“是啊，应该蘸着吃。”|Em trai Tiểu Vương cũng nói: “Đúng đấy, nên chấm mà ăn.”
黛比在美国学过汉语，听力不错，所以跟小王家人交流没问题，可是现在她却不明白大家的意思了。|Debby đã học tiếng Hán ở Mỹ, nghe khá tốt, nên nói chuyện với nhà Tiểu Vương không vấn đề gì, vậy mà bây giờ cô lại không hiểu ý mọi người.
“蘸着吃，好吃。”小王又说了一遍。|“Chấm mà ăn, ngon lắm.” Tiểu Vương nói lại lần nữa.
黛比拿着油条慢慢地站了起来，生气地对小王说：|Debby cầm quẩy từ từ đứng dậy, giận dỗi nói với Tiểu Vương:
“你，你还说中国尊重妇女呢，骗人。你们都坐着吃，为什么我一个人站着吃？”|“Anh, anh còn bảo Trung Quốc tôn trọng phụ nữ, nói dối. Mọi người đều ngồi ăn, sao chỉ mình em phải đứng ăn?”
"""), q=Q("""
请介绍一下黛比。|黛比是美国姑娘，是小王的妻子，在美国学过汉语。|Debby là cô gái Mỹ, vợ Tiểu Vương, từng học tiếng Hán ở Mỹ.
小王的父母喜欢黛比吗？怎么知道的呢？|特别喜欢，每天都给她做好吃的饭菜。|Rất quý, ngày nào cũng nấu món ngon cho cô.
为什么黛比说中国的皇帝奇怪？|因为皇帝娶那么多的妻子。|Vì hoàng đế lấy rất nhiều vợ.
为什么说如果黛比被选中了就回不去了？|因为大院子里的女人是没有自由的。|Vì phụ nữ trong cung không có tự do.
为什么说中国现在的妇女受尊重？|女人结婚以后都不用改姓。|Phụ nữ lấy chồng không phải đổi họ.
黛比喜欢吃油条吗？她怎么吃油条？|喜欢得不得了，大口大口地吃。|Thích vô cùng, ăn từng miếng to.
小王为什么告诉黛比“蘸着吃”？|因为他怕黛比噎着。|Vì sợ Debby bị nghẹn.
黛比为什么吃惊地看着小王？|因为她不懂小王说的是什么意思。|Vì cô không hiểu ý Tiểu Vương.
黛比为什么说小王骗人？|她把“蘸着吃”听成了“站着吃”，觉得大家都坐着吃，只有她一个人站着吃。|Cô nghe nhầm “chấm mà ăn” thành “đứng mà ăn”.
"""))],
grammar=[
 G("v1zhe_v2", "为什么我一个人站着吃？", "V1 + 着 + V2: vừa… vừa… / làm V2 trong trạng thái V1",
   "Hai hành động cùng diễn ra; V1 là cách thức hoặc trạng thái đi kèm của V2.",
   [F("S:Chủ ngữ|V1:V1|kw:着|V2:V2 (+O)", [
      ("我喜欢|听|[着]|音乐开车", "。", "Tôi thích vừa nghe nhạc vừa lái xe."),
      ("她|拿|[着]|伞走了", "。", "Cô ấy cầm ô đi rồi."),
      ("没有公共汽车了，只好|走|[着]|回家", "。", "Hết xe buýt rồi, đành đi bộ về nhà."),
      ("你们都|坐|[着]|吃", "。", "Mọi người đều ngồi ăn.")])],
   prac=["A:她怎么说的？\nB:她{笑}着说：“我找到工作了！”", "A:你喜欢怎么看书？\nB:我喜欢{躺}着看书，那样很舒服。", "A:今天太热了。\nB:{开}着窗户睡觉吧。"]),
 G("yiwen_dou", "现在你什么也不用怕。", "Từ nghi vấn + 也/都: chỉ “bất kỳ”",
   "Từ nghi vấn (什么、谁、哪儿、什么时候…) đứng trước 也/都 mang nghĩa “bất cứ… nào”. 都 dùng cả câu khẳng định và phủ định; 也 thường chỉ dùng trong câu phủ định.",
   [F("S:Chủ ngữ|Q:Từ nghi vấn (+N)|kw:也/都|V:Vị ngữ", [
      ("他|什么爱好|[也]|没有", "。", "Anh ấy chẳng có sở thích gì cả."),
      ("他是有名的歌手，|谁|[都]|认识他", "。", "Anh ấy là ca sĩ nổi tiếng, ai cũng biết."),
      ("星期天，我|哪儿|[都]|不去", "。", "Chủ nhật tôi chẳng đi đâu cả."),
      ("你|什么时候来|[都]|可以", "。", "Bạn đến lúc nào cũng được.")])],
   notes=["我哪儿都想去。(khẳng định – chỉ dùng 都)", "我哪儿都不想去。= 我哪儿也不想去。"],
   prac=["A:我们今天去哪儿？\nB:{去哪儿都可以}，我跟着你走。", "A:你们两个谁想和我一起去看电影？\nB:我们都很忙，{谁都不想去}。", "A:你喜欢哪件衣服？\nB:这些衣服都很漂亮，{哪件我都喜欢}。"]),
 G("buliao_haishuo", "黛比第一次吃油条，喜欢得不得了。", "Từ ngữ: 娶/嫁 · 洋 · 开玩笑 · 中(zhòng) · 不得了 · 还说……呢",
   "Một số từ ngữ trong bài khóa.",
   notes=["娶 (nam lấy vợ) / 嫁 (nữ lấy chồng): 他娶了一个漂亮姑娘。/ 她嫁给了一个外国人。",
          "洋: đến từ nước ngoài – 洋酒 rượu Tây, 洋葱 hành tây, 洋白菜 bắp cải.",
          "开玩笑: nói đùa – 我跟你开玩笑呢，你别生气。",
          "中 (zhòng): trúng, vừa đúng – 别的我都不喜欢，我就看中了那个红色的。/ 你猜中了。",
          "不得了: cực kỳ (đặt sau 得) – 今天冷得不得了。/ 他急得不得了，可是又没办法。",
          "还说……呢: khẩu ngữ, lời nói trái với sự thật – 你还说这儿不热呢，我都快热死了。"]),
],
ex=[
 pick("一、给“中”字注音", "Chữ “中” trong mỗi câu đọc là zhōng hay zhòng?", [
   (["zhōng", "zhòng"], ["今天去商店，我看【zhòng】了一件红色的毛衣。（看中）", "她是我们同学【zhōng】最漂亮的一个。（同学中）", "公司选【zhòng】了我，到中国公费留学。（选中）", "他在年轻人【zhōng】很受欢迎。（年轻人中）"])]),
 pool("二、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["游览", "开玩笑", "选中", "愿意", "自由", "改", "不得了", "吃惊", "交流", "骗人", "尊重"], [
   "我已经可以和同学们用汉语【交流】了。", "他说的是真的，没有【骗人】。", "听到这个消息，我很【吃惊】。", "如果你【愿意】，我【尊重】你的选择。",
   "学校真的【选中】了我？你不是在跟我【开玩笑】吧？", "听到这个好消息，他高兴得【不得了】。", "这个汉字写得不对，我【改】一下。", "放假了，我们现在【自由】了，可以去旅行了。", "我【游览】过故宫。"], inline=False),
 pick("三、选择意思相近的词语填空", "Chọn từ thích hợp (từ gần nghĩa).", [
   (["游览", "旅行"], ["我想和朋友一起去【游览】长城。", "他是个特别喜欢【旅行】的人。"]),
   (["麻烦", "难"], ["我的护照丢了，现在很【麻烦】。", "汉语的四声有点儿【难】，我总是说错。"]),
   (["愿意", "想"], ["如果你【愿意】帮忙，我很高兴。", "你【想】什么时候去旅行？"])]),
 match("四、连句", "Nối vế bên trái với vế bên phải thành câu.", ["这件事有点儿麻烦。", "又怕太麻烦你。", "因为你的发音像英国人一样。", "又不便宜。", "跟中国人交流没问题。", "累得不得了。"],
   [("走了一天，", "累得不得了。"), ("我想请你帮助我，", "又怕太麻烦你。"), ("跟旅行团游览既不自由，", "又不便宜。"), ("我听了你说的英语很吃惊，", "因为你的发音像英国人一样。"),
    ("他的听说能力很好，", "跟中国人交流没问题。"), ("有的要去，有的不去，", "这件事有点儿麻烦。")]),
 opn("五、用所给的词语或格式改写句子", "Viết lại câu với từ/cấu trúc cho sẵn. Ví dụ: 一边走一边吃东西不好。→ 走着吃东西不好。", [
   ("查词典需要很长时间。（麻烦）", "查词典很麻烦。"), ("他有困难了，我们应该帮助他。（麻烦）", "他遇到麻烦了，我们应该帮助他。"),
   ("今天非常忙。（不得了）", "今天忙得不得了。"), ("我们一边喝咖啡，一边聊天儿。（V1+着+V2）", "我们喝着咖啡聊天儿。"),
   ("我们班的同学上课都不迟到。（谁都）", "我们班的同学上课谁都不迟到。"), ("这里好玩儿的地方，我都去过了。（哪儿都）", "这里好玩儿的地方，我哪儿都去过了。"),
   ("你对哪一种颜色最满意？（选中）", "你选中了哪一种颜色？")]),
 opn("六、用“V1+着+V2”结构和所给的动词造句", "Đặt câu với V1 + 着 + V2.", [
   ("唱　洗", "他每天唱着歌洗衣服。"), ("走　回家", "没有车了，我们走着回家吧。"), ("骑　上学", "我每天骑着自行车上学。"), ("站　讲课", "老师站着讲课。")]),
 opn("七、情境表达", "Câu nào dùng trong tình huống nào; tình huống sau nên nói thế nào?", [
   ("“你还说这里的东西便宜呢！”“他的汉语真不得了！说得太好了！”——在什么情况下可以说？", "朋友说这里的东西便宜，可是其实很贵的时候；听到别人汉语说得非常好的时候。"),
   ("你表示喜欢去对方的公司工作，怎么说？（愿意）", "我很愿意去你们公司工作。"),
   ("你说了什么话，对方不高兴了，该怎么解释才能让他别生气？（开玩笑）", "对不起，我是跟你开玩笑的，你别生气。"),
   ("朋友问你去哪儿吃饭，你表示听他的。（哪儿都）", "去哪儿都可以，听你的。")]),
 opn("八、根据课文内容，用所给词语完成对话", "Hoàn thành hội thoại theo bài khóa.", [
   ("小王：我的父母太喜欢你了，每天______。\n黛比：那你呢？你喜欢我吗？\n小王：我喜欢你喜欢得______，你看，我每天都______。（不得了　游览）", "每天都给你做好吃的饭菜 / 不得了 / 陪着你到处游览"),
   ("黛比：中国的皇帝真奇怪，娶那么多妻子，______！（麻烦）\n小王：对了，要是一百年前你来到中国，______？（选中）", "多麻烦 / 皇帝选中了你，你怎么办"),
   ("黛比：那好办，要是______，就回美国去。（愿意）\n小王：那时候，故宫里的女人是______。不过现在就不一样了，中国很______。（自由　尊重）", "我不愿意 / 没有自由的 / 尊重妇女"),
   ("黛比：中国怎么尊重妇女的？\n小王：女人现在很自由，结婚______。（改）\n黛比：那为什么吃油条的时候，你们都坐着吃，______？（站）", "以后都不用改姓 / 为什么我一个人站着吃")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("“我”有两个儿子，一个女儿。", True), ("大儿子在家的时候，喜欢一边唱歌一边做事。", True), ("二儿子是大学生。", True), ("女儿常常撞到树上。", False)],
   passage="我有三个孩子。大儿子是工人，特别喜欢音乐。在家的时候，他总是唱着歌做事。他唱着歌洗衣服，唱着歌帮妈妈做饭，唱着歌给弟弟、妹妹打扫房间。他真是个好孩子，不但自己快乐，也给别人快乐。\n二儿子很聪明。他常常一边看电视一边写作业，一边听音乐一边复习功课。现在他一边上大学一边打工。可是，我不喜欢他一边开车一边打电话，这样太危险（wēixiǎn）了。\n小女儿特别喜欢看书。她坐着看书，站着看书，躺着看书，走着看书，上厕所的时候也看书。她的学习成绩是全班最好的，可是她的眼睛却越来越不好了。有一次，她一边走一边看书，撞到了树上，还对树说“对不起”。"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("“我”为什么说大儿子是个好孩子？", "因为他不但自己快乐，也给别人快乐。"),
   ("“我”为什么经常为二儿子担心？", "因为他一边开车一边打电话，太危险了。"),
   ("小女儿是个怎样的人？", "她特别喜欢看书，学习成绩是全班最好的，可是眼睛越来越不好了。"),
   ("给本文加一个题目。", "我的三个孩子")]),
 opn("十、说一说，写一写", "Viết đoạn văn ít nhất 60 chữ.", [
   ("你经常和别人用汉语交流吗？你在交流中觉得哪方面问题比较多？你在和别人用汉语交流时，发生过什么有意思的误会？请举例说明。",
    "（参考）我经常和中国朋友用汉语交流。我觉得听力问题比较多，因为中国人说话很快。有一次，朋友说“我请客”，我以为他要请很多客人，其实他的意思是他付钱。大家都笑了，我也笑得不得了。")]),
])

B[6] = dict(zh="我这里一切都好", en="Everything Is Fine Here", vi="Ở đây mọi thứ đều tốt",
intro="Đây là hai bức thư điện tử giữa một du học sinh và người mẹ ở quê nhà xa xôi. Học xong bài này, có lẽ bạn cũng sẽ gửi cho bố mẹ một email báo bình an.",
vocab=V("""
一切|yíqiè|dai|tất cả, mọi thứ
电子邮箱|diànzǐ yóuxiāng|dt|hộp thư điện tử
极了|jí le|cum|cực kỳ (đặt sau tính từ)
情况|qíngkuàng|dt|tình hình
网络|wǎngluò|dt|mạng (internet)
好像|hǎoxiàng|dong|hình như, dường như
放心|fàng xīn|dong|yên tâm
惯|guàn|dong|quen
可惜|kěxī|tt|tiếc, đáng tiếc
发|fā|dong|gửi (thư, email)
祝|zhù|dong|chúc
笑脸|xiàoliǎn|dt|khuôn mặt tươi cười
声音|shēngyīn|dt|giọng nói, âm thanh
闻|wén|dong|ngửi
香味|xiāngwèi|dt|mùi thơm
家乡|jiāxiāng|dt|quê hương
炒|chǎo|dong|xào
搬|bān|dong|chuyển, dọn (nhà)
秘密|mìmì|dt|bí mật
聪明|cōngming|tt|thông minh
健康|jiànkāng|tt|khỏe mạnh
"""),
texts=[dict(t="妈妈的邮件", narr=True, lines=T("""
马克：|Mark con:
每天早上一起床，就先上网打开电子邮箱，看看有没有你的新邮件，这成了我和你爸爸的习惯。|Mỗi sáng vừa dậy là lên mạng mở hộp thư xem có thư mới của con không, việc này đã thành thói quen của mẹ và bố con.
收到你的电子邮件，我们高兴极了。|Nhận được email của con, bố mẹ vui lắm.
能这么快地知道你那里的情况，真得好好儿感谢电脑和网络。|Biết được tình hình bên con nhanh như vậy, thật phải cảm ơn máy tính và internet.
不过，最近你的电子邮件好像越来越少，也越写越短了，为什么呢？|Nhưng gần đây hình như email của con ngày càng ít, càng viết càng ngắn, vì sao thế?
虽然你已经不是小孩子了，可是妈妈还是对你有点儿不放心。|Tuy con không còn là trẻ con nữa, nhưng mẹ vẫn hơi không yên tâm về con.
你最近身体怎么样？老师讲课你听得懂吗？中国菜吃得惯吗？|Dạo này con khỏe không? Thầy cô giảng bài con nghe có hiểu không? Ăn món Trung Quốc có quen không?
妈妈有很多话要和你说，可惜我的眼睛越来越不好，不能写得太长。|Mẹ có nhiều điều muốn nói với con, tiếc là mắt mẹ ngày càng kém, không viết dài được.
我和你爸爸都很好，别担心。有空儿常给我们发电子邮件。|Bố mẹ đều khỏe, con đừng lo. Có thời gian thì thường xuyên gửi email cho bố mẹ nhé.
祝你快乐！ 妈妈 2011年10月5日|Chúc con vui vẻ! Mẹ, ngày 5 tháng 10 năm 2011
""")), dict(t="马克的回信", narr=True, lines=T("""
亲爱的妈妈：|Mẹ yêu quý:
每次看到您的电子邮件，都好像看到了您的笑脸，听到了您的声音，闻到了您做的饭菜的香味儿。|Mỗi lần đọc email của mẹ, con như thấy nụ cười của mẹ, nghe thấy giọng mẹ, ngửi thấy mùi thơm món ăn mẹ nấu.
我有点儿想家了，想您和爸爸，想家里舒服的床，想家乡的咖啡馆，想那些常常在一起一边喝咖啡一边聊天儿的好朋友……|Con hơi nhớ nhà rồi, nhớ bố mẹ, nhớ chiếc giường êm ở nhà, nhớ quán cà phê ở quê, nhớ những người bạn thân thường cùng vừa uống cà phê vừa trò chuyện…
我这里的一切都很好，别为我担心。|Ở đây mọi thứ đều tốt, mẹ đừng lo cho con.
我现在已经吃惯了中国菜，还跟朋友学会了做中国菜呢，我做的西红柿炒鸡蛋好吃极了。|Giờ con đã ăn quen món Trung Quốc, còn học bạn nấu được món Trung nữa, món trứng xào cà chua con nấu ngon cực kỳ.
现在我住的地方离学校有点儿远，所以我和我的同屋打算搬到学校附近去住，这样我们早晨就可以晚一点儿起床了。|Chỗ con ở bây giờ hơi xa trường, nên con và bạn cùng phòng định chuyển đến gần trường, như vậy buổi sáng có thể dậy muộn hơn một chút.
我的汉语进步了，上课的时候，老师说的话我都听得懂。|Tiếng Hán của con tiến bộ rồi, trong giờ học thầy cô nói gì con cũng nghe hiểu.
不过到了街上，中国人说的话我还是听不懂。|Nhưng ra đường thì con vẫn nghe không hiểu người Trung Quốc nói.
告诉您一个秘密，我们班有一个韩国姑娘，我喜欢她，她也喜欢我。|Kể mẹ nghe một bí mật: lớp con có một cô gái Hàn Quốc, con thích cô ấy, cô ấy cũng thích con.
她又漂亮又聪明，我想您也一定会喜欢她的。|Cô ấy vừa xinh vừa thông minh, con nghĩ mẹ nhất định cũng sẽ thích cô ấy.
对不起，最近我的邮件越写越短，因为我真的太忙了。|Xin lỗi mẹ, dạo này thư con càng viết càng ngắn, vì con thật sự quá bận.
这个假期我回不去了，我得努力学习。|Kỳ nghỉ này con không về được, con phải chăm chỉ học.
祝您和爸爸身体健康！ 马克 2011年10月6日|Chúc bố mẹ mạnh khỏe! Mark, ngày 6 tháng 10 năm 2011
"""), q=Q("""
马克的父母每天早上起床先做什么？|先上网打开电子邮箱，看看有没有马克的新邮件。|Lên mạng mở hộp thư xem có thư mới của Mark không.
妈妈为什么说要感谢电脑和网络？|因为能这么快地知道马克那里的情况。|Vì biết được tình hình của Mark rất nhanh.
马克最近的邮件和以前有什么不一样？|越来越少，也越写越短了。|Ngày càng ít và càng ngắn.
妈妈想知道马克的哪些情况？|身体怎么样，老师讲课听得懂吗，中国菜吃得惯吗。|Sức khỏe, nghe giảng có hiểu không, ăn có quen không.
妈妈的电子邮件写得长吗？为什么？|不长，因为她的眼睛越来越不好。|Không dài, vì mắt mẹ ngày càng kém.
马克都想念家乡的什么？|想爸爸妈妈，想家里舒服的床、家乡的咖啡馆和好朋友。|Nhớ bố mẹ, giường ở nhà, quán cà phê, bạn bè.
马克会做什么菜？他觉得自己做得怎么样？|西红柿炒鸡蛋，他觉得好吃极了。|Trứng xào cà chua, ngon cực kỳ.
马克为什么要搬家？|因为住的地方离学校有点儿远。|Vì chỗ ở hơi xa trường.
马克的汉语学得怎么样了？|进步了，上课听得懂，可是街上中国人说的话还是听不懂。|Tiến bộ, trên lớp nghe hiểu, ngoài đường vẫn chưa.
马克的秘密是什么？|他喜欢班里的一个韩国姑娘，她也喜欢他。|Anh thích một cô gái Hàn Quốc trong lớp.
马克假期为什么不回家了？|因为他得努力学习。|Vì phải chăm chỉ học.
"""))],
grammar=[
 G("yue_a_yue_b", "你的电子邮件越写越短了。", "越 A 越 B: càng A càng B",
   "B thay đổi theo sự thay đổi của A. (1) A và B cùng chủ ngữ; (2) A và B khác chủ ngữ.",
   [F("S:Chủ ngữ|kw:越|A:A|kw2:越|B:B", [
      ("雨|[越]|下|[越]|大", "。", "Mưa càng lúc càng to."),
      ("汉语|[越]|学|[越]|有意思", "。", "Tiếng Hán càng học càng thú vị."),
      ("东西不是|[越]|便宜|[越]|好", "。", "Đồ không phải càng rẻ càng tốt.")], cap="Cùng chủ ngữ"),
    F("S:Chủ ngữ 1|kw:越|A:A|S2:Chủ ngữ 2|kw2:越|B:B", [
      ("他|[越]|说，|我|[越]|不懂", "。", "Anh ấy càng nói tôi càng không hiểu."),
      ("老师|[越]|表扬学生，|学生就|[越]|努力", "。", "Thầy càng khen học sinh, học sinh càng cố gắng.")], cap="Khác chủ ngữ")],
   prac=["A:什么样的苹果好吃？\nB:{越红越好吃}。", "A:你喜欢汉语吗？\nB:{越学越喜欢}。", "A:我什么时候去你那儿好呢？\nB:{越早越好}。", "A:你听听家乡的音乐就不想家了吧？\nB:{越听越想家}。"]),
 G("kenengbuyu", "老师讲课你听得懂吗？", "V + 得/不 + bổ ngữ kết quả/xu hướng (bổ ngữ khả năng)",
   "Diễn tả có thể (得) hay không thể (不) đạt được kết quả. Chủ yếu dùng dạng phủ định; dạng khẳng định thường dùng trong câu hỏi.",
   [F("S:Chủ ngữ|V:Động từ|kw:得/不|B:Bổ ngữ|O:Phần còn lại", [
      ("你看|看|[得]|懂|中文小说吗", "？", "Bạn đọc hiểu được tiểu thuyết tiếng Trung không?"),
      ("太多了，我|写|[不]|完|", "。", "Nhiều quá, tôi viết không xong."),
      ("那个公园没有票|进|[得]|去|吗", "？", "Công viên đó không có vé có vào được không?"),
      ("这个假期我|回|[不]|去|了", "。", "Kỳ nghỉ này tôi không về được rồi.")])],
   prac=["A:房间里没有卫生间，你{住得惯}吗？\nB:我住这儿半年多了，已经习惯了。", "A:你离黑板那么远，{看得见吗}？\nB:我的眼睛特别好，看得见。", "A:开着灯你{睡得着}吗？\nB:对不起，我马上关灯。"]),
 G("haoxiang_jile", "最近你的电子邮件好像越来越少。", "好像 / 极了",
   "好像: hình như, dường như (giọng không chắc chắn). Adj + 极了: cực kỳ.",
   notes=["这个词我好像学过，可是想不起来了。– Từ này hình như tôi học rồi, nhưng không nhớ ra.", "最近好像越来越热了。– Dạo này hình như càng ngày càng nóng.",
          "收到你的电子邮件，我们高兴极了。– Nhận được email của con, bố mẹ vui lắm."]),
],
ex=[
 pool("一、选词填空（邮）", "Chữ “邮” tạo từ 邮票/邮局/邮件. Chọn từ điền vào chỗ trống.", ["邮票", "邮局", "邮件"], [
   "【邮局】离这儿远不远？", "我想买几张好看的纪念【邮票】。", "我收到了你的电子【邮件】。"]),
 pool("一、选词填空（箱）", "Chữ “箱” tạo từ 行李箱/冰箱/信箱/垃圾箱. Chọn từ điền vào chỗ trống.", ["行李箱", "冰箱", "信箱", "垃圾箱"], [
   "【冰箱】里有饮料，你自己拿吧。", "衣服都在【行李箱】里。", "我扔到【垃圾箱】里了，不知道还在不在里面。"]),
 match("二、连线", "Nối từ có chữ “网” với lời giải thích.", ["网上结交的朋友", "有很多电脑，能够上网的店", "特别喜欢上网的人", "使用网络的人", "互联网"],
   [("网络", "互联网"), ("网民", "使用网络的人"), ("网吧", "有很多电脑，能够上网的店"), ("网友", "网上结交的朋友"), ("网迷", "特别喜欢上网的人")]),
 pool("三、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["附近", "放心", "一切", "可惜", "聪明", "秘密", "健康", "极了", "惯"], [
   "我有一个小【秘密】，现在还不能告诉你。", "你回来了，我就【放心】了。", "我们玩儿得非常高兴，【可惜】你不在。", "我刚到中国，觉得这里的【一切】都很新鲜。",
   "学校【附近】有一家小饭馆。", "我刚来四川，还吃不【惯】这里的饭菜。", "我觉得这里的东西便宜【极了】，什么都想买。", "你很【聪明】，一定能学会。", "祝您身体【健康】！"]),
 pick("四、选择意思相近的词语填空", "Chọn từ thích hợp (từ gần nghĩa).", [
   (["收到", "受到"], ["我【收到】了你的电子邮件。", "他迟到了，【受到】了老师的批评。"]),
   (["所有", "一切"], ["我们班【所有】的同学今天都来上课了。", "这里的【一切】我都喜欢。"]),
   (["寄", "发"], ["我用电子邮件给你【发】过去吧。", "他去邮局【寄】包裹，还没回来。"]),
   (["极了", "很"], ["他的口语好【极了】。", "这里的冬天冷得【很】。"])]),
 opn("五、根据提示改写句子", "Viết lại câu theo gợi ý. Ví dụ: 学汉语越来越难了。→ 汉语越学越难了。", [
   ("明天我父母来北京，我要带他们多参观参观。（好好儿）", "明天我父母来北京，我要带他们好好儿参观参观。"),
   ("我最近有点儿胖了，得努力锻炼身体了。（好好儿）", "我最近有点儿胖了，得好好儿锻炼身体了。"),
   ("那种水果红红的，也许挺好吃。（好像）", "那种水果红红的，好像挺好吃。")]),
 opn("六、模仿例子完成句子", "Hoàn thành câu theo mẫu. Ví dụ: 作业这么多，你写得完吗？", [
   ("我的钥匙丢了，______了，怎么办？（找　到）", "我的钥匙丢了，找不到了，怎么办？"),
   ("包饺子对我来说太难了，______。（学　会）", "包饺子对我来说太难了，我学不会。"),
   ("衣服上的油，______？（洗　干净）", "衣服上的油，洗得干净吗？"),
   ("银行卡在自动取款机里，______，快给银行打电话吧。（拿　出来）", "银行卡在自动取款机里，拿不出来了，快给银行打电话吧。")]),
 opn("七、情境表达", "Câu nào dùng trong tình huống nào; tình huống sau nên nói thế nào?", [
   ("“喂，你听得清楚吗？”“祝你身体健康！”“祝你生日快乐！”——在什么情况下可以说？", "打电话的时候；给老人写信或祝福的时候；朋友过生日的时候。"),
   ("你想去朋友家，却忘了怎么走，该怎么问他？（找不到）", "我找不到你家了，怎么走？"),
   ("黑板上的字太小，你想要求老师写得大一点儿，你该怎么说？（看不清楚）", "老师，我看不清楚，请您写得大一点儿。")]),
 opn("八、根据课文内容完成对话", "Hoàn thành hội thoại theo bài khóa, dùng các cách nói: 为什么 / 因为…… / 是啊、可不是吗 / 哪儿啊 / 担心、不放心 / 好极了、真不错.", [
   ("A：马克的父母为什么一起床就先打开电子邮箱？\nB：______。（因为　邮件　习惯）", "因为看马克的邮件已经成了他们的习惯。"),
   ("A：马克的妈妈觉得有了网络太方便了。\nB：______。（是啊　快　情况）", "是啊，能很快地知道马克那里的情况。"),
   ("A：妈妈对马克放心吗？\nB：______。（哪儿啊　担心　身体　听不懂　吃不惯）", "哪儿啊，她担心马克的身体，担心他听不懂老师讲课、吃不惯中国菜。"),
   ("A：马克一定很想家吧？\nB：______。（可不是嘛　饭菜　舒服　咖啡馆　朋友）", "可不是嘛，他想妈妈做的饭菜、家里舒服的床、家乡的咖啡馆和朋友。"),
   ("A：马克会做中国菜吗？老师讲课，他听得懂吗？\nB：______。（真不错　进步）", "真不错，他会做中国菜，汉语也进步了，老师讲课他都听得懂。"),
   ("A：马克有女朋友吗？\nB：______。（秘密　漂亮　聪明　好极了）", "这是个秘密，他喜欢一个又漂亮又聪明的韩国姑娘，她好极了。")]),
 pool("九、阅读理解 · 选词填空（网友）", "Đọc cuộc trò chuyện giữa hai bạn trên mạng, chọn từ điền vào chỗ trống (một từ có thể dùng nhiều lần).", ["聪明", "好好儿", "离", "惯", "搬", "漂亮", "网", "担心", "秘密", "极了", "闻到"], [
   "小草：这几天忙【极了】，好长时间没上【网】了，今天可得【好好儿】和你聊聊。",
   "大树：忙什么呢？\n小草：就要期末考试了，得好好儿复习了。\n大树：和我一样，平时不努力，越到考试的时候越忙。\n小草：是啊，越忙就越睡不着。我该怎么办呢？\n大树：别【担心】，好好儿睡一觉吧，明天早上起床的时候就有办法了。",
   "小草：我是想好好儿睡一觉，可是这几天宿舍楼里吵【极了】，睡不着。\n大树：看来，你还过不【惯】集体生活，学生宿舍都是这样的。",
   "小草：不行，我得【搬】家。\n大树：好主意！想不想搬到我这儿来？我这儿【离】你的大学特别近。",
   "小草：我可不想搬到你那儿去，我还不知道你是男的还是女的呢！\n大树：见面就知道了。不过，我想你一定是个好姑娘，又漂亮又【聪明】。",
   "小草：错了，我不【漂亮】也不聪明，但是会做好吃的中国菜。\n大树：太好了！我好像都【闻到】香味儿了。告诉你一个【秘密】，我还有一个网名叫“吃不饱”！"], inline=False),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn hội thoại ở trên.", [
   ("“大树”和“小草”是什么关系？", "他们是网友。"), ("为什么“小草”最近没上网？", "因为就要期末考试了，她得好好儿复习。"),
   ("你觉得“大树”和“小草”分别是男的还是女的？", "（参考）“大树”可能是男的，“小草”是女的。"),
   ("“大树”为什么让“小草”搬到他那儿住？", "因为小草的宿舍楼里太吵，大树那儿离小草的大学特别近。"),
   ("“小草”觉得自己是个什么样的女孩儿？", "不漂亮也不聪明，但是会做好吃的中国菜。")]),
 opn("十、说一说，写一写", "Viết email cho bố mẹ hoặc bạn bè (ít nhất 60 chữ) kể về tình hình của bạn.", [
   ("你是什么时候来的中国？你经常和父母联系吗？一般用什么方式联系？你常上网吗？上网做什么？",
    "（参考）亲爱的爸爸妈妈：你们好！我是九月来中国的，现在一切都很好。我已经吃惯了中国菜，老师讲课我也都听得懂。我每天都上网，查资料、看电影，也常常和你们网上聊天儿。别担心我。祝你们身体健康！")]),
])
