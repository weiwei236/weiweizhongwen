# -*- coding: utf-8 -*-
# HSK 3 – Bài 7: 那条裙子比短裤更好看
from gtb_gen import V, T, Q, F, G
B = {}

B[7] = dict(zh="那条裙子比短裤更好看", vi="Chiếc váy kia đẹp hơn quần soóc",
intro="Vợ chồng Lưu Minh đi trung tâm thương mại mua xe đạp mới cho Tiểu Tuyết, chọn quần áo, mua dưa hấu, rồi lên mạng chọn TV mới cho căn nhà mới.",
vocab=V("""
辆|liàng|lg|chiếc (dùng cho xe cộ)|楼下停着一辆红色的车。~Dưới nhà có một chiếc xe màu đỏ đang đỗ.
自行车|zìxíngchē|dt|xe đạp|我每天骑自行车去学校。~Ngày nào tôi cũng đạp xe đến trường.
旧|jiù|tt|cũ|这本书太旧了。~Quyển sách này cũ quá rồi.
矮|ǎi|tt|thấp, lùn|弟弟比我矮一点儿。~Em trai thấp hơn tôi một chút.
试|shì|dong|thử|这件衣服我可以试一下吗？~Cái áo này tôi mặc thử được không?
黄色|huángsè|dt|màu vàng|她喜欢黄色的花。~Cô ấy thích hoa màu vàng.
短裤|duǎnkù|dt|quần soóc|夏天我常常穿短裤。~Mùa hè tôi hay mặc quần soóc.
大小|dàxiǎo|dt|kích cỡ|这双鞋大小正好。~Đôi giày này cỡ vừa khít.
合适|héshì|tt|phù hợp|这件衣服你穿很合适。~Cái áo này bạn mặc rất hợp.
裙子|qúnzi|dt|váy, đầm|这条裙子真漂亮。~Chiếc váy này đẹp thật.
更|gèng|pho|càng, hơn|今天比昨天更冷。~Hôm nay còn lạnh hơn hôm qua.
决定|juédìng|dong|quyết định|我决定明年去中国留学。~Tôi quyết định sang năm đi Trung Quốc du học.
西瓜|xīguā|dt|dưa hấu|夏天吃西瓜最舒服了。~Mùa hè ăn dưa hấu là sướng nhất.
新鲜|xīnxiān|tt|tươi, tươi mới|这些水果很新鲜。~Những loại hoa quả này rất tươi.
甜|tián|tt|ngọt|这个苹果真甜！~Quả táo này ngọt thật!
公斤|gōngjīn|lg|kilôgam|我买了两公斤苹果。~Tôi mua hai cân táo.
冰|bīng|dt|đông, đá|我想喝一杯冰咖啡。~Tôi muốn uống một cốc cà phê đá.
极|jí|pho|cực kỳ|今天热极了！~Hôm nay nóng cực kỳ!
斤|jīn|lg|cân (0,5 kilôgam)|香蕉多少钱一斤？~Chuối bao nhiêu tiền một cân?
香蕉|xiāngjiāo|dt|chuối tiêu|我早上吃了一个香蕉。~Buổi sáng tôi ăn một quả chuối.
一共|yígòng|pho|tổng cộng|这些东西一共多少钱？~Những thứ này tổng cộng bao nhiêu tiền?
毛|máo|lg|hào (đơn vị tiền tệ)|一个苹果三块五毛。~Một quả táo ba tệ rưỡi.
结婚|jiéhūn|dong|kết hôn|我姐姐明年结婚。~Chị gái tôi năm sau kết hôn.
不但|búdàn|lien|không những|他不但会唱歌，而且会跳舞。~Anh ấy không những biết hát mà còn biết nhảy.
而且|érqiě|lien|mà còn|这家店的东西便宜，而且很好。~Đồ của cửa hàng này rẻ mà còn tốt.
声|shēng|lg|tiếng (dùng cho âm thanh), âm thanh|你到了叫我一声。~Bạn đến nơi thì gọi tôi một tiếng.
开机|kāijī|dong|mở máy, bật máy|我的手机开不了机了。~Điện thoại của tôi không mở máy được nữa.
"""),
texts=[dict(t="课文1", scene="在家里，王一雪和刘明商量去买东西。", scene_vi="Vương Nhất Tuyết và Lưu Minh đang ở trong nhà bàn bạc về việc đi mua đồ.", narr=False, lines=T("""
王一雪>这辆自行车是小雪八岁的时候买的，看起来有点儿旧了。|Chiếc xe đạp này mua lúc Tiểu Tuyết tám tuổi, trông hơi cũ rồi.
刘明>是啊，她现在长高了，这辆车已经太矮了。|Đúng vậy, bây giờ con bé cao lên rồi, chiếc xe này đã quá thấp.
王一雪>商场里开了一家自行车店，咱们给她买辆新的吧。|Trong trung tâm thương mại mới mở một cửa hàng xe đạp, chúng ta mua cho con một chiếc mới đi.
刘明>好，咱们带小雪一起去，让她试一下。|Được, chúng ta đưa Tiểu Tuyết đi cùng, để con thử.
王一雪>那今天就去吧！我也想再看看衣服。咱们怎么去？|Vậy hôm nay đi luôn! Em cũng muốn xem thêm quần áo. Chúng ta đi bằng gì?
刘明>商场不远，咱们可以走着去。|Trung tâm thương mại không xa, chúng ta có thể đi bộ.
"""), q=Q("""
他们为什么想给小雪买新自行车？|因为她现在长高了，这辆车已经太矮了。|Vì con bé cao lên, chiếc xe đã quá thấp.
他们为什么想带小雪一起去？|让她试一下。|Để con bé thử.
王一雪还想买什么？|她还想看看衣服。|Cô ấy còn muốn xem quần áo.
""")),
 dict(t="课文2", scene="在商场，刘明和王一雪买完自行车，又来挑选衣服。", scene_vi="Ở trung tâm thương mại, Lưu Minh và Vương Nhất Tuyết mua xong xe đạp rồi lại chọn quần áo.", narr=False, lines=T("""
王一雪>你看我穿这条黄色的短裤好看吗？|Anh xem em mặc chiếc quần soóc màu vàng này có đẹp không?
刘明>大小合适，但我觉得那条裙子比短裤更好看。|Cỡ thì vừa, nhưng anh thấy chiếc váy kia đẹp hơn quần soóc.
王一雪>裙子比短裤贵一点儿。|Váy đắt hơn quần soóc một chút.
刘明>贵多少？|Đắt hơn bao nhiêu?
王一雪>裙子480，短裤400。|Váy 480, quần soóc 400.
刘明>裙子不比短裤贵多少，还是买裙子吧，你穿裙子更好看。|Váy cũng chẳng đắt hơn quần soóc là mấy, mua váy đi, em mặc váy đẹp hơn.
王一雪>我多看看再决定。你看，那边有买二送一！|Em xem thêm rồi mới quyết định. Anh xem, bên kia có mua hai tặng một kìa!
"""), q=Q("""
刘明觉得短裤怎么样？|大小合适，但他觉得裙子更好看。|Cỡ vừa, nhưng anh ấy thấy váy đẹp hơn.
王一雪为什么不想买裙子？|因为裙子比短裤贵一点儿。|Vì váy đắt hơn quần soóc một chút.
裙子比短裤贵多少？|贵八十块。|Đắt hơn 80 tệ.
""")),
 dict(t="课文3", scene="在商店，王一雪在买东西。", scene_vi="Vương Nhất Tuyết đang mua đồ ở cửa hàng.", narr=False, lines=T("""
店员>西瓜又大又新鲜，不甜不要钱！|Dưa hấu vừa to vừa tươi, không ngọt không lấy tiền!
王一雪>西瓜看起来不错，怎么卖？|Dưa hấu trông được đấy, bán thế nào?
店员>五块钱一公斤。来，您先尝尝这块冰西瓜，甜极了！|Năm tệ một cân (kg). Nào, chị nếm thử miếng dưa hấu lạnh này trước, ngọt cực kỳ!
王一雪>是挺甜的！帮我选个大点儿的，再来两斤香蕉。|Đúng là khá ngọt! Chọn giúp tôi một quả to to, thêm hai cân chuối nữa.
店员>一共五十八块五毛。|Tổng cộng năm mươi tám tệ rưỡi.
王一雪>我买了这么多，便宜点儿吧。|Tôi mua nhiều thế này, rẻ chút đi.
店员>您给我五十五吧，不能再便宜了。|Chị đưa tôi năm mươi lăm thôi, không rẻ hơn được nữa.
"""), q=Q("""
西瓜多少钱一斤？|两块五一斤（五块钱一公斤）。|2,5 tệ một cân (5 tệ một kg).
王一雪买了什么水果？|一个西瓜和两斤香蕉。|Một quả dưa hấu và hai cân chuối.
店员给王一雪便宜了多少钱？|三块五毛。|3,5 tệ.
""")),
 dict(t="课文4", scene="在家里，刘明在看电视。", scene_vi="Lưu Minh đang xem ti vi ở trong nhà.", narr=True, lines=T("""
这几天我们在新家坐着看电视的时候，又发现了新问题。|Mấy hôm nay ngồi xem TV ở nhà mới, chúng tôi lại phát hiện vấn đề mới.
房子大了，电视看起来就有点儿小。|Nhà rộng ra, TV trông có vẻ hơi nhỏ.
这个电视是我们结婚时买的，是时候换个新电视了。|Chiếc TV này mua lúc chúng tôi cưới, đến lúc thay TV mới rồi.
今天我一直在网上选电视，|Hôm nay tôi cứ lên mạng chọn TV suốt,
没想到，现在的电视不但便宜，而且用着非常方便，有的电视叫它一声就能开机。|không ngờ TV bây giờ không những rẻ mà dùng còn rất tiện, có loại gọi một tiếng là tự bật.
我看了好几个，都很满意，晚上让一雪来决定吧。|Tôi xem mấy cái, đều rất ưng, tối để Nhất Tuyết quyết định vậy.
"""), q=Q("""
刘明家的电视是什么时候买的？|他们结婚时买的。|Mua lúc họ kết hôn.
刘明想在哪儿买新电视？|在网上。|Trên mạng.
刘明为什么觉得新电视用着很方便？|因为有的电视叫它一声就能开机。|Vì có loại gọi một tiếng là tự bật.
"""))],
grammar=[
 G("liandong2", "连动句（2）：V1着 + V2", "Câu liên động (2) – “V1 + 着 + V2”",
   "Trợ từ động thái “着” dùng sau động từ thứ nhất trong câu liên động, biểu thị trạng thái hoặc cách thức khi thực hiện hành động thứ hai. Cấu trúc: động từ 1 + 着 + (tân ngữ 1) + động từ 2 + (tân ngữ 2).",
   [F("S:Chủ ngữ|V1:Động từ 1|kw:着|O:(Tân ngữ 1)|V2:Động từ 2 (+ tân ngữ 2)", [
     ("咱们可以|走|[着]||去", "。", "Chúng ta có thể đi bộ đến đó."),
     ("弟弟|吃|[着]|苹果|写作业", "。", "Em trai vừa ăn táo vừa làm bài tập."),
     ("他们|坐|[着]||看电视", "。", "Họ ngồi xem TV."),
     ("服务员|笑|[着]||给客人点菜", "。", "Nhân viên cười tươi ghi món cho khách.")])]),
 G("bubi", "比较句（10）：A不比B + 形容词", "Câu so sánh (10) – “A 不比 B + tính từ”",
   "“A 不比 B + tính từ” có nghĩa là A và B gần như nhau (A không hơn B). Cấu trúc này thường dùng để nhấn mạnh sự tương đồng giữa hai sự vật hoặc để phản bác ý kiến của người khác. Trong câu so sánh, có thể thêm “还 / 更” trước tính từ để tăng mức độ.",
   [F("A:A|kw:不比|B:B|X:Tính từ (+ 多少)", [
     ("裙子|[不比]|短裤|贵多少", "。", "Váy chẳng đắt hơn quần soóc là bao."),
     ("他的中文|[不比]|你|好", "。", "Tiếng Trung của anh ấy không giỏi hơn bạn."),
     ("他跑得|[不比]|我|快多少", "。", "Anh ấy chạy cũng chẳng nhanh hơn tôi là mấy.")]),
    F("A:A|kw:比|B:B|kw2:更 / 还|X:Tính từ", [
     ("那条裙子|[比]|短裤|[更]|好看", "。", "Chiếc váy kia đẹp hơn quần soóc."),
     ("今天|[比]|昨天|[还]|冷", "。", "Hôm nay còn lạnh hơn hôm qua.")], cap="Thêm 更 / 还 để nhấn mạnh")]),
 G("jile", "程度补语（3）：……极了", "Bổ ngữ trình độ (3) – “……极了”",
   "Bổ ngữ trình độ “极了” đặt sau tính từ hoặc động từ tâm lý, biểu thị tính chất, trạng thái hoặc cảm xúc đạt đến mức rất cao (cực kỳ, vô cùng).",
   [F("S:Chủ ngữ|A:Tính từ / động từ tâm lý|kw:极了", [
     ("这块冰西瓜|甜|[极了]", "。", "Miếng dưa hấu lạnh này ngọt cực kỳ."),
     ("今年夏天|热|[极了]", "。", "Mùa hè năm nay nóng cực kỳ."),
     ("这本书我|喜欢|[极了]", "。", "Cuốn sách này tôi thích vô cùng."),
     ("她做的中国菜|好吃|[极了]", "。", "Món Trung Quốc cô ấy nấu ngon tuyệt.")])]),
 G("budanerqie", "递进复句“不但……，而且……”", "Câu ghép tăng tiến “不但……，而且……”",
   "“不但……，而且……” nối hai vế, biểu thị quan hệ tăng tiến (không những… mà còn…). Nếu hai vế cùng chủ ngữ, “不但” đặt sau chủ ngữ; nếu hai vế khác chủ ngữ, “不但” đặt trước chủ ngữ thứ nhất.",
   [F("S:(Chủ ngữ)|kw:不但|C:Vế 1|kw2:而且|X:Vế 2", [
     ("现在的电视|[不但]|便宜，|[而且]|用着非常方便", "。", "TV bây giờ không những rẻ mà dùng còn rất tiện."),
     ("家月|[不但]|喜欢唱歌，|[而且]|唱得很好听", "。", "Gia Nguyệt không những thích hát mà còn hát rất hay."),
     ("|[不但]|家月会说汉语，|[而且]|天中也会说汉语", "。", "Không những Gia Nguyệt biết nói tiếng Hán mà Thiên Trung cũng biết.")])]),
],
test=dict(
 l2=["特别甜|不太新鲜|昨天买的", "不舒服|颜色好看|大小不合适", "搬家|选空调|办信用卡"],
 l3=["很新鲜|不太甜|不便宜", "十块|二十五块七毛|三十五块七毛", "很小|人很多|水果很多", "她看错人了|去找手机了|去买水果了"],
 r1=(["咱们下午去看看吧。", "没问题，我先写完这些题。", "看起来不错，西瓜怎么卖？", "对，他要准备很多东西，忙极了。", "当然。我们先坐公交车，然后换地铁。", "你应该试试，有时候看起来不合适，穿上才好看。"],
     ["你走的时候叫我一声。", "这些衣服我都不喜欢。", "商场里新开了一家书店。", "尝一尝，看一看，不甜不要钱。", "听说你哥哥下个月就要结婚了。"]),
 r2=(["决定", "新鲜", "更", "合适", "鞋", "不但"],
     ["别买香蕉了，看起来都不太（　　）。", "我觉得那件衬衫比这件（　　）漂亮。", "这两个都很好吃，又甜又新鲜，我还不能（　　）买哪个。", "A：妈妈，这张床大小（　　）吗？\nB：有点儿小。前面那个大一些，我们去看看。", "A：这是最新的手机。我给你开机了，你看看好用不好用。\nB：好极了！（　　）好看，而且大小合适，拿着也方便。"]),
 r3=[("这些是您选的水果吗？两斤苹果、一个西瓜，一共二十一块五毛，您给我二十吧。", "买这些水果要花多少钱？", "二十块|二十一块|二十块五毛"),
     ("用洗衣机洗衣服比用手洗衣服好，不但一点儿也不累，而且洗得更干净，用的水也更少。", "他觉得用洗衣机洗衣服：", "洗得不干净|需要用更多水|一点儿也不累"),
     ("我家的旧冰箱已经用了十几年了，我想换一个大一点儿的。我在网上看了很久，觉得现在卖的冰箱不但更漂亮，而且更好用。我打算去商店看一看再决定买哪个。",
      ("他现在的冰箱：", "太大了|太旧了|特别漂亮"), ("关于现在卖的冰箱，可以知道什么？", "很贵|很好用|不能在网上买"))],
 w1=["香蕉十块钱一公（jīn）。", "我想买这个电视，不但更大，（ér）且更便宜。", "今天一（gòng）要来15个学生，我们多准备点儿饮料。"],
 w2=[("更", "姐姐比妹妹更高。"), ("结婚", "他们今天结婚，朋友们都来了。"), ("合适", "这件衣服大小很合适，颜色也好看。")],
 gl={"11": "Lúc bạn đi thì gọi mình một tiếng. → B: Không vấn đề, mình làm xong mấy câu này trước đã.",
     "12": "Mấy bộ quần áo này mình đều không thích. → F: Bạn nên mặc thử, có khi nhìn thì không hợp, mặc vào mới đẹp.",
     "13": "Trong trung tâm thương mại mới mở một hiệu sách. → A: Chiều nay chúng ta đi xem thử đi.",
     "14": "Nếm thử đi, xem thử đi, không ngọt không lấy tiền. → C: Trông được đấy, dưa hấu bán thế nào?",
     "15": "Nghe nói tháng sau anh bạn cưới vợ. → D: Đúng, anh ấy phải chuẩn bị nhiều thứ, bận cực kỳ.",
     "16": "看起来不太新鲜 – trông không tươi lắm. → B 新鲜.",
     "17": "比这件更漂亮 – đẹp hơn cái này. → C 更.",
     "18": "还不能决定买哪个 – vẫn chưa quyết định được mua cái nào. → A 决定.",
     "19": "大小合适吗 – kích cỡ có vừa không. → D 合适.",
     "20": "不但……而且…… – không những đẹp mà kích cỡ còn vừa. → F 不但.",
     "21": "Tổng 21,5 tệ, nhưng “您给我二十吧” → A 二十块.",
     "22": "“不但一点儿也不累” → C.",
     "23": "“旧冰箱已经用了十几年了” → B 太旧了.",
     "24": "“现在卖的冰箱不但更漂亮，而且更好用” → B 很好用."}),
)
