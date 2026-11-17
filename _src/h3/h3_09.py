# -*- coding: utf-8 -*-
# HSK 3 – Bài 9: 打不好没关系
from gtb_gen import V, T, Q, F, G
B = {}

B[9] = dict(zh="打不好没关系", vi="Đánh không giỏi cũng không sao",
intro="Cả trường đang chuẩn bị cho đại hội thể thao: Lý Văn luyện bóng, Bạch Gia Nguyệt tập tennis và cầu lông, cả nhóm cùng xem bóng đá — và Lý Văn chuẩn bị bài nói về Thế vận hội.",
vocab=V("""
校园|xiàoyuán|dt|khuôn viên trường|我们的校园很漂亮。~Khuôn viên trường chúng tôi rất đẹp.
卡|kǎ|dt|thẻ|我忘带银行卡了。~Tôi quên mang thẻ ngân hàng rồi.
球场|qiúchǎng|dt|sân bóng|下课后我们去球场踢球吧。~Tan học chúng ta ra sân đá bóng nhé.
为了|wèile|gioi|vì, để|为了学好汉语，他每天都练习。~Để học giỏi tiếng Hán, ngày nào anh ấy cũng luyện tập.
运动会|yùndònghuì|dt|đại hội thể dục thể thao|学校下个月开运动会。~Tháng sau trường tổ chức đại hội thể thao.
男生|nánshēng|dt|nam sinh, nam giới|我们班男生比女生多。~Lớp chúng tôi nam nhiều hơn nữ.
练|liàn|dong|luyện, tập|他每天练两个小时球。~Mỗi ngày anh ấy tập bóng hai tiếng.
参加|cānjiā|dong|tham gia|你参加明天的会吗？~Bạn có tham gia cuộc họp ngày mai không?
网球|wǎngqiú|dt|quần vợt, tennis|周末我常常打网球。~Cuối tuần tôi hay chơi tennis.
比赛|bǐsài|dt|trận đấu, thi đấu|今天的足球比赛很精彩。~Trận bóng đá hôm nay rất hay.
练习|liànxí|dong|luyện tập, bài tập|说汉语要多练习。~Nói tiếng Hán phải luyện tập nhiều.
好多|hǎoduō|so|khá nhiều|公园里有好多人。~Trong công viên có rất nhiều người.
几乎|jīhū|pho|hầu như|我几乎每天都喝咖啡。~Tôi hầu như ngày nào cũng uống cà phê.
只是|zhǐshì|pho|chỉ là, nhưng|我只是问一下，不买。~Tôi chỉ hỏi chút thôi, không mua.
啤酒|píjiǔ|dt|bia|爸爸喜欢喝啤酒。~Bố thích uống bia.
回|huí|lg|vụ, lần|这是怎么回事？~Chuyện này là thế nào vậy?
紧张|jǐnzhāng|tt|căng thẳng, hồi hộp|考试的时候别紧张。~Lúc thi đừng căng thẳng.
主要|zhǔyào|tt|chủ yếu, chính|这是我们公司的主要问题。~Đây là vấn đề chính của công ty chúng tôi.
受到|shòudào|dong|bị, nhận, chịu, nhận được|他受到了老师的表扬。~Cậu ấy được thầy giáo khen.
影响|yǐngxiǎng|dt|sự ảnh hưởng, ảnh hưởng|别影响别人休息。~Đừng làm ảnh hưởng người khác nghỉ ngơi.
得分|défēn|dong|ghi điểm, ghi bàn, tỉ số|他一个人得了二十分。~Một mình anh ấy ghi hai mươi điểm.
体育|tǐyù|dt|thể dục, thể thao|我最喜欢上体育课。~Tôi thích nhất giờ thể dục.
世界|shìjiè|dt|thế giới|我想去世界各地旅游。~Tôi muốn đi du lịch khắp thế giới.
运动员|yùndòngyuán|dt|vận động viên|他是一名网球运动员。~Anh ấy là một vận động viên tennis.
得到|dédào|dong|đạt được, nhận được|她得到了第一名。~Cô ấy đạt giải nhất.
成绩|chéngjì|dt|thành tích, kết quả|这次考试我的成绩不错。~Kết quả kỳ thi lần này của tôi khá tốt.
奥运会|Àoyùnhuì|rieng|Thế vận hội Olympic|奥运会每四年一次。~Thế vận hội bốn năm một lần.
"""),
texts=[dict(t="课文1", scene="在图书馆门口，李文向白家月跑过去。", scene_vi="Ở trước cửa thư viện, Lý Văn chạy về phía Bạch Gia Nguyệt.", narr=False, lines=T("""
李文>家月，对不起，我昨天忘了还你校园卡了。|Gia Nguyệt, xin lỗi, hôm qua mình quên trả thẻ sinh viên cho cậu.
白家月>没关系。你怎么这么快就过来了？|Không sao. Sao cậu đến nhanh vậy?
李文>我正在球场打球呢，接了你的电话就跑过来了。|Mình đang chơi bóng ở sân, nghe điện thoại của cậu là chạy sang luôn.
白家月>听说为了准备运动会，你们几个男生每天都练球。|Nghe nói để chuẩn bị cho đại hội thể thao, mấy bạn nam các cậu ngày nào cũng tập bóng.
李文>是啊！你打算参加运动会吗？|Đúng vậy! Cậu có định tham gia đại hội thể thao không?
白家月>我想参加网球比赛，最近一直在练习。|Mình muốn thi tennis, dạo này vẫn luyện tập suốt.
李文>好，到时候我去看你的比赛。|Được, đến lúc đó mình đi xem cậu thi đấu.
"""), q=Q("""
李文为什么来得很快？|因为他正在球场打球，接了电话就跑过来了。|Vì cậu ấy đang chơi bóng ở sân, nghe điện thoại là chạy sang.
李文每天在做什么？|为了准备运动会，每天练球。|Tập bóng mỗi ngày để chuẩn bị cho đại hội thể thao.
白家月最近在做什么？|她一直在练习网球。|Cô ấy luyện tập tennis suốt.
""")),
 dict(t="课文2", scene="在校园里，李文和白家月在聊天儿。", scene_vi="Lý Văn và Bạch Gia Nguyệt đang trò chuyện trong khuôn viên trường.", narr=False, lines=T("""
李文>家月，你跟我们一起打羽毛球吧？|Gia Nguyệt, cậu chơi cầu lông với bọn mình nhé?
白家月>我好多年没打羽毛球了，几乎忘了怎么打了。|Mình nhiều năm rồi không chơi cầu lông, gần như quên cách đánh rồi.
李文>不是比赛，打不好没关系。|Không phải thi đấu, đánh không giỏi cũng không sao.
白家月>这么多同学一起打，如果总是接不住球，就太不好意思了。|Nhiều bạn chơi cùng thế, nếu cứ đỡ cầu không được thì ngại lắm.
李文>你想得太多了！大家打球只是为了锻炼身体。|Cậu nghĩ nhiều quá! Mọi người chơi chỉ để rèn luyện sức khỏe thôi.
白家月>我先自己练练吧，下周再跟你们一起打。|Mình tự tập trước đã, tuần sau sẽ chơi cùng các cậu.
李文>我在教天中打羽毛球，你可以过来跟我们一起练。|Mình đang dạy Thiên Trung đánh cầu lông, cậu có thể qua tập cùng bọn mình.
"""), q=Q("""
李文叫白家月一起做什么？|一起打羽毛球。|Cùng chơi cầu lông.
白家月为什么不想去？|因为她好多年没打了，怕总是接不住球。|Vì nhiều năm không chơi, sợ cứ đỡ cầu không được.
白家月想先做什么？|她想先自己练练。|Cô ấy muốn tự tập trước.
""")),
 dict(t="课文3", scene="在李文家，李文、白家月和陈天中一起看电视。", scene_vi="Lý Văn xem bóng đá cùng Bạch Gia Nguyệt và Trần Thiên Trung tại nhà của anh ấy.", narr=False, lines=T("""
陈天中>足球比赛已经开始了，快过来看吧！|Trận bóng đá bắt đầu rồi, mau lại xem đi!
李文>你们先看，冰箱里有啤酒和饮料，我去拿一下。|Các cậu xem trước, trong tủ lạnh có bia và nước ngọt, mình đi lấy.
白家月>今天怎么回事？总是踢不进去！|Hôm nay làm sao vậy? Cứ sút không vào!
陈天中>几个老球员生病了，新球员第一次参加这么重要的比赛，太紧张了。|Mấy cầu thủ lâu năm bị ốm, cầu thủ mới lần đầu đá trận quan trọng thế này, căng thẳng quá.
李文>是啊，主要的球员没参加比赛，所以大家也都受到影响了。|Đúng vậy, cầu thủ chủ chốt không tham gia nên mọi người cũng bị ảnh hưởng.
白家月>越看越着急。我不看了，你们告诉我得分吧。|Càng xem càng sốt ruột. Mình không xem nữa, các cậu báo tỉ số cho mình nhé.
"""), q=Q("""
李文要去冰箱里拿什么？|啤酒和饮料。|Bia và nước ngọt.
今天的足球比赛踢得怎么样？|不太好，总是踢不进去。|Không tốt lắm, cứ sút không vào.
球员们受到什么影响了？|几个主要的老球员生病了，没参加比赛。|Mấy cầu thủ chủ chốt bị ốm, không ra sân.
""")),
 dict(t="课文4", scene="在家里，李文准备演讲稿。", scene_vi="Lý Văn chuẩn bị bài phát biểu ở trong nhà.", narr=True, lines=T("""
我喜欢看体育比赛，最爱看的就是奥运会。|Tôi thích xem thi đấu thể thao, thích xem nhất là Thế vận hội.
奥运会是世界上影响最大的体育比赛。|Thế vận hội là cuộc thi đấu thể thao có ảnh hưởng lớn nhất thế giới.
从1896年到2024年，每次奥运会都有非常多的运动员参加。|Từ năm 1896 đến 2024, kỳ Thế vận hội nào cũng có rất nhiều vận động viên tham gia.
第一位参加奥运会的中国运动员是刘长春，他1932年参加了100米和200米短跑比赛。|Vận động viên Trung Quốc đầu tiên dự Thế vận hội là Lưu Trường Xuân, năm 1932 ông thi chạy ngắn 100 mét và 200 mét.
虽然他没有得到好成绩，但是他让世界认识了中国。|Tuy ông không đạt thành tích tốt, nhưng ông đã giúp thế giới biết đến Trung Quốc.
"""), q=Q("""
奥运会是一个什么样的体育比赛？|是世界上影响最大的体育比赛。|Là cuộc thi đấu thể thao có ảnh hưởng lớn nhất thế giới.
1932年，中国运动员的比赛成绩怎么样？|没有得到好成绩。|Không đạt thành tích tốt.
刘长春的影响是什么？|他让世界认识了中国。|Ông giúp thế giới biết đến Trung Quốc.
"""))],
grammar=[
 G("weile", "目的复句“为了……，……”", "Câu ghép chỉ mục đích “为了……，……”",
   "Trong câu ghép “为了……，……”, vế đứng sau “为了” biểu thị mục đích, vế còn lại biểu thị hành động được thực hiện để đạt mục đích đó (để…, …).",
   [F("kw:为了|C:Mục đích|X:Hành động", [
     ("[为了]|准备运动会，|你们几个男生每天都练球", "。", "Để chuẩn bị cho đại hội thể thao, mấy bạn nam các cậu ngày nào cũng tập bóng."),
     ("[为了]|考上大学，|她每天努力学习", "。", "Để đỗ đại học, ngày nào cô ấy cũng chăm chỉ học."),
     ("[为了]|早点儿到家，|我打算坐飞机回去", "。", "Để về đến nhà sớm, tôi định đi máy bay về."),
     ("大家打球只是|[为了]|锻炼身体", "。", "Mọi người chơi bóng chỉ để rèn luyện sức khỏe.")])]),
 G("keneng", "可能补语", "Bổ ngữ khả năng",
   "Thêm “得” hoặc “不” vào giữa động từ và bổ ngữ kết quả / xu hướng để tạo bổ ngữ khả năng, biểu thị điều kiện có cho phép thực hiện kết quả hay hướng đó không. Khẳng định: động từ + 得 + bổ ngữ; phủ định: động từ + 不 + bổ ngữ; nghi vấn: động từ + 得 + bổ ngữ + động từ + 不 + bổ ngữ, hoặc động từ + 得 + bổ ngữ + 吗.",
   [F("S:Chủ ngữ|V:Động từ|kw:得 / 不|X:Bổ ngữ kết quả / xu hướng", [
     ("|打|[不]|好", "没关系。", "Đánh không giỏi cũng không sao."),
     ("如果总是|接|[不]|住球", "，就太不好意思了。", "Nếu cứ đỡ cầu không được thì ngại lắm."),
     ("这本书你|看|[得]|懂看不懂", "？", "Cuốn sách này bạn đọc hiểu được không?"),
     ("你只有一个星期的时间，|学|[得]|会游泳吗", "？", "Bạn chỉ có một tuần, có học bơi được không?")])]),
 G("yueyue", "固定格式“越A越B”", "Cấu trúc cố định “越A越B”",
   "Trong cấu trúc “越A越B”, A và B có thể đều là cụm động từ hoặc cụm tính từ, cũng có thể A là cụm động từ còn B là cụm tính từ, biểu thị B thay đổi theo sự thay đổi của A (càng… càng…).",
   [F("S:(Chủ ngữ)|kw:越|A:A|kw2:越|B:B", [
     ("今天的足球比赛我|[越]|看|[越]|着急", "。", "Trận bóng hôm nay tôi càng xem càng sốt ruột."),
     ("妈妈|[越]|说，他|[越]|不高兴", "。", "Mẹ càng nói, cậu ấy càng không vui."),
     ("我想认识中国朋友，|[越]|多|[越]|好", "。", "Tôi muốn quen bạn Trung Quốc, càng nhiều càng tốt."),
     ("这个电影|[越]|看|[越]|有意思", "。", "Bộ phim này càng xem càng hay.")])]),
],
test=dict(
 l2=["球踢得不好|没看完比赛|现在很着急", "去旅游了|在公司工作|出国比赛了", "注意打球|别去比赛了|现在多练习"],
 l3=["跑步|参加比赛|看奥运会", "练唱歌|打网球|参加唱歌比赛", "运动|去商场|参加比赛", "爱唱歌跳舞|不喜欢运动|喜欢参加比赛"],
 r1=(["我有点儿不舒服，就先回来了。", "晚上还要开车呢，来杯饮料吧。", "他搬家了，现在住的地方离公司很远。", "真的吗？那我多做一些练习，希望能考好。", "当然。我们先坐公交车，然后换地铁。", "是啊，从南边走到北边要一个小时呢。"],
     ["你们的校园真大啊！", "大家都去上体育课了，你怎么没去？", "小李最近经常迟到，你知道怎么回事吗？", "菜点好了，你想喝点儿什么？来瓶啤酒？", "如果你这次考试能得到好成绩，我就送你一个相机。"]),
 r2=(["卡", "只是", "网球", "练习", "鞋", "运动会"],
     ["老师让我们参加完（　　）回教室。", "我听得懂中国人说话，（　　）看不懂汉字。", "很多事情都是这样：（　　）得越多，得到的成绩就会越好。", "A：你会打（　　）吗？\nB：我不会打，但是我经常去看比赛。", "A：张老师，还您公交（　　），谢谢您。\nB：别客气。我有两张，如果以后忘带了，就告诉我。"]),
 r3=[("儿子最近天天上网看电影，影响了学习成绩，我和妻子都很着急。", "关于儿子，可以知道什么？", "很着急|不喜欢看电影|最近总是上网"),
     ("大家注意，山路越来越难走，都小心一点儿。大家可以穿上大衣，因为越高越冷，别感冒了。", "他们在做什么？", "爬山|看病|买大衣"),
     ("为了参加唱歌比赛，妹妹准备了一个多月，每天晚饭后都给我们唱一个小时，我们觉得她唱得好极了。比赛那天，妹妹穿上漂亮的衣服，高高兴兴地去了。晚上我下课回到家，发现妹妹难过得很，我以为她没有得到好成绩，没想到她告诉我，她记错时间了，她到的时候，比赛早就结束了。",
      ("关于妹妹，可以知道什么？", "没有漂亮的衣服|没时间准备比赛|每天在家练习唱歌"), ("妹妹为什么很难过？", "她唱错了|比赛迟到了|比赛成绩不好"))],
 w1=["这本书（zhǔ）要介绍了中国人的姓名。", "你感冒好了吗？会不会影响你（cān）加比赛？", "（shì）界很大，很多人都想走出去看看。"],
 w2=[("校园", "我们在校园里一起看足球比赛，大家都很开心。"), ("练习", "为了参加比赛，她每天都练习打网球。"), ("运动会", "学校的运动会开始了，同学们正在跑步。")],
 gl={"11": "Khuôn viên trường các bạn rộng thật! → F: Đúng vậy, đi từ phía nam đến phía bắc mất cả tiếng.",
     "12": "Mọi người đều đi học thể dục rồi, sao bạn không đi? → A: Mình hơi mệt nên về trước.",
     "13": "Dạo này Tiểu Lý hay đến muộn, bạn biết sao không? → C: Cậu ấy chuyển nhà, chỗ ở mới cách công ty rất xa.",
     "14": "Gọi món xong rồi, bạn muốn uống gì? Một chai bia nhé? → B: Tối còn phải lái xe, cho cốc nước ngọt thôi.",
     "15": "Nếu kỳ thi này con đạt kết quả tốt, bố sẽ tặng con một chiếc máy ảnh. → D: Thật ạ? Vậy con làm thêm bài tập, mong thi tốt.",
     "16": "参加完运动会 – tham gia xong đại hội thể thao. → F 运动会.",
     "17": "只是看不懂汉字 – chỉ là đọc không hiểu chữ Hán. → B 只是.",
     "18": "练习得越多 – luyện tập càng nhiều. → D 练习.",
     "19": "打网球 – chơi tennis. → C 网球.",
     "20": "公交卡 – thẻ xe buýt. → A 卡.",
     "21": "“儿子最近天天上网看电影” → C 最近总是上网.",
     "22": "“山路越来越难走……越高越冷” → A 爬山.",
     "23": "“每天晚饭后都给我们唱一个小时” → C 每天在家练习唱歌.",
     "24": "“她记错时间了，她到的时候，比赛早就结束了” → B 比赛迟到了."}),
)
