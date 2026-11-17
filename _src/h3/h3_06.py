# -*- coding: utf-8 -*-
# HSK 3 – Bài 6: 高铁上还可以点外卖
from gtb_gen import V, T, Q, F, G
B = {}

B[6] = dict(zh="高铁上还可以点外卖", vi="Trên tàu cao tốc còn có thể gọi đồ ăn",
intro="Bạch Gia Nguyệt lần đầu đi tàu cao tốc từ Bắc Kinh đến Thượng Hải: mua vé bằng app, suýt muộn vì đi nhầm đường, quẹt hộ chiếu vào ga và gọi đồ ăn ngay trên tàu.",
vocab=V("""
该|gāi|nn|nên, phải (đến lúc phải)|十二点了，该吃午饭了。~Mười hai giờ rồi, đến giờ ăn trưa rồi.
打算|dǎsuàn|dong|dự định; kế hoạch|你打算什么时候回国？~Bạn định khi nào về nước?
高铁|gāotiě|dt|tàu cao tốc|坐高铁去上海只要四个多小时。~Đi tàu cao tốc đến Thượng Hải chỉ mất hơn bốn tiếng.
行|xíng|dong|được, có thể|明天下午三点见，行吗？~Ba giờ chiều mai gặp nhé, được không?
路口|lùkǒu|dt|giao lộ, lối rẽ, đầu đường|到了前面的路口往左走。~Đến ngã tư phía trước thì rẽ trái.
小心|xiǎoxīn|dong|cẩn thận, chú ý|下雨了，路上小心！~Trời mưa rồi, đi đường cẩn thận nhé!
迟到|chídào|dong|đến muộn|对不起，我迟到了。~Xin lỗi, tôi đến muộn.
红绿灯|hónglǜdēng|dt|đèn giao thông|过了红绿灯就是我家。~Qua đèn giao thông là đến nhà tôi.
后来|hòulái|dt|sau đó, về sau|我们以前是同学，后来成了好朋友。~Trước đây chúng tôi là bạn học, sau đó trở thành bạn thân.
急|jí|tt|gấp, lo lắng|别急，慢慢说。~Đừng vội, từ từ nói.
如果|rúguǒ|lien|nếu|如果明天下雨，我们就不去了。~Nếu mai trời mưa thì chúng ta không đi nữa.
以前|yǐqián|dt|trước đây|我以前没来过这儿。~Trước đây tôi chưa từng đến đây.
耳机|ěrjī|dt|tai nghe|在图书馆听音乐要用耳机。~Nghe nhạc trong thư viện phải dùng tai nghe.
充电宝|chōngdiànbǎo|dt|sạc dự phòng|出门别忘了带充电宝。~Ra ngoài đừng quên mang sạc dự phòng.
常用|cháng yòng|cum|thường dùng|这些都是常用的汉字。~Đây đều là những chữ Hán thường dùng.
越|yuè|pho|càng… (càng…)|天气越来越冷了。~Thời tiết càng ngày càng lạnh.
分开|fēnkāi|dong|tách ra|人太多了，我们别分开走。~Đông người quá, chúng ta đừng đi tách nhau.
检查|jiǎnchá|dong|kiểm tra|写完以后再检查一下。~Viết xong thì kiểm tra lại một lượt.
刷|shuā|dong|quẹt (thẻ, mã QR…)|坐地铁可以刷手机。~Đi tàu điện ngầm có thể quẹt điện thoại.
检票|jiǎnpiào|dong|kiểm vé, soát vé|火车快开了，开始检票了。~Tàu sắp chạy rồi, bắt đầu soát vé.
电梯|diàntī|dt|thang máy|我们坐电梯上去吧。~Chúng ta đi thang máy lên đi.
放假|fàngjià|dong|nghỉ phép, nghỉ lễ|学校下个星期放假。~Tuần sau trường được nghỉ.
沙发|shāfā|dt|ghế sofa|他坐在沙发上看电视。~Anh ấy ngồi trên sofa xem TV.
安静|ānjìng|tt|yên tĩnh|图书馆里很安静。~Trong thư viện rất yên tĩnh.
选择|xuǎnzé|dong|chọn, lựa chọn|你可以选择你喜欢的颜色。~Bạn có thể chọn màu bạn thích.
必须|bìxū|pho|phải, nhất định phải|明天你必须早点儿来。~Ngày mai bạn nhất định phải đến sớm.
北京南站|Běijīng Nán Zhàn|rieng|ga Bắc Kinh Nam|我们从北京南站坐高铁。~Chúng tôi đi tàu cao tốc từ ga Bắc Kinh Nam.
"""),
texts=[dict(t="课文1", scene="在咖啡厅里，李文和白家月在聊天儿。", scene_vi="Lý Văn và Bạch Gia Nguyệt đang trò chuyện trong quán cà phê.", narr=False, lines=T("""
李文>家月，咱们该买去上海的票了。你打算怎么去上海？|Gia Nguyệt, chúng ta nên mua vé đi Thượng Hải rồi. Cậu định đi Thượng Hải bằng gì?
白家月>我还没坐过高铁，咱们坐高铁去，怎么样？|Mình chưa đi tàu cao tốc bao giờ, chúng ta đi tàu cao tốc nhé, thế nào?
李文>没问题，从北京到上海的高铁很多，非常方便。|Không vấn đề, tàu cao tốc từ Bắc Kinh đến Thượng Hải rất nhiều, vô cùng tiện.
白家月>行！怎么买高铁票？|Được! Mua vé tàu cao tốc thế nào?
李文>用手机App就能买。给我你的护照，我帮你买。|Dùng app trên điện thoại là mua được. Đưa mình hộ chiếu, mình mua giúp cho.
白家月>早就听说过高铁，终于可以坐上了。|Nghe nói về tàu cao tốc từ lâu, cuối cùng cũng được đi rồi.
李文>高铁又快又舒服，你一定会喜欢的。|Tàu cao tốc vừa nhanh vừa thoải mái, cậu nhất định sẽ thích.
"""), q=Q("""
李文和白家月打算去哪个城市？|上海。|Thượng Hải.
白家月为什么想坐高铁？|因为她还没坐过高铁。|Vì cô ấy chưa đi tàu cao tốc bao giờ.
他们打算怎么买高铁票？|用手机App买。|Mua bằng app trên điện thoại.
""")),
 dict(t="课文2", scene="在车上，刘明开车送白家月和李文去高铁站。", scene_vi="Trên xe, Lưu Minh lái xe đưa Bạch Gia Nguyệt và Lý Văn đến ga tàu cao tốc.", narr=False, lines=T("""
刘明>过了前面的路口就到高铁站了。|Qua ngã tư phía trước là đến ga tàu cao tốc rồi.
白家月>我看见了。马上就到了，这条路车很多，您小心点儿。|Em thấy rồi. Sắp tới rồi, đường này đông xe, anh cẩn thận chút nhé.
刘明>好，你们还有一个小时，应该不会迟到的。|Ừ, các em còn một tiếng nữa, chắc sẽ không muộn đâu.
白家月>我发现这条路车多，红绿灯也多。|Em thấy đường này đông xe, đèn giao thông cũng nhiều.
刘明>是啊，这条路我走过一次，后来再也不走了。|Đúng vậy, đường này anh đi một lần rồi, sau đó không bao giờ đi nữa.
白家月>那您今天为什么走了这条路？|Vậy sao hôm nay anh lại đi đường này?
刘明>我一急就走错了。如果没走错，二十分钟以前就到了。|Anh vội quá nên đi nhầm. Nếu không đi nhầm thì đã đến từ hai mươi phút trước rồi.
"""), q=Q("""
刘明为什么说“应该不会迟到”？|因为他们还有一个小时。|Vì họ còn một tiếng nữa.
白家月觉得这条路有什么问题？|车多，红绿灯也多。|Đông xe, đèn giao thông cũng nhiều.
刘明为什么今天走了这条路？|因为他一急就走错了。|Vì anh ấy vội nên đi nhầm.
""")),
 dict(t="课文3", scene="在高铁站，李文和白家月排队安检、检票。", scene_vi="Lý Văn và Bạch Gia Nguyệt xếp hàng kiểm tra an ninh và soát vé ở ga tàu cao tốc.", narr=False, lines=T("""
白家月>李文，我的耳机没电了，你有充电宝吗？|Lý Văn, tai nghe của mình hết pin rồi, cậu có sạc dự phòng không?
李文>有，这些常用的东西我都放在包里了，我给你拿。|Có, mấy thứ thường dùng này mình đều để trong túi, mình lấy cho.
白家月>前面的人越来越多。|Người phía trước càng lúc càng đông.
李文>对，马上就进高铁站了。咱们一起走，别分开。|Ừ, sắp vào ga rồi. Chúng ta đi cùng nhau, đừng tách ra.
白家月>好，你检查一下，高铁票都拿好了吗？|Được, cậu kiểm tra xem, vé tàu cầm đủ chưa?
李文>不用拿票，刷护照就能检票进站。|Không cần cầm vé, quẹt hộ chiếu là soát vé vào ga được.
白家月>去哪里检票？|Soát vé ở đâu?
李文>检票口在二层，我们一会儿坐电梯上去。|Cửa soát vé ở tầng hai, lát nữa chúng ta đi thang máy lên.
"""), q=Q("""
白家月为什么要用充电宝？|因为她的耳机没电了。|Vì tai nghe của cô ấy hết pin.
他们怎么检票进站？|刷护照就能检票进站。|Quẹt hộ chiếu là vào ga được.
他们怎么去检票口？|坐电梯上去。|Đi thang máy lên.
""")),
 dict(t="课文4", scene="在家里，白家月给安妮打电话介绍自己的旅行。", scene_vi="Trong nhà, Bạch Gia Nguyệt gọi điện cho Annie để giới thiệu về chuyến đi của mình.", narr=True, lines=T("""
这次放假，我去了北京，还去了上海。|Kỳ nghỉ lần này, mình đã đi Bắc Kinh, còn đi cả Thượng Hải.
我是从北京南站坐高铁去的上海。|Mình đi tàu cao tốc từ ga Bắc Kinh Nam đến Thượng Hải.
我觉得坐在高铁上跟坐在家里的沙发上一样，又安静又舒服。|Mình thấy ngồi trên tàu cao tốc giống như ngồi trên sofa ở nhà, vừa yên tĩnh vừa thoải mái.
坐累了就站一会儿，饿了就点外卖。|Ngồi mệt thì đứng một lát, đói thì gọi đồ ăn.
对，你没听错，高铁上可以点外卖，|Đúng vậy, bạn không nghe nhầm đâu, trên tàu cao tốc có thể gọi đồ ăn,
只需要选择好车站和想吃的东西，到站时不用下车，服务员就会给你拿过来。|chỉ cần chọn ga và món muốn ăn, đến ga không cần xuống tàu, nhân viên sẽ mang đến cho bạn.
现在喜欢坐高铁的人越来越多。|Bây giờ người thích đi tàu cao tốc ngày càng nhiều.
我爸妈来中国旅游的时候，必须带他们也坐一次高铁。|Khi bố mẹ mình sang Trung Quốc du lịch, nhất định phải đưa họ đi tàu cao tốc một lần.
"""), q=Q("""
白家月是怎么去上海的？|从北京南站坐高铁去的。|Đi tàu cao tốc từ ga Bắc Kinh Nam.
高铁上怎么点外卖？|选择好车站和想吃的东西，到站时服务员就会拿过来。|Chọn ga và món ăn, đến ga nhân viên sẽ mang đến.
白家月想带谁坐高铁？|她爸妈。|Bố mẹ cô ấy.
"""))],
grammar=[
 G("gaile", "固定格式“该……了”", "Cấu trúc cố định “该……了”",
   "“该……了” thường dùng trong văn nói, biểu thị đã đến lúc cần làm một việc gì đó (đến lúc… rồi, phải… rồi).",
   [F("S:(Chủ ngữ)|kw:该|V:Động từ + tân ngữ|kw2:了", [
     ("咱们|[该]|买去上海的票|[了]", "。", "Chúng ta nên mua vé đi Thượng Hải rồi."),
     ("八点了，|[该]|上课|[了]", "。", "Tám giờ rồi, đến giờ vào học rồi."),
     ("已经很晚了，我|[该]|睡觉|[了]", "。", "Muộn lắm rồi, tôi phải đi ngủ thôi."),
     ("天已经黑了，我们|[该]|回家|[了]", "。", "Trời tối rồi, chúng ta nên về nhà thôi.")])]),
 G("ruguo", "假设复句“如果……，就……”", "Câu ghép giả định “如果……，就……”",
   "Trong câu “如果……，就……”, vế sau “如果” là giả thiết, vế sau “就” là kết quả trong tình huống giả thiết đó (nếu… thì…). Lưu ý: chủ ngữ của vế thứ hai phải đặt trước “就”.",
   [F("kw:如果|C:Giả thiết|S:(Chủ ngữ / trạng ngữ vế 2)|kw2:就|V:Kết quả", [
     ("[如果]|没走错，|二十分钟以前|[就]|到了", "。", "Nếu không đi nhầm thì đã đến từ hai mươi phút trước."),
     ("[如果]|你需要帮忙，||[就]|给我打电话", "。", "Nếu bạn cần giúp thì gọi điện cho tôi."),
     ("[如果]|有时间，|我|[就]|去上海玩几天", "。", "Nếu có thời gian, tôi sẽ đi Thượng Hải chơi vài ngày."),
     ("[如果]|明天下雨，|咱们|[就]|在家看电影", "。", "Nếu mai trời mưa, chúng ta sẽ ở nhà xem phim.")])]),
 G("yuelaiyue", "固定短语“越来越”", "Cụm từ cố định “越来越”",
   "“越来越” đứng trước tính từ hoặc động từ tâm lý, biểu thị mức độ thay đổi theo thời gian (càng ngày càng…). Trước tính từ / động từ tâm lý đó không được thêm phó từ chỉ mức độ (không nói 越来越很多).",
   [F("S:Chủ ngữ|kw:越来越|A:Tính từ / động từ tâm lý", [
     ("前面的人|[越来越]|多", "。", "Người phía trước càng lúc càng đông."),
     ("我|[越来越]|喜欢这里的生活了", "。", "Tôi càng ngày càng thích cuộc sống ở đây."),
     ("她|[越来越]|漂亮了", "。", "Cô ấy càng ngày càng xinh."),
     ("喜欢坐高铁的人|[越来越]|多", "。", "Người thích đi tàu cao tốc ngày càng nhiều.")])]),
],
test=dict(
 l2=["找人|检票|买票", "回家|去花园|再玩一会儿", "飞机票太贵了|起飞时间太晚了|坐高铁比坐飞机快"],
 l3=["白楼的西边|路口的东边|路口的西边", "现在很难过|要出国上学了|是他初中时认识的", "一次|两次|三次", "走路|跑步|坐公交车"],
 r1=(["好的，我会慢慢开的。", "妈妈说她要带我去海边。", "不会，从这儿走过去只要十分钟。", "爸爸让我晚上九点以前必须回家。", "当然。我们先坐公交车，然后换地铁。", "从这儿往前走，到了第一个路口，往右走就是。"],
     ["就要放假了，你打算做什么？", "下雪了，你路上一定要小心。", "不好意思，请问地铁站怎么走？", "你一直看手表，有什么急事吗？", "还有30分钟电影就开始了，咱们会迟到吗？"]),
 r2=(["选择", "高铁", "小心", "电梯", "鞋", "检票"],
     ["该（　　）了。拿好票，我们现在就过去吧。", "路上（　　）点儿，到了那儿就给我打电话。", "你可以（　　）这家宾馆，就在火车站旁边，方便得很。", "A：你怎么还没到？大家都在等你。\nB：不好意思，我已经到楼下了，马上就坐（　　）上去。", "A：我们这次旅游还坐（　　），怎么样？\nB：行，又快又舒服，也比坐飞机方便。"]),
 r3=[("我爱人对现在住的房子比较满意。房子虽然不大，但很干净，也很安静，住着很舒服。", "他现在的房子怎么样？", "很大|很舒服|不太安静"),
     ("乐乐，你从酒店出来后往西走，到第一个红绿灯再往北走，就能看到咖啡馆了，我就在那儿等你。", "他在哪儿等乐乐？", "酒店|咖啡馆|红绿灯路口"),
     ("明天我是这么打算的：如果天气好，咱们就去爬山，在外面拍拍照、吃吃东西。这几天天气越来越热了，咱们早点儿去，下午就回来。如果明天下雨，咱们就在家里看电影吧。",
      ("如果明天不下雨，他打算做什么？", "去外面爬山|在家看电影|去超市买东西"), ("他为什么想下午回来？", "天气热|下午会下雨|想看个电影"))],
 w1=["你用（ěr）机听音乐吧，我要学习了。", "（rú）果您想换本书，就告诉我，我帮您拿。", "你再检（chá）一下，护照和机票都带好了吗？"],
 w2=[("电梯", "电梯里的人太多了，我们等下一趟吧。"), ("安静", "咖啡馆里很安静，他一边喝咖啡一边工作。"), ("检查", "医生正在给他检查眼睛。")],
 gl={"11": "Sắp nghỉ rồi, bạn định làm gì? → B: Mẹ nói sẽ đưa mình đi biển.",
     "12": "Tuyết rơi rồi, đi đường nhất định phải cẩn thận. → A: Vâng, con sẽ lái chậm.",
     "13": "Xin lỗi, cho hỏi ga tàu điện ngầm đi thế nào? → F: Từ đây đi thẳng, đến ngã tư đầu tiên rẽ phải là tới.",
     "14": "Bạn cứ nhìn đồng hồ mãi, có việc gấp à? → D: Bố bảo mình phải về nhà trước chín giờ tối.",
     "15": "Còn 30 phút nữa phim bắt đầu, chúng ta có muộn không? → C: Không đâu, từ đây đi bộ qua chỉ mất mười phút.",
     "16": "该检票了 – đến giờ soát vé rồi. → F 检票.",
     "17": "路上小心 – đi đường cẩn thận. → C 小心.",
     "18": "你可以选择这家宾馆 – bạn có thể chọn khách sạn này. → A 选择.",
     "19": "坐电梯上去 – đi thang máy lên. → D 电梯.",
     "20": "坐高铁 – đi tàu cao tốc, “vừa nhanh vừa thoải mái”. → B 高铁.",
     "21": "“住着很舒服” → B.",
     "22": "“就能看到咖啡馆了，我就在那儿等你” → B.",
     "23": "“如果天气好，咱们就去爬山” → A.",
     "24": "“这几天天气越来越热了，咱们早点儿去，下午就回来” → A 天气热."}),
)
