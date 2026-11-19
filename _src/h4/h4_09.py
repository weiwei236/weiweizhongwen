# -*- coding: utf-8 -*-
# HSK 4上 – Bài 9: 遇见你，刚刚好
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[9] = dict(zh="遇见你，刚刚好", vi="Gặp được bạn, thật vừa đúng lúc",
intro="Lý Văn tổ chức sinh nhật cho Bạch Gia Nguyệt; Vương Nhất Tuyết kể về hôn nhân hạnh phúc của em gái Vương Nhất Phi và Dương Đồng Lạc mà chị là người mai mối; bài học bàn về tình bạn, tình yêu và cách vun đắp tình cảm.",
vocab=V("""
祝|zhù|dong|chúc|祝你生日快乐！~Chúc bạn sinh nhật vui vẻ!
巧克力|qiǎokèlì|dt|sô-cô-la|她最喜欢吃巧克力。~Cô ấy thích ăn sô-cô-la nhất.
感动|gǎndòng|tt|cảm động|这个故事让我很感动。~Câu chuyện này khiến tôi rất cảm động.
浪漫|làngmàn|tt|lãng mạn|这是一个浪漫的晚上。~Đây là một buổi tối lãng mạn.
幽默|yōumò|tt|hài hước|我们的老师很幽默。~Thầy giáo của chúng tôi rất hài hước.
耐心|nàixīn|tt|kiên nhẫn; sự kiên nhẫn|她对孩子很有耐心。~Cô ấy rất kiên nhẫn với trẻ con.
吸引|xīyǐn|dong|thu hút, hấp dẫn|这本书吸引了很多读者。~Cuốn sách này thu hút rất nhiều độc giả.
当时|dāngshí|dt|lúc đó, khi ấy|当时我还在上大学。~Lúc đó tôi vẫn còn học đại học.
错过|cuòguò|dong|bỏ lỡ|别错过这么好的机会。~Đừng bỏ lỡ cơ hội tốt như vậy.
幸运|xìngyùn|tt|may mắn|能认识你，我很幸运。~Được quen bạn, tôi rất may mắn.
幸福|xìngfú|tt|hạnh phúc|祝你们生活幸福！~Chúc các bạn sống hạnh phúc!
尽管|jǐnguǎn|lien|mặc dù, tuy|尽管下着雨，他还是来了。~Mặc dù trời đang mưa, anh ấy vẫn đến.
性格|xìnggé|dt|tính cách|她的性格很开朗。~Tính cách cô ấy rất cởi mở.
共同|gòngtóng|tt|chung, cùng|我们有很多共同的爱好。~Chúng tôi có nhiều sở thích chung.
责任|zérèn|dt|trách nhiệm|照顾孩子是父母的责任。~Chăm sóc con cái là trách nhiệm của cha mẹ.
相互|xiānghù|pho|lẫn nhau, qua lại|朋友之间要相互帮助。~Giữa bạn bè phải giúp đỡ lẫn nhau.
理解|lǐjiě|dong|hiểu, thông cảm|谢谢你的理解。~Cảm ơn sự thông cảm của bạn.
支持|zhīchí|dong|ủng hộ, hỗ trợ|家人都很支持我的决定。~Gia đình đều rất ủng hộ quyết định của tôi.
印象|yìnxiàng|dt|ấn tượng|他给我留下了很好的印象。~Anh ấy để lại cho tôi ấn tượng rất tốt.
实在|shízài|tt|thật thà, chân thật; thật sự|他是一个很实在的人。~Anh ấy là một người rất thật thà.
阳光|yángguāng|tt|tươi sáng, năng động; ánh nắng|这个男孩儿很阳光。~Cậu bé này rất năng động, tươi sáng.
负责|fùzé|tt|có trách nhiệm; phụ trách|他工作很负责。~Anh ấy làm việc rất có trách nhiệm.
积极|jījí|tt|tích cực|她上课时回答问题很积极。~Trong giờ học cô ấy trả lời câu hỏi rất tích cực.
此|cǐ|dai|này, cái này|此事我已经知道了。~Việc này tôi đã biết rồi.
从此|cóngcǐ|pho|từ đó, từ đây|从此，他们成了好朋友。~Từ đó, họ trở thành bạn tốt.
产生|chǎnshēng|dong|nảy sinh, sinh ra|他对中文产生了兴趣。~Anh ấy nảy sinh hứng thú với tiếng Trung.
爱情|àiqíng|dt|tình yêu|这是一个关于爱情的故事。~Đây là một câu chuyện về tình yêu.
间|jiān|dt|giữa, khoảng giữa|同事间要互相帮助。~Giữa đồng nghiệp phải giúp đỡ nhau.
友情|yǒuqíng|dt|tình bạn|我们的友情很深。~Tình bạn của chúng tôi rất sâu sắc.
美好|měihǎo|tt|tốt đẹp|祝你有一个美好的未来。~Chúc bạn có một tương lai tốt đẹp.
人生|rénshēng|dt|đời người, cuộc đời|人生中有很多选择。~Trong cuộc đời có rất nhiều lựa chọn.
精彩|jīngcǎi|tt|đặc sắc, tuyệt vời|昨天的比赛非常精彩。~Trận đấu hôm qua vô cùng hấp dẫn.
感情|gǎnqíng|dt|tình cảm|他们俩的感情很好。~Tình cảm của hai người họ rất tốt.
深|shēn|tt|sâu, sâu đậm|这件事给我的印象很深。~Việc này để lại cho tôi ấn tượng rất sâu.
经营|jīngyíng|dong|kinh doanh, vun đắp, quản lý|他经营着一家小饭馆。~Anh ấy kinh doanh một quán ăn nhỏ.
对方|duìfāng|dt|đối phương, bên kia|我们要多听听对方的想法。~Chúng ta nên lắng nghe suy nghĩ của người kia nhiều hơn.
感受|gǎnshòu|dt|cảm nhận, cảm giác|说说你的感受吧。~Nói cảm nhận của bạn đi.
尤其|yóuqí|pho|đặc biệt là, nhất là|我喜欢运动，尤其是游泳。~Tôi thích thể thao, nhất là bơi lội.
日子|rìzi|dt|ngày, cuộc sống|我们的日子越过越好。~Cuộc sống của chúng tôi ngày càng tốt hơn.
从来|cónglái|pho|từ trước đến nay|他从来不迟到。~Từ trước đến nay anh ấy chưa bao giờ đến muộn.
"""),
texts=[dict(t="课文1", scene="在餐馆里，李文给白家月过生日。", scene_vi="Trong nhà hàng, Lý Văn tổ chức sinh nhật cho Bạch Gia Nguyệt.", narr=False, lines=T("""
李文>家月，给你的，祝你生日快乐！|Gia Nguyệt, tặng cậu, chúc cậu sinh nhật vui vẻ!
白家月>啊，好漂亮的花！还有巧克力！你怎么知道我喜欢这个巧克力？|A, hoa đẹp quá! Còn có sô-cô-la nữa! Sao cậu biết mình thích loại sô-cô-la này?
李文>上次咱们去超市，看你拿起来看了看又放下了，我就记住了。|Lần trước chúng mình đi siêu thị, thấy cậu cầm lên xem rồi lại đặt xuống, mình liền nhớ luôn.
白家月>好感动！我不说你也懂我在想什么，你真是细心又浪漫。其实刚认识不久，你的幽默与耐心就很吸引我，不过我当时也只把你当普通朋友。如果你没有一直找我聊天儿，我们可能就错过了。|Cảm động quá! Mình không nói cậu cũng hiểu mình nghĩ gì, cậu thật là chu đáo lại lãng mạn. Thật ra quen nhau chưa lâu, sự hài hước và kiên nhẫn của cậu đã thu hút mình, nhưng lúc đó mình chỉ coi cậu là bạn bình thường. Nếu cậu không luôn tìm mình trò chuyện, có lẽ chúng mình đã bỏ lỡ nhau rồi.
李文>我终于遇见了对的人，哪能错过呢？|Cuối cùng mình đã gặp được đúng người, sao có thể bỏ lỡ được chứ?
白家月>遇见你，我也觉得很幸运。|Gặp được cậu, mình cũng thấy rất may mắn.
"""), q=Q("""
白家月过生日时，李文送了什么生日礼物？|花和巧克力。|Hoa và sô-cô-la.
李文是怎么知道白家月喜欢那个巧克力的？|上次去超市时，他看到白家月拿起来看了看又放下了。|Lần trước đi siêu thị, cậu thấy Gia Nguyệt cầm lên xem rồi lại đặt xuống.
白家月认为李文是个什么样的人？|细心又浪漫，还很幽默、有耐心。|Chu đáo, lãng mạn, lại hài hước và kiên nhẫn.
白家月是怎么被李文吸引住的？|刚认识不久，李文的幽默与耐心就很吸引她。|Mới quen chưa lâu, sự hài hước và kiên nhẫn của Lý Văn đã thu hút cô.
""")),
 dict(t="课文2", scene="在家里，王一雪和刘明谈论王一飞和杨同乐的婚姻。", scene_vi="Ở nhà, Vương Nhất Tuyết và Lưu Minh nói chuyện về cuộc hôn nhân của Vương Nhất Phi và Dương Đồng Lạc.", narr=False, lines=T("""
王一雪>看到一飞和同乐结婚后这么幸福，我这个介绍人也特别开心。|Thấy Nhất Phi và Đồng Lạc cưới nhau rồi hạnh phúc như vậy, em là người mai mối cũng đặc biệt vui.
刘明>是啊，同乐是你的好朋友，一飞是你妹妹，你都很了解。|Đúng vậy, Đồng Lạc là bạn tốt của em, Nhất Phi là em gái em, em đều rất hiểu họ.
王一雪>嗯，他们尽管性格不同，但是有很多共同爱好。特别是同乐人好，性格也好，很有责任感。|Ừ, tuy tính cách họ khác nhau nhưng có nhiều sở thích chung. Đặc biệt Đồng Lạc là người tốt, tính tình cũng tốt, rất có trách nhiệm.
刘明>是的，一飞也算在对的时间遇到了对的人。后边的路还很长，希望他们能一直相互理解、相互支持。|Phải, Nhất Phi cũng coi như gặp đúng người vào đúng lúc. Con đường phía trước còn dài, hy vọng họ luôn hiểu nhau, ủng hộ lẫn nhau.
王一雪>我了解同乐，更了解一飞，相信他们会一直走下去的。|Em hiểu Đồng Lạc, càng hiểu Nhất Phi, tin rằng họ sẽ mãi đi cùng nhau.
刘明>祝他们越来越幸福。|Chúc họ ngày càng hạnh phúc.
"""), q=Q("""
王一飞和杨同乐结婚后怎么样？|非常幸福。|Rất hạnh phúc.
杨同乐和王一飞为什么能成为夫妻？|因为他们有很多共同爱好，杨同乐人好，性格也好，很有责任感。|Vì họ có nhiều sở thích chung, Đồng Lạc là người tốt, tính tình tốt, rất có trách nhiệm.
刘明对王一飞和杨同乐有什么希望？|希望他们能一直相互理解、相互支持。|Hy vọng họ luôn hiểu nhau, ủng hộ lẫn nhau.
王一雪为什么相信他们“会一直走下去的”？|因为她了解同乐，更了解一飞。|Vì cô hiểu Đồng Lạc, càng hiểu Nhất Phi.
""")),
 dict(t="课文3", scene="杨同乐的双份幸运", scene_vi="Niềm may mắn nhân đôi của Dương Đồng Lạc", narr=True, lines=T("""
王一雪比杨同乐更早进入公司。|Vương Nhất Tuyết vào công ty sớm hơn Dương Đồng Lạc.
杨同乐刚来不久，王一雪对他印象就非常好：人很实在，性格阳光，工作负责，表现积极……|Dương Đồng Lạc mới đến chưa lâu, Vương Nhất Tuyết đã có ấn tượng rất tốt về anh: thật thà, tính cách tươi sáng, làm việc có trách nhiệm, biểu hiện tích cực…
后来他们一起出了次差，此次出差，让两人熟悉了起来，从此成了好朋友。|Sau đó họ cùng đi công tác một lần, chuyến công tác này khiến hai người trở nên thân quen, từ đó thành bạn tốt.
一次聊天儿时，王一雪了解到杨同乐还没女朋友，正好自己的妹妹王一飞也没有男朋友，于是王一雪就把王一飞介绍给了他。|Một lần trò chuyện, Vương Nhất Tuyết biết Dương Đồng Lạc vẫn chưa có bạn gái, vừa hay em gái mình là Vương Nhất Phi cũng chưa có bạn trai, thế là chị giới thiệu Nhất Phi cho anh.
杨同乐和王一飞认识后，很聊得来，两人之间慢慢产生了爱情，最后成了夫妻。|Dương Đồng Lạc và Vương Nhất Phi quen nhau rồi rất hợp chuyện, giữa hai người dần nảy sinh tình yêu, cuối cùng thành vợ chồng.
杨同乐说自己很幸运，和王一雪这份同事间的友情，给他带来了美好的爱情。|Dương Đồng Lạc nói mình rất may mắn, tình bạn đồng nghiệp với Vương Nhất Tuyết đã mang đến cho anh một tình yêu tốt đẹp.
"""), q=Q("""
杨同乐进入公司后，王一雪对他的印象怎么样？|非常好：人很实在，性格阳光，工作负责，表现积极。|Rất tốt: thật thà, tính cách tươi sáng, làm việc có trách nhiệm, biểu hiện tích cực.
王一雪和杨同乐是怎么熟悉起来的？|一起出差。|Cùng đi công tác.
王一雪为什么把王一飞介绍给杨同乐？|因为杨同乐还没女朋友，王一飞也没有男朋友。|Vì Đồng Lạc chưa có bạn gái, Nhất Phi cũng chưa có bạn trai.
杨同乐为什么感觉自己很幸运？|因为和王一雪同事间的友情，给他带来了美好的爱情。|Vì tình bạn đồng nghiệp với Vương Nhất Tuyết mang đến cho anh tình yêu tốt đẹp.
""")),
 dict(t="课文4", scene="爱更需要经营", scene_vi="Tình yêu càng cần được vun đắp", narr=True, lines=T("""
李文在校园里遇见白家月，从此，他们的人生变得更加精彩；|Lý Văn gặp Bạch Gia Nguyệt trong khuôn viên trường, từ đó cuộc đời họ trở nên rực rỡ hơn;
王一飞和杨同乐通过王一雪介绍认识后，感情越来越深，最后两人幸福地走到了一起。|Vương Nhất Phi và Dương Đồng Lạc quen nhau qua sự giới thiệu của Vương Nhất Tuyết, tình cảm ngày càng sâu đậm, cuối cùng hai người hạnh phúc về chung một nhà.
在我看来，遇见爱情的方式并不重要，重要的是在合适的时间遇到了合适的人。遇见你，刚刚好。|Theo tôi, cách gặp được tình yêu không quan trọng, quan trọng là gặp đúng người vào đúng thời điểm. Gặp được bạn, thật vừa đúng lúc.
不过美好的遇见只是爱的开始，爱更需要经营。|Có điều cuộc gặp gỡ đẹp đẽ chỉ là khởi đầu của tình yêu, tình yêu càng cần được vun đắp.
在一段感情中，两个人要多关注对方的感受，尤其是结婚后，更要共同经营好家庭，日子才能越过越好。|Trong một mối quan hệ, hai người phải quan tâm nhiều hơn đến cảm nhận của đối phương, nhất là sau khi kết hôn, càng phải cùng nhau vun đắp gia đình, cuộc sống mới ngày càng tốt đẹp.
爱，从来都是相互尊重、理解与支持，不是吗？|Tình yêu, từ trước đến nay luôn là sự tôn trọng, thấu hiểu và ủng hộ lẫn nhau, phải không?
"""), q=Q("""
李文是在哪儿遇见白家月的？|校园里。|Trong khuôn viên trường.
遇见爱情的方式并不重要，重要的是什么？|在合适的时间遇到了合适的人。|Gặp đúng người vào đúng thời điểm.
“遇见你，刚刚好”是什么意思？|在合适的时间遇到合适的人。|Gặp đúng người vào đúng lúc.
爱需要怎样经营？|两个人要多关注对方的感受，结婚后更要共同经营好家庭。|Hai người phải quan tâm cảm nhận của nhau, sau khi kết hôn càng phải cùng vun đắp gia đình.
""")),
],
grammar=[
 G("buye", "紧缩复句“不……也……”", "Câu phức rút gọn “不……也……”",
   "Biểu thị dù ở điều kiện phủ định nào đó thì kết quả phía sau vẫn chắc chắn như vậy: “không… cũng…”. Thường dùng trong khẩu ngữ.",
   [F("S:Chủ ngữ|kw:不|X:Điều kiện phủ định|kw2:也|V:Kết quả chắc chắn", [
     ("我|[不]|说|你[也]|懂我在想什么", "。", "Mình không nói cậu cũng hiểu mình đang nghĩ gì."),
     ("他|[不]|复习|[也]|能考出好成绩", "。", "Anh ấy không ôn bài cũng thi được điểm tốt."),
     ("我很清楚他为什么生气，|[不]|问|我[也]|知道", "。", "Tôi biết rõ vì sao anh ấy giận, không hỏi tôi cũng biết.")])]),
 G("jinguan", "转折复句“尽管……，但是/可是……”", "Câu phức chuyển ngoặt “尽管……，但是 / 可是……”",
   "“尽管” mang nghĩa như “虽然” (mặc dù), dùng để dẫn ra một tình huống; “但是、可是” dẫn ra tình huống hay kết quả trái ngược.",
   [F("S:(Chủ ngữ)|kw:尽管|X:Tình huống|kw2:但是 / 可是|V:Kết quả trái ngược", [
     ("他们|[尽管]|性格不同|[但是]|有很多共同爱好", "。", "Tuy tính cách họ khác nhau, nhưng có nhiều sở thích chung."),
     ("|[尽管]|时间紧张、压力很大|[但是]|他们还是完成了任务", "。", "Mặc dù thời gian gấp gáp, áp lực lớn, nhưng họ vẫn hoàn thành nhiệm vụ."),
     ("|[尽管]|她已经很累了|[可是]|还是很耐心地给女儿读睡前故事", "。", "Dù đã rất mệt, cô ấy vẫn kiên nhẫn đọc truyện trước khi ngủ cho con gái.")])]),
 G("ci", "指示代词“此”", "Đại từ chỉ thị “此”",
   "“此” nghĩa là “này, cái này” (这、这个), thường dùng trong văn viết hoặc ngữ cảnh trang trọng.",
   [F("kw:此|N:Danh từ|V:Vị ngữ", [
     ("[此]|次出差|让两人熟悉了起来，从此成了好朋友", "。", "Chuyến công tác này khiến hai người trở nên thân quen, từ đó thành bạn tốt."),
     ("[此]|人|聪明、有能力，一定能顺利完成任务", "。", "Người này thông minh, có năng lực, nhất định sẽ hoàn thành nhiệm vụ thuận lợi."),
     ("[此]|材料|很重要，必须直接交给他", "。", "Tài liệu này rất quan trọng, phải giao trực tiếp cho anh ấy.")])]),
 G("conglai", "时间副词“从来”", "Phó từ thời gian “从来”",
   "“从来” chỉ việc từ quá khứ đến hiện tại vẫn luôn như vậy: “từ trước đến nay”. Thường dùng trong câu phủ định (从来不 / 从来没), đôi khi dùng trong câu khẳng định (从来都…).",
   [F("S:Chủ ngữ|kw:从来|D:都 / 不 / 没|V:Vị ngữ", [
     ("爱，|[从来]|都|是相互尊重、理解与支持，不是吗", "？", "Tình yêu, từ trước đến nay luôn là sự tôn trọng, thấu hiểu và ủng hộ lẫn nhau, phải không?"),
     ("我|[从来]|没|见过这个颜色的花，它叫什么名字啊", "？", "Tôi chưa từng thấy loài hoa màu này, nó tên là gì vậy?"),
     ("我|[从来]|不|喜欢一个人旅游，每次都要和家人或朋友一起去", "。", "Tôi từ trước đến nay không thích đi du lịch một mình, lần nào cũng đi cùng gia đình hoặc bạn bè.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["祝", "尤其", "性格", "吸引", "负责"], [
   "这次比赛【吸引】了很多同学参加，大家都表现得非常积极。", "我特别喜欢吃水果，【尤其】喜欢吃香蕉。", "今天是妈妈的生日，我和爸爸给她买了生日蛋糕，一起给她唱生日歌，【祝】她永远年轻、美丽。",
   "人要对自己说过的话【负责】，说到就一定要做到。", "这位新同事做事积极，【性格】也很好，大家都很喜欢她。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["日子", "感受", "感情", "深", "爱情"], [
   "A：他们夫妻两人的【感情】一直特别好。 B：是的，他们家真是一个幸福的家庭。", "A：你结婚的【日子】定了吗？ B：嗯，定在了下周六，到时候你一定要来啊！",
   "A：我希望自己遇见的【爱情】简单、美好，你呢？ B：我的想法和你一样，我也希望遇到简单的人，结婚后过简单的日子。", "A：我记得第一次看这个电影时，我都感动得哭了。 B：嗯，我对它的印象也很【深】。",
   "A：看完刚才的足球比赛，你有什么【感受】？ B：我觉得球员们踢得很精彩，尤其是8号，表现特别好。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["于是她们相互加了微信", "后来去了不同城市上大学", "尽管这么多年过去了", "她看了好一会儿"], [
   "去年，我刷短视频时看到有个人发了很多老照片，照片里有个女孩儿特别像我妈妈。我给妈妈看了这个视频，【她看了好一会儿】，说那就是她。原来那些照片是她和她以前的好朋友小江一起拍的。她们从小一起长大，【后来去了不同城市上大学】，从此就慢慢失去了联系。我跟发视频的人联系了一下，对方马上向我要了妈妈的微信号，【于是她们相互加了微信】。从此，她们常在网上聊天儿，好像回到了年轻时。妈妈说，【尽管这么多年过去了】，但是她们还能联系上，而且美好的友情还在，她觉得很幸运。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：昨天你怎么没吃晚饭？ B：我中午吃得太饱了，晚上______也不饿。（不……也……）", "我中午吃得太饱了，晚上不吃也不饿。"),
   ("A：今天和老同学的聚餐怎么样？ B：尽管很久没见了，______。", "尽管很久没见了，但是大家还是像以前一样聊得很开心。"),
   ("此项工作交给你，______。（负责）", "此项工作交给你，你要认真负责。"),
   ("她性格很好，______。（从来）", "她性格很好，从来不跟别人生气。")]),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l9", items=[
   ("精彩", "这场篮球比赛非常精彩。"), ("友情", "她们是多年的好朋友，友情很深。"), ("错过", "他来晚了，错过了这班飞机。")]),
])
