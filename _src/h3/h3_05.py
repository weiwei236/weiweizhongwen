# -*- coding: utf-8 -*-
# HSK 3 – Bài 5: 这样的照片才好看
from gtb_gen import V, T, Q, F, G
B = {}

B[5] = dict(zh="这样的照片才好看", vi="Những bức ảnh như thế này mới đẹp",
intro="Trời cuối cùng cũng nắng, cả nhóm rủ nhau đi leo núi, chụp ảnh. Ai chụp ảnh đẹp hơn: Bạch Gia Nguyệt hay Vương Nhất Phi?",
vocab=V("""
总是|zǒngshì|pho|luôn luôn|他总是第一个到教室。~Cậu ấy luôn là người đến lớp đầu tiên.
终于|zhōngyú|pho|cuối cùng|考试终于结束了。~Kỳ thi cuối cùng cũng kết thúc rồi.
爬|pá|dong|leo, leo trèo|周末我们去爬山吧。~Cuối tuần chúng ta đi leo núi đi.
山|shān|dt|núi, đồi|这座山不太高。~Ngọn núi này không cao lắm.
锻炼|duànliàn|dong|tập luyện, tập thể dục|爷爷每天早上锻炼身体。~Ông nội sáng nào cũng tập thể dục.
照|zhào|dong|chụp (ảnh)|你帮我们照一张相，好吗？~Bạn chụp giúp chúng tôi một tấm ảnh được không?
鞋|xié|dt|giày|这双鞋穿着很舒服。~Đôi giày này đi rất thoải mái.
大衣|dàyī|dt|áo khoác|天冷了，穿上大衣吧。~Trời lạnh rồi, mặc áo khoác vào đi.
拍照|pāizhào|dong|chụp ảnh|这里不能拍照。~Ở đây không được chụp ảnh.
感兴趣|gǎn xìngqù|cum|hứng thú, có hứng thú (với)|我对中国历史很感兴趣。~Tôi rất hứng thú với lịch sử Trung Quốc.
照相|zhàoxiàng|dong|chụp ảnh|我们在长城上照相了。~Chúng tôi đã chụp ảnh trên Vạn Lý Trường Thành.
难看|nánkàn|tt|xấu, khó coi|这件衣服的颜色有点儿难看。~Màu của cái áo này hơi xấu.
比较|bǐjiào|dong|so sánh; tương đối|这两个手机，你比较一下。~Hai chiếc điện thoại này, bạn so sánh thử xem.
水平|shuǐpíng|dt|trình độ, mức|他的中文水平很高。~Trình độ tiếng Trung của anh ấy rất cao.
太阳|tàiyáng|dt|mặt trời|太阳出来了。~Mặt trời mọc rồi.
树|shù|dt|cây|学校门口有一棵大树。~Ở cổng trường có một cái cây to.
干|gàn|dong|làm|你周末想干什么？~Cuối tuần bạn muốn làm gì?
电|diàn|dt|điện|我的手机快没电了。~Điện thoại của tôi sắp hết pin rồi.
收到|shōudào|dong|nhận được|你收到我的邮件了吗？~Bạn đã nhận được email của mình chưa?
封|fēng|lg|bức, lá (thư)|我给妈妈写了一封信。~Tôi đã viết cho mẹ một lá thư.
邮件|yóujiàn|dt|email, thư điện tử|我每天早上都看邮件。~Sáng nào tôi cũng xem email.
难过|nánguò|tt|buồn, buồn rầu|听到这个消息，他很难过。~Nghe tin này, anh ấy rất buồn.
哈哈|hāhā|than|ha ha (tiếng cười)|哈哈，你说得太对了！~Ha ha, bạn nói đúng quá!
音乐|yīnyuè|dt|âm nhạc|我喜欢一边听音乐一边做作业。~Tôi thích vừa nghe nhạc vừa làm bài tập.
兴趣|xìngqù|dt|hứng thú|你有什么兴趣？~Bạn có sở thích gì?
会|huì|dt|buổi gặp mặt, bữa tiệc, cuộc họp|明天下午有个会。~Chiều mai có một cuộc họp.
结束|jiéshù|dong|kết thúc|电影几点结束？~Phim mấy giờ kết thúc?
"""),
texts=[dict(t="课文1", scene="在街上，白家月和李文边散步边聊天儿。", scene_vi="Bạch Gia Nguyệt và Lý Văn vừa đi dạo vừa trò chuyện trên đường phố.", narr=False, lines=T("""
白家月>这个星期总是阴天，今天终于晴了。|Tuần này trời cứ âm u mãi, hôm nay cuối cùng cũng nắng rồi.
李文>现在天气好得很！我们去爬山怎么样？|Bây giờ trời đẹp lắm! Chúng ta đi leo núi thế nào?
白家月>好啊！又能锻炼身体，又能照好看的照片。|Hay đấy! Vừa rèn luyện sức khỏe, vừa chụp được ảnh đẹp.
李文>那我带点儿水和吃的，咱们现在就去？|Vậy mình mang ít nước và đồ ăn, chúng ta đi ngay bây giờ nhé?
白家月>我回去穿上运动鞋，拿上大衣。要不要叫一雪姐一起去？|Mình về đi giày thể thao, lấy áo khoác. Có rủ chị Nhất Tuyết đi cùng không?
李文>好主意。给她打个电话吧。|Ý hay đấy. Gọi điện cho chị ấy đi.
"""), q=Q("""
白家月觉得爬山怎么样？|又能锻炼身体，又能照好看的照片。|Vừa rèn luyện sức khỏe, vừa chụp được ảnh đẹp.
李文要带什么东西？|他要带点儿水和吃的。|Cậu ấy mang ít nước và đồ ăn.
白家月要先回去做什么？|回去穿上运动鞋，拿上大衣。|Về đi giày thể thao, lấy áo khoác.
""")),
 dict(t="课文2", scene="在出租车上，王一雪和白家月在聊天儿。", scene_vi="Vương Nhất Tuyết và Bạch Gia Nguyệt đang trò chuyện trên xe taxi.", narr=False, lines=T("""
白家月>这些照片是谁给您照的？张张都非常好看。|Những bức ảnh này ai chụp cho chị vậy? Tấm nào cũng rất đẹp.
王一雪>一飞。她对拍照一直很感兴趣，经常给我照相。|Nhất Phi đấy. Con bé luôn rất thích chụp ảnh, hay chụp cho chị.
白家月>我喜欢您大笑的这张，看起来很漂亮。|Em thích tấm chị cười tươi này, trông rất đẹp.
王一雪>我觉得这张有点儿难看，那时候我不知道她在给我照相。|Chị thấy tấm này hơi xấu, lúc đó chị không biết con bé đang chụp mình.
白家月>这样的照片才好看。我也喜欢拍照，爬山的时候我给您照几张照片吧。|Ảnh như thế này mới đẹp. Em cũng thích chụp ảnh, lúc leo núi em chụp cho chị vài tấm nhé.
王一雪>好，我可以比较一下你们两个谁的水平高。|Được, chị có thể so xem trình độ hai đứa ai cao hơn.
"""), q=Q("""
白家月喜欢哪张照片？为什么？|她喜欢王一雪大笑的这张，因为看起来很漂亮。|Cô ấy thích tấm Nhất Tuyết cười tươi, vì trông rất đẹp.
王一雪为什么不喜欢这张照片？|因为那时候她不知道一飞在给她照相。|Vì lúc đó chị không biết Nhất Phi đang chụp mình.
爬山的时候，白家月打算做什么？|她打算给王一雪照几张照片。|Cô ấy định chụp cho Nhất Tuyết vài tấm ảnh.
""")),
 dict(t="课文3", scene="在山上，王一雪和白家月边走边聊。", scene_vi="Vương Nhất Tuyết và Bạch Gia Nguyệt vừa đi vừa trò chuyện ở trên núi.", narr=False, lines=T("""
王一雪>家月，这里挺漂亮的，咱们在这里拍照吧。|Gia Nguyệt, chỗ này khá đẹp, chúng ta chụp ảnh ở đây đi.
白家月>这边没有太阳，咱们去那边吧。|Bên này không có nắng, chúng ta sang bên kia đi.
王一雪>好。你觉得我站在这些树中间怎么样？|Được. Em thấy chị đứng giữa mấy cái cây này thế nào?
白家月>挺好的。等一下，后边走过去两个人。|Khá đẹp. Đợi chút, phía sau có hai người đi qua.
王一雪>我准备好了，你照的时候告诉我。|Chị chuẩn bị xong rồi, lúc chụp thì báo chị nhé.
白家月>你不用看着我，想干什么都可以。|Chị không cần nhìn em, muốn làm gì cũng được.
王一雪>树上飞来了几只鸟，我就看它们吧。|Trên cây có mấy con chim bay đến, chị nhìn chúng vậy.
白家月>啊，手机没电了。|Ôi, điện thoại hết pin rồi.
"""), q=Q("""
王一雪想站在哪儿拍照？|站在那些树中间。|Đứng giữa những cái cây.
白家月为什么要等一下再照？|因为后边走过去两个人。|Vì phía sau có hai người đi qua.
白家月的手机怎么了？|手机没电了。|Điện thoại hết pin.
""")),
 dict(t="课文4", scene="在咖啡厅里，王一雪给白家月发短信。", scene_vi="Vương Nhất Tuyết gửi tin nhắn cho Bạch Gia Nguyệt trong quán cà phê.", narr=True, lines=T("""
家月，我收到了你的那封邮件，也看到了你给我照的照片，张张都很漂亮。|Gia Nguyệt, chị đã nhận được email của em, cũng xem ảnh em chụp cho chị rồi, tấm nào cũng rất đẹp.
我已经告诉了一飞，你的拍照水平比她高，她难过得很，哈哈。|Chị đã nói với Nhất Phi là trình độ chụp ảnh của em cao hơn nó, nó buồn lắm, ha ha.
不知道你对中国的音乐有没有兴趣？|Không biết em có hứng thú với âm nhạc Trung Quốc không?
我送你一张明天下午音乐会的门票。|Chị tặng em một vé buổi hòa nhạc chiều mai.
音乐会七点多结束，你听完了音乐会就来我家吃饭，尝尝我做的中国菜。你觉得怎么样？|Buổi hòa nhạc hơn bảy giờ kết thúc, em nghe xong thì đến nhà chị ăn cơm, nếm thử món Trung Quốc chị nấu. Em thấy sao?
"""), q=Q("""
王一雪觉得白家月的拍照水平怎么样？|比一飞高。|Cao hơn Nhất Phi.
音乐会什么时候结束？|七点多结束。|Hơn bảy giờ kết thúc.
听完音乐会，白家月可能做什么？|去王一雪家吃饭，尝尝她做的中国菜。|Đến nhà Nhất Tuyết ăn cơm, nếm món Trung Quốc chị nấu.
"""))],
grammar=[
 G("dehen", "程度补语（2）：……得很", "Bổ ngữ trình độ (2) – “……得很”",
   "Bổ ngữ trình độ “得很” thường dùng trong văn nói, đặt sau tính từ (hoặc động từ tâm lý), biểu thị mức độ cao (… lắm, … vô cùng).",
   [F("S:Chủ ngữ|A:Tính từ|kw:得很", [
     ("现在天气|好|[得很]", "。", "Bây giờ thời tiết đẹp lắm."),
     ("房间里面|热|[得很]", "。", "Trong phòng nóng lắm."),
     ("我觉得爬山|累|[得很]", "。", "Tôi thấy leo núi mệt lắm."),
     ("她|难过|[得很]", "。", "Cô ấy buồn lắm.")])]),
 G("lcchongdie", "量词重叠", "Lượng từ lặp lại",
   "Nhiều lượng từ có thể lặp lại (张张, 个个, 件件, 天天, 年年…) để nhấn mạnh mọi thành viên trong một phạm vi đều có chung một đặc điểm (… nào cũng…). Phía sau thường dùng “都”.",
   [F("S:Chủ ngữ|kw:Lượng từ lặp lại|kw2:都|V:Vị ngữ", [
     ("这些照片|[张张]|[都]|非常好看", "。", "Những bức ảnh này tấm nào cũng rất đẹp. (= 每张照片都非常好看)"),
     ("这些苹果|[个个]|[都]|很大", "。", "Những quả táo này quả nào cũng to. (= 每个苹果都很大)"),
     ("我想出去拍照，但是|[天天]||下雨", "。", "Tôi muốn ra ngoài chụp ảnh nhưng ngày nào cũng mưa. (= 每天都下雨)"),
     ("这些大衣|[件件]|[都]|很好看", "。", "Những chiếc áo khoác này cái nào cũng đẹp.")])]),
 G("cunxian3", "存现句（3）", "Câu tồn hiện (3) – xuất hiện / biến mất",
   "Để miêu tả sự xuất hiện hoặc biến mất của người, sự vật tại một nơi, dùng câu tồn hiện. Cấu trúc: Từ chỉ nơi chốn + động từ + bổ ngữ xu hướng / kết quả + (了) + cụm số lượng + người / vật.",
   [F("P:Nơi chốn|V:Động từ + bổ ngữ (+了)|Nu:Số lượng|N:Người / vật", [
     ("后边|走过去|两个|人", "。", "Phía sau có hai người đi qua."),
     ("前面|开过来|很多|车", "。", "Phía trước có nhiều xe chạy tới."),
     ("楼上|下来了|几个|人", "。", "Trên lầu có mấy người đi xuống."),
     ("树上|飞来了|几只|鸟", "。", "Trên cây có mấy con chim bay đến.")])]),
 G("lejiu", "紧缩复句“……了……就……”", "Câu ghép rút gọn “……了……就……”",
   "Cấu trúc “động từ 1 + 了 … 就 + động từ 2 …” biểu thị hai hành động xảy ra liên tiếp (… xong là …). Nếu hành động thứ hai cũng đã hoàn thành thì thêm “了” vào cuối câu.",
   [F("S:Chủ ngữ|V1:Động từ 1 + 了 + tân ngữ|kw:就|V2:Động từ 2", [
     ("你|听完了音乐会|[就]|来我家吃饭", "。", "Em nghe xong buổi hòa nhạc thì đến nhà chị ăn cơm."),
     ("我|吃了早饭|[就]|去学校了", "。", "Tôi ăn sáng xong là đi học rồi."),
     ("昨天我们|下了课|[就]|回家了", "。", "Hôm qua chúng tôi tan học xong là về nhà luôn."),
     ("爸爸每次|上了飞机|[就]|睡觉", "。", "Lần nào bố lên máy bay cũng ngủ ngay.")])]),
],
test=dict(
 l2=["等人|拍照|比较个子", "工作|吃饭|看电影", "他喜欢出去玩|这是他的相机|他照相水平很高"],
 l3=["电脑坏了|没收到邮件|没给她写邮件", "回家|爬山|买大衣", "女的不满意|张张都很好看|照片里的人太少", "多照几张照片|离自己远一点儿|先告诉自己一下"],
 r1=(["不好意思，我的没电了。", "我要去旅游，你呢？", "这里不好看，我们去那边吧。", "不好意思，我在听音乐，没听见。", "当然。我们先坐公交车，然后换地铁。", "除了爬山以外，别的我都不喜欢。"],
     ["你对什么运动感兴趣？", "你站在树前面，我给你拍张照。", "我能用你的手机打个电话吗？", "终于考完了，你假期要做什么？", "你在房间里干什么呢？我叫你好几次了。"]),
 r2=(["总是", "兴趣", "锻炼", "照相", "鞋", "难过"],
     ["假期我们要去海边玩，你有没有（　　）一起去？", "很久没有（　　）身体了，今天我要出去运动运动。", "前面走过来几个人，我去问问他们能不能帮我们（　　）。", "A：你怎么了？看起来有点儿（　　）。\nB：今天的考试我考得不太好。", "A：你怎么（　　）吃外卖？\nB：我这几天忙得很，没有时间自己做饭。"]),
 r3=[("这些大衣件件都非常好看，我都想买，但一看多少钱，就一件也不想买了。", "他为什么不想买大衣？", "很难看|太贵了|不需要"),
     ("我送给小白一张音乐会的票，她收到票特别高兴。她告诉我，她对音乐非常感兴趣，明年读大学时要学音乐。", "关于小白，可以知道什么？", "喜欢音乐|正在学习音乐|买了音乐会的票"),
     ("上个星期六，我和姐姐一起去爬山，还照了很多照片，有站在树下的，还有坐在地上的。我们想比较一下拍照水平，所以回到家就让妈妈在电脑上看我们的照片，妈妈觉得我照的照片比姐姐的好看，姐姐听了有点儿难过。",
      ("他和姐姐没有做什么？", "爬山|拍照|玩电脑"), ("妈妈：", "也去爬山了|照了很多照片|觉得他照的照片好"))],
 w1=["你看，太（yáng）出来了，天气很好，咱们出去走走吧。", "在这里，你可以爬（shān），也可以去海里游泳，想干什么就干什么。", "今天我（shōu）到了姐姐的邮件，她告诉了我很多大学里的事情。"],
 w2=[("锻炼", "他们每天下午都去公园锻炼身体。"), ("结束", "音乐会结束了，大家都站起来了。"), ("拍照", "她正在用手机拍照。")],
 gl={"11": "Bạn hứng thú với môn thể thao nào? → F: Ngoài leo núi ra, mấy môn khác mình đều không thích.",
     "12": "Bạn đứng trước cái cây, mình chụp cho bạn một tấm. → C: Chỗ này không đẹp, chúng ta sang bên kia đi.",
     "13": "Mình dùng điện thoại của bạn gọi một cuộc được không? → A: Ngại quá, máy mình hết pin rồi.",
     "14": "Cuối cùng cũng thi xong, kỳ nghỉ bạn định làm gì? → B: Mình đi du lịch, còn bạn?",
     "15": "Bạn làm gì trong phòng vậy? Mình gọi bạn mấy lần rồi. → D: Ngại quá, mình đang nghe nhạc, không nghe thấy.",
     "16": "有没有兴趣 – có hứng thú không. → B 兴趣.",
     "17": "锻炼身体 – rèn luyện sức khỏe. → C 锻炼.",
     "18": "帮我们照相 – chụp ảnh giúp chúng tôi. → D 照相.",
     "19": "看起来有点儿难过 – trông hơi buồn. → F 难过.",
     "20": "总是吃外卖 – lúc nào cũng gọi đồ ăn ngoài. → A 总是.",
     "21": "“但一看多少钱，就一件也不想买了” – xem giá xong thì chẳng muốn mua cái nào → B 太贵了.",
     "22": "“她对音乐非常感兴趣” → A 喜欢音乐 (năm sau mới học, vé là được tặng).",
     "23": "Họ leo núi, chụp ảnh; người xem ảnh trên máy tính là mẹ → C 玩电脑.",
     "24": "“妈妈觉得我照的照片比姐姐的好看” → C."}),
)
