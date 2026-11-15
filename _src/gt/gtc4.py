# -*- coding: utf-8 -*-
# 发展汉语·初级综合(I) – Bài 27, 28
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[27] = dict(zh="我正在看电视呢", en="I'm Watching TV", vi="Tôi đang xem ti vi",
intro="Sáng sớm cuối tuần, công viên đã đông người: người chạy bộ, người tập thái cực quyền… Martin gọi cho A Minh mà A Minh đang mải xem bóng đá. Còn mẹ Linna gọi điện lúc Linna đang chuẩn bị đi ngủ.",
vocab=V("""
习惯|xíguàn|dt|thói quen|早睡早起是好习惯。~Ngủ sớm dậy sớm là thói quen tốt.
了解|liǎojiě|dong|tìm hiểu, hiểu rõ|我想了解中国文化。~Tôi muốn tìm hiểu văn hóa Trung Quốc.
点钟|diǎnzhōng|lg|giờ (đúng)|现在八点钟。~Bây giờ là tám giờ.
路上|lùshang|dt|trên đường|路上车很多。~Trên đường rất nhiều xe.
正在|zhèngzài|pho|đang|我正在做作业呢。~Tôi đang làm bài tập.
正|zhèng|pho|đang (đúng lúc)|我正要给你打电话。~Tôi đang định gọi cho bạn.
在|zài|pho|đang|他在睡觉呢。~Anh ấy đang ngủ.
一边|yìbiān|lien|vừa … vừa …|我一边吃饭一边看电视。~Tôi vừa ăn cơm vừa xem ti vi.
散步|sàn bù|cum|đi dạo|晚饭后我们去散散步吧。~Ăn tối xong chúng ta đi dạo nhé.
下边|xiàbian|dt|phía dưới|桌子下边有一只猫。~Dưới gầm bàn có một con mèo.
打(太极拳)|dǎ (tàijíquán)|dong|tập (thái cực quyền)|爷爷每天早上打太极拳。~Sáng nào ông cũng tập thái cực quyền.
湖|hú|dt|hồ|湖边有很多人在散步。~Bên hồ có nhiều người đang đi dạo.
椅子|yǐzi|dt|cái ghế|请坐在这把椅子上。~Mời ngồi ghế này.
接|jiē|dong|nghe (điện thoại); đón|你怎么不接电话？~Sao bạn không nghe điện thoại?
忙|máng|dong|bận (làm gì)|你最近忙什么呢？~Dạo này bạn bận gì thế?
听见|tīngjiàn|dong|nghe thấy|你听见了吗？有人叫你。~Bạn nghe thấy chưa? Có người gọi bạn.
草地|cǎodì|dt|bãi cỏ|孩子们在草地上玩儿。~Bọn trẻ chơi trên bãi cỏ.
刚|gāng|pho|vừa mới|我刚到家。~Tôi vừa về đến nhà.
午饭|wǔfàn|dt|cơm trưa|你吃午饭了吗？~Bạn ăn trưa chưa?
作业|zuòyè|dt|bài tập|今天的作业很多。~Bài tập hôm nay rất nhiều.
睡觉|shuì jiào|cum|ngủ|我每天十一点睡觉。~Mỗi ngày tôi ngủ lúc 11 giờ.
睡|shuì|dong|ngủ|你昨天睡得好吗？~Hôm qua bạn ngủ ngon không?
马上|mǎshàng|pho|ngay lập tức|你等一下，我马上来。~Bạn đợi một chút, tôi đến ngay.
旅行|lǚxíng|dong|du lịch|我们暑假去云南旅行。~Nghỉ hè chúng tôi đi Vân Nam du lịch.
愉快|yúkuài|tt|vui vẻ|祝你周末愉快！~Chúc bạn cuối tuần vui vẻ!
晚安|wǎn'ān|dong|chúc ngủ ngon|妈妈，晚安！~Mẹ ơi, chúc mẹ ngủ ngon!
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
很多中国人有早起的习惯，我很想了解一下他们早上都做些什么。|Nhiều người Trung Quốc có thói quen dậy sớm, tôi rất muốn tìm hiểu xem buổi sáng họ làm những gì.
今天是星期六，我五点半就起床了，我想到学校附近的公园里去看看。|Hôm nay thứ Bảy, 5 rưỡi tôi đã dậy, tôi muốn đến công viên gần trường xem thử.
我到公园的时候才六点钟，那里人已经很多了。|Lúc tôi đến công viên mới 6 giờ, ở đó đã rất đông người.
路上有的人正在跑步，有的人一边散步，一边听收音机；|Trên đường có người đang chạy bộ, có người vừa đi dạo vừa nghe đài;
大树下边有许多人在打太极拳，也有一些人在跳舞；|dưới gốc cây lớn có nhiều người đang tập thái cực quyền, cũng có người đang nhảy;
湖边还有人正坐在椅子上看书……|bên hồ còn có người đang ngồi trên ghế đọc sách…
"""), q=Q("""
很多中国人有什么习惯？|有早起的习惯。|Thói quen dậy sớm.
“我”到公园以后，看见人们都在做什么？|有的在跑步，有的一边散步一边听收音机，有的在打太极拳，有的在跳舞，有的在看书。|Chạy bộ, đi dạo nghe đài, thái cực quyền, nhảy, đọc sách.
""")),
 dict(t="课文二", narr=False, lines=T("""
马丁>阿明，我给你打了两个电话，你都没接，你在忙什么呢？|A Minh, mình gọi cho bạn hai cuộc mà bạn đều không nghe, bạn đang bận gì thế?
阿明>对不起，我没听见。我正在看电视呢。|Xin lỗi, mình không nghe thấy. Mình đang xem ti vi.
马丁>看什么呢？|Xem gì thế?
阿明>看足球比赛呢。你找我有什么事？|Xem đá bóng. Bạn tìm mình có việc gì?
马丁>明天早上六点，你跟我们一起练习太极拳，别忘了。|Sáng mai 6 giờ, bạn cùng tụi mình tập thái cực quyền, đừng quên nhé.
阿明>六点，太早了！|6 giờ, sớm quá!
马丁>不早，你要是去晚了，我们就练习完了。|Không sớm đâu, bạn mà đến muộn thì tụi mình tập xong rồi.
阿明>在哪儿？|Ở đâu?
马丁>草地旁边。|Cạnh bãi cỏ.
"""), q=Q("""
马丁给阿明打电话的时候，阿明在做什么？|正在看电视，看足球比赛。|Đang xem đá bóng trên ti vi.
马丁找阿明有什么事？|让他明天早上六点一起练习太极拳。|Rủ sáng mai 6 giờ tập thái cực quyền.
""")),
 dict(t="课文三", scene="晚上十点，林娜接到妈妈的电话。", scene_vi="10 giờ tối, Linna nhận được điện thoại của mẹ.", narr=False, lines=T("""
妈妈>林娜，我是妈妈。|Linna, mẹ đây.
林娜>妈妈，您好！您现在做什么呢？|Mẹ ơi, con chào mẹ! Mẹ đang làm gì thế?
妈妈>我刚吃完午饭，现在正和朋友一起买东西呢。你在做什么？|Mẹ vừa ăn trưa xong, đang đi mua sắm với bạn. Con đang làm gì?
林娜>我刚写完作业，正准备睡觉呢。|Con vừa làm xong bài tập, đang chuẩn bị đi ngủ.
妈妈>你们那儿几点了？|Chỗ con mấy giờ rồi?
林娜>我们这儿十点。|Chỗ con 10 giờ.
妈妈>怎么这么早就睡觉？|Sao ngủ sớm thế?
林娜>书上说“早睡早起身体好”，我以前总是习惯晚睡，现在我喜欢早睡了。|Sách nói “ngủ sớm dậy sớm thì khỏe”, trước con luôn quen ngủ muộn, giờ con thích ngủ sớm rồi.
妈妈>我想告诉你，我马上就要去旅行了，两个星期以后回来。|Mẹ muốn nói với con, mẹ sắp đi du lịch rồi, hai tuần sau mới về.
林娜>妈妈，祝您旅行愉快！|Mẹ ơi, chúc mẹ đi du lịch vui vẻ!
妈妈>谢谢！晚安！|Cảm ơn con! Chúc con ngủ ngon!
"""), q=Q("""
林娜妈妈打电话的时候，林娜在做什么？|她刚写完作业，正准备睡觉。|Vừa làm xong bài, chuẩn bị ngủ.
林娜为什么要早睡？|书上说“早睡早起身体好”。|Vì “ngủ sớm dậy sớm thì khỏe”.
林娜妈妈打电话有什么事？|告诉林娜她马上就要去旅行了。|Báo sắp đi du lịch.
"""))],
grammar=[
 G("yibian", "有的人一边散步，一边听收音机。", "一边……，一边……: vừa … vừa …",
   "Biểu thị hai động tác tiến hành cùng lúc.",
   [F("S:Chủ ngữ|kw:一边|A:Động tác 1|kw2:一边|B:Động tác 2", [("我经常|[一边]|喝茶，|[一边]|看电视", "。", "Tôi thường vừa uống trà vừa xem ti vi."), ("我喜欢|[一边]|做饭，|[一边]|听音乐", "。", "Tôi thích vừa nấu ăn vừa nghe nhạc."), ("我们|[一边]|吃饭，|[一边]|聊天儿", "。", "Chúng tôi vừa ăn cơm vừa nói chuyện.")])]),
 G("zhengzai", "我正在看电视呢。", "正在/在/正 + V + (呢): đang …",
   "“正在……(呢)”, “在……(呢)”, “正……(呢)”, “……呢” biểu thị động tác đang diễn ra; “……呢” hay dùng trong khẩu ngữ. Phủ định: 没(有) + V.",
   [F("S:Chủ ngữ|kw:正在/在/正|V:V + O|kw2:呢", [("许多人|[正在]|跑步|[(呢)]", "。", "Nhiều người đang chạy bộ."), ("一些人|[在]|打太极拳|[(呢)]", "。", "Một số người đang tập thái cực quyền."), ("我|[正]|准备睡觉|[(呢)]", "。", "Tôi đang chuẩn bị đi ngủ."), ("你||忙什么|[呢]", "？", "Bạn đang bận gì thế?")])],
   notes=["A：你在看电视吗？ B：我没看电视。– Tôi không xem ti vi."]),
 G("zher_nar", "你们那儿几点了？我们这儿十点。", "Đại từ/Danh từ + 这儿/那儿: chỉ nơi chốn",
   "“这儿”, “那儿” kết hợp với đại từ nhân xưng hoặc danh từ để chỉ nơi chốn.",
   [F("N:Người|kw:这儿/那儿|P:Phần sau", [("我们|[那儿]|不常下雪", "。", "Chỗ chúng tôi ít khi có tuyết."), ("我的自行车在朋友|[那儿]|", "。", "Xe đạp của tôi ở chỗ bạn."), ("你|[这儿]|真漂亮啊", "！", "Chỗ bạn đẹp thật!")])]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["习惯", "了解", "散步", "接", "听见", "刚", "作业", "马上", "愉快", "晚安"], [
   "我有早上跑步的【习惯】。", "我想多【了解】一下中国人的生活。", "晚饭以后，我们常去湖边【散步】。", "我给你打电话，你怎么不【接】？", "我叫你，你没【听见】吗？",
   "我【刚】下课，还没吃饭。", "老师，我的【作业】写完了。", "别着急，我【马上】就到。", "祝大家周末【愉快】！", "妈妈，我睡觉了，【晚安】！"]),
 opn("二、用“一边……一边……”说句子", "Đặt câu với 一边……一边…….", [
   ("吃饭　看电视", "我一边吃饭，一边看电视。"), ("散步　聊天儿", "我们一边散步，一边聊天儿。"), ("听音乐　写作业", "她喜欢一边听音乐，一边写作业。")]),
 opn("三、看情况回答：他们正在做什么？", "Trả lời bằng 正在/在……呢.", [
   ("阿明在看什么？（足球比赛）", "阿明正在看足球比赛呢。"), ("林娜妈妈在做什么？（买东西）", "她正和朋友一起买东西呢。"), ("你现在在做什么？", "我正在学习汉语呢。"), ("你在看电视吗？（没）", "我没看电视，我在看书。")]),
 tf("四、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("“我”到公园的时候，那里人很少。", False), ("湖边有人坐在椅子上看书。", True), ("马丁打电话的时候，阿明在睡觉。", False), ("林娜以前习惯晚睡。", True), ("林娜妈妈两个星期以后回来。", True)]),
 opn("五、说一说，写一写", "Viết khoảng 60 chữ.", [
   ("周末早上你一般做什么？你的家人现在正在做什么？（正在……呢　一边……一边……　习惯）",
    "（参考）我有早起的习惯，周末早上我常常去公园跑步。公园里有的人正在打太极拳，有的人一边散步一边听音乐。现在我的妈妈正在做饭呢，爸爸在看电视，我正在写作业。")]),
])

