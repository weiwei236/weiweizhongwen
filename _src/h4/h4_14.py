# -*- coding: utf-8 -*-
# HSK 4下 – Bài 14: 合适才买
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[14] = dict(zh="合适才买", vi="Phù hợp mới mua",
intro="Annie mua trà ở tiệm trà; chị em Vương Nhất Tuyết đi mua giày thể thao khi trung tâm thương mại giảm giá; cửa hàng nhỏ của Từ Tiền đắt khách nhờ bán đúng thứ người trẻ thích; bài cuối bàn về người mua sắm “bình tĩnh” và “không bình tĩnh”.",
vocab=V("""
茶叶|cháyè|dt|lá trà, chè|我买了一斤茶叶送给爷爷。~Tôi mua một cân trà tặng ông.
究竟|jiūjìng|pho|rốt cuộc, cuối cùng thì|你究竟想去哪儿？~Rốt cuộc bạn muốn đi đâu?
分为|fēnwéi|dong|chia thành|一年分为四个季节。~Một năm chia thành bốn mùa.
抱歉|bàoqiàn|tt|xin lỗi, áy náy|很抱歉，我来晚了。~Rất xin lỗi, tôi đến muộn.
暂时|zànshí|tt|tạm thời|这个问题暂时还没有解决。~Vấn đề này tạm thời vẫn chưa giải quyết.
满|mǎn|dong|đủ, đạt mức; đầy|买满一百元送一个杯子。~Mua đủ một trăm tệ được tặng một cái cốc.
两|liǎng|lg|lạng (50 gam)|我要买三两茶叶。~Tôi muốn mua ba lạng trà.
超过|chāoguò|dong|vượt quá|今天的气温超过了三十度。~Nhiệt độ hôm nay vượt quá ba mươi độ.
盒子|hézi|dt|cái hộp|这个盒子里装的是什么？~Trong cái hộp này đựng gì?
装|zhuāng|dong|đựng, chứa; lắp đặt|请把书装进包里。~Hãy cho sách vào túi.
各位|gèwèi|dai|các vị, mọi người|各位同学，早上好！~Chào buổi sáng các bạn!
顾客|gùkè|dt|khách hàng|这家店的顾客很多。~Cửa hàng này rất đông khách.
本|běn|dai|này, bản (của mình)|本店今天全场打八折。~Cửa hàng chúng tôi hôm nay giảm giá 20% toàn bộ.
假日|jiàrì|dt|ngày nghỉ|假日里公园里人很多。~Ngày nghỉ công viên rất đông người.
低价|dījià|dt|giá thấp, giá rẻ|这家超市常常有低价商品。~Siêu thị này thường có hàng giá rẻ.
促销|cùxiāo|dong|khuyến mãi|商场正在做促销活动。~Trung tâm thương mại đang có chương trình khuyến mãi.
广播|guǎngbō|dt|phát thanh, loa phát thanh|广播里说飞机晚点了。~Loa phát thanh nói máy bay bị trễ.
减|jiǎn|dong|giảm, bớt|这件衣服减了一百块。~Chiếc áo này giảm một trăm tệ.
广告|guǎnggào|dt|quảng cáo|电视上的广告太多了。~Quảng cáo trên tivi nhiều quá.
首先|shǒuxiān|pho|trước hết, đầu tiên|首先，我们来看第一个问题。~Trước hết, chúng ta xem vấn đề thứ nhất.
牌子|páizi|dt|nhãn hiệu, thương hiệu|你喜欢哪个牌子的手机？~Bạn thích điện thoại hãng nào?
降价|jiàngjià|dong|giảm giá|年底很多商品都降价了。~Cuối năm nhiều mặt hàng đều giảm giá.
样式|yàngshì|dt|kiểu dáng, mẫu mã|这双鞋的样式很新。~Mẫu giày này rất mới.
价钱|jiàqián|dt|giá tiền|这件衣服价钱不贵。~Chiếc áo này giá không đắt.
商业|shāngyè|dt|thương nghiệp, thương mại|这里是城市的商业中心。~Đây là trung tâm thương mại của thành phố.
商品|shāngpǐn|dt|hàng hóa, sản phẩm|超市里的商品种类很多。~Hàng hóa trong siêu thị có rất nhiều loại.
种类|zhǒnglèi|dt|chủng loại, loại|这家店的水果种类很多。~Hoa quả của cửa hàng này có rất nhiều loại.
盲盒|mánghé|dt|hộp mù (blind box)|很多年轻人喜欢买盲盒。~Nhiều người trẻ thích mua hộp mù.
缺|quē|dong|thiếu|这本书缺了两页。~Cuốn sách này thiếu hai trang.
许多|xǔduō|so|nhiều, rất nhiều|公园里有许多人在跑步。~Trong công viên có rất nhiều người đang chạy bộ.
表示|biǎoshì|dong|bày tỏ, biểu thị|大家都表示同意。~Mọi người đều bày tỏ đồng ý.
加上|jiāshàng|lien|thêm vào đó, cộng thêm|他很聪明，加上很努力，所以成绩很好。~Cậu ấy thông minh, thêm vào đó rất chăm chỉ, nên thành tích rất tốt.
态度|tàidu|dt|thái độ|这家店的服务态度很好。~Thái độ phục vụ của cửa hàng này rất tốt.
友好|yǒuhǎo|tt|thân thiện, hữu hảo|这里的人对外国人很友好。~Người ở đây rất thân thiện với người nước ngoài.
使得|shǐde|dong|khiến cho, làm cho|这场大雨使得比赛推迟了。~Trận mưa to này khiến trận đấu bị hoãn.
者|zhě|tro|người (hậu tố)|他是一位成功的研究者。~Ông ấy là một nhà nghiên cứu thành công.
仔细|zǐxì|tt|cẩn thận, tỉ mỉ|请仔细检查一下作业。~Hãy kiểm tra bài tập cẩn thận.
对于|duìyú|gioi|đối với|对于这个问题，大家有什么看法？~Đối với vấn đề này, mọi người có ý kiến gì?
不光|bùguāng|lien|không chỉ|她不光会唱歌，还会跳舞。~Cô ấy không chỉ biết hát mà còn biết nhảy.
外套|wàitào|dt|áo khoác|天冷了，出门穿上外套。~Trời lạnh rồi, ra ngoài mặc áo khoác vào.
袜子|wàzi|dt|tất, vớ|我买了三双袜子。~Tôi mua ba đôi tất.
"""),
texts=[dict(t="课文1", scene="周六上午，安妮到茶叶店买茶叶。", scene_vi="Sáng thứ Bảy, Annie đến tiệm trà mua trà.", narr=False, lines=T("""
售货员>您要什么茶？|Chị muốn mua trà gì ạ?
安妮>我先看看。这里茶叶这么多，究竟买哪种好呢？|Tôi xem trước đã. Ở đây nhiều loại trà thế, rốt cuộc mua loại nào thì tốt nhỉ?
售货员>茶叶主要分为红茶、绿茶等，看您喜欢喝哪种。|Trà chủ yếu chia thành hồng trà, trà xanh v.v., tùy chị thích uống loại nào.
安妮>我想买一些自己喝，再买些送人。这种绿茶还有吗？|Tôi muốn mua một ít để tự uống, mua thêm ít để tặng người khác. Loại trà xanh này còn không?
售货员>抱歉，暂时没有。如果自己喝，可以买这个绿茶，今天满二两送半两，超过半斤再送小礼物；如果送人，可以买个盒子装进去。|Xin lỗi, tạm thời hết rồi. Nếu tự uống, chị có thể mua loại trà xanh này, hôm nay mua đủ hai lạng tặng nửa lạng, quá nửa cân còn tặng quà nhỏ; nếu tặng người khác, có thể mua một cái hộp để đựng.
安妮>嗯。那就先买六两这种绿茶吧，再买一个盒子。请帮我分着装，盒子里装半斤，剩下的用纸包一下就行。|Ừm. Vậy trước tiên mua sáu lạng trà xanh này, mua thêm một cái hộp. Phiền anh đựng riêng giúp, trong hộp để nửa cân, chỗ còn lại gói giấy là được.
"""), q=Q("""
安妮想知道什么？|买哪种茶合适。|Mua loại trà nào thì hợp.
安妮为什么要买茶叶？|想买一些自己喝，再买些送人。|Muốn mua để tự uống và để tặng người khác.
关于买茶叶送人，售货员有什么建议？|可以买个盒子装进去。|Có thể mua một cái hộp để đựng.
安妮最后买了什么？|六两绿茶和一个盒子。|Sáu lạng trà xanh và một cái hộp.
""")),
 dict(t="课文2", scene="周日下午，王一雪想买运动鞋，王一飞陪她去商场。", scene_vi="Chiều Chủ nhật, Vương Nhất Tuyết muốn mua giày thể thao, Vương Nhất Phi đi cùng chị đến trung tâm thương mại.", narr=False, lines=T("""
广播员>各位顾客，本商场正在举办运动鞋假日低价促销活动，全场五折。|Kính thưa quý khách, trung tâm thương mại đang tổ chức chương trình khuyến mãi giá rẻ ngày nghỉ cho giày thể thao, toàn bộ giảm 50%.
王一雪>一飞，广播里说价格减了一半呢，咱们过去看看？|Nhất Phi, loa nói giá giảm một nửa đấy, mình qua xem nhé?
王一飞>好的。不过咱们也不能只听广告说什么，还得看质量。|Được. Nhưng mình cũng không thể chỉ nghe quảng cáo nói gì, còn phải xem chất lượng.
王一雪>对，首先看样子喜不喜欢，然后再看质量怎么样、价格合适不合适。|Đúng, trước hết xem kiểu dáng có thích không, sau đó xem chất lượng thế nào, giá có hợp lý không.
售货员>二位看看喜欢哪双？这个牌子质量很好，今天又降价，一双减300块。|Hai chị xem thích đôi nào? Nhãn hiệu này chất lượng rất tốt, hôm nay lại giảm giá, mỗi đôi bớt 300 tệ.
王一雪>嗯，我知道这个牌子。一飞，你喜欢吗？你看，这个鞋的样式很新，价钱也不高。|Ừ, chị biết nhãn hiệu này. Nhất Phi, em thích không? Em xem, mẫu giày này rất mới, giá cũng không cao.
王一飞>你喜欢就买吧。我再看看别的。|Chị thích thì mua đi. Em xem thêm cái khác.
王一雪>好的。请给我拿一双37号的吧。|Được. Lấy cho tôi một đôi size 37 nhé.
"""), q=Q("""
商场做的运动鞋促销活动是什么？|全场打五折。|Toàn bộ giảm 50%.
听了广播后，王一雪为什么要过去看看？|因为广播里说价格减了一半。|Vì loa nói giá giảm một nửa.
关于运动鞋，王一飞更重视什么？|质量好不好。|Chất lượng có tốt không.
王一雪是怎么决定买那双运动鞋的？|首先看样子喜不喜欢，然后看质量和价格，这双鞋牌子好、样式新、价钱也不高。|Trước xem kiểu dáng, rồi xem chất lượng và giá; đôi này hãng tốt, mẫu mới, giá không cao.
""")),
 dict(t="课文3", scene="适合，就受欢迎", scene_vi="Phù hợp thì được yêu thích", narr=True, lines=T("""
李文的朋友徐前在商业区开了家小店，专门卖年轻人喜欢的东西。|Bạn của Lý Văn là Từ Tiền mở một cửa hàng nhỏ ở khu thương mại, chuyên bán những thứ người trẻ thích.
他的店里商品种类不少，既有几十年前的老游戏机，也有最近流行的盲盒等等，很吸引年轻人。|Cửa hàng anh có khá nhiều loại hàng, vừa có máy chơi game cũ từ mấy chục năm trước, vừa có hộp mù đang thịnh hành v.v., rất thu hút người trẻ.
徐前说，自己就是年轻人，知道年轻人喜欢什么。|Từ Tiền nói, bản thân anh là người trẻ nên biết người trẻ thích gì.
他也常和来店里的年轻顾客聊天儿，了解他们的兴趣爱好。|Anh cũng thường trò chuyện với khách trẻ đến cửa hàng để tìm hiểu sở thích của họ.
前段时间刚进的盲盒很快就卖到了缺货。|Lô hộp mù mới nhập thời gian trước rất nhanh đã bán hết hàng.
许多年轻人表示，在徐前的店里能感受到快乐。|Nhiều người trẻ cho biết ở cửa hàng của Từ Tiền họ cảm thấy vui vẻ.
小店虽然小，但东西适合年轻人，加上店员态度友好，使得小店的生意越来越好。|Cửa hàng tuy nhỏ nhưng đồ phù hợp với người trẻ, thêm vào đó nhân viên thái độ thân thiện, khiến việc buôn bán ngày càng tốt.
李文觉得自己的朋友真会做生意。|Lý Văn thấy bạn mình thật biết làm ăn.
"""), q=Q("""
徐前店里卖的东西怎么样？|种类很多，都是年轻人喜欢的。|Rất nhiều loại, đều là thứ người trẻ thích.
来徐前店里的顾客主要是什么人？|年轻人。|Người trẻ.
年轻人为什么喜欢徐前店里的东西？|因为店里的东西适合年轻人，在那里能感受到快乐。|Vì đồ hợp với người trẻ, ở đó họ cảm thấy vui.
徐前店里的生意做得怎么样？|越来越好。|Ngày càng tốt.
""")),
 dict(t="课文4", scene="合适的才是最好的", scene_vi="Phù hợp mới là tốt nhất", narr=True, lines=T("""
关于购物，你是一位冷静购物者，还是不冷静购物者？|Về chuyện mua sắm, bạn là người mua sắm bình tĩnh hay không bình tĩnh?
一般来说，冷静购物者往往是真正需要一件东西时才买。|Nói chung, người mua sắm bình tĩnh thường chỉ mua khi thật sự cần một món đồ.
购买时，还会从质量、价格等各方面仔细比较。|Khi mua, họ còn so sánh kỹ về mọi mặt như chất lượng, giá cả.
不冷静购物者看见一个东西时，只要感觉喜欢就买，不管需要不需要，|Người mua sắm không bình tĩnh khi thấy một món đồ, chỉ cần thấy thích là mua, bất kể có cần hay không,
结果常常买完就后悔，买的东西也成了“垃圾”，还不环保。|kết quả thường mua xong là hối hận, đồ mua về cũng thành “rác”, lại không bảo vệ môi trường.
王一飞说，她从来不随便买东西。对于想买的东西，她不光看质量，还看价格。|Vương Nhất Phi nói cô chưa bao giờ mua đồ tùy tiện. Đối với món muốn mua, cô không chỉ xem chất lượng mà còn xem giá.
无论是一件外套，还是一条裤子，甚至一双袜子，都是仔细比较后才决定买不买。|Dù là một chiếc áo khoác, một chiếc quần, thậm chí một đôi tất, cô đều so sánh kỹ rồi mới quyết định có mua hay không.
其实，不仅是买东西，人生的很多事情都一样，选择合适的才是最好的。|Thật ra không chỉ mua sắm, nhiều việc trong đời cũng vậy, chọn cái phù hợp mới là tốt nhất.
"""), q=Q("""
冷静购物者买东西时会怎么做？|需要才买，购买时还会从质量、价格等方面仔细比较。|Cần mới mua, khi mua còn so sánh kỹ chất lượng, giá cả.
冷静购物者和不冷静购物者最大的不同是什么？|冷静购物者需要时才买，不冷静购物者喜欢就买。|Người bình tĩnh cần mới mua, người không bình tĩnh thích là mua.
买东西时王一飞会怎么做？|仔细比较后才买。|So sánh kỹ rồi mới mua.
王一飞是冷静购物者吗？为什么？|是，因为她从来不随便买东西，对想买的东西不光看质量，还看价格。|Phải, vì cô không bao giờ mua tùy tiện, xem cả chất lượng lẫn giá.
""")),
],
grammar=[
 G("jiujing", "语气副词“究竟”", "Phó từ ngữ khí “究竟”",
   "“究竟” dùng trong câu hỏi, biểu thị truy hỏi đến cùng: “rốt cuộc, cuối cùng thì”.",
   [F("S:(Chủ ngữ)|kw:究竟|V:Câu hỏi", [
     ("这里茶叶这么多，|[究竟]|买哪种好呢", "？", "Ở đây nhiều trà thế, rốt cuộc mua loại nào thì tốt?"),
     ("我一直没找到他，他|[究竟]|去哪里了呢", "？", "Tôi tìm mãi không thấy anh ấy, rốt cuộc anh ấy đi đâu rồi?"),
     ("|[究竟]|是对还是错", "？我现在也不清楚。", "Rốt cuộc là đúng hay sai? Bây giờ tôi cũng không rõ.")])]),
 G("shouxian", "承接复句“首先……，然后/其次……”", "Câu phức nối tiếp “首先……，然后 / 其次……”",
   "Biểu thị trình tự trước sau hoặc phân biệt chính – phụ: “trước hết…, sau đó / tiếp theo…”. (其次 qícì: thứ hai, tiếp theo)",
   [F("kw:首先|X:Việc thứ nhất|kw2:然后 / 其次|V:Việc tiếp theo", [
     ("[首先]|看样子喜不喜欢|[然后]|再看质量怎么样、价格合适不合适", "。", "Trước hết xem kiểu dáng có thích không, sau đó xem chất lượng, giá có hợp không."),
     ("遇到问题，[首先]|想想问题为什么出现|[然后]|再积极想办法解决", "。", "Gặp vấn đề, trước hết nghĩ xem vì sao xảy ra, sau đó tích cực tìm cách giải quyết."),
     ("请大家[首先]|读一遍课文|[然后]|根据课文完成课后练习", "。", "Mọi người hãy đọc bài khóa một lượt trước, rồi làm bài tập theo bài khóa.")])]),
 G("jiashang", "连词“加上”", "Liên từ “加上”",
   "“加上” nối tiếp câu trước, biểu thị thêm một yếu tố nữa, câu sau thường nêu kết quả: “thêm vào đó, cộng thêm”.",
   [F("X:Yếu tố 1|kw:加上|X2:Yếu tố bổ sung|V:Kết quả".replace("X2", "B"), [
     ("小店虽然小，但东西适合年轻人|[加上]|店员态度友好|使得小店的生意越来越好", "。", "Cửa hàng tuy nhỏ nhưng đồ hợp với người trẻ, thêm vào đó nhân viên thân thiện, khiến việc buôn bán ngày càng tốt."),
     ("虽然这里是郊区，但周围交通很方便|[加上]|房租便宜|所以很多年轻人都在这里租房子", "。", "Tuy đây là ngoại ô nhưng giao thông thuận tiện, cộng thêm tiền thuê rẻ, nên nhiều người trẻ thuê nhà ở đây."),
     ("他很聪明|[加上]|一直非常努力|所以最后考上了理想的大学", "。", "Cậu ấy thông minh, thêm vào đó luôn rất cố gắng, nên cuối cùng đỗ vào trường đại học mơ ước.")])]),
 G("duiyu", "介词“对于”", "Giới từ “对于”",
   "“对于” dẫn ra đối tượng cụ thể (người, việc, vật…) mà hành động liên quan đến: “đối với, về”.",
   [F("kw:对于|N:Đối tượng|V:Nội dung", [
     ("[对于]|想买的东西|她不光看质量，还看价格", "。", "Đối với món muốn mua, cô không chỉ xem chất lượng mà còn xem giá."),
     ("[对于]|他的做法|大家都很支持", "。", "Đối với cách làm của anh ấy, mọi người đều rất ủng hộ."),
     ("[对于]|你们提的这个建议|我们一定好好研究", "。", "Đối với đề nghị các bạn đưa ra, chúng tôi nhất định sẽ nghiên cứu kỹ.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["暂时", "表示", "减", "态度", "两", "缺"], [
   "这家饭馆不仅菜好吃，服务员服务【态度】也特别好，所以我们经常来。", "茶叶一次不用买太多，买六【两】就够喝一段时间了。", "马上到景区了，大家准备下车，不需要的东西可以【暂时】放在车上。",
   "网上商店正在做活动，除了直接降价外，还有满100【减】30的活动，挺值的。", "我要买的那个手机现在【缺】货，过几天再去看看来没来货。", "高医生【表示】，病人过几天如果没什么问题就可以出院了。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["许多", "者", "不光", "分为", "友好", "顾客"], [
   "A：您的学生学习都很好！ B：是的，他们【不光】学习成绩优秀，还经常帮助别人。", "A：这家店人真多！ B：嗯，他们的商品种类多、价格合适，服务还特别好，所以很多【顾客】都喜欢来这里买东西。",
   "A：您能简单介绍一下武汉长江大桥吗？ B：这座桥全长1670米，【分为】上下两层，是长江上的第一座大桥。", "A：这个动物园虽然比较远，但动物特别多，有【许多】我以前没见过的动物。 B：是吗？有机会我也去看看。",
   "A：你这次去那儿玩感觉怎么样？ B：挺不错的，那里的人都很热情、【友好】，也给了我们很多帮助。", "A：电子邮件发出后，我才发现会议时间写错了。 B：那你快给参会【者】重新发邮件，向他们道歉，并告诉他们正确的时间。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["对于买衣服这件事", "但现在她更喜欢在网上买", "她都会仔细看商品介绍", "既不浪费钱"], [
   "吴红在一家公司上班，工资挺高的。和许多女孩子一样，她喜欢买衣服。【对于买衣服这件事】，她的想法是：不需要的就不买，只买对的，不买贵的。以前，吴红喜欢去商场买衣服，【但现在她更喜欢在网上买】。网上的选择多，每次看到喜欢的，【她都会仔细看商品介绍】，看颜色、大小、样子是不是自己满意的，都看好了才付钱。这样买东西，【既不浪费钱】，又能买到自己喜欢的。每次穿上新衣服，她都挺开心的。"], inline=False),
 opn("用词语造句", "Dùng từ cho sẵn đặt câu.", [
   ("商品", "这家超市的商品又多又便宜。"), ("仔细", "他正在仔细地看那朵花。"), ("友好", "邻居们对我们都很友好。")]),
])
