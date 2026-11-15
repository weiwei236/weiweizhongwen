# -*- coding: utf-8 -*-
# 发展汉语·初级综合(I) – Bài 25, 26
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[25] = dict(zh="我听不懂他们说的话", en="I Don't Understand What They Said", vi="Tôi nghe không hiểu họ nói gì",
intro="Trên lớp nghe hiểu thầy cô, nhưng ra đường thì nhiều người nói nhanh quá. Thôi Hạo nằm viện, các bạn và thầy đến thăm. Thôi Hạo nói chuyện với người Trung Quốc về những gì?",
vocab=V("""
懂|dǒng|dong|hiểu|你懂我的意思吗？~Bạn hiểu ý tôi không?
话|huà|dt|lời nói|老师的话我都记住了。~Lời thầy dặn tôi nhớ hết rồi.
出租车|chūzūchē|dt|xe taxi|我们坐出租车去机场吧。~Chúng ta đi taxi ra sân bay nhé.
虽然|suīrán|lien|tuy, mặc dù|虽然很累，但是我很高兴。~Tuy rất mệt nhưng tôi rất vui.
司机|sījī|dt|tài xế|我爸爸是出租车司机。~Bố tôi là tài xế taxi.
住院|zhù yuàn|cum|nằm viện|奶奶生病住院了。~Bà bị ốm phải nằm viện.
担心|dān xīn|dong|lo lắng|别担心，我没事。~Đừng lo, tôi không sao.
护士|hùshi|dt|y tá|我姐姐是医院的护士。~Chị tôi là y tá bệnh viện.
机会|jīhuì|dt|cơ hội|这是一个好机会。~Đây là một cơ hội tốt.
感觉|gǎnjué|dong|cảm thấy|我感觉有点儿冷。~Tôi cảm thấy hơi lạnh.
早|zǎo|tt|sớm|你今天来得真早！~Hôm nay bạn đến sớm thật!
出院|chū yuàn|cum|xuất viện|他下个星期就能出院了。~Tuần sau anh ấy có thể xuất viện.
好好儿|hǎohāor|pho|cho tử tế, hết lòng|你要好好儿学习。~Bạn phải học hành cho tử tế.
饿|è|tt|đói|我饿了，咱们去吃饭吧。~Tôi đói rồi, chúng ta đi ăn đi.
光盘|guāngpán|dt|đĩa CD|这张光盘里有很多中国歌。~Đĩa này có nhiều bài hát Trung Quốc.
关心|guān xīn|dong|quan tâm|谢谢你的关心！~Cảm ơn sự quan tâm của bạn!
部分|bùfen|dt|phần, bộ phận|这本书的第一部分很容易。~Phần một của quyển sách này rất dễ.
谈|tán|dong|nói chuyện, bàn|我们谈谈你的学习吧。~Chúng ta nói chuyện về việc học của bạn nhé.
些|xiē|lg|một số, vài|我买了一些水果。~Tôi mua một ít hoa quả.
经济|jīngjì|dt|kinh tế|他在大学学习经济。~Anh ấy học kinh tế ở đại học.
发展|fāzhǎn|dt|sự phát triển|这个城市发展得很快。~Thành phố này phát triển rất nhanh.
变化|biànhuà|dt|sự thay đổi|这几年北京的变化很大。~Mấy năm nay Bắc Kinh thay đổi rất nhiều.
生活|shēnghuó|dt|cuộc sống|你习惯这儿的生活了吗？~Bạn đã quen cuộc sống ở đây chưa?
比如|bǐrú|dong|ví dụ như|我喜欢水果，比如苹果、香蕉。~Tôi thích hoa quả, ví dụ táo, chuối.
留学|liú xué|dong|du học|我想去中国留学。~Tôi muốn đi du học Trung Quốc.
普通|pǔtōng|tt|bình thường, phổ thông|他是一个普通的学生。~Anh ấy là một học sinh bình thường.
像|xiàng|dong|giống|她长得很像妈妈。~Cô ấy trông rất giống mẹ.
那样|nàyàng|dai|như thế, như vậy|别那样做。~Đừng làm như thế.
方法|fāngfǎ|dt|phương pháp, cách|你学汉语的方法很好。~Cách học tiếng Hán của bạn rất hay.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
上课的时候，我能听懂老师说的话。可是到了大街上，很多中国人说的话我常常听不懂。|Trong giờ học, tôi nghe hiểu thầy cô nói. Nhưng ra đường, nhiều người Trung Quốc nói gì tôi thường nghe không hiểu.
坐出租车的时候，虽然我很喜欢跟司机聊天儿，但是他们说话太快，我常常听不懂。|Khi đi taxi, tuy tôi rất thích nói chuyện với tài xế, nhưng họ nói nhanh quá, tôi thường nghe không hiểu.
我生病住院的时候，也担心听不懂医生和护士说的话。|Lúc tôi ốm nằm viện, cũng lo nghe không hiểu bác sĩ và y tá nói.
可是他们知道我是外国人，跟我说话很慢，我差不多都能听懂。|Nhưng họ biết tôi là người nước ngoài, nói với tôi rất chậm, tôi gần như hiểu hết.
还有，很多中国人也喜欢跟我聊天儿。|Ngoài ra, nhiều người Trung Quốc cũng thích nói chuyện với tôi.
我每天能有机会跟这么多中国人练习汉语，感觉很不错。|Ngày nào tôi cũng có cơ hội luyện tiếng Hán với nhiều người Trung Quốc như vậy, cảm thấy rất tuyệt.
"""), q=Q("""
“我”能听懂一般中国人说的话吗？为什么？|常常听不懂，因为他们说话太快。|Thường không hiểu vì họ nói quá nhanh.
“我”在医院的时候，能不能听懂医生和护士的话？|差不多都能听懂，因为他们跟“我”说话很慢。|Gần như hiểu hết vì họ nói chậm.
""")),
 dict(t="课文二", scene="崔浩生病住院了，大家来医院看他。", scene_vi="Thôi Hạo ốm nằm viện, mọi người đến bệnh viện thăm.", narr=False, lines=T("""
李一民>你现在感觉怎么样了？|Bây giờ em cảm thấy thế nào rồi?
崔浩>好点儿了。我真想早点儿出院，回学校去。|Đỡ hơn rồi ạ. Em thật muốn sớm xuất viện để về trường.
李一民>别着急，你应该好好儿休息休息。这是我包的饺子，你吃点儿吧。|Đừng vội, em nên nghỉ ngơi cho tốt. Đây là sủi cảo thầy gói, em ăn chút đi.
崔浩>我真饿了。您做的饺子真好吃！|Em đói thật rồi. Sủi cảo thầy làm ngon thật!
林娜>你看，这是你要的书和音乐光盘。有时间你可以听听音乐，看看书。|Bạn xem, đây là sách và đĩa nhạc bạn cần. Có thời gian bạn có thể nghe nhạc, đọc sách.
马丁>这是你喜欢的水果。|Đây là hoa quả bạn thích.
崔浩>谢谢你们的关心！|Cảm ơn sự quan tâm của các bạn!
"""), q=Q("""
崔浩身体现在怎么样了？|好点儿了。|Đỡ hơn rồi.
崔浩的同学和老师给他带来了什么东西？|老师带来了饺子，林娜带来了书和音乐光盘，马丁带来了水果。|Sủi cảo, sách, đĩa nhạc, hoa quả.
""")),
 dict(t="课文三", narr=False, lines=T("""
马丁>你和中国人一起聊天儿，能听懂他们说的话吗？|Bạn nói chuyện với người Trung Quốc có nghe hiểu họ nói không?
崔浩>大部分能听懂，只有一小部分听不懂。|Phần lớn nghe hiểu, chỉ một phần nhỏ không hiểu.
马丁>你们都谈些什么呢？|Các bạn nói chuyện về những gì?
崔浩>谈中国的经济发展，中国的变化，中国人的生活。当然也谈韩国的事情。|Nói về sự phát triển kinh tế, sự thay đổi của Trung Quốc, cuộc sống người Trung Quốc. Đương nhiên cũng nói chuyện Hàn Quốc.
马丁>他们对什么事情感兴趣？|Họ hứng thú với chuyện gì?
崔浩>比如，来中国留学的韩国人为什么那么多？普通韩国人的生活真的像电视上那样吗？|Ví dụ, sao người Hàn sang Trung Quốc du học nhiều thế? Cuộc sống người Hàn bình thường có thật như trên ti vi không?
马丁>这些问题很有意思。虽然你学汉语的时间不长，但是你学到的东西很多。|Những câu hỏi này rất thú vị. Tuy thời gian bạn học tiếng Hán chưa lâu, nhưng bạn học được rất nhiều.
崔浩>是啊，多听、多说是练习汉语最好的方法。|Đúng vậy, nghe nhiều, nói nhiều là cách luyện tiếng Hán tốt nhất.
"""), q=Q("""
崔浩和中国人一起聊天儿都聊什么？|中国的经济发展、中国的变化、中国人的生活，还有韩国的事情。|Kinh tế, sự thay đổi, cuộc sống TQ và chuyện Hàn Quốc.
崔浩觉得练习汉语最好的方法是什么？|多听、多说。|Nghe nhiều, nói nhiều.
"""))],
grammar=[
 G("dingyu2", "我能听懂老师说的话。", "Định ngữ (2): V/VP/Cụm C-V + 的 + N",
   "Khi động từ, cụm động từ hoặc cụm chủ–vị làm định ngữ, giữa định ngữ và danh từ trung tâm phải có “的”.",
   [F("A:Định ngữ (V / VP / C-V)|kw:的|N:Danh từ", [("喜欢吃|[的]|水果", "", "hoa quả thích ăn"), ("学到|[的]|东西", "", "những gì học được"), ("练习汉语|[的]|方法", "", "cách luyện tiếng Hán"),
      ("我做|[的]|饺子", "", "sủi cảo tôi làm"), ("他们说|[的]|话", "", "lời họ nói")])],
   notes=["超市里吃的东西真多。/ 我买的苹果很不错。/ 这是你要的书和音乐光盘。"]),
 G("tingbudong", "很多中国人说的话我常常听不懂。", "听得懂 / 听不懂",
   "“听不懂” = không thể nghe hiểu, là dạng phủ định của “听得懂”. Tương tự: 看得懂/看不懂, 听得见/听不见.",
   [F("S:Chủ ngữ|V:听|kw:得/不|B:懂|O:", [("老师的话我|听|[得]|懂|", "。", "Lời thầy tôi nghe hiểu được."), ("他说得太快，我|听|[不]|懂|", "。", "Anh ấy nói nhanh quá, tôi nghe không hiểu."), ("这本书你看|[得]|懂|吗|", "？", "Quyển sách này bạn đọc hiểu không?")])]),
 G("suiran", "虽然我很喜欢跟司机聊天儿，但是他们说话太快。", "虽然……，但是/可是/还是……: tuy … nhưng …",
   "“虽然” đặt ở vế trước, thừa nhận một sự thật; vế sau thường dùng 但是 / 可是 / 还是.",
   [F("kw:虽然|A:Sự thật|kw2:但是/可是|B:Chuyển ý", [("我[虽然]|喜欢喝咖啡，|[可是]|不常喝", "。", "Tôi tuy thích uống cà phê nhưng không hay uống."), ("[虽然]|已经冬天了，天气|[还是]|很暖和", "。", "Tuy đã là mùa đông nhưng trời vẫn ấm."), ("[虽然]|你学汉语的时间不长，|[但是]|你学到的东西很多", "。", "Tuy bạn học chưa lâu nhưng học được rất nhiều.")])]),
 G("haohaor", "你应该好好儿休息休息。", "好好儿 + V: … cho tử tế, hết sức",
   "Phó từ, đặt trước động từ làm trạng ngữ, nghĩa là hết lòng, hết mức.",
   [F("S:Chủ ngữ|kw:好好儿|V:Động từ", [("我一定要|[好好儿]|学习", "。", "Tôi nhất định phải học hành chăm chỉ."), ("我们想|[好好儿]|玩儿两天", "。", "Chúng tôi muốn chơi cho đã hai ngày."), ("这件事我要|[好好儿]|想想", "。", "Việc này tôi phải suy nghĩ kỹ.")])]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["懂", "担心", "机会", "感觉", "关心", "好好儿", "比如", "像", "方法", "普通"], [
   "老师说的话你听【懂】了吗？", "妈妈很【担心】我的身体。", "我很想有【机会】去中国旅行。", "你现在【感觉】怎么样？", "谢谢大家对我的【关心】。",
   "考试快到了，你要【好好儿】复习。", "我喜欢运动，【比如】跑步、游泳。", "她长得很【像】她妈妈。", "你学汉字的【方法】很好。", "他是一个【普通】的大学生。"]),
 opn("二、用“虽然……但是……”完成句子", "Hoàn thành câu với 虽然……但是…….", [
   ("虽然汉语很难，______。", "虽然汉语很难，但是很有意思。"), ("______，但是我还想去。", "虽然那儿很远，但是我还想去。"), ("虽然他是中国人，______。", "虽然他是中国人，但是不会说广东话。")]),
 opn("三、把句子改成带“的”的说法", "Viết lại theo mẫu: 老师说话，我能听懂。→ 我能听懂老师说的话。", [
   ("妈妈做饭，饭很好吃。", "妈妈做的饭很好吃。"), ("我买书，书在桌子上。", "我买的书在桌子上。"), ("你要光盘，光盘我带来了。", "你要的光盘我带来了。")]),
 pick("四、选择“听得懂”或“听不懂”", "Chọn 听得懂 hoặc 听不懂.", [
   (["听得懂", "听不懂"], ["老师说得很慢，我都【听得懂】。", "司机说话太快，我【听不懂】。", "他说的是广东话，我一句也【听不懂】。", "你的话我【听得懂】，你说吧。"])]),
 tf("五、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("“我”能听懂所有中国人说的话。", False), ("医生和护士跟“我”说话很慢。", True), ("李老师给崔浩包了饺子。", True), ("崔浩跟中国人聊天儿，大部分听不懂。", False), ("崔浩觉得多听多说是最好的方法。", True)]),
 opn("六、说一说，写一写", "Viết khoảng 60 chữ.", [
   ("你能听懂中国人说的话吗？你常跟中国人聊什么？你觉得练习汉语最好的方法是什么？",
    "（参考）上课的时候，我能听懂老师说的话。可是中国人说话太快，我常常听不懂。虽然我的汉语不太好，但是我很喜欢跟中国朋友聊天儿，比如聊中国的生活、越南的事情。我觉得多听、多说是练习汉语最好的方法。")]),
])

