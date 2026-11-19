# -*- coding: utf-8 -*-
# HSK 4下 – Bài 20: 看不完也读不完
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[20] = dict(zh="看不完也读不完", vi="Xem không hết, đọc cũng không hết",
intro="Bạch Gia Nguyệt, Annie và Trần Thiên Trung đi tàu cao tốc đến Hàng Châu, Tô Châu; cả nhóm cùng Lý Văn bay đi Tây Song Bản Nạp (quá cảnh Tây An) xem lễ hội té nước; họ tổng kết kinh nghiệm du lịch và cảm nhận “đọc vạn quyển sách, đi vạn dặm đường”.",
vocab=V("""
堵车|dǔchē|dong|tắc đường|下班时间路上经常堵车。~Giờ tan tầm trên đường hay tắc xe.
乘|chéng|dong|đi, đáp (xe, tàu)|我们乘飞机去上海。~Chúng tôi đi máy bay đến Thượng Hải.
难道|nándào|pho|lẽ nào, chẳng lẽ|难道你不知道这件事吗？~Lẽ nào bạn không biết chuyện này sao?
无|wú|dong|không có|这趟车还有无座票。~Chuyến tàu này vẫn còn vé đứng (không ghế).
动车|dòngchē|dt|tàu cao tốc (动车)|我们坐动车去杭州。~Chúng tôi đi tàu cao tốc đến Hàng Châu.
车速|chēsù|dt|tốc độ xe|这条路上车速不能太快。~Trên đường này tốc độ xe không được quá nhanh.
列|liè|lg|đoàn, chuyến (lượng từ cho tàu)|这列火车开往北京。~Đoàn tàu này chạy về Bắc Kinh.
晚餐|wǎncān|dt|bữa tối|我们七点吃晚餐。~Chúng tôi ăn tối lúc bảy giờ.
夜|yè|dt|đêm|夜里的西湖更美。~Tây Hồ về đêm càng đẹp hơn.
大巴|dàbā|dt|xe khách lớn|我们坐大巴去苏州。~Chúng tôi đi xe khách đến Tô Châu.
杭州|Hángzhōu|rieng|Hàng Châu|杭州是一座美丽的城市。~Hàng Châu là một thành phố xinh đẹp.
西湖|Xī Hú|rieng|Tây Hồ|西湖在杭州。~Tây Hồ ở Hàng Châu.
苏州|Sūzhōu|rieng|Tô Châu|苏州离上海很近。~Tô Châu rất gần Thượng Hải.
苏州园林|Sūzhōu Yuánlín|rieng|Lâm viên Tô Châu|苏州园林非常有名。~Lâm viên Tô Châu rất nổi tiếng.
安检|ānjiǎn|dong|kiểm tra an ninh|安检完我们就去登机口。~Kiểm tra an ninh xong chúng ta ra cửa lên máy bay.
登机|dēngjī|dong|lên máy bay|飞机三点开始登机。~Ba giờ bắt đầu lên máy bay.
小说|xiǎoshuō|dt|tiểu thuyết|我很喜欢看小说。~Tôi rất thích đọc tiểu thuyết.
航班|hángbān|dt|chuyến bay|你的航班几点起飞？~Chuyến bay của bạn mấy giờ cất cánh?
值机|zhíjī|dong|làm thủ tục lên máy bay (check-in)|我们先去值机吧。~Chúng ta đi làm thủ tục check-in trước nhé.
旅客|lǚkè|dt|hành khách, du khách|请旅客们按顺序排队。~Mời quý hành khách xếp hàng theo thứ tự.
牌|pái|dt|thẻ, biển|请拿好登机牌。~Vui lòng cầm sẵn thẻ lên máy bay.
靠|kào|dong|sát, dựa vào|我的座位靠窗户。~Chỗ ngồi của tôi sát cửa sổ.
窗户|chuānghu|dt|cửa sổ|请把窗户关上。~Làm ơn đóng cửa sổ lại.
转机|zhuǎnjī|dong|quá cảnh, chuyển máy bay|我们在西安转机。~Chúng tôi quá cảnh ở Tây An.
老舍|Lǎoshě|rieng|Lão Xá|老舍是中国有名的作家。~Lão Xá là nhà văn nổi tiếng Trung Quốc.
唐诗|Tángshī|rieng|thơ Đường|她很喜欢读唐诗。~Cô ấy rất thích đọc thơ Đường.
泼水节|Pōshuǐjié|rieng|Lễ hội té nước|泼水节是傣族的传统节日。~Lễ hội té nước là ngày lễ truyền thống của dân tộc Thái.
西双版纳|Xīshuāngbǎnnà|rieng|Tây Song Bản Nạp|西双版纳在云南。~Tây Song Bản Nạp ở Vân Nam.
从中|cóngzhōng|pho|từ đó, qua đó|他们常旅行，从中了解中国。~Họ thường đi du lịch, qua đó hiểu Trung Quốc.
总结|zǒngjié|dong|tổng kết|我们要总结一下这次的经验。~Chúng ta cần tổng kết kinh nghiệm lần này.
道路|dàolù|dt|đường sá|这里的道路很宽。~Đường sá ở đây rất rộng.
特点|tèdiǎn|dt|đặc điểm|这个城市有什么特点？~Thành phố này có đặc điểm gì?
所有|suǒyǒu|tt|tất cả|所有人都同意了。~Tất cả mọi người đều đồng ý.
意见|yìjiàn|dt|ý kiến|你对这个计划有什么意见？~Bạn có ý kiến gì về kế hoạch này?
细|xì|tt|tỉ mỉ; mảnh, nhỏ|他做事想得很细。~Anh ấy làm việc suy nghĩ rất tỉ mỉ.
烦恼|fánnǎo|tt|phiền não, buồn phiền|别为这点小事烦恼。~Đừng phiền lòng vì chuyện nhỏ này.
百分之|bǎi fēn zhī|cum|phần trăm|百分之八十的同学都参加了。~80% học sinh đều đã tham gia.
节省|jiéshěng|dong|tiết kiệm|坐地铁能节省时间。~Đi tàu điện ngầm tiết kiệm được thời gian.
当|dàng|dong|coi như, xem như|你就把这儿当自己家吧。~Bạn cứ coi đây như nhà mình nhé.
红包|hóngbāo|dt|bao lì xì|过年时，孩子们都能收到红包。~Tết đến, trẻ con đều được nhận lì xì.
卷|juàn|lg|quyển (sách)|读万卷书，行万里路。~Đọc vạn quyển sách, đi vạn dặm đường.
里|lǐ|lg|dặm (đơn vị độ dài, 500m)|这里离城里有十几里路。~Từ đây đến thành phố hơn mười dặm.
要是|yàoshi|lien|nếu|要是明天下雨，我们就不去了。~Nếu mai mưa thì chúng ta không đi nữa.
少数|shǎoshù|dt|số ít, thiểu số|只有少数人不同意。~Chỉ có số ít người không đồng ý.
民族|mínzú|dt|dân tộc|中国有五十六个民族。~Trung Quốc có 56 dân tộc.
导游|dǎoyóu|dt|hướng dẫn viên du lịch|导游给我们介绍了这里的历史。~Hướng dẫn viên giới thiệu lịch sử nơi này cho chúng tôi.
解释|jiěshì|dong|giải thích|请你解释一下这个词的意思。~Bạn giải thích nghĩa của từ này giúp nhé.
泼|pō|dong|té, hắt (nước)|泼水节上大家互相泼水。~Ở lễ hội té nước, mọi người té nước vào nhau.
流利|liúlì|tt|lưu loát|他的中文说得很流利。~Anh ấy nói tiếng Trung rất lưu loát.
唐装|Tángzhuāng|rieng|Đường trang (áo truyền thống)|他穿了一件红色的唐装。~Anh ấy mặc một chiếc áo Đường trang màu đỏ.
"""),
texts=[dict(t="课文1", scene="白家月、安妮和陈天中坐动车去杭州、苏州游玩。", scene_vi="Bạch Gia Nguyệt, Annie và Trần Thiên Trung đi tàu cao tốc đến Hàng Châu, Tô Châu chơi.", narr=False, lines=T("""
安妮>终于上车了，刚刚路上堵车，差点儿晚了。|Cuối cùng cũng lên tàu rồi, lúc nãy tắc đường, suýt nữa thì trễ.
白家月>没关系，晚了就改乘下一趟。天中，你坐哪儿？看你一直不坐下，我还在想，难道你买的是无座票吗？|Không sao, trễ thì đổi sang chuyến sau. Thiên Trung, cậu ngồi đâu? Thấy cậu cứ không ngồi xuống, mình còn nghĩ, lẽ nào cậu mua vé đứng à?
陈天中>我的座位就在前边，我想先站这儿跟你们说说话。|Chỗ của mình ở ngay phía trước, mình muốn đứng đây nói chuyện với các cậu đã.
安妮>动车车速也挺快啊！对了，这列车晚上七点多到杭州，咱们在车上吃晚餐，到站后就先去西湖吧，夜里的西湖更美。|Tàu cao tốc chạy cũng nhanh ghê! À, chuyến tàu này hơn bảy giờ tối đến Hàng Châu, chúng mình ăn tối trên tàu, đến ga thì đi Tây Hồ trước nhé, Tây Hồ về đêm còn đẹp hơn.
陈天中>好！后天我们坐大巴去苏州，看苏州园林。|Được! Ngày kia chúng mình đi xe khách đến Tô Châu xem lâm viên Tô Châu.
白家月>嗯。中国太大了！真是看也看不完啊。|Ừ. Trung Quốc rộng quá! Đúng là xem cũng không hết.
"""), q=Q("""
如果安妮没有坐上车，白家月有什么建议？|坐下一趟车。|Đi chuyến tàu sau.
上车后，陈天中为什么没有直接坐到自己的座位上？|他想先站着跟大家说说话。|Cậu ấy muốn đứng nói chuyện với mọi người trước.
安妮为什么建议下车后就去西湖？|因为晚上的西湖更好看。|Vì Tây Hồ về đêm đẹp hơn.
安妮都有哪些安排？|在车上吃晚餐，到站后先去西湖。|Ăn tối trên tàu, đến ga thì đi Tây Hồ trước.
""")),
 dict(t="课文2", scene="在机场，李文和白家月、安妮、陈天中安检后准备登机去西双版纳，他们先在西安转机。", scene_vi="Ở sân bay, Lý Văn cùng Bạch Gia Nguyệt, Annie, Trần Thiên Trung qua kiểm tra an ninh, chuẩn bị bay đi Tây Song Bản Nạp, quá cảnh ở Tây An.", narr=False, lines=T("""
李文>安检完就等着登机了。你们在看什么？|Kiểm tra an ninh xong thì chờ lên máy bay thôi. Các cậu đang đọc gì thế?
白家月>我在读老舍的小说。|Mình đang đọc tiểu thuyết của Lão Xá.
陈天中>我读的是一本中国历史书。|Mình đọc một cuốn sách lịch sử Trung Quốc.
安妮>我读唐诗呢。几千年的中国文化，真是读也读不完。|Mình đọc thơ Đường. Mấy nghìn năm văn hóa Trung Quốc, đúng là đọc cũng không hết.
李文>谁说不是呢？不过，现在咱们得去排队，航班的值机员在叫大家登机呢——（值机员的话）去西安的旅客开始登机，请拿好登机牌按顺序排队。|Ai bảo không phải chứ? Nhưng giờ chúng mình phải đi xếp hàng, nhân viên chuyến bay đang gọi mọi người lên máy bay kìa — (Lời nhân viên) Hành khách đi Tây An bắt đầu lên máy bay, vui lòng cầm thẻ lên máy bay và xếp hàng theo thứ tự.
白家月>终于上来了，我的座位靠窗户。|Cuối cùng cũng lên rồi, chỗ của mình sát cửa sổ.
安妮>我在最外边。这么多人，是不是跟咱们一样，都是去感受泼水节的啊？|Mình ngồi ngoài cùng. Đông người thế, có phải đều giống chúng mình, đi trải nghiệm lễ hội té nước không nhỉ?
李文>应该不是。很多人的目的地是西安，你别忘了，咱们是在西安转机，然后再飞西双版纳。|Chắc không phải. Nhiều người điểm đến là Tây An, cậu đừng quên, chúng mình quá cảnh ở Tây An rồi mới bay tiếp đến Tây Song Bản Nạp.
"""), q=Q("""
安检完后，白家月、陈天中和安妮都在干什么？|看书。|Đọc sách.
他们这次去西双版纳要做什么？|感受泼水节。|Trải nghiệm lễ hội té nước.
安妮为什么觉得中国文化读也读不完？|因为中国有几千年的文化。|Vì Trung Quốc có mấy nghìn năm văn hóa.
李文他们的目的地是西安吗？为什么？|不是，他们只是在西安转机，目的地是西双版纳。|Không, họ chỉ quá cảnh ở Tây An, điểm đến là Tây Song Bản Nạp.
""")),
 dict(t="课文3", scene="旅行经验谈", scene_vi="Bàn về kinh nghiệm du lịch", narr=True, lines=T("""
来中国留学后，白家月、安妮和陈天中常外出旅行，从中了解中国。他们还总结出几点旅行经验：|Từ khi sang Trung Quốc du học, Bạch Gia Nguyệt, Annie và Trần Thiên Trung thường đi du lịch, qua đó tìm hiểu Trung Quốc. Họ còn tổng kết ra mấy kinh nghiệm du lịch:
第一，好计划是成功的一半。旅行前，要了解目的地天气、道路交通特点等，安排好每天的活动，保证所有人对计划都没意见。准备越细，烦恼越少。|Thứ nhất, kế hoạch tốt là một nửa thành công. Trước chuyến đi, cần tìm hiểu thời tiết, đặc điểm đường sá giao thông… ở điểm đến, sắp xếp ổn hoạt động mỗi ngày, bảo đảm mọi người đều không có ý kiến gì với kế hoạch. Chuẩn bị càng kỹ, phiền não càng ít.
第二，节假日早点儿订机票、酒店和各种门票，否则很难订到。|Thứ hai, dịp lễ tết nên đặt sớm vé máy bay, khách sạn và các loại vé vào cửa, nếu không sẽ rất khó đặt được.
第三，转机会比直飞更便宜。此次去西双版纳，在西安转机，机票价格比直飞便宜了百分之四十多。|Thứ ba, quá cảnh sẽ rẻ hơn bay thẳng. Lần này đi Tây Song Bản Nạp, quá cảnh ở Tây An, giá vé rẻ hơn bay thẳng hơn 40%.
虽然有些累，但累就累点儿吧，花更少的钱去看更多的地方，很值得，节省下来的钱就当是给自己的大“红包”了。|Tuy hơi mệt, nhưng mệt thì mệt chút vậy, tiêu ít tiền hơn mà đi được nhiều nơi hơn, rất đáng, tiền tiết kiệm được coi như “bao lì xì” lớn tặng chính mình.
"""), q=Q("""
白家月、安妮和陈天中想通过旅行做什么？|了解中国。|Tìm hiểu Trung Quốc.
他们的旅行经验首先是什么？|做好旅行计划。|Lập kế hoạch du lịch thật tốt.
为什么节假日要早点儿订机票？|否则很难订到。|Nếu không sẽ rất khó đặt được.
为什么他们觉得转机虽然累，但值得？|因为能花更少的钱去看更多的地方。|Vì tiêu ít tiền hơn mà đi được nhiều nơi hơn.
""")),
 dict(t="课文4", scene="读万卷书，行万里路", scene_vi="Đọc vạn quyển sách, đi vạn dặm đường", narr=True, lines=T("""
王一飞常对她的学生说：“读万卷书，行万里路。你们要是想多了解中国，就不能只通过读书，还要多出门旅行，否则只能认识课本里的中国。”|Vương Nhất Phi thường nói với học sinh của mình: “Đọc vạn quyển sách, đi vạn dặm đường. Các em nếu muốn hiểu thêm về Trung Quốc thì không thể chỉ qua sách vở, mà còn phải ra ngoài du lịch nhiều, nếu không chỉ biết được Trung Quốc trong sách giáo khoa thôi.”
旅行，不仅能看到自然美景，还能近距离感受不同的历史文化。|Du lịch không chỉ được ngắm cảnh đẹp thiên nhiên, mà còn được cảm nhận gần gũi những nền lịch sử văn hóa khác nhau.
比如，白家月等人想了解少数民族泼水节，就去了西双版纳。泼水节上，导游向他们解释说，被泼的水越多，新的一年就会越健康、幸福。|Ví dụ, Bạch Gia Nguyệt và các bạn muốn tìm hiểu lễ hội té nước của dân tộc thiểu số nên đã đến Tây Song Bản Nạp. Ở lễ hội, hướng dẫn viên giải thích với họ rằng bị té càng nhiều nước, năm mới sẽ càng khỏe mạnh, hạnh phúc.
安妮喜欢唐诗，就来到了西安，在那里遇到身穿唐装的“对诗人”，对诗人说上句，游客就能流利地说出下句。安妮觉得在西安，唐诗活了。|Annie thích thơ Đường nên đã đến Tây An, ở đó gặp những “người đối thơ” mặc Đường trang, người đối thơ đọc câu trên, du khách có thể lưu loát đọc ra câu dưới. Annie cảm thấy ở Tây An, thơ Đường như sống lại.
虽然已经去了很多地方，但是白家月他们觉得还不够。他们也认为，美丽中国，不只是在书中，更是在脚下。|Tuy đã đi rất nhiều nơi, nhưng Bạch Gia Nguyệt và các bạn thấy vẫn chưa đủ. Họ cũng cho rằng, Trung Quốc tươi đẹp không chỉ ở trong sách, mà còn ở dưới chân mình.
"""), q=Q("""
“读万卷书，行万里路”的意思是什么？|既读书学习，也外出看世界。|Vừa đọc sách học tập, vừa đi ra ngoài ngắm thế giới.
根据课文，旅行除了能看自然景色外，还能做什么？|了解（感受）历史文化。|Tìm hiểu (cảm nhận) lịch sử văn hóa.
安妮在西安遇见了什么人？有什么感受？|遇见了身穿唐装的“对诗人”，她觉得在西安唐诗活了。|Gặp “người đối thơ” mặc Đường trang, cô thấy thơ Đường như sống lại.
外出旅行后，白家月他们有什么感受？|觉得还不够，美丽中国不只是在书中，更是在脚下。|Thấy vẫn chưa đủ; Trung Quốc tươi đẹp không chỉ trong sách mà còn ở dưới chân.
""")),
],
grammar=[
 G("nandao", "语气副词“难道”", "Phó từ ngữ khí “难道”",
   "“难道” biểu thị ngữ khí phỏng đoán, hoặc dùng trong câu hỏi tu từ “难道……吗？” để nhấn mạnh: hình thức khẳng định mang nghĩa phủ định, hình thức phủ định mang nghĩa khẳng định. Tương đương “lẽ nào, chẳng lẽ”.",
   [F("S:(Phần trước)|kw:难道|X:Nội dung", [
     ("|[难道]|你买的是无座票", "吗？", "Lẽ nào cậu mua vé đứng à?"),
     ("车快开了他还没到，|[难道]|他不去了", "？", "Tàu sắp chạy mà anh ấy vẫn chưa đến, chẳng lẽ anh ấy không đi nữa?"),
     ("|[难道]|我们不应该保护环境", "吗？", "Lẽ nào chúng ta không nên bảo vệ môi trường sao?")])]),
 G("fanwen_yiwen", "反问句：由疑问代词构成的反问句", "Câu hỏi tu từ với đại từ nghi vấn",
   "Câu hỏi tu từ dùng các đại từ nghi vấn “谁, 什么, 怎么, 哪里, 为什么”… có tác dụng nhấn mạnh ngữ khí. Hình thức khẳng định mang nghĩa phủ định, hình thức phủ định mang nghĩa khẳng định.",
   [F("S:(Phần trước)|kw:Đại từ nghi vấn|X:(Phần sau)", [
     ("|[谁]|说不是", "呢？", "Ai bảo không phải chứ? (= đúng vậy)"),
     ("这里离苏州这么近，我们|[为什么]|不去苏州玩玩", "呢？", "Ở đây gần Tô Châu thế, sao chúng ta không đi Tô Châu chơi? (= nên đi)"),
     ("我们连手机都没有，|[怎么]|能查到这些信息", "啊？", "Chúng ta đến điện thoại cũng không có, làm sao tra được những thông tin này? (= không thể)")])]),
 G("xjiuxba", "固定格式“×就×（点儿）吧”", "Cấu trúc cố định “× 就 ×（点儿）吧”",
   "Biểu thị sự thỏa hiệp, nhượng bộ: chấp nhận tình huống như vậy cũng được. Thường dùng trong khẩu ngữ: “… thì … chút vậy”.",
   [F("A:×|kw:就|P:×（点儿）|kw2:吧", [
     ("累|[就]|累点儿|[吧]", "，花更少的钱去看更多的地方，很值得。", "Mệt thì mệt chút vậy, tiêu ít tiền mà đi được nhiều nơi, rất đáng."),
     ("我租的房子离公司有些远，我想，远|[就]|远|[吧]", "，至少房租便宜。", "Nhà tôi thuê hơi xa công ty, tôi nghĩ xa thì xa vậy, ít ra tiền thuê rẻ."),
     ("慢|[就]|慢点儿|[吧]", "，安全最重要。", "Chậm thì chậm chút vậy, an toàn là quan trọng nhất.")])]),
 G("yaoshi_fouze", "假设复句“要是……，（就）……，否则……”", "Câu phức giả thiết “要是……，（就）……，否则……”",
   "Câu phức gồm giả thiết và hệ quả. “要是……，（就）……” nêu hành động hoặc kết quả trong một điều kiện giả định; “否则” chỉ kết quả nếu không như vậy: “nếu… thì…, nếu không thì…”.",
   [F("S:(Chủ ngữ)|kw:要是|X:Giả thiết|kw2:就|V:Hành động|C:否则 + Kết quả", [
     ("你们|[要是]|想多了解中国，|[就]|不能只通过读书，还要多出门旅行|，否则只能认识课本里的中国", "。", "Các em nếu muốn hiểu thêm Trung Quốc thì không thể chỉ đọc sách, còn phải ra ngoài du lịch, nếu không chỉ biết Trung Quốc trong sách giáo khoa."),
     ("|[要是]|出去的话，咱们|[就]|爬山|，否则我哪儿都不去", "。", "Nếu đi ra ngoài thì chúng ta leo núi, nếu không thì tôi chẳng đi đâu cả."),
     ("|[要是]|你同意的话，这个计划|[就]|通过|，否则可能需要重新讨论", "。", "Nếu bạn đồng ý thì kế hoạch này được thông qua, nếu không có lẽ phải thảo luận lại.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["总结", "百分之", "登机", "烦恼", "特点", "列"], [
   "我们还没有看清楚，一【列】火车就快速开了过去。", "四点开始【登机】，我们准备下午两点到机场。", "经过努力，我们完成了一个大项目，得好好【总结】下经验。",
   "我心情不好的时候，就会干点儿自己喜欢的事情，比如听音乐，这样能让我暂时忘记【烦恼】。", "由于有【百分之】八十五的人支持，这项建议终于通过了。", "这个手机的【特点】是拍照好看，很适合年轻人。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["旅客", "流利", "意见", "难道", "转机", "解释"], [
   "A：您好，您对我们的服务有什么【意见】吗？ B：没有，挺好的，服务员很热情。", "A：这次出国旅行，你们也要【转机】吗？ B：不，这次旅行时间紧张，我们要直接飞过去。",
   "A：这位【旅客】，请问您有什么需要？ B：我想要一杯水。", "A：这个问题你都【解释】清楚了，我们完全理解，会支持你们的。 B：感谢你们的理解与支持！",
   "A：这么冷的天，你只穿了一件衬衫，【难道】不怕感冒吗？ B：我刚锻炼完，现在不觉得冷。", "A：你中文说得真【流利】！学了多久了？ B：谢谢，我已经学了四年了。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["我就出去旅行", "为了更好地了解自己国家的历史", "当时给我留下了很深的印象", "让我看见了更大的世界"], [
   "我小时候就喜欢历史方面的书。有一天上课时，老师说中华文明有五千多年的历史，【当时给我留下了很深的印象】。直到后来，学校开了历史课，老师从古代讲到现在的中国，我才真正感受到中国历史之长。【为了更好地了解自己国家的历史】，我希望自己也能够“读万卷书，行万里路”。于是，放假时，【我就出去旅行】，参观万里长城、故宫等历史文化景点。读书和旅行，【让我看见了更大的世界】。将来我也想去其他国家看看，了解更多国家的历史文化。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l20", items=[
   ("旅客", "机场里有很多旅客在等飞机。"), ("红包", "春节的时候，奶奶给了我好几个红包。"), ("大巴", "这辆大巴开往市中心。")]),
])
