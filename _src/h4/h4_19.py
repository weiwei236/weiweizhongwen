# -*- coding: utf-8 -*-
# HSK 4下 – Bài 19: 他们都很棒
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[19] = dict(zh="他们都很棒", vi="Họ đều rất tuyệt",
intro="Lưu Tiểu Tuyết tập kịch nói cho lễ hội nghệ thuật của trường; Lý Văn mời các bạn đến Nhà hát Lớn Quốc gia xem Kinh kịch và cả nhóm được xem một buổi biểu diễn đặc sắc; Bạch Gia Nguyệt viết nhật ký về cuốn “Du ký Marco Polo”.",
vocab=V("""
话剧|huàjù|dt|kịch nói|我们班要演一个话剧。~Lớp chúng tôi sắp diễn một vở kịch nói.
排|pái|dong|tập dượt (biểu diễn)|他们正在排新节目。~Họ đang tập tiết mục mới.
艺术|yìshù|dt|nghệ thuật|她对艺术很感兴趣。~Cô ấy rất quan tâm đến nghệ thuật.
内心|nèixīn|dt|nội tâm, trong lòng|我内心非常感谢你。~Trong lòng tôi vô cùng biết ơn bạn.
自信|zìxìn|tt|tự tin|她说话的时候很自信。~Cô ấy nói chuyện rất tự tin.
少年|shàonián|dt|thiếu niên|这是一个关于少年的故事。~Đây là câu chuyện về một thiếu niên.
歌手|gēshǒu|dt|ca sĩ|她的梦想是当一名歌手。~Ước mơ của cô ấy là trở thành ca sĩ.
歌声|gēshēng|dt|tiếng hát|她的歌声很好听。~Tiếng hát của cô ấy rất hay.
度假|dùjià|dong|đi nghỉ mát|我们全家去海边度假了。~Cả nhà tôi đi biển nghỉ mát.
演员|yǎnyuán|dt|diễn viên|他是一位有名的演员。~Anh ấy là một diễn viên nổi tiếng.
演唱|yǎnchàng|dong|biểu diễn (hát)|她在晚会上演唱了一首歌。~Cô ấy hát một bài trong buổi dạ tiệc.
留下|liúxia|dong|để lại, lưu lại|这次旅行给我留下了很深的印象。~Chuyến đi này để lại cho tôi ấn tượng rất sâu.
青年|qīngnián|dt|thanh niên|他是一位优秀的青年作家。~Anh ấy là một nhà văn trẻ xuất sắc.
观众|guānzhòng|dt|khán giả|观众们都很喜欢这个节目。~Khán giả đều rất thích tiết mục này.
功课|gōngkè|dt|bài vở; sự chuẩn bị|去旅游前要先做做功课。~Trước khi đi du lịch phải tìm hiểu trước.
转发|zhuǎnfā|dong|chuyển tiếp, chia sẻ lại|我把这条消息转发给你了。~Tôi đã chuyển tiếp tin này cho bạn.
入口|rùkǒu|dt|lối vào|我们在公园入口见。~Chúng ta gặp nhau ở lối vào công viên.
国家大剧院|Guójiā Dàjùyuàn|rieng|Nhà hát Lớn Quốc gia|国家大剧院在天安门附近。~Nhà hát Lớn Quốc gia ở gần Thiên An Môn.
京剧|Jīngjù|rieng|Kinh kịch|京剧是中国的国粹。~Kinh kịch là tinh hoa văn hóa của Trung Quốc.
梅兰芳|Méi Lánfāng|rieng|Mai Lan Phương|梅兰芳是著名的京剧艺术家。~Mai Lan Phương là nghệ sĩ Kinh kịch nổi tiếng.
入|rù|dong|vào|观众陆续入场了。~Khán giả lần lượt vào chỗ.
指|zhǐ|dong|chỉ, trỏ|他指着地图说：“我们在这儿。”~Anh ấy chỉ vào bản đồ nói: “Chúng ta ở đây.”
功夫|gōngfu|dt|công phu, tay nghề|他的书法很有功夫。~Thư pháp của ông ấy rất có công phu.
获奖|huòjiǎng|dong|đoạt giải|她的作品在比赛中获奖了。~Tác phẩm của cô ấy đoạt giải trong cuộc thi.
奖|jiǎng|dt|giải thưởng|他得了一等奖。~Anh ấy đạt giải nhất.
期待|qīdài|dong|mong đợi|我很期待这次旅行。~Tôi rất mong chờ chuyến đi này.
鼓掌|gǔzhǎng|dong|vỗ tay|演出结束，观众热烈鼓掌。~Buổi diễn kết thúc, khán giả vỗ tay nhiệt liệt.
邀请|yāoqǐng|dong|mời|他邀请我参加他的生日晚会。~Anh ấy mời tôi dự tiệc sinh nhật.
庆祝|qìngzhù|dong|chúc mừng, ăn mừng|我们一起庆祝新年吧。~Chúng ta cùng đón mừng năm mới nhé.
点头|diǎntóu|dong|gật đầu|他点头表示同意。~Anh ấy gật đầu tỏ ý đồng ý.
作品|zuòpǐn|dt|tác phẩm|这是他最有名的作品。~Đây là tác phẩm nổi tiếng nhất của ông ấy.
作者|zuòzhě|dt|tác giả|这本书的作者是谁？~Tác giả cuốn sách này là ai?
世纪|shìjì|dt|thế kỷ|这座桥是十九世纪建的。~Cây cầu này được xây vào thế kỷ 19.
读者|dúzhě|dt|độc giả|这本书很受读者欢迎。~Cuốn sách này rất được độc giả yêu thích.
作家|zuòjiā|dt|nhà văn|她是一位著名的作家。~Bà ấy là một nhà văn nổi tiếng.
版|bǎn|dt|bản, phiên bản|这本书有英文版。~Cuốn sách này có bản tiếng Anh.
文章|wénzhāng|dt|bài văn, bài viết|这篇文章写得很好。~Bài viết này viết rất hay.
全部|quánbù|dt|toàn bộ|作业我已经全部做完了。~Bài tập tôi đã làm xong toàn bộ.
整理|zhěnglǐ|dong|sắp xếp, chỉnh lý|我把房间整理了一下。~Tôi đã sắp xếp lại phòng một chút.
文字|wénzì|dt|chữ viết, văn tự|这本书的文字很美。~Văn phong cuốn sách này rất đẹp.
图片|túpiàn|dt|hình ảnh|这本书里有很多图片。~Cuốn sách này có rất nhiều hình ảnh.
报考|bàokǎo|dong|đăng ký dự thi|她打算报考研究生。~Cô ấy định đăng ký thi cao học.
文学|wénxué|dt|văn học|他很喜欢中国文学。~Anh ấy rất thích văn học Trung Quốc.
马可·波罗|Mǎkě·Bōluó|rieng|Marco Polo|马可·波罗是意大利旅行家。~Marco Polo là nhà du hành người Ý.
意大利|Yìdàlì|rieng|Ý (Italia)|意大利的面条很有名。~Mì Ý rất nổi tiếng.
"""),
texts=[dict(t="课文1", scene="在家里，王一雪和刘小雪谈小雪学校艺术节节目排练情况。", scene_vi="Ở nhà, Vương Nhất Tuyết và Lưu Tiểu Tuyết nói về việc tập tiết mục cho lễ hội nghệ thuật ở trường của Tiểu Tuyết.", narr=False, lines=T("""
王一雪>小雪，你们的话剧排好了吗？|Tiểu Tuyết, vở kịch của các con tập xong chưa?
刘小雪>差不多了，妈妈。艺术节周五下午开始，我内心还是有些紧张，有时候不是忘词，就是忘记做动作。|Gần xong rồi mẹ ạ. Lễ hội nghệ thuật bắt đầu chiều thứ Sáu, trong lòng con vẫn hơi hồi hộp, có lúc không quên lời thì lại quên động tác.
王一雪>没事，妈妈相信你一定可以。放松些，再自信些！|Không sao, mẹ tin con nhất định làm được. Thả lỏng chút, tự tin thêm chút!
刘小雪>好的，我同学演少年歌手，他的歌声美极了。我演他的妈妈，不知道像不像呢。|Vâng, bạn con đóng vai ca sĩ thiếu niên, giọng hát hay lắm. Con đóng vai mẹ bạn ấy, không biết có giống không nữa.
王一雪>没问题的，努力做最好的自己就好。演出时，我和你爸都去给你加油。|Không sao đâu, cố gắng làm tốt nhất là được. Lúc biểu diễn, mẹ và bố đều đến cổ vũ con.
刘小雪>好的，谢谢妈妈！|Vâng, cảm ơn mẹ!
"""), q=Q("""
小雪和同学们的话剧排得怎么样了？|基本上排好了。|Về cơ bản đã tập xong.
小雪紧张时会怎么样？|不是忘词，就是忘记做动作。|Không quên lời thì quên động tác.
小雪的同学唱歌怎么样？|特别好听，歌声美极了。|Rất hay, giọng hát tuyệt vời.
小雪演出时，妈妈和爸爸会去看吗？|会，他们都去给她加油。|Có, cả hai đều đến cổ vũ.
""")),
 dict(t="课文2", scene="周六，李文和白家月、安妮、陈天中视频通话。", scene_vi="Thứ Bảy, Lý Văn gọi video với Bạch Gia Nguyệt, Annie và Trần Thiên Trung.", narr=False, lines=T("""
李文>下周六晚上，我请大家去国家大剧院看京剧，怎么样？|Tối thứ Bảy tuần sau, mình mời mọi người đến Nhà hát Lớn Quốc gia xem Kinh kịch, thế nào?
安妮>好啊。我小时候在加拿大度假时，在宾馆的电视上看过一次，是梅兰芳等演员演的，演员们都非常棒，他们演唱得好听极了，给我留下的印象特别深。|Hay đấy. Hồi nhỏ đi nghỉ ở Canada, mình từng xem một lần trên tivi khách sạn, do Mai Lan Phương và các diễn viên khác diễn, ai cũng tuyệt, hát hay vô cùng, để lại cho mình ấn tượng rất sâu.
李文>梅兰芳先生是中国著名京剧艺术家。咱们要看的这个京剧是青年演员们演的，要去看的观众也特别多。|Ông Mai Lan Phương là nghệ sĩ Kinh kịch nổi tiếng của Trung Quốc. Vở Kinh kịch chúng ta sắp xem do các diễn viên trẻ diễn, khán giả đi xem cũng rất đông.
陈天中>不知道我们能不能看懂。|Không biết chúng mình có xem hiểu không.
白家月>咱们先做做功课，提前了解下，能懂一点儿是一点儿。|Chúng mình tìm hiểu trước một chút, hiểu được chút nào hay chút đó.
陈天中>对，我先去网上查资料，查完后也转发给你们。|Đúng, mình lên mạng tra tài liệu trước, tra xong chuyển cho các cậu.
安妮>谢谢天中！|Cảm ơn Thiên Trung!
李文>那我就在网上订票了，到时候咱们在大剧院入口见。|Vậy mình đặt vé online nhé, đến lúc đó gặp nhau ở lối vào nhà hát.
"""), q=Q("""
下周六晚上，李文请大家去做什么？|去国家大剧院看京剧。|Đến Nhà hát Lớn Quốc gia xem Kinh kịch.
在加拿大时安妮就看过京剧，她觉得怎么样？|演员们都非常棒，演唱得好听极了，给她留下的印象特别深。|Diễn viên rất tuyệt, hát rất hay, để lại ấn tượng sâu.
白家月说的“做功课”最可能是什么意思？|提前了解。|Tìm hiểu trước.
李文最后说他要去做什么？|在网上订票。|Đặt vé online.
""")),
 dict(t="课文3", scene="精彩的演出", scene_vi="Buổi biểu diễn đặc sắc", narr=True, lines=T("""
周六晚上，李文等四人来到国家大剧院观看京剧演出。|Tối thứ Bảy, Lý Văn cùng bốn người đến Nhà hát Lớn Quốc gia xem biểu diễn Kinh kịch.
入座后，李文指着节目表说：“这些演员很专业，功夫很深，在京剧比赛中获过很多奖，有的还是国家、国际大奖。我特别期待这场演出。”|Vào chỗ ngồi, Lý Văn chỉ vào tờ chương trình nói: “Các diễn viên này rất chuyên nghiệp, công phu rất sâu, đã đoạt nhiều giải trong các cuộc thi Kinh kịch, có người còn đạt giải lớn quốc gia, quốc tế. Mình rất mong chờ buổi diễn này.”
演出开始后，他们看到演员们做的动作很难，但是做得都特别好，观众们不断鼓掌。|Buổi diễn bắt đầu, họ thấy các động tác diễn viên làm rất khó nhưng đều làm rất đẹp, khán giả không ngừng vỗ tay.
因为李文他们提前把故事了解了一遍，所以差不多都看懂了。|Vì Lý Văn và các bạn đã tìm hiểu trước câu chuyện một lượt, nên gần như đều xem hiểu.
演出结束后，演员们邀请观众和他们一起庆祝演出成功。|Buổi diễn kết thúc, các diễn viên mời khán giả cùng họ chúc mừng buổi diễn thành công.
回来的路上，大家特别激动，觉得京剧很有意思，演员演得很精彩。李文点头说：“是啊，以后咱们还来看。”|Trên đường về, mọi người đều rất phấn khích, thấy Kinh kịch rất thú vị, diễn viên diễn rất đặc sắc. Lý Văn gật đầu nói: “Đúng thế, sau này chúng mình lại đến xem.”
"""), q=Q("""
李文很期待那场演出，因为什么？|演员很专业，功夫很深，获过很多奖。|Diễn viên rất chuyên nghiệp, công phu sâu, đoạt nhiều giải.
京剧演员们的表演怎么样？|动作很难，但是做得都特别好，演得很精彩。|Động tác khó nhưng làm rất đẹp, diễn rất đặc sắc.
演出结束后，演员们邀请观众一起做什么？|庆祝演出成功。|Chúc mừng buổi diễn thành công.
李文为什么说以后还来看京剧演出？|因为大家觉得京剧很有意思，演员演得很精彩。|Vì mọi người thấy Kinh kịch rất thú vị, diễn viên diễn rất hay.
""")),
 dict(t="课文4", scene="白家月的日记", scene_vi="Nhật ký của Bạch Gia Nguyệt", narr=True, lines=T("""
马可·波罗是意大利旅行家，在1275年和家人来到中国，在中国大约生活了17年，最后完成了一部作品——《马可·波罗游记》。|Marco Polo là nhà du hành người Ý, năm 1275 cùng gia đình đến Trung Quốc, sống ở Trung Quốc khoảng 17 năm, cuối cùng hoàn thành một tác phẩm — “Du ký Marco Polo”.
在这部影响很大的作品中，作者向世界介绍了13世纪时的中国。|Trong tác phẩm có ảnh hưởng rất lớn này, tác giả giới thiệu với thế giới Trung Quốc thế kỷ 13.
作为读者，读完这部作品后，我也很想成为作家，更想来中国看看。|Là độc giả, đọc xong tác phẩm này, tôi cũng rất muốn trở thành nhà văn, càng muốn đến Trung Quốc xem.
来到中国后，我发现现在的中国和书里的中国已有很大不同。|Đến Trung Quốc rồi, tôi phát hiện Trung Quốc bây giờ đã rất khác Trung Quốc trong sách.
前两天，我去书店看到了中文版的《马可·波罗游记》，马上买了一本，到家后又把这本书看了两天。|Mấy hôm trước, tôi ra hiệu sách thấy “Du ký Marco Polo” bản tiếng Trung, mua ngay một cuốn, về nhà lại đọc cuốn sách này suốt hai ngày.
看完后，我决定把自己来中国后写的文章、日记等全部整理出来，完成一部文字加图片的作品——《东方旅行日记》，再次把中国介绍给世界。|Đọc xong, tôi quyết định sắp xếp toàn bộ bài viết, nhật ký… viết từ khi đến Trung Quốc, hoàn thành một tác phẩm gồm chữ và ảnh — “Nhật ký du hành phương Đông”, một lần nữa giới thiệu Trung Quốc với thế giới.
同时我也想继续学习中文和中国文化，报考中国语言文学专业的研究生。|Đồng thời tôi cũng muốn tiếp tục học tiếng Trung và văn hóa Trung Quốc, đăng ký thi cao học chuyên ngành Ngôn ngữ và Văn học Trung Quốc.
"""), q=Q("""
《马可·波罗游记》介绍了什么内容？|13世纪的中国。|Trung Quốc thế kỷ 13.
来到中国后，白家月有什么发现？|现在的中国和书里的中国已有很大不同。|Trung Quốc ngày nay đã rất khác trong sách.
白家月看完中文版的《马可·波罗游记》之后打算做什么？|完成自己的作品《东方旅行日记》。|Hoàn thành tác phẩm của mình “Nhật ký du hành phương Đông”.
白家月后来决定读什么专业？|中国语言文学专业的研究生。|Cao học chuyên ngành Ngôn ngữ và Văn học Trung Quốc.
""")),
],
grammar=[
 G("bushi_jiushi", "选择复句“不是……，就是……”", "Câu phức lựa chọn “不是……，就是……”",
   "Biểu thị quan hệ lựa chọn: một trong hai tình huống chắc chắn xảy ra: “không… thì…”.",
   [F("S:(Chủ ngữ)|kw:不是|X:Khả năng 1|kw2:就是|V:Khả năng 2", [
     ("有时候|[不是]|忘词|[就是]|忘记做动作", "。", "Có lúc không quên lời thì lại quên động tác."),
     ("周末的时候，小文|[不是]|在家看书|[就是]|出去看演出", "。", "Cuối tuần, Tiểu Văn không ở nhà đọc sách thì ra ngoài xem biểu diễn."),
     ("杨同乐最近很忙，|[不是]|去外地出差|[就是]|在公司加班", "。", "Dạo này Dương Đồng Lạc rất bận, không đi công tác thì cũng tăng ca ở công ty.")])]),
 G("yixshiyix", "固定格式“动词+一×是一×”", "Cấu trúc cố định “Động từ + 一 × 是 一 ×”",
   "Nhấn mạnh việc cố gắng làm hết sức trong điều kiện có hạn: “… được chút nào hay chút đó”.",
   [F("V:Động từ|kw:一×|kw2:是一×|X:(Kết quả)", [
     ("咱们先做做功课，提前了解下，能懂|[一点儿]|[是一点儿]|", "。", "Chúng ta tìm hiểu trước, hiểu được chút nào hay chút đó."),
     ("虽然这本书很厚，但是我还是要看，看|[一页]|[是一页]|最后一定能看完", "。", "Tuy sách này dày, tôi vẫn muốn đọc, đọc được trang nào hay trang đó, cuối cùng chắc chắn đọc xong."),
     ("你能多吃|[一点儿]|[是一点儿]|这样身体才能好起来", "。", "Bạn ăn được thêm chút nào hay chút đó, như vậy cơ thể mới khỏe lên.")])]),
 G("ba_dongliang", "“把”字句“主语+把+宾语+动词+动量补语”", "Câu chữ “把”: Chủ ngữ + 把 + Tân ngữ + Động từ + Bổ ngữ động lượng",
   "Nhấn mạnh số lần hoặc tần suất hành động tác động lên tân ngữ. Bổ ngữ động lượng có cấu trúc “số từ + động lượng từ” (遍, 次, 下…), đứng sau động từ.",
   [F("S:Chủ ngữ|kw:把|O:Tân ngữ|V:Động từ|M:Bổ ngữ động lượng", [
     ("李文他们提前|[把]|故事|了解了|一遍", "，所以差不多都看懂了。", "Lý Văn và các bạn đã tìm hiểu trước câu chuyện một lượt, nên gần như đều hiểu."),
     ("他|[把]|这个动作|做了|好几次", "，最后终于做对了。", "Anh ấy làm động tác này mấy lần, cuối cùng cũng làm đúng."),
     ("白家月又|[把]|这本书|看了|几遍", "，越看越喜欢。", "Bạch Gia Nguyệt lại đọc cuốn sách này mấy lượt, càng đọc càng thích.")])]),
 G("ba_shiliang", "“把”字句“主语+把+宾语+动词+时量补语”", "Câu chữ “把”: Chủ ngữ + 把 + Tân ngữ + Động từ + Bổ ngữ thời lượng",
   "Nhấn mạnh độ dài thời gian chủ ngữ tác động lên tân ngữ. Từ chỉ khoảng thời gian làm bổ ngữ gọi là “bổ ngữ thời lượng”.",
   [F("S:Chủ ngữ|kw:把|O:Tân ngữ|V:Động từ|T:Bổ ngữ thời lượng", [
     ("（我）到家后又|[把]|这本书|看了|两天", "。", "Về nhà tôi lại đọc cuốn sách này suốt hai ngày."),
     ("王老师|[把]|这个问题|又讲了|十分钟", "，大家才明白。", "Thầy Vương giảng lại vấn đề này thêm mười phút, mọi người mới hiểu."),
     ("陈天中|[把]|这个动作|又练了|一小时", "。", "Trần Thiên Trung tập lại động tác này thêm một tiếng.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["文字", "留下", "内心", "艺术", "自信", "邀请"], [
   "那部作品写得很棒，给我们【留下】了很深的印象。", "收到演出【邀请】后，他们马上就开始排新节目。", "今年的【艺术】节，刘小雪参加了话剧表演。",
   "虽然没说什么，但是我【内心】很感动。", "妈妈总是鼓励我要【自信】，相信自己一定能做好。", "这部小说的【文字】很美，我都看了好几遍了。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["作家", "文章", "点头", "庆祝", "度假", "转发"], [
   "A：女儿马上放假了，今年咱们全家去哪儿【度假】？ B：郊区怎么样？那儿风景好，交通也方便。", "A：我已经把它读了好几遍了，还是记不住。 B：你理解这篇【文章】的意思了吗？你要在理解的基础上记忆。",
   "A：报纸上说，在这个国家，“【点头】”是“不”的意思。 B：是吗？我还是第一次听说。这就是文化上的不同啊！", "A：小赵，这个项目咱们怎么做？ B：听经理的吧。经理给我发了几条信息，我把他的信息【转发】给你。",
   "A：下周五是妈妈的生日，咱们给她买个礼物吧。 B：好啊，我再给她做几个她爱吃的菜，一起【庆祝】一下。", "A：我读过这本书，挺有意思的。 B：是啊，这个作者是现在最受欢迎的青年【作家】。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["上学后", "老师的鼓励", "她成为了一名优秀作家", "只是觉得有趣"], [
   "朱华从小就喜欢读书。【上学后】，她写的作文总会受到老师的表扬，老师经常把她的作文读给同学们听。【老师的鼓励】，让朱华更加自信，也更加努力。上高中后，她开始写小说。十几年后，【她成为了一名优秀作家】。她常说，那时候写文章、写小说并不是为了当作家，【只是觉得有趣】，就坚持下来了。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l19", items=[
   ("观众", "观众们看得很开心，都笑了起来。"), ("度假", "他们在海边度假，躺着看大海。"), ("演唱", "她拿着话筒在台上演唱。")]),
])
