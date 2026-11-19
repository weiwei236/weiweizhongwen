# -*- coding: utf-8 -*-
# HSK 4上 – Bài 10: 南方不懂北方的冷
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[10] = dict(zh="南方不懂北方的冷", vi="Miền Nam không hiểu cái lạnh miền Bắc",
intro="Lưu Minh kể chuyện chàng trai Quảng Châu đi công tác Cáp Nhĩ Tân bị lạnh cóng; các bạn bàn kế hoạch nghỉ đông, so sánh khí hậu và phương ngữ giữa Quảng Châu và Cáp Nhĩ Tân; cuối bài là thư kêu gọi “sống xanh” nhân Ngày Môi trường Thế giới.",
vocab=V("""
小伙子|xiǎohuǒzi|dt|chàng trai, thanh niên|这个小伙子很能干。~Chàng trai này rất giỏi giang.
气温|qìwēn|dt|nhiệt độ không khí|今天的气温比昨天高。~Nhiệt độ hôm nay cao hơn hôm qua.
零下|líng xià|cum|dưới 0 độ, âm|哈尔滨冬天常常零下二十度。~Mùa đông Cáp Nhĩ Tân thường âm hai mươi độ.
度|dù|lg|độ|今天最高气温三十度。~Hôm nay nhiệt độ cao nhất ba mươi độ.
冻|dòng|dong|lạnh cóng, đông cứng|外面太冷了，我的手都冻红了。~Bên ngoài lạnh quá, tay tôi lạnh đến đỏ cả lên.
后悔|hòuhuǐ|dong|hối hận|我很后悔没早点儿学中文。~Tôi rất hối hận vì không học tiếng Trung sớm hơn.
就是|jiùshì|pho|đúng thế, chính là (tỏ ý đồng ý)|就是，我也这么想。~Đúng thế, tôi cũng nghĩ vậy.
温度|wēndù|dt|nhiệt độ|房间里的温度有点儿高。~Nhiệt độ trong phòng hơi cao.
差别|chābié|dt|sự khác biệt, chênh lệch|两个城市的差别很大。~Sự khác biệt giữa hai thành phố rất lớn.
厚|hòu|tt|dày|冬天要穿厚衣服。~Mùa đông phải mặc quần áo dày.
广州|Guǎngzhōu|rieng|Quảng Châu|广州冬天也不太冷。~Mùa đông Quảng Châu cũng không lạnh lắm.
哈尔滨|Hā'ěrbīn|rieng|Cáp Nhĩ Tân|哈尔滨的冰雪节很有名。~Lễ hội băng tuyết Cáp Nhĩ Tân rất nổi tiếng.
寒假|hánjià|dt|kỳ nghỉ đông|寒假你打算去哪儿？~Kỳ nghỉ đông bạn định đi đâu?
暖和|nuǎnhuo|tt|ấm áp|今天天气很暖和。~Hôm nay trời rất ấm áp.
低于|dīyú|dong|thấp hơn|今天的气温低于零度。~Nhiệt độ hôm nay thấp hơn 0 độ.
摄氏度|shèshìdù|lg|độ C (độ bách phân)|明天最低气温五摄氏度。~Ngày mai nhiệt độ thấp nhất 5 độ C.
受不了|shòubuliǎo|dong|không chịu nổi|这么热的天气我真受不了。~Thời tiết nóng thế này tôi thật không chịu nổi.
举办|jǔbàn|dong|tổ chức|学校下周举办运动会。~Tuần sau trường tổ chức đại hội thể thao.
各种|gèzhǒng|dai|các loại, đủ loại|超市里有各种水果。~Trong siêu thị có đủ loại hoa quả.
植物|zhíwù|dt|thực vật, cây cối|这个公园里有很多植物。~Công viên này có rất nhiều loài thực vật.
公里|gōnglǐ|lg|ki-lô-mét|我家离学校三公里。~Nhà tôi cách trường ba ki-lô-mét.
气候|qìhòu|dt|khí hậu|这里的气候很舒服。~Khí hậu ở đây rất dễ chịu.
而|ér|lien|mà, còn, nhưng|他喜欢运动，而我喜欢看书。~Anh ấy thích thể thao, còn tôi thích đọc sách.
此外|cǐwài|lien|ngoài ra|此外，你还要注意休息。~Ngoài ra, bạn còn phải chú ý nghỉ ngơi.
方言|fāngyán|dt|phương ngữ, tiếng địa phương|我听不懂这里的方言。~Tôi nghe không hiểu tiếng địa phương ở đây.
普通话|pǔtōnghuà|dt|tiếng phổ thông|她的普通话说得很标准。~Cô ấy nói tiếng phổ thông rất chuẩn.
较|jiào|pho|tương đối, khá|今天的温度较高。~Nhiệt độ hôm nay khá cao.
使用|shǐyòng|dong|sử dụng|这台电脑使用起来很方便。~Chiếc máy tính này dùng rất tiện.
引起|yǐnqǐ|dong|gây ra, dẫn đến|这件事引起了大家的注意。~Việc này đã thu hút sự chú ý của mọi người.
误会|wùhuì|dt|hiểu lầm|别生气，这是一个误会。~Đừng giận, đây là một sự hiểu lầm.
亲爱|qīn'ài|tt|thân yêu, thân mến|亲爱的朋友们，欢迎你们！~Các bạn thân mến, chào mừng các bạn!
再次|zàicì|pho|lần nữa, một lần nữa|再次感谢大家的帮助！~Một lần nữa cảm ơn sự giúp đỡ của mọi người!
开展|kāizhǎn|dong|triển khai, tổ chức (hoạt động)|学校开展了很多课外活动。~Trường đã tổ chức nhiều hoạt động ngoại khóa.
绿色|lǜsè|tt|xanh, thân thiện môi trường|我们要过绿色生活。~Chúng ta phải sống xanh.
环保|huánbǎo|dt|bảo vệ môi trường|环保是每个人的责任。~Bảo vệ môi trường là trách nhiệm của mỗi người.
拒绝|jùjué|dong|từ chối|他拒绝了我的邀请。~Anh ấy đã từ chối lời mời của tôi.
浪费|làngfèi|dong|lãng phí|不要浪费时间。~Đừng lãng phí thời gian.
节约|jiéyuē|dong|tiết kiệm|我们要节约用水。~Chúng ta phải tiết kiệm nước.
资源|zīyuán|dt|tài nguyên|水是很重要的资源。~Nước là nguồn tài nguyên rất quan trọng.
光|guāng|tt|hết sạch, không còn gì|饭菜都吃光了。~Cơm canh đã ăn sạch rồi.
垃圾|lājī|dt|rác|请把垃圾扔进垃圾桶。~Hãy bỏ rác vào thùng rác.
分类|fēnlèi|dong|phân loại|我们小区开始垃圾分类了。~Khu dân cư chúng tôi đã bắt đầu phân loại rác.
日常|rìcháng|tt|hằng ngày, thường ngày|运动是我日常生活的一部分。~Vận động là một phần trong cuộc sống hằng ngày của tôi.
"""),
texts=[dict(t="课文1", scene="在家里，刘明和王一雪说他在网上看到的一条信息。", scene_vi="Ở nhà, Lưu Minh kể cho Vương Nhất Tuyết nghe một tin anh đọc được trên mạng.", narr=False, lines=T("""
刘明>你看，这个小伙子从广州去哈尔滨出差，没想到哈尔滨的气温降到了零下二十几度，把他冻坏了。|Em xem, chàng trai này từ Quảng Châu đi công tác Cáp Nhĩ Tân, không ngờ nhiệt độ Cáp Nhĩ Tân xuống tới âm hơn hai mươi độ, khiến cậu ấy lạnh cóng.
王一雪>他一定后悔自己穿少了吧？|Chắc cậu ấy hối hận vì mặc ít quá nhỉ?
刘明>是啊，这就叫南方不懂北方的冷。|Đúng thế, cái này gọi là miền Nam không hiểu cái lạnh của miền Bắc.
王一雪>就是呢，冬天北方和南方的温度差别还是很大的。|Đúng vậy, mùa đông nhiệt độ miền Bắc và miền Nam chênh lệch vẫn rất lớn.
刘明>所以冬天来北方，尤其是东北，一定要提前查好目的地的天气，看看下不下雪，气温怎么样。|Vì vậy mùa đông đến miền Bắc, nhất là vùng Đông Bắc, nhất định phải xem trước thời tiết nơi đến, xem có tuyết không, nhiệt độ thế nào.
王一雪>对。更重要的是，说什么也得穿上厚一点儿的衣服。|Đúng. Quan trọng hơn là dù thế nào cũng phải mặc quần áo dày một chút.
"""), q=Q("""
小伙子去哈尔滨出差，那里的气温降到了多少度？|零下二十几度。|Âm hơn hai mươi độ.
小伙子为什么后悔自己穿少了？|因为哈尔滨太冷了，把他冻坏了。|Vì Cáp Nhĩ Tân quá lạnh, khiến cậu lạnh cóng.
“南方不懂北方的冷”是什么意思？|南方人不知道北方的冬天有多冷。|Người miền Nam không biết mùa đông miền Bắc lạnh thế nào.
南方人冬天来北方，刘明和王一雪有什么建议？|提前查好目的地的天气，一定要穿上厚一点儿的衣服。|Xem trước thời tiết nơi đến, nhất định phải mặc quần áo dày.
""")),
 dict(t="课文2", scene="在校园里，王一飞下课后遇到陈天中和白家月。", scene_vi="Trong khuôn viên trường, tan học Vương Nhất Phi gặp Trần Thiên Trung và Bạch Gia Nguyệt.", narr=False, lines=T("""
王一飞>寒假你们打算做什么呢？|Kỳ nghỉ đông các em định làm gì?
陈天中>我们刚刚还说呢，家月春节时要去广州，我计划去哈尔滨。|Bọn em vừa nói chuyện này xong, Tết Gia Nguyệt muốn đi Quảng Châu, còn em định đi Cáp Nhĩ Tân.
王一飞>那时候广州暖和，但哈尔滨特别冷，气温一般都低于零下十摄氏度甚至零下二十摄氏度，这么低的温度你受不了吧？|Lúc đó Quảng Châu ấm áp, nhưng Cáp Nhĩ Tân đặc biệt lạnh, nhiệt độ thường thấp hơn âm 10 độ C, thậm chí âm 20 độ C, nhiệt độ thấp như vậy em chịu không nổi đâu nhỉ?
陈天中>没问题，受得了，我有的是厚衣服。我去哈尔滨主要是想看雪，听说春节时那里会举办很多活动。|Không sao, chịu được ạ, em có rất nhiều áo dày. Em đi Cáp Nhĩ Tân chủ yếu là muốn ngắm tuyết, nghe nói dịp Tết ở đó tổ chức nhiều hoạt động lắm.
白家月>我想在广州过年，那里冬天比较暖和。而且我喜欢看花，听说广州的鲜花市场很有名，里面有各种植物。|Em muốn ăn Tết ở Quảng Châu, mùa đông ở đó khá ấm. Hơn nữa em thích ngắm hoa, nghe nói chợ hoa Quảng Châu rất nổi tiếng, trong đó có đủ loại cây cối.
王一飞>真不错！听你们这么一说，我也想外出旅游了。|Hay quá! Nghe các em nói vậy, chị cũng muốn đi du lịch rồi.
"""), q=Q("""
白家月春节时打算做什么？|去广州看花，在广州过年。|Đi Quảng Châu ngắm hoa, ăn Tết ở Quảng Châu.
陈天中春节时去哈尔滨，王一飞担心他什么？|受不了那里的气温。|Không chịu nổi nhiệt độ ở đó.
春节时，陈天中为什么要去哈尔滨？|主要是想看雪，听说那里会举办很多活动。|Chủ yếu muốn ngắm tuyết, nghe nói ở đó có nhiều hoạt động.
听完陈天中和白家月的计划，王一飞有什么想法？|她也想外出旅游了。|Cô cũng muốn đi du lịch.
""")),
 dict(t="课文3", scene="广州与哈尔滨的不同", scene_vi="Sự khác nhau giữa Quảng Châu và Cáp Nhĩ Tân", narr=True, lines=T("""
广州和哈尔滨，一个在南方，一个在北方，两个城市之间的距离有三千多公里，气候也大不相同。|Quảng Châu và Cáp Nhĩ Tân, một ở miền Nam, một ở miền Bắc, khoảng cách giữa hai thành phố hơn ba nghìn ki-lô-mét, khí hậu cũng rất khác nhau.
广州基本上没有冬天，而哈尔滨的冬天一般会从十月开始，到第二年的三四月才结束。|Quảng Châu về cơ bản không có mùa đông, còn mùa đông Cáp Nhĩ Tân thường bắt đầu từ tháng Mười, đến tháng Ba, tháng Tư năm sau mới kết thúc.
广州四季开满鲜花，所以又叫“花城”；哈尔滨冬天冰雪多，所以也叫“冰城”。|Quảng Châu bốn mùa nở đầy hoa nên còn gọi là “Thành phố hoa”; Cáp Nhĩ Tân mùa đông nhiều băng tuyết nên cũng gọi là “Thành phố băng”.
此外，两地的方言也不一样。|Ngoài ra, phương ngữ hai nơi cũng khác nhau.
哈尔滨方言和普通话听起来比较像，而广州方言和普通话差别较大。|Tiếng địa phương Cáp Nhĩ Tân nghe khá giống tiếng phổ thông, còn tiếng Quảng Châu khác tiếng phổ thông khá nhiều.
如果广州人和哈尔滨人都只使用自己的方言，那么交流就很困难，甚至还可能引起误会。|Nếu người Quảng Châu và người Cáp Nhĩ Tân đều chỉ dùng phương ngữ của mình thì giao tiếp sẽ rất khó khăn, thậm chí có thể gây hiểu lầm.
其实，中国很多地方都有自己的方言，所以，为了顺利交流，中国人从小都要学习普通话。|Thật ra, nhiều nơi ở Trung Quốc đều có phương ngữ riêng, vì vậy để giao tiếp thuận lợi, người Trung Quốc từ nhỏ đều phải học tiếng phổ thông.
"""), q=Q("""
广州和哈尔滨之间有多远？|三千多公里。|Hơn ba nghìn ki-lô-mét.
广州和哈尔滨都有哪些不同？|气候大不相同，方言也不一样。|Khí hậu rất khác nhau, phương ngữ cũng khác nhau.
为什么广州叫“花城”，哈尔滨叫“冰城”？|广州四季开满鲜花；哈尔滨冬天冰雪多。|Quảng Châu bốn mùa nở đầy hoa; Cáp Nhĩ Tân mùa đông nhiều băng tuyết.
中国人为什么从小都要学习普通话？|为了顺利交流。|Để giao tiếp thuận lợi.
""")),
 dict(t="课文4", scene="“世界环境日”那天，刘小雪学校学生会发布了一份活动发起书。", scene_vi="Vào Ngày Môi trường Thế giới, Hội học sinh trường Lưu Tiểu Tuyết đăng một thư kêu gọi hoạt động.", narr=True, lines=T("""
亲爱的同学们：今年的“世界环境日”，我们再次开展“绿色生活”活动，希望同学们做到：|Các bạn học sinh thân mến: Ngày Môi trường Thế giới năm nay, chúng ta một lần nữa tổ chức hoạt động “Sống xanh”, mong các bạn thực hiện được:
一、绿色出行。绿色一小步，环保一大步。根据距离选择绿色交通方式。|Một, đi lại xanh. Một bước nhỏ xanh, một bước lớn bảo vệ môi trường. Chọn phương tiện giao thông xanh tùy theo khoảng cách.
距离短时可以走路或者骑自行车，距离长时多乘坐公交车或者地铁。|Quãng ngắn có thể đi bộ hoặc đạp xe, quãng dài nên đi xe buýt hoặc tàu điện ngầm.
二、拒绝浪费。节约资源，坚持一水多用、人走灯关、餐餐都“光盘”。|Hai, nói không với lãng phí. Tiết kiệm tài nguyên, kiên trì dùng nước nhiều lần, ra khỏi phòng tắt đèn, bữa nào cũng ăn sạch đĩa.
三、垃圾分类。积极参加校园、小区环保活动，学习垃圾分类知识，从小事做起，做好垃圾分类。|Ba, phân loại rác. Tích cực tham gia hoạt động bảo vệ môi trường ở trường và khu dân cư, học kiến thức phân loại rác, bắt đầu từ việc nhỏ, phân loại rác cho tốt.
保护环境是每一个人的责任。同学们，让我们共同努力，让绿色生活成为我们的日常习惯！|Bảo vệ môi trường là trách nhiệm của mỗi người. Các bạn, hãy cùng nhau cố gắng, để sống xanh trở thành thói quen hằng ngày của chúng ta!
"""), q=Q("""
“世界环境日”时，校学生会再次开展了什么活动？|“绿色生活”活动。|Hoạt động “Sống xanh”.
怎样做到绿色出行？|根据距离选择绿色交通方式，距离短时走路或者骑自行车，距离长时多乘坐公交车或者地铁。|Chọn phương tiện xanh theo khoảng cách: quãng ngắn đi bộ hoặc đạp xe, quãng dài đi xe buýt hoặc tàu điện.
怎样节约资源？|坚持一水多用、人走灯关、餐餐都“光盘”。|Dùng nước nhiều lần, ra khỏi phòng tắt đèn, bữa nào cũng ăn sạch đĩa.
关于垃圾分类，应该做些什么？|积极参加环保活动，学习垃圾分类知识，从小事做起，做好垃圾分类。|Tích cực tham gia hoạt động môi trường, học kiến thức phân loại rác, bắt đầu từ việc nhỏ.
""")),
],
grammar=[
 G("shuoshenme", "固定格式“说什么/怎么（着）也得×”", "Cấu trúc cố định “说什么 / 怎么(着) 也得 ×”",
   "Biểu thị nhất định phải, bắt buộc phải làm (“dù thế nào cũng phải…”), thường dùng trong khẩu ngữ.",
   [F("S:(Chủ ngữ)|kw:说什么 / 怎么（着）|kw2:也得|V:Việc nhất định phải làm", [
     ("更重要的是，|[说什么]|[也得]|穿上厚一点儿的衣服", "。", "Quan trọng hơn là dù thế nào cũng phải mặc quần áo dày một chút."),
     ("假期还有两天就结束了，我明天|[说什么]|[也得]|把作业做完了", "。", "Kỳ nghỉ còn hai ngày là hết, ngày mai dù thế nào tôi cũng phải làm xong bài tập."),
     ("我很后悔上次没参加这个活动，这次|[怎么着]|[也得]|去", "。", "Tôi rất hối hận lần trước không tham gia hoạt động này, lần này dù thế nào cũng phải đi.")])]),
 G("youdeshi", "固定短语“有的是”", "Cụm từ cố định “有的是”",
   "“有的是” thường dùng trong khẩu ngữ, biểu thị có rất nhiều, nhấn mạnh số lượng nhiều: “có khối, có thừa”.",
   [F("S:Chủ ngữ|kw:有的是|O:Sự vật (rất nhiều)", [
     ("没问题，受得了，我|[有的是]|厚衣服", "。", "Không sao, chịu được, em có thừa áo dày."),
     ("过年时，家里|[有的是]|好吃的、好喝的", "，孩子们特别开心。", "Dịp Tết, trong nhà có khối đồ ăn ngon, đồ uống ngon, bọn trẻ rất vui."),
     ("这个市场特别大，|[有的是]|水果和菜", "，你想买什么菜都能买到。", "Chợ này rất rộng, rau và hoa quả có khối, bạn muốn mua gì cũng có.")])]),
 G("er", "连词“而”", "Liên từ “而”",
   "“而” nối động từ, tính từ, cụm từ hoặc mệnh đề, có nhiều nghĩa. Bài này học ba cách dùng: (1) chuyển ngoặt, nối các thành phần trái nghĩa (còn, nhưng); (2) nối tiếp ý nghĩa (và, mà); (3) quan hệ nhân quả trước sau (vì… mà…).",
   [F("X:Vế / thành phần 1|kw:而|V:Vế / thành phần 2", [
     ("广州基本上没有冬天|[而]|哈尔滨的冬天一般会从十月开始，到第二年的三四月才结束", "。", "Quảng Châu về cơ bản không có mùa đông, còn mùa đông Cáp Nhĩ Tân thường từ tháng Mười đến tháng Ba, tháng Tư năm sau mới kết thúc."),
     ("在这个紧张|[而]|兴奋的日子里，我们都走出教室，为运动员们加油", "。", "Trong những ngày căng thẳng mà phấn khởi này, chúng tôi đều ra khỏi lớp cổ vũ cho các vận động viên."),
     ("冬天，这个城市因为天气暖和|[而]|吸引了很多游客", "。", "Mùa đông, thành phố này vì thời tiết ấm áp mà thu hút rất nhiều du khách.")])]),
 G("zaici", "频率副词“再次”", "Phó từ tần suất “再次”",
   "“再次” đứng trước động từ, biểu thị lần thứ hai, thêm một lần nữa: “lại, một lần nữa”.",
   [F("S:Chủ ngữ|kw:再次|V:Động từ / cụm động từ", [
     ("今年的“世界环境日”，我们|[再次]|开展“绿色生活”活动", "。", "Ngày Môi trường Thế giới năm nay, chúng ta một lần nữa tổ chức hoạt động “Sống xanh”."),
     ("今年冬天，我计划|[再次]|去哈尔滨看雪", "。", "Mùa đông năm nay, tôi định lại đi Cáp Nhĩ Tân ngắm tuyết."),
     ("|[再次]|感谢您的支持与关心", "！", "Một lần nữa cảm ơn sự ủng hộ và quan tâm của ngài!")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["此外", "节约", "引起", "厚", "举办"], [
   "这个时候你还是不要乱说话，否则可能会【引起】更大的误会。", "为了保护环境，我们学校每年都【举办】垃圾分类活动。", "老师说我们一定要学好知识、打好基础，【此外】，还要多出去走走，了解市场情况。",
   "这本书太【厚】了，一个星期都看不完。", "每个人平时都应该注意【节约】用水，不要浪费。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["受不了", "环保", "普通话", "就是", "摄氏度"], [
   "A：老师今天怎么一直咳嗽？ B：【就是】啊，是不是感冒了？", "A：北京那天只有零下五【摄氏度】，你们还是去了长城？ B：是的，我们去爬了长城。虽然温度低，但风不大，不觉得冷。",
   "A：你怎么回来了？ B：那里太冷了，我实在【受不了】那儿的气候。", "A：不好意思，我【普通话】说得不太好。 B：没有啊，我觉得您说得挺好的。",
   "A：这些垃圾不能放在一起，不【环保】。 B：好的，我们马上就把它们分好类。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["温度能达到二十几度", "而南方的气候比较好", "一到冬天", "还可以去超市买新鲜的水果和菜等"], [
   "现在，【一到冬天】，越来越多生活在北方，特别是东北的老年人就会到南方生活一段时间。这是因为冬天的北方比较冷，【而南方的气候比较好】，很暖和，特别是云南、海南的一些城市，【温度能达到二十几度】，很适合老年人。除了气候，在南方城市的生活和北方没有很大差别，老人平时可以去家附近的公园活动活动，【还可以去超市买新鲜的水果和菜等】。冬天结束后，老人们才回到自己北方的家。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：你要出去跑步吗？ B：是的，我已经好几天没运动了，今天______。（说什么也得）", "今天说什么也得去跑一会儿。"),
   ("A：今天上午你能陪孩子出去玩吗？ B：没问题，我______。（有的是）", "没问题，我有的是时间。"),
   ("他______，客户对他非常满意。（表现 / 而）", "他工作认真而负责，表现很好，客户对他非常满意。"),
   ("欢迎您______。（再次）", "欢迎您再次来中国。")]),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l10", items=[
   ("暖和", "春天到了，天气越来越暖和，花都开了。"), ("浪费", "这么多饭菜都扔了，太浪费了。"), ("后悔", "他没好好复习，考得不好，现在很后悔。")]),
])
