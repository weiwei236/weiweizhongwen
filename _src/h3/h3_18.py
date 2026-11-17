# -*- coding: utf-8 -*-
# HSK 3 – Bài 18: 我学会了包饺子
from gtb_gen import V, T, Q, F, G
B = {}

B[18] = dict(zh="我学会了包饺子", vi="Tôi đã học được cách gói sủi cảo",
intro="Bạch Gia Nguyệt về nhà Lý Văn đón Tết Nguyên đán: chúc Tết bố mẹ Lý Văn, cùng gói sủi cảo, xem ảnh cũ và nghe kể về hành trình du học của Lý Văn.",
vocab=V("""
怎样|zěnyàng|dai|thế nào|你们怎样过春节？~Các bạn đón Tết thế nào?
过节|guòjié|dong|đón lễ|今年我们回老家过节。~Năm nay chúng tôi về quê đón lễ.
节|jié|dt|lễ|中秋节快乐！~Chúc mừng Trung thu!
节日|jiérì|dt|ngày lễ|春节是中国最重要的节日。~Tết là ngày lễ quan trọng nhất của Trung Quốc.
联欢|liánhuān|dong|liên hoan|新年的时候，学校开联欢会。~Dịp năm mới, trường tổ chức liên hoan.
大概|dàgài|pho|khoảng, đại khái, chung chung|从这儿到机场大概要一个小时。~Từ đây ra sân bay mất khoảng một tiếng.
阿姨|āyí|dt|cô, dì|阿姨，您好！~Cháu chào cô ạ!
叔叔|shūshu|dt|chú|叔叔给我买了一本书。~Chú mua cho cháu một cuốn sách.
收|shōu|dong|nhận, thu|这是我的一点儿心意，请收下。~Đây là chút lòng thành của cháu, xin hãy nhận.
总|zǒng|pho|luôn luôn|他总是第一个到办公室。~Anh ấy luôn là người đến văn phòng đầu tiên.
起|qǐ|dong|(nói) đến (dùng sau động từ, chỉ người/vật liên quan)|我常听朋友说起你。~Tôi hay nghe bạn bè nhắc đến bạn.
见面|jiànmiàn|dong|gặp mặt|我们明天下午见面吧。~Chiều mai chúng ta gặp nhau nhé.
矿泉水|kuàngquánshuǐ|dt|nước khoáng, nước suối|请给我一瓶矿泉水。~Cho tôi một chai nước khoáng.
刚刚|gānggāng|pho|vừa mới|他刚刚来北京两个月。~Anh ấy vừa mới đến Bắc Kinh hai tháng.
出发|chūfā|dong|xuất phát|我们明天早上七点出发。~Bảy giờ sáng mai chúng ta xuất phát.
不久|bùjiǔ|tt|không lâu|不久以后，他就回国了。~Không lâu sau, anh ấy về nước.
发生|fāshēng|dong|xảy ra|这里发生了什么事？~Ở đây đã xảy ra chuyện gì?
刚|gāng|pho|vừa, vừa mới|我刚到家。~Tôi vừa về đến nhà.
只要|zhǐyào|lien|chỉ cần|只要你努力，就一定能学好。~Chỉ cần bạn cố gắng là nhất định sẽ học giỏi.
学期|xuéqī|dt|học kỳ|这个学期我有五门课。~Học kỳ này tôi có năm môn.
毕业|bìyè|dong|tốt nghiệp|我姐姐明年大学毕业。~Chị tôi năm sau tốt nghiệp đại học.
出生|chūshēng|dong|sinh, sinh ra|我是在北京出生的。~Tôi sinh ra ở Bắc Kinh.
过去|guòqù|dt|quá khứ, trước kia|过去的事情就别想了。~Chuyện cũ thì đừng nghĩ nữa.
懂得|dǒngde|dong|hiểu|她懂得关心别人。~Cô ấy biết quan tâm người khác.
坚持|jiānchí|dong|kiên trì|学外语要坚持每天练习。~Học ngoại ngữ phải kiên trì luyện tập mỗi ngày.
完成|wánchéng|dong|hoàn thành|我已经完成了今天的作业。~Tôi đã hoàn thành bài tập hôm nay.
目标|mùbiāo|dt|mục tiêu|我今年的目标是通过HSK三级。~Mục tiêu năm nay của tôi là đỗ HSK 3.
发展|fāzhǎn|dong|phát triển|这个城市发展得很快。~Thành phố này phát triển rất nhanh.
春节|Chūnjié|rieng|Tết Nguyên đán|春节的时候，大家都回家过年。~Dịp Tết mọi người đều về nhà ăn Tết.
"""),
texts=[dict(t="课文1", scene="在飞机上，白家月和李文在聊天儿。", scene_vi="Bạch Gia Nguyệt và Lý Văn đang trò chuyện trên máy bay.", narr=False, lines=T("""
白家月>我要在中国过年，真开心。|Mình sắp được đón Tết ở Trung Quốc, vui quá.
李文>第一次请外国朋友来家里过春节，我也很高兴。|Lần đầu mời bạn nước ngoài về nhà đón Tết, mình cũng rất vui.
白家月>你们怎样过节？|Các cậu đón Tết thế nào?
李文>春节是中国最重要的节日，我们一般会回家，跟家人一起过。|Tết là ngày lễ quan trọng nhất Trung Quốc, chúng mình thường về nhà, đón Tết cùng gia đình.
白家月>那你跟家人会一起做什么？|Vậy cậu với gia đình sẽ cùng làm gì?
李文>我们家会一边包饺子，一边看春节联欢晚会，一直到十二点以后才睡觉。|Nhà mình sẽ vừa gói sủi cảo vừa xem chương trình liên hoan mừng Xuân, mãi sau mười hai giờ mới đi ngủ.
白家月>听起来很有意思。春节放几天假？|Nghe thú vị quá. Tết được nghỉ mấy ngày?
李文>大概七八天。|Khoảng bảy tám ngày.
"""), q=Q("""
李文为什么很高兴？|因为第一次请外国朋友来家里过春节。|Vì lần đầu mời bạn nước ngoài về nhà đón Tết.
李文和家人春节的时候会做什么？|一边包饺子，一边看春节联欢晚会。|Vừa gói sủi cảo vừa xem liên hoan mừng Xuân.
春节大概放几天假？|大概七八天。|Khoảng bảy tám ngày.
""")),
 dict(t="课文2", scene="在李文家，白家月给李文的父母拜年。", scene_vi="Bạch Gia Nguyệt đến chúc Tết bố mẹ của Lý Văn tại nhà anh ấy.", narr=False, lines=T("""
白家月>张阿姨，李叔叔。过年好！这是我准备的礼物，请收下。|Cô Trương, chú Lý. Chúc mừng năm mới! Đây là quà cháu chuẩn bị, xin cô chú nhận cho.
李叔叔>谢谢家月，你太客气了！|Cảm ơn Gia Nguyệt, cháu khách sáo quá!
张阿姨>总听小文说起你，今天终于有机会见面了。|Cứ nghe Tiểu Văn nhắc đến cháu, hôm nay cuối cùng cũng có dịp gặp mặt.
白家月>谢谢您和叔叔请我来家里做客。|Cảm ơn cô chú đã mời cháu đến nhà chơi.
李叔叔>桌子上有饮料，还有矿泉水，你想喝什么就自己拿。|Trên bàn có nước ngọt, còn có nước khoáng, cháu muốn uống gì thì cứ tự lấy.
张阿姨>你先坐着看会儿电视，饺子很快就包好了。|Cháu ngồi xem TV một lát, sủi cảo sắp gói xong rồi.
白家月>我刚刚看视频学会了包饺子，我跟你们一起包吧。|Cháu vừa xem video học được cách gói sủi cảo rồi, cháu gói cùng cô chú nhé.
"""), q=Q("""
白家月送礼物的时候说什么了？|过年好！这是我准备的礼物，请收下。|Chúc mừng năm mới! Đây là quà cháu chuẩn bị, xin nhận cho.
李文的家人是怎么欢迎白家月的？|让她想喝什么就自己拿，先坐着看会儿电视。|Bảo cô muốn uống gì tự lấy, ngồi xem TV trước.
白家月想跟李文的家人一起做什么？|一起包饺子。|Cùng gói sủi cảo.
""")),
 dict(t="课文3", scene="在李文家，李文妈妈和白家月在聊天儿。", scene_vi="Mẹ của Lý Văn đang trò chuyện cùng Bạch Gia Nguyệt tại nhà anh ấy.", narr=False, lines=T("""
白家月>这张照片是李文出国前照的吗？|Bức ảnh này chụp trước khi Lý Văn ra nước ngoài ạ?
张阿姨>对，这是他从北京出发时，我们全家在机场照的。|Đúng, đây là lúc nó xuất phát từ Bắc Kinh, cả nhà chụp ở sân bay.
白家月>那是三四年前吧？|Đó là khoảng ba bốn năm trước nhỉ?
张阿姨>是啊，时间过得真快，好像是不久前发生的一样。|Ừ, thời gian trôi nhanh thật, cứ như mới xảy ra gần đây vậy.
白家月>您一定特别想李文吧？|Chắc cô nhớ Lý Văn lắm ạ?
张阿姨>他刚离开家时，我很不习惯，只要几天不跟他视频，就很想他。|Lúc nó vừa xa nhà, cô rất không quen, chỉ cần mấy ngày không gọi video là nhớ nó lắm.
白家月>还有最后一个学期就要毕业了，他很快就会回来了。|Còn học kỳ cuối cùng là tốt nghiệp rồi, anh ấy sắp về rồi ạ.
"""), q=Q("""
李文第一次出国留学，是从哪儿出发的？|从北京出发的。|Xuất phát từ Bắc Kinh.
李文全家的照片是什么时候照的？|三四年前，李文从北京出发时在机场照的。|Ba bốn năm trước, lúc Lý Văn xuất phát, chụp ở sân bay.
李文刚离开家的时候，张阿姨怎么样？|很不习惯，只要几天不跟他视频，就很想他。|Rất không quen, mấy ngày không gọi video là nhớ.
""")),
 dict(t="课文4", scene="在家里，白家月在写日记。", scene_vi="Bạch Gia Nguyệt đang ngồi viết nhật ký ở trong nhà.", narr=True, lines=T("""
这次来中国，我最高兴的是认识了李文的父母。|Lần này đến Trung Quốc, điều tôi vui nhất là được quen bố mẹ Lý Văn.
他们给我看了李文出生时的照片，还给我讲了很多他过去的故事。|Họ cho tôi xem ảnh lúc Lý Văn mới sinh, còn kể cho tôi nghe nhiều chuyện ngày xưa của anh ấy.
李文高中的时候想学医，从那时起就努力学习。|Hồi cấp ba Lý Văn muốn học y, từ lúc đó đã chăm chỉ học tập.
高三的时候，因为成绩特别好，他得到了出国留学的机会。|Năm lớp mười hai, vì thành tích đặc biệt tốt, anh ấy có được cơ hội du học.
在他身上，我懂得了，只要一直坚持，就能完成自己的目标。|Từ anh ấy, tôi hiểu được rằng chỉ cần luôn kiên trì là có thể hoàn thành mục tiêu của mình.
我相信，他以后一定会发展得更好。|Tôi tin rằng sau này anh ấy nhất định sẽ phát triển tốt hơn nữa.
"""), q=Q("""
李文的父母给白家月看什么了？|李文出生时的照片。|Ảnh lúc Lý Văn mới sinh.
白家月从李文的父母那里了解到什么了？|很多李文过去的故事。|Nhiều chuyện ngày xưa của Lý Văn.
李文为什么能得到出国留学的机会？|因为他高三的时候成绩特别好。|Vì năm lớp 12 thành tích của anh ấy rất tốt.
"""))],
grammar=[
 G("gaishu", "概数表达法", "Cách diễn đạt số ước lượng",
   "Trong tiếng Trung, dùng hai con số liền kề nhau để diễn đạt số lượng không xác định (khoảng, độ chừng): 七八天, 五六个, 三四年…",
   [F("S:Chủ ngữ / phần trước|Nu:Hai số liền kề|M:Lượng từ|N:Danh từ / phần sau", [
     ("春节大概放|七八|天|假", "。", "Tết được nghỉ khoảng bảy tám ngày."),
     ("教室里来了|五六|个|学生", "。", "Trong lớp có năm sáu học sinh đến."),
     ("这些照片是|三四|年|前照的吧", "？", "Những bức ảnh này chụp khoảng ba bốn năm trước nhỉ?")])]),
 G("gangcai", "“刚才”和“刚刚”", "“刚才” và “刚刚”",
   "“刚才” là danh từ chỉ thời gian, biểu thị khoảng thời gian ngắn ngay trước thời điểm nói (thường vài phút trước), có thể đứng đầu câu hoặc sau chủ ngữ, trước động từ. “刚刚” là phó từ, chỉ hành động xảy ra chưa lâu theo cảm nhận của người nói (có thể vài phút, vài ngày, thậm chí vài tháng), phải đứng sau chủ ngữ, trước động từ.",
   [F("kw:刚才|C:Sự việc (vài phút trước)", [
     ("[刚才]|的电话是我妈妈打来的", "。", "Cuộc điện thoại vừa rồi là mẹ tôi gọi."),
     ("[刚才]|我看过一遍，不想再看了", "。", "Tôi vừa xem một lượt rồi, không muốn xem nữa.")], cap="刚才 – danh từ thời gian, có thể đứng đầu câu"),
    F("S:Chủ ngữ|kw:刚刚|V:Động từ", [
     ("我|[刚刚]|看视频学会了包饺子", "。", "Tôi vừa xem video học được cách gói sủi cảo."),
     ("他|[刚刚]|来北京两个月", "。", "Anh ấy mới đến Bắc Kinh được hai tháng.")], cap="刚刚 – phó từ, đứng sau chủ ngữ")]),
 G("zhiyaojiu", "条件复句“只要……，就……”", "Câu ghép điều kiện “只要……，就……”",
   "Trong câu ghép “只要……，就……”, thành phần sau “只要” là điều kiện đủ; chỉ cần có điều kiện này là đạt được kết quả sau “就” (chỉ cần… là…). Chủ ngữ có thể đặt trước hoặc sau “只要”; nếu câu có hai chủ ngữ khác nhau, chủ ngữ thứ hai đặt trước “就”.",
   [F("S:(Chủ ngữ)|kw:只要|C:Điều kiện đủ|X:(Chủ ngữ 2)|kw2:就 + kết quả", [
     ("我|[只要]|几天不跟他视频，||[就很想他]", "。", "Tôi chỉ cần mấy ngày không gọi video với nó là nhớ nó lắm."),
     ("|[只要]|你同意，|我们|[就这么决定了]", "。", "Chỉ cần bạn đồng ý, chúng ta quyết định vậy nhé."),
     ("|[只要]|你坚持每天早睡，|身体|[就一定会好起来]", "。", "Chỉ cần bạn kiên trì ngủ sớm mỗi ngày, sức khỏe nhất định sẽ tốt lên.")])]),
 G("congqi", "固定格式“从……起”", "Cấu trúc cố định “从……起”",
   "Cấu trúc cố định “从……起” mang ý nghĩa tương tự “从……开始” (kể từ… ), thường đặt ở đầu câu làm trạng ngữ, đa phần biểu thị thời gian.",
   [F("kw:从|T:Mốc thời gian|kw2:起，|C:Phần còn lại", [
     ("[从]|那时|[起，]|他就努力学习", "。", "Kể từ lúc đó anh ấy đã chăm chỉ học tập."),
     ("[从]|那天|[起，]|我们就变成了好朋友", "。", "Từ hôm đó, chúng tôi trở thành bạn thân."),
     ("[从]|那次旅游|[起，]|我对中国文化更有兴趣了", "。", "Từ chuyến du lịch đó, tôi càng hứng thú với văn hóa Trung Quốc."),
     ("[从]|明天|[起，]|我要每天出去跑步", "。", "Từ ngày mai, tôi sẽ ra ngoài chạy bộ mỗi ngày.")])]),
],
test=dict(
 l2=["很聪明|常看书|爱旅游", "飞机上|出租车上|国家图书馆", "经常跑步|昨天跑步了|昨天去爬山了"],
 l3=["去睡觉|看电视|去爬山", "银行经理|爱人的弟弟|自己的男朋友", "看电影|出去旅游|在家里吃饭", "看电视|玩电脑游戏|去饭馆吃饭"],
 r1=(["希望你这次能坚持下去。", "谢谢你想着我，那我就收下了。", "是的，她变得比以前更懂得关心别人了。", "这个星期我都有时间，可以带你到处看看。", "当然。我们先坐公交车，然后换地铁。", "我的笔记本电脑坏了，里面有很重要的东西。"],
     ["从明天起，我要每天出去跑步。", "你看起来很难过，发生什么事了？", "新年快乐，这是我给你准备的礼物。", "女儿上学后，老师和同学对她的影响很大。", "我刚来留学不久，对这里的环境还不太了解。"]),
 r2=(["学期", "阿姨", "完成", "节日", "鞋", "大概"],
     ["黄叔叔和李（　　）已经结婚15年了。", "经理说我们这个月的工作（　　）得特别好。", "今天是这个（　　）的最后一天，明天就放假了。", "A：你汉语说得真好，学了多长时间了？\nB：（　　）有三年了吧。", "A：老师，（　　）快乐！这是我们班同学送您的礼物。\nB：谢谢大家，我非常喜欢这个礼物。"]),
 r3=[("西瓜是夏天最常见的水果，这个季节的西瓜又大又甜，而且很便宜，一斤才一两块钱。", "一斤西瓜多少钱？", "十块钱|一两块钱|十几块钱"),
     ("我女儿是去年冬天出生的，到今年12月9日就一岁了。到时候，我会请孩子的爷爷奶奶来家里吃饭，给她过第一个生日。", "关于他女儿，可以知道什么？", "已经一岁了|今天过生日|是12月出生的"),
     ("张叔叔，我刚才给您打电话，您没接，是不是已经出发了？真不好意思，经理刚刚告诉我，公司要开一个重要的会议，我们都得参加，所以我会晚到一会儿。您到了的话，就先点杯饮料，等我一会儿。我一开完会就去找您。",
      ("他为什么现在不跟张叔叔见面？", "不想去|要开会|想喝饮料"), ("他让张叔叔做什么？", "回家|等等他|参加会议"))],
 w1=["这家公司（fā）展得很快，越来越有名了。", "小李（gāng）毕业就得到了一个出国工作的机会。", "妈妈（zǒng）为我结婚的事情着急，可对我来说，现在工作更重要。"],
 w2=[("出发", "她拉着行李箱从机场出发了。"), ("坚持", "他每天坚持打两个小时网球。"), ("完成", "他终于完成了工作，开心得站了起来。")],
 gl={"11": "Từ ngày mai, mình sẽ ra ngoài chạy bộ mỗi ngày. → A: Mong lần này bạn kiên trì được.",
     "12": "Trông bạn buồn lắm, đã xảy ra chuyện gì vậy? → F: Máy tính xách tay của mình hỏng rồi, bên trong có đồ rất quan trọng.",
     "13": "Chúc mừng năm mới, đây là quà mình chuẩn bị cho bạn. → B: Cảm ơn bạn đã nghĩ đến mình, vậy mình nhận nhé.",
     "14": "Con gái đi học rồi, thầy cô và bạn bè ảnh hưởng đến con bé rất nhiều. → C: Đúng vậy, con bé trở nên biết quan tâm người khác hơn trước.",
     "15": "Mình mới đến du học chưa lâu, chưa hiểu rõ môi trường ở đây lắm. → D: Tuần này mình đều rảnh, có thể dẫn bạn đi khắp nơi xem.",
     "16": "李阿姨 – cô Lý. → B 阿姨.",
     "17": "工作完成得特别好 – công việc hoàn thành rất tốt. → C 完成.",
     "18": "这个学期的最后一天 – ngày cuối cùng của học kỳ. → A 学期.",
     "19": "大概有三年了 – khoảng ba năm rồi. → F 大概.",
     "20": "节日快乐 – chúc mừng ngày lễ (Ngày Nhà giáo). → D 节日.",
     "21": "“一斤才一两块钱” → B.",
     "22": "“到今年12月9日就一岁了” → C 是12月出生的.",
     "23": "“公司要开一个重要的会议，我们都得参加” → B 要开会.",
     "24": "“就先点杯饮料，等我一会儿” → B 等等他."}),
)
