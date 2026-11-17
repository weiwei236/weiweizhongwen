# -*- coding: utf-8 -*-
# HSK 3 – Bài 3: 这个小区挺好的
from gtb_gen import V, T, Q, F, G
B = {}

B[3] = dict(zh="这个小区挺好的", vi="Khu dân cư này khá tốt",
intro="Trường cấp hai của con gái hơi xa nhà, vợ chồng Lưu Minh và Vương Nhất Tuyết quyết định đổi nhà: xem khu dân cư mới, dọn dẹp, làm thẻ tín dụng và bàn kế hoạch chuyển nhà.",
vocab=V("""
初中|chūzhōng|dt|trung học cơ sở, cấp hai|我妹妹今年上初中了。~Em gái tôi năm nay lên cấp hai rồi.
咱们|zánmen|dai|chúng ta (gồm cả người nghe)|咱们一起去吃饭吧。~Chúng ta cùng đi ăn cơm đi.
换|huàn|dong|thay, thay đổi, đổi|这件衣服太小了，我想换一件。~Cái áo này nhỏ quá, tôi muốn đổi cái khác.
房子|fángzi|dt|nhà, căn nhà|他们家的房子很大。~Nhà của họ rất rộng.
小区|xiǎoqū|dt|khu dân cư, khu nhà ở|我们小区里有一个超市。~Trong khu nhà chúng tôi có một siêu thị.
环境|huánjìng|dt|môi trường|这个学校的环境很好。~Môi trường của trường này rất tốt.
挺|tǐng|pho|khá, rất|今天的天气挺好的。~Thời tiết hôm nay khá đẹp.
空调|kōngtiáo|dt|máy điều hòa|天太热了，开空调吧。~Trời nóng quá, bật điều hòa đi.
洗衣机|xǐyījī|dt|máy giặt|我家的洗衣机是新买的。~Máy giặt nhà tôi mới mua.
层|céng|lg|tầng|我住在八层。~Tôi ở tầng tám.
花园|huāyuán|dt|vườn hoa|晚饭后我们去花园走走。~Ăn tối xong chúng ta ra vườn hoa đi dạo.
灯|dēng|dt|đèn|房间里的灯太暗了。~Đèn trong phòng tối quá.
关|guān|dong|tắt, đóng|出门的时候请关门。~Lúc ra ngoài xin hãy đóng cửa.
冰箱|bīngxiāng|dt|tủ lạnh|冰箱里有很多水果。~Trong tủ lạnh có rất nhiều hoa quả.
卫生间|wèishēngjiān|dt|nhà vệ sinh|请问，卫生间在哪儿？~Xin hỏi, nhà vệ sinh ở đâu?
打扫|dǎsǎo|dong|dọn dẹp, quét dọn|周末我要打扫房间。~Cuối tuần tôi phải dọn phòng.
搬家|bānjiā|dong|chuyển nhà|我们下个月搬家。~Tháng sau chúng tôi chuyển nhà.
办|bàn|dong|làm, xử lý|我明天去银行办点儿事。~Ngày mai tôi ra ngân hàng làm chút việc.
信用卡|xìnyòngkǎ|dt|thẻ tín dụng|这里可以用信用卡吗？~Ở đây dùng thẻ tín dụng được không?
还|huán|dong|trả, hoàn trả|这本书我明天还你。~Quyển sách này mai mình trả bạn.
听说|tīngshuō|dong|nghe nói|听说你要去中国留学？~Nghe nói bạn sắp sang Trung Quốc du học?
银行|yínháng|dt|ngân hàng|银行几点开门？~Ngân hàng mấy giờ mở cửa?
才|cái|pho|(mãi)… mới|他晚上十点才回家。~Mười giờ tối anh ấy mới về nhà.
纸|zhǐ|dt|giấy|请给我一张纸。~Cho tôi một tờ giấy.
搬|bān|dong|chuyển, mang, bê|这个箱子太重了，我搬不动。~Cái thùng này nặng quá, tôi bê không nổi.
需要|xūyào|dong|cần, cần thiết; nhu cầu|你需要帮忙吗？~Bạn có cần giúp không?
"""),
texts=[dict(t="课文1", scene="在家里，刘明和王一雪在聊天儿。", scene_vi="Lưu Minh và Vương Nhất Tuyết đang trò chuyện ở trong nhà.", narr=False, lines=T("""
王一雪>小雪的初中离家有点儿远，咱们换一个近点儿的房子吧。|Trường cấp hai của Tiểu Tuyết hơi xa nhà, chúng ta đổi sang căn nhà gần hơn đi.
刘明>好啊，我上网看看。你觉得这个小区怎么样？|Được, anh lên mạng xem thử. Em thấy khu nhà này thế nào?
王一雪>环境挺好的，离地铁站还不远。|Môi trường khá tốt, lại không xa ga tàu điện ngầm.
刘明>房子里面也不错，空调和洗衣机都是新的。|Bên trong nhà cũng không tệ, điều hòa và máy giặt đều mới.
王一雪>是不错，但是我不喜欢住一层。|Đúng là không tệ, nhưng em không thích ở tầng một.
刘明>这个一层带一个小花园，我觉得咱们可以去看看。|Tầng một này có kèm một khu vườn nhỏ, anh nghĩ chúng ta có thể đi xem thử.
"""), q=Q("""
他们为什么要换房子？|因为小雪的初中离家有点儿远。|Vì trường cấp hai của Tiểu Tuyết hơi xa nhà.
王一雪觉得新小区怎么样？|环境挺好的，离地铁站还不远。|Môi trường khá tốt, không xa ga tàu điện ngầm.
刘明为什么喜欢这个房子？|因为空调和洗衣机都是新的，一层还带一个小花园。|Vì điều hòa và máy giặt đều mới, tầng một có vườn nhỏ.
""")),
 dict(t="课文2", scene="在新家，王一雪在收拾房间，刘明进来了。", scene_vi="Vương Nhất Tuyết đang dọn dẹp trong nhà mới thì Lưu Minh bước vào.", narr=False, lines=T("""
王一雪>我今天早上来的时候，灯还开着。|Sáng nay lúc em đến, đèn vẫn còn bật.
刘明>我这几天忙坏了，可能走的时候忘关了。|Mấy hôm nay anh bận muốn chết, chắc lúc đi quên tắt.
王一雪>冰箱不能用，这些吃的东西放在哪儿？|Tủ lạnh không dùng được, mấy thứ đồ ăn này để đâu?
刘明>不可能吧？冰箱是新买的，我来看看。|Không thể nào? Tủ lạnh mới mua mà, để anh xem.
王一雪>洗衣机也坏了吗？|Máy giặt cũng hỏng rồi à?
刘明>没坏，但是卫生间没打扫好，还不能洗衣服。|Không hỏng, nhưng nhà vệ sinh chưa dọn xong, vẫn chưa giặt đồ được.
王一雪>星期天我们真的能搬家吗？|Chủ nhật chúng ta thật sự chuyển nhà được không?
"""), q=Q("""
他们家的冰箱怎么了？|冰箱不能用了。|Tủ lạnh không dùng được.
为什么不能洗衣服？|因为卫生间没打扫好。|Vì nhà vệ sinh chưa dọn xong.
""")),
 dict(t="课文3", scene="在家里，刘明和王一雪在客厅聊天儿。", scene_vi="Lưu Minh và Vương Nhất Tuyết đang trò chuyện trong phòng khách ở nhà.", narr=False, lines=T("""
王一雪>这个月花了不少钱。|Tháng này tiêu không ít tiền.
刘明>是的，我们买了很多搬家时要用的东西。|Đúng vậy, chúng ta mua rất nhiều đồ cần dùng khi chuyển nhà.
王一雪>咱们办张信用卡吧，花的钱可以慢慢还。听说中国银行的服务不错，办了信用卡买东西还能便宜。|Chúng ta làm một cái thẻ tín dụng đi, tiền đã tiêu có thể trả dần. Nghe nói ngân hàng Trung Quốc phục vụ khá tốt, làm thẻ tín dụng rồi mua đồ còn được rẻ hơn.
刘明>好啊！中国银行很近，走路几分钟就能到。咱们什么时候去？|Được đấy! Ngân hàng Trung Quốc rất gần, đi bộ vài phút là tới. Khi nào chúng ta đi?
王一雪>今天下午？|Chiều nay nhé?
刘明>我下午要去医院，很晚才能回来。|Chiều anh phải đi bệnh viện, rất muộn mới về được.
王一雪>那我下午自己去吧。|Vậy chiều em tự đi vậy.
"""), q=Q("""
王一雪为什么想办信用卡？|因为花的钱可以慢慢还，买东西还能便宜。|Vì tiền tiêu có thể trả dần, mua đồ còn được rẻ.
王一雪想什么时候去银行？|今天下午。|Chiều nay.
刘明为什么今天不能去银行？|因为他下午要去医院，很晚才能回来。|Vì chiều anh ấy phải đi bệnh viện, rất muộn mới về.
""")),
 dict(t="课文4", scene="在家里，刘明和王一雪讨论搬家计划。", scene_vi="Lưu Minh và Vương Nhất Tuyết đang ở trong nhà thảo luận về kế hoạch chuyển nhà.", narr=False, lines=T("""
刘明>我觉得这个星期就能搬家。我明天去买一些纸箱，很快就能准备好。搬家那天，我想请几位朋友来帮忙，最多一天就能搬完。|Anh nghĩ tuần này là chuyển nhà được rồi. Mai anh đi mua ít thùng giấy, rất nhanh là chuẩn bị xong. Hôm chuyển nhà, anh muốn mời mấy người bạn đến giúp, nhiều nhất một ngày là chuyển xong.
王一雪>我觉得下个月才能搬家。这周开始准备，下周去打扫新家，这么多事情最少需要两个星期才能做完。搬家那天，我们应该找一家搬家公司。|Em nghĩ phải tháng sau mới chuyển được. Tuần này bắt đầu chuẩn bị, tuần sau đi dọn nhà mới, nhiều việc thế này ít nhất cần hai tuần mới làm xong. Hôm chuyển nhà, chúng ta nên tìm một công ty chuyển nhà.
"""), q=Q("""
刘明明天去买什么？|他明天去买一些纸箱。|Anh ấy mai đi mua ít thùng giấy.
王一雪打算下周做什么？|下周去打扫新家。|Tuần sau đi dọn nhà mới.
刘明打算找谁搬家？王一雪呢？|刘明想请几位朋友来帮忙，王一雪想找一家搬家公司。|Lưu Minh muốn nhờ bạn bè, Nhất Tuyết muốn thuê công ty chuyển nhà.
"""))],
grammar=[
 G("ting", "程度副词“挺”", "Phó từ chỉ mức độ “挺”",
   "“挺” thường dùng trong văn nói, đặt trước tính từ hoặc động từ chỉ tâm lý, biểu thị mức độ tương đối cao (khá, rất). Cấu trúc cơ bản: 挺 + tính từ / động từ tâm lý + 的.",
   [F("S:Chủ ngữ|kw:挺|A:Tính từ / động từ tâm lý|kw:的", [
     ("这个小区环境|[挺]|好|[的]", "。", "Môi trường khu nhà này khá tốt."),
     ("这家饭馆的菜|[挺]|好吃|[的]", "。", "Món ăn của quán này khá ngon."),
     ("买这个吧，我|[挺]|喜欢这个颜色|[的]", "。", "Mua cái này đi, mình khá thích màu này."),
     ("今天的天气|[挺]|热|[的]", "。", "Thời tiết hôm nay khá nóng.")])]),
 G("huaile", "程度补语（1）：……坏了", "Bổ ngữ trình độ (1) – “……坏了”",
   "Bổ ngữ trình độ “坏了” đặt sau tính từ (hoặc động từ tâm lý), biểu thị mức độ rất cao, mang ngữ khí cường điệu (… muốn chết, … quá chừng), thường dùng trong các tình huống tiêu cực.",
   [F("S:Chủ ngữ|A:Tính từ|kw:坏了", [
     ("我这几天|忙|[坏了]", "。", "Mấy hôm nay tôi bận muốn chết."),
     ("我|渴|[坏了]", "，哪里能买水？", "Tôi khát quá chừng, ở đâu mua được nước?"),
     ("这几天非常忙，大家都|累|[坏了]", "。", "Mấy hôm nay rất bận, mọi người đều mệt rã rời."),
     ("找不到护照，他|急|[坏了]", "。", "Không tìm thấy hộ chiếu, anh ấy sốt ruột lắm.")])]),
 G("jiucai", "“就”和“才”", "Phó từ “就” và “才”",
   "“就” và “才” đặt trước động từ làm trạng ngữ. “就” biểu thị người nói cho rằng hành động xảy ra sớm, nhanh, thuận lợi; “才” biểu thị người nói cho rằng hành động xảy ra muộn, chậm, không thuận lợi. Câu có “就” thường có “了” ở cuối, câu có “才” thì không dùng “了”.",
   [F("T:Thời gian / điều kiện|kw:就 / 才|V:Động từ", [
     ("中国银行很近，走路几分钟|[就]|能到", "。", "Ngân hàng Trung Quốc rất gần, đi bộ vài phút là tới."),
     ("我下午要去医院，很晚|[才]|能回来", "。", "Chiều tôi phải đi bệnh viện, rất muộn mới về được."),
     ("我早上五点|[就]|起床了", "。", "Tôi dậy từ năm giờ sáng rồi."),
     ("坐火车去北京，五个小时|[才]|能到", "。", "Đi tàu hỏa đến Bắc Kinh, năm tiếng mới tới.")])]),
],
test=dict(
 l2=["关门|买手机|办信用卡", "坏了|还能用|是新买的", "带个花园|现在没人住|能马上搬进去"],
 l3=["家离学校远|孩子上高中了|家离商场太近", "搬家|休息|准备搬家的东西", "要还信用卡|买东西能便宜点儿|想在手机上买东西", "花了很多钱|每个月都要还钱|银行离家挺远的"],
 r1=(["我很喜欢这里的环境。", "好，我马上让小王去买。", "那我去外面再看一会儿书。", "对，我看电视看到两点多才休息。", "当然。我们先坐公交车，然后换地铁。", "周五到下周一不上班，可以休息休息。"],
     ["公司里没有白纸了。", "这几天大家都忙坏了。", "我要睡觉了，你关一下灯吧。", "你觉得咱们搬到这个小区怎么样？", "你看起来有点儿累，是不是昨天睡得很晚？"]),
 r2=(["需要", "冰箱", "听说", "花园", "鞋", "卫生间"],
     ["（　　）你护照丢了，找到了吗？", "那边有一个（　　），咱们去走走吧。", "我家离公司太远了，我（　　）换个近点儿的小区。", "A：（　　）在哪儿？你知道吗？\nB：知道，在二层，你从这儿上去就能看到。", "A：妈妈，我回来了，现在又热又渴。\nB：我买了冰激凌，在（　　）里，你自己去拿。"]),
 r3=[("我们小区的环境挺好的，里面还有一个花园，很多人吃完晚饭后都会去那里走一走，休息休息。", "那个小区：", "不能休息|环境不错|旁边有个花园"),
     ("下周就要搬新家了，咱们明天去打扫一下吧。还要再买几个纸箱，你看，这些东西都需要放在箱子里。", "他们明天要做什么？", "搬家|拿箱子|打扫新家"),
     ("下个星期我就要搬家了，我今天给搬家公司打了一个电话，没想到搬家那么贵。我现在住在四层，新家在十层，搬一个箱子要50块钱。看着我那30多个箱子，我想今天晚上我就在家给朋友们打电话吧。",
      ("他的新家在几层？", "一层|四层|十层"), ("他可能会怎么搬家？", "自己搬家|请朋友帮忙|找搬家公司"))],
 w1=["银行（kǎ）明天就能办好。", "家里的（dēng）坏了，你去买个新的吧。", "我家住在三（céng），302号。"],
 w2=[("关", "你走的时候别忘了关电脑。"), ("搬", "他们正在搬一个大箱子。"), ("打扫", "搬家以前，他们在打扫房间。")],
 gl={"11": "Công ty hết giấy trắng rồi. → B: Được, tôi bảo Tiểu Vương đi mua ngay.",
     "12": "Mấy hôm nay mọi người đều bận muốn chết. → F: Từ thứ Sáu đến thứ Hai tuần sau không đi làm, có thể nghỉ ngơi.",
     "13": "Mình đi ngủ đây, bạn tắt đèn giúp nhé. → C: Vậy mình ra ngoài đọc sách thêm lát nữa.",
     "14": "Bạn thấy chúng ta chuyển đến khu nhà này thế nào? → A: Mình rất thích môi trường ở đây.",
     "15": "Trông bạn hơi mệt, có phải hôm qua ngủ muộn không? → D: Đúng, mình xem TV đến hơn hai giờ mới đi ngủ.",
     "16": "听说你护照丢了 – nghe nói hộ chiếu của bạn bị mất. → C 听说.",
     "17": "Đằng kia có một vườn hoa, chúng ta ra đi dạo đi. → D 花园.",
     "18": "我需要换个近点儿的小区 – tôi cần đổi sang khu nhà gần hơn. → A 需要.",
     "19": "Nhà vệ sinh ở đâu? — Ở tầng hai. → F 卫生间.",
     "20": "Kem để trong tủ lạnh. → B 冰箱.",
     "21": "“环境挺好的” → B 环境不错 (vườn hoa ở bên trong khu, không phải bên cạnh).",
     "22": "“咱们明天去打扫一下吧” → C 打扫新家.",
     "23": "“新家在十层” → C.",
     "24": "Chuyển nhà đắt quá nên “今天晚上我就在家给朋友们打电话吧” → B nhờ bạn bè giúp."}),
)
