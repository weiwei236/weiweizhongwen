# -*- coding: utf-8 -*-
# HSK 4下 – Bài 12: 幸福的家庭
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[12] = dict(zh="幸福的家庭", vi="Gia đình hạnh phúc",
intro="Dương Đồng Lạc và Vương Nhất Phi mua áo len cho mẹ; nhà Lưu Minh nói chuyện con trai cáu với bà; hai gia đình chăm lo cho cha mẹ già; Lâm Tĩnh Tĩnh cảm nhận “hương vị hạnh phúc” từ nồi canh gà bố mẹ gửi lên.",
vocab=V("""
毛衣|máoyī|dt|áo len|天冷了，多穿一件毛衣吧。~Trời lạnh rồi, mặc thêm một chiếc áo len đi.
样子|yàngzi|dt|kiểu dáng; dáng vẻ|这双鞋的样子很好看。~Kiểu dáng đôi giày này rất đẹp.
适合|shìhé|dong|phù hợp, hợp với|这份工作很适合你。~Công việc này rất hợp với bạn.
售货员|shòuhuòyuán|dt|nhân viên bán hàng|售货员热情地给我介绍衣服。~Nhân viên bán hàng nhiệt tình giới thiệu quần áo cho tôi.
质量|zhìliàng|dt|chất lượng|这家店的东西质量很好。~Đồ của cửa hàng này chất lượng rất tốt.
强|qiáng|tt|hơn, tốt hơn; mạnh|自己做饭比天天吃外卖强。~Tự nấu cơm còn hơn ngày nào cũng ăn đồ đặt ngoài.
年底|niándǐ|dt|cuối năm|年底公司特别忙。~Cuối năm công ty đặc biệt bận.
全|quán|tt|toàn bộ, cả; đầy đủ|全班同学都参加了比赛。~Cả lớp đều tham gia cuộc thi.
打折|dǎzhé|dong|giảm giá|这件衣服打八折。~Chiếc áo này giảm giá 20%.
值|zhí|dong|đáng, đáng giá|这本书很值得一看。~Cuốn sách này rất đáng đọc.
估计|gūjì|dong|ước tính, đoán chừng|估计他们半个小时后到。~Đoán chừng nửa tiếng nữa họ đến.
期|qī|lg|kỳ, khóa, số (lượng từ)|这一期的杂志很有意思。~Số tạp chí kỳ này rất hay.
听力|tīnglì|dt|thính lực; kỹ năng nghe|多听音频能提高听力。~Nghe nhiều có thể nâng cao kỹ năng nghe.
烦|fán|tt|phiền, bực bội|这几天工作太多，我心里很烦。~Mấy hôm nay việc nhiều quá, tôi rất bực bội.
脱|tuō|dong|cởi|进门请脱鞋。~Vào nhà vui lòng cởi giày.
挂|guà|dong|treo|把大衣挂在门后吧。~Treo áo khoác ở sau cửa nhé.
脾气|píqi|dt|tính khí, cáu giận|他脾气很好，从来不生气。~Anh ấy tính rất hiền, chưa bao giờ nổi giận.
伤心|shāngxīn|tt|đau lòng, buồn|听到这个消息，她很伤心。~Nghe tin này, cô ấy rất buồn.
批评|pīpíng|dong|phê bình, phê bình trách mắng|老师批评了上课迟到的学生。~Thầy giáo phê bình học sinh đi học muộn.
道歉|dàoqiàn|dong|xin lỗi|你应该向他道歉。~Bạn nên xin lỗi anh ấy.
老家|lǎojiā|dt|quê nhà|我的老家在广东。~Quê tôi ở Quảng Đông.
自|zì|gioi|từ (khi)|自来北京以后，我一直住在这儿。~Từ khi đến Bắc Kinh, tôi luôn sống ở đây.
父母|fùmǔ|dt|bố mẹ|我每个周末都给父母打电话。~Cuối tuần nào tôi cũng gọi điện cho bố mẹ.
父子|fùzǐ|dt|cha con|他们父子俩都喜欢踢足球。~Hai cha con họ đều thích đá bóng.
母子|mǔzǐ|dt|mẹ con|母子二人一起去旅游了。~Hai mẹ con cùng đi du lịch.
无论|wúlùn|lien|bất luận, dù|无论多晚，妈妈都等我回家。~Dù muộn đến đâu, mẹ cũng đợi tôi về nhà.
条件|tiáojiàn|dt|điều kiện|这里的生活条件很好。~Điều kiện sống ở đây rất tốt.
允许|yǔnxǔ|dong|cho phép|这里不允许停车。~Ở đây không cho phép đỗ xe.
另外|lìngwài|pho|ngoài ra; khác|另外，请再给我一杯水。~Ngoài ra, cho tôi thêm một cốc nước.
卫生|wèishēng|dt|vệ sinh|饭前要洗手，注意卫生。~Trước khi ăn phải rửa tay, chú ý vệ sinh.
母亲|mǔqīn|dt|mẹ, mẫu thân|母亲每天早上都给我们做早饭。~Mẹ sáng nào cũng nấu bữa sáng cho chúng tôi.
待|dāi|dong|ở, lưu lại|周末我一般待在家里看书。~Cuối tuần tôi thường ở nhà đọc sách.
将|jiāng|gioi|đem, lấy (giống 把)|请将材料交给经理。~Vui lòng đưa tài liệu cho giám đốc.
闻|wén|dong|ngửi|我闻到了花的香味。~Tôi ngửi thấy mùi hoa thơm.
味道|wèidao|dt|mùi vị|妈妈做的菜味道很好。~Món mẹ nấu có mùi vị rất ngon.
冷静|lěngjìng|tt|bình tĩnh|遇到问题要冷静。~Gặp vấn đề phải bình tĩnh.
鼻子|bízi|dt|cái mũi|我感冒了，鼻子不舒服。~Tôi bị cảm, mũi khó chịu.
父亲|fùqīn|dt|cha, bố|我父亲是一名医生。~Bố tôi là một bác sĩ.
城|chéng|dt|thành phố, thành|他住在城里，周末去郊区玩。~Anh ấy sống trong thành phố, cuối tuần ra ngoại ô chơi.
鲜|xiān|tt|tươi, ngon ngọt|这条鱼很鲜。~Con cá này rất tươi.
暖|nuǎn|tt|ấm|喝了一杯热茶，身上暖多了。~Uống một cốc trà nóng, người ấm hơn nhiều.
勇敢|yǒnggǎn|tt|dũng cảm|她是一个勇敢的女孩儿。~Cô ấy là một cô gái dũng cảm.
商量|shāngliang|dong|bàn bạc, thương lượng|这件事我们一起商量一下。~Việc này chúng ta cùng bàn bạc một chút.
"""),
texts=[dict(t="课文1", scene="在商场，杨同乐和王一飞在给父母买衣服。", scene_vi="Ở trung tâm thương mại, Dương Đồng Lạc và Vương Nhất Phi đang mua quần áo cho bố mẹ.", narr=False, lines=T("""
王一飞>你觉得老妈穿这件毛衣怎么样？|Anh thấy mẹ mặc chiếc áo len này thế nào?
杨同乐>样子不错，就是颜色好像不怎么适合她。|Kiểu dáng được, chỉ là màu hình như không hợp mẹ lắm.
售货员>老年人穿这种颜色的衣服正合适，颜色不深，质量还特别好。您看那位阿姨正试着呢，是不是很好看？|Người lớn tuổi mặc quần áo màu này là vừa vặn, màu không đậm, chất lượng lại rất tốt. Anh chị xem cô kia đang mặc thử kìa, có phải rất đẹp không?
王一飞>嗯，是挺不错的。同乐，我印象中，老妈也常穿这种颜色的衣服，她应该会喜欢的，买一件吧。|Ừ, khá đẹp đấy. Đồng Lạc, em nhớ mẹ cũng hay mặc màu này, chắc mẹ sẽ thích, mua một chiếc đi.
杨同乐>好的，老妈高兴比什么都强。|Được, mẹ vui là hơn tất cả.
售货员>就是，老人开心最重要。我们店正好年底有活动，全场打七折呢，挺值的。|Đúng vậy, người già vui là quan trọng nhất. Cửa hàng chúng tôi cuối năm vừa hay có chương trình, toàn bộ giảm 30%, rất đáng mua.
"""), q=Q("""
杨同乐认为毛衣的颜色怎么样？|不怎么适合他妈妈。|Không hợp mẹ anh lắm.
售货员认为老人穿那件毛衣怎么样？|正合适，颜色不深，质量还特别好。|Rất vừa, màu không đậm, chất lượng tốt.
杨同乐最后为什么愿意买那件毛衣了？|因为王一飞说妈妈常穿这种颜色，应该会喜欢，老妈高兴比什么都强。|Vì Nhất Phi nói mẹ hay mặc màu này, chắc sẽ thích; mẹ vui là hơn tất cả.
商场年底有什么活动？|全场打七折。|Toàn bộ giảm giá 30%.
""")),
 dict(t="课文2", scene="刘明下班回到家中，和王一雪聊天儿。", scene_vi="Lưu Minh tan làm về nhà, trò chuyện với Vương Nhất Tuyết.", narr=False, lines=T("""
刘明>爷爷、奶奶还没回来呢？|Ông bà vẫn chưa về à?
王一雪>没呢，估计快了。下午老年班举办一期听力保护活动，他们去参加活动了。|Chưa, chắc sắp rồi. Chiều nay lớp người cao tuổi tổ chức một buổi hoạt động bảo vệ thính lực, ông bà đi tham gia rồi.
刘明>他们的活动还挺丰富的！|Hoạt động của ông bà cũng phong phú ghê!
王一雪>嗯。小明最近要考试，心里有点儿烦，昨天因为脱、挂衣服这点儿小事，就对奶奶发脾气了。|Ừ. Tiểu Minh dạo này sắp thi, trong lòng hơi bực, hôm qua chỉ vì chuyện nhỏ cởi, treo quần áo mà nổi cáu với bà.
刘明>是吗？他这样做老人该伤心了。|Thật à? Nó làm vậy bà sẽ buồn lắm.
王一雪>就是啊。他也不是不知道自己错了，我批评他以后，他马上说放学回来就向奶奶道歉。|Đúng thế. Nó cũng không phải không biết mình sai, em phê bình xong, nó nói ngay là tan học về sẽ xin lỗi bà.
刘明>好的，我也再跟他聊聊。|Được, anh cũng sẽ nói chuyện thêm với nó.
王一雪>那就更好了。|Vậy thì càng tốt.
"""), q=Q("""
爷爷、奶奶下午去做什么了？|参加老年班的听力保护活动。|Tham gia hoạt động bảo vệ thính lực của lớp người cao tuổi.
小明因为什么对奶奶发了脾气？|因为最近要考试，心里有点儿烦，为了脱、挂衣服这点儿小事。|Vì sắp thi nên bực bội, vì chuyện nhỏ cởi, treo quần áo.
王一雪批评小明，是因为他什么？|对奶奶发脾气。|Nổi cáu với bà.
小明发脾气后，王一雪和小明都做了什么？|王一雪批评了他，小明说放学回来就向奶奶道歉。|Nhất Tuyết phê bình con, Tiểu Minh nói tan học về sẽ xin lỗi bà.
""")),
 dict(t="课文3", scene="为幸福而努力", scene_vi="Nỗ lực vì hạnh phúc", narr=True, lines=T("""
杨同乐的老家在上海，他自毕业后一直在北京工作。|Quê Dương Đồng Lạc ở Thượng Hải, từ khi tốt nghiệp anh luôn làm việc ở Bắc Kinh.
虽然没和父母生活在一起，但父子、母子关系特别好。|Tuy không sống cùng bố mẹ, nhưng quan hệ cha con, mẹ con rất tốt.
杨同乐很关心父母，无论平时工作有多忙，他每个周末都会给父母打电话。|Dương Đồng Lạc rất quan tâm bố mẹ, dù bình thường công việc bận đến đâu, cuối tuần nào anh cũng gọi điện cho bố mẹ.
条件允许时，他会回上海看父母。|Khi điều kiện cho phép, anh sẽ về Thượng Hải thăm bố mẹ.
刘明和王一雪结婚后，一直没有和父母生活在一起，|Lưu Minh và Vương Nhất Tuyết kết hôn rồi vẫn không sống cùng bố mẹ,
他们平时会另外找时间去看父母，帮父母做做饭，打扫打扫卫生。|bình thường họ sẽ tìm thời gian khác đến thăm bố mẹ, giúp bố mẹ nấu cơm, dọn dẹp vệ sinh.
这两年，刘明的母亲身体不太好，他们很担心，就把父母接到了自己家里照顾。|Hai năm nay, mẹ Lưu Minh sức khỏe không tốt, họ rất lo, nên đón bố mẹ về nhà mình chăm sóc.
父母待在他们身边，他们也终于能放心地去工作了。|Bố mẹ ở bên cạnh, cuối cùng họ cũng có thể yên tâm đi làm.
"""), q=Q("""
杨同乐每个周末都会做什么？|给父母打电话。|Gọi điện cho bố mẹ.
杨同乐是怎么关心父母的？|无论工作多忙，每个周末都给父母打电话，条件允许时回上海看父母。|Dù bận mấy cũng gọi điện mỗi cuối tuần, khi có điều kiện thì về Thượng Hải thăm.
刘明的母亲身体变差后，刘明和王一雪做了什么？|把父母接到了自己家里照顾。|Đón bố mẹ về nhà mình chăm sóc.
刘明和王一雪为什么要把父母接到自己家里？|因为刘明的母亲身体不太好，他们很担心。|Vì mẹ Lưu Minh sức khỏe không tốt, họ rất lo.
""")),
 dict(t="课文4", scene="幸福的味道", scene_vi="Hương vị hạnh phúc", narr=True, lines=T("""
下班回家，林静静将父母从老家寄来的鸡汤热了热，当闻到从小就熟悉的味道时，平时冷静的她鼻子还是酸了。|Tan làm về nhà, Lâm Tĩnh Tĩnh hâm nóng canh gà bố mẹ gửi từ quê lên, khi ngửi thấy mùi vị quen thuộc từ nhỏ, cô vốn bình tĩnh mà vẫn cay cay sống mũi.
林静静一个人来北京工作三年了，父母总是担心她为了节约时间而不好好吃饭，所以每个月都给她寄各种好吃的。|Lâm Tĩnh Tĩnh một mình lên Bắc Kinh làm việc đã ba năm, bố mẹ luôn lo cô vì tiết kiệm thời gian mà không ăn uống đàng hoàng, nên tháng nào cũng gửi đủ món ngon cho cô.
这次母亲专门做了林静静最爱喝的鸡汤，为了让食物新鲜，父亲选择了城里最快的快递，上午寄出，下午就能收到。|Lần này mẹ đặc biệt nấu món canh gà Tĩnh Tĩnh thích nhất, để đồ ăn tươi, bố chọn dịch vụ chuyển phát nhanh nhất trong thành phố, sáng gửi chiều đã nhận được.
鸡汤很鲜，林静静心里更暖，她觉得父母好像就在身边。|Canh gà rất ngọt, lòng Lâm Tĩnh Tĩnh càng ấm áp, cô cảm thấy bố mẹ như đang ở bên cạnh.
都说“儿行千里母担忧”，父母总对她说：“遇到困难别害怕，要勇敢面对，任何时候都可以和父母商量。”|Người ta nói “con đi nghìn dặm mẹ lo âu”, bố mẹ luôn nói với cô: “Gặp khó khăn đừng sợ, phải dũng cảm đối mặt, bất cứ lúc nào cũng có thể bàn với bố mẹ.”
尽管在大城市生活压力有些大，但每当想到父母的这些话，尝到来自老家熟悉的味道，她就觉得又能笑着面对生活了。|Dù sống ở thành phố lớn áp lực khá nhiều, nhưng mỗi khi nghĩ đến những lời đó của bố mẹ, nếm được hương vị quen thuộc từ quê nhà, cô lại thấy mình có thể mỉm cười đối mặt với cuộc sống.
"""), q=Q("""
林静静下班回家后热的是什么？|鸡汤。|Canh gà.
父母给林静静寄了什么？|各种好吃的。|Đủ các món ngon.
父亲为什么选择最快的快递？|为了让食物新鲜。|Để đồ ăn được tươi.
是什么让林静静能“笑着面对生活”？|父母的话和来自老家熟悉的味道。|Lời của bố mẹ và hương vị quen thuộc từ quê nhà.
""")),
],
grammar=[
 G("buzenme", "固定短语“不怎么”", "Cụm từ cố định “不怎么”",
   "“不怎么” biểu thị mức độ thấp, nghĩa là “không… lắm, không mấy, ít khi”.",
   [F("S:Chủ ngữ|kw:不怎么|V:Vị ngữ", [
     ("样子不错，就是颜色好像|[不怎么]|适合她", "。", "Kiểu dáng được, chỉ là màu hình như không hợp với mẹ lắm."),
     ("他总是在图书馆看书，|[不怎么]|出去玩", "。", "Anh ấy luôn đọc sách ở thư viện, ít khi ra ngoài chơi."),
     ("我爱吃饺子、包子，|[不怎么]|喜欢吃米饭", "。", "Tôi thích ăn sủi cảo, bánh bao, không thích ăn cơm lắm.")])]),
 G("shuangfou", "双重否定", "Phủ định kép",
   "Phủ định kép biểu thị ý khẳng định, ngữ khí mạnh hơn câu khẳng định thông thường. Các cấu trúc thường gặp: “不是不、不能不、不得不” (không phải không, không thể không, buộc phải).",
   [F("S:Chủ ngữ|kw:不是不 / 不能不 / 不得不|V:Vị ngữ", [
     ("他也|[不是不]|知道自己错了", "，我批评他以后，他马上说放学回来就向奶奶道歉。", "Nó cũng không phải không biết mình sai, phê bình xong nó nói ngay sẽ xin lỗi bà."),
     ("今天是我们毕业后第一次同学聚餐，你又是班长，|[不能不]|来啊", "！", "Hôm nay là bữa liên hoan đầu tiên sau khi tốt nghiệp, cậu lại là lớp trưởng, không thể không đến đâu!"),
     ("由于天气不好，飞机不能起飞，爸爸|[不得不]|改变计划，明天再去上海", "。", "Vì thời tiết xấu, máy bay không cất cánh được, bố buộc phải đổi kế hoạch, mai mới đi Thượng Hải.")])]),
 G("wulun", "条件复句“无论……，都/也……”", "Câu phức điều kiện “无论……，都 / 也……”",
   "Biểu thị trong bất kỳ điều kiện nào kết quả cũng không thay đổi: “bất luận / dù… thì đều…”. Sau “无论” thường có từ nghi vấn hoặc dạng chính phản.",
   [F("kw:无论|X:Điều kiện bất kỳ|S:(Chủ ngữ)|kw2:都 / 也|V:Kết quả không đổi", [
     ("杨同乐很关心父母，[无论]|平时工作有多忙|他每个周末|[都]|会给父母打电话", "。", "Dương Đồng Lạc rất quan tâm bố mẹ, dù bận đến đâu cuối tuần nào anh cũng gọi điện cho bố mẹ."),
     ("只要你努力了，[无论]|你考多少分|你在我们眼里|[都]|是最优秀的", "。", "Chỉ cần con đã cố gắng, dù thi được bao nhiêu điểm, trong mắt bố mẹ con vẫn là giỏi nhất."),
     ("[无论]|你遇到什么困难|我|[都]|会在你身边", "。", "Dù bạn gặp khó khăn gì, tôi đều sẽ ở bên bạn.")])]),
 G("weile_er", "固定格式“为了……而……”", "Cấu trúc cố định “为了……而……”",
   "“为了……” nêu mục đích hoặc mục tiêu, “而……” là hành động được thực hiện để đạt mục đích đó: “vì… mà…”.",
   [F("S:Chủ ngữ|kw:为了|X:Mục đích|kw2:而|V:Hành động", [
     ("父母总是担心她|[为了]|节约时间|[而]|不好好吃饭", "。", "Bố mẹ luôn lo cô vì tiết kiệm thời gian mà không ăn uống đàng hoàng."),
     ("我们都在|[为了]|生活幸福|[而]|努力工作着", "。", "Chúng ta đều đang nỗ lực làm việc vì cuộc sống hạnh phúc."),
     ("他们|[为了]|保护环境|[而]|拒绝使用纸杯", "。", "Họ từ chối dùng cốc giấy để bảo vệ môi trường.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["自", "无论", "允许", "冷静", "值", "鲜"], [
   "这位护士工作认真，最大的优点是遇到任何事情都很【冷静】。", "这家饭馆的汤味道特别【鲜】，每次来我都要点。", "【无论】你多大，在父母眼里，你一直都是那个需要被照顾的孩子。",
   "看到母亲那么喜欢这件毛衣，我觉得花多少钱都【值】了。", "小徐【自】2006年就离开了老家，在上海读大学，毕业后又在那儿工作了。", "我们换条路走吧，前面那个路口不【允许】右转。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["估计", "另外", "待", "烦", "质量", "脾气"], [
   "A：我想买这条裤子送给妈妈。 B：颜色很适合她，【质量】也不错，她应该会喜欢的。", "A：你好像不太开心，没什么事吧？ B：昨天我的银行卡丢了，我现在心里很【烦】。",
   "A：排队的人这么多，【估计】得等很长时间。 B：他家的包子好吃又便宜，买的人当然多，咱们等等吧。", "A：对不起，我刚刚不应该对你发【脾气】。 B：没关系，我知道你这几天心情不好。",
   "A：请加一碗米饭，【另外】再加一双筷子。 B：好的，马上就来。", "A：周末时我喜欢去公园散步，不喜欢在家【待】着。 B：周末我也喜欢出去活动活动。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["忘记了今天是自己的生日", "没想到送餐地址是自己家", "外卖员的眼睛红了", "要注意身体"], [
   "中午，一个外卖员到奶茶店取餐，拿到后一看，【没想到送餐地址是自己家】，上面还写着：“爸爸，生日快乐！天气很热，【要注意身体】。”原来，外卖员忙着工作，【忘记了今天是自己的生日】，但他的女儿没有忘。看着这份生日礼物，【外卖员的眼睛红了】。他喝了奶茶，又继续努力工作。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l12", items=[
   ("老家", "我的老家在一个小城市，那里风景很美。"), ("烦", "作业太多了，我心里很烦。"), ("商量", "这件事我得跟家人商量一下。")]),
])
