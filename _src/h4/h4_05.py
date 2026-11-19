# -*- coding: utf-8 -*-
# HSK 4上 – Bài 5: “不怕辣”和“怕不辣”
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[5] = dict(zh="“不怕辣”和“怕不辣”", vi="“Không sợ cay” và “sợ không cay”",
intro="Bạch Gia Nguyệt được vợ chồng Lưu Minh mời ăn cá nấu cay Tứ Xuyên, học sự khác nhau thú vị giữa “不怕辣” và “怕不辣”; cả nhóm đi ăn chung, chia tiền và tìm hiểu cách xếp chỗ ngồi trên bàn ăn của người Trung Quốc.",
vocab=V("""
至少|zhìshǎo|pho|ít nhất|这本书我至少看了三遍。~Cuốn sách này tôi đọc ít nhất ba lần rồi.
中餐|zhōngcān|dt|món ăn Trung Quốc, cơm Tàu|你喜欢吃中餐还是西餐？~Bạn thích ăn món Trung hay món Tây?
专门|zhuānmén|pho|chuyên, cố ý (dành riêng)|这是我专门为你买的。~Cái này tôi mua riêng cho bạn.
煮|zhǔ|dong|nấu, luộc|妈妈在煮饺子。~Mẹ đang luộc sủi cảo.
油|yóu|dt|dầu, mỡ|这个菜油太多了。~Món này nhiều dầu quá.
道|dào|lg|món (lượng từ cho món ăn); đạo, lượt|今天的这道菜特别好吃。~Món ăn hôm nay đặc biệt ngon.
熟|shú|tt|chín; quen|肉还没熟，再煮一会儿吧。~Thịt chưa chín, nấu thêm một lúc nữa.
倒|dào|dong|đổ, rót|请给我倒一杯水。~Làm ơn rót cho tôi một cốc nước.
辣椒|làjiāo|dt|ớt|我吃饭的时候喜欢放点儿辣椒。~Lúc ăn cơm tôi thích cho chút ớt.
辣|là|tt|cay|这个菜太辣了，我吃不了。~Món này cay quá, tôi không ăn được.
水煮鱼|Shuǐzhǔyú|rieng|cá nấu cay (món Tứ Xuyên)|水煮鱼是一道很有名的四川菜。~Cá nấu cay là một món Tứ Xuyên rất nổi tiếng.
敢|gǎn|dong|dám|他不敢一个人走夜路。~Anh ấy không dám đi đường đêm một mình.
肚子|dùzi|dt|bụng|我肚子有点儿疼。~Bụng tôi hơi đau.
相同|xiāngtóng|tt|giống nhau, tương đồng|我们俩的爱好相同。~Sở thích của hai chúng tôi giống nhau.
顺序|shùnxù|dt|thứ tự|请按顺序排队。~Vui lòng xếp hàng theo thứ tự.
够|gòu|pho|đủ; khá, rất (够……的)|今天够冷的，多穿点儿衣服。~Hôm nay lạnh thật đấy, mặc thêm áo vào.
不够|búgòu|dong|không đủ|钱不够，我们少买一点儿吧。~Không đủ tiền, chúng ta mua ít đi chút.
达到|dádào|dong|đạt tới, đạt được|他的中文已经达到了HSK四级水平。~Tiếng Trung của anh ấy đã đạt trình độ HSK 4.
聚|jù|dong|tụ tập, gặp gỡ|周末我们几个老同学聚了一下。~Cuối tuần mấy bạn học cũ chúng tôi tụ họp một chút.
午餐|wǔcān|dt|bữa trưa|我们一起吃午餐吧。~Chúng ta cùng ăn trưa nhé.
咸|xián|tt|mặn|汤有点儿咸，再加点儿水。~Canh hơi mặn, cho thêm chút nước.
凉|liáng|tt|nguội, mát, lạnh|菜都凉了，快吃吧。~Thức ăn nguội hết rồi, mau ăn đi.
酸|suān|tt|chua|这种水果有点儿酸。~Loại hoa quả này hơi chua.
汤|tāng|dt|canh, súp|我想喝一碗热汤。~Tôi muốn uống một bát canh nóng.
各|gè|dai|các, mỗi|各位同学，请安静一下。~Các bạn, xin yên lặng một chút.
付|fù|dong|trả (tiền)|这次我来付钱。~Lần này để tôi trả tiền.
聚餐|jùcān|dong|liên hoan, ăn uống chung|周五晚上我们班要聚餐。~Tối thứ Sáu lớp chúng tôi đi liên hoan.
辣子鸡|Làzǐjī|rieng|gà xào ớt khô|辣子鸡又香又辣。~Gà xào ớt vừa thơm vừa cay.
松鼠鳜鱼|Sōngshǔ Guìyú|rieng|cá quế hình con sóc (món Tô Châu)|松鼠鳜鱼是一道苏州名菜。~Cá quế hình con sóc là món nổi tiếng của Tô Châu.
红烧羊肉|Hóngshāo Yángròu|rieng|thịt dê kho tàu|冬天吃红烧羊肉很舒服。~Mùa đông ăn thịt dê kho rất dễ chịu.
贵州|Guìzhōu|rieng|Quý Châu (tỉnh)|贵州的风景很美。~Phong cảnh Quý Châu rất đẹp.
酸汤米线|Suāntāng Mǐxiàn|rieng|bún canh chua (Quý Châu)|这碗酸汤米线又酸又辣。~Bát bún canh chua này vừa chua vừa cay.
随意|suíyì|tt|tùy ý, thoải mái|大家随意坐吧。~Mọi người cứ ngồi tùy ý nhé.
正式|zhèngshì|tt|chính thức, trang trọng|明天的会议很正式，要穿西服。~Cuộc họp ngày mai rất trang trọng, phải mặc com-lê.
普通|pǔtōng|tt|bình thường, phổ thông|他只是一个普通的学生。~Cậu ấy chỉ là một học sinh bình thường.
重视|zhòngshì|dong|coi trọng|学校很重视学生的健康。~Nhà trường rất coi trọng sức khỏe học sinh.
座位|zuòwèi|dt|chỗ ngồi|请问，这个座位有人吗？~Xin hỏi, chỗ này có ai ngồi không?
安排|ānpái|dong|sắp xếp|明天的活动我已经安排好了。~Hoạt động ngày mai tôi đã sắp xếp xong.
按照|ànzhào|gioi|theo, dựa theo|请按照老师的要求做作业。~Hãy làm bài theo yêu cầu của thầy cô.
年龄|niánlíng|dt|tuổi tác|这个活动没有年龄要求。~Hoạt động này không yêu cầu về độ tuổi.
面对|miànduì|dong|đối diện, đối mặt|面对困难，我们不要怕。~Đối mặt với khó khăn, chúng ta đừng sợ.
主人|zhǔrén|dt|chủ nhà, người chủ|主人热情地欢迎客人。~Chủ nhà nhiệt tình đón khách.
等|děng|gioi|đợi đến, chờ đến khi|等你有空了，我们一起去看电影。~Đợi khi bạn rảnh, chúng ta cùng đi xem phim.
尊重|zūnzhòng|dong|tôn trọng|我们要尊重老人。~Chúng ta phải tôn trọng người già.
"""),
texts=[dict(t="课文1", scene="在刘明和王一雪家，夫妻两人请白家月和李文吃饭。", scene_vi="Ở nhà Lưu Minh và Vương Nhất Tuyết, hai vợ chồng mời Bạch Gia Nguyệt và Lý Văn ăn cơm.", narr=False, lines=T("""
刘明>家月，你来中国至少两个月了，习惯吃中餐了吗？|Gia Nguyệt, em đến Trung Quốc ít nhất hai tháng rồi, đã quen ăn món Trung chưa?
白家月>习惯了，而且我很喜欢吃中国菜。|Quen rồi ạ, hơn nữa em rất thích ăn món Trung Quốc.
王一雪>你还没吃过水煮鱼吧？这是我专门为你做的。|Em chưa ăn cá nấu cay bao giờ nhỉ? Món này chị làm riêng cho em đấy.
白家月>看起来不像水煮鱼，更像“油煮鱼”。|Trông không giống “cá nấu nước”, mà giống “cá nấu dầu” hơn.
王一雪>这道菜是先用水把鱼煮熟，最后再倒上辣椒油，其实只有最上面那一层是油。你尝尝，对你来说辣不辣？|Món này là luộc chín cá bằng nước trước, cuối cùng mới rưới dầu ớt lên, thật ra chỉ có lớp trên cùng là dầu. Em nếm thử xem, với em có cay không?
白家月>辣是辣，但是非常好吃！|Cay thì cay thật, nhưng ngon vô cùng!
王一雪>那你多吃点儿，不要客气。|Vậy em ăn nhiều vào, đừng khách sáo.
"""), q=Q("""
白家月来中国多久了？|至少两个月了。|Ít nhất hai tháng rồi.
白家月习惯吃中餐了吗？|习惯了，而且她很喜欢吃中国菜。|Quen rồi, hơn nữa cô rất thích ăn món Trung Quốc.
水煮鱼是怎么做的？|先用水把鱼煮熟，最后再倒上辣椒油。|Luộc chín cá bằng nước trước, cuối cùng rưới dầu ớt lên.
白家月觉得水煮鱼怎么样？|辣是辣，但是非常好吃。|Cay thì cay nhưng rất ngon.
""")),
 dict(t="课文2", scene="在刘明和王一雪家，夫妻两人和白家月、李文边吃边聊。", scene_vi="Ở nhà Lưu Minh và Vương Nhất Tuyết, hai vợ chồng vừa ăn vừa trò chuyện với Bạch Gia Nguyệt và Lý Văn.", narr=False, lines=T("""
王一雪>我听李文说，你现在也爱吃辣了？|Chị nghe Lý Văn nói, giờ em cũng thích ăn cay rồi à?
白家月>是的，来中国以后，我越来越喜欢吃辣了。|Vâng, từ khi đến Trung Quốc, em ngày càng thích ăn cay.
王一雪>我们以前不太敢吃辣，吃完可能会肚子不舒服，不过现在也慢慢适应了。|Trước đây bọn chị không dám ăn cay lắm, ăn xong có thể bị khó chịu bụng, nhưng giờ cũng dần quen rồi.
刘明>对，我们现在都不怕辣了。家月，你是“不怕辣”还是“怕不辣”？|Đúng, giờ bọn anh đều không sợ cay nữa. Gia Nguyệt, em là “không sợ cay” hay “sợ không cay”?
白家月>中文真有意思，相同的字，顺序一换，意思就变了。|Tiếng Trung thú vị thật, cùng những chữ ấy mà đổi thứ tự là nghĩa đã khác.
李文>你的中文水平够高的，这都听懂了！你说得对，“不怕辣”是说不怕吃辣的菜，“怕不辣”是担心菜还不够辣呢。|Trình độ tiếng Trung của cậu cao thật đấy, cái này mà cũng hiểu! Cậu nói đúng, “không sợ cay” là không sợ ăn món cay, còn “sợ không cay” là lo món ăn vẫn chưa đủ cay.
白家月>我还达不到“怕不辣”的水平，甚至也不能算“不怕辣”，只是喜欢吃辣。|Mình chưa đạt tới trình độ “sợ không cay”, thậm chí cũng chưa tính là “không sợ cay”, chỉ là thích ăn cay thôi.
"""), q=Q("""
王一雪一家以前敢不敢吃辣？为什么？|不太敢，因为吃完可能会肚子不舒服。|Không dám lắm, vì ăn xong có thể khó chịu bụng.
关于王一雪一家，可以知道什么？|现在能吃辣了。|Bây giờ đã ăn được cay.
“不怕辣”“怕不辣”都是什么意思？|“不怕辣”是不怕吃辣的菜，“怕不辣”是担心菜还不够辣。|“不怕辣” là không sợ ăn món cay, “怕不辣” là lo món ăn chưa đủ cay.
白家月现在的口味是什么？|只是喜欢吃辣，还不能算“不怕辣”。|Chỉ là thích ăn cay, chưa tính là “không sợ cay”.
""")),
 dict(t="课文3", scene="在餐厅里，白家月、陈天中、李文和安妮聚餐。", scene_vi="Tại nhà hàng, Bạch Gia Nguyệt, Trần Thiên Trung, Lý Văn và Annie ăn trưa cùng nhau.", narr=True, lines=T("""
周末，白家月、陈天中、李文和安妮聚在一起吃午餐。|Cuối tuần, Bạch Gia Nguyệt, Trần Thiên Trung, Lý Văn và Annie tụ họp ăn trưa cùng nhau.
白家月想吃辣的，要了辣子鸡；陈天中爱吃甜的，想尝尝松鼠鳜鱼；|Bạch Gia Nguyệt muốn ăn cay nên gọi gà xào ớt; Trần Thiên Trung thích ăn ngọt, muốn nếm thử cá quế hình con sóc;
李文更喜欢吃咸的，选了红烧羊肉和一道凉菜；安妮听说贵州酸汤很有名，点了酸汤米线。|Lý Văn thích ăn mặn hơn, chọn thịt dê kho và một món nguội; Annie nghe nói canh chua Quý Châu rất nổi tiếng nên gọi bún canh chua.
他们边吃边聊，非常愉快。|Họ vừa ăn vừa trò chuyện, rất vui vẻ.
结账时，李文想请客，但大家觉得还是各付各的更合适。|Lúc thanh toán, Lý Văn muốn mời, nhưng mọi người thấy ai trả phần nấy thì hợp lý hơn.
于是，李文付完钱后，大家把钱转给了他，还笑着说下次再一起聚餐。|Thế là Lý Văn trả tiền xong, mọi người chuyển khoản lại cho cậu, còn cười nói lần sau lại cùng đi ăn.
"""), q=Q("""
陈天中点了什么菜？|松鼠鳜鱼。|Cá quế hình con sóc.
李文喜欢吃什么口味的菜？|咸的。|Món mặn.
白家月点了什么菜？为什么？|辣子鸡，因为她想吃辣的。|Gà xào ớt, vì cô muốn ăn cay.
他们是怎么结账的？|李文先付钱，然后大家把钱转给他，各付各的。|Lý Văn trả trước, rồi mọi người chuyển tiền lại cho cậu, ai trả phần nấy.
""")),
 dict(t="课文4", scene="中国餐桌上的座位安排", scene_vi="Cách xếp chỗ ngồi trên bàn ăn Trung Quốc", narr=True, lines=T("""
今天吃饭的时候，大家坐得比较随意。|Hôm nay lúc ăn cơm, mọi người ngồi khá tùy ý.
李文告诉白家月，在中国，正式聚餐和普通聚餐不同，正式聚餐时人们比较重视座位的安排，|Lý Văn nói với Bạch Gia Nguyệt rằng ở Trung Quốc, bữa tiệc trang trọng khác với bữa ăn bình thường, khi ăn tiệc trang trọng người ta khá coi trọng việc sắp xếp chỗ ngồi,
比如可以按照年龄大小来安排，年龄比较大的客人往往会坐在中间或者面对门口的座位。|ví dụ có thể sắp xếp theo tuổi tác, khách lớn tuổi thường sẽ ngồi ở giữa hoặc ở chỗ ngồi đối diện cửa ra vào.
大家坐下时，主人会请客人先坐。|Khi mọi người ngồi xuống, chủ nhà sẽ mời khách ngồi trước.
如果聚餐时有老人，年轻人要等老人坐下后再坐。|Nếu bữa ăn có người già, người trẻ phải đợi người già ngồi xuống rồi mới ngồi.
白家月听后觉得很有意思，她认为这么做是照顾客人、尊重老人的表现。|Bạch Gia Nguyệt nghe xong thấy rất thú vị, cô cho rằng làm như vậy là biểu hiện của việc chăm sóc khách và tôn trọng người già.
"""), q=Q("""
一般来说，什么人会坐面对门口的座位？|年龄大的客人。|Khách lớn tuổi.
正式聚餐时，可以怎么安排座位？|可以按照年龄大小来安排。|Có thể sắp xếp theo tuổi tác.
一般来说，正式聚餐时，谁先坐下？|老人（客人）先坐。|Người già (khách) ngồi trước.
白家月怎么看这种座位安排方式？|她认为这是照顾客人、尊重老人的表现。|Cô cho rằng đó là biểu hiện của việc chăm sóc khách và tôn trọng người già.
""")),
],
grammar=[
 G("zhishao", "范围副词“至少”", "Phó từ phạm vi “至少”",
   "“至少” (ít nhất) biểu thị thời gian, số lượng, mức độ… không thấp hơn một giới hạn tối thiểu nào đó.",
   [F("S:Chủ ngữ|kw:至少|V:Số lượng / mức độ", [
     ("家月，你来中国|[至少]|两个月了，习惯吃中餐了吗", "？", "Gia Nguyệt, em đến Trung Quốc ít nhất hai tháng rồi, đã quen ăn món Trung chưa?"),
     ("每年|[至少]|有两百名留学生来我校学习中文专业", "。", "Mỗi năm có ít nhất hai trăm du học sinh đến trường tôi học chuyên ngành tiếng Trung."),
     ("我们虽然没有见过面，但|[至少]|在网上聊过很多次，也算比较熟悉了", "。", "Tuy chúng tôi chưa gặp mặt, nhưng ít nhất đã trò chuyện trên mạng nhiều lần, cũng coi như khá quen.")])]),
 G("gou", "副词/动词“够”", "Phó từ / động từ “够”",
   "(1) Phó từ: biểu thị mức độ cao, hay dùng trong cấu trúc “够……的” (… thật đấy, khá là…). (2) Động từ: về số lượng đáp ứng được nhu cầu, hoặc đạt tới một tiêu chuẩn / mức độ nào đó (đủ).",
   [F("S:Chủ ngữ|kw:够|A:Tính từ|kw2:的", [
     ("你的中文水平|[够]|高|[的]", "，这都听懂了！", "Trình độ tiếng Trung của cậu cao thật đấy, cái này mà cũng hiểu!"),
     ("今天|[够]|冷|[的]", "，多穿点儿衣服。", "Hôm nay lạnh thật đấy, mặc thêm áo vào.")], cap="够……的: mức độ cao"),
    F("S:Chủ ngữ|kw:够 / 不够|X:(Bổ sung)", [
     ("明天请家月和李文来家里吃饭，四个菜|[够不够]|", "？", "Mai mời Gia Nguyệt và Lý Văn đến nhà ăn cơm, bốn món có đủ không?"),
     ("我尝了一下，还|[不够]|甜，再加一点儿糖吧", "。", "Tôi nếm thử rồi, vẫn chưa đủ ngọt, thêm chút đường nữa nhé.")], cap="够 làm động từ: đủ")]),
 G("gegede", "固定格式“各×各的”", "Cấu trúc cố định “各 × 各的”",
   "Biểu thị mỗi người độc lập làm cùng một loại hành động, không ảnh hưởng nhau: “ai… nấy”, “mỗi người… phần của mình”.",
   [F("S:Chủ ngữ|kw:各|V:Động từ|kw2:各的|O:(Tân ngữ)", [
     ("大家觉得还是|[各]|付|[各的]|更合适", "。", "Mọi người thấy ai trả phần nấy thì hợp lý hơn."),
     ("到了办公室，大家就开始|[各]|忙|[各的]|", "了。", "Đến văn phòng, mọi người bắt đầu ai bận việc nấy."),
     ("在图书馆里，大家都很安静，|[各]|看|[各的]|书", "。", "Trong thư viện, mọi người đều rất yên lặng, ai đọc sách nấy.")])]),
 G("deng", "介词“等”", "Giới từ “等”",
   "Trong bài này “等” là giới từ, nghĩa là “đợi đến (khi)”, dùng để dẫn ra thời gian hoặc điều kiện; vế sau thường có “再、就、已经…”.",
   [F("S:(Phần trước)|kw:等|X:Thời điểm / điều kiện|V:Hành động sau đó", [
     ("如果聚餐时有老人，年轻人要|[等]|老人坐下后|再坐", "。", "Nếu bữa ăn có người già, người trẻ phải đợi người già ngồi xuống rồi mới ngồi."),
     ("|[等]|我写完作业|再跟你出去玩", "。", "Đợi mình làm xong bài tập rồi đi chơi với bạn."),
     ("|[等]|我们到火车站的时候|火车已经开走了", "。", "Đến khi chúng tôi tới ga thì tàu đã chạy mất rồi.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["熟", "敢", "油", "专门", "肚子"], [
   "家里没【油】了，你去超市买一瓶吧。", "这道菜看起来太辣了，我不【敢】吃。", "我【肚子】有点儿不舒服，想休息一下。",
   "已经煮了十多分钟了，饺子【熟】了吧？", "这是我【专门】为你准备的礼物，希望你喜欢。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["凉", "咸", "付", "重视", "座位"], [
   "A：请问，这个【座位】有人吗？ B：没有人，您坐吧。", "A：你尝尝，这道菜是不是做得太【咸】了？ B：嗯，是的，我跟服务员说一下。",
   "A：你们怎么还不吃？一会儿菜都【凉】了。 B：我们在等你呢，一起吃更热闹。", "A：我发现早上出来跑步的人变多了。 B：是啊，因为人们越来越【重视】身体健康了。",
   "A：这是我去超市帮你带的东西。 B：谢谢！多少钱？我把钱【付】给你。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["不够再加", "刘明和两个孩子也各点了一道菜", "大家聚在一起", "感谢他们这段时间对自己的照顾"], [
   "周末，白家月请大家一起吃饭，【感谢他们这段时间对自己的照顾】。点菜时，白家月让大家想吃什么就点什么，并说自己很喜欢这家饭店的菜，味道特别好。王一雪建议每个人先点一个自己喜欢的菜，【不够再加】。王一雪要了一个汤，李文选了一道凉菜，【刘明和两个孩子也各点了一道菜】，白家月最后点了一道肉菜。【大家聚在一起】，边吃边聊，非常开心。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：老师，我刚入学，不知道应该选几门课。 B：研究生一年级的时候，______。（至少）", "研究生一年级的时候，至少要选五门课。"),
   ("A：完成这个工作需要三天，现在只有两天，时间______。（不够）", "时间不够。"),
   ("他们虽然住在一起，但是口味不同，______。（各×各的）", "他们虽然住在一起，但是口味不同，各做各的饭。"),
   ("别着急，______就去找你。（等）", "别着急，等我下了课就去找你。")]),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l5", items=[
   ("午餐", "中午我们点了一大桌菜当午餐。"), ("辣", "这道菜上面有很多辣椒，看起来很辣。"), ("汤", "这锅汤看起来又白又香。")]),
])
