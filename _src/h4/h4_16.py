# -*- coding: utf-8 -*-
# HSK 4下 – Bài 16: 计划赶不上变化
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[16] = dict(zh="计划赶不上变化", vi="Kế hoạch không theo kịp thay đổi",
intro="Bạch Gia Nguyệt phải hoãn chuyến đi Nam Kinh vì có lịch thi; cuộc họp ở công ty Vương Nhất Tuyết bị dời ngày; các bạn bàn về việc có nên lập kế hoạch hay không, và cách đón nhận, thích nghi với những thay đổi trong cuộc sống.",
vocab=V("""
本来|běnlái|pho|vốn dĩ, lúc đầu|我本来想去，后来有事没去成。~Lúc đầu tôi định đi, sau có việc nên không đi được.
只好|zhǐhǎo|pho|đành phải|下雨了，我们只好在家看电影。~Trời mưa, chúng tôi đành ở nhà xem phim.
赶上|gǎnshàng|dong|đuổi kịp, theo kịp; gặp đúng|快走吧，还能赶上最后一班车。~Đi nhanh lên, vẫn kịp chuyến xe cuối.
旅行|lǚxíng|dong|du lịch, đi chơi xa|我打算暑假去云南旅行。~Tôi định nghỉ hè đi du lịch Vân Nam.
推迟|tuīchí|dong|hoãn lại, lùi lại|因为下雨，比赛推迟到下周了。~Vì trời mưa, trận đấu hoãn sang tuần sau.
取消|qǔxiāo|dong|hủy bỏ|航班因为天气不好取消了。~Chuyến bay bị hủy vì thời tiết xấu.
可惜|kěxī|tt|đáng tiếc|你没来参加晚会，真可惜。~Bạn không đến dự buổi tiệc, thật đáng tiếc.
确实|quèshí|pho|quả thật, đúng là|这个办法确实不错。~Cách này quả thật không tồi.
等到|děngdào|gioi|đợi đến khi|等到天晴了，我们再出去。~Đợi đến khi trời tạnh, chúng ta hẵng ra ngoài.
早晨|zǎochen|dt|buổi sáng sớm|早晨的空气很新鲜。~Không khí buổi sáng sớm rất trong lành.
忽然|hūrán|pho|bỗng nhiên, đột nhiên|天忽然下起雨来了。~Trời bỗng đổ mưa.
增加|zēngjiā|dong|tăng thêm|今年学校增加了很多新课程。~Năm nay trường tăng thêm nhiều môn học mới.
调整|tiáozhěng|dong|điều chỉnh|我们要调整一下学习计划。~Chúng ta phải điều chỉnh lại kế hoạch học tập.
错误|cuòwù|dt|lỗi, sai lầm|这篇文章里有几个错误。~Bài viết này có mấy lỗi.
并且|bìngqiě|lien|và, hơn nữa|她学习很好，并且常常帮助同学。~Cô ấy học giỏi, hơn nữa còn hay giúp bạn bè.
例子|lìzi|dt|ví dụ|老师举了一个例子。~Thầy giáo đưa ra một ví dụ.
关键|guānjiàn|dt|then chốt, mấu chốt|学好中文的关键是多练习。~Mấu chốt để học tốt tiếng Trung là luyện tập nhiều.
详细|xiángxì|tt|chi tiết, tỉ mỉ|请你详细地介绍一下。~Bạn giới thiệu chi tiết một chút nhé.
时间表|shíjiānbiǎo|dt|thời gian biểu|我给自己做了一个学习时间表。~Tôi lập cho mình một thời gian biểu học tập.
把握|bǎwò|dt|sự chắc chắn, nắm chắc|这次考试我很有把握。~Lần thi này tôi rất chắc chắn.
相反|xiāngfǎn|lien|ngược lại|他没有生气，相反，还笑了。~Anh ấy không giận, ngược lại còn cười.
部分|bùfen|dt|bộ phận, phần|这本书的第一部分很有意思。~Phần đầu cuốn sách này rất hay.
轻松|qīngsōng|tt|nhẹ nhàng, thoải mái|考完试，大家都觉得很轻松。~Thi xong, mọi người đều thấy rất nhẹ nhõm.
标准|biāozhǔn|dt|tiêu chuẩn|这件事没有统一的标准。~Việc này không có tiêu chuẩn thống nhất.
严格|yángé|tt|nghiêm khắc, nghiêm ngặt|我们的老师很严格。~Thầy giáo chúng tôi rất nghiêm khắc.
取得|qǔdé|dong|đạt được, giành được|他在比赛中取得了好成绩。~Anh ấy đạt thành tích tốt trong cuộc thi.
说不定|shuōbudìng|pho|không chừng, biết đâu|说不定明天会下雨。~Không chừng mai trời sẽ mưa.
灵活|línghuó|tt|linh hoạt|遇到问题要灵活处理。~Gặp vấn đề phải xử lý linh hoạt.
一切|yíqiè|dai|tất cả, mọi thứ|祝你一切顺利！~Chúc bạn mọi việc thuận lợi!
却|què|pho|nhưng, lại|他很累，却不想休息。~Anh ấy rất mệt nhưng lại không muốn nghỉ.
不得不|bùdébù|pho|buộc phải, không thể không|车坏了，我们不得不走回家。~Xe hỏng, chúng tôi buộc phải đi bộ về nhà.
约|yuē|dong|hẹn|我约了朋友周末去爬山。~Tôi hẹn bạn cuối tuần đi leo núi.
不便|búbiàn|tt|bất tiện|给您带来不便，非常抱歉。~Gây bất tiện cho quý khách, chúng tôi rất xin lỗi.
失望|shīwàng|tt|thất vọng|没买到票，他很失望。~Không mua được vé, anh ấy rất thất vọng.
也许|yěxǔ|pho|có lẽ|他也许已经回家了。~Có lẽ anh ấy đã về nhà rồi.
逛|guàng|dong|dạo, đi dạo|周末我们去逛商场吧。~Cuối tuần chúng ta đi dạo trung tâm thương mại nhé.
有趣|yǒuqù|tt|thú vị|这是一个很有趣的故事。~Đây là một câu chuyện rất thú vị.
观看|guānkàn|dong|xem, theo dõi|很多人来观看比赛。~Rất nhiều người đến xem trận đấu.
部|bù|lg|bộ (phim, sách)|这部电影我看了两遍。~Bộ phim này tôi xem hai lần rồi.
无法|wúfǎ|dong|không có cách nào, không thể|我无法相信这是真的。~Tôi không thể tin đây là sự thật.
接受|jiēshòu|dong|tiếp nhận, chấp nhận|我接受你的建议。~Tôi chấp nhận đề nghị của bạn.
"""),
texts=[dict(t="课文1", scene="在王一雪家，王一雪和白家月在聊天儿。", scene_vi="Ở nhà Vương Nhất Tuyết, Nhất Tuyết và Bạch Gia Nguyệt đang trò chuyện.", narr=False, lines=T("""
王一雪>家月，周末你还打算去南京旅游吗？我去年去过那里，可以给你介绍一下。|Gia Nguyệt, cuối tuần em vẫn định đi Nam Kinh du lịch à? Năm ngoái chị đã đến đó, có thể giới thiệu cho em.
白家月>本来都计划好了，可是昨天突然接到通知，下周学校要安排一次考试，所以周末只好在家复习了。|Lúc đầu em đã lên kế hoạch hết rồi, nhưng hôm qua bỗng nhận được thông báo tuần sau trường sắp xếp một bài thi, nên cuối tuần đành ở nhà ôn bài.
王一雪>真是计划赶不上变化啊！看来你的旅行计划只能推迟了。|Đúng là kế hoạch không theo kịp thay đổi! Xem ra kế hoạch du lịch của em đành phải hoãn lại.
白家月>是的，我已经把机票和酒店取消了。虽然有点儿可惜，但学习更重要。|Vâng, em đã hủy vé máy bay và khách sạn rồi. Tuy hơi tiếc nhưng học quan trọng hơn.
王一雪>学习确实要放在第一位。等到考试结束后，你再找个时间去。|Việc học quả thật phải đặt lên hàng đầu. Đợi thi xong em hẵng tìm lúc khác đi.
白家月>我也是这么想的，以后肯定还有很多机会。|Em cũng nghĩ vậy, sau này chắc chắn còn nhiều cơ hội.
"""), q=Q("""
白家月本来计划周末做什么？|去南京旅游。|Đi Nam Kinh du lịch.
白家月为什么周末不能去南京了？|因为下周学校要安排一次考试，她得在家复习。|Vì tuần sau trường có bài thi, cô phải ở nhà ôn bài.
旅行计划推迟后，白家月做什么了？|把机票和酒店取消了。|Hủy vé máy bay và khách sạn.
王一雪建议白家月什么时候去旅游？|考试结束后。|Sau khi thi xong.
""")),
 dict(t="课文2", scene="在公司，王一雪和杨同乐在谈论工作。", scene_vi="Ở công ty, Vương Nhất Tuyết và Dương Đồng Lạc đang bàn công việc.", narr=False, lines=T("""
杨同乐>刚接到通知，明天早晨的会议，时间改到下周了。|Vừa nhận thông báo, cuộc họp sáng mai đổi sang tuần sau rồi.
王一雪>啊？时间都安排好了，怎么说变就变了？|Hả? Thời gian sắp xếp xong hết rồi, sao nói đổi là đổi vậy?
杨同乐>是啊，没想到忽然要改时间。|Đúng vậy, không ngờ bỗng nhiên phải đổi thời gian.
王一雪>好吧，那再看看有没有新的安排，或者增加的会议内容。|Thôi được, vậy xem thêm có sắp xếp mới, hoặc nội dung họp được bổ sung không.
杨同乐>好的。会议材料还需要调整吗？|Vâng. Tài liệu họp còn cần điều chỉnh không chị?
王一雪>再检查一下有没有细节上的错误，并且试着增加一些例子，把内容准备得更全一些。|Kiểm tra lại xem có lỗi chi tiết nào không, đồng thời thử thêm vài ví dụ, chuẩn bị nội dung đầy đủ hơn.
杨同乐>没问题，这样效果肯定会更好。|Không vấn đề gì, như vậy hiệu quả chắc chắn sẽ tốt hơn.
王一雪>看来有时候变化不一定是坏事，关键是我们怎么去适应变化。|Xem ra đôi khi thay đổi chưa chắc là chuyện xấu, mấu chốt là chúng ta thích nghi với thay đổi thế nào.
"""), q=Q("""
杨同乐接到了什么通知？|会议时间变化了，改到下周了。|Thời gian họp thay đổi, dời sang tuần sau.
王一雪让杨同乐做什么？|检查细节问题，并且增加一些例子。|Kiểm tra lỗi chi tiết và thêm một số ví dụ.
王一雪建议怎么调整会议材料？|检查有没有细节上的错误，增加一些例子，把内容准备得更全一些。|Kiểm tra lỗi chi tiết, thêm ví dụ, chuẩn bị nội dung đầy đủ hơn.
对于变化，王一雪是怎么看的？|变化不一定是坏事，关键是怎么去适应变化。|Thay đổi chưa chắc là xấu, mấu chốt là thích nghi thế nào.
""")),
 dict(t="课文3", scene="在课堂上，白家月表达自己对做计划的看法。", scene_vi="Trên lớp, Bạch Gia Nguyệt trình bày quan điểm của mình về việc lập kế hoạch.", narr=True, lines=T("""
在生活和工作中，有的人喜欢做计划，他们会提前安排好每天要做的事情，然后按照详细的时间表去完成任务，觉得这样做更有把握。|Trong cuộc sống và công việc, có người thích lập kế hoạch, họ sắp xếp trước những việc phải làm mỗi ngày, rồi hoàn thành nhiệm vụ theo thời gian biểu chi tiết, cảm thấy làm vậy chắc chắn hơn.
相反，也有一部分人不爱做计划，他们认为随意一些也很好，想到什么就去做什么，感觉这样比较轻松。|Ngược lại, cũng có một số người không thích lập kế hoạch, họ cho rằng tùy ý một chút cũng tốt, nghĩ ra gì thì làm nấy, cảm thấy như vậy thoải mái hơn.
其实，事前做计划是好是坏没有标准答案。|Thật ra, lập kế hoạch trước là tốt hay xấu không có đáp án chuẩn.
严格按照计划做事，常常能取得不错的效果；而不做计划，说不定也会带来新的发现。|Làm việc nghiêm ngặt theo kế hoạch thường đạt hiệu quả tốt; còn không lập kế hoạch, biết đâu cũng mang lại những phát hiện mới.
无论做不做计划，只要既能按时完成任务，又能根据情况灵活调整，就是适合自己的方式。|Dù có lập kế hoạch hay không, chỉ cần vừa hoàn thành nhiệm vụ đúng hạn, vừa điều chỉnh linh hoạt theo tình hình, thì đó là cách phù hợp với mình.
"""), q=Q("""
有的人为什么喜欢做计划？|觉得这样做更有把握。|Cảm thấy làm vậy chắc chắn hơn.
喜欢做计划的人一般是怎么安排事情的？|提前安排好每天要做的事情，然后按照详细的时间表去完成任务。|Sắp xếp trước việc mỗi ngày, rồi làm theo thời gian biểu chi tiết.
不做计划可能会有什么结果？|说不定会带来新的发现。|Biết đâu mang lại phát hiện mới.
事前做计划是好是坏？为什么？|没有标准答案，只要能按时完成任务，又能灵活调整，就是适合自己的方式。|Không có đáp án chuẩn; chỉ cần đúng hạn và linh hoạt là cách hợp với mình.
""")),
 dict(t="课文4", scene="计划与变化", scene_vi="Kế hoạch và thay đổi", narr=True, lines=T("""
人们常说“计划赶不上变化”。|Người ta thường nói “kế hoạch không theo kịp thay đổi”.
有时候，你准备好了一切，却突然出现了新情况，让你不得不改变计划。|Có lúc bạn đã chuẩn bị xong mọi thứ, nhưng bỗng xuất hiện tình huống mới, khiến bạn buộc phải thay đổi kế hoạch.
比如准备出去旅行，可能因为有事而取消；约好见朋友，可能因为天气不好而推迟。|Ví dụ chuẩn bị đi du lịch, có thể vì có việc mà hủy; hẹn gặp bạn, có thể vì thời tiết xấu mà hoãn.
虽然变化经常打乱计划，给我们带来不便，甚至让人感到失望，但这些变化也许会给生活带来新的可能。|Tuy thay đổi thường làm rối kế hoạch, gây bất tiện cho chúng ta, thậm chí khiến người ta thất vọng, nhưng những thay đổi đó có lẽ sẽ mang lại cho cuộc sống những khả năng mới.
比如没去成旅行，于是在家门口的小公园逛了逛，发现那里也很有趣；|Ví dụ không đi du lịch được, thế là đi dạo công viên nhỏ trước nhà, phát hiện ở đó cũng rất thú vị;
没见到朋友，于是在家观看了一部电影，心情也变得很愉快。|không gặp được bạn, thế là ở nhà xem một bộ phim, tâm trạng cũng trở nên vui vẻ.
生活中很多变化是无法提前知道的，我们要做的就是学会接受变化、适应变化，在变化中找到新的解决办法。|Nhiều thay đổi trong cuộc sống không thể biết trước, việc chúng ta cần làm là học cách chấp nhận, thích nghi với thay đổi, tìm ra cách giải quyết mới trong thay đổi.
这样不仅能锻炼自己在面对不同情况时解决问题的能力，也能让我们的生活更轻松。|Như vậy không chỉ rèn luyện năng lực giải quyết vấn đề khi đối mặt các tình huống khác nhau, mà còn khiến cuộc sống của chúng ta nhẹ nhàng hơn.
"""), q=Q("""
“计划赶不上变化”是什么意思？|准备好了一切，却突然出现了新情况，不得不改变计划。|Đã chuẩn bị xong mọi thứ nhưng bỗng có tình huống mới, buộc phải đổi kế hoạch.
变化可能会带来什么影响？|给生活带来新的可能。|Mang lại khả năng mới cho cuộc sống.
面对变化，人们应该怎么做？|接受并适应变化，在变化中找到新的解决办法。|Chấp nhận, thích nghi với thay đổi, tìm cách giải quyết mới.
我们为什么应该积极适应变化？|这样能锻炼解决问题的能力，也能让生活更轻松。|Vì như vậy rèn luyện năng lực giải quyết vấn đề và giúp cuộc sống nhẹ nhàng hơn.
""")),
],
grammar=[
 G("ba_vle", "“把”字句“主语+把+宾语+动词+了”", "Câu chữ “把”: Chủ ngữ + 把 + Tân ngữ + Động từ + 了",
   "Biểu thị xử lý tương ứng đối với người hoặc sự vật xác định, và tạo ra một kết quả nào đó.",
   [F("S:Chủ ngữ|kw:把|O:Tân ngữ|V:Động từ|kw2:了", [
     ("我已经|[把]|机票和酒店|取消|[了]", "。", "Tôi đã hủy vé máy bay và khách sạn rồi."),
     ("你|[把]|灯|关|[了]", "吧，我想睡觉了。", "Bạn tắt đèn đi, tôi muốn ngủ rồi."),
     ("你别忘了|[把]|衣服|洗|[了]", "，明天还得穿呢。", "Bạn đừng quên giặt quần áo, mai còn phải mặc.")])]),
 G("bingqie", "递进复句“……，并且……”", "Câu phức tăng tiến “……，并且……”",
   "“并且” dùng để nối các hành động hoặc tình huống, biểu thị giải thích thêm một bước: “và, hơn nữa, đồng thời”.",
   [F("X:Vế trước|kw:并且|V:Vế sau (thêm một bước)", [
     ("再检查一下有没有细节上的错误|[并且]|试着增加一些例子", "。", "Kiểm tra lại xem có lỗi chi tiết không, đồng thời thử thêm vài ví dụ."),
     ("他按时完成了任务|[并且]|做得很好", "。", "Anh ấy hoàn thành nhiệm vụ đúng hạn, hơn nữa làm rất tốt."),
     ("人们的生活水平提高了|[并且]|生活方式也发生了很大的变化", "。", "Mức sống của mọi người được nâng cao, đồng thời lối sống cũng thay đổi rất nhiều.")])]),
 G("shuobuding", "固定短语“说不定”", "Cụm từ cố định “说不定”",
   "“说不定” biểu thị suy đoán, ước đoán về tình huống hoặc kết quả có thể xảy ra: “không chừng, biết đâu”.",
   [F("X:Tình huống|kw:说不定|V:Suy đoán", [
     ("不做计划|[说不定]|也会带来新的发现", "。", "Không lập kế hoạch, biết đâu cũng mang lại phát hiện mới."),
     ("今天这么阴|[说不定]|会下雨", "。", "Hôm nay trời âm u thế, không chừng sẽ mưa."),
     ("你再试一次|[说不定]|就成功了", "。", "Bạn thử lại một lần nữa, biết đâu sẽ thành công.")])]),
 G("que", "关联副词“却”", "Phó từ liên kết “却”",
   "“却” biểu thị chuyển ngoặt (nhưng, lại), đứng sau chủ ngữ, trước động từ / tính từ ở vế sau.",
   [F("X:Vế trước|S:(Chủ ngữ)|kw:却|V:Vế sau (trái ý)", [
     ("你准备好了一切||[却]|突然出现了新情况，让你不得不改变计划", "。", "Bạn đã chuẩn bị xong mọi thứ, nhưng bỗng xuất hiện tình huống mới, buộc bạn phải đổi kế hoạch."),
     ("他通过了面试||[却]|一点儿也不激动", "。", "Anh ấy qua vòng phỏng vấn, lại chẳng hề phấn khích chút nào."),
     ("她长得很像她姐姐|性格|[却]|完全不同", "。", "Cô ấy trông rất giống chị gái, nhưng tính cách lại hoàn toàn khác.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["等到", "关键", "例子", "本来", "确实", "可惜"], [
   "要想提高成绩，【关键】是坚持每天复习。", "他【确实】说得很对，我也同意他的看法。", "你没能参加文化节活动，真是太【可惜】了。",
   "【等到】工作不那么忙了，我想和家人去旅游。", "我【本来】打算周末出去玩，可是后来有事，就没去成。", "王老师讲课时常常会用一些【例子】，帮助学生们更好地理解。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["约", "标准", "相反", "详细", "无法", "一切"], [
   "A：这次公司招聘的【标准】是什么？ B：至少有五年的工作经验，并且有较强的个人工作能力。", "A：老师，这个问题可以讲得再【详细】一点儿吗？ B：好的，我再给你讲一遍。",
   "A：很久没有见到你了，你最近过得怎么样？ B：还不错，【一切】都很顺利。", "A：我以为他会同意，没想到结果正好【相反】。 B：是啊，看来他还是不太愿意参加。",
   "A：你什么时候有时间？我想【约】你喝杯咖啡。 B：好啊，我也正想跟你聊聊呢。明天中午怎么样？", "A：经理，我明天有事，【无法】参加会议，想跟您请假。 B：好的，那你提前把工作安排好吧。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["天气忽然变阴了", "他只好取消了爬山的计划", "虽然有点儿失望", "需要学会接受新的情况"], [
   "小李周末本来计划和朋友去爬山，还提前准备好了水和食物。可是周六早晨，【天气忽然变阴了】，看起来可能会下雨。为了安全，【他只好取消了爬山的计划】。【虽然有点儿失望】，但小李重新做了计划，用原来爬山的时间完成了一些学习任务。周末结束后，他觉得这样安排也不错。这次经历让他明白，遇到变化时，【需要学会接受新的情况】。只要灵活调整计划，就能把事情安排好，让自己过得轻松、愉快。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l16", items=[
   ("逛", "周末我和朋友一起去逛商场。"), ("有趣", "妈妈给孩子讲了一个有趣的故事。"), ("错误", "经理发现材料里有一个错误。")]),
])
