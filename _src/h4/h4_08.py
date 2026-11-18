# -*- coding: utf-8 -*-
# HSK 4上 – Bài 8: 该放松时就放松
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[8] = dict(zh="该放松时就放松", vi="Lúc cần thư giãn thì hãy thư giãn",
intro="Annie và Bạch Gia Nguyệt hẹn nhau leo Vạn Lý Trường Thành để xả stress; Dương Đồng Lạc kể chuyện từng làm thêm giờ đến kiệt sức, rồi học cách nghỉ ngơi để làm việc hiệu quả hơn; bài học còn giới thiệu những nơi thư giãn cuối tuần ở Bắc Kinh.",
vocab=V("""
紧张|jǐnzhāng|tt|căng thẳng, hồi hộp; khan hiếm|考试前我有点儿紧张。~Trước khi thi tôi hơi căng thẳng.
放松|fàngsōng|dong|thả lỏng, thư giãn|周末我想好好放松一下。~Cuối tuần tôi muốn thư giãn cho thoải mái.
呀|yā|than|a, ô (tỏ vẻ ngạc nhiên)|呀，下雪了！~Ô, tuyết rơi rồi!
不管|bùguǎn|lien|bất kể, dù|不管天气怎么样，他都去跑步。~Bất kể thời tiết thế nào, anh ấy đều đi chạy bộ.
郊区|jiāoqū|dt|ngoại ô|周末很多人去郊区玩儿。~Cuối tuần nhiều người đi ngoại ô chơi.
游玩|yóuwán|dong|đi chơi, du ngoạn|我们去公园游玩了一天。~Chúng tôi đi chơi công viên cả ngày.
主意|zhǔyi|dt|ý kiến, ý tưởng|这是个好主意！~Đây là một ý hay!
外出|wàichū|dong|ra ngoài, đi ra ngoài|外出时要注意安全。~Khi ra ngoài phải chú ý an toàn.
戴|dài|dong|đội, đeo|外面很冷，戴上帽子吧。~Ngoài trời lạnh, đội mũ vào đi.
帽子|màozi|dt|cái mũ|这顶帽子很好看。~Cái mũ này rất đẹp.
长城|Chángchéng|rieng|Vạn Lý Trường Thành|我去年爬过长城。~Năm ngoái tôi đã leo Vạn Lý Trường Thành.
项目|xiàngmù|dt|dự án, hạng mục|这个项目需要三个月才能完成。~Dự án này cần ba tháng mới hoàn thành được.
加班|jiābān|dong|tăng ca, làm thêm giờ|他这个星期每天都加班。~Tuần này ngày nào anh ấy cũng tăng ca.
熬夜|áoyè|dong|thức khuya|经常熬夜对身体不好。~Thường xuyên thức khuya không tốt cho sức khỏe.
否则|fǒuzé|lien|nếu không thì|快走吧，否则要迟到了。~Đi nhanh lên, nếu không sẽ muộn mất.
失去|shīqù|dong|mất, mất đi|他失去了这次机会。~Anh ấy đã mất cơ hội lần này.
值得|zhídé|dong|đáng, xứng đáng|这本书值得一看。~Cuốn sách này đáng đọc.
暂停|zàntíng|dong|tạm dừng|比赛暂停了十分钟。~Trận đấu tạm dừng mười phút.
之后|zhīhòu|dt|sau khi, sau đó|下课之后我们去吃饭吧。~Sau khi tan học chúng ta đi ăn nhé.
风景|fēngjǐng|dt|phong cảnh|这里的风景特别美。~Phong cảnh ở đây đặc biệt đẹp.
效率|xiàolǜ|dt|hiệu suất, năng suất|他工作效率很高。~Anh ấy làm việc năng suất rất cao.
下降|xiàjiàng|dong|giảm xuống, đi xuống|最近气温下降了。~Gần đây nhiệt độ giảm xuống.
相比|xiāngbǐ|dong|so với|跟去年相比，今年冷多了。~So với năm ngoái, năm nay lạnh hơn nhiều.
因此|yīncǐ|lien|vì vậy, do đó|他生病了，因此没来上课。~Anh ấy bị ốm, vì vậy không đến lớp.
提醒|tíxǐng|dong|nhắc nhở|请提醒我明天带护照。~Nhắc tôi ngày mai mang hộ chiếu nhé.
与|yǔ|gioi|với, và|他常常与朋友去爬山。~Anh ấy thường đi leo núi với bạn bè.
大自然|dàzìrán|dt|thiên nhiên|我喜欢去大自然里走走。~Tôi thích đi dạo giữa thiên nhiên.
美丽|měilì|tt|đẹp, xinh đẹp|这是一个美丽的城市。~Đây là một thành phố xinh đẹp.
景色|jǐngsè|dt|cảnh sắc, cảnh vật|秋天的景色特别美。~Cảnh sắc mùa thu đặc biệt đẹp.
首都|shǒudū|dt|thủ đô|北京是中国的首都。~Bắc Kinh là thủ đô của Trung Quốc.
市区|shìqū|dt|nội thành, khu thành phố|我住在市区，上班很方便。~Tôi sống ở nội thành, đi làm rất tiện.
眼前|yǎnqián|dt|trước mắt|眼前是一片美丽的大海。~Trước mắt là một vùng biển xinh đẹp.
美景|měijǐng|dt|cảnh đẹp|山上的美景让人难忘。~Cảnh đẹp trên núi khiến người ta khó quên.
参观|cānguān|dong|tham quan|我们下午去参观博物馆。~Chiều nay chúng tôi đi tham quan bảo tàng.
景点|jǐngdiǎn|dt|điểm tham quan, thắng cảnh|这个景点每天都有很多游客。~Điểm tham quan này ngày nào cũng đông khách.
交通|jiāotōng|dt|giao thông|这里交通很方便。~Giao thông ở đây rất thuận tiện.
乘坐|chéngzuò|dong|đi (tàu, xe), ngồi|我们乘坐高铁去上海。~Chúng tôi đi tàu cao tốc đến Thượng Hải.
十分|shífēn|pho|rất, vô cùng|今天的天气十分好。~Thời tiết hôm nay vô cùng đẹp.
实际上|shíjìshang|pho|thực ra, trên thực tế|他看起来很年轻，实际上已经五十岁了。~Ông ấy trông rất trẻ, thực ra đã năm mươi tuổi rồi.
故宫|Gùgōng|rieng|Cố Cung (Tử Cấm Thành)|故宫是北京有名的景点。~Cố Cung là danh thắng nổi tiếng của Bắc Kinh.
"""),
texts=[dict(t="课文1", scene="周五晚上，安妮给白家月打电话。", scene_vi="Tối thứ Sáu, Annie gọi điện cho Bạch Gia Nguyệt.", narr=False, lines=T("""
安妮>家月，最近学习太紧张了，咱们明天出去放松放松吧。|Gia Nguyệt, dạo này học căng thẳng quá, mai chúng mình đi ra ngoài thư giãn đi.
白家月>呀，正好我也想出去呢。咱们去哪儿好呢？|Ồ, mình cũng đang muốn đi ra ngoài đây. Chúng mình đi đâu thì hay nhỉ?
安妮>不管去哪儿，能放松的地方都行。|Đi đâu cũng được, miễn là chỗ thư giãn được.
白家月>郊区怎么样？|Ngoại ô thì sao?
安妮>天中说，下周王老师要带咱们去郊区游玩呢。|Thiên Trung nói tuần sau cô Vương sẽ dẫn chúng mình đi chơi ngoại ô đấy.
白家月>是吗？那咱们明天去爬长城吧，不是说“不到长城非好汉”吗？|Thật à? Vậy mai mình đi leo Trường Thành đi, chẳng phải người ta nói “chưa đến Trường Thành chưa phải hảo hán” sao?
安妮>好主意！不过明天是个大晴天，外出记得戴帽子。|Ý hay đấy! Nhưng mai trời nắng to, ra ngoài nhớ đội mũ nhé.
"""), q=Q("""
安妮为什么想出去放松放松？|因为最近学习太紧张了。|Vì dạo này học quá căng thẳng.
安妮想外出放松一下，白家月呢？|正好她也想出去。|Cô cũng đang muốn ra ngoài.
安妮和白家月最后决定去哪里？|长城。|Vạn Lý Trường Thành.
安妮觉得白家月提的爬长城的建议怎么样？|觉得是个好主意，不过提醒她外出记得戴帽子。|Thấy là ý hay, nhưng nhắc cô ra ngoài nhớ đội mũ.
""")),
 dict(t="课文2", scene="周末，李文、杨同乐等人去郊区游玩。", scene_vi="Cuối tuần, Lý Văn, Dương Đồng Lạc và mọi người đi chơi ngoại ô.", narr=False, lines=T("""
李文>同乐哥，你们平时工作忙吗？|Anh Đồng Lạc, ngày thường các anh làm việc có bận không?
杨同乐>挺忙的。以前我总觉得年轻时要多学多干，所以参加了公司里的很多项目，经常加班、熬夜，身体也亮起了红灯。|Khá bận. Trước đây anh luôn nghĩ lúc còn trẻ phải học nhiều làm nhiều, nên tham gia rất nhiều dự án của công ty, thường xuyên tăng ca, thức khuya, sức khỏe cũng báo động đỏ.
李文>还是别给自己太大压力，否则，失去健康就不值得了。|Anh đừng tạo áp lực quá lớn cho bản thân, nếu không mất sức khỏe thì không đáng đâu.
杨同乐>是啊，后来我就不接那么多项目了。我发现暂停下来、好好休息之后，我能把工作做得更快更好。|Đúng vậy, sau này anh không nhận nhiều dự án như thế nữa. Anh phát hiện sau khi tạm dừng lại, nghỉ ngơi cho tốt, anh làm việc nhanh hơn và tốt hơn.
李文>对，该工作时就工作，该放松时就要放松。|Đúng, lúc cần làm thì làm, lúc cần thư giãn thì phải thư giãn.
杨同乐>是的，现在我周末常来郊区，在好山好水好风景中放松自己。|Phải, bây giờ cuối tuần anh hay ra ngoại ô, thư giãn giữa núi non sông nước và phong cảnh đẹp.
"""), q=Q("""
杨同乐以前工作怎么样？|经常加班、熬夜。|Thường xuyên tăng ca, thức khuya.
杨同乐以前为什么经常加班、熬夜？|因为他觉得年轻时要多学多干，参加了公司里的很多项目。|Vì anh nghĩ lúc trẻ phải học nhiều làm nhiều, nên tham gia nhiều dự án.
李文为什么说别给自己太大压力？|因为失去健康就不值得了。|Vì mất sức khỏe thì không đáng.
杨同乐周末来郊区是为了什么？|放松自己。|Để thư giãn.
""")),
 dict(t="课文3", scene="学会放松", scene_vi="Học cách thư giãn", narr=True, lines=T("""
以前杨同乐总觉得自己年轻，就应该多学多干、积累经验。|Trước đây Dương Đồng Lạc luôn cảm thấy mình còn trẻ thì nên học nhiều làm nhiều, tích lũy kinh nghiệm.
很多年轻人和他想法一样。|Nhiều người trẻ cũng nghĩ giống anh.
但是，由于工作紧张，他们经常加班、熬夜，休息不够，结果工作效率下降，健康也受到了影响。|Nhưng do công việc căng thẳng, họ thường xuyên tăng ca, thức khuya, nghỉ ngơi không đủ, kết quả là năng suất giảm sút, sức khỏe cũng bị ảnh hưởng.
现在越来越多的人认识到，跟一直加班相比，休息好了再工作，效率更高。|Bây giờ ngày càng nhiều người nhận ra, so với tăng ca liên tục, nghỉ ngơi đầy đủ rồi mới làm việc thì năng suất cao hơn.
因此，很多人开始做出改变，提醒自己减轻压力、多多放松。|Vì vậy, nhiều người bắt đầu thay đổi, tự nhắc mình giảm bớt áp lực, thư giãn nhiều hơn.
比如，杨同乐周末时或者与朋友们去郊区游玩，在大自然美丽的景色中好好放松自己；或者就在家里安安静静地看看书。|Ví dụ, cuối tuần Dương Đồng Lạc hoặc cùng bạn bè đi chơi ngoại ô, thư giãn giữa cảnh sắc thiên nhiên tươi đẹp; hoặc ở nhà yên tĩnh đọc sách.
休息好了，再回去上班时，心情愉快，工作效率也更高。|Nghỉ ngơi đầy đủ rồi quay lại đi làm, tâm trạng vui vẻ, năng suất làm việc cũng cao hơn.
"""), q=Q("""
根据课文，经常加班、熬夜会怎么样？|工作效率下降，健康也受到影响。|Năng suất giảm, sức khỏe bị ảnh hưởng.
跟一直加班相比，现在人们认识到，怎样才能效率更高？|休息好了再工作。|Nghỉ ngơi đầy đủ rồi mới làm việc.
现在杨同乐周末时一般会怎样放松自己？|与朋友们去郊区游玩，或者在家里安安静静地看看书。|Đi chơi ngoại ô với bạn bè, hoặc ở nhà yên tĩnh đọc sách.
周末好好休息，给杨同乐带来了什么变化？|心情愉快，工作效率也更高了。|Tâm trạng vui vẻ, năng suất làm việc cao hơn.
""")),
 dict(t="课文4", scene="去哪儿放松好", scene_vi="Đi đâu để thư giãn", narr=True, lines=T("""
一到周末，很多人都喜欢外出游玩。你一般去哪里呢？|Cứ đến cuối tuần, nhiều người thích ra ngoài đi chơi. Bạn thường đi đâu?
我生活在中国的首都——北京。|Tôi sống ở thủ đô của Trung Quốc — Bắc Kinh.
在北京，周末的时候，有人会在市区公园走走，看看眼前的美景；|Ở Bắc Kinh, vào cuối tuần, có người đi dạo trong các công viên nội thành, ngắm cảnh đẹp trước mắt;
有人喜欢去参观长城、故宫等有名的景点，放松心情的同时，也能了解历史文化。|có người thích đi tham quan các danh thắng nổi tiếng như Trường Thành, Cố Cung, vừa thư giãn vừa tìm hiểu lịch sử văn hóa.
北京交通很方便，所以我和家人更爱乘坐公交车去郊区，偶尔也会自己开车。|Giao thông Bắc Kinh rất thuận tiện, nên tôi và gia đình thích đi xe buýt ra ngoại ô hơn, thỉnh thoảng cũng tự lái xe.
郊区有山有水，还有很多农家乐，吃、玩、住都十分方便。|Ngoại ô có núi có sông, còn có nhiều nhà vườn du lịch (nông gia lạc), ăn, chơi, ở đều rất tiện.
在我看来，不管去哪里玩，实际上都是为了放松。也可以说，只要能放松，去哪儿都合适。|Theo tôi, dù đi chơi ở đâu thì thực ra cũng là để thư giãn. Cũng có thể nói, chỉ cần thư giãn được thì đi đâu cũng hợp.
"""), q=Q("""
根据课文，周末的时候，很多人都喜欢做什么？|外出游玩。|Ra ngoài đi chơi.
在北京，周末外出游玩，人们一般会去哪里？|市区公园、长城、故宫等景点，还有郊区。|Công viên nội thành, Trường Thành, Cố Cung và các thắng cảnh khác, cả ngoại ô nữa.
他和家人为什么喜欢坐公交车去郊区？|因为北京交通很方便。|Vì giao thông Bắc Kinh rất thuận tiện.
农家乐怎么样？|吃、玩、住都十分方便。|Ăn, chơi, ở đều rất tiện.
""")),
],
grammar=[
 G("buguan", "条件复句“不管……，都/也……”", "Câu phức điều kiện “不管……，都 / 也……”",
   "Vế trước nêu điều kiện có thể xảy ra (thường có từ nghi vấn hoặc dạng chính phản), vế sau cho biết kết quả không thay đổi. Cấu trúc: 不管 + điều kiện / tình huống / sự thay đổi, (chủ ngữ) + 都/也 + kết quả.",
   [F("kw:不管|X:Điều kiện|S:(Chủ ngữ)|kw2:都 / 也|V:Kết quả không đổi", [
     ("[不管]|去哪儿|能放松的地方|[都]|行", "。", "Đi đâu cũng được, miễn là nơi thư giãn được."),
     ("[不管]|有什么想法|你|[都]|要说出来，让我们知道", "。", "Bất kể có suy nghĩ gì, bạn đều phải nói ra cho chúng tôi biết."),
     ("[不管]|遇到多大困难|我们|[也]|要坚持，最后一定能完成任务", "。", "Dù gặp khó khăn lớn đến đâu, chúng ta cũng phải kiên trì, cuối cùng nhất định sẽ hoàn thành nhiệm vụ.")])]),
 G("fouze", "假设复句“……，否则……”", "Câu phức giả thiết “……，否则……”",
   "Vế trước đưa ra yêu cầu, đề nghị hoặc điều kiện; vế sau nói hậu quả nếu điều ở vế trước không thực hiện được: “…, nếu không thì…”.",
   [F("X:Yêu cầu / đề nghị|kw:否则|V:Hậu quả", [
     ("还是别给自己太大压力|[否则]|失去健康就不值得了", "。", "Đừng tạo áp lực quá lớn cho bản thân, nếu không mất sức khỏe thì không đáng."),
     ("今晚早点儿睡吧|[否则]|明天早上起不来，又该迟到了", "。", "Tối nay ngủ sớm đi, nếu không sáng mai dậy không nổi lại muộn mất."),
     ("吃不完的菜要放进冰箱|[否则]|很容易坏", "。", "Thức ăn ăn không hết phải cho vào tủ lạnh, nếu không rất dễ hỏng.")])]),
 G("genxiangbi", "比较句“跟……相比”", "Câu so sánh “跟……相比”",
   "“跟……相比” là cấu trúc so sánh (so với…). Giới từ “跟” thường dùng trong khẩu ngữ, ngữ cảnh không trang trọng; trong văn viết, ngữ cảnh trang trọng hay dùng “与”.",
   [F("kw:跟 / 与|X:Đối tượng so sánh|kw2:相比|V:Kết luận", [
     ("[跟]|一直加班|[相比]|休息好了再工作，效率更高", "。", "So với tăng ca liên tục, nghỉ ngơi đầy đủ rồi mới làm việc thì năng suất cao hơn."),
     ("[跟]|读研究生|[相比]|我更想直接工作", "。", "So với học cao học, tôi muốn đi làm luôn hơn."),
     ("[跟]|用现金|[相比]|手机支付更方便些", "。", "So với dùng tiền mặt, thanh toán bằng điện thoại tiện hơn.")])]),
 G("youayoub", "固定短语“有A有B”", "Cụm từ cố định “有A有B”",
   "Trong “有A有B”, A và B phần lớn là từ đơn âm tiết, số ít là song âm tiết; nghĩa của A và B thường liên quan, gần nhau hoặc đối lập nhau: “có A có B, vừa có A vừa có B”.",
   [F("S:Chủ ngữ|kw:有|A:A|kw2:有|B:B", [
     ("郊区|[有]|山|[有]|水", "，还有很多农家乐。", "Ngoại ô có núi có sông, còn có nhiều nhà vườn du lịch."),
     ("超市里的苹果|[有]|大|[有]|小", "，有红有绿，看起来都非常好吃。", "Táo trong siêu thị có to có nhỏ, có đỏ có xanh, trông đều rất ngon."),
     ("春天，公园里到处是人，|[有]|男|[有]|女", "，有大人有孩子，特别热闹。", "Mùa xuân, công viên đâu đâu cũng là người, có nam có nữ, có người lớn có trẻ con, rất náo nhiệt.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["戴", "主意", "乘坐", "提醒", "紧张"], [
   "从北京【乘坐】高铁去上海，四五个小时就能到，特别快。", "下雨天妈妈总是【提醒】我，出门时别忘了带雨伞。", "夏天比较热，出汗多，所以我一般不【戴】手表。",
   "他今天是第一次参加比赛，所以十分【紧张】。", "大家正不知道怎么办时，小文想出了一个好【主意】，这个难题马上就解决了。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["风景", "下降", "否则", "景点", "实际上"], [
   "A：明天有什么安排？ B：明天就安排了一个【景点】——八达岭长城。因为有些远，需要坐高铁去。", "A：八达岭长城的【风景】太美了，我很喜欢。你以前来过吗？ B：来过，这是我第三次来了。",
   "A：你怎么了？感觉这段时间你的工作效率【下降】了。 B：可能是因为最近晚上睡不着，休息不好。", "A：这道菜看着不太好吃，我不想吃。 B：【实际上】挺好吃的，你尝尝。",
   "A：我刚收到通知，今天下午要停水。 B：那咱们赶快多接点儿水，【否则】做不了饭了。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["累了就休息", "这样效率才能更高", "还经常感冒", "中午也不按时吃饭"], [
   "工作或学习时间长了就要休息一会儿，【这样效率才能更高】。我以前在学校读书时，很长一段时间里，除了上课，就是在图书馆学习，【中午也不按时吃饭】。结果是不仅学习效果不好，【还经常感冒】。后来，我开始注意锻炼身体，【累了就休息】，学习效率也提高了。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：外边雨特别大，你们还去看电影吗？ B：票都买了，所以______，我们都______。（不管……都……）", "票都买了，所以不管雨多大，我们都要去。"),
   ("A：妈妈，我不想吃药。 B：快吃吧，否则______。", "快吃吧，否则病好不了。"),
   ("跟在家里看电视相比，______。（大自然）", "跟在家里看电视相比，我更喜欢去大自然里走走。"),
   ("小花园里______，非常漂亮。（有A有B）", "小花园里有红有绿，非常漂亮。")]),
 opn("用词语造句", "Dùng từ cho sẵn đặt câu.", [
   ("市区", "我住在市区，周末常去公园走走。"), ("景色", "秋天山上的景色特别美。"), ("交通", "这个城市的交通很方便。")]),
])
