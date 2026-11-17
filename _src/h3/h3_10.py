# -*- coding: utf-8 -*-
# HSK 3 – Bài 10: 你明天再把书还给我
from gtb_gen import V, T, Q, F, G
B = {}

B[10] = dict(zh="你明天再把书还给我", vi="Ngày mai em hãy trả lại sách cho cô",
intro="Lưu Tiểu Tuyết chia sẻ cách học Toán, cùng bạn ôn thi, lên văn phòng hỏi bài cô Lý, rồi viết email kể cho chị Gia Nguyệt về việc học ở trường cấp hai.",
vocab=V("""
数学|shùxué|dt|môn Toán, toán học|我最喜欢上数学课。~Tôi thích giờ Toán nhất.
认真|rènzhēn|tt|chăm chỉ, nghiêm túc|他学习非常认真。~Cậu ấy học rất chăm chỉ.
笔记|bǐjì|dt|ghi chép|上课要记笔记。~Lên lớp phải ghi chép.
清楚|qīngchu|tt|rõ ràng, hiểu rõ|老师讲得很清楚。~Thầy giảng rất rõ ràng.
黑板|hēibǎn|dt|bảng đen|请看黑板。~Mời các em nhìn lên bảng.
把|bǎ|gioi|(đưa tân ngữ lên trước động từ)|请把门关上。~Hãy đóng cửa lại.
作业|zuòyè|dt|bài tập về nhà|今天的作业不多。~Bài tập hôm nay không nhiều.
遍|biàn|lg|lượt|这本书我看了三遍。~Cuốn sách này tôi đọc ba lượt rồi.
提高|tígāo|dong|nâng cao|我想提高我的汉语水平。~Tôi muốn nâng cao trình độ tiếng Hán.
历史|lìshǐ|dt|môn Lịch sử, lịch sử|北京有很长的历史。~Bắc Kinh có lịch sử rất lâu đời.
难|nán|tt|khó, khó khăn|这次考试不太难。~Kỳ thi lần này không khó lắm.
要求|yāoqiú|dt|yêu cầu, đòi hỏi|老师要求我们每天读课文。~Cô giáo yêu cầu chúng tôi đọc bài mỗi ngày.
差|chà|tt|kém, thiếu|我的数学成绩有点儿差。~Điểm Toán của tôi hơi kém.
复习|fùxí|dong|ôn tập|明天考试，今天要好好复习。~Mai thi, hôm nay phải ôn tập kỹ.
外语|wàiyǔ|dt|ngoại ngữ|你会说几门外语？~Bạn biết nói mấy ngoại ngữ?
当然|dāngrán|pho|đương nhiên, dĩ nhiên|你来我家，我当然高兴。~Bạn đến nhà tôi, tôi đương nhiên vui.
遇到|yùdào|dong|gặp, gặp phải|我在路上遇到了老同学。~Tôi gặp bạn học cũ trên đường.
办公室|bàngōngshì|dt|văn phòng, phòng làm việc|王老师在办公室。~Thầy Vương ở văn phòng.
页|yè|lg|trang (giấy, sách)|请打开书，看第十页。~Mời mở sách, xem trang mười.
对话|duìhuà|dong|đối thoại, hội thoại, trò chuyện|我们来练习这个对话。~Chúng ta cùng luyện đoạn hội thoại này.
明白|míngbai|dong|hiểu, rõ ràng|你明白我的意思吗？~Bạn hiểu ý tôi không?
讲|jiǎng|dong|giảng, giải thích|老师给我们讲了一个故事。~Thầy kể cho chúng tôi một câu chuyện.
句|jù|lg|câu (nói, văn)|我只会说几句汉语。~Tôi chỉ biết nói vài câu tiếng Hán.
句子|jùzi|dt|câu|这个句子是什么意思？~Câu này có nghĩa là gì?
年级|niánjí|dt|khối lớp|我弟弟上三年级。~Em trai tôi học lớp ba.
后年|hòunián|dt|năm kia, năm sau nữa|后年我要去中国留学。~Năm sau nữa tôi sẽ sang Trung Quốc du học.
一般|yìbān|tt|bình thường, phổ biến|我一般七点起床。~Tôi thường bảy giờ dậy.
努力|nǔlì|tt|chăm chỉ, nỗ lực|只要努力，就能学好。~Chỉ cần nỗ lực là sẽ học tốt.
"""),
texts=[dict(t="课文1", scene="在教室里，刘小雪跟同学聊学习方法。", scene_vi="Lưu Tiểu Tuyết trò chuyện với bạn học về phương pháp học tập ở trong lớp học.", narr=False, lines=T("""
同学>你的数学越来越好，能不能介绍一下学习方法？|Toán của cậu ngày càng giỏi, có thể chia sẻ cách học không?
刘小雪>没有什么特别的方法，认真听课，认真记笔记。|Chẳng có cách gì đặc biệt, nghe giảng chăm chú, ghi chép cẩn thận.
同学>我看过你的笔记，记得非常清楚。|Mình xem vở ghi của cậu rồi, ghi rất rõ ràng.
刘小雪>老师写在黑板上的题都很重要，所以我会把这些题都记在本子上。|Những bài thầy viết lên bảng đều rất quan trọng, nên mình chép hết vào vở.
同学>你说得对。我没有记笔记的习惯。|Cậu nói đúng. Mình không có thói quen ghi chép.
刘小雪>笔记挺重要的，我每天写作业以前，都要看一遍。|Ghi chép khá quan trọng, mỗi ngày trước khi làm bài tập mình đều xem lại một lượt.
同学>这个方法真好！我以后也试试，希望能提高成绩。|Cách này hay thật! Sau này mình cũng thử, mong nâng được điểm.
"""), q=Q("""
刘小雪的数学为什么越来越好？|因为她认真听课，认真记笔记。|Vì cô ấy nghe giảng chăm chú, ghi chép cẩn thận.
刘小雪觉得老师写在黑板上的题重要吗？|很重要。|Rất quan trọng.
刘小雪的同学打算怎么做？为什么？|他以后也要记笔记，希望能提高成绩。|Cậu ấy cũng sẽ ghi chép, mong nâng điểm.
""")),
 dict(t="课文2", scene="在教室里，刘小雪跟同学聊昨天的考试。", scene_vi="Lưu Tiểu Tuyết trò chuyện với bạn học về bài kiểm tra hôm qua ở trong lớp học.", narr=False, lines=T("""
同学>小雪，昨天的考试，你考得怎么样？|Tiểu Tuyết, bài thi hôm qua cậu làm thế nào?
刘小雪>我觉得历史有点儿难，你呢？|Mình thấy Lịch sử hơi khó, còn cậu?
同学>数学考试我没看清楚要求，做错了好几个题，考得挺差的。|Thi Toán mình không đọc kỹ yêu cầu, làm sai mấy câu, làm khá tệ.
刘小雪>明天还有考试呢，别想那么多了，先复习外语吧。|Mai còn thi nữa, đừng nghĩ nhiều thế, ôn ngoại ngữ trước đi.
同学>外语作业里有几个问题，我可以问问你吗？|Trong bài tập ngoại ngữ có mấy câu hỏi, mình hỏi cậu được không?
刘小雪>当然可以。在学习上，遇到什么问题都可以问我。|Đương nhiên được. Trong học tập, gặp vấn đề gì cũng có thể hỏi mình.
刘小雪>不好意思，这几个题我也不会。咱们还是一起去办公室问问李老师吧。|Ngại quá, mấy câu này mình cũng không biết. Chúng ta cùng lên văn phòng hỏi cô Lý đi.
"""), q=Q("""
明天还有什么考试？|外语考试。|Thi ngoại ngữ.
同学要问刘小雪什么问题？|外语作业里的几个问题。|Mấy câu hỏi trong bài tập ngoại ngữ.
刘小雪和同学为什么一起去办公室？|因为这几个题小雪也不会，要去问李老师。|Vì Tiểu Tuyết cũng không biết làm, phải hỏi cô Lý.
""")),
 dict(t="课文3", scene="在李老师办公室，刘小雪跟同学问问题。", scene_vi="Lưu Tiểu Tuyết hỏi bài cùng bạn học ở trong phòng làm việc của cô Lý.", narr=False, lines=T("""
同学>李老师，书上有几个问题，我们想问问您。|Cô Lý, trong sách có mấy câu, chúng em muốn hỏi cô.
李老师>好，坐下说吧，哪个题不会？|Được, ngồi xuống nói đi, câu nào không biết?
同学>书上第五页的这个对话我看不懂，小雪也不明白。|Đoạn hội thoại ở trang năm em đọc không hiểu, Tiểu Tuyết cũng không hiểu.
李老师>我课上讲过这几句话，再给你们讲一遍。|Mấy câu này cô giảng trên lớp rồi, cô giảng lại cho các em một lượt.
同学>我终于懂了。这些句子一点儿也不难。|Cuối cùng em hiểu rồi. Mấy câu này chẳng khó chút nào.
刘小雪>我也明白了，谢谢您，李老师。|Em cũng hiểu rồi, cảm ơn cô Lý.
李老师>我这本书上还有几个练习，你们回家也做一做，明天再把书还给我。|Cuốn sách này của cô còn mấy bài luyện tập, các em về nhà làm thử, mai hãy trả sách cho cô.
"""), q=Q("""
刘小雪的同学听明白了吗？|听明白了，他说这些句子一点儿也不难。|Hiểu rồi, cậu ấy nói mấy câu này chẳng khó.
李老师上课的时候讲过这几句话吗？|讲过。|Có giảng rồi.
李老师为什么给他们一本书？|因为书上还有几个练习，让他们回家做一做。|Vì sách còn mấy bài luyện tập, để các em về làm.
""")),
 dict(t="课文4", scene="在家里，刘小雪在写邮件。", scene_vi="Lưu Tiểu Tuyết đang viết email ở trong nhà.", narr=True, lines=T("""
家月姐姐：你最近怎么样？忙不忙？|Chị Gia Nguyệt: Dạo này chị thế nào? Có bận không?
我现在上初中二年级，学习越来越忙，后年就要考高中了。|Em đang học lớp tám (năm hai cấp hai), học hành ngày càng bận, năm sau nữa là thi lên cấp ba rồi.
中国的学校一般是小学六年，初中三年，高中三年。|Trường học ở Trung Quốc thường là tiểu học sáu năm, cấp hai ba năm, cấp ba ba năm.
妈妈说想考上好大学，就得上一个好高中；|Mẹ nói muốn đỗ đại học tốt thì phải học một trường cấp ba tốt;
为了考上好高中，初中就得有一个不错的成绩，所以我现在非常努力。|để đỗ cấp ba tốt, cấp hai phải có thành tích khá, nên bây giờ em rất nỗ lực.
家月姐姐，你知道吗？在你的影响下，我也开始喜欢拍照了。|Chị Gia Nguyệt biết không? Dưới ảnh hưởng của chị, em cũng bắt đầu thích chụp ảnh rồi.
下次你再来北京，我给你看看我照的照片。|Lần sau chị lại đến Bắc Kinh, em cho chị xem ảnh em chụp.
"""), q=Q("""
刘小雪现在读几年级？|初中二年级。|Lớp tám (năm hai cấp hai).
中国的学校一般是怎么安排的？|小学六年，初中三年，高中三年。|Tiểu học 6 năm, cấp hai 3 năm, cấp ba 3 năm.
在白家月的影响下，刘小雪喜欢做什么了？|拍照。|Chụp ảnh.
"""))],
grammar=[
 G("ba1", "“把”字句（1）", "Câu chữ “把” (1) – thay đổi vị trí",
   "Câu chữ “把” miêu tả một hành động tác động tới người hoặc sự vật đã xác định, khiến vị trí của nó thay đổi. Phó từ phủ định “不 / 没” và động từ năng nguyện đặt trước “把”. Cấu trúc: Chủ ngữ + (不 / 没 / động từ năng nguyện) + 把 + tân ngữ + động từ + 在 / 到 + địa điểm.",
   [F("S:Chủ ngữ (+ 不/没/会…)|kw:把|O:Tân ngữ|V:Động từ + 在 / 到|P:Địa điểm", [
     ("我会|[把]|这些题|都记在|本子上", "。", "Tôi sẽ chép hết những bài này vào vở."),
     ("老师|[把]|作业本|放到|桌子上了", "。", "Thầy để vở bài tập lên bàn rồi."),
     ("你不能|[把]|名字|写在|这里", "。", "Bạn không được viết tên ở đây."),
     ("我好像|[把]|校园卡|忘在|图书馆了", "。", "Hình như tôi để quên thẻ sinh viên ở thư viện rồi.")])]),
 G("zaishang", "固定格式“在……上/中/下”", "Cấu trúc cố định “在……上 / 中 / 下”",
   "“在 + danh từ + 上” biểu thị phạm vi hoặc phương diện; “在……中” biểu thị môi trường hoặc thời gian hành động xảy ra / trạng thái tồn tại; “在 + định ngữ + động từ hai âm tiết + 下” biểu thị điều kiện.",
   [F("kw:在|X:Danh từ / cụm từ|kw2:上 / 中 / 下|C:Phần còn lại", [
     ("[在]|学习|[上]|，遇到什么问题都可以问我", "。", "Trong học tập, gặp vấn đề gì cũng có thể hỏi tôi."),
     ("[在]|比赛|[中]|，他得分最高", "。", "Trong trận đấu, anh ấy ghi điểm cao nhất."),
     ("[在]|假期|[中]|，我认识了几个新朋友", "。", "Trong kỳ nghỉ, tôi quen thêm mấy người bạn mới."),
     ("[在]|她的影响|[下]|，我开始喜欢拍照", "。", "Dưới ảnh hưởng của cô ấy, tôi bắt đầu thích chụp ảnh."),
     ("[在]|老师的帮助|[下]|，我的成绩提高很快", "。", "Nhờ sự giúp đỡ của thầy, thành tích của tôi tăng rất nhanh.")])]),
 G("ba2", "“把”字句（2）", "Câu chữ “把” (2) – chuyển giao",
   "Câu chữ “把” còn biểu thị thông qua hành động khiến sự vật đã xác định chuyển sang người khác. Cấu trúc: Chủ ngữ + 把 + tân ngữ 1 + động từ + 给 + tân ngữ 2.",
   [F("S:Chủ ngữ|kw:把|O1:Tân ngữ 1 (vật)|V:Động từ + 给|O2:Tân ngữ 2 (người)", [
     ("你明天再|[把]|书|还给|我", "。", "Ngày mai em hãy trả sách cho cô."),
     ("我|[把]|礼物|送给|她了", "。", "Tôi đã tặng quà cho cô ấy rồi."),
     ("请你|[把]|这本书|带给|老师", "。", "Nhờ bạn mang cuốn sách này cho thầy."),
     ("我|[把]|今天上课的笔记|发给|你吧", "。", "Mình gửi vở ghi buổi học hôm nay cho bạn nhé.")])]),
],
test=dict(
 l2=["每天读历史书|上课认真听课|看同学的笔记", "老师没讲过|女的做对了|男的觉得不太难", "考得不好|没准备考试|每天都复习"],
 l3=["学习很认真|不常写作业|让妈妈检查作业", "画画|中文歌|中国电影", "不爱看书|学习认真|每天很早回家", "快要考试了|姐姐影响了他|考试成绩不好"],
 r1=(["我想在出国前提高我的水平。", "好主意。在数学上我帮你，历史上你多帮帮我。", "你把它写在本子上，每天写几遍就记住了。", "他现在就在办公室，咱们一起去吧。", "当然。我们先坐公交车，然后换地铁。", "对。我读三年级，她读二年级。"],
     ["我有几个问题想问李老师，不知道什么时间合适。", "你为什么每天用这么多时间学外语？", "你和妹妹在一个学校读书吗？", "我总是忘了这个字怎么写。", "马上就要考试了，咱们一起复习吧。"]),
 r2=(["差", "要求", "当然", "遇到", "鞋", "清楚"],
     ["我昨天在学校门口（　　）了以前的体育老师。", "他这次考试考得很（　　），因为没认真复习。", "我在教室外面，听不（　　）老师说什么。", "A：你能帮我把这本书还给李老师吗？\nB：（　　）可以。", "A：老师（　　）我们明天把错题本拿给他。\nB：我的错题太多了，今天晚上一定写不完。"]),
 r3=[("张老师教我们外语。他上课讲得很清楚，还常在休息的时候让我们听音乐，同学们都很喜欢他。", "关于张老师，可以知道什么？", "他教音乐|他上课听音乐|学生都很喜欢他"),
     ("今天有历史课，但是我忘了带历史课本。上课时，我和同学一起看书、做练习，有点儿不方便。下次我一定会记得带。", "他今天怎么了？", "没带课本|没做练习|没上历史课"),
     ("昨天作业里的几个错题我不太明白，想问问李老师。进办公室的时候，李老师正在给别的同学讲题，我站在旁边听了一会儿，发现我想问的句子跟这几个同学一样。李老师讲得很清楚，听完我们都明白了。我把作业本放进书包里，高高兴兴地走出了办公室。",
      ("他为什么去找李老师？", "他想找作业本|他有不明白的题|李老师要给他讲题"), ("关于李老师，可以知道什么？", "在上课|在教室里等他|在给学生讲题"))],
 w1=["她一般（bǎ）这些东西放在桌子上。", "老师要求我们这个星期就开始（fù）习。", "这（jù）话我没听懂，请你再说一遍。"],
 w2=[("努力", "同学们上课都很努力，大家都举手回答问题。"), ("后年", "后年我们就要大学毕业了。"), ("对话", "两个女孩儿坐在沙发上对话，聊得很开心。")],
 gl={"11": "Mình có mấy câu muốn hỏi cô Lý, không biết lúc nào thì tiện. → D: Cô đang ở văn phòng, chúng ta đi cùng đi.",
     "12": "Sao ngày nào bạn cũng dành nhiều thời gian học ngoại ngữ vậy? → A: Mình muốn nâng trình độ trước khi ra nước ngoài.",
     "13": "Bạn và em gái học cùng một trường à? → F: Đúng. Mình học lớp ba, em ấy học lớp hai.",
     "14": "Mình cứ quên cách viết chữ này. → C: Bạn chép nó vào vở, mỗi ngày viết vài lượt là nhớ.",
     "15": "Sắp thi rồi, chúng ta cùng ôn tập nhé. → B: Ý hay. Môn Toán mình giúp bạn, Lịch sử bạn giúp mình nhé.",
     "16": "遇到了以前的体育老师 – gặp lại thầy thể dục cũ. → D 遇到.",
     "17": "考得很差 – thi rất kém. → A 差.",
     "18": "听不清楚 – nghe không rõ. → F 清楚.",
     "19": "当然可以 – đương nhiên được. → C 当然.",
     "20": "老师要求我们… – thầy yêu cầu chúng tôi… → B 要求.",
     "21": "“同学们都很喜欢他” → C.",
     "22": "“我忘了带历史课本” → A 没带课本.",
     "23": "“作业里的几个错题我不太明白” → B.",
     "24": "“李老师正在给别的同学讲题” → C."}),
)
