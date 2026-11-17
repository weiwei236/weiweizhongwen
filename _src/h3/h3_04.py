# -*- coding: utf-8 -*-
# HSK 3 – Bài 4: 这家宾馆跟别的都不一样
from gtb_gen import V, T, Q, F, G
B = {}

B[4] = dict(zh="这家宾馆跟别的都不一样", vi="Khách sạn này không giống những khách sạn khác",
intro="Dương Đồng Lạc và Vương Nhất Phi lên kế hoạch cho kỳ nghỉ: không đi biển mà lên thảo nguyên cưỡi ngựa, chọn một khách sạn đặc biệt, gặp anh tài xế nhiệt tình dù máy bay bị trễ.",
vocab=V("""
假期|jiàqī|dt|kỳ nghỉ|这个假期你打算去哪儿？~Kỳ nghỉ này bạn định đi đâu?
海|hǎi|dt|biển|我从来没见过大海。~Tôi chưa từng nhìn thấy biển.
草原|cǎoyuán|dt|thảo nguyên|夏天的草原特别漂亮。~Thảo nguyên mùa hè đặc biệt đẹp.
主意|zhǔyi|dt|ý tưởng, chủ ý|这是个好主意！~Đây là một ý hay!
骑|qí|dong|cưỡi, đi (xe đạp, xe máy)|我每天骑自行车上班。~Ngày nào tôi cũng đạp xe đi làm.
马|mǎ|dt|ngựa|你会骑马吗？~Bạn biết cưỡi ngựa không?
羊|yáng|dt|cừu, dê|草原上有很多牛和羊。~Trên thảo nguyên có rất nhiều bò và cừu.
月亮|yuèliang|dt|mặt trăng|今天晚上的月亮又大又圆。~Mặt trăng tối nay vừa to vừa tròn.
一定|yídìng|pho|nhất định, chắc chắn|明天我一定早点儿来。~Ngày mai tôi nhất định đến sớm một chút.
刻|kè|lg|khắc (15 phút)|现在是八点一刻。~Bây giờ là tám giờ mười lăm.
起飞|qǐfēi|dong|cất cánh|飞机几点起飞？~Máy bay mấy giờ cất cánh?
宾馆|bīnguǎn|dt|khách sạn|我们住的宾馆离车站很近。~Khách sạn chúng tôi ở rất gần nhà ga.
特别|tèbié|tt|đặc biệt; rất, vô cùng|今天的晚饭特别好吃。~Bữa tối hôm nay ngon cực kỳ.
别的|biéde|dai|khác, cái khác|你还想买别的东西吗？~Bạn còn muốn mua thứ gì khác không?
一样|yíyàng|tt|giống nhau|我的手机跟你的一样。~Điện thoại của tôi giống của bạn.
牛|niú|dt|bò|那头牛正在吃草。~Con bò kia đang ăn cỏ.
相机|xiàngjī|dt|máy ảnh|这是我新买的相机。~Đây là máy ảnh tôi mới mua.
欢迎|huānyíng|dong|chào đón, hoan nghênh|欢迎你来我家玩儿！~Chào mừng bạn đến nhà mình chơi!
司机|sījī|dt|tài xế|出租车司机很热情。~Bác tài taxi rất nhiệt tình.
晚点|wǎndiǎn|dong|muộn, muộn giờ, trễ giờ|火车晚点了半个小时。~Tàu hỏa trễ nửa tiếng.
久|jiǔ|tt|lâu|对不起，让你久等了。~Xin lỗi, để bạn đợi lâu rồi.
除了|chúle|gioi|ngoài… (ra), trừ… (ra)|除了他，我们都去了。~Trừ anh ấy ra, chúng tôi đều đi cả.
以外|yǐwài|dt|(ngoài)… ra|除了中文以外，他还会说英文。~Ngoài tiếng Trung ra, anh ấy còn biết nói tiếng Anh.
先|xiān|pho|trước, trước tiên|你先吃饭，我一会儿就来。~Bạn ăn cơm trước, mình đến ngay.
一直|yìzhí|pho|luôn luôn, suốt|今天一直在下雨。~Hôm nay mưa suốt.
干净|gānjìng|tt|sạch, sạch sẽ|房间打扫得很干净。~Phòng được dọn rất sạch sẽ.
满意|mǎnyì|dong|hài lòng|你对这个房间满意吗？~Bạn có hài lòng với căn phòng này không?
"""),
texts=[dict(t="课文1", scene="在王一飞家客厅，杨同乐和王一飞在聊天儿。", scene_vi="Dương Đồng Lạc và Vương Nhất Phi đang trò chuyện trong phòng khách nhà Vương Nhất Phi.", narr=False, lines=T("""
杨同乐>这个假期咱们去哪儿玩玩吧。|Kỳ nghỉ này chúng ta đi đâu đó chơi đi.
王一飞>好啊，你想去哪儿，咱们就去哪儿。|Được thôi, anh muốn đi đâu thì chúng ta đi đó.
杨同乐>你喜欢海，找个海边住几天，怎么样？|Em thích biển, tìm chỗ nào ven biển ở vài ngày, thế nào?
王一飞>现在去海边有点儿冷。|Bây giờ ra biển hơi lạnh.
杨同乐>那去草原吧？草原一点儿也不冷。|Vậy đi thảo nguyên nhé? Thảo nguyên chẳng lạnh chút nào.
王一飞>这个主意好！我好久没骑马了。|Ý này hay! Lâu lắm rồi em không cưỡi ngựa.
杨同乐>对，在草原上骑马、吃羊肉、看月亮，一定很有意思。|Đúng, trên thảo nguyên cưỡi ngựa, ăn thịt cừu, ngắm trăng, chắc chắn rất thú vị.
"""), q=Q("""
王一飞为什么不想去海边？|因为现在去海边有点儿冷。|Vì bây giờ ra biển hơi lạnh.
王一飞为什么觉得去草原好？|因为她好久没骑马了。|Vì lâu rồi cô ấy không cưỡi ngựa.
他们在草原上可以做什么？|可以骑马、吃羊肉、看月亮。|Có thể cưỡi ngựa, ăn thịt cừu, ngắm trăng.
""")),
 dict(t="课文2", scene="在王一飞家客厅，杨同乐和王一飞在聊天儿。", scene_vi="Dương Đồng Lạc và Vương Nhất Phi đang trò chuyện trong phòng khách nhà Vương Nhất Phi.", narr=False, lines=T("""
杨同乐>出去玩的机票买好了吗？|Vé máy bay đi chơi mua xong chưa?
王一飞>买好了。星期六上午十点一刻起飞。|Mua rồi. Thứ Bảy, mười giờ mười lăm sáng cất cánh.
杨同乐>宾馆也选好了吗？|Khách sạn cũng chọn xong rồi à?
王一飞>是的，这家宾馆很特别，跟别的都不一样，一出门就能看见牛和羊！|Rồi, khách sạn này rất đặc biệt, không giống những nơi khác, vừa ra khỏi cửa là thấy bò và cừu!
杨同乐>太好了！你看看要带什么东西？|Tuyệt quá! Em xem cần mang theo những gì?
王一飞>我们不用带太多东西，别忘了拿上新买的相机。|Chúng ta không cần mang nhiều đồ, đừng quên cầm theo máy ảnh mới mua.
杨同乐>一定不会忘带的。我现在就去准备行李。|Chắc chắn không quên đâu. Anh đi chuẩn bị hành lý ngay đây.
"""), q=Q("""
他们什么时候坐飞机出去玩？|星期六上午十点一刻。|Thứ Bảy, 10 giờ 15 sáng.
王一飞选的宾馆怎么样？|很特别，跟别的都不一样，一出门就能看见牛和羊。|Rất đặc biệt, ra cửa là thấy bò và cừu.
杨同乐说一定不会忘带什么？|新买的相机。|Máy ảnh mới mua.
""")),
 dict(t="课文3", scene="在机场，杨同乐和王一飞走出来，跟他们预约的司机兼导游见面。", scene_vi="Dương Đồng Lạc và Vương Nhất Phi đi ra phía ngoài sân bay và gặp lái xe kiêm hướng dẫn viên đã đặt trước.", narr=False, lines=T("""
小李>欢迎你们！我是你们的司机，我姓李，叫我小李就可以。|Chào mừng hai bạn! Tôi là tài xế của hai bạn, tôi họ Lý, gọi tôi là Tiểu Lý là được.
杨同乐>您好！不好意思，飞机晚点了，让您久等了。|Chào anh! Ngại quá, máy bay bị trễ, để anh đợi lâu.
小李>没关系。除了这个行李箱以外，还有别的东西吗？|Không sao. Ngoài chiếc va li này ra, còn đồ gì khác không?
杨同乐>还有一个包，我自己拿就可以。|Còn một cái túi, tôi tự cầm là được.
小李>车在一层，请跟我来。|Xe ở tầng một, mời đi theo tôi.
杨同乐>我们住的宾馆离机场远吗？|Khách sạn chúng tôi ở có xa sân bay không?
小李>不远，三十分钟就能到。两位到了可以先休息休息，晚饭的时候我叫你们。|Không xa, ba mươi phút là tới. Hai bạn đến nơi có thể nghỉ ngơi trước, đến bữa tối tôi gọi.
"""), q=Q("""
他们为什么到晚了？|因为飞机晚点了。|Vì máy bay bị trễ.
他们有几个行李箱？|一个行李箱，还有一个包。|Một va li, còn một cái túi.
宾馆离机场远吗？|不远，三十分钟就能到。|Không xa, 30 phút là tới.
""")),
 dict(t="课文4", scene="在宾馆房间，王一飞在写日记。", scene_vi="Vương Nhất Phi đang viết nhật ký trong phòng khách sạn.", narr=True, lines=T("""
今天是我们旅游的第一天。|Hôm nay là ngày đầu tiên chuyến du lịch của chúng tôi.
我们很早就起床去机场了，没想到飞机晚点了。|Chúng tôi dậy rất sớm ra sân bay, không ngờ máy bay bị trễ.
我们到的时候，天已经黑了，但是司机小李一直在机场等我们，一点儿也没着急。|Lúc chúng tôi đến, trời đã tối, nhưng tài xế Tiểu Lý vẫn đợi chúng tôi ở sân bay suốt, chẳng sốt ruột chút nào.
他特别热情，路上给我们介绍了很多东西，还准备了水果。|Anh ấy cực kỳ nhiệt tình, trên đường giới thiệu cho chúng tôi rất nhiều thứ, còn chuẩn bị cả hoa quả.
宾馆的房间跟我想的一样漂亮，又大又干净，我非常满意。|Phòng khách sạn đẹp đúng như tôi nghĩ, vừa rộng vừa sạch, tôi rất hài lòng.
"""), q=Q("""
他们是怎么去宾馆的？|司机小李开车送他们去的。|Tài xế Tiểu Lý lái xe đưa họ đi.
王一飞为什么觉得小李很热情？|他一直在机场等他们，路上给他们介绍了很多东西，还准备了水果。|Anh ấy đợi suốt ở sân bay, giới thiệu nhiều thứ, còn chuẩn bị hoa quả.
宾馆的房间怎么样？|跟她想的一样漂亮，又大又干净。|Đẹp như cô ấy nghĩ, vừa rộng vừa sạch.
"""))],
grammar=[
 G("yiyebu", "固定格式“一……也/都+不/没……”", "Cấu trúc cố định “一……也/都 + 不/没……”",
   "Cấu trúc “一 + lượng từ + danh từ + 也/都 + 不/没 + động từ” biểu thị phủ định hoàn toàn (một … cũng không). “一 + lượng từ” đôi khi có thể thay bằng “一点儿”. Khi vị ngữ là tính từ, thường dùng “一点儿也/都 + 不/没 + tính từ”.",
   [F("S:Chủ ngữ|kw:一 + lượng từ / 一点儿|O:(Danh từ)|kw2:也 / 都 + 不 / 没|V:Động từ / tính từ", [
     ("她|[一件]|衣服|[都不]|想买", "。", "Cô ấy một cái áo cũng không muốn mua."),
     ("我|[一个]|中国电影|[也没]|看过", "。", "Tôi chưa xem bộ phim Trung Quốc nào cả."),
     ("我|[一点儿]|东西|[也不]|想吃", "。", "Tôi chẳng muốn ăn chút gì."),
     ("草原||[一点儿]|[也不]|冷", "。", "Thảo nguyên chẳng lạnh chút nào.")])]),
 G("genyiyang", "比较句（9）：A跟B一样", "Câu so sánh (9) – “A 跟 B 一样”",
   "Câu so sánh “A 跟 B 一样” diễn đạt A và B giống nhau sau khi so sánh. Sau “一样” có thể dùng tính từ để chỉ phương diện so sánh: A 跟 B 一样 + tính từ. Hình thức phủ định thêm “不” trước “一样”.",
   [F("A:A|kw:跟|B:B|kw2:(不)一样|X:(Tính từ)", [
     ("这家宾馆|[跟]|别的都|[不一样]|", "。", "Khách sạn này không giống những khách sạn khác."),
     ("他买的新手机|[跟]|我的|[一样]|", "。", "Điện thoại mới anh ấy mua giống của tôi."),
     ("这个房间|[跟]|那个房间|[一样]|大", "。", "Phòng này rộng bằng phòng kia."),
     ("宾馆的房间|[跟]|我想的|[一样]|漂亮", "。", "Phòng khách sạn đẹp đúng như tôi nghĩ.")])]),
 G("chule", "固定格式“除了……（以外），……都/还/也……”", "Cấu trúc cố định “除了……（以外），……都/还/也……”",
   "“除了……（以外），……都……” diễn đạt: loại trừ một phần, những phần còn lại trong phạm vi đều giống nhau (trừ… ra, … đều…). “除了……（以外），……还/也……” biểu thị loại trừ một phần và bổ sung thêm phần khác (ngoài… ra, … còn / cũng…). “以外” có thể lược bỏ.",
   [F("kw:除了|X:Phần loại trừ|kw2:(以外)，|S:(Chủ ngữ)|V:都 / 还 / 也 + vị ngữ", [
     ("[除了]|我|[以外]|大家|都在玩手机", "。", "Ngoài tôi ra, mọi người đều đang chơi điện thoại."),
     ("[除了]|这个汉字||别的汉字我|都会写", "。", "Trừ chữ Hán này ra, những chữ khác tôi đều biết viết."),
     ("[除了]|这个行李箱|[以外]||还有别的东西吗", "？", "Ngoài chiếc va li này ra, còn đồ gì khác không?"),
     ("[除了]|唱歌|[以外]|他|也喜欢跳舞", "。", "Ngoài hát ra, anh ấy cũng thích nhảy.")])]),
],
test=dict(
 l2=["第一次|第二次|第三次", "三点|四点|五点一刻", "床很舒服|房间不大|不太干净"],
 l3=["吃羊肉|去海边|看月亮", "车坏了|走错路了|飞机晚点了", "看见草原了|看见大海了|拍了很多照片", "相机坏了|照片不好看|相机不见了"],
 r1=(["我还在选宾馆呢，你先休息吧。", "您好，不好意思，让您久等了。", "别着急，过几个月，你就什么都会了。", "我也特别喜欢这里，下次假期我还要来。", "当然。我们先坐公交车，然后换地铁。", "我没带出来，一直在宾馆的房间里。"],
     ["你的相机在哪儿？", "你为什么还不睡觉？", "欢迎您来北京，我是您的司机小王。", "这里真是太好玩儿了。", "除了“谢谢”以外，别的我一点儿都不会说。"]),
 r2=(["别的", "一样", "一直", "一定", "鞋", "特别"],
     ["小丽想去草原看月亮、吃羊肉，但是（　　）没有时间去。", "我和姐姐都喜欢大海，但是妹妹跟我们不（　　），她喜欢草原。", "我今天不舒服，不想吃这个，还有（　　）吗？", "A：你要一个人开车去旅游吗？\nB：对，我一个人去，这次（　　）没问题。", "A：昨天住的那家宾馆很（　　），服务也很好，你觉得呢？\nB：我也觉得不错，房间又大又舒服。"]),
 r3=[("小王要去国外旅游，但是飞机晚点了，他在机场等了六个小时，飞机才起飞。", "关于小王，可以知道什么？", "要回中国|坐了六小时飞机|在机场等了六小时"),
     ("这个假期我们去中国旅游了，除了北京以外，还去了上海和西安。", "他们假期：", "去了上海|只去了北京|哪儿都没去"),
     ("我们一家人一起旅游的时候，最大的问题就是选宾馆。我觉得住的宾馆一定要去哪儿都方便。我妻子希望房间和床都大一些，休息的时候舒服点儿。儿子和女儿说：“最重要的是宾馆的早饭要好吃。”怎么才能选到大家都满意的宾馆呢？",
      ("谁希望选一个房间大的宾馆？", "妻子|女儿|儿子"), ("儿子和女儿觉得宾馆最重要的是什么？", "舒服的床|大的房间|好吃的早饭"))],
 w1=["今天的天气太热了，咱们下午去（hǎi）边玩吧。", "这个假期我一（dìng）要去草原骑马。", "昨天住的那家宾馆很特（bié），服务也很好。"],
 w2=[("特别", "爷爷奶奶带着孙子在草地上玩儿，特别开心。"), ("一直", "她太累了，在飞机上一直在睡觉。"), ("先", "我们先看看地图，再决定去哪儿。")],
 gl={"11": "Máy ảnh của bạn đâu? → F: Mình không mang ra, nó vẫn ở trong phòng khách sạn.",
     "12": "Sao bạn vẫn chưa ngủ? → A: Mình vẫn đang chọn khách sạn, bạn nghỉ trước đi.",
     "13": "Chào mừng anh đến Bắc Kinh, tôi là tài xế Tiểu Vương. → B: Chào anh, ngại quá, để anh đợi lâu.",
     "14": "Ở đây vui thật đấy. → D: Mình cũng cực kỳ thích nơi này, kỳ nghỉ sau mình còn đến nữa.",
     "15": "Ngoài “cảm ơn” ra, mấy câu khác mình chẳng biết nói câu nào. → C: Đừng sốt ruột, vài tháng nữa là bạn biết hết thôi.",
     "16": "一直没有时间 – mãi vẫn không có thời gian. → C 一直.",
     "17": "跟我们不一样 – không giống chúng tôi. → B 一样.",
     "18": "还有别的吗 – còn món khác không? → A 别的.",
     "19": "这次一定没问题 – lần này chắc chắn không vấn đề gì. → D 一定.",
     "20": "宾馆很特别 – khách sạn rất đặc biệt. → F 特别.",
     "21": "“他在机场等了六个小时” → C.",
     "22": "“除了北京以外，还去了上海和西安” → A 去了上海.",
     "23": "“我妻子希望房间和床都大一些” → A 妻子.",
     "24": "“最重要的是宾馆的早饭要好吃” → C."}),
)
