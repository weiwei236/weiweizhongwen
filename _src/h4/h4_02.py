# -*- coding: utf-8 -*-
# HSK 4上 – Bài 2: 租到了合适的房子
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[2] = dict(zh="租到了合适的房子", vi="Đã thuê được căn nhà phù hợp",
intro="Bạch Gia Nguyệt đi xem nhà thuê cùng Lý Văn, tìm hiểu khu dân cư xung quanh, chuyển vào nhà mới rồi chia sẻ kinh nghiệm thuê được căn nhà ưng ý ở Trung Quốc.",
vocab=V("""
房东|fángdōng|dt|chủ nhà (cho thuê)|房东人很好，常常帮我们修东西。~Chủ nhà rất tốt, thường giúp chúng tôi sửa đồ.
出租|chūzū|dong|cho thuê|这个房子出租吗？~Căn nhà này có cho thuê không?
房租|fángzū|dt|tiền thuê nhà|这里的房租一个月三千块。~Tiền thuê nhà ở đây ba nghìn tệ một tháng.
收拾|shōushi|dong|dọn dẹp, thu dọn|周末我要收拾一下房间。~Cuối tuần tôi phải dọn dẹp phòng một chút.
租|zū|dong|thuê|我在学校附近租了一个房子。~Tôi thuê một căn nhà gần trường.
嗯|ǹg|than|ừ, ờ (tỏ ý đồng ý)|嗯，我知道了。~Ừ, tôi biết rồi.
亮|liàng|tt|sáng|这个房间又大又亮。~Căn phòng này vừa rộng vừa sáng.
就是|jiùshì|tro|(cuối câu, đi với 了) là được, cứ…|你放心就是了。~Bạn cứ yên tâm là được.
种|zhòng|dong|trồng|爷爷在院子里种了很多花。~Ông trồng rất nhiều hoa trong sân.
周围|zhōuwéi|dt|xung quanh|学校周围有很多饭馆。~Xung quanh trường có rất nhiều quán ăn.
不过|búguò|lien|nhưng, có điều|这件衣服很漂亮，不过有点儿贵。~Chiếc áo này rất đẹp, có điều hơi đắt.
毕业|bìyè|dong|tốt nghiệp|哥哥明年大学毕业。~Năm sau anh trai tôi tốt nghiệp đại học.
恐怕|kǒngpà|pho|e rằng, sợ rằng|今天恐怕会下雨。~Hôm nay e là sẽ mưa.
热闹|rènao|tt|náo nhiệt, nhộn nhịp|春节的时候，街上特别热闹。~Dịp Tết, ngoài phố đặc biệt náo nhiệt.
入住|rùzhù|dong|dọn vào ở, nhận phòng|我们下午两点可以入住酒店。~Hai giờ chiều chúng tôi có thể nhận phòng khách sạn.
日记|rìjì|dt|nhật ký|她每天晚上都写日记。~Tối nào cô ấy cũng viết nhật ký.
顺利|shùnlì|tt|thuận lợi, suôn sẻ|祝你考试顺利！~Chúc bạn thi cử thuận lợi!
并|bìng|lien|và, đồng thời; (phó từ) hoàn toàn (không)|这件事我并不知道。~Chuyện này tôi hoàn toàn không biết.
客厅|kètīng|dt|phòng khách|客厅里有一台大电视。~Trong phòng khách có một chiếc tivi lớn.
台|tái|lg|chiếc, cái (máy móc, thiết bị)|我买了一台新电脑。~Tôi đã mua một chiếc máy tính mới.
厨房|chúfáng|dt|nhà bếp|妈妈在厨房做饭。~Mẹ đang nấu cơm trong bếp.
平常|píngcháng|dt|ngày thường; bình thường|我平常七点起床。~Ngày thường tôi dậy lúc bảy giờ.
基本上|jīběnshang|pho|về cơ bản, nhìn chung|作业我基本上做完了。~Bài tập tôi về cơ bản đã làm xong.
整个|zhěnggè|tt|cả, toàn bộ|整个下午他都在图书馆。~Cả buổi chiều anh ấy đều ở thư viện.
毛巾|máojīn|dt|khăn mặt, khăn tắm|这条毛巾是新买的。~Chiếc khăn này mới mua.
建议|jiànyì|dt|đề nghị, lời khuyên; khuyên|医生建议我多休息。~Bác sĩ khuyên tôi nghỉ ngơi nhiều hơn.
查看|chákàn|dong|kiểm tra, xem xét|出门前请查看一下天气。~Trước khi ra ngoài hãy xem thời tiết một chút.
信息|xìnxī|dt|thông tin; tin nhắn|我在网上找到了很多有用的信息。~Tôi tìm được nhiều thông tin hữu ích trên mạng.
查找|cházhǎo|dong|tìm kiếm, tra tìm|我在网上查找资料。~Tôi tra tìm tài liệu trên mạng.
接着|jiēzhe|pho|tiếp theo, tiếp đó|我们先吃饭，接着去看电影。~Chúng ta ăn cơm trước, tiếp đó đi xem phim.
同时|tóngshí|lien|đồng thời, cùng lúc|他是我的老师，同时也是我的朋友。~Anh ấy là thầy tôi, đồng thời cũng là bạn tôi.
位置|wèizhì|dt|vị trí|这家饭馆的位置很好。~Vị trí của quán ăn này rất tốt.
价格|jiàgé|dt|giá cả|这里的水果价格不贵。~Giá hoa quả ở đây không đắt.
理想|lǐxiǎng|tt|lý tưởng; ước mơ|我的理想是当一名医生。~Ước mơ của tôi là trở thành bác sĩ.
由于|yóuyú|lien|do, bởi vì|由于下雨，比赛推迟了。~Do trời mưa, trận đấu bị hoãn lại.
工资|gōngzī|dt|tiền lương|他的工资比以前高了。~Lương của anh ấy cao hơn trước rồi.
感|gǎn|hau|cảm giác (hậu tố, như 安全感)|住在这里很有安全感。~Sống ở đây rất có cảm giác an toàn.
"""),
texts=[dict(t="课文1", scene="白家月想租房，李文陪白家月去看房。", scene_vi="Bạch Gia Nguyệt muốn thuê nhà, Lý Văn đi cùng cô ấy xem nhà.", narr=False, lines=T("""
房东>请进！我给你们介绍一下，这个房子有两个房间，那个大房间出租，房租每月5500元。现在已经收拾好了，想租的话，今天就可以搬进来。|Mời vào! Tôi giới thiệu với các bạn một chút, căn nhà này có hai phòng, phòng lớn kia cho thuê, tiền thuê mỗi tháng 5500 tệ. Bây giờ đã dọn dẹp xong rồi, nếu muốn thuê thì hôm nay có thể chuyển vào luôn.
白家月>嗯，这个房间真不小，还挺亮。小区离我们学校也不远。|Ừm, căn phòng này rộng thật, lại khá sáng. Khu dân cư cách trường chúng tôi cũng không xa.
房东>是的，我们小区离地铁站也很近，生活上很方便。如果决定租了，告诉我就是了。|Đúng vậy, khu chúng tôi cũng rất gần ga tàu điện ngầm, sinh hoạt rất tiện. Nếu quyết định thuê thì cứ báo tôi là được.
白家月>好的，我们再去看看外边的环境。|Vâng, chúng tôi đi xem thêm môi trường bên ngoài.
"""), q=Q("""
白家月在看的房子每个月房租是多少？|5500元。|5500 tệ.
房东要出租哪个房间？那个房间怎么样？|那个大房间，房间不小，还挺亮。|Phòng lớn, phòng khá rộng và khá sáng.
房东为什么说住在那个小区生活上很方便？|因为小区离地铁站很近。|Vì khu dân cư rất gần ga tàu điện ngầm.
""")),
 dict(t="课文2", scene="在小区里，白家月和李文继续查看周围环境。", scene_vi="Trong khu dân cư, Bạch Gia Nguyệt và Lý Văn tiếp tục xem môi trường xung quanh.", narr=False, lines=T("""
李文>家月，你看，那边还有个小花园。|Gia Nguyệt, cậu xem, bên kia còn có một khu vườn nhỏ.
白家月>嗯，这个小区到处是花，还种了不少树，周围也很安静。|Ừ, khu này đâu đâu cũng có hoa, còn trồng khá nhiều cây, xung quanh cũng rất yên tĩnh.
李文>是啊！这个小区的环境真不错，不过我听说，附近有十几家公司，很多刚毕业的学生都租住在这里。周末他们可能会玩到很晚，恐怕会影响你休息。|Đúng vậy! Môi trường khu này thật không tệ, có điều mình nghe nói gần đây có mười mấy công ty, nhiều sinh viên mới tốt nghiệp thuê ở đây. Cuối tuần họ có thể chơi đến khuya, e là sẽ ảnh hưởng đến việc nghỉ ngơi của cậu.
白家月>没关系，我还想多认识一些朋友，和他们一起玩呢。|Không sao, mình còn muốn quen thêm bạn bè, chơi cùng họ nữa.
李文>是呢，大家可以一起热闹热闹。|Cũng phải, mọi người có thể cùng nhau vui vẻ náo nhiệt.
白家月>这里房租合适，环境很好，而且房东也热情，所以我决定租这个房子了，明天就入住新家。|Ở đây tiền thuê hợp lý, môi trường tốt, chủ nhà lại nhiệt tình, nên mình quyết định thuê căn này, mai sẽ dọn vào nhà mới.
"""), q=Q("""
白家月觉得小区的环境怎么样？|很安静。|Rất yên tĩnh.
李文为什么担心周末白家月休息不好？|因为附近很多刚毕业的学生周末可能会玩到很晚。|Vì nhiều sinh viên mới tốt nghiệp ở gần đó cuối tuần có thể chơi đến khuya.
白家月为什么决定租那个房子？|因为房租合适，环境很好，而且房东也热情。|Vì tiền thuê hợp lý, môi trường tốt và chủ nhà nhiệt tình.
白家月想什么时候搬进新房子？|明天。|Ngày mai.
""")),
 dict(t="课文3", scene="搬进新家后，白家月很开心，写了一篇日记。", scene_vi="Sau khi chuyển vào nhà mới, Bạch Gia Nguyệt rất vui và viết một trang nhật ký.", narr=True, lines=T("""
8月25日，晴。|Ngày 25 tháng 8, trời nắng.
昨天我顺利租到了合适的房子，今天李文帮我搬家。|Hôm qua tôi đã thuận lợi thuê được căn nhà phù hợp, hôm nay Lý Văn giúp tôi chuyển nhà.
搬进去的时候，房东又向我介绍了一下房子里的东西，并告诉我这些东西怎么用。|Lúc chuyển vào, chủ nhà lại giới thiệu với tôi đồ đạc trong nhà, đồng thời chỉ cho tôi cách dùng những thứ đó.
我看了一下，客厅里有椅子、沙发，还有一台大电视；|Tôi xem qua một chút, trong phòng khách có ghế, sofa, còn có một chiếc tivi lớn;
厨房里有冰箱和一些做饭用的东西，不过，我平常主要在学校食堂吃，基本上不做饭。|trong bếp có tủ lạnh và một số đồ nấu ăn, có điều ngày thường tôi chủ yếu ăn ở căng tin trường, về cơ bản không nấu cơm.
我租的房间里，除了一张床以外，还有一台空调、一张书桌和一把椅子。|Trong phòng tôi thuê, ngoài một chiếc giường ra còn có một cái điều hòa, một bàn học và một chiếc ghế.
看完整个房子后，我准备再去买几条毛巾，其他东西还不需要。|Xem xong cả căn nhà, tôi định đi mua thêm vài chiếc khăn, những thứ khác thì chưa cần.
"""), q=Q("""
白家月租的房子，客厅里都有什么？|有椅子、沙发和一台大电视。|Có ghế, sofa và một chiếc tivi lớn.
白家月平常主要在哪儿吃饭？|在学校食堂。|Ở căng tin trường.
白家月租的房间里都有什么？|有一张床、一台空调、一张书桌和一把椅子。|Có một chiếc giường, một cái điều hòa, một bàn học và một chiếc ghế.
白家月准备去买什么？|几条毛巾。|Vài chiếc khăn.
""")),
 dict(t="课文4", scene="怎样租到合适的房子", scene_vi="Làm thế nào để thuê được căn nhà phù hợp", narr=True, lines=T("""
在李文的帮助下，白家月租到了合适的房子。|Nhờ sự giúp đỡ của Lý Văn, Bạch Gia Nguyệt đã thuê được căn nhà phù hợp.
对白家月来说，这次租房并不容易。|Đối với Bạch Gia Nguyệt, lần thuê nhà này hoàn toàn không dễ dàng.
根据李文的建议，她先在租房网站和App上查看有关信息，查找合适的房子，接着又去看了看房子，同时了解房子周围的环境。|Theo lời khuyên của Lý Văn, trước tiên cô xem thông tin liên quan trên các trang web và ứng dụng thuê nhà, tìm căn phù hợp, tiếp đó đi xem nhà, đồng thời tìm hiểu môi trường xung quanh.
她看了好几个房子，才找到一个位置、环境和价格都合适的，最后顺利租到了理想的房子。|Cô xem mấy căn nhà mới tìm được một căn có vị trí, môi trường và giá cả đều phù hợp, cuối cùng đã thuận lợi thuê được căn nhà lý tưởng.
租房的时候，李文告诉白家月，在中国，由于很多刚工作的年轻人工资还不太高，所以他们一开始也不买房，都选择租房。|Lúc thuê nhà, Lý Văn nói với Bạch Gia Nguyệt rằng ở Trung Quốc, do nhiều người trẻ mới đi làm lương chưa cao lắm, nên ban đầu họ không mua nhà mà đều chọn thuê.
工作几年后，不少人就会买房，因为大家一直觉得，有房才有家，有自己的房子会更有安全感。|Đi làm vài năm, không ít người sẽ mua nhà, vì mọi người luôn cho rằng có nhà mới có gia đình, có nhà riêng sẽ có cảm giác an toàn hơn.
"""), q=Q("""
白家月觉得这次租房怎么样？|不容易。|Không dễ dàng.
白家月是怎么租到合适的房子的？|她先在网上查看信息，查找合适的房子，接着去看房子，同时了解周围的环境。|Cô xem thông tin trên mạng, tìm căn phù hợp, rồi đi xem nhà và tìm hiểu môi trường xung quanh.
很多刚工作的年轻人为什么选择租房？|因为他们的工资还不太高。|Vì lương của họ chưa cao lắm.
在中国，为什么不少人工作几年后会买房？|因为大家觉得有房才有家，有自己的房子会更有安全感。|Vì mọi người cho rằng có nhà mới có gia đình, có nhà riêng sẽ có cảm giác an toàn hơn.
"""))],
grammar=[
 G("jiushile", "固定格式“×就是了”", "Cấu trúc cố định “× 就是了”",
   "Dùng trong khẩu ngữ, đặt ở cuối câu để khẳng định, trấn an: “cứ… là được”, “… thôi mà”.",
   [F("X:Điều kiện / tình huống|V:Hành động|kw:就是了", [
     ("如果决定租了|告诉我|[就是了]", "。", "Nếu quyết định thuê thì cứ báo tôi là được."),
     ("我一定能办到|您放心|[就是了]", "。", "Tôi nhất định làm được, ngài cứ yên tâm."),
     ("这次考得不好没关系|下次努力|[就是了]", "。", "Lần này thi không tốt cũng không sao, lần sau cố gắng là được.")])]),
 G("buguo", "转折复句“……，不过……”", "Câu phức chuyển ngoặt “……，不过……”",
   "Liên từ “不过” đứng đầu vế sau, biểu thị ý chuyển ngoặt: “nhưng, có điều”. Ngữ khí nhẹ hơn “但是”.",
   [F("X:Vế trước|kw:不过|V:Vế sau (chuyển ý)", [
     ("这个小区的环境真不错|[不过]|我听说附近有十几家公司，很多刚毕业的学生都租住在这里", "。", "Môi trường khu này thật không tệ, có điều nghe nói gần đây có mười mấy công ty, nhiều sinh viên mới tốt nghiệp thuê ở đây."),
     ("我们在动物园看见了很多动物|[不过]|没看见大熊猫", "。", "Chúng tôi thấy nhiều động vật ở sở thú, nhưng không thấy gấu trúc."),
     ("我刚来北京时还不太习惯这里的天气|[不过]|很快就适应了", "。", "Lúc mới đến Bắc Kinh tôi chưa quen thời tiết ở đây lắm, nhưng rất nhanh đã thích nghi.")])]),
 G("bing", "连词/副词“并”", "Liên từ / phó từ “并”",
   "(1) Liên từ: nối hai động từ hai âm tiết, cụm từ hoặc mệnh đề song song, mang ý tăng tiến: “và, đồng thời”. (2) Phó từ: đứng trước từ phủ định, nhấn mạnh sự phủ định, cho biết sự thật hoàn toàn không phải như vậy: “hoàn toàn (không)”.",
   [F("S:Chủ ngữ|V1:Hành động 1|kw:并|V2:Hành động 2", [
     ("房东|又向我介绍了一下房子里的东西|[并]|告诉我这些东西怎么用", "。", "Chủ nhà lại giới thiệu đồ đạc trong nhà và chỉ cho tôi cách dùng."),
     ("她|考上了北京大学|[并]|申请到了奖学金", "。", "Cô ấy đỗ Đại học Bắc Kinh và xin được học bổng.")], cap="并 làm liên từ"),
    F("S:Chủ ngữ|kw:并|D:没 / 不|V:Vị ngữ", [
     ("我|[并]|没有|答应你就租这个房子，我还要再想想", "。", "Tôi hoàn toàn chưa hứa với anh là thuê căn này, tôi còn phải nghĩ thêm."),
     ("这次租房|[并]|不|容易", "。", "Lần thuê nhà này hoàn toàn không dễ dàng.")], cap="并 làm phó từ (nhấn mạnh phủ định)")]),
 G("youyu", "连词/介词“由于”", "Liên từ / giới từ “由于”",
   "(1) Liên từ: đứng đầu vế trước của câu phức, chỉ nguyên nhân; vế sau thường có “所以、因此 (yīncǐ – vì vậy)”. (2) Giới từ: chỉ nguyên nhân, lý do: “do, nhờ”.",
   [F("kw:由于|X:Nguyên nhân|kw2:所以 / 因此|V:Kết quả", [
     ("[由于]|很多刚工作的年轻人工资还不太高|[所以]|他们一开始也不买房，都选择租房", "。", "Do nhiều người trẻ mới đi làm lương chưa cao, nên ban đầu họ không mua nhà mà chọn thuê."),
     ("[由于]|一直下大雨|[所以]|我们决定不爬山了", "。", "Do trời mưa to suốt, nên chúng tôi quyết định không leo núi nữa."),
     ("[由于]|大家的努力||这次运动会我们班获得了第一名", "。", "Nhờ sự nỗ lực của mọi người, đại hội thể thao lần này lớp chúng tôi giành giải nhất.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["收拾", "房租", "入住", "租", "查看"], [
   "这个小区环境好，【房租】也不高，一个月才5000元。", "要【租】一个好房子也不容易，需要多多比较。", "我女儿每天都把房间【收拾】得干干净净的。",
   "这次比赛的通知已经发到大家的邮箱了，请注意【查看】。", "【入住】后我发现，宾馆房间的灯是坏的。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["周围", "建议", "查找", "客厅", "接着"], [
   "A：我最近打算在公司附近租个房子。 B：那你上网【查找】租房信息时，一定要小心，不要只看价格。", "A：你假期打算做什么？ B：我要先回家住几天，【接着】跟朋友去上海玩。",
   "A：听说小区【周围】有很多公司，很多年轻人都租住在附近。 B：是的，所以周末时特别热闹。", "A：这个房子怎么样？ B：很大，【客厅】也大，里边除了沙发以外，还有一台大电视。",
   "A：关于租什么样的房子合适，你还有什么好【建议】？ B：除了离公司近以外，我觉得生活上方便也很重要。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["就给房东打了电话", "觉得房子很不错", "她决定在公司附近租个房子", "但是很干净"], [
   "小张最近换了一个比较理想的工作。由于新公司离她现在住的地方比较远，【她决定在公司附近租个房子】。她在网上查找到一条出租信息，【就给房东打了电话】。房东说，小张要租的房子不太大，【但是很干净】，房租不高，位置也比较好。接着，房东又建议小张过去看看。小张看了以后，【觉得房子很不错】，就租了下来。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：这个房子很干净，小区也安静，我租不租呢？ B：______。（就是了）", "你喜欢的话，租下来就是了。"),
   ("A：你觉得这个手机怎么样？ B：还可以，不过______。", "还可以，不过有点儿贵。"),
   ("他毕业后来到北京工作，______。（并 / 租）", "他毕业后来到北京工作，并在公司附近租了一个房子。"),
   ("由于手机没电了，______。", "由于手机没电了，所以我没接到你的电话。")]),
 opn("用词语造句", "Dùng từ cho sẵn đặt câu.", [
   ("房东", "我们的房东很热情，常常来看我们。"), ("毛巾", "我去超市买了两条新毛巾。"), ("理想", "我终于找到了一个理想的工作。")]),
])
