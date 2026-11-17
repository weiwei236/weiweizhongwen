# -*- coding: utf-8 -*-
# HSK 3 – Bài 11: 看来我没办法解决这个问题
from gtb_gen import V, T, Q, F, G
B = {}

B[11] = dict(zh="看来我没办法解决这个问题", vi="Có vẻ như tôi không có cách nào giải quyết vấn đề này",
intro="Ở công ty, Vương Nhất Tuyết và Dương Đồng Lạc chuẩn bị cuộc họp: đổi giờ họp, kết nối máy tính không có tiếng, đồng nghiệp xin nghỉ… Còn Nhất Tuyết thì đang phân vân có nên lên Thượng Hải làm việc không.",
vocab=V("""
会议|huìyì|dt|cuộc họp, hội nghị|明天上午有一个重要的会议。~Sáng mai có một cuộc họp quan trọng.
经理|jīnglǐ|dt|giám đốc|经理现在不在办公室。~Giám đốc bây giờ không có ở văn phòng.
开会|kāihuì|dong|họp|我们下午三点开会。~Ba giờ chiều chúng ta họp.
后天|hòutiān|dt|ngày kia|后天是星期六。~Ngày kia là thứ Bảy.
地点|dìdiǎn|dt|địa điểm|会议的时间和地点都换了。~Thời gian và địa điểm họp đều đổi rồi.
室|shì|dt|phòng|会议室在三层。~Phòng họp ở tầng ba.
发|fā|dong|gửi|我把照片发给你了。~Mình gửi ảnh cho bạn rồi.
笔记本电脑|bǐjìběn diànnǎo|dt|máy tính xách tay|我的笔记本电脑很轻。~Máy tính xách tay của tôi rất nhẹ.
或者|huòzhě|lien|hoặc, hoặc là|你可以坐地铁或者打车去。~Bạn có thể đi tàu điện ngầm hoặc bắt taxi.
声音|shēngyīn|dt|âm thanh|电视的声音太大了。~Tiếng TV to quá.
看来|kànlái|dong|xem ra, dường như, có vẻ như|看来今天要下雨了。~Xem ra hôm nay sắp mưa rồi.
办法|bànfǎ|dt|biện pháp, cách|你有什么好办法吗？~Bạn có cách gì hay không?
解决|jiějué|dong|giải quyết|这个问题很难解决。~Vấn đề này rất khó giải quyết.
只能|zhǐ néng|cum|chỉ có thể|没有车了，我们只能走回去。~Hết xe rồi, chúng ta chỉ có thể đi bộ về.
别人|biérén|dai|người khác|别说别人不好。~Đừng nói xấu người khác.
请假|qǐngjià|dong|xin nghỉ, xin nghỉ phép|我明天想请一天假。~Mai tôi muốn xin nghỉ một ngày.
同事|tóngshì|dt|đồng nghiệp|我的同事都很热情。~Đồng nghiệp của tôi đều rất nhiệt tình.
休假|xiūjià|dong|nghỉ phép|经理下个星期休假。~Tuần sau giám đốc nghỉ phép.
怕|pà|dong|sợ|我怕晚上一个人走路。~Tôi sợ đi bộ một mình buổi tối.
邮箱|yóuxiāng|dt|hộp thư điện tử|请把你的邮箱告诉我。~Hãy cho tôi địa chỉ email của bạn.
愿意|yuànyì|nn|sẵn lòng, bằng lòng|我很愿意帮助你。~Tôi rất sẵn lòng giúp bạn.
城市|chéngshì|dt|thành phố|这是一个很漂亮的城市。~Đây là một thành phố rất đẹp.
离开|líkāi|dong|rời khỏi|他昨天离开了北京。~Hôm qua anh ấy rời Bắc Kinh.
机会|jīhuì|dt|cơ hội|这是一个很好的机会。~Đây là một cơ hội rất tốt.
生活|shēnghuó|dt|cuộc sống, sinh sống|我很喜欢这里的生活。~Tôi rất thích cuộc sống ở đây.
为|wèi|gioi|vì|妈妈为我准备了生日礼物。~Mẹ đã chuẩn bị quà sinh nhật cho tôi.
或|huò|lien|hoặc, hoặc là|周末我在家看书或看电影。~Cuối tuần tôi ở nhà đọc sách hoặc xem phim.
"""),
texts=[dict(t="课文1", scene="在办公室里，王一雪跟杨同乐在讨论工作。", scene_vi="Vương Nhất Tuyết và Dương Đồng Lạc đang thảo luận công việc trong văn phòng.", narr=False, lines=T("""
王一雪>会议下午几点开始？|Cuộc họp chiều mấy giờ bắt đầu?
杨同乐>今天下午经理不在，不开会了。|Chiều nay giám đốc không có mặt, không họp nữa.
王一雪>那什么时候开会？|Vậy khi nào họp?
杨同乐>后天上午十点，会议地点换到第一会议室。我正要给大家发邮件。|Mười giờ sáng ngày kia, địa điểm họp đổi sang phòng họp số một. Tôi đang định gửi email cho mọi người.
王一雪>开会的时候，我们用会议室的电脑还是自己的笔记本电脑？|Lúc họp, chúng ta dùng máy tính phòng họp hay máy tính xách tay của mình?
杨同乐>会议室的电脑或者自己的电脑都可以。|Máy tính phòng họp hoặc máy của mình đều được.
王一雪>那到时候咱们早点儿过去，你帮我把电脑接好吧。|Vậy đến lúc đó chúng ta qua sớm một chút, cậu giúp tôi kết nối máy tính nhé.
"""), q=Q("""
今天为什么不开会了？|因为今天下午经理不在。|Vì chiều nay giám đốc không có mặt.
会议换到了什么时间和地点？|后天上午十点，第一会议室。|10 giờ sáng ngày kia, phòng họp số một.
王一雪需要杨同乐帮忙做什么？|帮她把电脑接好。|Giúp cô ấy kết nối máy tính.
""")),
 dict(t="课文2", scene="在会议室，王一雪跟杨同乐在做会前准备。", scene_vi="Vương Nhất Tuyết và Dương Đồng Lạc đang chuẩn bị cho cuộc họp ở trong phòng họp.", narr=False, lines=T("""
王一雪>电脑接好了吗？|Máy tính kết nối xong chưa?
杨同乐>已经接好了，您开机看看有没有问题。|Kết nối xong rồi, chị mở máy xem có vấn đề gì không.
王一雪>现在什么都看不见。|Bây giờ chẳng thấy gì cả.
杨同乐>我检查一下哪里出问题了……您再试一下。|Để tôi kiểm tra xem lỗi ở đâu… Chị thử lại xem.
王一雪>看见了，但是听不见声音。|Thấy rồi, nhưng không nghe thấy tiếng.
杨同乐>现在呢？|Bây giờ thì sao?
王一雪>听得见声音，但是声音有点儿小，听不清楚。|Nghe thấy tiếng rồi, nhưng tiếng hơi nhỏ, nghe không rõ.
杨同乐>看来我没办法解决这个问题，只能找别人来帮帮忙了。|Xem ra tôi không có cách giải quyết vấn đề này, chỉ có thể nhờ người khác đến giúp thôi.
"""), q=Q("""
开机以后，电脑有什么问题？|什么都看不见。|Chẳng thấy gì cả.
杨同乐检查以后，电脑怎么样了？|看得见了，但是听不见声音。|Thấy được rồi nhưng không nghe tiếng.
听见声音以后，又出现了什么问题？|声音有点儿小，听不清楚。|Tiếng hơi nhỏ, nghe không rõ.
""")),
 dict(t="课文3", scene="在办公室里，王一雪跟杨同乐在聊天儿。", scene_vi="Vương Nhất Tuyết và Dương Đồng Lạc đang trò chuyện trong văn phòng.", narr=False, lines=T("""
王一雪>同乐，你看见老张了吗？|Đồng Lạc, cậu thấy anh Trương không?
杨同乐>老张没来。他说家里有点儿事，所以请假了。|Anh Trương không đến. Anh ấy nói nhà có chút việc nên xin nghỉ rồi.
王一雪>好几个同事都休假了，开会前这么多工作我怕干不完。|Mấy đồng nghiệp đều nghỉ phép, trước cuộc họp nhiều việc thế này tôi sợ làm không xong.
杨同乐>十二点多了，咱们先去吃饭吧。吃完饭，我跟您一起把这些工作做完。|Hơn mười hai giờ rồi, chúng ta đi ăn cơm trước đi. Ăn xong tôi cùng chị làm xong chỗ việc này.
王一雪>你先去吃，我想再干一会儿。明天开会前要发到公司的邮箱里。|Cậu đi ăn trước đi, tôi muốn làm thêm một lát. Trước cuộc họp ngày mai phải gửi vào hộp thư của công ty.
杨同乐>您没看到邮件吗？经理还没回来呢，下周才能开会。|Chị chưa xem email à? Giám đốc vẫn chưa về, tuần sau mới họp được.
王一雪>那不着急了。走，吃饭去。|Vậy thì không vội nữa. Đi, đi ăn thôi.
"""), q=Q("""
老张今天为什么没来上班？|他家里有点儿事，所以请假了。|Nhà anh ấy có chút việc nên xin nghỉ.
王一雪为什么没时间吃饭？|因为好几个同事都休假了，她怕工作干不完。|Vì nhiều đồng nghiệp nghỉ phép, chị sợ làm không xong việc.
明天公司开会吗？|不开，经理还没回来，下周才能开会。|Không, giám đốc chưa về, tuần sau mới họp.
""")),
 dict(t="课文4", scene="在家里，王一雪在写日记。", scene_vi="Vương Nhất Tuyết đang ngồi viết nhật ký ở trong nhà.", narr=True, lines=T("""
前几天，上海的同事来北京了。|Mấy hôm trước, đồng nghiệp ở Thượng Hải đến Bắc Kinh.
一起吃饭时，他们跟我说最近有不少同事去上海工作了，问我愿意不愿意也去上海。|Lúc ăn cơm cùng nhau, họ nói với tôi gần đây có khá nhiều đồng nghiệp lên Thượng Hải làm việc, hỏi tôi có muốn đi Thượng Hải không.
我是这样想的：现在丈夫和孩子都在北京，刘明的工作很忙，小雪和小明也还小，|Tôi nghĩ thế này: bây giờ chồng và con đều ở Bắc Kinh, công việc của Lưu Minh rất bận, Tiểu Tuyết và Tiểu Minh cũng còn nhỏ,
我去别的城市工作就要离开他们。|tôi đi thành phố khác làm việc thì phải xa họ.
虽然去上海可能会有更好的机会，但是对我来说，生活也很重要，我不愿意为工作或学习离开家人。|Tuy đi Thượng Hải có thể sẽ có cơ hội tốt hơn, nhưng với tôi, cuộc sống cũng rất quan trọng, tôi không muốn vì công việc hay học tập mà xa gia đình.
"""), q=Q("""
上海的同事告诉王一雪什么了？|最近有不少同事去上海工作了。|Gần đây nhiều đồng nghiệp lên Thượng Hải làm việc.
王一雪觉得去上海工作有什么好处？|可能会有更好的机会。|Có thể có cơ hội tốt hơn.
对王一雪来说，工作和生活哪个更重要？|生活也很重要，她不愿意为工作离开家人。|Cuộc sống cũng rất quan trọng, chị không muốn xa gia đình vì công việc.
"""))],
grammar=[
 G("haishihuozhe", "“还是”和“或者”", "“还是” và “或者”",
   "“还是” thường dùng trong câu hỏi, đưa ra hai hoặc nhiều phương án để người nghe lựa chọn. “或者” thường dùng trong câu trần thuật, không dùng trong câu hỏi.",
   [F("A:Phương án 1|kw:还是|B:Phương án 2 (câu hỏi)", [
     ("我们用会议室的电脑|[还是]|自己的笔记本电脑", "？", "Chúng ta dùng máy tính phòng họp hay máy tính xách tay của mình?"),
     ("我们今天去、明天去|[还是]|后天去", "？", "Chúng ta đi hôm nay, ngày mai hay ngày kia?")], cap="还是 – dùng trong câu hỏi"),
    F("A:Phương án 1|kw:或者|B:Phương án 2 (câu trần thuật)", [
     ("会议室的电脑|[或者]|自己的电脑都可以", "。", "Máy tính phòng họp hoặc máy của mình đều được."),
     ("你可以坐地铁|[或者]|打车去学校", "。", "Bạn có thể đi tàu điện ngầm hoặc bắt taxi đến trường.")], cap="或者 – dùng trong câu trần thuật")]),
 G("kanlai", "固定短语“看来”", "Cụm từ cố định “看来”",
   "Sau “看来” là một kết luận, thể hiện sự phân tích hoặc suy đoán của người nói về tình huống hiện tại dựa trên quan sát hoặc suy nghĩ (xem ra, có vẻ như).",
   [F("C:Tình huống (quan sát được)|kw:看来|X:Kết luận / suy đoán", [
     ("|[看来]|我没办法解决这个问题", "。", "Xem ra tôi không có cách giải quyết vấn đề này."),
     ("这么晚了，|[看来]|他今天不会来了", "。", "Muộn thế này rồi, xem ra hôm nay anh ấy không đến nữa."),
     ("电梯坏了，|[看来]|咱们只能走下去了", "。", "Thang máy hỏng rồi, xem ra chúng ta chỉ có thể đi bộ xuống."),
     ("外面天阴得很，|[看来]|要下雨了", "。", "Bên ngoài trời âm u lắm, có vẻ sắp mưa rồi.")])]),
 G("ba3", "“把”字句（3）", "Câu chữ “把” (3) – tạo ra kết quả",
   "Câu chữ “把” biểu thị hành động tác động lên một đối tượng xác định và tạo ra kết quả cụ thể. Cấu trúc: Chủ ngữ + 把 + tân ngữ + động từ + bổ ngữ kết quả.",
   [F("S:Chủ ngữ|kw:把|O:Tân ngữ|V:Động từ|X:Bổ ngữ kết quả", [
     ("我跟您一起|[把]|这些工作|做|完", "。", "Tôi cùng chị làm xong những việc này."),
     ("妈妈|[把]|衣服|洗|干净了", "。", "Mẹ giặt sạch quần áo rồi."),
     ("他还没|[把]|笔记本电脑|接|好呢", "。", "Anh ấy vẫn chưa kết nối xong máy tính xách tay."),
     ("你帮我|[把]|电脑|接|好吧", "。", "Cậu giúp tôi kết nối máy tính nhé.")])]),
 G("duilaishuo", "固定格式“对……来说”", "Cấu trúc cố định “对……来说”",
   "Cấu trúc “对……来说” dùng để chỉ rõ đối tượng liên quan trực tiếp đến một quan điểm, cảm nhận hoặc tình huống cụ thể (đối với…, với…).",
   [F("kw:对|S:Đối tượng|kw2:来说，|C:Quan điểm / tình huống", [
     ("[对]|我|[来说，]|生活也很重要", "。", "Với tôi, cuộc sống cũng rất quan trọng."),
     ("[对]|她|[来说，]|学习汉语很有意思", "。", "Với cô ấy, học tiếng Hán rất thú vị."),
     ("[对]|孩子|[来说，]|玩也是一种学习", "。", "Với trẻ con, chơi cũng là một cách học."),
     ("[对]|年轻人|[来说，]|找工作的时候机会最重要", "。", "Với người trẻ, lúc tìm việc thì cơ hội là quan trọng nhất.")])]),
],
test=dict(
 l2=["参加比赛|听音乐会|问别人事情", "他生病了|他今天结婚|他姐姐结婚", "换手机|买电脑|买手机"],
 l3=["还没结婚|非常想结婚|对自己不满意", "离开公司|参加会议|跟朋友喝茶", "睡前常看电影|每天很早睡觉|觉得上网挺累的", "要请假|要去医院|想去看电影"],
 r1=(["对我来说，开心最重要。", "我想我会把他们接到我这儿。", "啊，不好意思，那应该在哪儿开会？", "是的，生活很方便，环境也不错，我很满意。", "当然。我们先坐公交车，然后换地铁。", "901室或902室都行，现在里面都有我的同事。"],
     ["小王，你把会议地点写错了。", "看来你很喜欢这个小区。", "请问，我把笔记本送到哪儿？", "你找工作的时候，最关心什么？", "你会为家人离开这里，回到他们住的城市吗？"]),
 r2=(["城市", "邮箱", "机会", "办法", "鞋", "后天"],
     ["我今天得到了一个去上海工作的（　　），特别开心。", "我（　　）就休假了，这两天做不完这个工作，您还是让别人做吧。", "他们都收到公司发的邮件了，我的（　　）里怎么没有？", "A：你去过哪些（　　）？\nB：我才来中国三个星期，除了北京，哪儿都没去过。", "A：会议室的电脑坏了，你有什么（　　）吗？\nB：我去拿办公室的笔记本电脑吧，看看能不能接上。"]),
 r3=[("我最愿意教小学生，因为孩子的世界很简单，跟他们在一起，我觉得自己年轻了很多。", "他为什么喜欢教小孩子？", "他现在很年轻|教的东西很简单|孩子的世界很简单"),
     ("今天会议上经理说的那两个办法，虽然同事们都觉得第一个好，但我觉得第二个更好，因为它能更快地解决问题。", "关于第二个办法，可以知道什么？", "同事们觉得好|不能解决问题|能更快解决问题"),
     ("请大家安静一下，听我说。我们明天早上七点在宾馆门口见，一起坐汽车去高铁站。大家今晚就把行李准备好，明早离开前一定要再认真检查一下，别忘了自己的东西。我会为大家准备好早饭，明天六点带过来。大家可以在宾馆里吃，或者到了高铁站再吃，但是不能在汽车上吃。",
      ("大家应该什么时候把行李准备好？", "今天晚上|明早6:00|明早7:00"), ("大家不能在哪儿吃早饭？", "宾馆里|汽车上|高铁站里"))],
 w1=["你说话（shēng）音大一点儿好吗？我听不清楚。", "不好意思，我不太舒服，想请（jià）回去休息一下。", "张经理，我（pà）您不在市里，给您打个电话，问一下您在哪儿。"],
 w2=[("城市", "上海是一个非常漂亮的城市。"), ("声音", "手机的声音太小了，他们听不清楚。"), ("笔记本（电脑）", "会议室的桌子上放着一台笔记本电脑。")],
 gl={"11": "Tiểu Vương, cậu ghi sai địa điểm họp rồi. → C: Ôi, ngại quá, vậy phải họp ở đâu?",
     "12": "Xem ra bạn rất thích khu nhà này. → D: Đúng vậy, sống rất tiện, môi trường cũng tốt, mình rất hài lòng.",
     "13": "Xin hỏi, tôi mang máy tính xách tay đến đâu? → F: Phòng 901 hoặc 902 đều được, bây giờ trong đó đều có đồng nghiệp của tôi.",
     "14": "Lúc tìm việc, bạn quan tâm nhất điều gì? → A: Với mình, vui vẻ là quan trọng nhất.",
     "15": "Bạn có vì gia đình mà rời khỏi đây, về thành phố họ ở không? → B: Mình nghĩ mình sẽ đón họ đến chỗ mình.",
     "16": "一个去上海工作的机会 – một cơ hội đi Thượng Hải làm việc. → C 机会.",
     "17": "我后天就休假了 – ngày kia tôi nghỉ phép rồi. → F 后天.",
     "18": "我的邮箱里怎么没有 – sao trong hộp thư của tôi không có. → B 邮箱.",
     "19": "你去过哪些城市 – bạn đã đến những thành phố nào. → A 城市.",
     "20": "你有什么办法吗 – bạn có cách gì không. → D 办法.",
     "21": "“因为孩子的世界很简单” → C.",
     "22": "“因为它能更快地解决问题” → C.",
     "23": "“大家今晚就把行李准备好” → A 今天晚上.",
     "24": "“但是不能在汽车上吃” → B 汽车上."}),
)
