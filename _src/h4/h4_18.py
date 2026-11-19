# -*- coding: utf-8 -*-
# HSK 4下 – Bài 18: 科技改变生活
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[18] = dict(zh="科技改变生活", vi="Công nghệ thay đổi cuộc sống",
intro="Annie đạp xe đạp công cộng đến trường của Bạch Gia Nguyệt; nhóm của Annie quay video ngắn để AI Tiểu Ngữ “làm đầu bếp” giới thiệu món ăn vặt Trung Quốc; cả ba bàn về kính AI, máy in 3D; bài cuối giới thiệu “kinh tế tận nhà”.",
vocab=V("""
猜|cāi|dong|đoán|你猜我买了什么？~Bạn đoán xem tôi mua gì?
共享单车|gòngxiǎng dānchē|cum|xe đạp công cộng (chia sẻ)|很多人骑共享单车上班。~Nhiều người đi xe đạp công cộng đi làm.
出口|chūkǒu|dt|lối ra|地铁站的出口在那边。~Lối ra của ga tàu điện ngầm ở bên kia.
推|tuī|dong|đẩy|他推着自行车走回家。~Anh ấy dắt xe đạp đi bộ về nhà.
对|duì|dong|hướng vào, nhắm vào|对着镜子笑一笑。~Cười một cái trước gương nào.
二维码|èrwéimǎ|dt|mã QR|扫一下这个二维码就可以付钱。~Quét mã QR này là có thể trả tiền.
注册|zhùcè|dong|đăng ký (tài khoản)|使用前请先注册。~Trước khi dùng vui lòng đăng ký.
费用|fèiyong|dt|chi phí, phí|这次旅行的费用不高。~Chi phí chuyến đi này không cao.
说明|shuōmíng|dt|hướng dẫn, sự giải thích|请先看一下使用说明。~Vui lòng xem hướng dẫn sử dụng trước.
办事|bànshì|dong|làm việc, giải quyết công việc|我下午要去银行办事。~Chiều nay tôi phải ra ngân hàng làm việc.
差点儿|chàdiǎnr|pho|suýt nữa|我今天差点儿迟到。~Hôm nay tôi suýt nữa đến muộn.
拍|pāi|dong|chụp, quay|我们一起拍张照片吧。~Chúng ta cùng chụp một tấm ảnh nhé.
各个|gègè|dai|các, từng|各个国家的学生都来参加了。~Học sinh từ các nước đều đến tham gia.
小组|xiǎozǔ|dt|nhóm nhỏ|我们小组有五个人。~Nhóm chúng tôi có năm người.
讨论|tǎolùn|dong|thảo luận|大家一起讨论一下这个问题。~Mọi người cùng thảo luận vấn đề này.
演|yǎn|dong|diễn, đóng vai|她在电影里演一个老师。~Cô ấy đóng vai một giáo viên trong phim.
厨师|chúshī|dt|đầu bếp|这家饭馆的厨师很有名。~Đầu bếp của quán ăn này rất nổi tiếng.
各地|gèdì|dt|các nơi|中国各地都有自己的小吃。~Các nơi ở Trung Quốc đều có món ăn vặt riêng.
著名|zhùmíng|tt|nổi tiếng|西湖是著名的景点。~Tây Hồ là danh thắng nổi tiếng.
小吃|xiǎochī|dt|đồ ăn vặt, món ăn nhẹ|这条街上有很多好吃的小吃。~Con phố này có nhiều món ăn vặt ngon.
互联网|hùliánwǎng|dt|internet|互联网让生活更方便了。~Internet khiến cuộc sống tiện lợi hơn.
点赞|diǎnzàn|dong|bấm thích (like)|很多人给这个视频点赞。~Rất nhiều người bấm thích video này.
AI眼镜|AI yǎnjìng|cum|kính AI|AI眼镜可以帮我们翻译。~Kính AI có thể giúp chúng ta dịch.
3D打印机|3D dǎyìnjī|cum|máy in 3D|用3D打印机可以做出各种东西。~Dùng máy in 3D có thể làm ra đủ thứ.
上门|shàngmén|dong|đến tận nhà|快递员上门取件。~Nhân viên giao hàng đến tận nhà lấy hàng.
到底|dàodǐ|pho|rốt cuộc|你到底想说什么？~Rốt cuộc bạn muốn nói gì?
仅|jǐn|pho|chỉ|这个工作仅用了三天就完成了。~Công việc này chỉ mất ba ngày đã xong.
多样|duōyàng|tt|đa dạng|这里的菜品丰富多样。~Món ăn ở đây phong phú đa dạng.
推出|tuīchū|dong|tung ra, ra mắt|公司推出了一款新手机。~Công ty ra mắt một mẫu điện thoại mới.
预约|yùyuē|dong|đặt hẹn, đặt trước|看病要先在网上预约。~Khám bệnh phải đặt lịch trước trên mạng.
取|qǔ|dong|lấy, nhận|我去快递站取个快递。~Tôi ra trạm chuyển phát lấy bưu phẩm.
原因|yuányīn|dt|nguyên nhân|你知道他迟到的原因吗？~Bạn biết nguyên nhân anh ấy đến muộn không?
然而|rán'ér|lien|tuy nhiên, thế nhưng|他很努力，然而成绩还是不太好。~Cậu ấy rất cố gắng, tuy nhiên thành tích vẫn chưa tốt lắm.
不必|búbì|pho|không cần|你不必担心，我能照顾自己。~Bạn không cần lo, tôi có thể tự chăm sóc mình.
亲戚|qīnqi|dt|họ hàng|春节时我们去看亲戚。~Tết chúng tôi đi thăm họ hàng.
按|àn|gioi|theo, dựa theo|请按要求完成作业。~Hãy làm bài tập theo yêu cầu.
提出|tíchū|dong|đưa ra, đề xuất|他提出了一个好建议。~Anh ấy đưa ra một đề xuất hay.
大大|dàdà|pho|rất nhiều, đáng kể|新技术大大提高了效率。~Công nghệ mới nâng cao hiệu suất đáng kể.
现有|xiànyǒu|tt|hiện có|现有的设备不够用了。~Thiết bị hiện có không đủ dùng.
"""),
texts=[dict(t="课文1", scene="周末下午，安妮骑共享单车到白家月、陈天中所在的学校，三人在学校咖啡馆聊天儿。", scene_vi="Chiều cuối tuần, Annie đạp xe đạp công cộng đến trường của Bạch Gia Nguyệt, Trần Thiên Trung, ba người trò chuyện ở quán cà phê của trường.", narr=False, lines=T("""
白家月>安妮，我们在这儿呢。|Annie, bọn mình ở đây này.
安妮>天中、家月，你们猜我是怎么过来的？|Thiên Trung, Gia Nguyệt, các cậu đoán xem mình đến bằng cách nào?
白家月>坐公交车吗？|Đi xe buýt à?
安妮>我先坐的公交车，然后骑共享单车，快到那边那个出口时又推了一小段。|Mình đi xe buýt trước, rồi đạp xe đạp công cộng, gần đến lối ra đằng kia thì dắt bộ một đoạn ngắn.
白家月>我看很多人都骑共享单车，我还没骑过呢。|Mình thấy nhiều người đi xe đạp công cộng lắm, mình còn chưa đi bao giờ.
陈天中>我骑过，很方便的。第一次骑的时候，你打开微信，对着共享单车上的二维码扫一下，在App上完成注册就可以了，怎么使用、费用标准什么的App上都有说明。|Mình đi rồi, tiện lắm. Lần đầu đi, cậu mở WeChat, quét mã QR trên xe, hoàn tất đăng ký trên App là được, cách dùng, mức phí các thứ trên App đều có hướng dẫn.
白家月>好啊！哪天我出去办事时也试试。|Hay quá! Hôm nào mình ra ngoài làm việc cũng thử xem.
"""), q=Q("""
安妮是怎么到白家月的学校的？|先坐公交车，然后骑共享单车。|Đi xe buýt trước rồi đạp xe đạp công cộng.
白家月骑过共享单车吗？|没骑过，她打算出去办事时试试。|Chưa, cô định khi ra ngoài làm việc sẽ thử.
第一次骑共享单车，需要扫码后再在App上做什么？|完成注册。|Hoàn tất đăng ký.
怎么使用、费用标准等在哪儿可以了解？|App上都有说明。|Trên App đều có hướng dẫn.
""")),
 dict(t="课文2", scene="安妮和白家月、陈天中在学校咖啡馆继续聊天儿。", scene_vi="Annie, Bạch Gia Nguyệt và Trần Thiên Trung tiếp tục trò chuyện ở quán cà phê trường.", narr=False, lines=T("""
安妮>差点儿忘了，我给你们看个短视频。|Suýt quên, mình cho các cậu xem một video ngắn.
白家月>啊？你们拍的？真不错！|Hả? Các cậu quay à? Hay thật!
安妮>对！前段时间老师留了个作业，叫各个小组拍个短视频，介绍中国美食。我们小组讨论后决定，由AI小语演厨师，做出中国各地的著名小吃。拍完后，老师说很不错。|Đúng! Thời gian trước cô giáo giao bài tập, bảo mỗi nhóm quay một video ngắn giới thiệu ẩm thực Trung Quốc. Nhóm mình thảo luận rồi quyết định để AI Tiểu Ngữ đóng vai đầu bếp, làm các món ăn vặt nổi tiếng của các vùng Trung Quốc. Quay xong cô khen hay lắm.
陈天中>嗯，语言也很幽默！|Ừ, lời thoại cũng rất hài hước!
安妮>后来这个视频让我同学放到了互联网上，很多人都来点赞。|Sau đó video này được bạn mình đăng lên mạng, rất nhiều người vào bấm thích.
白家月>看来大家都喜欢这个视频。|Xem ra mọi người đều thích video này.
安妮>后边我们打算拍第二个、第三个，让小语带大家到中国各地走一走、看一看。|Sắp tới bọn mình định quay video thứ hai, thứ ba, để Tiểu Ngữ dẫn mọi người đi dạo khắp các vùng Trung Quốc.
陈天中>这样大家就能通过你们的视频了解中国了，我支持你们！|Như vậy mọi người có thể hiểu thêm về Trung Quốc qua video của các cậu, mình ủng hộ!
"""), q=Q("""
老师留的短视频作业是关于什么的？|介绍中国美食。|Giới thiệu ẩm thực Trung Quốc.
安妮他们小组拍了什么样的短视频？|由AI小语演厨师，做出中国各地的著名小吃。|AI Tiểu Ngữ đóng vai đầu bếp làm các món ăn vặt nổi tiếng.
大家觉得安妮他们小组拍的短视频怎么样？|非常精彩，很多人都来点赞。|Rất hay, nhiều người bấm thích.
安妮后边还想拍什么短视频？|让小语带大家到中国各地走一走、看一看。|Để Tiểu Ngữ dẫn mọi người đi khắp các vùng Trung Quốc.
""")),
 dict(t="课文3", scene="科技正在改变我们的生活", scene_vi="Công nghệ đang thay đổi cuộc sống của chúng ta", narr=True, lines=T("""
安妮骑共享单车到了白家月、陈天中的学校，三人从共享单车聊到AI眼镜和3D打印机，从绿色经济聊到上门经济。|Annie đạp xe đạp công cộng đến trường của Bạch Gia Nguyệt, Trần Thiên Trung, ba người nói từ xe đạp công cộng đến kính AI và máy in 3D, từ kinh tế xanh đến kinh tế tận nhà.
科技到底对世界产生了怎样的影响？他们都认为，科技确实改变了人们的生活。|Rốt cuộc công nghệ ảnh hưởng thế nào đến thế giới? Họ đều cho rằng công nghệ quả thật đã thay đổi cuộc sống con người.
接着，安妮给大家看了她和同学们拍的短视频。|Tiếp đó, Annie cho mọi người xem video ngắn cô và các bạn quay.
安妮说，短视频是用手机拍的，他们装了一些免费的App，仅用几天就拍完了。|Annie nói video quay bằng điện thoại, họ cài một số App miễn phí, chỉ mất vài ngày đã quay xong.
视频里，小语做的小吃丰富多样，看起来好吃极了。|Trong video, món ăn vặt Tiểu Ngữ làm rất phong phú đa dạng, trông cực kỳ ngon.
短视频推出后，大家认为非常精彩，白家月和陈天中看后也特别喜欢，并且表示支持他们拍更多的视频。|Video ra mắt, mọi người thấy rất đặc sắc, Bạch Gia Nguyệt và Trần Thiên Trung xem xong cũng rất thích, đồng thời ủng hộ họ quay thêm nhiều video.
"""), q=Q("""
安妮和朋友们怎么看科技的发展？|科技确实改变了人们的生活。|Công nghệ quả thật đã thay đổi cuộc sống.
安妮他们的短视频是用什么拍的？|手机。|Điện thoại.
安妮和同学们的短视频是怎么拍的？|用手机拍，装了一些免费的App，仅用几天就拍完了。|Quay bằng điện thoại, cài App miễn phí, vài ngày là xong.
对于安妮他们拍的短视频，白家月和陈天中有什么想法？|特别喜欢，并且表示支持他们拍更多的视频。|Rất thích, ủng hộ họ quay thêm video.
""")),
 dict(t="课文4", scene="当代新经济——上门经济", scene_vi="Kinh tế mới thời nay – kinh tế tận nhà", narr=True, lines=T("""
随着互联网技术的发展，现在又出现了一种新的服务方式——上门经济，|Cùng với sự phát triển của công nghệ internet, hiện nay lại xuất hiện một hình thức dịch vụ mới — kinh tế tận nhà,
就是预约者通过网上预约，让服务人员在合适的时间到家里或者约好的地点服务，服务内容有上门做饭、照顾小动物、取东西等。|tức là người đặt hẹn đặt lịch trên mạng, để nhân viên phục vụ đến nhà hoặc địa điểm đã hẹn vào thời gian phù hợp, dịch vụ gồm nấu ăn tận nhà, chăm sóc thú cưng, lấy đồ v.v.
赵女士养了一只猫，由于工作等原因，她需要经常出差，然而又很担心猫的安全。|Chị Triệu nuôi một con mèo, vì công việc nên chị phải thường xuyên đi công tác, thế nhưng lại rất lo cho sự an toàn của mèo.
有了上门服务后，她觉得方便多了，不必再找亲戚帮忙。|Có dịch vụ tận nhà, chị thấy tiện hơn nhiều, không cần nhờ họ hàng giúp nữa.
每次出差，在网上预约并支付费用后，服务人员就会按她提出的要求上门照顾小猫，大大减轻了她的压力，赵女士也特别满意。|Mỗi lần đi công tác, đặt lịch và thanh toán trên mạng xong, nhân viên sẽ đến nhà chăm sóc mèo theo yêu cầu của chị, giảm bớt áp lực rất nhiều, chị Triệu cũng rất hài lòng.
当然，上门经济也有一些问题，特别是现有服务人员有些还不够专业，需要重新学习，提高服务质量。|Tất nhiên, kinh tế tận nhà cũng có một số vấn đề, đặc biệt là một số nhân viên hiện có chưa đủ chuyên nghiệp, cần học lại, nâng cao chất lượng dịch vụ.
"""), q=Q("""
什么是上门经济？|预约者通过网上预约，让服务人员到家里或约好的地点服务。|Đặt lịch trên mạng để nhân viên đến nhà hoặc nơi đã hẹn phục vụ.
上门服务怎么预约？|在网上预约。|Đặt lịch trên mạng.
赵女士觉得上门服务怎么样？|很方便，大大减轻了她的压力，她特别满意。|Rất tiện, giảm bớt áp lực, chị rất hài lòng.
上门经济还有什么问题？|现有服务人员有些还不够专业，需要重新学习，提高服务质量。|Một số nhân viên chưa đủ chuyên nghiệp, cần nâng cao chất lượng.
""")),
],
grammar=[
 G("yidaduan", "“数词+形容词+量词”结构", "Cấu trúc “Số từ + Tính từ + Lượng từ”",
   "Cấu trúc này mang ngữ khí khoa trương, nhấn mạnh chủ quan về độ lớn / nhỏ của số lượng. Số từ thường là “一”, tính từ thường là từ đơn âm tiết như “大, 小”, lượng từ thường là lượng từ danh từ tạm thời. Hay dùng trong khẩu ngữ.",
   [F("S:(Phần trước)|kw:一|A:大 / 小|M:Lượng từ|N:(Danh từ)", [
     ("快到那边那个出口时又推了|[一]|小|段|", "。", "Gần đến lối ra đằng kia lại dắt bộ một đoạn ngắn."),
     ("中午饿极了，吃了|[一]|大|碗|面条儿", "。", "Trưa đói lắm, ăn một bát mì to."),
     ("打开快递一看，除了衣服外，里边还有|[一]|大|包|巧克力", "。", "Mở bưu phẩm ra xem, ngoài quần áo còn có một túi sô-cô-la to.")])]),
 G("rang_jiao", "被动句“主语+让/叫+宾语+动词+其他成分”", "Câu bị động “Chủ ngữ + 让 / 叫 + Tân ngữ + Động từ + thành phần khác”",
   "Biểu thị nghĩa bị động. Chủ ngữ là người / vật chịu tác động, “让” hoặc “叫” dẫn ra người thực hiện. Thường dùng trong khẩu ngữ. Sau động từ thường có “给”, bổ ngữ hoặc trợ từ động thái.",
   [F("S:Chủ ngữ (bị tác động)|kw:让 / 叫|O:Người thực hiện|V:Động từ + thành phần khác", [
     ("后来这个视频|[让]|我同学|放到了互联网上", "。", "Sau đó video này được bạn tôi đăng lên mạng."),
     ("门|[叫]|小明|给关上了", "。", "Cửa bị Tiểu Minh đóng lại rồi."),
     ("不好意思，月饼都|[让]|我|吃了", "。", "Xin lỗi, bánh trung thu bị tôi ăn hết rồi.")])]),
 G("daodi", "语气副词“到底”", "Phó từ ngữ khí “到底”",
   "“到底” dùng trong câu hỏi, biểu thị truy hỏi, tìm hiểu đến cùng; hay dùng trong khẩu ngữ: “rốt cuộc”.",
   [F("S:Chủ ngữ|kw:到底|V:Câu hỏi", [
     ("科技|[到底]|对世界产生了怎样的影响", "？", "Rốt cuộc công nghệ ảnh hưởng thế nào đến thế giới?"),
     ("你们|[到底]|还来不来", "？", "Rốt cuộc các bạn có đến không?"),
     ("你|[到底]|是怎么想的", "？为什么不同意？", "Rốt cuộc bạn nghĩ thế nào? Sao không đồng ý?")])]),
 G("raner", "转折复句“……，然而……”", "Câu phức chuyển ngoặt “……，然而……”",
   "“然而” đứng đầu vế sau, biểu thị chuyển ngoặt. Tình huống sau “然而” tương phản với vế trước, hoặc khác với dự đoán trước đó: “tuy nhiên, thế nhưng”.",
   [F("X:Vế trước|kw:然而|V:Vế sau (tương phản)", [
     ("由于工作等原因，她需要经常出差|[然而]|又很担心猫的安全", "。", "Vì công việc, chị phải thường xuyên đi công tác, thế nhưng lại rất lo cho mèo."),
     ("毕业旅行现在越来越流行|[然而]|由于学生没什么社会和生活经验，可能会遇到各种问题", "。", "Du lịch tốt nghiệp ngày càng thịnh hành, tuy nhiên vì sinh viên ít kinh nghiệm xã hội và cuộc sống nên có thể gặp đủ vấn đề."),
     ("春天应该是花开的季节|[然而]|由于前一段时间下大雪，现在花都没开", "。", "Mùa xuân lẽ ra là mùa hoa nở, thế nhưng vì thời gian trước tuyết rơi dày, giờ hoa vẫn chưa nở.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["互联网", "猜", "提出", "按", "差点儿", "各地"], [
   "请大家【猜】一下，我手里拿的是什么东西？", "你从手机上打开使用说明，【按】说明一步一步做就行了。", "春节前，【各地】火车站都增加了服务人员，保证大家出行安全。",
   "他们【提出】了一个能够更好地保护环境的建议。", "由于早上起晚了，他们【差点儿】没赶上飞机。", "【互联网】让我们的生活越来越方便，我们可以在网上购物，也可以和在外地的父母视频聊天儿。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["推出", "不必", "到底", "讨论", "仅", "取"], [
   "A：经理，这次调查发现，还是有一些客人对我们酒店的服务不太满意。 B：我们周五开个会，【讨论】下怎么解决这个问题。", "A：这是什么菜？味道真好，我以前都没吃过。 B：您好，这是我们新【推出】的一道菜，叫香辣鱼块。",
   "A：你们的这个小船【到底】是不是用纸做的？ B：是用纸做的，但不是普通的纸。", "A：我去【取】个快递，顺便买个早餐，你想吃什么？ B：给我带两个包子吧。",
   "A：这把伞我明天就还给你。 B：你用吧，【不必】还给我了，我还有一把。", "A：这道题我们都做不出来，他【仅】用不到五分钟就做出来了。 B：我知道他特别聪明。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["病人只要有手机和网络", "线上看病一般分为以下几步", "最后才能和医生线上交流", "给人们看病提供了方便"], [
   "随着科技的发展，社会上有了一种新的看病方式——线上看病，互联网医院就这样出现了。【病人只要有手机和网络】，就可以在互联网医院线上看病。【线上看病一般分为以下几步】：首先病人根据病情选择好医院和科室，然后在网上填写姓名、身体情况和看病经历等，【最后才能和医生线上交流】。互联网医院的出现，【给人们看病提供了方便】，这种方式也越来越受到欢迎。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l18", items=[
   ("小组", "我们小组正在讨论老师留的作业。"), ("亲戚", "春节的时候很多亲戚来我家做客。"), ("办事", "他今天去银行办事了。")]),
])
