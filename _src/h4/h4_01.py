# -*- coding: utf-8 -*-
# HSK 4上 – Bài 1: 我们来中国学习了
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[1] = dict(zh="我们来中国学习了", vi="Chúng tôi đến Trung Quốc học rồi",
intro="Bạch Gia Nguyệt và Trần Thiên Trung làm thủ tục nhập học ở một trường đại học Trung Quốc, tìm hiểu học bổng, cuộc sống du học và nói về chuyên ngành, dự định nghề nghiệp sau này.",
vocab=V("""
签证|qiānzhèng|dt|thị thực, visa|去中国留学要先办签证。~Đi du học Trung Quốc phải làm visa trước.
入学|rùxué|dong|nhập học|我是去年九月入学的。~Tôi nhập học vào tháng Chín năm ngoái.
通知|tōngzhī|dong|thông báo; giấy báo|老师通知我们明天不上课。~Thầy giáo thông báo ngày mai chúng tôi không học.
证件|zhèngjiàn|dt|giấy tờ (tùy thân)|请带好你的证件。~Vui lòng mang theo giấy tờ của bạn.
材料|cáiliào|dt|tài liệu, hồ sơ; vật liệu|申请奖学金要准备很多材料。~Xin học bổng phải chuẩn bị nhiều hồ sơ.
证|zhèng|dt|thẻ, giấy chứng nhận|这是我的学生证。~Đây là thẻ sinh viên của tôi.
任何|rènhé|dai|bất kỳ, bất cứ|有任何问题都可以问我。~Có bất kỳ vấn đề gì cũng có thể hỏi tôi.
食堂|shítáng|dt|nhà ăn, căng tin|我们中午在食堂吃饭。~Buổi trưa chúng tôi ăn cơm ở căng tin.
座|zuò|lg|tòa, ngọn (lượng từ cho núi, nhà...)|那儿有一座很高的山。~Ở đó có một ngọn núi rất cao.
申请|shēnqǐng|dong|xin, nộp đơn xin|我想申请去中国留学。~Tôi muốn nộp đơn đi du học Trung Quốc.
奖学金|jiǎngxuéjīn|dt|học bổng|她获得了学校的奖学金。~Cô ấy đã nhận được học bổng của trường.
表现|biǎoxiàn|dong|biểu hiện, thể hiện|他在比赛中表现得很好。~Anh ấy thể hiện rất tốt trong cuộc thi.
获得|huòdé|dong|đạt được, giành được|我们班获得了第一名。~Lớp chúng tôi giành được giải nhất.
要是|yàoshi|lien|nếu, nếu như|要是明天下雨，我们就不去了。~Nếu ngày mai mưa thì chúng ta không đi nữa.
减轻|jiǎnqīng|dong|giảm nhẹ, làm nhẹ bớt|运动可以减轻压力。~Vận động có thể giảm bớt áp lực.
经济|jīngjì|dt|kinh tế; tài chính|这几年这个城市的经济发展很快。~Mấy năm nay kinh tế thành phố này phát triển rất nhanh.
压力|yālì|dt|áp lực|最近工作压力很大。~Dạo này áp lực công việc rất lớn.
加油|jiāyóu|dong|cố lên, cố gắng|明天考试，加油！~Mai thi rồi, cố lên nhé!
随着|suízhe|gioi|cùng với, theo đà|随着天气变冷，穿毛衣的人多了。~Theo đà trời lạnh đi, người mặc áo len nhiều hơn.
课程|kèchéng|dt|môn học, khóa học|这学期我有五门课程。~Học kỳ này tôi có năm môn học.
专业|zhuānyè|dt|chuyên ngành; chuyên nghiệp|你学的是什么专业？~Bạn học chuyên ngành gì?
本科|běnkē|dt|đại học (hệ chính quy, cử nhân)|我姐姐本科学的是经济。~Chị tôi học đại học ngành kinh tế.
硕士|shuòshì|dt|thạc sĩ|他正在读硕士。~Anh ấy đang học thạc sĩ.
研究生|yánjiūshēng|dt|nghiên cứu sinh, học viên cao học|她打算明年考研究生。~Cô ấy dự định năm sau thi cao học.
博士|bóshì|dt|tiến sĩ|王老师是语言学博士。~Thầy Vương là tiến sĩ ngôn ngữ học.
研究|yánjiū|dong|nghiên cứu|他在研究中国历史。~Anh ấy đang nghiên cứu lịch sử Trung Quốc.
活动|huódòng|dt|hoạt động|周末学校有很多活动。~Cuối tuần trường có nhiều hoạt động.
通过|tōngguò|gioi|thông qua; vượt qua|通过这次旅游，我认识了很多朋友。~Thông qua chuyến du lịch này, tôi quen được nhiều bạn.
交流|jiāoliú|dong|giao lưu, trao đổi|我常常跟中国朋友用中文交流。~Tôi thường giao lưu với bạn Trung Quốc bằng tiếng Trung.
适应|shìyìng|dong|thích ứng, thích nghi|你适应这里的生活了吗？~Bạn đã thích nghi với cuộc sống ở đây chưa?
将来|jiānglái|dt|tương lai, sau này|你将来想做什么工作？~Sau này bạn muốn làm công việc gì?
国际|guójì|tt|quốc tế|她在一家国际公司工作。~Cô ấy làm việc ở một công ty quốc tế.
当|dāng|dong|làm, đảm nhận (vai trò)|我想当一名老师。~Tôi muốn làm giáo viên.
教育|jiàoyù|dt|giáo dục|父母的教育对孩子很重要。~Sự giáo dục của bố mẹ rất quan trọng với con cái.
成为|chéngwéi|dong|trở thành|我们成为了好朋友。~Chúng tôi đã trở thành bạn tốt.
教师|jiàoshī|dt|giáo viên|她是一名中学教师。~Cô ấy là một giáo viên trung học.
贸易|màoyì|dt|thương mại, mậu dịch|他做国际贸易工作。~Anh ấy làm công việc thương mại quốc tế.
方面|fāngmiàn|dt|phương diện, mặt|这方面的书我读过不少。~Sách về mặt này tôi đã đọc không ít.
知识|zhīshi|dt|kiến thức, tri thức|读书可以学到很多知识。~Đọc sách có thể học được nhiều kiến thức.
另|lìng|dai|khác (cái khác)|我有两个哥哥，一个是医生，另一个是老师。~Tôi có hai anh trai, một người là bác sĩ, người kia là giáo viên.
"""),
texts=[dict(t="课文1", scene="在学院办公室，白家月和陈天中在办理入学手续。", scene_vi="Tại văn phòng khoa, Bạch Gia Nguyệt và Trần Thiên Trung đang làm thủ tục nhập học.", narr=False, lines=T("""
老师>你们好，欢迎来到中国留学！请把护照、签证和入学通知书给我。|Chào các em, chào mừng các em đến Trung Quốc du học! Các em đưa cô hộ chiếu, visa và giấy báo nhập học nhé.
白家月>好的。这是我们的证件和材料。|Vâng ạ. Đây là giấy tờ và hồ sơ của chúng em.
老师>办好了，这是你们的学生证，下周一开始上课。先试听两周，然后在网上选课。|Xong rồi, đây là thẻ sinh viên của các em, thứ Hai tuần sau bắt đầu học. Học thử hai tuần trước, sau đó chọn môn trên mạng.
白家月>谢谢老师。|Cảm ơn cô ạ.
老师>不客气，你们以后有任何问题都可以来找我。|Không có gì, sau này các em có bất kỳ vấn đề gì cũng có thể đến tìm cô.
"""), q=Q("""
老师给白家月什么了？|学生证。|Thẻ sinh viên.
他们要给老师什么证件和材料？|护照、签证和入学通知书。|Hộ chiếu, visa và giấy báo nhập học.
他们什么时候开始上课？|下周一。|Thứ Hai tuần sau.
他们在哪儿选课？|在网上选课。|Chọn môn trên mạng.
""")),
 dict(t="课文2", scene="在大学校园，白家月和陈天中边逛边聊。", scene_vi="Trong khuôn viên trường đại học, Bạch Gia Nguyệt và Trần Thiên Trung vừa đi dạo vừa trò chuyện.", narr=False, lines=T("""
陈天中>你看，咱们的校园真大！有图书馆、体育馆、超市，还有好几个食堂。|Cậu xem, khuôn viên trường mình rộng thật! Có thư viện, nhà thi đấu, siêu thị, còn có mấy nhà ăn nữa.
白家月>是啊，我觉得学校就像一座小城市，什么都有，方便极了。|Đúng vậy, mình thấy trường giống như một thành phố nhỏ, cái gì cũng có, tiện vô cùng.
陈天中>刚才老师说，咱们可以申请奖学金，你了解过吗？|Lúc nãy cô giáo nói mình có thể xin học bổng, cậu đã tìm hiểu chưa?
白家月>我听说过一点儿，好像成绩好、表现好的学生都有机会获得奖学金。|Mình có nghe qua một chút, hình như sinh viên học giỏi, biểu hiện tốt đều có cơ hội nhận học bổng.
陈天中>那太好了，要是申请到奖学金，就能减轻不少经济压力。|Vậy thì tốt quá, nếu xin được học bổng thì có thể giảm bớt không ít áp lực tài chính.
白家月>没错，我们一起加油吧！|Đúng thế, chúng ta cùng cố lên nhé!
"""), q=Q("""
白家月觉得学校怎么样？|像一座小城市，什么都有，方便极了。|Giống một thành phố nhỏ, cái gì cũng có, rất tiện.
他们的校园里有什么？|有图书馆、体育馆、超市，还有好几个食堂。|Có thư viện, nhà thi đấu, siêu thị và mấy nhà ăn.
什么样的学生有机会获得奖学金？|成绩好、表现好的学生。|Sinh viên học giỏi, biểu hiện tốt.
陈天中为什么想申请奖学金？|为了减轻经济压力。|Để giảm bớt áp lực tài chính.
""")),
 dict(t="课文3", scene="外国学生在中国大学的学习和生活", scene_vi="Việc học và cuộc sống của sinh viên nước ngoài ở đại học Trung Quốc", narr=True, lines=T("""
随着中国的发展，越来越多的外国学生来到中国的大学学习。|Cùng với sự phát triển của Trung Quốc, ngày càng nhiều sinh viên nước ngoài đến học ở các trường đại học Trung Quốc.
他们可以先上一年的中文课程，然后根据自己的兴趣和需要选择专业。|Họ có thể học một năm khóa tiếng Trung trước, sau đó chọn chuyên ngành theo sở thích và nhu cầu của mình.
除了读本科课程，他们还可以申请读硕士研究生或者博士研究生。|Ngoài học chương trình đại học, họ còn có thể xin học thạc sĩ hoặc tiến sĩ.
在大学里，外国学生可以和中国学生一起学习、做研究、参加校园活动。|Ở trường đại học, sinh viên nước ngoài có thể cùng sinh viên Trung Quốc học tập, nghiên cứu, tham gia các hoạt động trong trường.
通过这些交流，外国学生能更快地适应中国的大学生活。|Thông qua những giao lưu này, sinh viên nước ngoài có thể thích nghi nhanh hơn với cuộc sống đại học ở Trung Quốc.
"""), q=Q("""
外国学生可以根据什么选择专业？|根据自己的兴趣和需要。|Theo sở thích và nhu cầu của bản thân.
为什么很多外国学生来中国学习？|因为随着中国的发展，来中国学习的机会越来越多。|Vì cùng với sự phát triển của Trung Quốc, cơ hội học ở Trung Quốc ngày càng nhiều.
除了学习，外国学生还可以和中国学生一起做什么？|一起做研究、参加校园活动。|Cùng nghiên cứu, tham gia các hoạt động trong trường.
外国学生怎么能更快地适应中国的大学生活？|多跟中国学生交流。|Giao lưu nhiều với sinh viên Trung Quốc.
""")),
 dict(t="课文4", scene="专业选择与职业发展", scene_vi="Chọn chuyên ngành và phát triển nghề nghiệp", narr=True, lines=T("""
很多外国学生来中国学习以前，就已经想好了自己的发展方向。|Nhiều sinh viên nước ngoài trước khi đến Trung Quốc học đã nghĩ kỹ hướng phát triển của mình.
有人对经济感兴趣，希望将来在国际公司工作；|Có người quan tâm đến kinh tế, hy vọng sau này làm việc ở công ty quốc tế;
有人喜欢学医，打算回国后当一名医生；|có người thích học y, dự định về nước làm bác sĩ;
还有人对教育有热情，想要成为一名教师。|còn có người nhiệt huyết với giáo dục, muốn trở thành giáo viên.
陈天中想选择跟经济有关的专业，希望通过学习，了解更多国际贸易方面的知识。|Trần Thiên Trung muốn chọn chuyên ngành liên quan đến kinh tế, hy vọng thông qua việc học hiểu thêm kiến thức về thương mại quốc tế.
安妮以后想做一名中文老师，所以要选择国际中文教育专业。|Annie sau này muốn làm giáo viên tiếng Trung, nên sẽ chọn chuyên ngành Giáo dục tiếng Trung quốc tế.
对他们来说，来到中国留学，一方面是为了学习语言和知识，另一方面也是为将来的工作和生活做准备。|Đối với họ, đến Trung Quốc du học một mặt là để học ngôn ngữ và kiến thức, mặt khác cũng là chuẩn bị cho công việc và cuộc sống sau này.
"""), q=Q("""
很多外国学生来中国学习以前，做了什么准备？|已经想好了自己的发展方向。|Đã nghĩ kỹ hướng phát triển của mình.
陈天中想选择什么专业？为什么？|跟经济有关的专业，因为他希望了解更多国际贸易方面的知识。|Chuyên ngành liên quan đến kinh tế, vì muốn hiểu thêm kiến thức thương mại quốc tế.
安妮以后想做什么？|想做一名中文老师。|Muốn làm giáo viên tiếng Trung.
陈天中和安妮来到中国留学是为了什么？|一方面是为了学习语言和知识，另一方面是为将来的工作和生活做准备。|Một mặt để học ngôn ngữ và kiến thức, mặt khác để chuẩn bị cho công việc và cuộc sống sau này.
"""))],
grammar=[
 G("renhe", "指示代词“任何”", "Đại từ chỉ thị “任何”",
   "“任何” nghĩa là “bất kỳ, bất cứ… nào”. Khi bổ nghĩa cho danh từ thường không dùng “的”; phía sau hay đi kèm “都” hoặc “也”.",
   [F("kw:任何|N:Danh từ|S:(Chủ ngữ)|kw2:都 / 也|V:Vị ngữ", [
     ("你们以后有[任何]|问题||[都]|可以来找我", "。", "Sau này các em có bất kỳ vấn đề gì cũng có thể đến tìm cô."),
     ("明天我们8点出发，[任何]|人||[也]|不能迟到", "。", "Mai chúng ta xuất phát lúc 8 giờ, bất kỳ ai cũng không được đến muộn."),
     ("学校有[任何]|通知|我|[都]|会第一时间告诉你", "。", "Trường có bất kỳ thông báo nào, tôi đều sẽ báo cho bạn ngay lập tức.")])]),
 G("yaoshi", "假设复句“要是……，就……”", "Câu phức giả thiết “要是……，就……”",
   "Vế trước nêu một giả thiết, vế sau nói kết quả xảy ra khi giả thiết đó thành hiện thực: “nếu… thì…”. “要是” có thể đứng trước hoặc sau chủ ngữ.",
   [F("kw:要是|X:Giả thiết|kw2:就|V:Kết quả", [
     ("[要是]|申请到奖学金|[就]|能减轻不少经济压力", "。", "Nếu xin được học bổng thì có thể giảm bớt không ít áp lực tài chính."),
     ("你[要是]|明天有时间|[就]|跟我一起去爬山吧", "。", "Nếu ngày mai bạn rảnh thì đi leo núi với mình nhé."),
     ("[要是]|她不愿意参加比赛|我们[就]|再问问别人", "。", "Nếu cô ấy không muốn tham gia cuộc thi thì chúng ta hỏi người khác.")])]),
 G("suizhe", "介词“随着”", "Giới từ “随着”",
   "Sau “随着” thường là từ ngữ hoặc mệnh đề biểu thị sự thay đổi, cho biết một việc là điều kiện khiến việc khác xảy ra: “cùng với…, theo đà…”.",
   [F("kw:随着|X:Sự thay đổi|V:Kết quả kéo theo", [
     ("[随着]|中国的发展|越来越多的外国学生来到中国的大学学习", "。", "Cùng với sự phát triển của Trung Quốc, ngày càng nhiều sinh viên nước ngoài đến học ở đại học Trung Quốc."),
     ("[随着]|中文水平的提高|我现在能看懂中文报纸了", "。", "Cùng với việc trình độ tiếng Trung được nâng cao, giờ tôi đã đọc hiểu được báo tiếng Trung."),
     ("[随着]|小区的环境越来越好|来这里买房子的人也变多了", "。", "Theo đà môi trường khu dân cư ngày càng tốt, người đến đây mua nhà cũng nhiều lên.")])]),
 G("yifangmian", "并列复句“一方面……，另一方面……”", "Câu phức đẳng lập “一方面……，另一方面……”",
   "Dùng để trình bày hai mặt (lý do, tình huống…) cùng tồn tại: “một mặt…, mặt khác…”. Vế sau thường có thêm “也”.",
   [F("S:Chủ đề|kw:一方面|X:Mặt thứ nhất|kw2:另一方面|V:Mặt thứ hai", [
     ("来到中国留学|[一方面]|是为了学习语言和知识|[另一方面]|也是为将来的工作和生活做准备", "。", "Đến Trung Quốc du học, một mặt là để học ngôn ngữ và kiến thức, mặt khác cũng là chuẩn bị cho công việc và cuộc sống sau này."),
     ("他经常在网上买东西|[一方面]|因为便宜|[另一方面]|因为方便", "。", "Anh ấy hay mua đồ trên mạng, một mặt vì rẻ, mặt khác vì tiện."),
     ("多做运动|[一方面]|能让身体更健康|[另一方面]|也能减轻压力", "。", "Vận động nhiều một mặt giúp cơ thể khỏe hơn, mặt khác cũng giảm được áp lực.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["入学", "签证", "获得", "专业", "食堂"], [
   "她【获得】了三年的奖学金，高兴极了。", "我是2024年【入学】的，学的是国际经济专业。", "我打算考研究生，提高自己的【专业】水平。",
   "咱们晚上别去【食堂】吃饭了，我请你出去吃饭吧。", "王经理今天下午去办【签证】了，您明天再来找他吧。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["加油", "研究", "活动", "任何", "将来"], [
   "A：你【将来】想做什么工作？ B：我想在国际公司工作，有更多的发展机会。", "A：你为什么选择这门课程？ B：因为我想认真【研究】中国的历史和文化。",
   "A：今天下午公司有【活动】，我晚点儿回家。 B：好。大概几点结束？需要我去接你吗？", "A：你们要去哪儿？ B：我们要去给参加比赛的同学【加油】，你去吗？",
   "A：你们这次旅游怎么样？ B：虽然天气不太好，但是和朋友在一起，做【任何】事情都很有意思。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["也会觉得有一些压力", "她除了复习大学学过的课程", "她决定参加硕士研究生考试", "希望拿到研究生的入学通知书"], [
   "李雪还有一年就本科毕业了，【她决定参加硕士研究生考试】。为了准备考试，【她除了复习大学学过的课程】，还读了一些新的专业书，希望更多地了解这方面的知识。有时候她学习的时间很长，【也会觉得有一些压力】，但是她还是坚持每天学习。随着考试的时间越来越近，李雪也更努力地复习，【希望拿到研究生的入学通知书】，在新的学校里继续学习更多知识。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：听说王老师特别热情？ B：______。（任何）", "对，学生有任何问题，她都愿意帮忙。"),
   ("A：你不开心的时候会做什么？ B：我要是不开心，______。", "我要是不开心，就去跑步或者听音乐。"),
   ("随着______，人们越来越关注身体健康。（提高）", "随着生活水平的提高，人们越来越关注身体健康。"),
   ("我很喜欢旅游，因为一方面______，另一方面______。", "我很喜欢旅游，因为一方面能放松心情，另一方面能了解不同的文化。")]),
 opn("用词语造句", "Dùng từ cho sẵn đặt câu.", [
   ("申请", "我想申请明年的奖学金。"), ("通知", "老师通知我们下周一开始上课。"), ("压力", "考试前我的压力很大。")]),
])
