# -*- coding: utf-8 -*-
# 发展汉语·初级综合(II) – Bài 3, 4
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[3] = dict(zh="卖辣椒的女孩儿", en="The Girl Selling Chili Peppers", vi="Cô bé bán ớt",
intro="Một cô bé bán ớt ở chợ. Ngày đầu, ớt vừa tươi vừa đẹp mà không bán được quả nào. Nhưng đến ngày thứ tư, cô bé lại bán hết sạch. Hãy xem “kỳ tích” này đã xảy ra như thế nào.",
vocab=V("""
辣椒|làjiāo|dt|ớt
市场|shìchǎng|dt|chợ, thị trường
经验|jīngyàn|dt|kinh nghiệm
篮子|lánzi|dt|cái giỏ
新鲜|xīnxiān|tt|tươi
相信|xiāngxìn|dong|tin, tin tưởng
顾客|gùkè|dt|khách hàng
辣|là|tt|cay
甜|tián|tt|ngọt
摇头|yáo tóu|dong|lắc đầu
姑娘|gūniang|dt|cô gái
赶紧|gǎnjǐn|pho|vội vàng, nhanh chóng
怕|pà|dong|sợ, lo
难过|nánguò|dong|buồn, khó chịu
想不通|xiǎng bu tōng|cum|nghĩ không ra, không hiểu nổi
味道|wèidao|dt|mùi vị
既……也……|jì……yě……|cum|vừa… vừa…, đã… lại…
中间|zhōngjiān|dt|ở giữa
香|xiāng|tt|thơm, ngon
奇迹|qíjì|dt|kỳ tích, phép màu
发生|fāshēng|dong|xảy ra
四川|Sìchuān|rieng|tỉnh Tứ Xuyên
山东|Shāndōng|rieng|tỉnh Sơn Đông
"""),
texts=[dict(t="卖辣椒的女孩儿", narr=True, lines=T("""
有个女孩儿到市场去卖辣椒。|Có một cô bé ra chợ bán ớt.
第一天，因为没有经验，她只带了一篮子辣椒。|Ngày đầu tiên, vì chưa có kinh nghiệm, cô chỉ mang một giỏ ớt.
她的辣椒红红的，又好看又新鲜，女孩儿相信自己的辣椒一定好卖。|Ớt của cô đỏ au, vừa đẹp vừa tươi, cô bé tin rằng ớt của mình nhất định dễ bán.
第一个顾客走过来问：“这辣椒是辣的还是甜的？”|Người khách đầu tiên đi tới hỏi: “Ớt này cay hay ngọt?”
女孩儿站起来热情地回答：“辣椒当然是辣的了。”|Cô bé đứng dậy nhiệt tình trả lời: “Ớt thì đương nhiên là cay rồi.”
顾客摇摇头说：“我是上海人，喜欢吃甜的。”|Khách lắc đầu nói: “Tôi là người Thượng Hải, thích ăn ngọt.”
第二位顾客走过来问：“这辣椒是辣的还是甜的？”|Vị khách thứ hai đi tới hỏi: “Ớt này cay hay ngọt?”
小姑娘赶紧回答：“甜的。”|Cô bé vội trả lời: “Ngọt ạ.”
顾客又摇了摇头说：“我是四川人，不怕辣，就怕不辣。不辣的就不能叫辣椒。”|Khách lại lắc đầu: “Tôi là người Tứ Xuyên, không sợ cay, chỉ sợ không cay. Không cay thì không gọi là ớt được.”
这一天，小姑娘一个辣椒都没卖出去，她只好把辣椒拿回家去。|Hôm đó, cô bé không bán được quả ớt nào, đành phải mang ớt về nhà.
女孩儿很难过，她怎么也想不通：这么好的辣椒，为什么会卖不出去呢？|Cô bé rất buồn, nghĩ mãi không hiểu: ớt ngon thế này, sao lại không bán được?
第二天，她带了两篮子辣椒去市场卖，一篮子是辣的，一篮子是甜的。|Ngày thứ hai, cô mang hai giỏ ớt ra chợ bán, một giỏ cay, một giỏ ngọt.
上海人买了甜的，四川人买了辣的。|Người Thượng Hải mua ớt ngọt, người Tứ Xuyên mua ớt cay.
一个北京人走过来问：“这辣椒是什么味道的？”|Một người Bắc Kinh đi tới hỏi: “Ớt này vị gì thế?”
小姑娘回答：“左边的篮子里是辣的，右边的篮子里是甜的。”|Cô bé trả lời: “Giỏ bên trái là ớt cay, giỏ bên phải là ớt ngọt.”
顾客摇了摇头说：“怎么没有既不辣也不甜的青椒呢？”|Khách lắc đầu: “Sao không có ớt xanh chẳng cay cũng chẳng ngọt nhỉ?”
第三天，她带了三篮子辣椒去卖，一篮子甜的，一篮子辣的，一篮子既不辣又不甜的。|Ngày thứ ba, cô mang ba giỏ ớt đi bán: một giỏ ngọt, một giỏ cay, một giỏ không cay cũng không ngọt.
上海人、四川人、北京人买了不同味道的辣椒。|Người Thượng Hải, Tứ Xuyên, Bắc Kinh đều mua được ớt có vị mình thích.
一个山东人走过来问：“这辣椒是什么味道的？”|Một người Sơn Đông đi tới hỏi: “Ớt này vị gì thế?”
小姑娘回答：“左边的篮子里是甜的，右边的篮子里是辣的，中间的是既不辣又不甜的。”|Cô bé trả lời: “Giỏ bên trái là ngọt, giỏ bên phải là cay, giỏ ở giữa không cay cũng không ngọt.”
顾客摇了摇头说：“怎么没有又辣又甜又香的呢？”|Khách lắc đầu: “Sao không có loại vừa cay vừa ngọt vừa thơm nhỉ?”
第四天，她带了四篮子辣椒去卖，一篮子辣的，一篮子甜的，一篮子既不辣又不甜的，一篮子又辣又甜又香的。|Ngày thứ tư, cô mang bốn giỏ ớt đi bán: một giỏ cay, một giỏ ngọt, một giỏ không cay không ngọt, một giỏ vừa cay vừa ngọt vừa thơm.
这一天，奇迹发生了，小姑娘把所有的辣椒都卖出去了。|Hôm đó, kỳ tích đã xảy ra: cô bé bán được hết tất cả số ớt.
"""), q=Q("""
女孩儿为什么相信自己的辣椒一定好卖？|因为她的辣椒红红的，又好看又新鲜。|Vì ớt của cô đỏ au, vừa đẹp vừa tươi.
第一个顾客为什么没买辣椒？|因为他是上海人，喜欢吃甜的。|Vì ông ấy là người Thượng Hải, thích ăn ngọt.
第二个顾客为什么也没买？|因为他是四川人，不怕辣，就怕不辣。|Vì ông là người Tứ Xuyên, không sợ cay chỉ sợ không cay.
女孩儿第一天为什么一个辣椒也没卖出去？|因为她没有经验，只带了一种辣椒。|Vì cô chưa có kinh nghiệm, chỉ mang một loại ớt.
女孩儿想不通什么？|这么好的辣椒，为什么会卖不出去。|Ớt ngon như vậy sao lại không bán được.
第二天，女孩儿的生意好点儿了吗？为什么？|好点儿了，因为她带了辣的和甜的两种辣椒。|Khá hơn, vì cô mang cả ớt cay và ớt ngọt.
北京人为什么没买女孩儿的辣椒呢？|因为他想买既不辣也不甜的青椒。|Vì ông muốn mua ớt xanh không cay cũng không ngọt.
第三天，女孩儿的生意怎么样？为什么？|更好了，上海人、四川人、北京人都买了。|Tốt hơn nữa, người ba nơi đều mua.
山东人想买什么样的辣椒呢？|又辣又甜又香的辣椒。|Ớt vừa cay vừa ngọt vừa thơm.
第四天发生了什么奇迹？为什么？|她把所有的辣椒都卖出去了，因为每个顾客都能买到自己喜欢的味道。|Cô bán hết sạch ớt, vì khách nào cũng mua được vị mình thích.
"""))],
grammar=[
 G("fuhe_quxiang", "第一个顾客走过来。", "Bổ ngữ xu hướng kép: V + 上/下/进/出/回/过/起 + 来/去",
   "来/去 kết hợp với 上、下、进、出、回、过、起 đặt sau động từ, chỉ hướng của động tác. 来 = về phía người nói, 去 = rời xa người nói. Tân ngữ chỉ nơi chốn phải đặt TRƯỚC 来/去 (跑下山去); tân ngữ chỉ người/vật có thể đặt trước hoặc sau 来/去.",
   [F("S:Chủ ngữ|V:Động từ|kw:上/下/进/出/回/过/起|kw2:来/去|X:Phần sau", [
      ("她|跑|[出]|[去]|，又马上跑回来了", "。", "Cô ấy chạy ra ngoài, rồi lại chạy ngay về."),
      ("大家|站|[起]|[来]|，有的走了出去", "。", "Mọi người đứng dậy, có người đi ra ngoài."),
      ("快|爬|[上]|[来]|吧，山上可美了", "！", "Mau leo lên đây, trên núi đẹp lắm!")]),
    F("S:Chủ ngữ|V:Động từ|kw:Hướng|P:Nơi chốn|kw2:来/去", [
      ("小王|跑|[下]|山|[去]", "了。", "Tiểu Vương chạy xuống núi rồi."),
      ("他|跑|[回]|宿舍|[去]", "了。", "Anh ấy chạy về ký túc xá rồi.")], cap="Tân ngữ nơi chốn đặt trước 来/去"),
    F("S:Chủ ngữ|V:Động từ|O:Cách đặt tân ngữ chỉ vật", [
      ("她从学校|带|回来一本书", "。", "Cô ấy mang từ trường về một quyển sách."),
      ("她从学校|带|回一本书来", "。", "(cùng nghĩa)"),
      ("她从学校|带|了一本书回来", "。", "(cùng nghĩa)")], cap="Tân ngữ chỉ người/vật: 3 vị trí")],
   notes=["老师领进来一个新同学。→ người nói ở trong lớp.", "还没考完试，他的心早就飞回家去了。→ người nói không ở nhà."]),
 G("yi_dou_mei", "小姑娘一个辣椒都没卖出去。", "一 + lượng từ (+ danh từ) + 都/也 + 不/没: nhấn mạnh phủ định",
   "Nghĩa là “một … cũng không / chẳng … nào”, phủ định hoàn toàn.",
   [F("S:Chủ ngữ|kw:一+M|N:Danh từ|kw2:都/也|V:不/没 + V", [
      ("这几个字，我|[一个]||[都]|不认识", "。", "Mấy chữ này, tôi chẳng biết chữ nào."),
      ("上午，我|[一点儿]|水|[也]|没喝", "。", "Cả buổi sáng tôi chẳng uống chút nước nào."),
      ("这几天，我|[一句]|汉语|[也]|没说", "。", "Mấy hôm nay tôi chẳng nói câu tiếng Hán nào.")])],
   prac=["A:我早晨没吃饭。→\nB:我早晨{一口饭也没吃}。", "A:她刚到北京，还没有朋友。→\nB:她{一个朋友也没有}。", "A:我的钱都花了，钱包里没有钱了。→\nB:钱包里{一分钱也没有}了。"]),
 G("ji_ye", "怎么没有既不辣也不甜的青椒呢？", "既……也/又……: vừa… vừa…",
   "Hai trạng thái/tính chất cùng tồn tại; phủ định: 既不……也不…… (chẳng… cũng chẳng…).",
   [F("S:Chủ ngữ|kw:既|A:Tính chất 1|kw2:又/也|B:Tính chất 2", [
      ("这个菜|[既]|好吃|[又]|便宜", "。", "Món này vừa ngon vừa rẻ."),
      ("|[既]|会说英语|[又]|会说汉语", "，容易找工作。", "Vừa biết tiếng Anh vừa biết tiếng Hán thì dễ tìm việc."),
      ("两个人住一个房间，|[既]|不方便，|[也]|不安静", "。", "Hai người ở một phòng, vừa bất tiện lại không yên tĩnh.")])],
   prac=["A:你现在住的房子怎么样？\nB:{既大又干净}，我很满意。", "A:那个饭馆怎么样？\nB:{既不好吃也不便宜}，咱们别去那儿了。"]),
 G("ba_quxiang", "小姑娘把所有的辣椒都卖出去了。", "把 + O + V + bổ ngữ xu hướng",
   "Câu chữ 把, nhấn mạnh tân ngữ bị tác động và di chuyển theo hướng nào.",
   [F("kw:把|O:Tân ngữ|V:Động từ|kw2:Xu hướng", [
      ("请[把]|护照|拿|[出来]", "看一下。", "Xin đưa hộ chiếu ra cho xem một chút."),
      ("请[把]|椅子|拿|[进去]", "吧。", "Hãy mang ghế vào trong."),
      ("[把]|书包|送|[回宿舍去]", "，我们去打球吧。", "Mang cặp sách về ký túc xá đi, chúng ta đi chơi bóng.")])],
   notes=["怕: sợ, lo (我怕迟到，很早就起床了。– Tôi sợ muộn nên dậy rất sớm.)", "只好: đành phải (我的手机没电了，只好打公用电话了。)",
          "想不通: không hiểu nổi (这么努力，还是进步不快，我想不通为什么。)", "所有: tất cả, đặt trước danh từ (这里所有的东西都是公司的。)"]),
],
ex=[
 pool("一、选词填空（好）", "“好+V”: 好看/好吃/好听/好喝. Chọn từ điền vào chỗ trống.", ["好看", "好吃", "好听", "好喝"], [
   "这件衣服真【好看】，你穿很合适。", "这首歌太【好听】了，你教我唱吧。", "青岛啤酒很【好喝】，我喝过。", "北京烤鸭很【好吃】，我吃过。"]),
 pool("一、选词填空（难）", "“难+V”: 难吃/难听/难喝/难看. Chọn từ điền vào chỗ trống.", ["难吃", "难听", "难喝", "难看"], [
   "食堂的菜太【难吃】，我们还是去饭馆吧。", "这种药太【难喝】了，我不想喝。", "我写的汉字有点儿【难看】，请原谅。", "他唱歌真【难听】，他自己都不知道。"]),
 match("二、连线", "“好/难+V” còn chỉ việc dễ hay khó làm. Nối từ với lời giải thích.", ["容易洗干净", "不容易找到", "容易买到", "路的情况不好，不容易走", "不容易学会", "容易记住"],
   [("好买", "容易买到"), ("好洗", "容易洗干净"), ("好记", "容易记住"), ("难找", "不容易找到"), ("难学", "不容易学会"), ("难走", "路的情况不好，不容易走")]),
 pool("三、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["经验", "新鲜", "相信", "热情", "赶紧", "只好", "想不通", "发生", "所有"], [
   "这些水果是刚买的，很【新鲜】。", "商店已经关门了，我们【只好】明天去买了。", "我刚来公司工作，没有【经验】。", "这个老板对顾客很【热情】，所以来他的饭馆吃饭的人很多。",
   "他做事很认真，【相信】他一定能做好。", "来了这么多人，【发生】了什么事？", "他在我们学校很有名，学校里【所有】的人都认识他。", "我们【赶紧】走吧，要迟到了。", "我【想不通】他为什么这么做。"]),
 opn("四、根据提示完成句子", "Hoàn thành câu theo gợi ý.", [
   ("早晨起床太晚了，我一口饭______，就来上课了。（也没+V）", "早晨起床太晚了，我一口饭也没吃，就来上课了。"),
   ("我现在一分钱______，怎么办？（也没+V）", "我现在一分钱也没有，怎么办？"),
   ("这本书______，你应该看看。（既……又……）", "这本书既有意思又不太难，你应该看看。"),
   ("A：请你______，给我们看看。（把……V出来）\nB：我现在没有她的照片，明天吧。", "请你把你女朋友的照片拿出来，给我们看看。")]),
 pick("五、按说话人的位置，写出“来/去”", "Chọn 来 hoặc 去 theo vị trí người nói.", [
   (["来", "去"], ["他从中国寄回【去】一些书。（说话人在中国）", "妈妈每星期打电话过【来】。（说话人是接电话的人）", "小王从马路对面跑过【来】。（说话人在小王对面）",
                   "那本书我还回【去】了。（说话人不是图书馆的人）", "她急急忙忙跑下【去】了。（说话人在楼上）", "这本书你要是喜欢，就买回【去】慢慢看吧。（说话人在书店）"])]),
 opn("六、根据提示，用复合趋向补语完成对话", "Hoàn thành hội thoại bằng bổ ngữ xu hướng kép.", [
   ("（A和B在火车站）\nA：请您把车票拿______看一下。\nB：给您。", "请您把车票拿出来看一下。"),
   ("（A在楼下，B在楼上）\nA：我忘了带伞，你能给我送______吗？\nB：好，我马上给你送______。", "你能给我送下来吗？——好，我马上给你送下去。"),
   ("（A和B住在学校宿舍，他们现在在校外）\nA：已经没有公共汽车了，我们只好坐出租车回去了。\nB：这里离学校也不太远，我们还是走______吧。", "我们还是走回去吧。"),
   ("（B从图书馆还书回来，遇见了A）\nA：你能把昨天看的那本书借给我看看吗？\nB：对不起，我刚把书还______。", "对不起，我刚把书还回去了。")]),
 opn("七、情境表达", "Câu nào dùng trong tình huống nào; tình huống sau nên nói thế nào?", [
   ("“请把护照拿出来看一下。”“能帮我把行李拿进来吗？”“我们只好走回去了。”——在什么情况下可以说？", "在机场、海关或宾馆前台检查护照的时候；行李很多，请别人帮忙拿进房间的时候；没有车了，只能走路回去的时候。"),
   ("你不理解你的朋友为什么不喜欢旅行。（想不通）", "我想不通你为什么不喜欢旅行。"),
   ("有人让你帮忙买一本书，你去了很多家书店都没买到。（难买）", "这本书太难买了，我去了很多家书店都没买到。"),
   ("中国朋友说话太快，你完全听不懂，你要求他说得慢一点儿。（一……都不……）", "你说得太快了，我一句都听不懂，请说慢一点儿。")]),
 opn("八、根据课文内容回答问题", "Trả lời câu hỏi theo nội dung bài khóa.", [
   ("卖辣椒的女孩儿第一天为什么只带了一种口味的辣椒？（没经验）", "因为她没有经验。"),
   ("女孩儿第一天先说辣椒是辣的，然后又说辣椒是甜的，你对这种做法怎么看？", "（参考）她太想卖出去了，可是做生意不应该说假话。"),
   ("你能根据课文内容说说中国四川、上海、北京、山东四个地方的人吃东西的口味吗？（辣、甜、香）", "四川人喜欢吃辣的，上海人喜欢吃甜的，北京人喜欢既不辣也不甜的，山东人喜欢又辣又甜又香的。")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("后羿是个力气很大的人。", True), ("后羿用箭射下来了所有的太阳。", False), ("后羿告诉那个太阳，每天必须升起来，不能落下去。", False), ("后羿射日以后，地球上开始有了白天和黑夜，也有了四季。", True)],
   passage="后羿射日\n很久很久以前，天上出现了十个太阳。那时候，只有白天，没有黑夜，又干又热，很多人和动物（dòngwù）都死了。\n有一个叫后羿（Hòuyì）的人，他既有力气，射（shè）箭（jiàn）又准（zhǔn）。为了救（jiù）地球，他用箭射下来九个太阳，只留下一个太阳。\n那个太阳害怕了，就跳进了大海里，不敢出来。天上一个太阳也没有了，地球变得又黑又冷。后羿找到了那个太阳，告诉它，每天早晨公鸡（gōngjī）一叫，它就得马上从海里升起来。\n从那以后，地球上有了白天和黑夜，有了四季，人和动物在地球上的生活，变得舒服极了。"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("很久以前为什么没有黑夜，只有白天？", "因为天上有十个太阳。"),
   ("后羿射落九个太阳以后，地球曾经变得怎么样？为什么？", "变得又黑又冷，因为剩下的那个太阳害怕了，跳进大海里不敢出来。"),
   ("后来地球为什么适合人和动物生活了？", "因为太阳每天早晨公鸡一叫就升起来，地球上有了白天和黑夜，有了四季。")]),
 opn("十、说一说，写一写", "Viết đoạn văn khoảng 60 chữ.", [
   ("写一篇小短文《如果我是老板》。（经验　顾客　所有的　只好　热情　一……也……　好+V　难+V　既……也/又……）",
    "（参考）如果我是老板，我想开一家咖啡馆。我没有经验，所以要先好好儿学习。我会对所有的顾客都很热情，我的咖啡既好喝又便宜。如果东西卖不出去，我就想想顾客喜欢什么，不会一个顾客也没有的。")]),
])

