# -*- coding: utf-8 -*-
# HSK 4上 – Bài 4: 很高兴能帮到你
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[4] = dict(zh="很高兴能帮到你", vi="Rất vui vì giúp được bạn",
intro="Điện thoại bị cắt dịch vụ, Trần Thiên Trung được người lạ mua vé tàu điện giúp; Bạch Gia Nguyệt xách đồ giúp hàng xóm; bài học còn giới thiệu cách đi lại quãng ngắn và những dịch vụ chu đáo trong ga tàu điện ngầm.",
vocab=V("""
啊|ā|than|a, á (thán từ)|啊，我的钥匙不见了！~A, chìa khóa của tôi không thấy đâu!
停|tíng|dong|dừng, ngừng; đỗ (xe)|雨停了，我们走吧。~Mưa tạnh rồi, chúng ta đi thôi.
交|jiāo|dong|nộp, giao|明天要交作业。~Ngày mai phải nộp bài tập.
费|fèi|dt|phí, chi phí|这个月的电话费是多少？~Tiền điện thoại tháng này bao nhiêu?
信号|xìnhào|dt|tín hiệu, sóng|山上手机没有信号。~Trên núi điện thoại không có sóng.
感谢|gǎnxiè|dong|cảm ơn, biết ơn|非常感谢你的帮助。~Vô cùng cảm ơn sự giúp đỡ của bạn.
联系|liánxì|dong|liên hệ, liên lạc|到了北京以后给我联系。~Đến Bắc Kinh rồi thì liên lạc với tôi.
方式|fāngshì|dt|phương thức, cách thức|这是我的联系方式。~Đây là thông tin liên lạc của tôi.
客气|kèqi|dong|khách sáo|别客气，就像在自己家一样。~Đừng khách sáo, cứ như ở nhà mình vậy.
剩|shèng|dong|còn lại, thừa|钱包里只剩十块钱了。~Trong ví chỉ còn lại mười tệ.
提|tí|dong|xách (cầm buông tay xuống)|他手里提着两个袋子。~Tay anh ấy xách hai cái túi.
袋子|dàizi|dt|cái túi|这个袋子太小了，放不下。~Cái túi này nhỏ quá, không để vừa.
重|zhòng|tt|nặng|这个箱子很重，我们一起搬吧。~Cái thùng này rất nặng, chúng ta cùng khiêng nhé.
算|suàn|dong|coi như, tính là|今天就算休息一天吧。~Hôm nay coi như nghỉ một ngày vậy.
再说|zàishuō|lien|hơn nữa, vả lại|太晚了，再说外面还在下雨，明天去吧。~Muộn quá rồi, vả lại bên ngoài còn đang mưa, mai đi nhé.
之间|zhījiān|dt|giữa (hai người/vật)|朋友之间应该互相帮助。~Giữa bạn bè nên giúp đỡ lẫn nhau.
互相|hùxiāng|pho|lẫn nhau, với nhau|同学们互相学习。~Các bạn học hỏi lẫn nhau.
辛苦|xīnkǔ|tt|vất vả, cực nhọc|你辛苦了，快休息一下吧。~Bạn vất vả rồi, mau nghỉ một lát đi.
出行|chūxíng|dong|đi lại, ra ngoài (đi xa)|节假日出行的人特别多。~Ngày lễ người đi lại đặc biệt đông.
距离|jùlí|dt|khoảng cách|我家到学校的距离不远。~Khoảng cách từ nhà tôi đến trường không xa.
往往|wǎngwǎng|pho|thường thường, thường hay|周末的公园往往人很多。~Công viên cuối tuần thường rất đông người.
既|jì|pho|vừa… (vừa…), đã… (lại…)|这件衣服既便宜又好看。~Chiếc áo này vừa rẻ vừa đẹp.
电动车|diàndòngchē|dt|xe đạp điện, xe máy điện|他每天骑电动车上班。~Hằng ngày anh ấy đi xe điện đi làm.
速度|sùdù|dt|tốc độ|请慢一点儿，速度太快了。~Chậm lại chút, tốc độ nhanh quá.
充电|chōngdiàn|dong|sạc điện|我的手机要充电了。~Điện thoại của tôi cần sạc rồi.
流行|liúxíng|dong|thịnh hành, phổ biến|今年流行这种颜色。~Năm nay thịnh hành màu này.
省|shěng|dong|tiết kiệm|坐地铁能省不少时间。~Đi tàu điện ngầm có thể tiết kiệm không ít thời gian.
力气|lìqi|dt|sức lực|他力气很大，一个人就搬动了。~Anh ấy khỏe lắm, một mình đã khiêng được.
乘客|chéngkè|dt|hành khách|地铁上的乘客很多。~Hành khách trên tàu điện ngầm rất đông.
购买|gòumǎi|dong|mua|可以在网上购买火车票。~Có thể mua vé tàu trên mạng.
食物|shíwù|dt|thức ăn, đồ ăn|不要把食物带进教室。~Đừng mang đồ ăn vào lớp học.
免费|miǎnfèi|dong|miễn phí|这个博物馆免费参观。~Bảo tàng này tham quan miễn phí.
早餐|zǎocān|dt|bữa sáng|这家酒店的早餐很丰富。~Bữa sáng của khách sạn này rất phong phú.
来得及|láidejí|dong|kịp (còn thời gian)|别着急，现在去还来得及。~Đừng vội, bây giờ đi vẫn còn kịp.
鲜花|xiānhuā|dt|hoa tươi|我买了一束鲜花送给妈妈。~Tôi mua một bó hoa tươi tặng mẹ.
顺便|shùnbiàn|pho|tiện thể, nhân tiện|你去超市的时候，顺便帮我买瓶水。~Lúc đi siêu thị tiện thể mua giúp tôi chai nước.
心情|xīnqíng|dt|tâm trạng|今天天气好，我的心情也很好。~Hôm nay trời đẹp, tâm trạng tôi cũng rất tốt.
更加|gèngjiā|pho|càng, càng thêm|雨后的空气更加新鲜了。~Không khí sau mưa càng trong lành hơn.
愉快|yúkuài|tt|vui vẻ, vui sướng|祝你周末愉快！~Chúc bạn cuối tuần vui vẻ!
"""),
texts=[dict(t="课文1", scene="在地铁站，陈天中准备买票进站。", scene_vi="Ở ga tàu điện ngầm, Trần Thiên Trung chuẩn bị mua vé vào ga.", narr=False, lines=T("""
陈天中>啊，我的手机停机了！怎么办啊？|A, điện thoại mình bị cắt dịch vụ rồi! Làm sao đây?
路人>你好，你看上去很着急，需要帮忙吗？|Chào bạn, trông bạn rất sốt ruột, cần giúp gì không?
陈天中>我忘了交电话费，手机停机了。我没带现金，手机没有信号，上不了网，买不了地铁票了。|Mình quên nộp tiền điện thoại nên bị cắt dịch vụ. Mình không mang tiền mặt, điện thoại không có sóng, không lên mạng được, không mua được vé tàu điện ngầm.
路人>你要去哪儿？我帮你买张票。|Bạn muốn đi đâu? Mình mua giúp bạn một vé.
陈天中>太感谢你了，我要去北京大学站。对了，能不能告诉我你的联系方式？我想把钱还给你。|Cảm ơn bạn nhiều lắm, mình đi ga Đại học Bắc Kinh. À đúng rồi, bạn có thể cho mình thông tin liên lạc được không? Mình muốn trả lại tiền cho bạn.
路人>别客气，很高兴能帮到你。|Đừng khách sáo, rất vui vì giúp được bạn.
"""), q=Q("""
陈天中的手机怎么了？|停机了。|Bị cắt dịch vụ (khóa máy).
陈天中为什么很着急？|因为手机停机了，没有信号，他也没带现金，买不了地铁票。|Vì điện thoại bị cắt dịch vụ, không có sóng, cậu cũng không mang tiền mặt nên không mua được vé tàu.
陈天中要去哪儿？|北京大学站。|Ga Đại học Bắc Kinh.
陈天中为什么想要那个人的联系方式？|因为他想把钱还给那个人。|Vì cậu muốn trả lại tiền cho người đó.
""")),
 dict(t="课文2", scene="在楼下，白家月遇到了住在同一层的邻居。", scene_vi="Dưới tầng, Bạch Gia Nguyệt gặp người hàng xóm sống cùng tầng.", narr=False, lines=T("""
白家月>阿姨，您怎么站在这儿不上楼？|Cô ơi, sao cô đứng ở đây không lên lầu ạ?
邻居>我开车去超市买了不少东西，刚拿过来了一些。我先休息一会儿，再去车里拿剩下的。|Cô lái xe đi siêu thị mua khá nhiều đồ, vừa mang qua được một ít. Cô nghỉ một lát rồi ra xe lấy chỗ còn lại.
白家月>我正好要上楼，我帮您提上去吧。|Cháu đang định lên lầu, cháu xách lên giúp cô nhé.
邻居>不用不用，这几个袋子太重了，我自己拿吧。|Không cần đâu, mấy cái túi này nặng lắm, cô tự mang được rồi.
白家月>没事，我提着这些东西就算锻炼身体了，再说邻居之间就是要互相帮助啊。|Không sao ạ, cháu xách mấy thứ này coi như rèn luyện thân thể, vả lại hàng xóm với nhau là phải giúp đỡ lẫn nhau mà.
邻居>谢谢家月！那就辛苦你了。|Cảm ơn Gia Nguyệt! Vậy vất vả cho cháu rồi.
"""), q=Q("""
白家月现在要做什么？|上楼。|Lên lầu.
邻居为什么不上楼？|因为她想先休息一会儿，再去车里拿剩下的东西。|Vì cô muốn nghỉ một lát rồi ra xe lấy chỗ đồ còn lại.
白家月为什么帮邻居提东西？|因为她觉得提东西就算锻炼身体了，再说邻居之间就是要互相帮助。|Vì cô thấy xách đồ coi như rèn luyện thân thể, vả lại hàng xóm phải giúp đỡ lẫn nhau.
""")),
 dict(t="课文3", scene="短距离出行的新选择", scene_vi="Lựa chọn mới cho việc đi lại quãng ngắn", narr=True, lines=T("""
在城市里，人们出行的方式越来越多。|Ở thành phố, cách đi lại của mọi người ngày càng nhiều.
短距离出行时，骑自行车往往是人们常见的选择。|Khi đi quãng ngắn, đi xe đạp thường là lựa chọn phổ biến.
白家月就很喜欢骑车去学校，她觉得这样既方便，又能锻炼身体，还能保护环境。|Bạch Gia Nguyệt rất thích đạp xe đến trường, cô thấy như vậy vừa tiện, vừa rèn luyện thân thể, lại còn bảo vệ môi trường.
除了骑自行车，人们还会选择骑电动车。|Ngoài đạp xe, mọi người còn chọn đi xe điện.
电动车速度快，价格不高，充电也很方便，所以越来越流行。|Xe điện chạy nhanh, giá không cao, sạc điện cũng tiện, nên ngày càng thịnh hành.
陈天中平时也骑自行车，不过为了省力气，他最近打算买一辆电动车。|Trần Thiên Trung ngày thường cũng đạp xe, nhưng để đỡ tốn sức, gần đây cậu định mua một chiếc xe điện.
"""), q=Q("""
白家月怎么去学校？|骑自行车。|Đi xe đạp.
白家月为什么喜欢骑车？|因为她觉得这样既方便，又能锻炼身体，还能保护环境。|Vì cô thấy như vậy vừa tiện, vừa rèn luyện thân thể, lại bảo vệ môi trường.
电动车为什么越来越流行？|因为电动车速度快，价格不高，充电也很方便。|Vì xe điện chạy nhanh, giá không cao, sạc điện cũng tiện.
最近陈天中打算买什么？|一辆电动车。|Một chiếc xe điện.
""")),
 dict(t="课文4", scene="地铁站里的贴心服务", scene_vi="Những dịch vụ chu đáo trong ga tàu điện ngầm", narr=True, lines=T("""
在中国，乘客可以在不少地铁站里直接扫码购买食物和饮料，有的地铁站还提供免费借雨伞、发雨衣等服务。|Ở Trung Quốc, hành khách có thể quét mã mua đồ ăn thức uống ngay trong nhiều ga tàu điện ngầm, có ga còn cung cấp dịch vụ cho mượn ô, phát áo mưa miễn phí.
有些地铁站附近公司比较多，工作日站里还有早餐车，没来得及吃早饭的人在这里就能买到热包子和牛奶等，省了不少时间。|Gần một số ga có khá nhiều công ty, ngày làm việc trong ga còn có xe bán đồ ăn sáng, ai chưa kịp ăn sáng có thể mua bánh bao nóng, sữa v.v. ở đây, tiết kiệm được khá nhiều thời gian.
有的地铁站里甚至还有鲜花店，乘客下班时可以顺便买花送给家人。|Có ga thậm chí còn có cửa hàng hoa tươi, hành khách tan làm có thể tiện thể mua hoa tặng người nhà.
这些小小的服务，不仅方便了人们的出行，也让大家的心情变得更加愉快。|Những dịch vụ nhỏ bé này không chỉ giúp mọi người đi lại thuận tiện mà còn khiến tâm trạng mọi người vui vẻ hơn.
"""), q=Q("""
什么样的地铁站里最可能有早餐车？|附近公司多的地铁站。|Ga có nhiều công ty ở gần.
在中国，不少地铁站都提供什么服务？|可以扫码购买食物和饮料，有的还提供免费借雨伞、发雨衣等服务。|Quét mã mua đồ ăn thức uống, có ga còn cho mượn ô, phát áo mưa miễn phí.
地铁站里的服务有什么作用？|不仅方便了人们的出行，也让大家的心情变得更加愉快。|Vừa giúp mọi người đi lại thuận tiện vừa khiến tâm trạng mọi người vui vẻ hơn.
""")),
],
grammar=[
 G("budeliao", "可能补语“动词+得/不+了”", "Bổ ngữ khả năng “Động từ + 得 / 不 + 了”",
   "“得了 / 不了” đặt sau động từ hoặc chen vào giữa từ ly hợp, tạo thành bổ ngữ khả năng, cho biết hành động hay kết quả có thể hoàn thành / thực hiện được hay không.",
   [F("S:Chủ ngữ|V:Động từ|kw:得了 / 不了|O:Tân ngữ", [
     ("手机没有信号，|上|[不了]|网", "。", "Điện thoại không có sóng, không lên mạng được."),
     ("她刚才给我发信息，说她今天|来|[不了]|", "了。", "Cô ấy vừa nhắn tin cho tôi, nói hôm nay cô ấy không đến được."),
     ("明天的足球比赛，你们班男生|参加|[得了]|", "吗？", "Trận bóng đá ngày mai, nam sinh lớp các bạn có tham gia được không?")])]),
 G("zaishuo", "连词“再说”", "Liên từ “再说”",
   "Sau khi đã nêu một lý do hay tình huống, dùng “再说” để bổ sung thêm một lý do / tình huống nữa: “vả lại, hơn nữa”.",
   [F("X:Lý do / tình huống 1|kw:再说|V:Bổ sung lý do 2", [
     ("我提着这些东西就算锻炼身体了|[再说]|邻居之间就是要互相帮助啊", "。", "Cháu xách đồ coi như rèn luyện thân thể, vả lại hàng xóm phải giúp đỡ lẫn nhau mà."),
     ("今天太晚了，别去超市了|[再说]|外面还在下雨呢", "。", "Hôm nay muộn quá, đừng đi siêu thị nữa, vả lại bên ngoài còn đang mưa."),
     ("你就跟我们一起参加活动吧。你今天正好有时间|[再说]|人多也更热闹", "。", "Bạn tham gia hoạt động cùng bọn mình đi. Hôm nay bạn vừa hay rảnh, hơn nữa đông người cũng vui hơn.")])]),
 G("jiyou", "并列复句“既……，又/也……”", "Câu phức đẳng lập “既……，又 / 也……”",
   "Dùng nối tính từ, động từ hoặc cụm từ, biểu thị đồng thời có nhiều tính chất hoặc tồn tại nhiều tình huống: “vừa… vừa…, đã… lại…”.",
   [F("S:Chủ ngữ|kw:既|A:Tính chất 1|kw2:又 / 也|B:Tính chất 2", [
     ("她觉得这样|[既]|方便|[又]|能锻炼身体，还能保护环境", "。", "Cô thấy như vậy vừa tiện, vừa rèn luyện thân thể, lại bảo vệ môi trường."),
     ("这家饭馆的菜|[既]|好吃|[又]|便宜", "。", "Món ăn của quán này vừa ngon vừa rẻ."),
     ("我很喜欢这门课程，|[既]|能提高中文水平|[也]|能学到历史知识", "。", "Tôi rất thích môn học này, vừa nâng cao trình độ tiếng Trung vừa học được kiến thức lịch sử.")])]),
 G("laideji", "固定短语“来得及/来不及”", "Cụm từ cố định “来得及 / 来不及”",
   "“来得及” biểu thị vẫn còn thời gian, có thể kịp làm / kịp đến; “来不及” biểu thị vì thời gian gấp nên không kịp.",
   [F("S:Chủ ngữ|kw:来得及 / 来不及|V:Hành động", [
     ("没|[来得及]|吃早饭的人在这里就能买到热包子和牛奶等", "。", "Người chưa kịp ăn sáng có thể mua bánh bao nóng và sữa ở đây."),
     ("你现在才告诉我，我|[来不及]|通知大家了", "。", "Bây giờ bạn mới nói, tôi không kịp thông báo cho mọi người nữa rồi."),
     ("中午12点的飞机，咱们9点出发|[来得及]|", "吗？", "Máy bay 12 giờ trưa, chúng ta 9 giờ xuất phát có kịp không?")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["停", "算", "剩", "联系", "之间"], [
   "还【剩】不少菜，我们带回家吃吧。", "外面的雨【停】了，咱们出去走走吧。", "同学【之间】应该互相帮助、互相学习。",
   "今天我再准备一下材料，明天跟您【联系】。", "奶奶说她每天打扫房间，就【算】做运动了。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["更加", "距离", "顺便", "流行", "力气"], [
   "A：你要去超市吗？能不能【顺便】帮我买个面包？ B：没问题。", "A：听说你最近一直坚持锻炼。 B：是的，我希望自己的身体【更加】健康。",
   "A：我发现街上很多人都穿绿色的衣服。 B：是啊，看来今年比较【流行】绿色。", "A：咱们先休息休息吧，我一点儿【力气】也没有了。 B：好，你先坐一会儿，我去给你买瓶饮料。",
   "A：你每天走路上下班吗？ B：对，我家到公司的【距离】不算远，走路大概半个小时。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["扫不了码", "一天的心情都非常愉快", "小王非常感谢她", "没来得及吃早饭就去上班了"], [
   "小王今天早上起晚了，【没来得及吃早饭就去上班了】。她坐地铁到了公司附近，想在地铁站买点儿吃的。小王选好早餐后，突然发现手机没电了，【扫不了码】。她正要把吃的放回去，一位乘客看到了，问她需不需要帮忙。小王把事情告诉了她，她就给小王买了一份早餐。【小王非常感谢她】，一直向她说“谢谢”。小王因为这件事，【一天的心情都非常愉快】。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：咱们点的菜多不多？ B：______。（吃不了）", "太多了，咱们两个人吃不了。"),
   ("A：你今天还出门吗？ B：______。（再说）", "不出门了，太累了，再说外面还在下雨。"),
   ("我想买一辆电动车，因为______。（既……又……）", "我想买一辆电动车，因为它既省力气，速度又快。"),
   ("别着急，还有15分钟，咱们______。（来得及）", "别着急，还有15分钟，咱们来得及。")]),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l4", items=[
   ("重", "这个箱子太重了，我一个人搬不动。"), ("心情", "听到这个好消息，她的心情特别好。"), ("提", "妈妈提着两个大袋子从超市回来了。")]),
])
