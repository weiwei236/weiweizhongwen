# -*- coding: utf-8 -*-
# HSK 3 – Bài 13: 我的新邻居来自英国
from gtb_gen import V, T, Q, F, G
B = {}

B[13] = dict(zh="我的新邻居来自英国", vi="Hàng xóm mới của tôi đến từ nước Anh",
intro="Dương Đồng Lạc mời đồng nghiệp ăn món miền Nam, Vương Nhất Tuyết chuẩn bị tiệc sinh nhật cho Tiểu Minh và mời đôi vợ chồng hàng xóm người Anh đến chơi.",
vocab=V("""
请客|qǐngkè|dong|đãi khách, mời khách|今天我请客，大家别客气。~Hôm nay tôi mời, mọi người đừng khách sáo.
南方|nánfāng|dt|miền Nam|南方的冬天不太冷。~Mùa đông miền Nam không lạnh lắm.
北方|běifāng|dt|miền Bắc|北方人喜欢吃饺子。~Người miền Bắc thích ăn sủi cảo.
做法|zuòfǎ|dt|cách làm|这个菜的做法很简单。~Cách làm món này rất đơn giản.
不同|bù tóng|tt|khác nhau|我们的想法不同。~Suy nghĩ của chúng tôi khác nhau.
加|jiā|dong|thêm|咖啡里再加一点儿糖。~Cho thêm chút đường vào cà phê.
的话|dehuà|tro|nếu|你有时间的话，就来我家玩儿。~Nếu bạn có thời gian thì đến nhà mình chơi.
做客|zuòkè|dong|làm khách|周末我去朋友家做客。~Cuối tuần tôi đến nhà bạn chơi.
邻居|línjū|dt|hàng xóm, láng giềng|我的邻居很热情。~Hàng xóm của tôi rất nhiệt tình.
放心|fàngxīn|dong|yên tâm|放心吧，我会照顾好自己的。~Yên tâm đi, con sẽ tự chăm sóc tốt bản thân.
酒|jiǔ|dt|rượu|开车的时候不能喝酒。~Lúc lái xe không được uống rượu.
放|fàng|dong|đặt, để|把书放在桌子上吧。~Để sách lên bàn đi.
客人|kèrén|dt|khách, khách hàng|今天家里来了很多客人。~Hôm nay nhà có nhiều khách.
晚会|wǎnhuì|dt|dạ hội, buổi liên hoan buổi tối|新年晚会八点开始。~Dạ hội năm mới bắt đầu lúc tám giờ.
礼物|lǐwù|dt|quà, món quà|这是我送你的生日礼物。~Đây là quà sinh nhật tôi tặng bạn.
画家|huàjiā|dt|họa sĩ|他想当一名画家。~Cậu ấy muốn làm họa sĩ.
盘子|pánzi|dt|đĩa|请把盘子拿过来。~Hãy mang cái đĩa lại đây.
一边|yìbiān|pho|vừa (…vừa…)|他一边吃饭一边看电视。~Anh ấy vừa ăn cơm vừa xem TV.
聊天儿|liáotiānr|dong|trò chuyện, tán gẫu|我们在咖啡馆聊天儿。~Chúng tôi trò chuyện ở quán cà phê.
来自|láizì|dong|đến từ|她来自上海。~Cô ấy đến từ Thượng Hải.
夫妻|fūqī|dt|vợ chồng|他们是一对年轻的夫妻。~Họ là một đôi vợ chồng trẻ.
红茶|hóngchá|dt|hồng trà, trà đen|英国人喜欢喝红茶。~Người Anh thích uống hồng trà.
直到|zhídào|dong|cho đến khi|我们聊天儿直到晚上十点。~Chúng tôi trò chuyện mãi đến mười giờ tối.
地图|dìtú|dt|bản đồ|墙上有一张中国地图。~Trên tường có một tấm bản đồ Trung Quốc.
感到|gǎndào|dong|cảm thấy|听到这个消息，我感到很高兴。~Nghe tin này, tôi cảm thấy rất vui.
东方|dōngfāng|dt|phương Đông|他对东方的文化很感兴趣。~Anh ấy rất hứng thú với văn hóa phương Đông.
文化|wénhuà|dt|văn hóa|中国文化有很长的历史。~Văn hóa Trung Quốc có lịch sử lâu đời.
英国|Yīngguó|rieng|nước Anh|我的新邻居来自英国。~Hàng xóm mới của tôi đến từ nước Anh.
"""),
texts=[dict(t="课文1", scene="在饭馆，杨同乐请同事吃饭。", scene_vi="Dương Đồng Lạc mời đồng nghiệp ăn cơm tại nhà hàng.", narr=False, lines=T("""
杨同乐>今天我请客，你们想吃什么就点什么！|Hôm nay tôi mời, mọi người muốn ăn gì cứ gọi nấy!
王一雪>那我就不客气了。听说这家饭馆的鱼做得很特别？|Vậy tôi không khách sáo nữa. Nghe nói cá ở quán này làm rất đặc biệt?
杨同乐>对，南方菜跟你们北方菜的做法不同。除了鱼，你们还想吃什么？|Đúng vậy, món miền Nam có cách làm khác món miền Bắc của các bạn. Ngoài cá ra, các bạn còn muốn ăn gì?
同事>我不常吃南方菜，还是你决定吧。|Tôi không hay ăn món miền Nam, cậu quyết định đi.
杨同乐>好，那再加一个鸡肉，一个……|Được, vậy thêm một món gà, một món…
王一雪>咱们就三个人，别点那么多。|Chúng ta chỉ có ba người, đừng gọi nhiều thế.
杨同乐>好，那先来这几个菜。|Được, vậy gọi mấy món này trước.
王一雪>对了，下周我儿子过生日，你们有时间的话，就来我家做客，我给你们做北京菜。|À phải rồi, tuần sau con trai tôi sinh nhật, nếu các bạn có thời gian thì đến nhà tôi chơi, tôi nấu món Bắc Kinh cho các bạn.
"""), q=Q("""
这家饭馆什么菜做得很特别？|鱼。|Cá.
王一雪为什么要请同事去她家？|因为下周她儿子过生日。|Vì tuần sau con trai chị ấy sinh nhật.
王一雪打算给大家做什么菜？|北京菜。|Món Bắc Kinh.
""")),
 dict(t="课文2", scene="在家里，王一雪和刘明为生日会做准备。", scene_vi="Vương Nhất Tuyết và Lưu Minh đang chuẩn bị cho bữa tiệc sinh nhật ở nhà.", narr=False, lines=T("""
王一雪>第一次请新邻居来做客，总是担心有什么没准备好。|Lần đầu mời hàng xóm mới đến chơi, cứ lo có gì đó chưa chuẩn bị xong.
刘明>放心吧，我帮你看了，都已经准备好了。|Yên tâm đi, anh xem giúp em rồi, đều chuẩn bị xong cả rồi.
王一雪>我记得刚才已经把饮料拿出来了，怎么不见了？|Em nhớ lúc nãy đã lấy nước ngọt ra rồi, sao lại không thấy đâu?
刘明>我把饮料和酒都放进冰箱里了，客人来了再拿出来。|Anh để nước ngọt và rượu vào tủ lạnh rồi, khách đến rồi lấy ra.
王一雪>音乐的声音合适吗？|Âm lượng nhạc vừa chưa?
刘明>你把声音开得太大了，我去关小一点儿。|Em mở to quá, để anh vặn nhỏ lại chút.
王一雪>好，那我们就等客人来吧。|Được, vậy chúng ta đợi khách đến thôi.
"""), q=Q("""
王一雪刚才把什么拿出来了？|饮料。|Nước ngọt.
刘明把饮料和酒放在哪儿了？|放进冰箱里了。|Để vào tủ lạnh.
刘明觉得音乐的声音合适吗？|不合适，声音开得太大了。|Không, mở to quá.
""")),
 dict(t="课文3", scene="在家里，王一雪和刘明办生日会。", scene_vi="Vương Nhất Tuyết và Lưu Minh đang tổ chức tiệc sinh nhật ở trong nhà.", narr=False, lines=T("""
王一雪>谢谢你们来参加我儿子的生日晚会，希望大家今晚玩得开心。|Cảm ơn mọi người đến dự tiệc sinh nhật con trai tôi, chúc mọi người tối nay chơi vui vẻ.
杨同乐>小明，生日快乐！我准备了一个小礼物，希望你喜欢！|Tiểu Minh, chúc mừng sinh nhật! Chú chuẩn bị một món quà nhỏ, mong cháu thích!
刘小明>谢谢您，我可以打开吗？|Cháu cảm ơn chú, cháu mở ra được không ạ?
杨同乐>当然可以，你妈妈说你跟姐姐一样，都喜欢画画，对吗？|Tất nhiên rồi, mẹ cháu nói cháu cũng giống chị, đều thích vẽ, đúng không?
刘小明>对，我想做一名画家。啊！画板和画笔，这正是我需要的。我太喜欢了。|Vâng, cháu muốn làm họa sĩ. A! Bảng vẽ và bút vẽ, đúng thứ cháu cần. Cháu thích lắm.
王一雪>我去把盘子拿过来，咱们一边吃蛋糕，一边聊天儿吧。|Tôi đi lấy đĩa lại đây, chúng ta vừa ăn bánh vừa trò chuyện nhé.
"""), q=Q("""
杨同乐送给刘小明什么礼物？|画板和画笔。|Bảng vẽ và bút vẽ.
刘小明收到礼物后说什么了？|这正是我需要的，我太喜欢了。|Đúng thứ cháu cần, cháu thích lắm.
刘小明以后想做什么？|做一名画家。|Làm họa sĩ.
""")),
 dict(t="课文4", scene="在家里，王一雪在写日记。", scene_vi="Vương Nhất Tuyết đang viết nhật ký ở trong nhà.", narr=True, lines=T("""
我的新邻居是来自英国的夫妻。|Hàng xóm mới của tôi là một đôi vợ chồng đến từ nước Anh.
上周我去他们家做客了。|Tuần trước tôi đến nhà họ chơi.
他们做了很多好吃的，还准备了英国的红茶。|Họ nấu rất nhiều món ngon, còn chuẩn bị cả hồng trà Anh.
那天我跟他们一边喝红茶，一边聊天儿，直到十二点多才回家。|Hôm đó tôi vừa uống hồng trà vừa trò chuyện với họ, mãi hơn mười hai giờ mới về nhà.
他们年轻的时候喜欢旅游，他家有一张世界地图，上面每一个红点都是他们去过的地方。|Hồi trẻ họ thích đi du lịch, nhà họ có một tấm bản đồ thế giới, mỗi chấm đỏ trên đó đều là nơi họ đã đến.
后来，他们感到东方的文化很特别，就开始学习中文。|Sau đó, họ cảm thấy văn hóa phương Đông rất đặc biệt nên bắt đầu học tiếng Trung.
今天是小明的生日，我请他们到我家玩，来看看中国人的家，也尝尝中国菜。|Hôm nay là sinh nhật Tiểu Minh, tôi mời họ đến nhà chơi, xem nhà của người Trung Quốc, cũng nếm thử món Trung Quốc.
"""), q=Q("""
王一雪家的新邻居是什么人？|来自英国的夫妻。|Một đôi vợ chồng đến từ nước Anh.
世界地图上的红点是什么？|是他们去过的地方。|Là những nơi họ đã đến.
他们为什么开始学习中文？|因为他们感到东方的文化很特别。|Vì họ thấy văn hóa phương Đông rất đặc biệt.
"""))],
grammar=[
 G("dehua", "假设复句“……的话，就……”", "Câu ghép giả định “……的话，就……”",
   "Câu ghép giả định “……的话，就……” thường dùng trong văn nói: vế thứ nhất đưa ra giả thiết, vế thứ hai biểu thị kết quả hoặc kết luận có được (nếu… thì…).",
   [F("C:Giả thiết|kw:的话，|S:(Chủ ngữ)|kw2:就|V:Kết quả", [
     ("你们有时间|[的话，]||[就]|来我家做客", "。", "Nếu các bạn có thời gian thì đến nhà tôi chơi."),
     ("你觉得满意|[的话，]|咱们|[就]|买", "。", "Nếu bạn thấy hài lòng thì chúng ta mua."),
     ("明天天气好|[的话，]|我|[就]|去爬山", "。", "Nếu mai trời đẹp thì tôi đi leo núi.")])]),
 G("ba4", "“把”字句（4）", "Câu chữ “把” (4) – bổ ngữ xu hướng / trạng thái",
   "Trong câu chữ “把”, sau động từ có thể dùng bổ ngữ xu hướng hoặc bổ ngữ trạng thái để biểu thị sự thay đổi vị trí hoặc trạng thái của sự vật. Cấu trúc: Chủ ngữ + 把 + tân ngữ + động từ + bổ ngữ xu hướng / trạng thái.",
   [F("S:Chủ ngữ|kw:把|O:Tân ngữ|V:Động từ|X:Bổ ngữ xu hướng / trạng thái", [
     ("你|[把]|声音|开|得太大了", "。", "Em mở âm lượng to quá."),
     ("他|[把]|球|踢|进去了吗", "？", "Anh ấy sút bóng vào chưa?"),
     ("你|[把]|字|写|得太小了", "，我看不清楚。", "Bạn viết chữ nhỏ quá, tôi nhìn không rõ."),
     ("我去|[把]|盘子|拿|过来", "。", "Tôi đi lấy đĩa lại đây.")])]),
 G("yibian", "并列复句“一边……，一边……”", "Câu ghép đẳng lập “一边……，一边……”",
   "Cấu trúc “一边……，一边……” biểu thị hai hành động xảy ra đồng thời (vừa… vừa…), có thể rút gọn thành “边……边……”.",
   [F("S:Chủ ngữ|kw:一边 / 边|V1:Hành động 1|kw2:一边 / 边|V2:Hành động 2", [
     ("咱们|[一边]|吃蛋糕，|[一边]|聊天儿吧", "。", "Chúng ta vừa ăn bánh vừa trò chuyện nhé."),
     ("我喜欢|[一边]|跑步，|[一边]|听音乐", "。", "Tôi thích vừa chạy bộ vừa nghe nhạc."),
     ("你不应该|[边]|开车|[边]|打电话", "。", "Bạn không nên vừa lái xe vừa gọi điện thoại.")])]),
],
test=dict(
 l2=["常骑车|不会骑车|想买自行车", "找书|看地图|找地图", "找工作|学习新东西|教东西方文化"],
 l3=["她现在不骑了|是她的生日礼物|是她送妈妈的礼物", "酒|花|水果", "两天|一周|两个星期", "两个|三个|四个"],
 r1=(["这些都是我去过的地方。", "谢谢，我很喜欢这位画家。", "不好意思，可能是糖放多了。", "好的，没想到天气越来越冷了。", "当然。我们先坐公交车，然后换地铁。", "那是张先生和王女士，他们是夫妻。"],
     ["那边的两个人是谁？", "你把蛋糕做得太甜了。", "你的地图上怎么有这么多红点？", "我觉得你们家的这些画太漂亮了。", "明天有雪，出去的话，就再加一件衣服吧。"]),
 r2=(["请客", "感到", "不同", "放心", "鞋", "来自"],
     ["我在比赛中得到了好成绩，（　　）特别快乐。", "老师，我有一个问题：这两个词有什么（　　）？", "大家好，我（　　）英国，欢迎你们有时间去旅游。", "A：今天我（　　），您想吃什么就点什么。\nB：您太客气了，我吃什么都可以。", "A：下课后，别忘了把这些书放回办公室去。\nB：好的，李老师，您（　　）吧。"]),
 r3=[("喂，我才看见您的电话，刚才我去楼下接几位客人，没带手机。您找我有什么事？", "他正在做什么？", "打电话|接客人|往楼下走"),
     ("你写作业以前先复习笔记吗？小安跟你不同，她是遇到不会做的题再看笔记。", "小安是怎么做的？", "先复习|先写作业|边看笔记边写作业"),
     ("明天晚上公司有一个晚会，小丽很想参加，但是她找不到合适的衣服，需要买一条新裙子。小丽希望同事明天有时间的话，能和她一起去买，但是同事明天白天要去开会，没有时间去商场，只能和小丽在晚会上见了。",
      ("小丽明天做什么？", "买衣服|去开会|和朋友吃饭"), ("关于同事，可以知道什么？", "要去参加晚会|没有合适的衣服|要跟小丽去买裙子"))],
 w1=["我下周休假，打算去（nán）方旅游。", "五个人点四个菜有点儿少，再（jiā）两个吧。", "今天是我的生日，这是妈妈送我的生日（lǐ）物。"],
 w2=[("做客", "他们一家人带着礼物去朋友家做客。"), ("盘子", "妈妈正在洗盘子。"), ("聊天儿", "三个朋友一边喝茶一边聊天儿。")],
 gl={"11": "Hai người đằng kia là ai? → F: Đó là ông Trương và bà Vương, họ là vợ chồng.",
     "12": "Bạn làm bánh ngọt quá. → C: Ngại quá, chắc cho nhiều đường quá.",
     "13": "Sao bản đồ của bạn có nhiều chấm đỏ thế? → A: Đây đều là những nơi mình đã đến.",
     "14": "Mình thấy mấy bức tranh nhà bạn đẹp quá. → B: Cảm ơn, mình rất thích họa sĩ này.",
     "15": "Mai có tuyết, nếu ra ngoài thì mặc thêm một cái áo nhé. → D: Vâng, không ngờ trời ngày càng lạnh.",
     "16": "感到特别快乐 – cảm thấy đặc biệt vui. → B 感到.",
     "17": "有什么不同 – có gì khác nhau. → C 不同.",
     "18": "我来自英国 – tôi đến từ nước Anh. → F 来自.",
     "19": "今天我请客 – hôm nay tôi mời. → A 请客.",
     "20": "您放心吧 – thầy cứ yên tâm. → D 放心.",
     "21": "“刚才我去楼下接几位客人” – việc vừa xong; bây giờ anh ấy đang gọi lại điện thoại → A 打电话.",
     "22": "“她是遇到不会做的题再看笔记” → B 先写作业.",
     "23": "“需要买一条新裙子” → A 买衣服.",
     "24": "Đồng nghiệp “只能和小丽在晚会上见了” → A 要去参加晚会."}),
)
