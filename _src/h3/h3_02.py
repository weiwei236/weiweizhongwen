# -*- coding: utf-8 -*-
# HSK 3 – Bài 2: 你们想吃什么就点什么
from gtb_gen import V, T, Q, F, G
B = {}

B[2] = dict(zh="你们想吃什么就点什么", vi="Các em muốn ăn món gì thì gọi món đó",
intro="Vừa đến Bắc Kinh, cả nhóm cùng đi ăn ở một nhà hàng quen: gọi món, xin thêm đũa thìa, nếm món gà… và phát hiện ở Trung Quốc gọi đồ ăn giao tận nơi tiện đến mức nào.",
vocab=V("""
菜单|càidān|dt|thực đơn|服务员，请给我们看看菜单。~Phục vụ ơi, cho chúng tôi xem thực đơn.
又|yòu|pho|lại, vừa (…vừa…)|这个苹果又大又红。~Quả táo này vừa to vừa đỏ.
饿|è|tt|đói|我饿了，我们去吃饭吧。~Mình đói rồi, chúng ta đi ăn cơm đi.
渴|kě|tt|khát|天太热了，我很渴。~Trời nóng quá, mình khát lắm.
客气|kèqi|dong|khách sáo, khách khí|别客气，多吃点儿。~Đừng khách sáo, ăn nhiều chút nhé.
饮料|yǐnliào|dt|đồ uống|你想喝什么饮料？~Bạn muốn uống đồ uống gì?
好久|hǎojiǔ|tt|lâu, rất lâu|好久不见，你最近怎么样？~Lâu rồi không gặp, dạo này bạn thế nào?
服务|fúwù|dong|phục vụ|这家商店的服务很好。~Dịch vụ của cửa hàng này rất tốt.
员|yuán|hau|(hậu tố chỉ người làm nghề, thành viên)|我姐姐是银行的服务员。~Chị gái tôi là nhân viên phục vụ ở ngân hàng.
双|shuāng|lg|đôi|我买了一双新鞋。~Tôi đã mua một đôi giày mới.
筷子|kuàizi|dt|đũa|你会用筷子吃饭吗？~Bạn có biết dùng đũa ăn cơm không?
勺子|sháozi|dt|thìa|喝汤要用勺子。~Ăn canh phải dùng thìa.
碗|wǎn|dt|bát|我早上吃了一碗面条儿。~Buổi sáng tôi ăn một bát mì.
马上|mǎshàng|pho|lập tức, ngay lập tức|你等一下，我马上来。~Bạn đợi một chút, mình đến ngay.
热情|rèqíng|tt|nhiệt tình|中国朋友对我们很热情。~Bạn bè Trung Quốc rất nhiệt tình với chúng tôi.
尝|cháng|dong|nếm, thử|这是我做的菜，你尝尝。~Đây là món mình nấu, bạn nếm thử xem.
记|jì|dong|nhớ, ghi nhớ|你记住他的电话号码了吗？~Bạn đã nhớ số điện thoại của anh ấy chưa?
用|yòng|dong|dùng, sử dụng|我可以用一下你的手机吗？~Mình dùng điện thoại của bạn một chút được không?
鸡|jī|dt|gà|我最喜欢吃鸡肉。~Tôi thích ăn thịt gà nhất.
张|zhāng|lg|tờ, bức (dùng cho giấy, tranh…)|桌子上有两张电影票。~Trên bàn có hai tấm vé xem phim.
不用|búyòng|pho|không cần|不用谢，这是我应该做的。~Không cần cảm ơn, đây là việc mình nên làm.
选|xuǎn|dong|chọn, lựa chọn|这两件衣服，你选哪件？~Hai cái áo này, bạn chọn cái nào?
外卖|wàimài|dt|đồ ăn giao tận nơi; đặt đồ ăn giao tận nơi|今天太累了，我们点外卖吧。~Hôm nay mệt quá, chúng ta gọi đồ ăn về đi.
方便|fāngbiàn|tt|thuận tiện, tiện lợi|我家旁边就有超市，很方便。~Ngay cạnh nhà tôi có siêu thị, rất tiện.
蛋糕|dàngāo|dt|bánh ngọt, bánh kem, bánh ga tô|妈妈给我买了一个生日蛋糕。~Mẹ mua cho tôi một chiếc bánh sinh nhật.
只|zhǐ|pho|chỉ|我只有一个弟弟。~Tôi chỉ có một em trai.
方便面|fāngbiànmiàn|dt|mì ăn liền|晚上我吃了一碗方便面。~Buổi tối tôi ăn một bát mì ăn liền.
简单|jiǎndān|tt|đơn giản|这个问题很简单。~Câu hỏi này rất đơn giản.
"""),
texts=[dict(t="课文1", scene="在饭馆，王一雪、刘明、白家月和李文在点菜。", scene_vi="Vương Nhất Tuyết, Lưu Minh, Bạch Gia Nguyệt và Lý Văn đang gọi món tại nhà hàng.", narr=False, lines=T("""
王一雪>家月、李文，你们看看菜单，想吃点儿什么？|Gia Nguyệt, Lý Văn, các em xem thực đơn đi, muốn ăn gì nào?
李文>谢谢一雪姐，我都可以，你们点吧。|Cảm ơn chị Nhất Tuyết, em món gì cũng được, mọi người gọi đi ạ.
白家月>飞了这么远，现在还真是又饿又渴。|Bay xa thế này, bây giờ em đúng là vừa đói vừa khát.
王一雪>那多点点儿，别客气。你们喝什么饮料？|Vậy gọi nhiều một chút, đừng khách sáo. Các em uống gì?
白家月>好久没喝中国茶，也好久没吃饺子了。我想喝绿茶、吃饺子，可以吗？|Lâu lắm rồi em không uống trà Trung Quốc, cũng lâu rồi không ăn sủi cảo. Em muốn uống trà xanh, ăn sủi cảo, được không ạ?
王一雪>没问题。你们看看还想吃什么。|Không vấn đề gì. Các em xem còn muốn ăn gì nữa.
"""), q=Q("""
白家月现在觉得怎么样？|她又饿又渴。|Cô ấy vừa đói vừa khát.
白家月想喝什么？|她想喝绿茶。|Cô ấy muốn uống trà xanh.
""")),
 dict(t="课文2", scene="在饭馆，王一雪、刘明、白家月和李文一起吃饭。", scene_vi="Vương Nhất Tuyết, Lưu Minh, Bạch Gia Nguyệt và Lý Văn đang ăn cùng nhau tại nhà hàng.", narr=False, lines=T("""
王一雪>服务员，再给我们拿一双筷子、一个勺子和一个碗。|Phục vụ ơi, lấy thêm cho chúng tôi một đôi đũa, một cái thìa và một cái bát.
服务员>好的，请等一下，我马上去拿。|Vâng, xin chờ một chút, tôi đi lấy ngay.
王一雪>这家饭馆的服务很热情，菜也都做得很好吃。你们尝尝，看喜不喜欢这些菜。|Nhà hàng này phục vụ rất nhiệt tình, món nào cũng nấu rất ngon. Các em nếm thử xem có thích những món này không.
白家月>哪个菜都好吃。您点的这些菜真不错。|Món nào cũng ngon. Những món chị gọi thật không tệ.
王一雪>这里的饭菜又便宜又好吃，我们经常来，服务员都记住我们爱吃的菜了。|Cơm canh ở đây vừa rẻ vừa ngon, chúng tôi hay đến, nhân viên đều nhớ món chúng tôi thích ăn rồi.
服务员>王姐，您经常来吃饭，今天送您一些水果，请慢用。|Chị Vương, chị thường xuyên đến ăn, hôm nay quán tặng chị ít hoa quả, mời chị dùng ạ.
"""), q=Q("""
王一雪觉得这家饭馆怎么样？|服务很热情，菜也做得很好吃，又便宜又好吃。|Phục vụ nhiệt tình, món ngon, vừa rẻ vừa ngon.
白家月觉得这家饭馆的菜怎么样？|哪个菜都好吃。|Món nào cũng ngon.
服务员为什么送了一些水果？|因为王一雪经常来吃饭。|Vì Vương Nhất Tuyết thường xuyên đến ăn.
""")),
 dict(t="课文3", scene="在饭馆，王一雪、刘明、白家月和李文继续边吃边聊。", scene_vi="Vương Nhất Tuyết, Lưu Minh, Bạch Gia Nguyệt và Lý Văn tiếp tục vừa ăn vừa trò chuyện trong nhà hàng.", narr=False, lines=T("""
白家月>这个鸡肉饭太好吃了，我要再来吃一次。|Món cơm gà này ngon quá, em phải đến ăn thêm lần nữa.
李文>你可以拿走这张菜单，看看下次还吃点儿什么。|Cậu có thể cầm tờ thực đơn này về, xem lần sau ăn gì nữa.
王一雪>不用拿菜单，在手机上就能看到，也可以选好了让他们给你送。|Không cần cầm thực đơn, xem trên điện thoại là được, cũng có thể chọn xong rồi để họ giao cho em.
白家月>他们家还能送外卖？|Quán họ còn giao đồ ăn tận nơi nữa à?
王一雪>对，现在很多饭馆都能送外卖，想吃什么就点什么。|Đúng vậy, bây giờ nhiều nhà hàng đều giao tận nơi, muốn ăn gì thì gọi nấy.
白家月>那真是太方便了！|Vậy thì tiện quá!
"""), q=Q("""
白家月为什么要再来吃一次？|因为这个鸡肉饭太好吃了。|Vì món cơm gà quá ngon.
这家饭馆可以怎么点菜？|在手机上就能看到菜单，选好了让他们送。|Xem thực đơn trên điện thoại, chọn xong để họ giao.
听说很多饭馆都能送外卖，白家月觉得怎么样？|她觉得真是太方便了。|Cô ấy thấy thật là quá tiện.
""")),
 dict(t="课文4", scene="在李文家，李文在写日记。", scene_vi="Lý Văn đang viết nhật ký ở trong nhà mình.", narr=True, lines=T("""
这些年在国外，我很少自己做饭。|Mấy năm nay ở nước ngoài, tôi rất ít khi tự nấu cơm.
早饭我吃一个面包，有时候吃一块蛋糕，再喝一杯咖啡。|Bữa sáng tôi ăn một cái bánh mì, có khi ăn một miếng bánh ngọt, rồi uống một cốc cà phê.
午饭和晚饭也都在外面吃。|Bữa trưa và bữa tối cũng đều ăn ở ngoài.
快要考试的时候又忙又累，没时间出去吃饭，家里又什么吃的都没有，|Lúc sắp thi vừa bận vừa mệt, không có thời gian ra ngoài ăn, trong nhà lại chẳng có gì để ăn,
我可能好几天只吃方便面。|có khi tôi chỉ ăn mì ăn liền mấy ngày liền.
现在回到中国了，每天能吃到妈妈做的饭，我真是太高兴了！|Bây giờ về Trung Quốc rồi, ngày nào cũng được ăn cơm mẹ nấu, tôi thật sự rất vui!
有时候妈妈只做几个简单的菜，我也非常爱吃，因为什么都没有妈妈做的饭好吃。|Có khi mẹ chỉ nấu vài món đơn giản, tôi cũng rất thích ăn, vì chẳng gì ngon bằng cơm mẹ nấu.
"""), q=Q("""
李文在国外经常做饭吗？|不，他很少自己做饭。|Không, cậu ấy rất ít tự nấu cơm.
李文为什么好几天只吃方便面？|因为快要考试的时候又忙又累，家里什么吃的都没有。|Vì sắp thi vừa bận vừa mệt, trong nhà không có gì ăn.
回到中国后什么事让他非常高兴？|每天能吃到妈妈做的饭。|Ngày nào cũng được ăn cơm mẹ nấu.
"""))],
grammar=[
 G("youyou", "并列复句“又……又……”", "Câu ghép đẳng lập “又……又……”",
   "“又……又……” kết hợp với tính từ, biểu thị người hoặc sự vật đồng thời mang hai đặc điểm (vừa… vừa…). Cấu trúc cơ bản: 又 + tính từ 1 + 又 + tính từ 2. Hai tính từ thường cùng sắc thái (cùng tốt hoặc cùng xấu).",
   [F("S:Chủ ngữ|kw:又|A:Tính từ 1|kw:又|B:Tính từ 2", [
     ("我现在还真是|[又]|饿|[又]|渴", "。", "Bây giờ tôi đúng là vừa đói vừa khát."),
     ("那个女孩儿|[又]|高|[又]|漂亮", "。", "Cô gái kia vừa cao vừa xinh."),
     ("这个饭馆的菜|[又]|便宜|[又]|好吃", "。", "Món ăn của quán này vừa rẻ vừa ngon."),
     ("快要考试的时候|[又]|忙|[又]|累", "。", "Lúc sắp thi vừa bận vừa mệt.")])]),
 G("yiwen2", "疑问代词的非疑问用法（2）", "Cách dùng linh hoạt của đại từ nghi vấn (2) – chỉ bất kỳ",
   "Đại từ nghi vấn “哪、哪儿、什么、谁、怎么” còn biểu thị ý nghĩa chỉ chung (bất kỳ): “谁” = bất kỳ ai, “什么” = bất cứ thứ gì, “哪儿” = bất cứ đâu… Thường dùng kết hợp với phó từ “都” (hoặc “也”) phía sau.",
   [F("S:Chủ ngữ / phần trước|kw:Đại từ nghi vấn|X:(Danh từ / động từ)|kw:都|V:Vị ngữ", [
     ("|[哪个]|菜|[都]|好吃", "。", "Món nào cũng ngon."),
     ("这次旅游，我去|[哪儿]||[都]|可以", "。", "Chuyến du lịch này, tôi đi đâu cũng được."),
     ("我下午有时间，你想|[什么]|时候来|[都]|没问题", "。", "Chiều nay tôi rảnh, bạn muốn đến lúc nào cũng không vấn đề gì."),
     ("|[谁]|吃了|[都]|说好吃", "。", "Ai ăn rồi cũng khen ngon.")])]),
 G("yiwen3", "疑问代词的非疑问用法（3）", "Cách dùng linh hoạt của đại từ nghi vấn (3) – hai đại từ hô ứng",
   "Hai đại từ nghi vấn giống nhau đứng ở hai vế, hô ứng với nhau, cùng chỉ một người, một việc, một cách thức, một thời điểm hay một nơi chốn (… gì thì … nấy). Nếu hai vế cùng chủ ngữ, chủ ngữ vế sau có thể lược bỏ; nếu khác chủ ngữ, chủ ngữ thứ hai đặt trước “就”.",
   [F("A:Vế 1 (có đại từ nghi vấn)|kw:就|B:Vế 2 (lặp lại đại từ đó)", [
     ("你们想吃什么|[就]|点什么", "。", "Các em muốn ăn gì thì gọi nấy."),
     ("你觉得哪个好看|[就]|买哪个", "。", "Bạn thấy cái nào đẹp thì mua cái đó."),
     ("你想去哪儿，我们|[就]|去哪儿", "。", "Bạn muốn đi đâu thì chúng ta đi đó."),
     ("谁先到，谁|[就]|买票", "。", "Ai đến trước thì người đó mua vé.")])]),
],
test=dict(
 l2=["女的不会做饭|男的喜欢吃鸡肉|男的请女的去他家", "离家近|人不多|菜好吃还便宜", "她不太饿|她不会点外卖|她不喜欢吃外卖"],
 l3=["上午|中午|晚上", "很忙|很热情|很着急", "菜很好吃|朋友来了|什么都想尝尝", "两双筷子|两个包子|两碗面条儿"],
 r1=(["别着急，现在是午饭时间，所以有点儿慢。", "没有，但是每个菜都有一张照片，您可以看照片点菜。", "没问题，我什么都会做。", "我妈妈做的鸡肉面，谁吃了都说好吃。", "当然。我们先坐公交车，然后换地铁。", "我家只有筷子，用筷子吃吧。"],
     ["我们用什么吃蛋糕？", "你吃过的最好吃的菜是什么？", "外卖怎么还没送到？", "你可以教我做中国菜吗？", "服务员，请问有英文（Yīngwén, English）菜单吗？"]),
 r2=(["好久", "尝", "记", "马上", "鞋", "简单"],
     ["蛋糕已经卖完了，您可以（　　）一下我们的面包。", "今天的服务员很热情，但是我没（　　）住她的名字。", "用筷子吃面条儿很（　　），我来教你吧。", "A：我们（　　）没一起吃饭了，明天你有时间吗？\nB：好啊，明天中午怎么样？", "A：你饿不饿？我（　　）去给你做晚饭。\nB：不用做，我吃完晚饭了。"]),
 r3=[("学校门口新开了一家饭馆，同学们说那里的菜又好吃又便宜，我明天中午想去尝一尝。", "他想什么时候去那家饭馆？", "马上|今天|明天中午"),
     ("我爱吃中国菜，但是我不会用筷子。李老师让我下课后去他家吃饭，他要教我用筷子，我太高兴了。", "他高兴是因为：", "学做中国菜|去饭馆吃饭|老师教他用筷子"),
     ("今天天气非常热，我和小王又渴又累，看到一家冰激凌店就走进去了。服务员介绍了几个卖得很好的冰激凌，我买了水果冰激凌，但是小王不知道选什么。服务员对他说：“您尝一尝绿茶冰激凌，谁吃了都说好吃。”",
      ("小王：", "想吃水果|不知道选什么|想吃绿茶冰激凌"), ("服务员为什么让小王尝尝绿茶冰激凌？", "只有这个|很多人都说好吃|小王不爱吃水果"))],
 w1=["我太（kě）了，请给我一杯水。", "你想喝什么（yǐn）料？", "这是我们的菜（dān），请您看看。"],
 w2=[("马上", "外卖马上就送到了。"), ("热情", "这家饭馆的服务员都很热情。"), ("选", "她正在手机上选菜。")],
 gl={"11": "Chúng ta ăn bánh ngọt bằng gì? → F: Nhà mình chỉ có đũa, ăn bằng đũa đi.",
     "12": "Món ngon nhất bạn từng ăn là gì? → D: Mì gà mẹ mình nấu, ai ăn cũng khen ngon.",
     "13": "Sao đồ ăn gọi về vẫn chưa tới? → A: Đừng sốt ruột, bây giờ là giờ ăn trưa nên hơi chậm.",
     "14": "Bạn dạy mình nấu món Trung Quốc được không? → C: Không vấn đề, món gì mình cũng biết nấu.",
     "15": "Phục vụ ơi, có thực đơn tiếng Anh không? → B: Không có, nhưng món nào cũng có ảnh, anh có thể xem ảnh để gọi món.",
     "16": "尝一下 – nếm thử: Bánh kem bán hết rồi, chị có thể nếm thử bánh mì của chúng tôi. → B 尝.",
     "17": "记住 – nhớ được: Nhân viên hôm nay rất nhiệt tình nhưng tôi không nhớ tên cô ấy. → C 记.",
     "18": "很简单 – rất đơn giản: Ăn mì bằng đũa rất đơn giản, để mình dạy bạn. → F 简单.",
     "19": "好久没… – lâu rồi không…: Lâu rồi chúng ta không ăn cơm cùng nhau. → A 好久.",
     "20": "马上 – ngay lập tức: Mình đi nấu cơm tối cho bạn ngay. → D 马上.",
     "21": "“我明天中午想去尝一尝” → C 明天中午.",
     "22": "Thầy Lý “要教我用筷子，我太高兴了” → C.",
     "23": "“小王不知道选什么” → B.",
     "24": "“谁吃了都说好吃” – ai ăn cũng khen ngon → B: nhiều người đều nói ngon."}),
)
