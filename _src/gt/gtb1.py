# -*- coding: utf-8 -*-
# 发展汉语·初级综合(II) – Bài 1, 2
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[1] = dict(zh="入乡随俗", en="Do as the Romans Do", vi="Nhập gia tùy tục",
intro="Một người đến nơi ở mới có thể gặp những điều chưa quen, phải làm sao? Cách tốt nhất là “nhập gia tùy tục”.",
vocab=V("""
入乡随俗|rù xiāng suí sú|cum|nhập gia tùy tục (đến đâu theo phong tục nơi đó)
渐渐|jiànjiàn|pho|dần dần
迟到|chídào|dong|đến muộn
着|zhe|tro|(trợ từ, chỉ hành động/trạng thái đang kéo dài)
不好意思|bù hǎoyìsi|cum|ngại, xấu hổ; xin lỗi (lịch sự)
为了|wèile|gioi|để, vì (mục đích)
闹钟|nàozhōng|dt|đồng hồ báo thức
懒虫|lǎnchóng|dt|đồ lười, con sâu lười
该|gāi|nn|nên, phải, đến lúc phải
感谢|gǎnxiè|dong|cảm ơn, biết ơn
打招呼|dǎ zhāohu|cum|chào hỏi
有些|yǒuxiē|dai|một số, có những
问好|wèn hǎo|dong|hỏi thăm, chào hỏi
而|ér|lien|mà, còn (nối hai vế đối lập)
奇怪|qíguài|tt|lạ, kỳ lạ
下面|xiàmiàn|dt|dưới đây, sau đây
邻居|línjū|dt|hàng xóm
对话|duìhuà|dt|cuộc đối thoại, hội thoại
伞|sǎn|dt|cái ô, dù
肯定|kěndìng|pho|chắc chắn, nhất định
却|què|pho|nhưng, lại (chỉ sự trái ngược)
挺|tǐng|pho|khá, rất
亲切|qīnqiè|tt|thân thiết, gần gũi
熟人|shúrén|dt|người quen
回答|huídá|dong|trả lời
成语|chéngyǔ|dt|thành ngữ
适应|shìyìng|dong|thích nghi, thích ứng
风俗|fēngsú|dt|phong tục
夜猫子|yèmāozi|dt|cú đêm (người hay thức khuya)|他是个夜猫子，常常夜里三四点钟才睡觉。~Anh ấy là cú đêm, thường ba bốn giờ sáng mới ngủ.
"""),
texts=[dict(t="入乡随俗", narr=True, lines=T("""
来中国半年多了，我已经渐渐地习惯了这里的生活。|Đến Trung Quốc hơn nửa năm rồi, tôi đã dần dần quen với cuộc sống ở đây.
刚来中国的时候，最不习惯的是早上八点钟上课。|Lúc mới đến Trung Quốc, điều tôi không quen nhất là 8 giờ sáng đã vào học.
因为我是个夜猫子，喜欢晚睡晚起，所以经常迟到。|Vì tôi là “cú đêm”, thích ngủ muộn dậy muộn, nên thường xuyên đến muộn.
你进教室的时候，别人正上着课呢，大家都看着你，真不好意思。|Lúc bạn bước vào lớp, mọi người đang học, ai cũng nhìn bạn, thật là ngại.
为了不迟到，我买了一个闹钟。|Để không đến muộn, tôi đã mua một cái đồng hồ báo thức.
每天早上一到七点钟，它就大叫：“懒虫，该起床了！懒虫，该起床了！”|Sáng nào cứ đến 7 giờ là nó kêu to: “Đồ lười, dậy đi thôi! Đồ lười, dậy đi thôi!”
虽然不好听，我还不能不感谢它。|Tuy nghe không hay, nhưng tôi vẫn không thể không cảm ơn nó.
因为有了它，我现在已经很少迟到了。|Nhờ có nó, bây giờ tôi đã rất ít khi đến muộn.
我还有一件不习惯的事，就是打招呼。|Tôi còn một chuyện chưa quen nữa, đó là cách chào hỏi.
有些中国人和我见面不是问好，而是问一些奇怪的问题。|Một số người Trung Quốc gặp tôi không phải chào hỏi, mà là hỏi những câu hỏi kỳ lạ.
下面就是今天早上我和邻居的对话：|Dưới đây là cuộc đối thoại sáng nay giữa tôi và hàng xóm:
“早！”“早上好！”|“Chào buổi sáng!” “Chào buổi sáng!”
“吃了吗？”“吃了。”|“Ăn sáng chưa?” “Ăn rồi.”
“去上课呀？”“是。”|“Đi học à?” “Vâng.”
“外面正下着雨呢，带伞了吗？”“谢谢，我带着呢。”|“Bên ngoài đang mưa đấy, có mang ô không?” “Cảm ơn, tôi có mang đây.”
这要是在半年以前，有人这样跟我打招呼，我肯定生气了。|Nếu là nửa năm trước mà có người chào hỏi tôi như thế, chắc chắn tôi đã giận rồi.
可是，现在我却觉得挺亲切的，因为我知道，他们跟熟人才这么打招呼。|Nhưng bây giờ tôi lại thấy khá thân thiết, vì tôi biết họ chỉ chào hỏi như vậy với người quen.
要是你不想回答他们的问题，问好就可以了。|Nếu bạn không muốn trả lời câu hỏi của họ thì chào lại là được.
中国有一个成语叫“入乡随俗”，意思是：到了一个新的地方，就要适应那里的风俗习惯。|Trung Quốc có câu thành ngữ “nhập gia tùy tục”, nghĩa là: đến một nơi mới thì phải thích nghi với phong tục tập quán ở đó.
"""), q=Q("""
“我”来中国多长时间了，有什么变化？|半年多了，已经渐渐地习惯了这里的生活。|Hơn nửa năm rồi, đã dần quen với cuộc sống ở đây.
“我”最不习惯的是什么？|早上八点钟上课。|Học lúc 8 giờ sáng.
“我”为什么经常迟到？|因为“我”是个夜猫子，喜欢晚睡晚起。|Vì “tôi” là cú đêm, thích ngủ muộn dậy muộn.
迟到的时候，“我”为什么觉得不好意思？|因为别人正上着课呢，大家都看着“我”。|Vì mọi người đang học, ai cũng nhìn “tôi”.
为了不迟到，“我”做了什么？|“我”买了一个闹钟。|“Tôi” mua một cái đồng hồ báo thức.
闹钟怎么叫“我”起床？|每天早上七点钟，它就大叫：“懒虫，该起床了！”|7 giờ mỗi sáng nó kêu to: “Đồ lười, dậy thôi!”
“我”为什么要感谢闹钟？|因为有了它，“我”现在已经很少迟到了。|Vì nhờ có nó mà giờ “tôi” rất ít đến muộn.
“我”为什么不习惯和中国人打招呼？|因为有些中国人见面不是问好，而是问一些奇怪的问题。|Vì một số người gặp nhau không chào mà hỏi những câu kỳ lạ.
半年前，有人这样跟“我”打招呼，“我”会怎么样？|“我”肯定生气了，因为“我”觉得这些问题很奇怪。|Chắc chắn “tôi” sẽ giận, vì thấy những câu hỏi đó kỳ lạ.
中国人和熟人怎么打招呼？|问“吃了吗？”“去上课呀？”等问题。|Hỏi “Ăn chưa?”, “Đi học à?”…
要是不想回答中国人打招呼的问题，可以怎么办？|问好就可以了。|Chỉ cần chào lại là được.
“入乡随俗”是什么意思？|到了一个新的地方，就要适应那里的风俗习惯。|Đến nơi mới thì phải thích nghi với phong tục tập quán ở đó.
"""))],
grammar=[
 G("v_zhe", "外面正下着雨呢。", "V + 着: hành động / trạng thái đang kéo dài",
   "“着” đặt sau động từ, diễn tả hành động đang tiếp diễn hoặc trạng thái được duy trì. Thường đi với 正/在…呢. Phủ định: 没(有)+V+着.",
   [F("S:Chủ ngữ|V:Động từ|kw:着|O:Tân ngữ", [
      ("他|闭|[着]|眼睛", "，在想什么呢？", "Anh ấy đang nhắm mắt, đang nghĩ gì thế?"),
      ("她|穿|[着]|一件漂亮的新衣服", "。", "Cô ấy đang mặc một bộ quần áo mới rất đẹp."),
      ("他|拿|[着]|一束花", "去看老师。", "Anh ấy cầm một bó hoa đi thăm thầy giáo."),
      ("玛丽|背|[着]|一个大包", "站在路口。", "Mary đeo một chiếc túi to đứng ở đầu đường.")]),
    F("S:Chủ ngữ|kw:正|V:Động từ|kw2:着|O:Tân ngữ|X:呢", [
      ("外面|[正]|下|[着]|雨|[呢]", "。", "Bên ngoài đang mưa đấy."),
      ("别人|[正]|上|[着]|课|[呢]", "。", "Người khác đang học đấy.")], cap="正 + V + 着 + O + 呢")],
   notes=["“我带着呢” = tôi có mang (theo người) đây rồi."],
   prac=["A:外面正下着雨呢，{带着伞吧}。（带）", "A:我该走了，朋友们在{等着我呢}。（等）", "A:你听我说。\nB:{我听着呢}，你说吧。（听）"]),
 G("double_neg", "我还不能不感谢它。", "不/没……不/没……: phủ định kép = khẳng định mạnh",
   "Hai lần phủ định trong một câu mang nghĩa khẳng định, nhấn mạnh hơn câu khẳng định thường: 不能不 = phải; 不会不 = chắc chắn sẽ; 没有人不 = ai cũng.",
   [F("S:Chủ ngữ|kw:不/没|V:Động từ / Năng nguyện|kw2:不/没|O:Phần còn lại", [
      ("这件事他|[不]|会|[不]|知道", "。", "Chuyện này anh ấy không thể không biết (chắc chắn biết)."),
      ("我们|[没]|有人|[不]|愿意", "。", "Chúng tôi không ai là không muốn (ai cũng muốn)."),
      ("我|[不]|能|[不]|感谢它", "。", "Tôi không thể không cảm ơn nó.")])],
   notes=["我又不是没告诉过你，怎么忘了呢？– Tôi đâu phải chưa từng nói với bạn, sao lại quên rồi? (= tôi đã nói rồi)",
          "他说来，就不会不来。– Anh ấy đã nói sẽ đến thì không thể không đến."]),
 G("bushi_ershi", "不是问好，而是问一些奇怪的问题。", "不是 A，而是 B: không phải A mà là B",
   "Phủ định A, khẳng định B; dùng để đính chính hoặc giải thích lý do thật.",
   [F("kw:不是|A:A (phủ định)|kw2:而是|B:B (khẳng định)", [
      ("[不是]|我没来|[而是]|你没看见我", "。", "Không phải tôi không đến, mà là bạn không nhìn thấy tôi."),
      ("他[不是]|不会说汉语|[而是]|不好意思说", "。", "Anh ấy không phải không biết nói tiếng Hán, mà là ngại nói."),
      ("他[不是]|普通人|[而是]|一个非常有名的画家", "。", "Ông ấy không phải người bình thường, mà là một họa sĩ rất nổi tiếng.")])]),
 G("yinwei_suoyi", "因为我是个夜猫子，所以经常迟到。", "因为……，所以……: vì… nên…",
   "Nối nguyên nhân và kết quả; có thể lược 因为 hoặc 所以.",
   [F("kw:因为|C:Nguyên nhân|kw2:所以|B:Kết quả", [
      ("[因为]|天气不好，|[所以]|运动会不开了", "。", "Vì thời tiết xấu nên đại hội thể thao không tổ chức nữa."),
      ("|他太忙，|[所以]|没来", "。", "Anh ấy bận quá nên không đến."),
      ("[因为]|一件小事，|他就|生气了", "。", "Chỉ vì một chuyện nhỏ mà anh ấy nổi giận.")])]),
 G("que", "现在我却觉得挺亲切的。", "却: nhưng, lại (chuyển ý)",
   "Phó từ, đặt trước động từ/tính từ ở vế sau, chỉ sự trái với dự đoán; thường đi với 虽然.",
   [F("C:Vế trước|S:Chủ ngữ|kw:却|V:Vị ngữ", [
      ("文章虽然短，||[却]|很难", "。", "Bài văn tuy ngắn nhưng lại rất khó."),
      ("虽然知道这个字的意思，|我|[却]|不知道怎么读", "。", "Tuy biết nghĩa chữ này nhưng tôi lại không biết đọc thế nào.")])]),
],
ex=[
 pool("一、选词填空", "Chữ “室” trong 办公室 nghĩa là căn phòng. Chọn từ thích hợp điền vào chỗ trống.", ["办公室", "图书室", "会客室", "会议室", "浴室", "室外"], [
   "房间里没有【浴室】，洗澡不太方便。", "我去留学生【办公室】报名。", "【会议室】里正在开会呢。", "今天，【图书室】里的人很多。",
   "A：小刘，有人找你。B：在哪儿呢？A：在【会客室】。", "下课以后，最好做做【室外】活动。"]),
 match("二、连线", "Nối từ có chữ “室” bên trái với lời giải thích bên phải.", ["同屋", "屋子外面", "看书报或杂志的房间", "睡觉的房间"],
   [("室友", "同屋"), ("室外", "屋子外面"), ("阅览室", "看书报或杂志的房间"), ("卧室", "睡觉的房间")]),
 pool("三、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["不好意思", "为了", "感谢", "有些", "对话", "肯定", "挺", "回答", "适应"], [
   "【为了】学习汉语，我来到了中国。", "我来晚了，真【不好意思】！", "您给了我很多帮助，太【感谢】了！", "周末，【有些】人喜欢去郊游，有些人喜欢在家里休息。",
   "请听下面的【对话】，然后【回答】问题。", "我刚来北京，还不太【适应】这里的生活。", "他说来，就【肯定】会来，我们再等一会儿吧。", "老师说，我口语【挺】好的，可是听力不太好。"]),
 pick("四、选择意思相近的词语填空", "Chọn từ thích hợp (từ gần nghĩa).", [
   (["感谢", "谢谢"], ["您做的菜太好吃了，【谢谢】！", "在北京的时候，您给了我很多帮助，非常【感谢】！"]),
   (["渐渐", "慢慢"], ["他【慢慢】地走着，在打电话。", "天气【渐渐】地热了。"]),
   (["习惯", "适应"], ["我【习惯】了早睡早起。", "我很快【适应】了这里的生活。"]),
   (["为了", "因为"], ["我【因为】喜欢中国文化，所以来中国留学。", "我来这儿，不是为了找工作，而是【为了】学习。"])]),
 opn("五、根据提示改写句子", "Viết lại câu theo gợi ý.", [
   ("他说来，就一定会来。（不会不）", "他说来，就不会不来。"),
   ("应该说对不起的是我，不是你。（不是……而是……）", "应该说对不起的不是你，而是我。"),
   ("我正在开车，不能给你打电话。（着）", "我正开着车呢，不能给你打电话。"),
   ("我的汉语听力不太好，经常听错。（因为……所以……）", "因为我的汉语听力不太好，所以经常听错。")]),
 opn("六、根据提示完成对话", "Hoàn thành hội thoại theo gợi ý.", [
   ("A：你上课怎么不发言呢？\nB：因为怕说错，所以______。（不好意思）", "因为怕说错，所以不好意思发言。"),
   ("A：马克怎么还没来呢？\nB：______。（因为……所以……）", "因为路上堵车，所以他还没来。"),
   ("A：飞机是1点半起飞吗？\nB：______，而是7点半起飞。（不是……）", "不是1点半起飞，而是7点半起飞。"),
   ("A：我送给她巧克力，她会喜欢吗？\nB：她最爱吃巧克力，______。（不会不）", "她最爱吃巧克力，不会不喜欢的。")]),
 opn("七、情境表达", "Những câu sau dùng trong tình huống nào? Trong tình huống sau nên nói thế nào?", [
   ("“吃饭了吗？”“不早了，我该走了。”“去上课呀？”——这些话在什么情况下可以说？", "“吃饭了吗？”“去上课呀？”：和熟人见面打招呼的时候说；“不早了，我该走了。”：在朋友家，时间晚了，要离开的时候说。"),
   ("如果不马上走，就要迟到了，怎么说？（该……了）", "我该走了，要不就迟到了。"),
   ("有人提醒你别忘了带照相机，你带了，该怎么说？（着）", "谢谢，我带着呢。"),
   ("告诉朋友你一定来参加晚会，让他放心。（不会不）", "放心吧，我不会不来的。")]),
 opn("八、根据课文内容完成对话", "Hoàn thành hội thoại theo nội dung bài khóa.", [
   ("A：我刚来中国的时候，______。\nB：是吗？都有什么事情觉得不习惯呢？\nA：我不习惯的有两件事，一个是______，还有一个是______。", "有两件事不太习惯 / 早上八点钟上课 / 打招呼"),
   ("B：八点上课有什么不习惯的？\nA：因为______，所以______。后来我______，现在______了。", "我是个夜猫子，喜欢晚睡晚起 / 经常迟到 / 买了一个闹钟 / 已经很少迟到"),
   ("B：那，你为什么对中国人打招呼的方式不习惯呢？\nA：中国人见面不是______，而是______，比如______。", "问好 / 问一些奇怪的问题 / “吃了吗？”“去上课呀？”"),
   ("B：我觉得挺亲切的。\nA：可是我开始的时候______，现在______。\nB：看来你已经“入乡随俗”了。", "不习惯 / 也觉得挺亲切的")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("中国的年轻人都喜欢夜生活。", False), ("晚起的人不一定是“懒虫”。", True), ("老人们喜欢早睡早起。", True), ("中国的老年人都喜欢打太极拳。", False)],
   passage="年轻人的夜生活和老年人的“早生活”\n中国的年轻人也开始喜欢夜生活了，酒吧、咖啡馆什么的，是很多年轻人晚上喜欢去的地方。晚睡晚起的年轻人越来越多，有的人白天睡觉，很晚才起来，就是人们说的“夜猫子”；也有的人不是不想早起，而是工作到很晚才睡觉，早晨起不来，所以这些人并不是“懒虫”。\n中国的老人们一般喜欢早睡早起。每天早上6点钟左右，公园里就有许多人在锻炼身体了。有的人在打太极拳，有的人在跳舞，还有的人在唱京剧。老年人觉得早睡早起身体好。"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("年轻人晚上喜欢去哪里？", "酒吧、咖啡馆什么的。"),
   ("什么是“夜猫子”？", "晚睡晚起、白天睡觉、很晚才起来的人。"),
   ("为什么说晚睡晚起的人不都是“懒虫”？", "因为有的人不是不想早起，而是工作到很晚才睡觉，早晨起不来。"),
   ("老年人早上起来一般做什么？", "去公园锻炼身体：打太极拳、跳舞、唱京剧。")]),
 opn("十、说一说，写一写", "Viết một đoạn văn ngắn (khoảng 50 chữ trở lên).", [
   ("你有晚睡晚起的生活习惯吗？这里和你的家乡有什么不一样的风俗习惯？你入乡随俗了吗？（因为……，所以……　适应　入乡随俗　渐渐　该　不能不　风俗　习惯）",
    "（参考）我刚来的时候，因为晚上常常上网，所以早上起不来，经常迟到。现在我已经渐渐适应了这里的生活，晚上十一点就睡觉了。这里的风俗习惯和我的家乡不太一样，比如见面的时候问“吃了吗？”。开始我觉得很奇怪，现在我觉得挺亲切的，我已经入乡随俗了。")]),
])

