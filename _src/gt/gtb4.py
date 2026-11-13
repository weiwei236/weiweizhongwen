# -*- coding: utf-8 -*-
# 发展汉语·初级综合(II) – Bài 7, 8
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[7] = dict(zh="我要去埃及", en="I Want to Go to Egypt", vi="Tôi muốn đi Ai Cập",
intro="Đi Ai Cập là ước mơ hồi nhỏ của “tôi”. Tuy chỉ là một ước mơ nhỏ, nhưng để thực hiện nó, “tôi” đã cố gắng suốt 20 năm.",
vocab=V("""
小学|xiǎoxué|dt|tiểu học
得|dé|dong|được, đạt được
世界|shìjiè|dt|thế giới
地图|dìtú|dt|bản đồ
轮|lún|dong|đến lượt, luân phiên
烧|shāo|dong|đun, đốt
洗澡|xǐ zǎo|dong|tắm
围|wéi|dong|quấn, vây
浴巾|yùjīn|dt|khăn tắm
浴室|yùshì|dt|phòng tắm
冲|chōng|dong|lao, xông
叫|jiào|dong|kêu, hét
干|gàn|dong|làm
火|huǒ|dt|lửa
灭|miè|dong|tắt (lửa, đèn)
讨厌|tǎoyàn|dong|ghét
小声|xiǎo shēng|cum|nói nhỏ, khẽ
巴掌|bāzhang|dt|bàn tay; cái tát
一辈子|yíbèizi|dt|cả đời
了|liǎo|tro|(dùng trong V得了/V不了: có thể/không thể)
敢|gǎn|dong|dám
继续|jìxù|dong|tiếp tục
明信片|míngxìnpiàn|dt|bưu thiếp
面前|miànqián|dt|trước mặt
金字塔|jīnzìtǎ|dt|kim tự tháp
记得|jìde|dong|nhớ
小时候|xiǎoshíhou|dt|hồi nhỏ
灵|líng|tt|linh nghiệm, hiệu nghiệm
小子|xiǎozi|dt|thằng bé, thằng nhóc
埃及|Āijí|rieng|Ai Cập
"""),
texts=[dict(t="我要去埃及", narr=True, lines=T("""
小学的时候，我考试得了第一名，老师给了我一本《世界地图》。|Hồi tiểu học, tôi thi được hạng nhất, thầy giáo tặng tôi một cuốn “Bản đồ thế giới”.
我太喜欢那本地图了，一回到家就看了起来。|Tôi thích cuốn bản đồ đó lắm, vừa về đến nhà là xem ngay.
那一天，轮到我给全家人烧洗澡水，我就一边烧水一边看地图。|Hôm ấy đến lượt tôi đun nước tắm cho cả nhà, tôi vừa đun nước vừa xem bản đồ.
我最喜欢的国家是埃及，“长大以后我一定要去埃及……”我看着埃及地图想。|Đất nước tôi thích nhất là Ai Cập, “lớn lên nhất định mình phải đến Ai Cập…”, tôi vừa nhìn bản đồ Ai Cập vừa nghĩ.
突然，一个人围着浴巾从浴室里冲出来，对着我大叫：“你在干什么呢？火都灭了！”|Bỗng một người quấn khăn tắm từ phòng tắm lao ra, hét lớn với tôi: “Mày đang làm gì thế? Lửa tắt hết rồi!”
是爸爸，他最讨厌做事不认真的人。|Đó là bố, bố ghét nhất người làm việc không nghiêm túc.
我说：“对不起！我在看地图呢。”|Tôi nói: “Con xin lỗi! Con đang xem bản đồ ạ.”
爸爸生气地说：“看什么地图！快烧火！”|Bố giận dữ nói: “Xem bản đồ gì mà xem! Mau nhóm lửa đi!”
“我在看埃及地图呢。”我小声说。|“Con đang xem bản đồ Ai Cập ạ.” Tôi nói khẽ.
爸爸更生气了，打了我一巴掌：“看什么埃及地图！你一辈子也去不了那么远的地方！快烧火！”|Bố càng giận, tát tôi một cái: “Xem bản đồ Ai Cập gì! Cả đời mày cũng không đi được nơi xa như thế! Mau nhóm lửa!”
我不敢再看下去了，只好放下地图，继续烧水。|Tôi không dám xem tiếp nữa, đành bỏ bản đồ xuống, tiếp tục đun nước.
我一边烧水一边想：“我真的去不了埃及吗？”|Tôi vừa đun nước vừa nghĩ: “Mình thật sự không đi được Ai Cập sao?”
20年后，我第一次出国就去了埃及。|20 năm sau, lần đầu tiên ra nước ngoài tôi đã đến Ai Cập.
在埃及，我给爸爸寄回一张明信片，上面写着：|Ở Ai Cập, tôi gửi về cho bố một tấm bưu thiếp, trên đó viết:
“亲爱的爸爸，我现在正在埃及，我的面前就是金字塔。|“Bố thân yêu, bây giờ con đang ở Ai Cập, trước mặt con chính là kim tự tháp.
您还记得吗？小时候，因为我看埃及地图，您打了我，还说我一辈子也去不了埃及。我要谢谢您的那句话！”|Bố còn nhớ không? Hồi nhỏ, vì con xem bản đồ Ai Cập mà bố đánh con, còn nói cả đời con cũng không đi được Ai Cập. Con muốn cảm ơn câu nói ấy của bố!”
爸爸看着明信片，不好意思地问我妈妈：|Bố nhìn tấm bưu thiếp, ngượng ngùng hỏi mẹ tôi:
“我什么时候说过那样的话？我说过吗？打了一下就那么灵？这小子真的到埃及去了？”|“Tôi nói câu đó bao giờ nhỉ? Tôi có nói không? Đánh một cái mà linh nghiệm thế à? Thằng nhóc này đến Ai Cập thật rồi?”
"""), q=Q("""
老师给了“我”什么？|一本《世界地图》。|Một cuốn “Bản đồ thế giới”.
“我”为什么一到家就看起那本地图来？|因为“我”太喜欢那本地图了。|Vì “tôi” rất thích cuốn bản đồ.
这一天，“我”应该做什么？|给全家人烧洗澡水。|Đun nước tắm cho cả nhà.
“我”长大了想去哪儿？为什么？|想去埃及，因为“我”最喜欢的国家是埃及。|Muốn đi Ai Cập, vì đó là nước “tôi” thích nhất.
谁从浴室里跑了出来？为什么？|爸爸，因为火灭了。|Bố, vì lửa tắt.
爸爸为什么生气？|因为“我”做事不认真，看地图，火都灭了。|Vì “tôi” làm việc không nghiêm túc, lửa tắt cả.
“看什么地图！”是什么意思？|别看地图了。|Đừng xem bản đồ nữa.
“我”为什么放下地图？|因为“我”不敢再看下去了。|Vì “tôi” không dám xem tiếp.
为什么“我”第一次出国就去了埃及？|因为这是“我”小时候的理想。|Vì đó là ước mơ từ nhỏ.
“我”给爸爸寄回了什么？|一张明信片。|Một tấm bưu thiếp.
爸爸记得自己做过的事和说过的话吗？|不记得了。|Không nhớ nữa.
"""))],
grammar=[
 G("qilai", "我一回到家就看了起来。", "V/Adj + 起来: bắt đầu và tiếp diễn",
   "Chỉ động tác hoặc sự thay đổi bắt đầu và tiếp tục. Nếu có tân ngữ, đặt GIỮA 起 và 来.",
   [F("S:Chủ ngữ|V:Động từ/Tính từ|kw:起来|X:Phần sau", [
      ("她们大声|唱|[起来]|", "。", "Họ bắt đầu hát to lên."),
      ("最近|热|[起来]|了", "。", "Dạo này trời bắt đầu nóng lên rồi."),
      ("听了我的话，她|笑了|[起来]|", "。", "Nghe tôi nói, cô ấy bật cười.")]),
    F("S:Chủ ngữ|V:Động từ|kw:起|O:Tân ngữ|kw2:来", [
      ("他高兴得|唱|[起]|歌|[来]", "。", "Anh ấy vui đến mức hát vang lên."),
      ("他急忙|查|[起]|词典|[来]", "。", "Anh ấy vội vàng tra từ điển.")], cap="Có tân ngữ: V + 起 + O + 来")]),
 G("v_shenme", "看什么地图！快烧火！", "V + 什么: ngăn cản, phủ định (giọng không vừa lòng)",
   "Không phải câu hỏi; dùng để ngăn cản, khuyên can hoặc phủ định, thường mang ý không hài lòng, sốt ruột.",
   [F("V:Động từ|kw:什么|O:Tân ngữ|C:Lý do", [
      ("都快迟到了，还吃|[什么]||", "！", "Sắp muộn rồi, còn ăn gì nữa!"),
      ("唱|[什么]||！别人都在睡觉呢", "！", "Hát hò gì! Mọi người đang ngủ đấy!"),
      ("预习|[什么]|课文|！这么好的天气，还是出去玩儿玩儿吧", "。", "Chuẩn bị bài gì chứ! Trời đẹp thế này, đi chơi thôi.")])],
   prac=["A:我今天得给妈妈写信。\nB:{写什么信}呀？发个电子邮件多方便。", "A:明天上午我想睡觉。\nB:{睡什么觉}？天气那么好，还是出去玩儿玩儿吧。", "A:我想结婚了。\nB:{结什么婚}？一个人多自由。"]),
 G("buliao", "你一辈子也去不了那么远的地方！", "V + 得了 / 不了 (liǎo)",
   "V不了 là dạng phủ định của V得了. (1) Có thể/không thể thực hiện V; (2) có thể/không thể V hết (= V得完/V不完).",
   [F("S:Chủ ngữ|V:Động từ|kw:得了/不了|X:Phần sau", [
      ("他病了，今天|来|[不了]|了，你别等他了", "。", "Anh ấy ốm, hôm nay không đến được, đừng đợi nữa."),
      ("车坏了，|开|[不了]|了，我们走着去吧", "。", "Xe hỏng rồi, không lái được, chúng ta đi bộ thôi."),
      ("这么难，你|翻译|[得了]|吗", "？", "Khó thế này, bạn dịch nổi không?"),
      ("这么多，咱们肯定|吃|[不了]|", "。", "Nhiều thế này, chắc chắn chúng ta ăn không hết."),
      ("这么多啤酒，你一个人|喝|[得了]|吗", "？", "Nhiều bia thế, một mình bạn uống hết nổi không?")])],
   prac=["A:你今天能参加晚会吗？\nB:对不起，我工作太忙了，{去不了}。", "A:我想用一下你的电脑，可以吗？\nB:对不起，我的电脑坏了，{用不了}。", "A:我的手机没电了，{打不了电话了}。\nB:没关系，可以用我的手机打。"]),
 G("xiaqu", "我不敢再看下去了。", "V/Adj + 下去: tiếp tục",
   "Chỉ động tác đã bắt đầu và sẽ tiếp tục, hoặc tình trạng đã xuất hiện và sẽ tiếp tục tồn tại.",
   [F("S:Chủ ngữ|V:Động từ/Tính từ|kw:下去", [
      ("虽然外语很难，但是我还要|学|[下去]", "。", "Tuy ngoại ngữ khó, nhưng tôi vẫn sẽ học tiếp."),
      ("如果你不锻炼，你可能还会|胖|[下去]", "。", "Nếu không tập luyện, bạn có thể còn béo lên nữa."),
      ("这个工作太累了，我不想|干|[下去]", "了。", "Công việc này mệt quá, tôi không muốn làm tiếp nữa.")])],
   notes=["Phân biệt: 起来 = bắt đầu (大家都笑了起来)；下去 = tiếp tục (我还要练下去)。", "轮: lần lượt, đến lượt – 我考完了，下一个就轮到你口试了。", "灵: hiệu nghiệm – 这种药真灵，吃了就不疼了。"],
   prac=["A:中国功夫你练了几年了？\nB:我已经练了三年了，我还要{练下去}。", "A:天气怎么样？\nB:天气{热起来}了，我应该买夏天的衣服了。"]),
],
ex=[
 pool("一、选词填空（片）", "Chữ “片” (tấm mỏng) tạo từ 照片/名片/卡片/面包片. Chọn từ điền vào chỗ trống.", ["照片", "名片", "卡片", "面包片"], [
   "认识您很高兴。对不起，我今天没带【名片】。", "这次去云南，我们拍了很多【照片】。", "为了帮助记生词，我写了很多生词【卡片】。", "他的早饭就是【面包片】、牛奶，很简单。"]),
 match("二、连线", "“浴” là tắm. Nối từ có chữ “浴” với lời giải thích.", ["晒太阳", "洗澡前后穿的衣服", "洗澡的房间", "洗澡时用的大毛巾", "许多人同时洗澡的地方"],
   [("浴室", "洗澡的房间"), ("浴巾", "洗澡时用的大毛巾"), ("浴衣", "洗澡前后穿的衣服"), ("日光浴", "晒太阳"), ("浴池", "许多人同时洗澡的地方")]),
 pool("三、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["世界", "轮", "突然", "干", "讨厌", "敢", "继续", "认真", "记得", "小时候"], [
   "今天【轮】到谁打扫房间了？", "他最【讨厌】做事不【认真】的人。", "我不【敢】一个人走夜路，你陪着我吧。", "这个【世界】真的太小了，我们又见面了。",
   "您还【记得】吗？两年前我们见过面。", "你想【继续】学习汉语吗？", "【小时候】我就很想做出租车司机，现在真的【干】上这个工作了。", "刚才天气那么好，怎么【突然】下起雨来了？"]),
 opn("四、模仿例子完成句子", "Hoàn thành câu theo mẫu. Ví dụ: 老师讲的故事很有意思，大家都笑了起来。", [
   ("雨又______了，咱们明天再见面吧。", "雨又下起来了，咱们明天再见面吧。"), ("你干得______，继续干下去吧。", "你干得很好，继续干下去吧。"),
   ("我就怕热，我希望______下去了。", "我就怕热，我希望天气别再热下去了。"), ("大家______音乐跳起舞来。", "大家听着音乐跳起舞来。"),
   ("刚才两个人还______呢，怎么突然吵起来了？", "刚才两个人还好好儿的呢，怎么突然吵起来了？")]),
 opn("五、根据提示完成对话", "Hoàn thành hội thoại theo gợi ý.", [
   ("A：明天是周末，我们出去玩儿玩儿吧。\nB：______呀，听说明天刮大风。（V+什么）", "玩儿什么呀，听说明天刮大风。"),
   ("A：小王的身体渐渐______了，下星期就可以上班了。（起来）\nB：他上星期都病得______床了，好得可真快。（不了）", "好起来 / 起不了"),
   ("A：你还能继续住在中国朋友家里吗？\nB：我的朋友说如果我愿意，就可以______。（下去）", "就可以一直住下去。"),
   ("A：她高兴得哭了。\nB：她真奇怪，别人高兴都笑，她怎么______了？（起来）", "她怎么哭起来了？"),
   ("A：是谁呀？这么晚了，______？（什么）\nB：对不起，我明天有钢琴比赛，今天不得不练习。", "这么晚了，还弹什么钢琴？")]),
 opn("六、情境表达", "Câu nào dùng trong tình huống nào; tình huống sau nên nói thế nào?", [
   ("“还玩儿什么！快走吧！”“你说得很好，请继续说下去。”“他那么忙，来得了吗？”——在什么情况下可以说？", "时间不早了，别人还在玩儿的时候；别人说话停下来了，你想让他接着说的时候；担心别人太忙不能来的时候。"),
   ("别人请你参加晚会，你不能去，怎么说更好？（去不了）", "谢谢你请我，可是那天我有事，去不了。"),
   ("晚会上你希望大家开始唱歌跳舞，该怎么说？（起来）", "大家一起唱起来、跳起来吧！"),
   ("你告诉别人，如果继续努力，一定能成功，你还能找出别的说法吗？（下去）", "只要你努力下去，就一定能成功。")]),
 opn("七、回忆课文内容，补出短文中没有出现的动词", "Điền động từ còn thiếu theo nội dung bài khóa.", [
   ("突然，一个人（　）着浴巾从浴室里（　）出来，对着我大（　）：“你在（　）什么呢？火都（　）了！”是爸爸，他最（　）做事不认真的人。", "围 / 冲 / 叫 / 干 / 灭 / 讨厌"),
   ("我说：“对不起！我在（　）地图呢。”爸爸生气地说：“（　）什么地图！快（　）火！”“我在看埃及地图呢。”我小声（　）。", "看 / 看 / 烧 / 说"),
   ("爸爸更生气了，（　）了我一巴掌：“看什么埃及地图！你一辈子也（　）不了那么远的地方！”我不敢再看下去了，只好（　）下地图，继续烧水。我一边烧水一边（　）：“我真的去不了埃及吗？”", "打 / 去 / 放 / 想")]),
 opn("八、根据课文内容回答问题", "Trả lời câu hỏi theo nội dung bài khóa.", [
   ("“我”为什么想去埃及？", "因为“我”最喜欢的国家是埃及。"), ("“我”为什么第一次出国就选择了埃及？", "因为这是“我”小时候的理想，爸爸说“我”一辈子也去不了，“我”一直努力。"),
   ("爸爸为什么打了“我”？是因为不喜欢“我”看地图吗？", "不是，是因为“我”做事不认真，看地图看得火都灭了。"),
   ("“我”为什么要谢谢爸爸？", "因为爸爸的那句话让“我”努力了20年，实现了理想。"), ("爸爸为什么感到不好意思？", "因为他不记得自己说过那样的话，还打了孩子。")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("朋友的爸爸不爱他。", False), ("朋友后天要去南非工作。", True), ("爸爸去书房拿出来一本《中国地图》。", False), ("爸爸知道南非在哪里。", False), ("他们的家在南京。", True)],
   passage="我的一个朋友，跟他爸爸的关系不太好。父子俩不太说话。朋友觉得爸爸不爱他。\n最近，朋友要去南非（South Africa）工作。回到家里，吃完饭，他对爸爸说：“爸，我要到南非去工作了。”\n“南非？什么时候走？”爸爸吃惊地问。“后天。”“那……那什么时候回来？”“我不知道。”“哦，……”\n儿子突然看见爸爸眼睛里有眼泪。爸爸站了起来，向书房走去。儿子看着爸爸的背影，眼睛也有些湿了。\n过了一会儿，父亲拿着一本《世界地图》和一支钢笔走出来，问儿子：“南非在哪里？”儿子指着说：“看，就在这里。”爸爸用笔画了一条红线，把南京和南非连在了一起。\n然后，爸爸对儿子说：“我去不了南非，想你的时候，就看看这张地图吧。”"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("朋友为什么觉得爸爸不爱他？", "因为父子俩不太说话，关系不太好。"), ("爸爸为什么拿来《世界地图》？", "他想知道南非在哪里，想儿子的时候就看看地图。"),
   ("从什么地方可以看出来爸爸其实很爱儿子？", "爸爸眼睛里有眼泪；他用红线把南京和南非连在一起，说想儿子的时候就看看地图。")]),
 opn("十、说一说，写一写", "Viết đoạn văn ngắn 《童年的理想》 khoảng 60 chữ.", [
   ("你小时候有什么梦想？现在你的梦想实现了吗？你还在为实现童年的梦想努力吗？",
    "（参考）小时候我的梦想是当一名老师。那时候我常常和朋友们玩儿“上课”的游戏。现在我还是学生，梦想还没实现，但是我一直在努力学习。我相信只要继续努力下去，我的梦想一定能实现。")]),
])

