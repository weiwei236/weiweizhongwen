# -*- coding: utf-8 -*-
# HSK 4下 – Bài 15: 我去应聘了
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[15] = dict(zh="我去应聘了", vi="Tôi đã đi ứng tuyển",
intro="Lý Văn đi ứng tuyển thực tập ở một công ty dược: đăng ký online, thi viết, phỏng vấn rồi nhận tin trúng tuyển; bài cuối nói về ý nghĩa của việc thực tập đối với sinh viên Trung Quốc.",
vocab=V("""
期中|qīzhōng|dt|giữa kỳ|下周我们有期中考试。~Tuần sau chúng tôi thi giữa kỳ.
医药|yīyào|dt|y dược|她在一家医药公司工作。~Cô ấy làm việc ở một công ty dược.
应聘|yìngpìn|dong|ứng tuyển, dự tuyển|他去一家大公司应聘了。~Anh ấy đã đi ứng tuyển ở một công ty lớn.
招聘|zhāopìn|dong|tuyển dụng|这家公司正在招聘新员工。~Công ty này đang tuyển nhân viên mới.
实习|shíxí|dong|thực tập|暑假我在一家医院实习。~Kỳ nghỉ hè tôi thực tập ở một bệnh viện.
考虑|kǎolǜ|dong|cân nhắc, suy nghĩ|这件事我需要好好考虑一下。~Việc này tôi cần suy nghĩ kỹ một chút.
单位|dānwèi|dt|đơn vị, cơ quan|你在哪个单位工作？~Bạn làm việc ở cơ quan nào?
毕业生|bìyèshēng|dt|sinh viên tốt nghiệp|今年的毕业生比去年多。~Sinh viên tốt nghiệp năm nay nhiều hơn năm ngoái.
经历|jīnglì|dt|kinh nghiệm, trải nghiệm|这是一次难忘的经历。~Đây là một trải nghiệm khó quên.
消息|xiāoxi|dt|tin tức|我还在等公司的消息。~Tôi vẫn đang đợi tin của công ty.
报名|bàomíng|dong|đăng ký, ghi danh|我已经报名参加比赛了。~Tôi đã đăng ký tham gia cuộc thi.
填写|tiánxiě|dong|điền (biểu mẫu)|请填写你的姓名和电话。~Vui lòng điền họ tên và số điện thoại.
笔试|bǐshì|dong|thi viết|笔试通过以后才能参加面试。~Qua vòng thi viết mới được phỏng vấn.
面试|miànshì|dong|phỏng vấn|明天上午我要去面试。~Sáng mai tôi phải đi phỏng vấn.
答|dá|dong|trả lời, làm (bài)|这道题我答错了。~Câu này tôi làm sai rồi.
由|yóu|gioi|do (ai đó làm)|这次会议由王经理负责。~Cuộc họp này do giám đốc Vương phụ trách.
部门|bùmén|dt|bộ phận, phòng ban|他在市场部门工作。~Anh ấy làm ở bộ phận thị trường.
负责人|fùzérén|dt|người phụ trách|有问题可以问这个项目的负责人。~Có vấn đề có thể hỏi người phụ trách dự án này.
不论|búlùn|lien|bất luận, dù|不论多难，我都要试试。~Dù khó đến đâu tôi cũng muốn thử.
肯定|kěndìng|pho|chắc chắn, nhất định|他肯定会来的。~Anh ấy chắc chắn sẽ đến.
短信|duǎnxìn|dt|tin nhắn|我给你发了一条短信。~Tôi đã gửi cho bạn một tin nhắn.
激动|jīdòng|tt|xúc động, phấn khích|听到这个消息，她激动得哭了。~Nghe tin này, cô ấy xúc động đến bật khóc.
扔|rēng|dong|ném, vứt|别把垃圾扔在地上。~Đừng vứt rác xuống đất.
理发|lǐfà|dong|cắt tóc|周末我要去理发。~Cuối tuần tôi phải đi cắt tóc.
镜子|jìngzi|dt|cái gương|她每天出门前都要照镜子。~Ngày nào trước khi ra ngoài cô ấy cũng soi gương.
自我|zìwǒ|dai|tự mình, bản thân|面试时先做一下自我介绍。~Khi phỏng vấn trước hết hãy tự giới thiệu bản thân.
能够|nénggòu|dong|có thể|我能够用中文和朋友聊天儿了。~Tôi đã có thể trò chuyện với bạn bằng tiếng Trung.
运用|yùnyòng|dong|vận dụng|要学会运用学到的知识。~Phải học cách vận dụng kiến thức đã học.
工厂|gōngchǎng|dt|nhà máy|他爸爸在工厂上班。~Bố cậu ấy làm việc ở nhà máy.
规定|guīdìng|dt|quy định|学校规定上课不能用手机。~Nhà trường quy định trong giờ học không được dùng điện thoại.
课堂|kètáng|dt|lớp học, giờ học|课堂上大家都很认真。~Trong giờ học mọi người đều rất chăm chú.
完全|wánquán|pho|hoàn toàn|我完全同意你的看法。~Tôi hoàn toàn đồng ý với quan điểm của bạn.
例如|lìrú|dong|ví dụ như|我喜欢很多运动，例如游泳和跑步。~Tôi thích nhiều môn thể thao, ví dụ bơi và chạy bộ.
不如|bùrú|dong|không bằng; chi bằng|坐公交车不如坐地铁快。~Đi xe buýt không nhanh bằng đi tàu điện ngầm.
细节|xìjié|dt|chi tiết|做事要注意细节。~Làm việc phải chú ý chi tiết.
答案|dá'àn|dt|đáp án|这道题的答案是什么？~Đáp án của câu này là gì?
职业|zhíyè|dt|nghề nghiệp|你对哪种职业感兴趣？~Bạn quan tâm đến nghề nghiệp nào?
"""),
texts=[dict(t="课文1", scene="李文来到陈天中的学校，跟他边走边聊。", scene_vi="Lý Văn đến trường của Trần Thiên Trung, vừa đi vừa trò chuyện với cậu.", narr=False, lines=T("""
陈天中>李文，期中考试后就再也没见过你了，你这段时间在忙什么呢？|Lý Văn, từ sau thi giữa kỳ là không gặp cậu nữa, dạo này cậu bận gì thế?
李文>我最近去一家医药公司应聘了，他们正在招聘实习生。|Dạo này mình đi ứng tuyển ở một công ty dược, họ đang tuyển thực tập sinh.
陈天中>你这么早就考虑实习了？|Cậu đã tính chuyện thực tập sớm vậy à?
李文>现在很多单位在招聘毕业生时，都很重视有没有实习经历，所以我想提前去锻炼一下，积累一些经验。|Bây giờ nhiều đơn vị khi tuyển sinh viên tốt nghiệp đều rất coi trọng có kinh nghiệm thực tập hay không, nên mình muốn đi rèn luyện trước, tích lũy chút kinh nghiệm.
陈天中>那现在有结果了吗？|Vậy giờ có kết quả chưa?
李文>我还在等消息，希望能有好结果。|Mình vẫn đang đợi tin, hy vọng sẽ có kết quả tốt.
"""), q=Q("""
李文最近在忙什么？|去公司应聘。|Đi ứng tuyển ở công ty.
很多单位招聘毕业生时，比较重视什么？|有没有实习经历。|Có kinh nghiệm thực tập hay không.
李文为什么现在就想去实习？|因为单位重视实习经历，他想提前去锻炼一下，积累一些经验。|Vì các đơn vị coi trọng kinh nghiệm thực tập, cậu muốn rèn luyện trước, tích lũy kinh nghiệm.
李文应聘成功了吗？|还不知道，他还在等消息。|Chưa biết, cậu vẫn đang đợi tin.
""")),
 dict(t="课文2", scene="在校园，陈天中和李文边走边聊。", scene_vi="Trong khuôn viên trường, Trần Thiên Trung và Lý Văn vừa đi vừa trò chuyện.", narr=False, lines=T("""
陈天中>李文，你是怎么应聘的？|Lý Văn, cậu ứng tuyển thế nào?
李文>我先在网上报名，填写个人信息，然后等公司通知我去参加笔试。|Mình đăng ký online trước, điền thông tin cá nhân, rồi đợi công ty báo đi thi viết.
陈天中>笔试都考些什么？|Thi viết thi những gì?
李文>主要是一些专业知识。考完没多久，他们就让我去面试了。|Chủ yếu là kiến thức chuyên ngành. Thi xong không lâu, họ gọi mình đi phỏng vấn.
陈天中>看来你笔试答得不错，那你面试得怎么样？|Xem ra cậu làm bài thi viết tốt, thế phỏng vấn thế nào?
李文>那天是由部门负责人来面试的，我有点儿紧张。他让我介绍了自己的学习经历、兴趣爱好和对工作的想法。|Hôm đó do trưởng bộ phận phỏng vấn, mình hơi căng thẳng. Anh ấy bảo mình giới thiệu quá trình học tập, sở thích và suy nghĩ về công việc.
陈天中>听起来挺正式的。|Nghe có vẻ khá trang trọng.
李文>是啊，我觉得这次经历很有用。不论结果怎么样，对我以后找工作肯定有帮助。|Đúng vậy, mình thấy trải nghiệm lần này rất hữu ích. Dù kết quả thế nào, chắc chắn sẽ giúp ích cho việc tìm việc sau này.
"""), q=Q("""
李文应聘时，第一步做的是什么？|在网上报名。|Đăng ký online.
公司的笔试主要考什么？|专业知识。|Kiến thức chuyên ngành.
李文面试的内容是什么？|介绍自己的学习经历、兴趣爱好和对工作的想法。|Giới thiệu quá trình học tập, sở thích và suy nghĩ về công việc.
李文觉得这次应聘经历怎么样？|很有用，对以后找工作肯定有帮助。|Rất hữu ích, chắc chắn giúp ích cho việc tìm việc sau này.
""")),
 dict(t="课文3", scene="在家里，李文收到了公司发来的短信。", scene_vi="Ở nhà, Lý Văn nhận được tin nhắn của công ty.", narr=True, lines=T("""
一天下午，李文突然收到一条短信，说他通过了面试，让他下周一到公司实习。|Một buổi chiều, Lý Văn bất ngờ nhận được tin nhắn báo cậu đã qua vòng phỏng vấn, thứ Hai tuần sau đến công ty thực tập.
李文看到信息后，激动得把手机扔到床上，在屋子里跳了起来。|Đọc tin xong, Lý Văn phấn khích đến mức ném điện thoại lên giường, nhảy cẫng lên trong phòng.
之后的几天，李文忙着做各种准备。|Mấy ngày sau đó, Lý Văn bận rộn chuẩn bị đủ thứ.
为了给大家留个好印象，他去理发店把头发理了理，又去商店买了一身正式的衣服，还打算在镜子前把自我介绍练一练。|Để để lại ấn tượng tốt với mọi người, cậu đi tiệm cắt tóc sửa sang lại tóc, lại đi cửa hàng mua một bộ quần áo trang trọng, còn định luyện phần tự giới thiệu trước gương.
在他看来，这次实习是一个新的开始。|Theo cậu, lần thực tập này là một khởi đầu mới.
他希望不仅能够运用专业知识完成任务，还能够积累更多经验，为将来找工作打下基础。|Cậu hy vọng không chỉ vận dụng được kiến thức chuyên ngành để hoàn thành nhiệm vụ, mà còn tích lũy thêm kinh nghiệm, đặt nền móng cho việc tìm việc sau này.
"""), q=Q("""
李文收到的短信内容是什么？|他通过了面试，下周一到公司实习。|Cậu đã qua phỏng vấn, thứ Hai tuần sau đến công ty thực tập.
李文看到信息后做什么了？|激动得把手机扔到床上，在屋子里跳了起来。|Phấn khích ném điện thoại lên giường, nhảy cẫng lên trong phòng.
李文做了什么准备？|去理发，买了一身正式的衣服，还打算练习自我介绍。|Đi cắt tóc, mua bộ quần áo trang trọng, định luyện tự giới thiệu.
李文是怎么看这次实习的？|是一个新的开始。|Là một khởi đầu mới.
""")),
 dict(t="课文4", scene="实习的收获", scene_vi="Thu hoạch từ thực tập", narr=True, lines=T("""
在中国，很多大学生在毕业前都会去实习。实习的地方有公司、工厂，也有学校和医院。|Ở Trung Quốc, nhiều sinh viên đi thực tập trước khi tốt nghiệp. Nơi thực tập có công ty, nhà máy, cũng có trường học và bệnh viện.
学生们通过实习，可以积累工作经验，熟悉工作内容和单位的管理规定，提前了解并适应社会。|Qua thực tập, sinh viên có thể tích lũy kinh nghiệm làm việc, làm quen với nội dung công việc và quy định quản lý của đơn vị, sớm hiểu và thích nghi với xã hội.
在实习中，学生常常会发现，课堂上学到的知识和实际工作并不完全一样。|Trong quá trình thực tập, sinh viên thường phát hiện kiến thức học trên lớp và công việc thực tế không hoàn toàn giống nhau.
例如：有些事情，在课本上学不如自己做一遍，因为只有在做的时候，才会发现有很多细节需要注意；|Ví dụ: có những việc học trong sách không bằng tự làm một lần, vì chỉ khi làm mới phát hiện có nhiều chi tiết cần chú ý;
还有一些问题，在书上找不到答案，只能通过日常工作慢慢理解。|còn có những vấn đề không tìm được đáp án trong sách, chỉ có thể dần hiểu ra qua công việc hằng ngày.
在这样的过程中，学生能够对学到的知识有更好的认识，也更清楚自己的职业发展方向。|Trong quá trình đó, sinh viên có thể hiểu rõ hơn kiến thức đã học, cũng rõ hơn về hướng phát triển nghề nghiệp của mình.
"""), q=Q("""
为什么很多大学生要去实习？|可以积累工作经验，提前了解并适应社会。|Có thể tích lũy kinh nghiệm, sớm hiểu và thích nghi với xã hội.
通过实习，学生可以学到什么？|积累工作经验，熟悉工作内容和单位的管理规定。|Tích lũy kinh nghiệm, làm quen nội dung công việc và quy định của đơn vị.
为什么说有些事情需要自己做一遍？|因为只有在做的时候，才会发现有很多细节需要注意。|Vì chỉ khi làm mới phát hiện nhiều chi tiết cần chú ý.
在实习中，学生们会有什么发现？|课堂上学到的知识和实际工作并不完全一样。|Kiến thức trên lớp và công việc thực tế không hoàn toàn giống nhau.
""")),
],
grammar=[
 G("zaiyebu", "固定格式“再也不/没……”", "Cấu trúc cố định “再也不 / 没……”",
   "“再也不” biểu thị trong tương lai sẽ không xảy ra việc gì đó nữa; “再也没” biểu thị từ quá khứ đến hiện tại việc đó không xảy ra lại lần nào: “không bao giờ… nữa / từ đó không… nữa”.",
   [F("S:Chủ ngữ|kw:再也|D:不 / 没|V:Vị ngữ", [
     ("期中考试后就|[再也]|没|见过你了", "。", "Từ sau thi giữa kỳ là không gặp lại cậu nữa."),
     ("对不起，我以后|[再也]|不|迟到了", "。", "Xin lỗi, sau này tôi sẽ không bao giờ đến muộn nữa."),
     ("我出国以后就|[再也]|没|给他打过电话", "。", "Từ khi ra nước ngoài, tôi không gọi điện cho anh ấy lần nào nữa.")])]),
 G("you", "介词“由”", "Giới từ “由”",
   "Trong bài này, giới từ “由” dùng để dẫn ra người thực hiện hành động: “do (ai)…”.",
   [F("S:(Chủ ngữ)|kw:由|N:Người thực hiện|V:Hành động", [
     ("那天是|[由]|部门负责人|来面试的", "，我有点儿紧张。", "Hôm đó do trưởng bộ phận phỏng vấn, tôi hơi căng thẳng."),
     ("这个问题究竟|[由]|谁|来负责解决", "？", "Vấn đề này rốt cuộc do ai phụ trách giải quyết?"),
     ("这次活动是|[由]|他们公司|来安排的", "。", "Hoạt động lần này do công ty họ sắp xếp.")])]),
 G("ba_vv", "“把”字句“主语+把+宾语+动词（+一/了）+动词”", "Câu chữ “把”: Chủ ngữ + 把 + Tân ngữ + Động từ (+一/了) + Động từ",
   "Trong câu chữ “把” này, động từ có thể lặp lại theo dạng “VV”, “V一V” hoặc “V了V”, biểu thị hành động diễn ra trong thời gian ngắn, mức độ nhẹ.",
   [F("S:Chủ ngữ|kw:把|O:Tân ngữ|V:V(一/了)V", [
     ("他去理发店|[把]|头发|理了理", "。", "Cậu ấy đến tiệm cắt tóc sửa sang lại tóc."),
     ("你先|[把]|作业|检查检查", "，然后再交给老师。", "Bạn kiểm tra lại bài tập trước, rồi hãy nộp cho thầy cô."),
     ("上课前，我|[把]|今天要学习的内容|看了看", "。", "Trước giờ học, tôi xem qua nội dung hôm nay sẽ học.")])]),
 G("buru", "比较句“A不如B（+形容词）”", "Câu so sánh “A 不如 B (+ tính từ)”",
   "“A 不如 B” biểu thị A không tốt bằng B. Nếu trong câu có tính từ, thì biểu thị A về mặt đó kém hơn B: “A không… bằng B”.",
   [F("A:A|kw:不如|B:B|X:(Tính từ)", [
     ("有些事情，在课本上学|[不如]|自己做一遍|", "。", "Có những việc học trong sách không bằng tự mình làm một lần."),
     ("这家店|[不如]|那家店|环境好", "。", "Cửa hàng này môi trường không tốt bằng cửa hàng kia."),
     ("我觉得坐公交|[不如]|坐地铁|方便", "。", "Tôi thấy đi xe buýt không tiện bằng đi tàu điện ngầm.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["考虑", "笔试", "不论", "消息", "肯定", "负责人"], [
   "你这么努力，这次考试【肯定】能通过。", "您有什么问题，可以直接跟【负责人】联系。", "【不论】你同不同意，我都会按照计划去做。",
   "这件事比较重要，我需要再认真【考虑】一下。", "我们要先进行【笔试】，了解一下大家的专业能力。", "我已经等了好几天了，还是没有收到他的【消息】。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["能够", "理发", "答案", "工厂", "激动", "职业"], [
   "A：你知道这道题的【答案】吗？ B：知道，我已经写在纸上了。", "A：听说你获得奖学金了？ B：是的，我【激动】得昨天晚上都没睡好。",
   "A：你现在中文说得怎么样了？ B：我已经【能够】和中国朋友进行简单交流了。", "A：下午我去【理发】，你想跟我一起去吗？ B：好啊，我最近头发有点儿长了，正好下午有时间。",
   "A：你对自己的【职业】发展有什么打算？ B：我希望先去大公司工作，积累一些经验，然后自己开一家公司。", "A：听说你哥哥换工作了，他现在在哪儿工作？ B：他现在在一家【工厂】工作，主要负责检查产品的质量。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["面试结束后", "练习介绍自己的学习经历", "不仅让他了解了应聘的过程", "他在网上看到了几条招聘信息"], [
   "王明是一名大三学生，最近正在找实习机会。【他在网上看到了几条招聘信息】，选了一家自己感兴趣的单位报名。为了顺利通过面试，他提前准备了很多内容，比如了解公司的情况，【练习介绍自己的学习经历】。面试那天，他刚开始有点儿紧张，不过慢慢放松了一些。【面试结束后】，他觉得自己的表现没有那么好。虽然最后没有通过面试，但是他认为这次应聘的经历很有用，【不仅让他了解了应聘的过程】，也让他在交流方面更有信心了。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l15", items=[
   ("扔", "他把瓶子扔进了垃圾桶。"), ("答案", "这道题她想了很久，还是不知道答案。"), ("激动", "他看到手机上的消息，激动得叫了起来。")]),
])
