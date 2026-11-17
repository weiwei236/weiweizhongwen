# -*- coding: utf-8 -*-
# HSK 3 – Bài 14: 这本书被别人借走了
from gtb_gen import V, T, Q, F, G
B = {}

B[14] = dict(zh="这本书被别人借走了", vi="Cuốn sách này bị người khác mượn mất rồi",
intro="Lý Văn nhờ Bạch Gia Nguyệt trả sách giúp ở thư viện, nhưng thẻ sinh viên của cô lại không thấy đâu. Rồi cả nhóm chuẩn bị tiết mục cho dạ hội năm mới của trường.",
vocab=V("""
词典|cídiǎn|dt|từ điển|这本词典很有用。~Cuốn từ điển này rất hữu ích.
最好|zuìhǎo|pho|tốt nhất|你最好早点儿去。~Bạn tốt nhất nên đi sớm một chút.
节|jié|lg|tiết, giờ (học)|我今天上午有三节课。~Sáng nay tôi có ba tiết học.
图书馆|túshūguǎn|dt|thư viện|我常去图书馆看书。~Tôi hay đến thư viện đọc sách.
被|bèi|gioi|bị, được|我的自行车被弟弟骑走了。~Xe đạp của tôi bị em trai đạp đi mất rồi.
名人|míngrén|dt|người nổi tiếng, danh nhân|他是一个很有名的名人。~Ông ấy là một người rất nổi tiếng.
故事|gùshi|dt|câu chuyện|奶奶给我讲了一个故事。~Bà kể cho tôi một câu chuyện.
然后|ránhòu|lien|sau đó|我们先吃饭，然后去看电影。~Chúng ta ăn cơm trước, sau đó đi xem phim.
报纸|bàozhǐ|dt|báo, tờ báo|爷爷每天早上看报纸。~Ông nội sáng nào cũng đọc báo.
忘记|wàngjì|dong|quên|我忘记带钥匙了。~Tôi quên mang chìa khóa rồi.
电子书|diànzǐshū|dt|sách điện tử|现在很多人喜欢看电子书。~Bây giờ nhiều người thích đọc sách điện tử.
女生|nǚshēng|dt|nữ sinh|我们班有十个女生。~Lớp chúng tôi có mười bạn nữ.
表演|biǎoyǎn|dong|biểu diễn, diễn|她在晚会上表演了一个节目。~Cô ấy biểu diễn một tiết mục ở dạ hội.
节目|jiémù|dt|tiết mục|今天的节目很精彩。~Các tiết mục hôm nay rất hay.
怎么办|zěnme bàn|cum|làm (như) thế nào|钱包丢了，怎么办？~Mất ví rồi, làm sao bây giờ?
校长|xiàozhǎng|dt|hiệu trưởng|校长在办公室等你。~Thầy hiệu trưởng đang đợi bạn ở văn phòng.
面前|miànqián|dt|phía trước, trước mặt|他站在大家面前唱歌。~Anh ấy đứng trước mặt mọi người hát.
有些|yǒuxiē|pho|có một vài, có một số; hơi|我今天有些累。~Hôm nay tôi hơi mệt.
相信|xiāngxìn|dong|tin, tin tưởng, tin rằng|我相信你一定能考好。~Tôi tin bạn nhất định sẽ thi tốt.
新年|xīnnián|dt|năm mới|新年快乐！~Chúc mừng năm mới!
班级|bānjí|dt|lớp học, cấp học|每个班级都有一个节目。~Lớp nào cũng có một tiết mục.
跳|tiào|dong|nhảy, khiêu vũ|孩子们高兴得跳了起来。~Bọn trẻ vui đến nhảy cẫng lên.
留学生|liúxuéshēng|dt|lưu học sinh|我们学校有很多留学生。~Trường chúng tôi có rất nhiều du học sinh.
最后|zuìhòu|dt|cuối cùng|最后一个问题有点儿难。~Câu hỏi cuối cùng hơi khó.
一块儿|yíkuàir|pho|cùng, cùng nhau, cùng một chỗ|我们一块儿去吃饭吧。~Chúng ta cùng đi ăn đi.
网站|wǎngzhàn|dt|trang web|这个网站上有很多学习资料。~Trang web này có nhiều tài liệu học tập.
视频|shìpín|dt|đoạn phim, video|我在网上看了一个有意思的视频。~Tôi xem một video thú vị trên mạng.
"""),
texts=[dict(t="课文1", scene="在校园餐厅，李文和白家月在聊天儿。", scene_vi="Lý Văn và Bạch Gia Nguyệt đang trò chuyện trong căng tin trường.", narr=False, lines=T("""
李文>我借的这本词典最好今天还，但是我没时间去。|Cuốn từ điển mình mượn tốt nhất là trả hôm nay, nhưng mình không có thời gian đi.
白家月>下午我只有两节课，可以帮你去图书馆还书。|Chiều nay mình chỉ có hai tiết, có thể giúp cậu đi thư viện trả sách.
李文>那太谢谢了。你能再帮我借本书吗？|Vậy cảm ơn cậu nhiều. Cậu có thể mượn giúp mình một cuốn sách nữa không?
白家月>行，你告诉我书名。|Được, cậu cho mình biết tên sách.
李文>我把名字写在纸上吧。我去了好几次图书馆，这本书都被别人借走了。|Để mình viết tên lên giấy. Mình đến thư viện mấy lần rồi, cuốn này đều bị người khác mượn mất.
白家月>《名人的故事》？我有这本书。明天我借给你吧。|“Câu chuyện danh nhân”? Mình có cuốn này. Mai mình cho cậu mượn nhé.
"""), q=Q("""
李文请白家月帮他借什么书？|《名人的故事》。|“Câu chuyện danh nhân”.
李文为什么没借到这本书？|因为这本书都被别人借走了。|Vì cuốn sách đều bị người khác mượn mất.
李文把书名写在哪儿了？|写在纸上了。|Viết lên giấy.
""")),
 dict(t="课文2", scene="在校园里，白家月和安妮在聊天儿。", scene_vi="Bạch Gia Nguyệt và Annie đang trò chuyện trong khuôn viên trường.", narr=False, lines=T("""
安妮>今天下课早，你一会儿做什么？|Hôm nay tan học sớm, lát nữa cậu làm gì?
白家月>我今天忙得很，要先去图书馆借书，然后去游泳。|Hôm nay mình bận lắm, phải đi thư viện mượn sách trước, sau đó đi bơi.
安妮>咱们一起走吧，我想去图书馆看看中文报纸。|Chúng ta đi cùng nhé, mình muốn đến thư viện đọc báo tiếng Trung.
白家月>等等，我的校园卡不见了，没有卡进不去图书馆。|Đợi đã, thẻ sinh viên của mình không thấy đâu, không có thẻ không vào thư viện được.
安妮>你想想上一次用是什么时候？|Cậu nghĩ xem lần trước dùng là lúc nào?
白家月>我忘记了，可能被我放在家里了。|Mình quên mất rồi, có lẽ mình để ở nhà.
安妮>进不去图书馆也没关系，上网看看有没有电子书。|Không vào được thư viện cũng không sao, lên mạng xem có sách điện tử không.
白家月>不行，我必须去，我还得帮李文还书呢。|Không được, mình phải đi, mình còn phải trả sách giúp Lý Văn nữa.
"""), q=Q("""
下课以后安妮要做什么？|去图书馆看看中文报纸。|Đến thư viện đọc báo tiếng Trung.
白家月为什么不能进图书馆？|因为她的校园卡不见了。|Vì thẻ sinh viên của cô ấy không thấy đâu.
白家月觉得校园卡可能在哪儿？|可能被她放在家里了。|Có lẽ để ở nhà.
""")),
 dict(t="课文3", scene="在校园餐厅，李文和白家月边吃边聊。", scene_vi="Lý Văn và Bạch Gia Nguyệt vừa ăn vừa trò chuyện trong căng tin trường.", narr=False, lines=T("""
李文>下周学校有晚会，你知道吗？|Tuần sau trường có dạ hội, cậu biết không?
白家月>知道，我和几个女生要表演一个节目。你也参加吗？|Biết chứ, mình với mấy bạn nữ sẽ biểu diễn một tiết mục. Cậu cũng tham gia à?
李文>我想唱中文歌，但是还没找到人一起表演，不知道怎么办。|Mình muốn hát bài tiếng Trung, nhưng chưa tìm được người cùng biểu diễn, không biết làm sao.
白家月>找不到人，你就一个人唱吧。|Không tìm được người thì cậu hát một mình đi.
李文>一想到要在校长、老师和那么多同学面前表演，我就有些紧张。|Cứ nghĩ đến phải biểu diễn trước mặt hiệu trưởng, thầy cô và bao nhiêu bạn học, mình lại hơi hồi hộp.
白家月>紧张什么啊，我们都喜欢听你唱歌，你要相信自己。|Hồi hộp gì chứ, bọn mình đều thích nghe cậu hát, cậu phải tin vào bản thân.
"""), q=Q("""
白家月要在晚会上做什么？|和几个女生表演一个节目。|Cùng mấy bạn nữ biểu diễn một tiết mục.
李文为什么紧张？|因为要在校长、老师和那么多同学面前表演。|Vì phải biểu diễn trước mặt hiệu trưởng, thầy cô và nhiều bạn.
听说李文有点儿紧张，白家月是怎么说的？|紧张什么啊，我们都喜欢听你唱歌，你要相信自己。|Hồi hộp gì chứ, mọi người đều thích nghe cậu hát, hãy tin vào bản thân.
""")),
 dict(t="课文4", scene="在家里，白家月在写日记。", scene_vi="Bạch Gia Nguyệt đang viết nhật ký ở trong nhà.", narr=True, lines=T("""
昨天是我们学校的新年晚会，每个班级的同学都表演节目了。|Hôm qua là dạ hội năm mới của trường, các bạn ở mỗi lớp đều biểu diễn tiết mục.
晚会是八点开始的，差不多十二点才结束。|Dạ hội bắt đầu lúc tám giờ, gần mười hai giờ mới kết thúc.
我一个晚上跟大家一起又唱又跳，开心极了，也累坏了。|Cả buổi tối tôi cùng mọi người vừa hát vừa nhảy, vui cực kỳ, cũng mệt rã rời.
我最喜欢的节目是留学生们跳舞，|Tiết mục tôi thích nhất là các du học sinh nhảy,
最后老师和校长也被叫起来一块儿跳，特别有意思。|cuối cùng thầy cô và hiệu trưởng cũng được kéo lên nhảy cùng, cực kỳ thú vị.
过几天学校的网站上会有晚会的视频，我打算再看一遍。|Vài hôm nữa trên trang web của trường sẽ có video dạ hội, tôi định xem lại một lượt.
"""), q=Q("""
晚会是什么时候开始的？什么时候结束的？|八点开始的，差不多十二点才结束。|Bắt đầu 8 giờ, gần 12 giờ mới kết thúc.
白家月最喜欢哪个节目？为什么？|留学生们跳舞，因为最后老师和校长也被叫起来一块儿跳，特别有意思。|Du học sinh nhảy, vì cuối cùng thầy cô và hiệu trưởng cũng nhảy cùng, rất thú vị.
过几天白家月打算做什么？|在学校网站上再看一遍晚会的视频。|Xem lại video dạ hội trên trang web trường.
"""))],
grammar=[
 G("bei1", "被动句（1）", "Câu bị động (1) – câu chữ “被”",
   "Câu dùng “被” diễn đạt nghĩa bị động, nhấn mạnh chủ ngữ chịu ảnh hưởng của một hành động, ngữ khí thường mang sắc thái bị động, bất lực hoặc tiêu cực. Phó từ và động từ năng nguyện đặt trước “被”; tân ngữ sau “被” có thể lược bỏ. Cấu trúc: Chủ ngữ + 被 + tân ngữ + động từ + thành phần khác.",
   [F("S:Chủ ngữ (+ phó từ / năng nguyện)|kw:被|O:(Tân ngữ – người làm)|V:Động từ + thành phần khác", [
     ("这本书|[被]|别人|借走了", "。", "Cuốn sách này bị người khác mượn mất rồi."),
     ("水果可能|[被]|弟弟|吃了", "。", "Hoa quả có lẽ bị em trai ăn mất rồi."),
     ("我们俩经常|[被]||叫错名字", "。", "Hai đứa chúng tôi hay bị gọi nhầm tên."),
     ("校园卡可能|[被]|我|放在家里了", "。", "Thẻ sinh viên có lẽ bị tôi để ở nhà rồi.")])]),
 G("xianzai", "承接复句“先……，再/然后……”", "Câu ghép tiếp nối “先……，再/然后……”",
   "Trong câu ghép tiếp nối “先……，再/然后……”, hai vế biểu thị thứ tự trước sau của hành động (trước… rồi / sau đó…).",
   [F("S:(Chủ ngữ)|kw:先|V1:Việc 1|kw2:再 / 然后|V2:Việc 2", [
     ("我要|[先]|去图书馆借书，|[然后]|去游泳", "。", "Tôi phải đi thư viện mượn sách trước, sau đó đi bơi."),
     ("你|[先]|去买门票，|[再]|来这里找我", "。", "Bạn đi mua vé trước rồi đến đây tìm tôi."),
     ("你们|[先]|回房间休息一会儿，|[然后]|再出来吃晚饭", "。", "Các bạn về phòng nghỉ một lát, sau đó ra ăn tối.")])]),
 G("shenmea", "固定格式“×什么（啊）”", "Cấu trúc cố định “× 什么 (啊)”",
   "Cấu trúc “× 什么（啊）” (× là động từ / tính từ người kia vừa nói) thường dùng để phủ định sự lo lắng, hoài nghi của đối phương hoặc nhấn mạnh sự thật, mang ngữ khí phản bác hoặc an ủi (… gì chứ).",
   [F("X:Động từ / tính từ (lặp lại)|kw:什么（啊）|C:Lời phản bác / an ủi", [
     ("紧张|[什么啊]|，我们都喜欢听你唱歌，你要相信自己", "。", "Hồi hộp gì chứ, bọn mình đều thích nghe cậu hát, hãy tin vào bản thân."),
     ("胖|[什么啊]|，你看起来不胖也不瘦", "。", "Béo gì đâu, trông bạn không béo cũng không gầy."),
     ("急|[什么啊]|，马上就到了", "。", "Vội gì chứ, sắp tới nơi rồi."),
     ("远|[什么啊]|，走路十几分钟就到了", "。", "Xa gì đâu, đi bộ mười mấy phút là tới.")])]),
],
test=dict(
 l2=["跳舞|唱外语歌|历史故事", "用手机听书|去书店买书|去图书馆借书", "用字典|选字典|参加考试"],
 l3=["看书|听外语故事|找人帮助她", "在老师那儿|在图书馆里|被别人借走了", "边走边学|在网上学习|在教室里学习", "很方便|没意思|让人不开心"],
 r1=(["我有一个，不常用，我借给你吧。", "我也不知道，我有事很早就离开了。", "我的电脑打不开那个视频，怎么办？", "我昨天去找了，这几本书都被别人借走了。", "当然。我们先坐公交车，然后换地铁。", "一本介绍中国历史和文化的电子书。"],
     ["你在看什么呢？", "这本词典太旧了，我想买个电子词典。", "昨天的新年晚会是几点结束的？", "老师说先看视频，再开始写作业。", "你不用去书店，图书馆有这些书。"]),
 r2=(["最好", "忘记", "怎么办", "面前", "鞋", "有些"],
     ["昨天的作业我（　　）写了，老师会不会不高兴？", "来看我们表演节目的人太多了，我们都（　　）紧张。", "昨天的晚会上，我第一次在同学们（　　）跳了一个舞。", "A：我借的那本书不见了，（　　）？\nB：我刚才还看见了，我跟你一块儿去教室里找找。", "A：我想学好中文，你有什么好办法？\nB：你（　　）每天读一会儿中文书，或者看一些中文视频。"]),
 r3=[("我们班的新年晚会很有意思，有很多节目。除了同学们表演了节目，老师们也一起跳了一个舞。", "关于新年晚会，可以知道什么？", "节目不多|老师唱歌了|晚会有意思"),
     ("我的汉语词典被弟弟拿走了，老师让我们用词典学汉字，我现在不知道怎么办。", "他遇到什么问题了？", "他不想写作业|老师不让用词典|词典被弟弟拿走了"),
     ("我们学校的图书馆很大，有很多种语言的书，中文书是最多的。有的书我们可以借回家看，有的书只能在图书馆里看。现在越来越多的学生喜欢看电子书，所以图书馆的网站上也准备了很多电子书。学生不用来图书馆，在家里打开电脑或者手机就可以借到自己想看的书。",
      ("关于图书馆，可以知道：", "比较小|有不少中文书|书都可以借回家"), ("学生可以怎么借电子书？", "去书店借|去图书馆借|自己在网站上借"))],
 w1=["老师一直相（xìn）我们能学好中文。", "我很喜欢听妈妈讲我小时候的（gù）事。", "那个女生在电影里表演得特别好，所以她（bèi）大家记住了。"],
 w2=[("一块儿", "同学们在图书馆里一块儿看书、做作业。"), ("最后", "表演最后，大家一起站在台上。"), ("忘记", "她忘记带书了，正在包里找。")],
 gl={"11": "Bạn đang đọc gì vậy? → F: Một cuốn sách điện tử giới thiệu lịch sử và văn hóa Trung Quốc.",
     "12": "Cuốn từ điển này cũ quá, mình muốn mua từ điển điện tử. → A: Mình có một cái, ít dùng, cho bạn mượn nhé.",
     "13": "Dạ hội năm mới hôm qua mấy giờ kết thúc? → B: Mình cũng không biết, mình có việc nên về sớm.",
     "14": "Thầy nói xem video trước, rồi mới làm bài tập. → C: Máy tính mình không mở được video đó, làm sao bây giờ?",
     "15": "Bạn không cần đi hiệu sách, thư viện có những sách này. → D: Hôm qua mình đi tìm rồi, mấy cuốn này đều bị người khác mượn mất.",
     "16": "我忘记写了 – tôi quên làm rồi. → B 忘记.",
     "17": "有些紧张 – hơi hồi hộp. → F 有些.",
     "18": "在同学们面前 – trước mặt các bạn. → D 面前.",
     "19": "怎么办 – làm sao bây giờ. → C 怎么办.",
     "20": "你最好每天读… – tốt nhất bạn nên mỗi ngày đọc… → A 最好.",
     "21": "“我们班的新年晚会很有意思” → C.",
     "22": "“我的汉语词典被弟弟拿走了” → C.",
     "23": "“中文书是最多的” → B 有不少中文书.",
     "24": "“在家里打开电脑或者手机就可以借到” → C 自己在网站上借."}),
)