B[28] = dict(zh="长城有八千八百五十多公里", en="The Great Wall Is More Than 8,850 Kilometres Long", vi="Vạn Lý Trường Thành dài hơn 8.850 km",
intro="Đi Bát Đạt Lĩnh bằng gì, mất bao lâu, bao nhiêu tiền? Vì sao gọi là “Vạn Lý Trường Thành”? Và làm thẻ ngân hàng ở Trung Quốc thế nào?",
vocab=V("""
西北部|xīběi bù|cum|phía tây bắc|这个城市在中国的西北部。~Thành phố này ở phía tây bắc Trung Quốc.
市区|shìqū|dt|nội thành, khu trung tâm|我家离市区很远。~Nhà tôi cách nội thành rất xa.
大概|dàgài|pho|khoảng, có lẽ|从这儿到机场大概要一个小时。~Từ đây ra sân bay mất khoảng một tiếng.
公里|gōnglǐ|lg|ki-lô-mét|学校离这儿三公里。~Trường cách đây 3 km.
火车|huǒchē|dt|tàu hỏa|我们坐火车去上海。~Chúng tôi đi tàu hỏa đến Thượng Hải.
公共汽车|gōnggòng qìchē|dt|xe buýt|我每天坐公共汽车上学。~Ngày nào tôi cũng đi xe buýt đến trường.
多|duō|so|hơn (sau số)|我们班有二十多个人。~Lớp chúng tôi có hơn hai mươi người.
车票|chēpiào|dt|vé xe, vé tàu|车票多少钱一张？~Vé xe bao nhiêu tiền một vé?
票|piào|dt|vé|我买了两张电影票。~Tôi mua hai vé xem phim.
几|jǐ|so|vài, mấy|我等了十几分钟。~Tôi đợi mười mấy phút.
到达|dàodá|dong|đến nơi|飞机几点到达北京？~Máy bay mấy giờ đến Bắc Kinh?
元|yuán|lg|đồng, tệ (đơn vị tiền)|这本书三十元。~Quyển sách này 30 tệ.
快车|kuàichē|dt|xe tốc hành, tàu nhanh|坐快车一个小时就到了。~Đi xe nhanh một tiếng là đến.
公交卡|gōngjiāokǎ|dt|thẻ xe buýt|我的公交卡没钱了。~Thẻ xe buýt của tôi hết tiền rồi.
公交车|gōngjiāochē|dt|xe buýt|公交车来了，快上车吧！~Xe buýt đến rồi, mau lên xe!
通过|tōngguò|gioi|thông qua, qua|我通过朋友认识了她。~Tôi quen cô ấy qua một người bạn.
它|tā|dai|nó (vật)|这是我的猫，它很可爱。~Đây là con mèo của tôi, nó rất đáng yêu.
万|wàn|so|vạn, mười nghìn|这台电脑一万多块钱。~Chiếc máy tính này hơn mười nghìn tệ.
里|lǐ|lg|dặm (= 0,5 km)|一公里是二里。~Một ki-lô-mét là hai dặm.
所以|suǒyǐ|lien|cho nên|今天下雨，所以我没去。~Hôm nay mưa nên tôi không đi.
原来|yuánlái|pho|hóa ra|原来是你啊！~Hóa ra là bạn à!
张|zhāng|lg|tấm, tờ, chiếc (giấy, vé, bàn…)|给我两张车票。~Cho tôi hai vé xe.
信用卡|xìnyòngkǎ|dt|thẻ tín dụng|可以用信用卡吗？~Có thể dùng thẻ tín dụng không?
存(钱)|cún (qián)|dong|gửi (tiền)|我去银行存钱。~Tôi đi ngân hàng gửi tiền.
取(钱)|qǔ (qián)|dong|rút (tiền)|我要取五百块钱。~Tôi muốn rút năm trăm tệ.
住|zhù|dong|ở, sống|你住在哪儿？~Bạn sống ở đâu?
刷卡|shuā kǎ|cum|quẹt thẻ|这儿可以刷卡吗？~Ở đây quẹt thẻ được không?
学生证|xuéshēngzhèng|dt|thẻ sinh viên|请带上你的学生证。~Hãy mang theo thẻ sinh viên.
八达岭|Bādálǐng|rieng|Bát Đạt Lĩnh (một đoạn Trường Thành)|周末我们去八达岭吧。~Cuối tuần chúng ta đi Bát Đạt Lĩnh nhé.
长城|Chángchéng|rieng|Trường Thành|你去过长城吗？~Bạn đã đến Trường Thành chưa?
万里长城|Wànlǐ Chángchéng|rieng|Vạn Lý Trường Thành|万里长城很有名。~Vạn Lý Trường Thành rất nổi tiếng.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
八达岭长城在北京的西北部，离市区大概有八十公里。|Trường Thành Bát Đạt Lĩnh ở phía tây bắc Bắc Kinh, cách nội thành khoảng 80 km.
从市区去八达岭长城可以坐火车，也可以坐公共汽车，还可以坐旅游车。|Từ nội thành đi Bát Đạt Lĩnh có thể đi tàu hỏa, xe buýt, hoặc xe du lịch.
火车早上八点半左右出发，坐两个多小时就到了，车票十几块钱。|Tàu hỏa xuất phát khoảng 8 rưỡi sáng, đi hơn hai tiếng là đến, vé mười mấy tệ.
坐旅游车四十多分钟可以到达，每天早上六点半到上午十点有车，车票五十元。|Đi xe du lịch hơn 40 phút là đến, có xe từ 6 rưỡi đến 10 giờ sáng hằng ngày, vé 50 tệ.
坐公共汽车最便宜，普通车车票七元，快车车票十二元。如果有公交卡，坐公交车更便宜。|Đi xe buýt rẻ nhất, xe thường 7 tệ, xe nhanh 12 tệ. Nếu có thẻ xe buýt thì còn rẻ hơn.
"""), q=Q("""
八达岭长城在哪儿？|在北京的西北部，离市区大概八十公里。|Ở phía tây bắc Bắc Kinh, cách nội thành 80 km.
怎么去八达岭？|可以坐火车、公共汽车或者旅游车。|Tàu hỏa, xe buýt hoặc xe du lịch.
从市区到八达岭长城坐火车要多长时间？|两个多小时。|Hơn hai tiếng.
""")),
 dict(t="课文二", narr=False, lines=T("""
马丁>你了解长城吗？|Bạn có hiểu về Trường Thành không?
山田>不能说了解，通过看书知道一些。|Không dám nói là hiểu, qua đọc sách biết được một ít.
马丁>我想问你一个问题。|Mình muốn hỏi bạn một câu.
山田>你说吧。|Bạn nói đi.
马丁>长城有多长？|Trường Thành dài bao nhiêu?
山田>长城有八千八百五十多公里。|Trường Thành dài hơn 8.850 km.
马丁>为什么人们叫它“万里长城”呢？|Sao mọi người gọi nó là “Vạn Lý Trường Thành”?
山田>中国人习惯用“里”，一公里是二里，八千八百五十多公里是一万七千七百多里，所以长城也叫“万里长城”。|Người Trung Quốc quen dùng “dặm”, 1 km là 2 dặm, hơn 8.850 km là hơn 17.700 dặm, nên Trường Thành còn gọi là “Vạn Lý Trường Thành”.
马丁>原来是这样啊。|Hóa ra là vậy.
"""), q=Q("""
长城有多长？|有八千八百五十多公里。|Hơn 8.850 km.
长城为什么也叫“万里长城”？|因为八千八百五十多公里是一万七千七百多里。|Vì hơn 8.850 km là hơn 17.700 dặm.
""")),
 dict(t="课文三", narr=False, lines=T("""
韩国学生>你知道在哪儿可以办公交卡吗？|Bạn biết làm thẻ xe buýt ở đâu không?
崔浩>我家旁边有一个地方就可以办，我带你去。|Cạnh nhà mình có chỗ làm được, mình dẫn bạn đi.
韩国学生>多长时间可以办好？|Bao lâu thì làm xong?
崔浩>五六分钟就可以办好。|Năm sáu phút là xong.
韩国学生>我还想办一张信用卡，你知道怎么办吗？|Mình còn muốn làm thẻ tín dụng, bạn biết làm thế nào không?
崔浩>学生办信用卡很麻烦。在中国，用银行卡很方便，可以存钱、取钱，买东西、住宾馆也可以刷卡。|Sinh viên làm thẻ tín dụng rất phiền. Ở Trung Quốc dùng thẻ ngân hàng rất tiện, gửi tiền, rút tiền, mua đồ, ở khách sạn cũng quẹt thẻ được.
韩国学生>怎么办银行卡呢？|Làm thẻ ngân hàng thế nào?
崔浩>很简单，准备好你的护照和学生证，再带一些钱去银行就行了。|Rất đơn giản, chuẩn bị hộ chiếu và thẻ sinh viên, mang ít tiền đến ngân hàng là được.
韩国学生>好，那我就办银行卡吧。|Được, vậy mình làm thẻ ngân hàng.
"""), q=Q("""
办信用卡方便还是办银行卡方便？|办银行卡方便。|Làm thẻ ngân hàng tiện hơn.
办公交卡要多长时间？|五六分钟就可以办好。|Năm sáu phút.
"""))],
grammar=[
 G("duo_ji", "车票十几块钱。长城有八千八百五十多公里。", "Số ước lượng (3): 多 và 几",
   "(1) “多” sau số tròn 十、百、千、万: 二十多斤, 五百多个人, 一千多公里. Nếu số có hàng đơn vị, “多” đặt SAU lượng từ: 一斤多, 五块多, 两个多小时. (2) “几” chỉ số ước lượng: 几个人, 十几斤, 几百公里, 五十几块钱.",
   [F("N:Số|kw:多/几|M:Lượng từ + danh từ", [("二十|[多]|斤水果", "", "hơn hai mươi cân hoa quả"), ("一千|[多]|公里", "", "hơn một nghìn km"), ("十|[几]|块钱", "", "mười mấy tệ"), ("|[几]|个人", "", "vài người")]),
    F("N:Số|M:Lượng từ|kw:多|X:", [("两|个|[多]|小时", "", "hơn hai tiếng"), ("一|斤|[多]|", "", "hơn một cân"), ("五|块|[多]|", "", "hơn năm tệ")], cap="Số có hàng đơn vị: 多 sau lượng từ")]),
 G("tongguo", "通过看书知道一些。", "通过: thông qua",
   "Giới từ, chỉ dùng người hoặc sự vật làm phương tiện để đạt mục đích.",
   [F("kw:通过|P:Phương tiện|C:Kết quả", [("我[通过]|看电视|学习汉语", "。", "Tôi học tiếng Hán qua việc xem ti vi."), ("[通过]|朱云的介绍，|我认识了他", "。", "Qua sự giới thiệu của Chu Vân, tôi quen anh ấy."), ("[通过]|半年学习，|我进步很大", "。", "Qua nửa năm học, tôi tiến bộ rất nhiều.")])]),
 G("duo_q", "长城有多长？", "多 + Adj?: … bao nhiêu? (hỏi mức độ, số lượng)",
   "Phó từ “多” dùng trong câu hỏi, hỏi về mức độ, số lượng.",
   [F("S:Chủ ngữ|kw:多|A:Tính từ", [("你每天学习|[多]|长时间", "？", "Mỗi ngày bạn học bao lâu?"), ("这个孩子|[多]|大了", "？", "Đứa bé này bao nhiêu tuổi rồi?"), ("从北京到上海|[多]|远", "？", "Từ Bắc Kinh đến Thượng Hải bao xa?")])],
   notes=["所以: cho nên – 今天下雨，所以我没去。", "原来: hóa ra – 原来是这样啊。"]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["大概", "到达", "通过", "所以", "原来", "存", "取", "刷卡", "办", "多"], [
   "从这儿到火车站【大概】要半个小时。", "飞机下午三点【到达】上海。", "我是【通过】朋友认识她的。", "今天太冷了，【所以】我没出门。", "【原来】你也是越南人啊！",
   "我想去银行【存】点儿钱。", "我没有现金了，得去银行【取】钱。", "这儿可以【刷卡】，不用带现金。", "我想【办】一张银行卡。", "你的家离学校【多】远？"]),
 pick("二、选择“多”的位置", "Chọn cách nói đúng.", [
   (["两个多小时", "两多个小时"], ["坐火车要【两个多小时】。"]), (["二十多个人", "二十个多人"], ["我们班有【二十多个人】。"]), (["五块多", "五多块"], ["这个苹果【五块多】。"]), (["一千多公里", "一千公里多"], ["从这儿到那儿有【一千多公里】。"])]),
 opn("三、用“多+Adj”提问", "Đặt câu hỏi với 多 + tính từ.", [
   ("长城有八千八百五十多公里。", "长城有多长？"), ("从学校到机场有四十公里。", "从学校到机场有多远？"), ("我弟弟十八岁了。", "你弟弟多大了？"), ("我每天学习三个小时。", "你每天学习多长时间？")]),
 tf("四、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("八达岭长城离市区大概八十公里。", True), ("坐火车去八达岭最便宜。", False), ("坐旅游车四十多分钟可以到达。", True), ("一公里是二里。", True), ("在中国，学生办信用卡很方便。", False)]),
 opn("五、说一说，写一写", "Giới thiệu một nơi nổi tiếng ở nước bạn (khoảng 60 chữ).", [
   ("这个地方在哪儿？离市区多远？怎么去？要多长时间？车票多少钱？（大概　多　几　如果）",
    "（参考）下龙湾在越南的北部，离河内大概一百七十公里。从河内去下龙湾可以坐旅游车，坐三个多小时就到了，车票两百多块钱。如果有时间，你一定要去看看。")]),
])