B[4] = dict(zh="我和中国有个约会", en="I Have a Date with China", vi="Tôi có một cuộc hẹn với Trung Quốc",
intro="Phim ảnh, võ thuật, tiếng Hán đã thay đổi cuộc sống của một chàng trai người Đức. Vì sao anh sang Trung Quốc du học? Vì sao muốn làm hướng dẫn viên và đầu bếp? Hóa ra anh có một cuộc hẹn với Trung Quốc.",
vocab=V("""
约会|yuēhuì|dt|cuộc hẹn
缘分|yuánfèn|dt|duyên, duyên phận
流行|liúxíng|dong|thịnh hành, phổ biến
功夫|gōngfu|dt|võ thuật, kung fu
不但|búdàn|lien|không những
而且|érqiě|lien|mà còn
做人|zuòrén|dong|làm người, cách đối nhân xử thế
道理|dàolǐ|dt|đạo lý, lẽ phải
挣|zhèng|dong|kiếm (tiền)
出息|chūxi|dt|tiền đồ, triển vọng
选择|xuǎnzé|dong|chọn, lựa chọn
后悔|hòuhuǐ|dong|hối hận
交(朋友)|jiāo (péngyou)|dong|kết (bạn)
文化|wénhuà|dt|văn hóa
元素|yuánsù|dt|yếu tố
唐装|tángzhuāng|dt|Đường trang (áo kiểu truyền thống TQ)
学费|xuéfèi|dt|học phí
因此|yīncǐ|lien|vì vậy, do đó
认真|rènzhēn|tt|nghiêm túc, chăm chỉ
厨师|chúshī|dt|đầu bếp
流|liú|dong|chảy
口水|kǒushuǐ|dt|nước bọt (流口水: thèm chảy nước miếng)
导游|dǎoyóu|dt|hướng dẫn viên du lịch
其实|qíshí|pho|thật ra, kỳ thực
成龙|Chéng Lóng|rieng|Thành Long (ngôi sao võ thuật Hồng Kông)
宫保鸡丁|gōngbǎo jīdīng|dt|gà xào cung bảo (món Tứ Xuyên)
麻婆豆腐|Mápó dòufu|dt|đậu phụ Ma Bà (món Tứ Xuyên cay tê)
"""),
texts=[dict(t="我和中国有个约会", narr=True, lines=T("""
我叫马丁，是从德国来的。|Tôi tên là Martin, đến từ nước Đức.
我和中国的缘分是从六岁开始的。|Duyên của tôi với Trung Quốc bắt đầu từ năm sáu tuổi.
那时正在流行成龙的电影，我就开始喜欢中国功夫了。|Hồi đó phim của Thành Long đang thịnh hành, tôi bắt đầu thích võ thuật Trung Quốc.
我有一个中国老师，他不但教我中国功夫，而且还教我很多做人的道理。|Tôi có một thầy giáo người Trung Quốc, thầy không những dạy tôi võ thuật mà còn dạy tôi nhiều đạo lý làm người.
后来，我又开始学习汉语。|Sau đó, tôi lại bắt đầu học tiếng Hán.
有人对我说：“学汉语没用，既不能挣大钱，也没什么出息。”|Có người nói với tôi: “Học tiếng Hán vô ích, vừa không kiếm được nhiều tiền, lại chẳng có tiền đồ gì.”
但是我还是选择了汉语，而且一点儿也不后悔。|Nhưng tôi vẫn chọn tiếng Hán, và không hề hối hận chút nào.
我交了很多中国朋友，我们一起吃中国菜，喝中国茶，谈中国文化，去中国旅行。|Tôi kết bạn với rất nhiều người Trung Quốc, chúng tôi cùng ăn món Trung, uống trà Trung Quốc, nói chuyện văn hóa Trung Hoa, đi du lịch Trung Quốc.
现在，不但我喜欢中国，我的家人和朋友也都喜欢中国。|Bây giờ, không chỉ tôi thích Trung Quốc mà gia đình và bạn bè tôi cũng đều thích.
在我的生活里，到处都能找到中国元素：|Trong cuộc sống của tôi, chỗ nào cũng có thể thấy yếu tố Trung Quốc:
我家的墙上挂着中国画，书架上放着中文书，我身上穿着唐装。|trên tường nhà tôi treo tranh Trung Quốc, trên giá để sách tiếng Trung, trên người tôi mặc áo Đường trang.
一年前我来到中国留学，学费是我利用假期打工挣的。|Một năm trước tôi sang Trung Quốc du học, học phí là do tôi tranh thủ kỳ nghỉ đi làm thêm kiếm được.
在中国，能经常和中国人用汉语聊天儿，因此我的汉语进步得很快，说得越来越好。|Ở Trung Quốc, tôi thường xuyên được nói chuyện bằng tiếng Hán với người Trung Quốc, vì vậy tiếng Hán của tôi tiến bộ rất nhanh, nói ngày càng tốt.
现在，我快毕业了，是得认真想一想工作的事了。|Bây giờ tôi sắp tốt nghiệp, đã đến lúc phải nghĩ nghiêm túc về chuyện việc làm.
做什么工作好呢？当中国饭馆的厨师挺好，这样我就可以每天吃好吃的“宫保鸡丁”、“麻婆豆腐”了。|Làm việc gì thì tốt nhỉ? Làm đầu bếp nhà hàng Trung Quốc cũng hay, như thế ngày nào tôi cũng được ăn món “gà cung bảo”, “đậu phụ Ma Bà” ngon lành.
这些菜名，一想起来我就要流口水。|Những tên món này, cứ nhớ đến là tôi lại thèm chảy nước miếng.
给中国人当导游也不错，我可以每天说汉语，还可以交很多中国朋友。|Làm hướng dẫn viên cho người Trung Quốc cũng không tệ, ngày nào tôi cũng được nói tiếng Hán, lại kết được nhiều bạn Trung Quốc.
虽然当厨师、当导游都不能挣大钱，但是我都喜欢。|Tuy làm đầu bếp hay hướng dẫn viên đều không kiếm được nhiều tiền, nhưng tôi đều thích.
其实，到现在我还没想好以后做什么工作呢，|Thật ra, đến giờ tôi vẫn chưa nghĩ kỹ sau này sẽ làm gì,
但是，我知道我的工作一定和中国有关系，因为，我和中国有个约会。|nhưng tôi biết công việc của tôi nhất định sẽ liên quan đến Trung Quốc, bởi vì tôi có một cuộc hẹn với Trung Quốc.
"""), q=Q("""
马丁和中国的缘分是从什么时候开始的？|从六岁开始的。|Từ năm sáu tuổi.
马丁为什么喜欢中国功夫？|因为那时正在流行成龙的电影。|Vì hồi đó phim Thành Long đang thịnh hành.
马丁的中国老师都教了他什么？|不但教他中国功夫，而且还教他很多做人的道理。|Dạy võ thuật và nhiều đạo lý làm người.
为什么有人反对马丁学汉语？|他们觉得学汉语既不能挣大钱，也没什么出息。|Họ cho rằng học tiếng Hán không kiếm được nhiều tiền, chẳng có tiền đồ.
马丁经常和中国朋友一起做什么？|吃中国菜，喝中国茶，谈中国文化，去中国旅行。|Ăn món Trung, uống trà, nói chuyện văn hóa, đi du lịch.
马丁的生活里有哪些中国元素？|墙上挂着中国画，书架上放着中文书，身上穿着唐装。|Tranh Trung Quốc, sách tiếng Trung, áo Đường trang.
马丁的汉语进步快吗？为什么？|很快，因为他能经常和中国人用汉语聊天儿。|Rất nhanh, vì thường nói chuyện bằng tiếng Hán với người Trung Quốc.
为什么马丁得认真想想工作的事了？|因为他快毕业了。|Vì anh sắp tốt nghiệp.
马丁想做什么工作？为什么？|当厨师或者导游。当厨师可以每天吃好吃的中国菜，当导游可以每天说汉语、交朋友。|Đầu bếp hoặc hướng dẫn viên.
马丁为什么知道自己的工作一定和中国有关系？|因为他和中国有个约会。|Vì anh có một cuộc hẹn với Trung Quốc.
"""))],
grammar=[
 G("shi_de", "我叫马丁，是从德国来的。", "(是)……的: nhấn mạnh thời gian / nơi chốn / cách thức / mục đích",
   "Dùng cho việc ĐÃ xảy ra, nhấn mạnh thời gian, địa điểm, phương thức, mục đích… 是 có thể lược bỏ; phủ định dùng 不是……的. Tân ngữ có thể đặt sau 的.",
   [F("S:Chủ ngữ|kw:是|T:Thời gian/Nơi/Cách thức|V:Động từ (+O)|kw2:的", [
      ("我们|[(是)]|昨天|到北京|[的]", "。", "Chúng tôi đến Bắc Kinh hôm qua. (nhấn mạnh thời gian)"),
      ("我|[不是]|从美国|来|[的]", "。", "Tôi không phải từ Mỹ đến. (nơi chốn)"),
      ("你|[(是)]|坐飞机|去旅行|[的]", "吗？", "Bạn đi du lịch bằng máy bay à? (cách thức)"),
      ("你|[(是)]|怎么|来|[的]", "？", "Bạn đến bằng cách nào?"),
      ("我们|[(是)]||来中国学习汉语|[的]", "。", "Chúng tôi đến Trung Quốc để học tiếng Hán. (mục đích)")]),
    F("S:Chủ ngữ|kw:是|T:Thời gian/Nơi|V:Động từ|kw2:的|O:Tân ngữ", [
      ("我们|[是]|昨天|到|[的]|北京", "。", "Chúng tôi đến Bắc Kinh hôm qua."),
      ("你|[是]|在学校的书店|买|[的]|这本书", "吗？", "Bạn mua quyển sách này ở hiệu sách của trường à?")], cap="Tân ngữ đặt sau 的")],
   prac=["A:这本词典不错，{是在哪儿买的}？\nB:{是在图书城买的}。", "A:听说你们昨天去长城了？{你们是怎么去的}？\nB:{我们是坐火车去的}。", "A:听说你父母来了？{他们是什么时候来的}？\nB:{是上星期来的}。"]),
 G("budan_erqie", "他不但教我中国功夫，而且还教我很多做人的道理。", "不但……而且/还/也……: không những… mà còn…",
   "Quan hệ tăng tiến. Hai vế cùng chủ ngữ: 不但 đứng SAU chủ ngữ; khác chủ ngữ: 不但 đứng TRƯỚC chủ ngữ thứ nhất.",
   [F("S:Chủ ngữ|kw:不但|A:Vế 1|kw2:而且/还/也|B:Vế 2", [
      ("那家超市的水果|[不但]|新鲜，|[而且]|便宜", "。", "Trái cây siêu thị đó không những tươi mà còn rẻ."),
      ("小王|[不但]|会说英语，|[还]|会说韩国语", "。", "Tiểu Vương không chỉ biết tiếng Anh mà còn biết tiếng Hàn."),
      ("玛丽|[不但]|会唱歌，|[还]|会跳舞", "。", "Mary không chỉ biết hát mà còn biết nhảy.")], cap="Cùng chủ ngữ"),
    F("kw:不但|A:Chủ ngữ 1 + vị ngữ|S:Chủ ngữ 2|kw2:也|B:Vị ngữ", [
      ("[不但]|玛丽会唱歌，|安娜|[也]|会唱歌", "。", "Không chỉ Mary biết hát, Anna cũng biết hát.")], cap="Khác chủ ngữ")],
   prac=["A:你喜欢你的工作吗？\nB:我很喜欢我的工作，{不但有意思，而且能说汉语}。", "A:你的同屋会说英语吗？\nB:{他不但会说英语，而且说得很好}。"]),
 G("qishi", "其实，到现在我还没想好以后做什么工作呢。", "其实: thật ra",
   "Chỉ tình hình thực tế, thường mang ý chuyển ngoặt so với điều nói trước.",
   [F("C:Vế trước|kw:其实|B:Sự thật", [
      ("我|[其实]|很不高兴，只是没说", "。", "Thật ra tôi rất không vui, chỉ là không nói ra."),
      ("有人说北京的夏天很热，|[其实]|不太热", "。", "Có người nói mùa hè Bắc Kinh rất nóng, thật ra không nóng lắm."),
      ("|[其实]|考试不太难，你不用担心", "。", "Thật ra bài thi không khó lắm, bạn không cần lo.")])],
   notes=["因此: vì vậy – dùng giữa vế nguyên nhân và vế kết quả, KHÔNG dùng cùng 因为. 今年冬天很冷，因此感冒的人很多。"],
   prac=["A:听说四川菜非常辣，我不想吃。\nB:{其实不是所有的四川菜都辣}，你不用怕。", "A:小王说那个电影很有意思，你觉得怎么样？\nB:{其实没什么意思}，看完有点儿后悔。"]),
],
ex=[
 pool("一、选词填空（旅）", "Chữ “旅” tạo từ 旅客/旅店/旅途/旅游/旅馆… Chọn từ điền vào chỗ trống.", ["旅客", "旅店", "旅途", "旅游", "旅馆"], [
   "“【旅游】”和“旅行”的意思差不多。", "火车站【旅客】很多。", "祝你【旅途】愉快！", "我们旅行时都是住在小【旅店】或者小【旅馆】里，条件还可以。"]),
 match("二、连线", "Nối từ có chữ “旅” với lời giải thích.", ["旅行的路程", "旅行用的路费", "一起去旅行的人", "出门旅行的人"],
   [("旅费", "旅行用的路费"), ("旅程", "旅行的路程"), ("旅客", "出门旅行的人"), ("旅伴", "一起去旅行的人")]),
 pool("三、选择课文中学过的词语填空", "Chọn từ đã học trong bài điền vào chỗ trống.", ["约会", "流行", "选择", "后悔", "交", "到处", "假期", "认真", "适应"], [
   "这首歌现在很【流行】，大家都在唱。", "我今天下午有个【约会】，不能来参加你们的活动。", "我真【后悔】小时候没好好儿学习英语。", "两个都很好，我不知道【选择】哪一个。",
   "这个【假期】，你想去哪儿旅行？", "我刚来北京，还不太【适应】这里的生活。", "听说你【交】了一个中国朋友。", "一到晚上，院子里【到处】都是车。", "他是个【认真】的人，做什么事都很努力。"]),
 pick("四、选择意思相近的词语填空", "Chọn từ thích hợp (từ gần nghĩa).", [
   (["因为", "因此"], ["【因为】这种卡很方便，所以我也想办一张。", "路上的车太多了，【因此】经常堵车。"]),
   (["其实", "真的"], ["这本书看起来挺厚的，【其实】不太难。", "朋友说得没错，这里的天气【真的】很热。"]),
   (["交", "做"], ["他喜欢【交】朋友。", "我很想【做】你的朋友。"]),
   (["的", "了"], ["你来得真早，几点到【的】？", "我昨天上午给你打电话【了】，你不在家。"])]),
 opn("五、根据提示完成对话", "Hoàn thành hội thoại theo gợi ý.", [
   ("A：你是一个人去云南旅行的吗？\nB：不是，______。（是……的）", "不是，我是和朋友一起去的。"),
   ("A：马克是坐飞机来的吗？\nB：不是坐飞机来的，______。（是……的）", "不是坐飞机来的，是坐火车来的。"),
   ("A：坐飞机贵，坐船便宜吧？\nB：______。（其实）", "其实坐船也不便宜。"),
   ("A：你一定喜欢踢足球，因为你喜欢看足球。\nB：______，虽然我喜欢看足球。（其实）", "其实我不喜欢踢足球，虽然我喜欢看足球。"),
   ("A：都有谁参加明天的晚会？你参加吗？\nB：______，而且我的朋友都参加。（不但）", "不但我参加，而且我的朋友都参加。")]),
 opn("六、情境表达", "Câu nào dùng trong tình huống nào; tình huống sau nên nói thế nào?", [
   ("“其实我不是那个意思，你听错了。”“我是和朋友一起来的。”“我们交个朋友吧。”——在什么情况下可以说？", "别人误会了你的话的时候；别人问你是不是一个人来的时候；认识了一个新朋友，想和他做朋友的时候。"),
   ("你的朋友学汉语的时间才半年，可是说得很好。你怎么介绍他？（其实　是……的）", "他汉语说得很好，其实他是半年前才开始学汉语的。"),
   ("你在上海遇见你的朋友，你想知道他到上海的时间，你怎么问？（是……的）", "你是什么时候到上海的？")]),
 opn("七、根据课文内容完成句子", "Hoàn thành câu theo nội dung bài khóa.", [
   ("我和中国的缘分是从六岁______。", "开始的"),
   ("我有一个中国老师，他不但______，而且还______。", "教我中国功夫 / 教我很多做人的道理"),
   ("但我还是______了汉语，而且一点儿也不______。我______了很多中国朋友，我们一起______中国菜，______中国茶，______中国文化，去中国______。", "选择 / 后悔 / 交 / 吃 / 喝 / 谈 / 旅行"),
   ("一年前我来到中国留学，学费是我打工______的。", "挣"),
   ("在中国，能经常和中国人用汉语______，因此我的汉语______得很快，说得越来越好了。", "聊天儿 / 进步")]),
 opn("八、根据课文内容完成对话", "Hoàn thành hội thoại theo nội dung bài khóa.", [
   ("A：你为什么选择学习汉语？\nB：那是因为有两个人对我的影响很大。一个是______，还有一个是______。", "成龙 / 我的中国功夫老师"),
   ("A：有人不同意你学汉语吗？\nB：有啊。有人说学汉语既不______，也没______。", "能挣大钱 / 什么出息"),
   ("A：你学汉语后悔了吗？\nB：我______后悔。现在不但我______，______也喜欢中国。", "一点儿也不 / 喜欢中国 / 我的家人和朋友"),
   ("A：你将来想做什么工作？\nB：我想当中国饭馆的厨师，因为______。或者给中国人当导游也不错，不但可以______，还可以______。", "这样我就可以每天吃好吃的宫保鸡丁、麻婆豆腐了 / 每天说汉语 / 交很多中国朋友"),
   ("A：那你的工作决定了吗？\nB：还没想好，不过我知道______，因为______。", "我的工作一定和中国有关系 / 我和中国有个约会")]),
 tf("九、阅读理解 · 判断正误", "Đọc đoạn văn rồi phán đoán đúng (对) / sai (错).", [
   ("那个人一看到别人的东西就想偷。", False), ("那个门铃只是声音好听。", False), ("他担心自己听到门铃声。", False), ("他想，堵住了耳朵，别人就听不见了。", True), ("门铃的主人听见了门铃声。", True)],
   passage="从前有一个人，一看到别人的好东西就想偷。有一天，他看见一家大门上挂着一个漂亮的门铃（ménlíng）。这个门铃不但好看，而且声音也很好听，他就想把门铃偷来。不过他知道，要是手碰到了门铃，它就会响起来。门铃一响，别人就会听到声音。这可怎么办呢？\n“对了，其实，想听不见门铃声也不难，堵（dǔ）住自己的耳朵就行了。”他想。\n晚上，他来到那家门前，堵住了自己的耳朵，放心地去摘那只门铃。可是，他刚碰到那个门铃，门铃就“丁零”地响了。那家人听到了铃声，急忙跑了出来，看到那人正偷门铃呢，就抓住了他。\n偷门铃的人不明白，自己是堵着耳朵偷的，别人是怎么听见门铃声的呢？"),
 opn("九、阅读理解 · 回答问题", "Trả lời câu hỏi theo đoạn văn ở trên.", [
   ("这个故事想告诉我们什么道理？", "自己骗自己是没有用的。"),
   ("关于这个故事，中国有一个成语，你知道是什么吗？", "掩耳盗铃（yǎn ěr dào líng）。")]),
 opn("十、说一说，写一写", "Viết đoạn văn ít nhất 60 chữ.", [
   ("你是从什么时候开始学习汉语的？你和汉语的缘分是怎么开始的？谁对你的影响最大？你将来想做什么工作？",
    "（参考）我是两年前开始学习汉语的。我和汉语的缘分是从一部中国电影开始的。对我影响最大的是我的汉语老师，她不但教我汉语，而且还教我很多中国文化。我交了很多中国朋友。将来我想当导游，因为我喜欢旅行，也喜欢说汉语。")]),
])
