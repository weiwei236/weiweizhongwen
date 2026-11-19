# -*- coding: utf-8 -*-
# HSK 4下 – Bài 17: 运动让我更健康
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[17] = dict(zh="运动让我更健康", vi="Vận động giúp tôi khỏe mạnh hơn",
intro="Dương Đồng Lạc đăng ký tập ở phòng gym mới mở cạnh công ty, rủ cả Vương Nhất Tuyết cùng tập; anh chia sẻ lợi ích của việc tập gym; bài cuối giới thiệu bóng bàn – “quốc cầu” của Trung Quốc.",
vocab=V("""
路过|lùguò|dong|đi ngang qua|我每天上班都路过这家咖啡店。~Ngày nào đi làm tôi cũng đi ngang qua quán cà phê này.
趟|tàng|lg|chuyến, lượt|我明天要去一趟上海。~Mai tôi phải đi Thượng Hải một chuyến.
健身房|jiànshēnfáng|dt|phòng tập thể hình|他每周去三次健身房。~Mỗi tuần anh ấy đến phòng gym ba lần.
健身|jiànshēn|dong|tập thể hình, rèn luyện sức khỏe|健身让我变得更有精神。~Tập thể hình khiến tôi khỏe khoắn hơn.
体重|tǐzhòng|dt|cân nặng|最近我的体重增加了。~Dạo này cân nặng của tôi tăng lên.
会员|huìyuán|dt|hội viên, thành viên|我办了一张超市的会员卡。~Tôi làm một thẻ thành viên siêu thị.
饼干|bǐnggān|dt|bánh quy|孩子们很喜欢吃饼干。~Bọn trẻ rất thích ăn bánh quy.
酸奶|suānnǎi|dt|sữa chua|我每天早上喝一杯酸奶。~Sáng nào tôi cũng uống một cốc sữa chua.
果汁|guǒzhī|dt|nước hoa quả|请给我来一杯苹果汁。~Cho tôi một cốc nước táo.
教练|jiàoliàn|dt|huấn luyện viên|我们的游泳教练很专业。~Huấn luyện viên bơi của chúng tôi rất chuyên nghiệp.
动作|dòngzuò|dt|động tác|这个动作有点儿难。~Động tác này hơi khó.
科学|kēxué|tt|khoa học (hợp lý)|锻炼身体要讲究科学方法。~Rèn luyện thân thể phải theo phương pháp khoa học.
受伤|shòushāng|dong|bị thương|他踢球时受伤了。~Anh ấy bị thương khi đá bóng.
操场|cāochǎng|dt|sân vận động (trường), bãi tập|同学们在操场上跑步。~Các bạn đang chạy bộ trên sân trường.
其中|qízhōng|dt|trong đó|班里有三十个学生，其中一半是女生。~Lớp có ba mươi học sinh, trong đó một nửa là nữ.
之|zhī|tro|của (văn viết)|他是我最好的朋友之一。~Anh ấy là một trong những người bạn tốt nhất của tôi.
火|huǒ|tt|nổi, hot, đắt khách|这家饭馆最近很火。~Quán ăn này dạo này rất đắt khách.
好处|hǎochù|dt|lợi ích, cái hay|多运动对身体有很多好处。~Vận động nhiều có rất nhiều lợi ích cho cơ thể.
设备|shèbèi|dt|thiết bị|这家医院的设备很先进。~Thiết bị của bệnh viện này rất hiện đại.
全身|quánshēn|dt|toàn thân|游泳可以锻炼全身。~Bơi lội có thể rèn luyện toàn thân.
准确|zhǔnquè|tt|chính xác|你的发音很准确。~Phát âm của bạn rất chính xác.
仅仅|jǐnjǐn|pho|chỉ, vẻn vẹn|仅仅一个月，他就学会了游泳。~Chỉ một tháng, anh ấy đã biết bơi.
表扬|biǎoyáng|dong|khen ngợi, biểu dương|老师表扬了他的作业。~Thầy giáo khen bài tập của cậu ấy.
进步|jìnbù|dong|tiến bộ|你的中文进步很大。~Tiếng Trung của bạn tiến bộ rất nhiều.
鼓励|gǔlì|dong|khích lệ, động viên|妈妈一直鼓励我坚持下去。~Mẹ luôn động viên tôi kiên trì.
帅|shuài|tt|đẹp trai, ngầu|他穿这件衣服很帅。~Anh ấy mặc áo này rất đẹp trai.
乒乓球|pīngpāngqiú|dt|bóng bàn|爷爷每天早上都打乒乓球。~Sáng nào ông cũng chơi bóng bàn.
队|duì|dt|đội|他是我们学校篮球队的。~Cậu ấy ở đội bóng rổ của trường chúng tôi.
项|xiàng|lg|hạng mục, môn (lượng từ)|这项工作由他负责。~Hạng mục công việc này do anh ấy phụ trách.
赢得|yíngdé|dong|giành được, giành chiến thắng|他们赢得了比赛。~Họ đã giành chiến thắng trong trận đấu.
叫作|jiàozuò|dong|gọi là|这种花叫作牡丹。~Loài hoa này gọi là mẫu đơn.
梦|mèng|dt|giấc mơ|昨天晚上我做了一个梦。~Tối qua tôi mơ một giấc mơ.
不断|búduàn|pho|không ngừng|他不断地努力学习。~Anh ấy không ngừng nỗ lực học tập.
队员|duìyuán|dt|đội viên, thành viên đội|队员们每天都要训练。~Các thành viên đội ngày nào cũng phải tập luyện.
训练|xùnliàn|dong|huấn luyện, tập luyện|运动员们正在训练。~Các vận động viên đang tập luyện.
球队|qiúduì|dt|đội bóng|你喜欢哪个球队？~Bạn thích đội bóng nào?
球迷|qiúmí|dt|người hâm mộ bóng (fan)|很多球迷来看这场比赛。~Rất nhiều cổ động viên đến xem trận đấu này.
梦想|mèngxiǎng|dt|ước mơ|我的梦想是当一名老师。~Ước mơ của tôi là trở thành giáo viên.
大赛|dàsài|dt|giải đấu lớn|他参加了国际大赛。~Anh ấy tham gia giải đấu quốc tế.
赢|yíng|dong|thắng|我们赢了！~Chúng ta thắng rồi!
连|lián|gioi|ngay cả, thậm chí|他连饭都没吃就走了。~Anh ấy thậm chí chưa ăn cơm đã đi rồi.
"""),
texts=[dict(t="课文1", scene="在公司，王一雪准备下班，跟杨同乐打了个招呼。", scene_vi="Ở công ty, Vương Nhất Tuyết chuẩn bị tan làm, chào Dương Đồng Lạc.", narr=False, lines=T("""
王一雪>下班了！同乐，我今天正好要路过你们家那边，用不用我开车送你？|Tan làm rồi! Đồng Lạc, hôm nay chị vừa hay đi ngang qua nhà em, có cần chị lái xe đưa em về không?
杨同乐>谢谢一雪姐，不过您走您的吧，我一会儿还要去一趟健身房。|Cảm ơn chị Nhất Tuyết, nhưng chị cứ về đi, lát nữa em còn phải đến phòng gym một chuyến.
王一雪>去健身房？你什么时候开始健身的？|Đến phòng gym à? Em bắt đầu tập từ khi nào thế?
杨同乐>我上个星期发现单位旁边新开了一家健身房。我最近体重增加了不少，正好想运动一下，就进去看了看。|Tuần trước em phát hiện bên cạnh cơ quan mới mở một phòng gym. Dạo này em tăng cân khá nhiều, đúng lúc muốn vận động, nên vào xem thử.
王一雪>感觉怎么样？|Thấy thế nào?
杨同乐>挺不错的。当时正好有打折活动，我就办了一张会员卡。|Khá tốt ạ. Lúc đó vừa hay có chương trình giảm giá, em làm luôn một thẻ hội viên.
"""), q=Q("""
杨同乐一会儿要做什么？|去健身房健身。|Đến phòng gym tập.
杨同乐为什么想健身？|因为他最近体重增加了不少。|Vì dạo này anh tăng cân khá nhiều.
关于那家健身房，可以知道什么？|是单位旁边新开的。|Mới mở bên cạnh cơ quan.
杨同乐为什么办了会员卡？|因为当时正好有打折活动。|Vì lúc đó vừa có chương trình giảm giá.
""")),
 dict(t="课文2", scene="在公司，王一雪和杨同乐下班后在聊天儿。", scene_vi="Ở công ty, Vương Nhất Tuyết và Dương Đồng Lạc trò chuyện sau giờ làm.", narr=False, lines=T("""
王一雪>同乐，你晚上不吃饭就去健身，不会饿吗？|Đồng Lạc, tối em không ăn cơm đã đi tập, không đói à?
杨同乐>我带了饼干、酸奶和果汁，一会儿吃完了再去。|Em mang bánh quy, sữa chua và nước hoa quả, lát ăn xong rồi mới đi.
王一雪>那你为什么不在家附近找健身房？吃完晚饭，休息一下再去，不是更好吗？|Thế sao em không tìm phòng gym gần nhà? Ăn tối xong nghỉ một lát rồi đi, chẳng phải tốt hơn sao?
杨同乐>离我家最近的健身房也要坐两站公交车，一来一回得半个小时，太浪费时间了。|Phòng gym gần nhà em nhất cũng phải đi hai trạm xe buýt, đi về mất nửa tiếng, phí thời gian quá.
王一雪>确实。那这家健身房的教练怎么样？|Đúng thật. Thế huấn luyện viên ở phòng gym này thế nào?
杨同乐>教练很热情，也非常专业，动作讲得很清楚。|Huấn luyện viên rất nhiệt tình, cũng rất chuyên nghiệp, giảng động tác rất rõ ràng.
王一雪>听你这么一说，我也想试试了。我现在都是在家看着视频练，动作不一定标准。|Nghe em nói vậy, chị cũng muốn thử. Bây giờ chị toàn tập theo video ở nhà, động tác chưa chắc chuẩn.
杨同乐>好啊，那您也来吧。锻炼要科学，否则容易受伤。|Hay quá, vậy chị cũng đến đi. Tập luyện phải khoa học, nếu không dễ bị thương.
"""), q=Q("""
杨同乐去健身房前要做什么？|吃饼干、酸奶，喝果汁。|Ăn bánh quy, sữa chua, uống nước hoa quả.
杨同乐为什么不去家附近的健身房？|因为离家最近的也要坐两站公交车，一来一回得半个小时，太浪费时间了。|Vì gần nhất cũng hai trạm xe buýt, đi về mất nửa tiếng, phí thời gian.
公司附近那家健身房的教练怎么样？|很热情，也非常专业，动作讲得很清楚。|Rất nhiệt tình, rất chuyên nghiệp, giảng động tác rõ ràng.
王一雪为什么也想去健身房锻炼？|因为她在家看视频练，动作不一定标准。|Vì cô tập theo video ở nhà, động tác chưa chắc chuẩn.
""")),
 dict(t="课文3", scene="杨同乐的健身情况", scene_vi="Chuyện tập gym của Dương Đồng Lạc", narr=True, lines=T("""
有人爱在操场跑步，有人喜欢通过打球锻炼身体，还有一部分人愿意去健身房健身，杨同乐就是其中之一。|Có người thích chạy bộ ở sân vận động, có người thích rèn luyện bằng chơi bóng, còn một số người thích đến phòng gym tập, Dương Đồng Lạc là một trong số đó.
杨同乐认为健身房火起来是因为它有很多好处——环境好、设备全，可以锻炼全身。|Dương Đồng Lạc cho rằng phòng gym trở nên “hot” vì có nhiều ưu điểm — môi trường tốt, thiết bị đầy đủ, có thể rèn luyện toàn thân.
另外，健身房里一般还有专业教练，能帮助大家把动作做准确，练习的效果也更好。|Ngoài ra, phòng gym thường có huấn luyện viên chuyên nghiệp, giúp mọi người thực hiện động tác chính xác, hiệu quả luyện tập cũng tốt hơn.
仅仅经过一个月左右的锻炼，杨同乐就感觉自己的身体比以前更健康了。|Chỉ sau khoảng một tháng tập luyện, Dương Đồng Lạc đã cảm thấy cơ thể khỏe mạnh hơn trước.
教练也表扬他取得了很大的进步，并鼓励他坚持下去，还说随着身体越来越好，人看起来也会更帅。|Huấn luyện viên cũng khen anh tiến bộ rất nhiều, động viên anh kiên trì, còn nói cơ thể càng ngày càng khỏe thì người trông cũng đẹp trai hơn.
"""), q=Q("""
杨同乐喜欢用什么方式锻炼？|去健身房健身。|Đến phòng gym tập.
健身房为什么会火起来？|因为它环境好、设备全，可以锻炼全身，还有专业教练。|Vì môi trường tốt, thiết bị đầy đủ, rèn luyện toàn thân, có huấn luyện viên chuyên nghiệp.
锻炼一个月后，杨同乐有什么变化？|感觉身体比以前更健康了。|Cảm thấy khỏe mạnh hơn trước.
教练为什么表扬杨同乐？|因为他取得了很大的进步。|Vì anh tiến bộ rất nhiều.
""")),
 dict(t="课文4", scene="中国的“国球”", scene_vi="“Quốc cầu” của Trung Quốc", narr=True, lines=T("""
中国乒乓球队非常有名，常在各项比赛中赢得第一名，被叫作“梦之队”。|Đội tuyển bóng bàn Trung Quốc rất nổi tiếng, thường giành giải nhất ở các giải đấu, được gọi là “Đội hình trong mơ”.
为了不断提高自己的水平，队员们每天都要进行严格的训练。|Để không ngừng nâng cao trình độ, các thành viên ngày nào cũng tập luyện nghiêm ngặt.
正因为这样，球队才能在比赛中取得更好的成绩，获得更多球迷的喜爱。|Chính vì vậy, đội mới đạt thành tích tốt hơn trong thi đấu, được nhiều người hâm mộ yêu mến hơn.
许多年轻的乒乓球运动员都有一个梦想，那就是进入国家队，参加世界大赛，为球队赢下比赛。|Nhiều vận động viên bóng bàn trẻ đều có một ước mơ, đó là vào đội tuyển quốc gia, tham gia giải đấu thế giới, giành chiến thắng cho đội.
在中国，除了专业运动员，喜欢打乒乓球的普通人也特别多。|Ở Trung Quốc, ngoài vận động viên chuyên nghiệp, người bình thường thích chơi bóng bàn cũng rất nhiều.
连一些年龄比较大的老人都坚持打球，年轻人更是把它作为一种日常锻炼的方式。|Ngay cả một số người lớn tuổi cũng kiên trì chơi bóng, người trẻ thì càng coi nó là một cách rèn luyện hằng ngày.
可以说，乒乓球是中国人生活中最常见的运动之一。|Có thể nói, bóng bàn là một trong những môn thể thao phổ biến nhất trong cuộc sống của người Trung Quốc.
"""), q=Q("""
中国乒乓球队为什么被叫作“梦之队”？|因为常在各项比赛中赢得第一名。|Vì thường giành giải nhất ở các giải đấu.
乒乓球队为什么每天都要进行严格的训练？|为了不断提高自己的水平。|Để không ngừng nâng cao trình độ.
许多年轻的乒乓球运动员有什么梦想？|进入国家队，参加世界大赛，为球队赢下比赛。|Vào đội tuyển quốc gia, dự giải thế giới, giành chiến thắng cho đội.
关于乒乓球在中国的情况，哪项正确？|乒乓球是中国人生活中最常见的运动之一。|Bóng bàn là một trong những môn thể thao phổ biến nhất ở Trung Quốc.
""")),
],
grammar=[
 G("nixnide", "固定格式“你×你的吧”", "Cấu trúc cố định “你 × 你的吧”",
   "Biểu thị mỗi người làm việc của mình, không cần cùng làm việc gì đó; thường dùng để từ chối một cách lịch sự: “bạn cứ… việc của bạn đi”.",
   [F("S:你 / 您 / 你们|V:×|kw:你的吧", [
     ("您|走|[您的吧]", "，我一会儿还要去一趟健身房。", "Chị cứ về đi, lát nữa em còn phải đến phòng gym."),
     ("你|忙|[你的吧]", "，我自己就能完成。", "Bạn cứ làm việc của bạn đi, tôi tự làm được."),
     ("你们|玩|[你们的吧]", "，我今天想在家休息。", "Các bạn cứ chơi đi, hôm nay tôi muốn nghỉ ở nhà.")])]),
 G("yiAyiB", "固定短语“一A一B”", "Cụm từ cố định “一A一B”",
   "“一A一B” biểu thị hai mặt đối xứng hoặc hai phương diện của tình huống; A và B là từ đơn âm tiết.",
   [F("S:(Phần trước)|kw:一|A:A|kw2:一|B:B|V:Nội dung", [
     ("|[一]|来|[一]|回|得半个小时，太浪费时间了", "。", "Đi một lượt về một lượt mất nửa tiếng, phí thời gian quá."),
     ("她说话的声音不大，但是|[一]|字|[一]|句|说得很清楚", "。", "Giọng cô ấy không to, nhưng từng chữ từng câu nói rất rõ."),
     ("记者和运动员|[一]|问|[一]|答|谈到了很多比赛中的事情", "。", "Phóng viên và vận động viên hỏi đáp qua lại, nói về nhiều chuyện trong trận đấu.")])]),
 G("biaoyang", "兼语句“主语+表扬/批评+宾语1+动词+宾语2”", "Câu kiêm ngữ: Chủ ngữ + 表扬 / 批评 + Tân ngữ 1 + Động từ + Tân ngữ 2",
   "Biểu thị đánh giá (khen / phê bình) việc người nào đó đã làm.",
   [F("S:Chủ ngữ|kw:表扬 / 批评|O:Tân ngữ 1 (người)|V:Việc được đánh giá", [
     ("教练也|[表扬]|他|取得了很大的进步", "。", "Huấn luyện viên cũng khen anh ấy tiến bộ rất nhiều."),
     ("老师|[表扬]|白家月|坚持每天学习中文", "。", "Cô giáo khen Bạch Gia Nguyệt kiên trì học tiếng Trung mỗi ngày."),
     ("经理|[批评]|他|没有按时完成工作", "。", "Giám đốc phê bình anh ấy không hoàn thành công việc đúng hạn.")])]),
 G("lianyedou", "递进复句“连……也/都……，……更……”", "Câu phức tăng tiến “连……也 / 都……，……更……”",
   "Nêu một ví dụ cực đoan để làm rõ một tình huống: “ngay cả… cũng…, thì… càng…”.",
   [F("S:(Chủ ngữ)|kw:连|X:Ví dụ cực đoan|kw2:也 / 都|V:Vị ngữ|B:……更……", [
     ("|[连]|一些年龄比较大的老人|[都]|坚持打球|年轻人更是把它作为一种日常锻炼的方式", "。", "Ngay cả một số người lớn tuổi cũng kiên trì chơi bóng, người trẻ thì càng coi nó là cách rèn luyện hằng ngày."),
     ("我有时候|[连]|老师说的话|[也]|听不懂|听广播就更难了", "。", "Có khi ngay cả lời thầy cô tôi cũng nghe không hiểu, nghe đài lại càng khó."),
     ("今天早上他|[连]|脸|[都]|没来得及洗|更没有时间准备早饭了", "。", "Sáng nay anh ấy ngay cả mặt cũng chưa kịp rửa, càng không có thời gian chuẩn bị bữa sáng.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["趟", "科学", "路过", "会员", "酸奶", "健身"], [
   "随着【科学】的发展，人们的生活方式发生了很大的变化。", "昨天我在回家的路上【路过】了一家新开的咖啡店。", "我吃完晚饭后都会去【健身】，已经坚持两年多了。",
   "她早上一般都会喝杯【酸奶】，觉得这样对身体有好处。", "明天我要去一【趟】上海，咱们下周再约时间见面吧。", "楼下新开了一家超市，正在做活动，办【会员】还送小礼物。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["队", "赢", "准确", "梦想", "其中", "不断"], [
   "A：昨天的比赛结果怎么样？ B：三比二，我们球队最后【赢】了。", "A：你儿子以后想做什么工作？ B：他的【梦想】是当一名医生。",
   "A：您看我这个句子写得对吗？ B：不太【准确】，你再检查一下吧。", "A：你最近工作怎么样？ B：公司给我们的任务【不断】增加，我们越来越忙了。",
   "A：他们班参加羽毛球比赛的人多吗？ B：挺多的，【其中】还有几个水平很高的。", "A：听说你进入了学校的乒乓球【队】？ B：没错，我很喜欢打乒乓球，而且打得很好。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["体重也一直增加", "他决定去健身房锻炼", "虽然他刚开始做得还不太标准", "只要方法科学"], [
   "小张以前不太爱运动，下班以后常常在家看电视或玩手机，很少锻炼身体。时间长了，他感觉自己的身体越来越差，【体重也一直增加】，工作的时候还容易觉得累。后来在朋友的建议下，【他决定去健身房锻炼】。教练先教了他一些最简单的动作。【虽然他刚开始做得还不太标准】，但他慢慢练、慢慢改，最后还是坚持了下来。现在，小张已经养成了运动的习惯。他觉得，【只要方法科学】，并且坚持锻炼，就一定能取得不错的效果。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l17", items=[
   ("赢得", "我们队赢得了这次比赛。"), ("受伤", "她跳舞的时候不小心受伤了。"), ("球迷", "球迷们为自己喜欢的球队加油。")]),
])
