# -*- coding: utf-8 -*-
# HSK 4下 – Bài 11: 活到老学到老
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[11] = dict(zh="活到老学到老", vi="Sống đến già, học đến già",
intro="Lý Văn và Bạch Gia Nguyệt nói về cuộc sống phong phú của người cao tuổi; các bạn bàn về lớp học số và việc tự học online; nhà Vương Nhất Tuyết thay đổi cách giáo dục con; bài cuối bàn về tinh thần “học không biết chán”.",
vocab=V("""
老年|lǎonián|dt|tuổi già, người cao tuổi|她每周去老年大学学画画。~Mỗi tuần bà ấy đến trường đại học người cao tuổi học vẽ.
散步|sànbù|dong|đi dạo, tản bộ|吃完晚饭我们常去公园散步。~Ăn tối xong chúng tôi thường ra công viên đi dạo.
丰富|fēngfù|tt|phong phú|这家图书馆的书很丰富。~Sách của thư viện này rất phong phú.
羡慕|xiànmù|dong|ngưỡng mộ, ghen tị|大家都很羡慕他找到了好工作。~Mọi người đều ngưỡng mộ anh ấy tìm được việc tốt.
即使|jíshǐ|lien|cho dù, dù cho|即使很累，她也每天坚持跑步。~Dù rất mệt, ngày nào cô ấy cũng kiên trì chạy bộ.
活|huó|dong|sống; sinh động; công việc|这棵树种了三年，还活得很好。~Cây này trồng ba năm rồi, vẫn sống rất tốt.
继续|jìxù|dong|tiếp tục|休息一下，我们继续上课。~Nghỉ một chút rồi chúng ta tiếp tục học.
网友|wǎngyǒu|dt|bạn trên mạng|他在网上认识了很多网友。~Anh ấy quen nhiều bạn trên mạng.
无聊|wúliáo|tt|chán, buồn tẻ|周末一个人在家有点儿无聊。~Cuối tuần ở nhà một mình hơi chán.
太极拳|Tàijíquán|rieng|Thái cực quyền|爷爷每天早上打太极拳。~Sáng nào ông cũng tập Thái cực quyền.
数字|shùzì|tt|kỹ thuật số; con số|学校新建了一个数字教室。~Trường mới xây một phòng học số.
点名|diǎnmíng|dong|điểm danh|老师上课前先点名。~Trước giờ học thầy giáo điểm danh.
教授|jiàoshòu|dt|giáo sư|王教授在大学教历史。~Giáo sư Vương dạy lịch sử ở đại học.
线上|xiànshàng|dt|trực tuyến, online|今天的会议在线上开。~Cuộc họp hôm nay họp online.
线下|xiànxià|dt|trực tiếp, offline|线上线下的课我都上过。~Lớp online và lớp trực tiếp tôi đều học rồi.
视频|shìpín|dt|video|她喜欢在网上看做饭的视频。~Cô ấy thích xem video nấu ăn trên mạng.
记录|jìlù|dt|bản ghi, ghi chép; ghi lại|我把会议的内容都记录下来了。~Tôi đã ghi lại hết nội dung cuộc họp.
资料|zīliào|dt|tài liệu|写论文需要查很多资料。~Viết luận văn cần tra rất nhiều tài liệu.
自学|zìxué|dong|tự học|他自学了三年日语。~Anh ấy tự học tiếng Nhật ba năm.
口语|kǒuyǔ|dt|khẩu ngữ, kỹ năng nói|多和中国人聊天儿能提高口语。~Trò chuyện nhiều với người Trung Quốc có thể nâng cao kỹ năng nói.
科技|kējì|dt|khoa học kỹ thuật, công nghệ|科技让生活越来越方便。~Công nghệ làm cuộc sống ngày càng tiện lợi.
获取|huòqǔ|dong|thu được, lấy được|现在上网获取信息很容易。~Bây giờ lên mạng lấy thông tin rất dễ.
礼貌|lǐmào|dt|lễ phép, lịch sự|这个孩子很有礼貌。~Đứa trẻ này rất lễ phép.
打招呼|dǎ zhāohu|dong|chào hỏi|见到老师要打招呼。~Gặp thầy cô phải chào hỏi.
家长|jiāzhǎng|dt|phụ huynh|明天学校开家长会。~Ngày mai trường họp phụ huynh.
成功|chénggōng|tt|thành công|祝你这次比赛成功！~Chúc bạn thi đấu lần này thành công!
分数|fēnshù|dt|điểm số|这次考试的分数还没出来。~Điểm thi lần này vẫn chưa có.
目的|mùdì|dt|mục đích|你学中文的目的是什么？~Mục đích bạn học tiếng Trung là gì?
养成|yǎngchéng|dong|hình thành, tập thành (thói quen)|她从小养成了早起的习惯。~Từ nhỏ cô ấy đã tập được thói quen dậy sớm.
留|liú|dong|để lại, dành ra; ở lại|请给我留一个座位。~Hãy để lại cho tôi một chỗ ngồi.
做法|zuòfǎ|dt|cách làm|我觉得你的做法很好。~Tôi thấy cách làm của bạn rất hay.
棒|bàng|tt|giỏi, tuyệt|你的中文说得真棒！~Bạn nói tiếng Trung giỏi thật!
一生|yìshēng|dt|cả đời, một đời|他一生都在研究汉字。~Cả đời ông ấy nghiên cứu chữ Hán.
快速|kuàisù|tt|nhanh chóng, tốc độ cao|这个城市发展得很快速。~Thành phố này phát triển rất nhanh.
优秀|yōuxiù|tt|xuất sắc, ưu tú|她是我们班最优秀的学生。~Cô ấy là học sinh xuất sắc nhất lớp chúng tôi.
律师|lǜshī|dt|luật sư|他的理想是当一名律师。~Ước mơ của anh ấy là làm luật sư.
仍|réng|pho|vẫn, vẫn còn|下雨了，比赛仍在进行。~Trời mưa rồi, trận đấu vẫn đang tiếp tục.
准时|zhǔnshí|tt|đúng giờ|飞机准时起飞了。~Máy bay đã cất cánh đúng giờ.
网页|wǎngyè|dt|trang web|这个网页打不开。~Trang web này không mở được.
弹|tán|dong|đánh, chơi (đàn)|她会弹钢琴。~Cô ấy biết chơi piano.
钢琴|gāngqín|dt|đàn piano|我从小就学钢琴。~Tôi học piano từ nhỏ.
重新|chóngxīn|pho|lại, làm lại từ đầu|这篇作文写得不好，我要重新写。~Bài văn này viết chưa tốt, tôi phải viết lại.
孔子|Kǒngzǐ|rieng|Khổng Tử|孔子是中国古代有名的教育家。~Khổng Tử là nhà giáo dục nổi tiếng thời cổ đại Trung Quốc.
"""),
texts=[dict(t="课文1", scene="李文和白家月在公园里散步聊天儿。", scene_vi="Lý Văn và Bạch Gia Nguyệt đi dạo, trò chuyện trong công viên.", narr=False, lines=T("""
白家月>这里的老年人真不少。|Ở đây người cao tuổi đông thật.
李文>嗯，住在附近的老年人都会来这儿，有的散步，有的唱歌、跳舞，还有的打太极拳。|Ừ, người cao tuổi sống gần đây đều đến chỗ này, có người đi dạo, có người hát, nhảy múa, còn có người tập Thái cực quyền.
白家月>他们的生活真丰富，让人羡慕。|Cuộc sống của họ thật phong phú, khiến người ta ngưỡng mộ.
李文>是的。有些人即使年龄大了，也坚持去老年班学习。|Đúng vậy. Có những người dù tuổi đã cao vẫn kiên trì đến lớp người cao tuổi để học.
白家月>真是活到老学到老啊。|Đúng là sống đến già học đến già.
李文>对，我爷爷就每周都去老年班学电脑。他总说，老年人也要继续学习，“你看，我都七八十岁了，还上网和网友们聊天儿呢，生活一点儿都不无聊。”|Đúng, ông mình tuần nào cũng đến lớp người cao tuổi học máy tính. Ông luôn nói người già cũng phải tiếp tục học: “Cháu xem, ông bảy tám chục tuổi rồi mà vẫn lên mạng trò chuyện với bạn mạng đấy, cuộc sống chẳng chán chút nào.”
"""), q=Q("""
白家月觉得公园里老年人的生活怎么样？|很丰富，让人羡慕。|Rất phong phú, khiến người ta ngưỡng mộ.
在公园里，老年人都会做些什么活动？|有的散步，有的唱歌、跳舞，还有的打太极拳。|Có người đi dạo, có người hát, nhảy múa, có người tập Thái cực quyền.
李文的爷爷每周去老年班做什么？|学电脑。|Học máy tính.
李文的爷爷为什么去老年班学习？|因为他觉得老年人也要继续学习。|Vì ông cho rằng người già cũng phải tiếp tục học.
""")),
 dict(t="课文2", scene="在餐馆，李文请白家月、安妮一起吃饭。", scene_vi="Ở nhà hàng, Lý Văn mời Bạch Gia Nguyệt và Annie ăn cơm.", narr=False, lines=T("""
安妮>家月，我们今天的课是在数字教室上的，感觉挺不一样的。|Gia Nguyệt, hôm nay chúng mình học ở phòng học số, cảm giác khá khác.
白家月>是的，数字教室可以拍照点名，教授在线上点名，不用像线下那样一个个叫名字，特别节约时间。|Đúng vậy, phòng học số có thể chụp ảnh điểm danh, giáo sư điểm danh online, không cần gọi tên từng người như lớp trực tiếp, rất tiết kiệm thời gian.
李文>最方便的是，课上没听明白时，课后还能在学校网站上找到视频记录看。|Tiện nhất là lúc trên lớp chưa hiểu, sau giờ học còn có thể tìm video ghi lại trên trang web của trường để xem.
安妮>对，上课我都不用着急记笔记了。|Đúng, trên lớp mình cũng không cần vội ghi chép nữa.
李文>不仅数字教室很方便，现在网上到处是学习资料，想查什么都能查到，自学也更方便了。|Không chỉ phòng học số tiện lợi, bây giờ trên mạng đâu đâu cũng có tài liệu học tập, muốn tra gì cũng tra được, tự học cũng tiện hơn.
白家月>是的，只要有手机或电脑，我就是不在教室，也可以学习中文，和同学一起练口语。|Đúng vậy, chỉ cần có điện thoại hoặc máy tính, dù không ở lớp mình vẫn có thể học tiếng Trung, luyện nói cùng các bạn.
安妮>科技真是让获取知识变得简单多了。|Công nghệ thật sự khiến việc tiếp thu kiến thức đơn giản hơn nhiều.
"""), q=Q("""
白家月认为线上点名怎么样？|特别节约时间。|Rất tiết kiệm thời gian.
对安妮来说，线上上课时，自己不用急着做的事情是什么？|记笔记。|Ghi chép.
李文说，线上上课时，如果没听懂，课后还可以怎么做？|在学校网站上找到视频记录看。|Tìm video ghi lại trên trang web của trường để xem.
人们自学为什么变得越来越方便了？|因为网上到处是学习资料，想查什么都能查到。|Vì trên mạng đâu cũng có tài liệu học tập, muốn tra gì cũng được.
""")),
 dict(t="课文3", scene="周六，白家月和李文去王一雪家玩。回来后，白家月在家写日记。", scene_vi="Thứ Bảy, Bạch Gia Nguyệt và Lý Văn đến nhà Vương Nhất Tuyết chơi. Về nhà, Bạch Gia Nguyệt viết nhật ký.", narr=True, lines=T("""
今天星期六，我们去了一雪姐姐家。|Hôm nay thứ Bảy, chúng tôi đến nhà chị Nhất Tuyết.
姐姐家的两个孩子很有礼貌，我们一进门，就马上和我们打招呼。|Hai đứa con nhà chị rất lễ phép, chúng tôi vừa vào cửa là chúng chào hỏi ngay.
在姐姐家，我们也聊到了孩子的教育。|Ở nhà chị, chúng tôi cũng nói chuyện về việc giáo dục con cái.
姐姐说，以前他们和很多家长一样，觉得孩子上个好大学，人生才是成功的。|Chị nói, trước đây anh chị cũng như nhiều phụ huynh khác, cho rằng con vào được trường đại học tốt thì cuộc đời mới thành công.
所以，他们只关心孩子的分数，结果孩子压力特别大，每天都很不开心。|Vì vậy, anh chị chỉ quan tâm điểm số của con, kết quả là con chịu áp lực rất lớn, ngày nào cũng không vui.
后来，他们认识到，教育的目的不是让孩子考高分，而是帮助孩子养成好习惯。|Sau này, anh chị nhận ra mục đích của giáo dục không phải là để con thi được điểm cao, mà là giúp con hình thành thói quen tốt.
于是，他们做出改变，每天都给孩子留出时间外出锻炼身体，或者看些自己感兴趣的书。|Thế là anh chị thay đổi, mỗi ngày đều dành thời gian cho con ra ngoài rèn luyện thân thể, hoặc đọc những cuốn sách con thích.
我觉得他们的做法真棒。|Tôi thấy cách làm của anh chị thật tuyệt.
"""), q=Q("""
以前，王一雪和刘明认为孩子的人生怎样才是成功的？|孩子上个好大学，人生才是成功的。|Con vào được đại học tốt thì cuộc đời mới thành công.
以前，王一雪的孩子为什么不开心？|因为父母只关心孩子的分数，孩子压力特别大。|Vì bố mẹ chỉ quan tâm điểm số, con chịu áp lực rất lớn.
后来，王一雪和刘明认为教育是为了让孩子怎么样？|养成好习惯。|Hình thành thói quen tốt.
王一雪和刘明做出了什么样的改变？|每天都给孩子留出时间外出锻炼身体，或者看些自己感兴趣的书。|Mỗi ngày dành thời gian cho con ra ngoài rèn luyện hoặc đọc sách con thích.
""")),
 dict(t="课文4", scene="学习，让生活更有意义", scene_vi="Học tập khiến cuộc sống ý nghĩa hơn", narr=True, lines=T("""
“学而不厌”是两千多年前中国教育家孔子说过的话，意思是人要一直坚持学习，|“Học nhi bất yếm” là câu nói của nhà giáo dục Khổng Tử hơn hai nghìn năm trước, ý là con người phải luôn kiên trì học tập,
就是说，学习是人一生的事情，要活到老学到老。|nghĩa là học tập là việc cả đời, phải sống đến già học đến già.
在世界快速变化的今天，“学而不厌”变得更加重要。|Ngày nay khi thế giới thay đổi nhanh chóng, “học không biết chán” càng trở nên quan trọng.
我有一位很优秀的律师朋友，他一直在学习新的法律知识。|Tôi có một người bạn luật sư rất xuất sắc, anh ấy luôn học kiến thức pháp luật mới.
他说，这不仅是律师的要求和责任，也是提高自己能力的重要方法。|Anh ấy nói đây không chỉ là yêu cầu và trách nhiệm của luật sư, mà còn là cách quan trọng để nâng cao năng lực bản thân.
同时我也认为，人就是不再工作了，坚持学习仍很重要。|Đồng thời tôi cũng cho rằng, dù con người không còn đi làm nữa, kiên trì học tập vẫn rất quan trọng.
就像我爷爷，虽然七十多岁了，每天还准时去老年大学上课，学习做网页、弹钢琴。|Giống như ông tôi, tuy đã hơn bảy mươi tuổi, ngày nào cũng đúng giờ đến trường đại học người cao tuổi học làm trang web, chơi piano.
他说，重新当一回学生，生活更有意思了，也感觉自己变年轻了。|Ông nói, được làm học sinh lại một lần nữa, cuộc sống thú vị hơn, cũng cảm thấy mình trẻ lại.
"""), q=Q("""
“学而不厌”是孔子什么时候说的？|两千多年前。|Hơn hai nghìn năm trước.
“活到老学到老”是什么意思？|学习是人一生的事情，要一直坚持学习。|Học tập là việc cả đời, phải luôn kiên trì học.
那位律师为什么一直坚持学习法律知识？|因为这不仅是律师的要求和责任，也是提高自己能力的重要方法。|Vì đó không chỉ là yêu cầu, trách nhiệm của luật sư mà còn là cách nâng cao năng lực.
坚持学习，爷爷觉得怎么样？|生活更有意思了，也感觉自己变年轻了。|Cuộc sống thú vị hơn, cảm thấy mình trẻ lại.
""")),
],
grammar=[
 G("jishi", "让步复句“即使……，也……”", "Câu phức nhượng bộ “即使……，也……”",
   "Vế trước nêu một giả thiết (thường là tình huống bất lợi hoặc cực đoan), vế sau cho biết kết quả không thay đổi, không bị ảnh hưởng: “cho dù… thì vẫn…”.",
   [F("S:(Chủ ngữ)|kw:即使|X:Giả thiết|kw2:也|V:Kết quả không đổi", [
     ("有些人|[即使]|年龄大了|[也]|坚持去老年班学习", "。", "Có những người dù tuổi đã cao vẫn kiên trì đến lớp người cao tuổi học."),
     ("|[即使]|明天下大雨|我们[也]|会按时出发", "。", "Cho dù mai mưa to, chúng ta vẫn sẽ xuất phát đúng giờ."),
     ("|[即使]|大家都说很难|我[也]|要试一试", "。", "Dù mọi người đều nói khó, tôi vẫn muốn thử.")])]),
 G("jiushi", "让步复句“就是……，也……”", "Câu phức nhượng bộ “就是……，也……”",
   "“就是” ở đây là liên từ, cấu trúc thường dùng trong khẩu ngữ. Vế trước nêu giả thiết cực đoan hoặc điều kiện nhượng bộ, vế sau cho biết dù vậy kết quả vẫn không đổi, hoặc vẫn giữ thái độ, hành động nào đó: “dù cho… cũng…”.",
   [F("S:(Chủ ngữ)|kw:就是|X:Giả thiết|kw2:也|V:Kết quả / thái độ", [
     ("我|[就是]|不在教室|[也]|可以学习中文，和同学一起练口语", "。", "Dù không ở lớp mình vẫn có thể học tiếng Trung, luyện nói với bạn bè."),
     ("锻炼身体很重要，|[就是]|再忙|[也]|要坚持运动", "。", "Rèn luyện thân thể rất quan trọng, dù bận mấy cũng phải kiên trì vận động."),
     ("明天开会需要这份材料，我|[就是]|今晚不睡觉|[也]|要把它改完", "。", "Mai họp cần tài liệu này, dù tối nay không ngủ tôi cũng phải sửa xong nó.")])]),
 G("bushi_ershi", "并列复句“不是……，而是……”", "Câu phức đẳng lập “不是……，而是……”",
   "Phủ định vế trước, khẳng định vế sau, nhấn mạnh sự khác biệt hoặc đối lập giữa hai vế: “không phải… mà là…”.",
   [F("S:Chủ ngữ|kw:不是|X:Điều bị phủ định|kw2:而是|V:Điều được khẳng định", [
     ("教育的目的|[不是]|让孩子考高分|[而是]|帮助孩子养成好习惯", "。", "Mục đích của giáo dục không phải để con thi điểm cao, mà là giúp con hình thành thói quen tốt."),
     ("我|[不是]|想喝茶|[而是]|想喝水", "。", "Tôi không phải muốn uống trà, mà là muốn uống nước."),
     ("我放学后|[不是]|直接回家|[而是]|先去超市买笔", "。", "Tan học tôi không về nhà ngay, mà đi siêu thị mua bút trước.")])]),
 G("jiushishuo", "固定短语“就是说”", "Cụm từ cố định “就是说”",
   "“就是说” dùng để giải thích thêm nội dung phía trước, diễn đạt lại theo cách khác cho rõ hơn: “nghĩa là, tức là”.",
   [F("X:Nội dung trước|kw:就是说|V:Giải thích lại", [
     ("人要一直坚持学习|[就是说]|学习是人一生的事情，要活到老学到老", "。", "Con người phải luôn kiên trì học tập, nghĩa là học tập là việc cả đời, phải sống đến già học đến già."),
     ("别着急写|[就是说]|别着急动笔，想好后再写", "。", "Đừng vội viết, tức là đừng vội cầm bút, nghĩ kỹ rồi hãy viết."),
     ("这份工作的工资是根据你工作的完成情况来发的|[就是说]|你完成得越多，工资越高", "。", "Lương của công việc này trả theo mức hoàn thành công việc, nghĩa là bạn làm được càng nhiều thì lương càng cao.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["一生", "打招呼", "丰富", "留", "弹", "优秀"], [
   "即使每天工作很忙，我也会【留】出时间读书。", "我刚坐下，她就过来和我【打招呼】。", "他【一生】只做了一件事，那就是研究数学，最后他成为了一位很有名的数学家。",
   "小雪很喜欢【弹】钢琴，每天都会练习至少两个小时。", "他非常【优秀】，把任务交给他，我很放心。", "老王工作三十年了，有很【丰富】的工作经验，这个问题他能解决。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["羡慕", "礼貌", "律师", "数字", "继续", "口语"], [
   "A：你们还要【继续】加班吗？ B：对，今天必须要把这些货全部发出去。", "A：你觉得怎样才能学好外语？ B：我自己学外语的经验是，开始学习时要特别重视【口语】，多听多说。",
   "A：你女儿真有【礼貌】。 B：谢谢，从小我们就教她要尊重别人，得到别人的帮助时，要说“谢谢”。", "A：你们做【律师】的，平时工作一定很忙吧？ B：也不一定，有时候周末也不能休息，有时候就能按时下班。",
   "A：姐姐，我太【羡慕】你的工作了！从来不加班，而且工资高。 B：可是我们经常出差，很累的。", "A：真是【数字】社会啊，我要的信息马上就查到了。 B：是啊，不仅是查资料，现在很多事情也都可以在网上解决了。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["还可以直接给大家放视频", "第一个进教室的人", "老师和学生都觉得方便", "上课时"], [
   "现在有了数字教室，上课方式和以前大不相同了。【第一个进教室的人】，只要按下门口的“上课”，灯和空调就会自己打开，不用一个一个去开。【上课时】，用到的“黑板”是一块能上网的电子屏幕，老师不仅可以在上面写字，【还可以直接给大家放视频】。数字教室里的桌椅也分成几个小组，小组里的人聚在一起，都能互相看到对方，这样方便大家交流。这些变化让上课方式丰富了不少，【老师和学生都觉得方便】，所以数字教室很受欢迎。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l11", items=[
   ("老年人", "这两位老年人身体很好，每天都很开心。"), ("准时", "这班飞机准时起飞了。"), ("散步", "傍晚，他们手拉着手在河边散步。")]),
])