B[26] = dict(zh="圣诞节快到了", en="Christmas Is About to Come", vi="Giáng sinh sắp đến rồi",
intro="Giáng sinh sắp đến, cửa hàng bán đầy đồ Giáng sinh. Người Trung Quốc có đón Giáng sinh không? Người Pháp đón Giáng sinh thế nào? Kỳ nghỉ Giáng sinh mọi người định làm gì?",
vocab=V("""
快要|kuàiyào|pho|sắp, sắp sửa|快要下雨了，我们回家吧。~Sắp mưa rồi, chúng ta về nhà thôi.
要|yào|nn|sắp (要……了)|火车要开了。~Tàu sắp chạy rồi.
快|kuài|pho|sắp (快……了)|快考试了，我很紧张。~Sắp thi rồi, tôi rất căng thẳng.
许多|xǔduō|tt|nhiều, rất nhiều|公园里有许多人。~Trong công viên có rất nhiều người.
没想到|méi xiǎngdào|cum|không ngờ|没想到你也在这儿！~Không ngờ bạn cũng ở đây!
丰富|fēngfù|tt|phong phú|学校的活动很丰富。~Hoạt động của trường rất phong phú.
不同|bùtóng|tt|khác nhau|我们俩的爱好不同。~Sở thích của hai chúng tôi khác nhau.
利用|lìyòng|dong|tận dụng, lợi dụng|我利用周末学习汉语。~Tôi tận dụng cuối tuần để học tiếng Hán.
饭店|fàndiàn|dt|khách sạn, nhà hàng|这家饭店的菜很好吃。~Đồ ăn nhà hàng này rất ngon.
迎接|yíngjiē|dong|đón, nghênh đón|我们去机场迎接新同学。~Chúng tôi ra sân bay đón bạn mới.
各种|gè zhǒng|cum|các loại|超市里有各种水果。~Siêu thị có đủ loại hoa quả.
市场|shìchǎng|dt|chợ, thị trường|这个市场的东西很便宜。~Đồ ở chợ này rất rẻ.
到处|dàochù|pho|khắp nơi|春天到处都是花。~Mùa xuân khắp nơi đều là hoa.
教堂|jiàotáng|dt|nhà thờ|圣诞节晚上，很多人去教堂。~Đêm Giáng sinh nhiều người đi nhà thờ.
全|quán|tt|toàn, cả|全班同学都来了。~Cả lớp đều đến rồi.
唱歌|chàng gē|cum|hát|我很喜欢唱歌。~Tôi rất thích hát.
唱|chàng|dong|hát|你唱一首中文歌吧。~Bạn hát một bài tiếng Trung đi.
歌|gē|dt|bài hát|这首歌很好听。~Bài hát này rất hay.
跳舞|tiào wǔ|cum|nhảy múa|她跳舞跳得很好。~Cô ấy nhảy rất đẹp.
跳|tiào|dong|nhảy|小狗跳得很高。~Con chó nhỏ nhảy rất cao.
孩子|háizi|dt|trẻ con, con|孩子们都很喜欢过节。~Bọn trẻ đều rất thích ngày lễ.
家人|jiārén|dt|người nhà|春节我想跟家人一起过。~Tết tôi muốn đón cùng gia đình.
打算|dǎsuan|dong|dự định|你寒假打算去哪儿？~Kỳ nghỉ đông bạn định đi đâu?
外地|wàidì|dt|nơi khác, tỉnh khác|他是从外地来的。~Anh ấy từ nơi khác đến.
附近|fùjìn|dt|gần đây, lân cận|学校附近有一家超市。~Gần trường có một siêu thị.
考试|kǎo shì|dong|thi|明天我们考试。~Mai chúng tôi thi.
认真|rènzhēn|tt|chăm chỉ, nghiêm túc|她学习很认真。~Cô ấy học rất chăm chỉ.
要是|yàoshi|lien|nếu|要是你不去，我也不去。~Nếu bạn không đi thì tôi cũng không đi.
没意思|méi yìsi|cum|chán, không thú vị|这个电影真没意思。~Bộ phim này thật chán.
圣诞节|Shèngdàn Jié|rieng|Lễ Giáng sinh|圣诞节你回国吗？~Giáng sinh bạn có về nước không?
朱云|Zhū Yún|rieng|Chu Vân (sinh viên Trung Quốc)|朱云是林娜的中国朋友。~Chu Vân là bạn Trung Quốc của Linna.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
圣诞节快要到了，许多商店都开始卖圣诞节用的东西。|Giáng sinh sắp đến, nhiều cửa hàng bắt đầu bán đồ dùng Giáng sinh.
有一天，马丁去一家商店买圣诞礼物，没想到商店里圣诞节用的东西那么丰富，买的人也不少。|Một hôm, Martin đến một cửa hàng mua quà Giáng sinh, không ngờ đồ Giáng sinh trong cửa hàng phong phú thế, người mua cũng không ít.
他问营业员：“中国也过圣诞节吗？”|Anh hỏi nhân viên bán hàng: “Trung Quốc cũng đón Giáng sinh à?”
营业员说：“以前中国人不过圣诞节。但是现在不同了，很多人喜欢过圣诞节，特别是年轻人，|Nhân viên nói: “Trước đây người Trung Quốc không đón Giáng sinh. Nhưng bây giờ khác rồi, nhiều người thích đón Giáng sinh, đặc biệt là người trẻ,
他们想利用这个机会玩儿一玩儿，商店、饭店也利用这个机会挣钱。”|họ muốn nhân dịp này đi chơi, cửa hàng, nhà hàng cũng nhân cơ hội này kiếm tiền.”
"""), q=Q("""
中国人过圣诞节吗？|以前不过，现在很多人喜欢过，特别是年轻人。|Trước không đón, giờ nhiều người thích đón.
为什么现在有很多中国人喜欢过圣诞节？|他们想利用这个机会玩儿一玩儿。|Họ muốn nhân dịp đi chơi.
""")),
 dict(t="课文二", narr=False, lines=T("""
朱云>要过圣诞节了。你们那儿圣诞节以前做什么呢？|Sắp đến Giáng sinh rồi. Chỗ các bạn trước Giáng sinh làm gì?
林娜>为了迎接圣诞节，我们在圣诞节以前四个星期就开始准备了。|Để đón Giáng sinh, chúng mình bắt đầu chuẩn bị từ bốn tuần trước Giáng sinh.
林娜>我们要准备圣诞礼物、酒，还有各种好吃的。商店里、圣诞市场里，到处都是买东西的人，非常热闹。|Phải chuẩn bị quà, rượu và đủ loại đồ ăn ngon. Trong cửa hàng, chợ Giáng sinh, khắp nơi đều là người mua sắm, rất náo nhiệt.
朱云>12月24日晚上你们做什么呢？|Tối 24 tháng 12 các bạn làm gì?
林娜>我们一般先去教堂参加活动，然后全家一起吃晚饭。我们唱歌、跳舞，聊天儿、喝酒，非常快乐。|Thường chúng mình đến nhà thờ dự lễ trước, rồi cả nhà cùng ăn tối. Chúng mình hát, nhảy, trò chuyện, uống rượu, rất vui.
朱云>听说你们会收到很多圣诞礼物。|Nghe nói các bạn sẽ nhận được nhiều quà Giáng sinh.
林娜>没错儿。最高兴的是孩子们，他们会收到许许多多的礼物。|Đúng vậy. Vui nhất là bọn trẻ, chúng sẽ nhận được rất rất nhiều quà.
朱云>要过圣诞节了，你给家人买礼物了吗？|Sắp Giáng sinh rồi, bạn đã mua quà cho gia đình chưa?
林娜>当然买了。我已经给他们寄去了，他们也给我寄来了礼物。|Đương nhiên mua rồi. Mình đã gửi cho họ rồi, họ cũng gửi quà cho mình.
"""), q=Q("""
圣诞节以前，法国人一般要准备什么？|准备圣诞礼物、酒，还有各种好吃的。|Quà, rượu, đồ ăn ngon.
法国人怎么过圣诞节？|先去教堂参加活动，然后全家一起吃晚饭，唱歌、跳舞、聊天儿、喝酒。|Đi nhà thờ, cả nhà ăn tối, hát, nhảy…
""")),
 dict(t="课文三", narr=False, lines=T("""
崔浩>听说圣诞节要放五天假，你们想怎么过啊？|Nghe nói Giáng sinh được nghỉ năm ngày, các bạn định đón thế nào?
马丁>我父母下个星期就要来北京了，我打算和他们一起到外地去旅游。你呢？|Bố mẹ mình tuần sau sẽ đến Bắc Kinh, mình định cùng họ đi du lịch nơi khác. Còn bạn?
崔浩>我想在附近玩儿一玩儿。|Mình muốn chơi quanh đây thôi.
山田>圣诞节以后我们就要考试了，我想在家学习。|Sau Giáng sinh chúng ta sắp thi rồi, mình muốn ở nhà học.
马丁>放假也不休息啊？你学习也太认真了。|Nghỉ lễ mà cũng không nghỉ à? Bạn học chăm quá đấy.
崔浩>要是不放假呢？|Nếu không được nghỉ thì sao?
马丁>要是不放假，我就不能去旅游了。不放假就太没意思了。|Nếu không nghỉ thì mình không đi du lịch được. Không nghỉ thì chán lắm.
"""), q=Q("""
圣诞节的时候，马丁打算做什么？|和父母一起到外地去旅游。|Đi du lịch nơi khác với bố mẹ.
崔浩和山田打算做什么？|崔浩想在附近玩儿一玩儿，山田想在家学习。|Thôi Hạo chơi gần đây, Yamada ở nhà học.
"""))],
grammar=[
 G("kuaiyao_le", "圣诞节快要到了。", "快要/要/快/就要 + V + 了: sắp …",
   "Bốn cách nói này đều biểu thị động tác hoặc sự việc sắp xảy ra. Trước “就要……了” có thể dùng trạng ngữ thời gian; trước “快要……了” thì không.",
   [F("S:Chủ ngữ|kw:要/快/快要/就要|V:V (+O)|kw2:了", [("|[要]|过圣诞节|[了]", "。", "Sắp đến Giáng sinh rồi."), ("|[快]|考试|[了]", "。", "Sắp thi rồi."), ("天|[快要]|下雨|[了]", "。", "Trời sắp mưa rồi."), ("我父母|[就要]|来北京|[了]", "。", "Bố mẹ tôi sắp đến Bắc Kinh rồi.")]),
    F("S:Chủ ngữ|T:Thời gian|kw:就要|V:V (+O)|kw2:了", [("我父母|下个星期|[就要]|来北京|[了]", "。", "Tuần sau bố mẹ tôi đến Bắc Kinh rồi."), ("他|明天|[就要]|回国|[了]", "。", "Mai anh ấy về nước rồi."), ("我们|星期五|[就要]|考试|[了]", "。", "Thứ Sáu chúng tôi thi rồi.")], cap="Có trạng ngữ thời gian: chỉ dùng 就要")]),
 G("tebieshi", "很多人喜欢过圣诞节，特别是年轻人。", "……，特别是……: đặc biệt là",
   "Nêu một sự vật trong cùng loại để nhấn mạnh; phía trước liệt kê chung, phía sau là sự vật được nhấn mạnh.",
   [F("C:Nói chung|kw:特别是|B:Nhấn mạnh", [("他非常喜欢吃水果，|[特别是]|苹果", "。", "Anh ấy rất thích ăn hoa quả, đặc biệt là táo."), ("老师们都喜欢他，|[特别是]|口语老师，更喜欢他", "。", "Các thầy cô đều quý cậu ấy, đặc biệt là cô dạy khẩu ngữ."), ("他每天都很忙，|[特别是]|周末，更忙", "。", "Ngày nào anh ấy cũng bận, nhất là cuối tuần.")])]),
 G("liheci", "听说圣诞节要放五天假。", "Từ ly hợp: 放假 → 放五天假",
   "Những từ như 放假、考试、见面、洗澡、睡觉、聊天儿、帮忙、请客、生气、旅游… có thể dùng liền, cũng có thể tách ra chèn thành phần khác vào giữa.",
   [F("A:A|X:Thành phần chèn|B:B", [("放|五天|假", "", "nghỉ năm ngày"), ("考|三天|试", "", "thi ba ngày"), ("见|过|面", "", "đã gặp mặt"), ("洗|一个小时|澡", "", "tắm một tiếng"), ("聊|一会儿|天", "", "trò chuyện một lúc")])],
   notes=["要是……就……: nếu … thì … (giống 如果……就……) – 要是不放假，我就不能去旅游了。"]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["许多", "没想到", "丰富", "利用", "迎接", "到处", "打算", "附近", "认真", "要是"], [
   "图书馆里有【许多】中文书。", "【没想到】今天这么冷。", "这个超市的东西很【丰富】。", "我想【利用】假期去旅游。", "为了【迎接】新年，大家都在准备。",
   "春节的时候，【到处】都很热闹。", "寒假你【打算】做什么？", "我家【附近】有一个公园。", "他上课很【认真】。", "【要是】明天下雨，我们就不去了。"]),
 opn("二、用“快要/就要……了”完成句子", "Hoàn thành câu với 快要/就要……了.", [
   ("天黑了，______。", "天黑了，快要下雨了。"), ("我们下个星期______。", "我们下个星期就要考试了。"), ("新年______，你打算做什么？", "新年快要到了，你打算做什么？")]),
 opn("三、用离合词扩展", "Mở rộng từ ly hợp theo mẫu: 放假 → 放五天假.", [
   ("考试（两天）", "考两天试"), ("见面（一次）", "见一次面"), ("聊天儿（一会儿）", "聊一会儿天"), ("睡觉（一个小时）", "睡一个小时觉")]),
 tf("四、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("以前中国人也过圣诞节。", False), ("法国人圣诞节以前四个星期就开始准备。", True), ("圣诞节最高兴的是孩子们。", True), ("马丁打算一个人去旅游。", False), ("山田圣诞节想在家学习。", True)]),
 opn("五、说一说，写一写", "Giới thiệu một ngày lễ ở nước bạn (khoảng 60 chữ).", [
   ("你们国家最重要的节日是什么？节日以前做什么准备？大家怎么过？（快要……了　为了　特别是　到处）",
    "（参考）春节快要到了。在越南，春节是最重要的节日。为了迎接春节，大家很早就开始准备，买新衣服、做好吃的。到处都很热闹。最高兴的是孩子们，特别是他们会收到红包。")]),
])