B[8] = dict(zh="旧梦", en="An Old Memory", vi="Giấc mơ xưa",
intro="Đây là một câu chuyện có thật. Mấy chục năm trước, tình bạn giữa một cậu bé Trung Quốc và một cô bé nước ngoài nay đã trở thành ký ức đẹp nhất và nỗi nhớ sâu sắc trong lòng một ông lão.",
vocab=V("""
旧梦|jiùmèng|dt|giấc mơ xưa, chuyện cũ
闭|bì|dong|nhắm, đóng
往事|wǎngshì|dt|chuyện cũ, chuyện đã qua
进入|jìnrù|dong|đi vào
梦|mèng|dt|giấc mơ
一生|yìshēng|dt|cả đời
中|zhōng|dt|trong
难忘|nánwàng|tt|khó quên
老年|lǎonián|dt|tuổi già
忘记|wàngjì|dong|quên
同事|tóngshì|dt|đồng nghiệp
有时|yǒushí|pho|có khi, đôi khi
出现|chūxiàn|dong|xuất hiện
比|bǐ|gioi|so với, hơn
矮|ǎi|tt|thấp (người)
双|shuāng|lg|đôi
年级|niánjí|dt|lớp, khối lớp
年龄|niánlíng|dt|tuổi tác
马路|mǎlù|dt|đường phố
领|lǐng|dong|dẫn, dắt
照顾|zhàogù|dong|chăm sóc
拉(手)|lā (shǒu)|dong|nắm (tay), kéo
使劲儿|shǐ jìnr|dong|ra sức, dùng sức
亲|qīn|dong|hôn
告别|gàobié|dong|chia tay, từ biệt
飞吻|fēiwěn|dt|nụ hôn gió
刚刚|gānggāng|pho|vừa mới
爱情|àiqíng|dt|tình yêu (nam nữ)
并|bìng|pho|(đặt trước từ phủ định để nhấn mạnh) hoàn toàn (không)
初恋|chūliàn|dt|mối tình đầu
活|huó|dong|sống
打听|dǎting|dong|hỏi thăm, dò hỏi
消息|xiāoxi|dt|tin tức
广东话|Guǎngdōnghuà|rieng|tiếng Quảng Đông
司苔拉|Sītáilā|rieng|Stella (tên người)
"""),
texts=[dict(t="旧梦", narr=True, lines=T("""
人老了，梦就多起来了，一闭上眼睛，往事就进入梦里。|Người già rồi thì mơ nhiều lên, vừa nhắm mắt là chuyện cũ đã hiện về trong mơ.
在人的一生中，什么最难忘呢？是小时候遇到过的人和事。|Trong cuộc đời một người, điều gì khó quên nhất? Đó là những người và việc đã gặp hồi nhỏ.
到了老年的时候，最近几年的事差不多都忘记了，老同事的名字，有时都想不起来了，|Đến tuổi già, chuyện mấy năm gần đây hầu như quên hết, tên đồng nghiệp cũ có khi cũng không nhớ ra,
可是童年的朋友却忘不了，他们会常常在梦里出现。|nhưng bạn bè thời thơ ấu thì lại không quên được, họ thường xuất hiện trong giấc mơ.
最近经常出现在我梦里的是一个外国女孩子，她的名字叫司苔拉。|Người gần đây hay xuất hiện trong giấc mơ của tôi là một cô bé nước ngoài, tên là Stella.
司苔拉比我大，但只比我大一点儿。她家跟我家是邻居。|Stella lớn hơn tôi, nhưng chỉ lớn hơn một chút. Nhà cô ấy và nhà tôi là hàng xóm.
我记得，她比中国女孩子高得多，我比她矮一头。|Tôi nhớ cô ấy cao hơn con gái Trung Quốc nhiều, tôi thấp hơn cô ấy một cái đầu.
她的头发又黑又长，还有一双美丽的蓝眼睛。|Tóc cô vừa đen vừa dài, còn có đôi mắt xanh rất đẹp.
她会说英语，也会说广东话，她说广东话比我还好。她真聪明！|Cô biết nói tiếng Anh, cũng biết nói tiếng Quảng Đông, nói tiếng Quảng Đông còn giỏi hơn tôi. Cô ấy thật thông minh!
我上小学二年级的时候，年龄很小，我一个人过马路上学，妈妈不放心，|Hồi tôi học lớp hai, còn rất nhỏ, một mình qua đường đi học, mẹ không yên tâm,
就请这位外国姐姐领着我上学、领着我回家。|nên nhờ chị gái nước ngoài này dắt tôi đi học, dắt tôi về nhà.
司苔拉真的像姐姐一样照顾我，她拉着我的手，在马路上跳着走；|Stella thật sự chăm sóc tôi như một người chị, cô nắm tay tôi, vừa đi vừa nhảy chân sáo trên đường;
有时还使劲儿地亲我的脸；每天告别的时候还送给我一个飞吻。|có khi còn hôn mạnh lên má tôi; mỗi ngày lúc chia tay còn gửi tôi một nụ hôn gió.
那时我刚刚八岁，在那个年龄，还不懂“爱情”。|Khi ấy tôi vừa tròn tám tuổi, ở tuổi đó chưa hiểu “tình yêu” là gì.
但是我知道，司苔拉很喜欢我，我也喜欢这个姐姐，虽然她不是中国人。|Nhưng tôi biết Stella rất quý tôi, tôi cũng quý người chị này, dù cô ấy không phải người Trung Quốc.
我跟她的关系并不是什么“初恋”，可是为什么到了老年，司苔拉会经常出现在我的梦里呢？|Quan hệ giữa tôi và cô ấy hoàn toàn không phải “mối tình đầu” gì cả, nhưng sao đến tuổi già, Stella lại hay xuất hiện trong giấc mơ của tôi?
司苔拉是不是还活在这个世界上呢？到哪里才能打听到她的消息呢？|Stella có còn sống trên đời này không? Đến đâu mới hỏi thăm được tin tức của cô ấy?
"""), q=Q("""
人老了会有什么变化？|梦就多起来了，一闭上眼睛，往事就进入梦里。|Mơ nhiều hơn, nhắm mắt là chuyện cũ hiện về.
在人的一生中，什么会留下最深的印象？|小时候遇到过的人和事。|Những người và việc gặp hồi nhỏ.
“我”最近经常梦见的是谁？|一个外国女孩子，叫司苔拉。|Một cô bé nước ngoài tên Stella.
司苔拉和“我”是什么关系？|邻居，她像姐姐一样照顾“我”。|Hàng xóm, chăm sóc “tôi” như chị.
司苔拉长什么样？|比中国女孩子高得多，头发又黑又长，有一双美丽的蓝眼睛。|Cao, tóc đen dài, mắt xanh đẹp.
“我”为什么觉得司苔拉聪明？|她会说英语，也会说广东话，说广东话比“我”还好。|Biết tiếng Anh và tiếng Quảng Đông, nói giỏi hơn “tôi”.
妈妈为什么请司苔拉领着“我”上学、放学？|因为“我”年龄很小，一个人过马路，妈妈不放心。|Vì “tôi” còn nhỏ, mẹ không yên tâm.
司苔拉是怎么照顾“我”的？|拉着“我”的手在马路上跳着走，亲“我”的脸，告别时送“我”一个飞吻。|Nắm tay, hôn má, gửi hôn gió.
“我”当时不懂什么？但是知道什么？|不懂“爱情”，但是知道司苔拉很喜欢“我”。|Chưa hiểu tình yêu, nhưng biết Stella quý mình.
从哪些句子能看出“我”对司苔拉的思念？|司苔拉是不是还活在这个世界上呢？到哪里才能打听到她的消息呢？|Những câu hỏi cuối bài.
"""))],
grammar=[
 G("bi", "司苔拉比我大。", "A 比 B + Adj/VP: câu so sánh",
   "So sánh mức độ, tính chất. Phủ định: (1) A 没有 B + Adj (A không bằng B); (2) A 不比 B + Adj (A và B ngang nhau hoặc xấp xỉ).",
   [F("A:A|kw:比|B:B|V:Adj / VP", [
      ("他|[比]|我|努力", "。", "Anh ấy chăm chỉ hơn tôi."),
      ("今天|[比]|昨天|冷", "。", "Hôm nay lạnh hơn hôm qua."),
      ("你|[比]|我|唱得好", "。", "Bạn hát hay hơn tôi.")], cap="Khẳng định"),
    F("A:A|kw:没有 / 不比|B:B|V:Adj / VP", [
      ("弟弟|[没有]|我|高", "。", "Em trai không cao bằng tôi."),
      ("我的汉语|[没有]|他的|好", "。", "Tiếng Hán của tôi không giỏi bằng anh ấy."),
      ("今天和昨天差不多，|[不比]|昨天|冷", "。", "Hôm nay cũng như hôm qua, không lạnh hơn."),
      ("他其实|[不比]|我|高", "。", "Thật ra anh ấy không cao hơn tôi.")], cap="Phủ định")],
   prac=["A:这个城市大吗？\nB:这个城市{没有那个城市}大，人口却比那个城市多。", "A:你说得比他好吧？\nB:我比他学汉语的时间长，可是说得却{没有他好}。"]),
 G("bi_shuliang", "她比中国女孩子高得多，我比她矮一头。", "A 比 B + Adj + mức độ / số lượng",
   "Sau tính từ có thể thêm mức độ (一点儿、得多、多了) hoặc số lượng cụ thể.",
   [F("A:A|kw:比|B:B|V:Adj/VP|Nu:Mức độ / số lượng", [
      ("长江|[比]|黄河|长|一点儿", "。", "Trường Giang dài hơn Hoàng Hà một chút."),
      ("这儿的东西|[比]|我们国家|便宜|多了", "。", "Đồ ở đây rẻ hơn nước tôi nhiều."),
      ("姐姐|[比]|弟弟|大|五岁", "。", "Chị lớn hơn em trai năm tuổi."),
      ("他|[比]|我|多喝|三瓶（啤酒）", "。", "Anh ấy uống nhiều hơn tôi ba chai bia.")])],
   notes=["Không dùng 很、非常、太 trong câu chữ 比: ✗ 他比我很高。✓ 他比我高得多。"]),
 G("bi_haigeng", "她说广东话比我还好。", "A 比 B + 还/更 + Adj: còn… hơn",
   "Khẳng định B đã đạt mức nhất định, nhấn mạnh A còn hơn thế.",
   [F("A:A|kw:比|B:B|kw2:还/更|V:Adj/VP", [
      ("昨天比前天暖和，今天|[比]|昨天|[还]|暖和", "。", "Hôm qua ấm hơn hôm kia, hôm nay còn ấm hơn hôm qua."),
      ("这个月|[比]|上个月|[更]|忙", "。", "Tháng này còn bận hơn tháng trước."),
      ("我觉得这个故事|[比]|那个故事|[更]|有意思", "。", "Tôi thấy câu chuyện này còn hay hơn chuyện kia.")])],
   prac=["A:她的英语真好。\nB:{她的法语更好}。", "A:我很早就到教室了。\nB:{她比你还早}。"]),
 G("bing_xiang", "我跟她的关系并不是什么“初恋”。", "并 + 不/没 · 像……一样 · 闭上 · 想不起来",
   "Một số từ ngữ trong bài.",
   notes=["并: đặt trước từ phủ định, nhấn mạnh (trái với suy nghĩ) – 他们都说汉语难，我觉得汉语并不难。",
          "A 像 B 一样: A giống như B – 他家像图书馆一样，到处都是书。/ 那里的风景像画儿一样美。",
          "V + 上: có kết quả (đóng lại) – 闭上眼睛 / 合上书 / 关上电视 / 关上门。",
          "想不起来: không nhớ ra – 我认识他，可是想不起来他叫什么名字了。"]),
],
ex=[
 pool("一、选词填空（年）", "“年” chỉ giai đoạn trong đời: 童年/少年/青年/中年. Chọn từ điền vào chỗ trống.", ["童年", "少年", "青年", "中年"], [
   "人的一生要经历从【童年】、【少年】到【青年】、【中年】，再到老年的生命过程。"]),
 pool("一、选词填空（同）", "“同” là giống nhau: 同学/同屋/同岁/同乡. Chọn từ điền vào chỗ trống.", ["同学", "同屋", "同岁", "同乡"], [
   "我们过去是【同学】，在同一个学校上学，现在是同事，在同一家公司工作。", "我和我的【同屋】轮流打扫房间。", "我和我的男朋友【同岁】，他的生日比我大一点儿。", "我和我的【同乡】常常在一起用家乡话聊天儿，在一起做家乡菜。"]),
 pool("二、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["忘记", "同事", "有时", "出现", "年级", "年龄", "照顾", "刚刚", "告别", "打听", "消息"], [
   "他是我的【同事】，我们在一起工作三年了。", "这几天天气不好，【有时】刮风，有时下雨。", "谢谢你对我的【照顾】！", "他【年龄】比我小一岁，在学校却比我高一个【年级】。",
   "最近【出现】了许多新歌手。", "对不起，我【忘记】了你的手机号码，能再告诉我一遍吗？", "我们【刚刚】认识，就成了好朋友。", "我向很多人【打听】他的【消息】，可是大家都说不知道。", "我明天就回国了，今天来向您【告别】。"]),
 pick("三、选择意思相近的词语填空", "Chọn từ thích hợp (từ gần nghĩa).", [
   (["闭", "关"], ["请【闭】上眼睛，认真听。", "请【关】上门。"]),
   (["忘记", "想不起来"], ["你别【忘记】吃药。", "他的名字，我怎么也【想不起来】了。"]),
   (["告别", "再见"], ["我下星期走，来和大家说【再见】。", "他来跟我们【告别】。"]),
   (["矮", "低"], ["他的个子比我【矮】一头。", "我的汉语水平很【低】。"]),
   (["岁", "年龄"], ["你的孩子几【岁】了？", "他的【年龄】比我小。"])]),
 opn("四、把下面的词语整理成句子", "Sắp xếp các từ thành câu.", [
   ("这本小说　没有　有意思　那本", "这本小说没有那本有意思。"), ("我　比　晚　姐姐　睡得", "姐姐比我睡得晚。（我比姐姐睡得晚。）"),
   ("这儿的东西　比　不　贵　我们那儿", "这儿的东西不比我们那儿贵。"), ("这种啤酒　青岛啤酒　好喝　没有", "这种啤酒没有青岛啤酒好喝。"), ("这辆汽车　新　那辆　比", "这辆汽车比那辆新。")]),
 opn("五、模仿例子完成对话", "Hoàn thành hội thoại theo mẫu. Ví dụ: 昨天20℃，今天21℃。今天比昨天热吗？→ 今天比昨天热一点儿。", [
   ("这件衣服150元，那件衣服152元。\nA：那件衣服比这件衣服贵吗？\nB：______。（一点儿）", "那件衣服比这件贵一点儿。"),
   ("城市A离这里有900多公里，城市B离这里有890多公里。\nA：城市B比城市A远吗？\nB：______。（不比）", "城市B不比城市A远。"),
   ("今年的新生是3000人，去年的新生是3100人。\nA：______？（比）\nB：今年的新生没有去年多。", "今年的新生比去年多吗？"),
   ("这种水果好吃，那种水果不好吃。\nA：那种水果比这种好吃吗？\nB：______。（没有）", "那种水果没有这种好吃。")]),
 opn("六、情境表达", "Câu nào dùng trong tình huống nào; tình huống sau nên nói thế nào?", [
   ("“这本词典不比那本贵。”“这个故事比那个故事更有意思。”“明天比今天还暖和。”——在什么情况下可以说？", "两本词典价钱差不多的时候；两个故事都有意思，这个更有意思的时候；今天已经很暖和，明天会更暖和的时候。"),
   ("有人认为汉语比日语难，你认为差不多，你该怎么说？（不比）", "我觉得汉语不比日语难。"),
   ("你觉得在北京很舒服，跟在你的家乡差不多，该怎么说？（像……一样）", "在北京就像在我的家乡一样舒服。"),
   ("有人说中国的东西很贵，你不同意这个说法，你该怎么说？（并）", "中国的东西并不贵。")]),
 opn("七、猜谜语（谜底在本课找）", "Đoán câu đố (đáp án là từ trong bài).", [
   ("长的比短的少，短的比长的多，短的用脚踩（cǎi），长的用手摸（mō）。（打一用具）", "梯子（cái thang）"),
   ("弟弟不比哥哥高，哥哥不比弟弟大，睡觉的时候很安静，起了床就打架。（打一餐具）", "筷子（đôi đũa）")]),
 opn("八、根据课文内容完成对话", "Hoàn thành hội thoại theo nội dung bài khóa.", [
   ("A：您觉得人的一生中什么最难忘？\nB：______的人和事。", "小时候遇到过"),
   ("A：为什么这么说呢？\nB：人到了老年，最近几年的事差不多都______了，老同事的名字，有时都______了，可是童年的朋友却______，他们会常常在______出现。", "忘记 / 想不起来 / 忘不了 / 梦里"),
   ("A：最近经常出现在您梦里的是什么人？\nB：是一个叫司苔拉的外国女孩儿。她又漂亮又聪明，广东话说得______。", "比我还好"),
   ("A：你们是怎么认识的？\nB：她家跟我家是邻居。我上小学二年级的时候，妈妈请她______。她像______照顾我。", "领着我上学、领着我回家 / 姐姐一样"),
   ("A：她是您的“初恋”吗？\nB：我们的关系并______，我们太小，还不懂“爱情”。\nA：司苔拉现在怎么样了？\nB：我不知道她是不是______，也不知道到哪里才能打听到______。", "不是什么“初恋” / 还活在这个世界上 / 她的消息")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("男青年觉得农村什么都比城里的好。", False), ("爸爸因为儿子不喜欢自己的家乡，很生气。", True), ("中国的中秋节是农历八月十五。", True), ("儿子说城里的月饼没有家乡的月饼好吃。", False), ("爸爸没批评儿子，是因为太生气了。", False)],
   passage="有一个男青年，刚刚从城里回到了农村，他总说城里什么都比农村的好，他爸爸听了很生气。\n农历的八月十五日是中国的传统节日——中秋节，中国人有吃月饼和赏月（shǎng yuè）的风俗。爸爸一边吃月饼一边说：“今年的月饼真好吃！”儿子马上说：“您吃过城里的月饼吗？城里的月饼比这里的好吃多了！”爸爸听了很生气，可是因为今天过节，就没批评他。\n爸爸看着天上的月亮说：“今晚的月亮真圆啊！”儿子又说：“圆什么？城里的月亮比这儿的月亮圆多了！”爸爸太生气了，打了儿子一巴掌。儿子却笑着说：“城里人比您打得使劲儿多了！”"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("男青年从城里回来后有哪些变化？", "他总说城里什么都比农村的好。"), ("爸爸为什么生气打了儿子一巴掌？", "因为儿子说城里的月亮比这儿的月亮圆多了，爸爸太生气了。")]),
 opn("十、说一说，写一写", "Viết đoạn văn 《我最好的朋友》 khoảng 70 chữ.", [
   ("你最好的朋友是什么时候的朋友？他/她是一个什么样的人？你们在一起有过什么难忘的事？他/她现在在哪里？你们还有联系吗？（往事　难忘　忘不了　想起来　告别　出现　梦里　消息　打听）",
    "（参考）我最好的朋友是我的小学同学小林。她比我高一点儿，又聪明又热情。小时候我们每天一起上学，一起玩儿，这些往事我永远忘不了。后来她家搬走了，我们告别的时候都哭了。现在我常常向别人打听她的消息，有时她还会在我的梦里出现。")]),
])