B[2] = dict(zh="儿子要回家", en="My Son Is Coming Home", vi="Con trai sắp về nhà",
intro="Con trai tốt nghiệp sắp về nhà, mẹ lại rất lo lắng. Người bạn bác sĩ không hỏi về sức khỏe của cậu con trai mà cứ hỏi tình hình ký túc xá… Vì sao vậy?",
vocab=V("""
毕业|bìyè|dong|tốt nghiệp
恭喜|gōngxǐ|dong|chúc mừng
关系|guānxì|dt|quan hệ, liên quan
从来|cónglái|pho|từ trước đến nay (thường dùng với phủ định)
害怕|hàipà|dong|sợ
病毒|bìngdú|dt|vi rút
哦|ò|than|ồ, à (hiểu ra)
靠|kào|dong|dựa, sát (vào)
墙|qiáng|dt|tường
摆|bǎi|dong|bày, đặt
堆|duī|lg|đống (lượng từ); chất đống
脏|zāng|tt|bẩn
旧|jiù|tt|cũ
乱七八糟|luànqībāzāo|tt|lộn xộn, bừa bộn
墙角|qiángjiǎo|dt|góc tường
垃圾|lājī|dt|rác
箱|xiāng|dt|thùng, hòm
空|kōng|tt|rỗng, trống
食品|shípǐn|dt|thực phẩm
袋|dài|dt|túi
酸奶|suānnǎi|dt|sữa chua
盒|hé|dt|hộp
袜子|wàzi|dt|tất, vớ
废纸|fèizhǐ|dt|giấy vụn, giấy bỏ
衣柜|yīguì|dt|tủ quần áo
不过|búguò|lien|nhưng, có điều
挂|guà|dong|treo
自由|zìyóu|tt|tự do
小心|xiǎoxīn|dong|cẩn thận
消毒|xiāodú|dong|khử trùng
环境|huánjìng|dt|môi trường
保护|bǎohù|dong|bảo vệ
"""),
texts=[dict(t="儿子要回家", narr=False, lines=T("""
医生>听说你儿子大学毕业了，恭喜恭喜！|Nghe nói con trai chị tốt nghiệp đại học rồi, chúc mừng chúc mừng!
妈妈>你别恭喜我，我正为这件事担心呢，你快帮帮我吧。|Anh đừng chúc mừng tôi, tôi đang lo vì chuyện này đây, anh mau giúp tôi với.
医生>儿子要回家了，是好事啊，你为什么这么担心呢？我能给你什么帮助呢？|Con trai sắp về nhà là chuyện tốt mà, sao chị lại lo thế? Tôi có thể giúp gì cho chị?
妈妈>当然能，因为你是医生啊。|Đương nhiên là được, vì anh là bác sĩ mà.
医生>这件事跟我是医生有什么关系吗？|Chuyện này thì liên quan gì đến việc tôi là bác sĩ?
妈妈>当然有关系。儿子从上大学到现在，从来没打扫过房间，我害怕他带着病毒回家。|Đương nhiên là có. Con tôi từ lúc vào đại học đến giờ chưa bao giờ dọn phòng, tôi sợ nó mang vi rút về nhà.
医生>哦，我明白了。那请您给我介绍一下他的宿舍吧。|À, tôi hiểu rồi. Vậy chị kể cho tôi nghe về ký túc xá của cậu ấy đi.
妈妈>房间不大不小。靠墙摆着一张床，床下放着一堆脏衣服。|Căn phòng không to không nhỏ. Sát tường kê một chiếc giường, dưới gầm giường để một đống quần áo bẩn.
妈妈>桌子上面放着一台电脑、许多旧书、几张音乐CD、两个啤酒瓶子。|Trên bàn để một cái máy tính, rất nhiều sách cũ, mấy đĩa CD nhạc, hai cái chai bia.
妈妈>对了，书上还放着一只鞋。房间里乱七八糟的，太脏了。|À đúng rồi, trên sách còn để một chiếc giày. Trong phòng bừa bộn lung tung, bẩn quá.
医生>墙角放着一个垃圾箱，是吧？|Ở góc tường có để một thùng rác, phải không?
妈妈>对呀，里面放着空食品袋、空酸奶盒、脏袜子、废纸什么的。|Đúng thế, bên trong có túi đồ ăn rỗng, hộp sữa chua rỗng, tất bẩn, giấy vụn các thứ.
医生>屋子里有衣柜吗？|Trong phòng có tủ quần áo không?
妈妈>有，不过衣柜里没挂着衣服，却放着足球、篮球什么的，衣服都在地上堆着呢……|Có, nhưng trong tủ không treo quần áo mà lại để bóng đá, bóng rổ các thứ, quần áo thì chất đống dưới đất…
医生>他自己每天洗碗吗？|Cậu ấy có tự rửa bát hằng ngày không?
妈妈>用过的盘子和碗，他一个星期才洗一次。|Đĩa và bát đã dùng, một tuần nó mới rửa một lần.
医生>你们以前没发现这个问题吗？|Trước đây anh chị không phát hiện ra vấn đề này à?
妈妈>刚上大学的时候，他说要自由，不让我们去他的宿舍。我们是最近才发现了这个问题。|Lúc mới vào đại học, nó nói muốn tự do, không cho chúng tôi đến ký túc xá của nó. Gần đây chúng tôi mới phát hiện ra vấn đề này.
医生>他真是太自由了！你儿子的宿舍里一定有不少病毒。|Cậu ấy đúng là quá tự do! Ký túc xá của con trai chị chắc chắn có không ít vi rút.
医生>你们真应该小心点儿，最好给他的东西消消毒。对了，你儿子毕业以后想做什么工作？|Anh chị nên cẩn thận một chút, tốt nhất là khử trùng đồ đạc của cậu ấy. À, con trai chị tốt nghiệp rồi muốn làm công việc gì?
妈妈>他想做和环境保护有关系的工作。|Nó muốn làm công việc liên quan đến bảo vệ môi trường.
"""), q=Q("""
儿子要回家了，妈妈的心情怎么样？|妈妈很担心。|Mẹ rất lo lắng.
妈妈为什么让对方帮助自己？|因为对方是医生，妈妈害怕儿子带着病毒回家。|Vì người kia là bác sĩ, mẹ sợ con mang vi rút về nhà.
儿子宿舍的床下放着什么？|床下放着一堆脏衣服。|Dưới giường để một đống quần áo bẩn.
桌子上放着什么？你认为什么放错了地方？|电脑、旧书、音乐CD、啤酒瓶子，书上还放着一只鞋。鞋放错了地方。|Máy tính, sách cũ, CD, chai bia, trên sách còn có chiếc giày – giày để sai chỗ.
垃圾箱里有什么？|空食品袋、空酸奶盒、脏袜子、废纸什么的。|Túi đồ ăn rỗng, hộp sữa chua rỗng, tất bẩn, giấy vụn…
衣柜里放着什么？|放着足球、篮球什么的，没挂着衣服。|Để bóng đá, bóng rổ…, không treo quần áo.
儿子多长时间洗一次盘子和碗？|一个星期才洗一次。|Một tuần mới rửa một lần.
医生朋友给了妈妈什么建议？|最好给儿子的东西消消毒。|Tốt nhất là khử trùng đồ đạc của con.
儿子想做什么工作？这个结尾有什么可笑的地方？|他想做和环境保护有关系的工作。可是他自己的房间又脏又乱。|Muốn làm việc liên quan bảo vệ môi trường – trong khi phòng mình vừa bẩn vừa bừa.
"""))],
grammar=[
 G("conglai", "儿子从来没打扫过房间。", "从来: từ trước đến nay (chưa/không bao giờ)",
   "Phó từ, chỉ từ quá khứ đến hiện tại luôn như vậy; thường dùng trong câu phủ định: 从来不 + V (thói quen), 从来没(有) + V + 过 (chưa từng).",
   [F("S:Chủ ngữ|kw:从来|kw2:不/没|V:Động từ|O:Tân ngữ", [
      ("我|[从来]|[不]|吃|这种东西", "。", "Tôi trước giờ không bao giờ ăn loại này."),
      ("毕业以后，我们|[从来]|[没]|见过|面", "。", "Tốt nghiệp xong, chúng tôi chưa từng gặp lại nhau."),
      ("这个问题我|[从来]|[没]|想过|", "。", "Vấn đề này tôi chưa từng nghĩ tới.")])],
   prac=["A:听说你去过云南丽江。\nB:我{从来没去过}丽江，不过我听说那儿很有意思。"]),
 G("bu_a_bu_b", "房间不大不小。", "不 A 不 B: không A không B (vừa phải)",
   "A và B là hai tính từ trái nghĩa, diễn tả mức độ vừa phải, thích hợp.",
   [F("S:Chủ ngữ|kw:不|A:Tính từ A|kw2:不|B:Tính từ B|C:Đánh giá", [
      ("这件衣服|[不]|大|[不]|小|，正合适", "。", "Bộ quần áo này không to không nhỏ, vừa đúng."),
      ("北京的秋天|[不]|冷|[不]|热|，很舒服", "。", "Mùa thu Bắc Kinh không lạnh không nóng, rất dễ chịu."),
      ("我来得|[不]|早|[不]|晚|，正好开始上课", "。", "Tôi đến không sớm không muộn, vừa đúng lúc vào học.")])],
   prac=["A:这个房间怎么样？\nB:{不大不小}，一个人住正合适。", "A:老师说得快不快？\nB:{不快不慢}，我都听懂了。"]),
 G("cunxian", "靠墙摆着一张床。", "Nơi chốn + V + 着 + (số lượng) + N: câu tồn hiện",
   "Diễn tả ở một nơi nào đó có (tồn tại) người/vật gì, ở trạng thái thế nào.",
   [F("P:Nơi chốn|V:Động từ|kw:着|Nu:Số lượng|N:Người / vật", [
      ("书架上|摆|[着]|许多|书", "。", "Trên giá sách bày rất nhiều sách."),
      ("门口|停|[着]|一辆|出租车", "。", "Trước cửa đỗ một chiếc taxi."),
      ("墙上|挂|[着]|一幅|地图", "。", "Trên tường treo một tấm bản đồ."),
      ("床下|放|[着]|一堆|脏衣服", "。", "Dưới giường để một đống quần áo bẩn.")])],
   prac=["A:桌子上有什么？\nB:桌子上{放着两本书}。", "A:教室里有人吗？\nB:教室里{坐着几个学生}。"]),
 G("duile_shenmede", "空食品袋、空酸奶盒、脏袜子、废纸什么的。", "对了 / ……什么的 / 最好",
   "对了: chợt nhớ ra, chuyển sang chuyện khác. ……什么的: … các thứ, vân vân (dùng sau một hoặc vài sự vật liệt kê). 最好: tốt nhất là (đưa lời khuyên).",
   notes=["明天上午9点出发。对了，你问问马丁去不去。– Sáng mai 9 giờ xuất phát. À, bạn hỏi Martin xem có đi không.",
          "校园里，银行、邮局、书店什么的都有，很方便。– Trong trường có ngân hàng, bưu điện, hiệu sách…, rất tiện.",
          "想要提高汉语听说能力，最好多听多说。– Muốn nâng cao khả năng nghe nói tiếng Hán, tốt nhất là nghe nhiều nói nhiều.",
          "去旅行的时候，最好带点儿常用药。– Khi đi du lịch, tốt nhất nên mang theo ít thuốc thông dụng."]),
],
ex=[
 pool("一、选词填空（医）", "Chữ “医” trong 医生 có thể tạo từ 中医/西医. Chọn từ điền vào chỗ trống.", ["医生", "中医", "西医"], [
   "昨天我去医院了，【医生】说我只是感冒，没关系。", "我昨天去看【中医】了，我想试试中药。", "这家医院没有中医，只能看【西医】。"]),
 pool("一、选词填空（电）", "Chữ “电” có thể tạo từ 电话/电影/电视/电灯. Chọn từ điền vào chỗ trống.", ["电话", "电影", "电视", "电灯"], [
   "我每星期给家里打一次【电话】。", "我昨天和朋友一起看了一个新【电影】，很晚才回来。", "我很喜欢一边吃饭，一边看【电视】。", "我宿舍的【电灯】坏了，您帮我修一下，好吗？"]),
 pool("二、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["毕业", "害怕", "病毒", "脏", "旧", "乱七八糟", "小心", "保护"], [
   "旅行的时候，我很【害怕】生病，因为有时候找不到医院。", "我的电脑有【病毒】了，怎么办？", "【毕业】以后，我就去上海工作。", "那件衣服太【旧】了，参加晚会最好穿件新衣服。",
   "他的字写得【乱七八糟】，我看不懂。", "路上车多人多，骑自行车【小心】一点儿！", "你的车太【脏】了，洗洗吧。", "你用电脑的时间别太长了，【保护】好自己的眼睛。"]),
 match("三、连线", "Nối từ bên trái với lời giải thích bên phải.", ["认真地放好", "很多东西像小山一样放在一起", "从过去到现在", "很不整齐", "注意", "不新"],
   [("摆", "认真地放好"), ("堆", "很多东西像小山一样放在一起"), ("从来", "从过去到现在"), ("乱七八糟", "很不整齐"), ("小心", "注意"), ("旧", "不新")]),
 pick("四、选择意思相近的词语填空", "Chọn từ thích hợp (từ gần nghĩa).", [
   (["旧", "老"], ["我和他是【老】朋友了。", "我有一台【旧】电脑，想换一台新的。"]),
   (["放", "摆", "堆"], ["桌子上【摆】着家人的照片。", "东西别乱【放】，从哪里拿来的，再放回哪里去。", "地上【堆】着很多书。"]),
   (["担心", "害怕"], ["她一定能照顾好自己，你别【担心】。", "天太黑了，一个人走路有点儿【害怕】。"])]),
 match("五、连句", "Nối vế bên trái với vế bên phải thành câu hoàn chỉnh.", ["和他没关系。", "不知道今天是怎么了。", "得好好儿收拾收拾。", "大家最好小心一点儿。", "应当小心保护好。"],
   [("这些老建筑都很重要，", "应当小心保护好。"), ("屋子里乱七八糟的，", "得好好儿收拾收拾。"), ("他从来不迟到，", "不知道今天是怎么了。"), ("是我不小心摔倒了，", "和他没关系。"), ("现在出现了一种新的电脑病毒，", "大家最好小心一点儿。")]),
 posq("六、选择括号中词语的正确位置", "Chọn vị trí đúng cho từ trong ngoặc.", [
   ("虽然都在北京A工作，B我们C两年多D没见面了。", "却", "C"), ("他的名片上只写A姓名和电话，却没有B地址。", "着", "A"),
   ("学习是A你自己的事，B别人没C关系。", "跟", "B"), ("他A从来B都C吃D早饭。", "不", "C")]),
 opn("七、根据提示完成对话", "Hoàn thành hội thoại theo gợi ý.", [
   ("A：你睡觉前喝咖啡吗？\nB：______，我害怕睡不着觉。（从来）", "我从来不在睡觉前喝咖啡，我害怕睡不着觉。"),
   ("A：我住在留学生宿舍好呢，还是住在中国朋友家好呢？\nB：______，这样你就可以每天和中国朋友练习汉语了。（最好）", "你最好住在中国朋友家。"),
   ("A：旅行包里装着______，太多了！（……什么的）\nB：路上可能有用，你还是带着吧。", "旅行包里装着衣服、书、药什么的，太多了！"),
   ("A：你最近工作太忙，小心别累坏了身体。\nB：是啊。我很想休息休息，______。（不过）", "我很想休息休息，不过最近实在没有时间。"),
   ("A：你毕业以后想做什么工作？\nB：______。（跟……有关系）", "我想做跟汉语有关系的工作。")]),
 opn("八、看图完成对话", "Mẹ và con trai nói chuyện về căn phòng bừa bộn. Hoàn thành hội thoại.", [
   ("妈妈：你看看你的房间！唉！______，真没办法！（乱七八糟　从来）", "房间里乱七八糟的，你从来不打扫，真没办法！"),
   ("儿子：……对了，妈，我的书包在哪儿？\n妈妈：衣帽架上______。（挂）", "衣帽架上挂着呢。"),
   ("儿子：我看到了。对了，我的鞋也少了一只。\n妈妈：床旁边______。（放）", "床旁边放着呢。"),
   ("儿子：哦，我看到了。对了，______。（最好）\n妈妈：好，我不给你打扫，你的房间乱不乱跟我没关系。", "对了，你最好别给我打扫房间。")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("叶公喜欢真的龙。", False), ("他的衣服上画着龙。", False), ("真龙来看望叶公。", True), ("叶公很害怕真的龙。", True)],
   passage="叶公好龙\n很早以前，有一个叫叶公的人，经常对别人说：“我太喜欢龙了！”他家的门上刻（kè）着龙，窗子上刻着龙，墙上画着龙，他的衣服上也绣（xiù）着龙。\n有人告诉天上的真龙说：“叶公这么喜欢龙，可是还从来没见过真龙呢，你最好下去看看他。”有一天，真龙从天上飞到了叶公的家。叶公听到外面有声音，出门一看，天啊，自己家的院子里来了一条真的龙，大大的眼睛正看着自己呢！叶公吓得脸都白了，大叫一声，逃走（táozǒu）了。"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("叶公真的喜欢龙吗？", "不是。他只喜欢画的、刻的龙，看到真的龙就害怕得逃走了。"),
   ("短文中有几个带“着”的句子？请读一下。", "门上刻着龙；窗子上刻着龙；墙上画着龙；衣服上也绣着龙；大大的眼睛正看着自己呢。"),
   ("这个故事是一个成语，你知道是什么吗？", "叶公好龙（Yè Gōng hào lóng）：表面上喜欢，其实并不是真的喜欢。")]),
 opn("十、说一说，写一写", "Viết khoảng 60 chữ giới thiệu căn phòng của bạn.", [
   ("介绍一下你的房间。（摆着　放着　装着　挂着　贴着　不大不小　乱七八糟）",
    "（参考）我的房间不大不小。靠窗摆着一张桌子，桌子上放着一台电脑和几本书。墙上挂着一张中国地图，门上贴着一张照片。衣柜里挂着我的衣服。我的房间不太乱，我每个星期都打扫一次。")]),
])
