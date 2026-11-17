# -*- coding: utf-8 -*-
# HSK 3 – Bài 15: 我是半个南京人
from gtb_gen import V, T, Q, F, G
B = {}

B[15] = dict(zh="我是半个南京人", vi="Tôi là nửa người Nam Kinh",
intro="Dương Đồng Lạc muốn mua nhà ở khu Lam Thiên và giới thiệu Nam Kinh – nơi anh học đại học. Vương Nhất Tuyết kể cho con trai về sông Hoàng Hà và về dòng sông gắn với tuổi thơ của mình.",
vocab=V("""
蓝|lán|tt|màu xanh lam, xanh dương|今天的天特别蓝。~Bầu trời hôm nay xanh đặc biệt.
段|duàn|lg|đoạn, quãng (thời gian, không gian)|这段时间我很忙。~Khoảng thời gian này tôi rất bận.
附近|fùjìn|dt|gần đó, lân cận|学校附近有一家书店。~Gần trường có một hiệu sách.
马路|mǎlù|dt|đường chính, đường cái|过马路要小心。~Qua đường phải cẩn thận.
平时|píngshí|dt|thường ngày|我平时七点起床。~Ngày thường tôi bảy giờ dậy.
放学|fàngxué|dong|tan học|孩子四点放学。~Bọn trẻ bốn giờ tan học.
游戏|yóuxì|dt|trò chơi|孩子们在花园里做游戏。~Bọn trẻ chơi trò chơi trong vườn.
老人|lǎorén|dt|người già|公园里有很多老人在锻炼。~Trong công viên có nhiều người già đang tập thể dục.
根据|gēnjù|gioi|căn cứ vào, dựa vào|老师根据学生的水平选书。~Thầy chọn sách dựa vào trình độ học sinh.
了解|liǎojiě|dong|hiểu, hiểu rõ, tìm hiểu|我不太了解这个城市。~Tôi không hiểu rõ thành phố này lắm.
可是|kěshì|lien|nhưng, tuy nhiên|我想去，可是没有时间。~Tôi muốn đi nhưng không có thời gian.
以上|yǐshàng|dt|trở lên, trên|这本书有三百页以上。~Cuốn sách này dày hơn ba trăm trang.
有名|yǒumíng|tt|nổi tiếng, có tiếng|这家饭馆很有名。~Quán ăn này rất nổi tiếng.
景点|jǐngdiǎn|dt|cảnh điểm, điểm du lịch|北京有很多有名的景点。~Bắc Kinh có nhiều điểm du lịch nổi tiếng.
游客|yóukè|dt|du khách|夏天来这里的游客很多。~Mùa hè có rất nhiều du khách đến đây.
外地|wàidì|dt|nơi khác, vùng khác|他是从外地来的。~Anh ấy từ nơi khác đến.
聊|liáo|dong|trò chuyện, nói chuyện|我们边喝咖啡边聊。~Chúng ta vừa uống cà phê vừa trò chuyện.
河|hé|dt|sông|这条河很长。~Con sông này rất dài.
关系|guānxì|dt|quan hệ|我们的关系很好。~Quan hệ của chúng tôi rất tốt.
养|yǎng|dong|nuôi, nuôi dưỡng|我家养了一只猫。~Nhà tôi nuôi một con mèo.
西北|xīběi|dt|tây bắc|他家在城市的西北边。~Nhà anh ấy ở phía tây bắc thành phố.
经过|jīngguò|dong|đi qua, trải qua, trải nghiệm|去学校要经过一个公园。~Đi đến trường phải qua một công viên.
草地|cǎodì|dt|thảm cỏ, đồng cỏ|孩子们在草地上玩儿。~Bọn trẻ chơi trên bãi cỏ.
遇见|yùjiàn|dong|gặp, tình cờ gặp|我在超市遇见了老师。~Tôi tình cờ gặp thầy ở siêu thị.
南京|Nánjīng|rieng|Nam Kinh (thủ phủ tỉnh Giang Tô)|南京有很长的历史。~Nam Kinh có lịch sử lâu đời.
黄河|Huáng Hé|rieng|sông Hoàng Hà|黄河是中国第二长的河。~Hoàng Hà là con sông dài thứ hai Trung Quốc.
"""),
texts=[dict(t="课文1", scene="在办公室里，王一雪和杨同乐在聊天儿。", scene_vi="Vương Nhất Tuyết và Dương Đồng Lạc đang trò chuyện trong văn phòng.", narr=False, lines=T("""
杨同乐>您搬到蓝天小区一段时间了，觉得怎么样？|Chị chuyển đến khu Lam Thiên được một thời gian rồi, thấy thế nào?
王一雪>小区环境挺好的，附近买东西也很方便，过马路就是超市。|Môi trường khu khá tốt, mua đồ gần đó cũng tiện, qua đường là siêu thị.
杨同乐>平时孩子们在哪儿玩？|Ngày thường bọn trẻ chơi ở đâu?
王一雪>小区里有很多树，孩子们放学后就在树下做游戏。你想买房子吗？|Trong khu có nhiều cây, bọn trẻ tan học là chơi trò chơi dưới gốc cây. Cậu muốn mua nhà à?
杨同乐>是。我想买一个大房子，让我爸妈过来跟我一起住。|Vâng. Em muốn mua một căn nhà rộng, để bố mẹ em sang ở cùng.
王一雪>蓝天小区的老人挺多的，这几年小区根据他们的需要，有了很多变化。|Khu Lam Thiên có khá nhiều người già, mấy năm nay khu đã thay đổi nhiều theo nhu cầu của họ.
杨同乐>真不错！过几天我去蓝天小区看看。|Tốt quá! Vài hôm nữa em đến khu Lam Thiên xem thử.
"""), q=Q("""
蓝天小区附近买东西方便吗？|很方便，过马路就是超市。|Rất tiện, qua đường là siêu thị.
蓝天小区的孩子们放学后都在哪里玩？|在树下做游戏。|Chơi trò chơi dưới gốc cây.
蓝天小区为老人做什么了？|根据他们的需要，有了很多变化。|Thay đổi nhiều theo nhu cầu của họ.
""")),
 dict(t="课文2", scene="在办公室里，王一雪和杨同乐在聊天儿。", scene_vi="Vương Nhất Tuyết và Dương Đồng Lạc đang trò chuyện trong văn phòng.", narr=False, lines=T("""
王一雪>假期我想去南京旅游，但是我不太了解那里。|Kỳ nghỉ chị muốn đi Nam Kinh du lịch, nhưng chị không hiểu rõ nơi đó lắm.
杨同乐>我虽然不是南京人，可是我是在南京上的大学，可以说是半个南京人。|Em tuy không phải người Nam Kinh, nhưng em học đại học ở Nam Kinh, có thể nói là nửa người Nam Kinh.
王一雪>太好了！你快给我介绍一下南京吧。|Tuyệt quá! Cậu mau giới thiệu Nam Kinh cho chị đi.
杨同乐>南京有两千年以上的历史，有老城、老街，还有很多有名的景点，每年去旅游的游客特别多。|Nam Kinh có lịch sử hơn hai nghìn năm, có thành cổ, phố cổ, còn có nhiều điểm du lịch nổi tiếng, năm nào du khách cũng rất đông.
王一雪>除了这些以外，你再告诉我一些外地人不知道的地方。|Ngoài những nơi này, cậu nói thêm cho chị vài chỗ người nơi khác không biết.
杨同乐>那太多了，我得一点儿一点儿给您讲。|Thế thì nhiều lắm, em phải kể dần dần cho chị.
王一雪>行，下班后我请你吃晚饭，咱们边吃边聊。|Được, tan làm chị mời cậu ăn tối, chúng ta vừa ăn vừa nói chuyện.
"""), q=Q("""
王一雪了解南京吗？|不太了解。|Không hiểu rõ lắm.
杨同乐为什么了解南京？|因为他是在南京上的大学。|Vì anh ấy học đại học ở Nam Kinh.
王一雪为什么请杨同乐吃晚饭？|想边吃边聊，让他给她讲南京。|Muốn vừa ăn vừa nghe anh ấy kể về Nam Kinh.
""")),
 dict(t="课文3", scene="在家里，王一雪和刘小明在聊天儿。", scene_vi="Vương Nhất Tuyết và Lưu Tiểu Minh đang trò chuyện ở trong nhà.", narr=False, lines=T("""
王一雪>小明，中国有一条大河，它的名字跟颜色有关系，你知道是什么河吗？|Tiểu Minh, Trung Quốc có một con sông lớn, tên của nó liên quan đến màu sắc, con biết là sông gì không?
刘小明>我知道，是黄河！|Con biết, là sông Hoàng Hà!
王一雪>你说对了。我再问问你，你知道它为什么叫黄河吗？|Con nói đúng rồi. Mẹ hỏi tiếp nhé, con biết vì sao nó tên là Hoàng Hà không?
刘小明>因为河水看起来是黄色的，所以叫这个名字。黄河是中国最长的河吗？|Vì nước sông trông màu vàng nên mới có tên này. Hoàng Hà là sông dài nhất Trung Quốc ạ?
王一雪>不是。黄河虽然不是最长的河，可是在历史上很重要。|Không phải. Hoàng Hà tuy không phải sông dài nhất, nhưng rất quan trọng trong lịch sử.
刘小明>这个我知道。很久以前，很多中国人都住在黄河边上。|Cái này con biết. Rất lâu về trước, nhiều người Trung Quốc sống ven sông Hoàng Hà.
王一雪>对。在我们中国人看来，黄河像妈妈一样，养了我们几千年。|Đúng vậy. Với người Trung Quốc chúng ta, Hoàng Hà giống như người mẹ, đã nuôi dưỡng chúng ta mấy nghìn năm.
"""), q=Q("""
黄河的名字为什么跟“黄”这个颜色有关系？|因为河水看起来是黄色的。|Vì nước sông trông màu vàng.
黄河是中国最长的河吗？|不是，可是在历史上很重要。|Không, nhưng rất quan trọng trong lịch sử.
在中国人看来，黄河像什么一样？为什么？|像妈妈一样，因为它养了中国人几千年。|Như người mẹ, vì đã nuôi dưỡng người Trung Quốc mấy nghìn năm.
""")),
 dict(t="课文4", scene="在家里，王一雪在写日记。", scene_vi="Vương Nhất Tuyết đang viết nhật ký ở trong nhà.", narr=True, lines=T("""
我小时候住在北京的西北边，有一条非常有名的河经过那里。|Hồi nhỏ tôi sống ở phía tây bắc Bắc Kinh, có một con sông rất nổi tiếng chảy qua đó.
我家就住在河边。那里有高高的大树和绿绿的草地。|Nhà tôi ở ngay bên sông. Ở đó có những cây to cao vút và bãi cỏ xanh mướt.
春天，河边的花都开了，看起来特别漂亮。|Mùa xuân, hoa ven sông nở rộ, trông vô cùng đẹp.
还记得小时候，一到夏天我就去河里游泳。|Vẫn còn nhớ hồi nhỏ, cứ đến hè là tôi xuống sông bơi.
长大以后，遇到什么不开心的事情，我就去河边的树下坐着，|Lớn lên rồi, gặp chuyện gì không vui, tôi lại ra ngồi dưới gốc cây ven sông,
听听鸟叫，看看河水，跟遇见的朋友聊聊天儿，难过的事情不一会儿就忘了。|nghe chim hót, ngắm dòng nước, trò chuyện với người bạn tình cờ gặp, chuyện buồn chẳng mấy chốc đã quên.
那是我最喜欢的地方。|Đó là nơi tôi yêu thích nhất.
"""), q=Q("""
王一雪小时候住的地方环境怎么样？|有高高的大树和绿绿的草地，春天河边的花都开了。|Có cây cao, cỏ xanh, mùa xuân hoa ven sông nở rộ.
小时候，王一雪一到夏天就做什么？|去河里游泳。|Xuống sông bơi.
长大以后，王一雪会去河边做什么？|坐在树下，听鸟叫，看河水，跟朋友聊天儿。|Ngồi dưới gốc cây, nghe chim hót, ngắm sông, trò chuyện với bạn.
"""))],
grammar=[
 G("genju", "介词“根据”", "Giới từ “根据”",
   "Giới từ “根据” dùng để dẫn ra căn cứ hoặc lý do của một hành động trong câu (căn cứ vào, dựa vào).",
   [F("S:(Chủ ngữ)|kw:根据|O:Căn cứ|V:Hành động", [
     ("这几年小区|[根据]|他们的需要，|有了很多变化", "。", "Mấy năm nay khu đã thay đổi nhiều theo nhu cầu của họ."),
     ("|[根据]|要求，|我们必须参加明天的会议", "。", "Theo yêu cầu, chúng ta phải tham dự cuộc họp ngày mai."),
     ("老师|[根据]|每个学生的兴趣，|选择了不一样的书", "。", "Thầy chọn những cuốn sách khác nhau dựa trên sở thích của từng học sinh.")])]),
 G("shuliangcd", "数量重叠“数词+量词+数词+量词”", "Cụm số lượng lặp lại “số từ + lượng từ + số từ + lượng từ”",
   "Cụm từ chỉ số lượng có thể lặp lại, làm trạng ngữ, thường chỉ phương thức của hành động (từng… từng…, dần dần), có tác dụng hình tượng hóa. Cấu trúc: số từ + lượng từ + số từ + lượng từ + (地) + động từ.",
   [F("S:Chủ ngữ|kw:Số lượng lặp lại (+地)|V:Động từ", [
     ("我得|[一点儿一点儿]|给您讲", "。", "Tôi phải kể dần dần cho chị."),
     ("学生们的汉语水平|[一天一天地]|提高了", "。", "Trình độ tiếng Hán của học sinh nâng cao từng ngày."),
     ("他们|[两个两个地]|走进去了", "。", "Họ đi vào từng đôi một."),
     ("你看课文的时候|[一段一段地]|看", "。", "Lúc đọc bài khóa bạn hãy đọc từng đoạn một.")])]),
 G("zaikanlai", "固定短语“在……看来”", "Cấu trúc cố định “在……看来”",
   "Cấu trúc cố định “在……看来” dùng để biểu thị quan điểm của cá nhân hoặc tập thể (theo… thì, đối với…).",
   [F("kw:在|S:Cá nhân / tập thể|kw2:看来，|C:Quan điểm", [
     ("[在]|我们中国人|[看来，]|黄河像妈妈一样，养了我们几千年", "。", "Với người Trung Quốc chúng ta, Hoàng Hà như người mẹ, nuôi dưỡng chúng ta mấy nghìn năm."),
     ("[在]|同事们|[看来，]|她工作非常认真", "。", "Theo các đồng nghiệp, cô ấy làm việc rất nghiêm túc."),
     ("[在]|我|[看来，]|每天读书是一种很好的习惯", "。", "Theo tôi, đọc sách mỗi ngày là một thói quen rất tốt.")])]),
 G("buyihuir", "固定短语“不一会儿”", "Cụm từ cố định “不一会儿”",
   "Cụm từ cố định “不一会儿” thường dùng trong văn nói, làm trạng ngữ, biểu thị thời gian rất ngắn (chẳng mấy chốc, một lát sau).",
   [F("S:(Chủ ngữ)|kw:不一会儿|V:(就) + hành động", [
     ("难过的事情|[不一会儿]|就忘了", "。", "Chuyện buồn chẳng mấy chốc đã quên."),
     ("|[不一会儿]|，张校长就来了", "。", "Một lát sau, thầy hiệu trưởng Trương đã đến."),
     ("两个小时看起来长，但是|[不一会儿]|就过去了", "。", "Hai tiếng trông có vẻ dài, nhưng chẳng mấy chốc đã trôi qua.")])]),
],
test=dict(
 l2=["鱼|鸡肉|鸡蛋面", "是南方人|来这儿很久了|在南方上的大学", "生病了|有点儿累|睡觉睡多了"],
 l3=["花茶|绿茶|红茶", "有高高的山|有蓝色的鱼|有很多游客", "很快乐|对学习好|对身体好", "看电视|在外面玩|玩电脑游戏"],
 r1=(["对，我去过中国十个以上的城市。", "我不太了解他，只跟他见过几次。", "我知道有一位老人很了解那里。", "不是的，昨晚看足球比赛，睡得太晚了。", "当然。我们先坐公交车，然后换地铁。", "我明天要去南京旅游，把它放到朋友家了。"],
     ["你和小王的关系怎么样？", "你平时也是十点多才起床吗？", "听说你对中国文化特别感兴趣？", "我记得你养了一条狗，怎么不见了？", "我想找个人给我讲讲那个城市的历史。"]),
 r2=(["了解", "游客", "根据", "遇见", "鞋", "附近"],
     ["大家可以（　　）自己的需要选择要买的东西。", "这些（　　）不一会儿就把要送人的礼物买好了。", "我家（　　）有个公园，我经常去公园的草地上看书。", "A：你（　　）黄河的历史吗？\nB：当然，我们上课的时候学过。", "A：你今天怎么回来这么晚？\nB：我在路上（　　）了一个老朋友，跟他聊了好久。"]),
 r3=[("你看课文的时候别着急，一段一段地看，一个词一个词地看，一定能看懂的。", "看课文的时候应该怎么做？", "慢慢看|越看越快|边写边看"),
     ("他爸爸是音乐学校的校长，妈妈是有名的音乐老师，可是他对音乐没什么兴趣。他想以后做个医生，帮助那些生病的人。", "他以后想做什么工作？", "校长|医生|音乐老师"),
     ("我每天都刷牙，而且每次都刷三分钟以上，可是没想到还是牙疼。可能是因为最近一段时间，我吃了太多甜的东西。以后我应该少吃点儿甜的，有时间还要再去医院检查一下。",
      ("他为什么会牙疼？", "不是每天刷牙|吃了太多甜的|刷牙时间太短了"), ("他要做什么？", "多刷牙|少吃东西|去医院检查"))],
 w1=["这（duàn）时间，我一直住在朋友家里。", "中国银行在（mǎ）路的北边还是南边？", "我家门前有一条小（hé），我常去游泳。"],
 w2=[("聊", "两个朋友坐在一起，一边吃东西一边聊。"), ("经过", "她们买完东西，经过一家商店。"), ("放学", "放学以后，爸爸妈妈一起去接孩子。")],
 gl={"11": "Quan hệ giữa bạn và Tiểu Vương thế nào? → B: Mình không hiểu rõ anh ấy lắm, chỉ gặp vài lần.",
     "12": "Ngày thường bạn cũng hơn mười giờ mới dậy à? → D: Không phải, tối qua xem bóng đá, ngủ muộn quá.",
     "13": "Nghe nói bạn đặc biệt thích văn hóa Trung Quốc? → A: Đúng, mình đã đến hơn mười thành phố Trung Quốc.",
     "14": "Mình nhớ bạn nuôi một con chó, sao không thấy đâu? → F: Mai mình đi Nam Kinh du lịch, gửi nó ở nhà bạn rồi.",
     "15": "Mình muốn tìm người kể cho mình nghe lịch sử của thành phố đó. → C: Mình biết có một cụ già rất hiểu nơi đó.",
     "16": "根据自己的需要 – dựa vào nhu cầu của mình. → C 根据.",
     "17": "这些游客 – những du khách này. → B 游客.",
     "18": "我家附近 – gần nhà tôi. → F 附近.",
     "19": "了解黄河的历史 – hiểu lịch sử Hoàng Hà. → A 了解.",
     "20": "遇见了一个老朋友 – tình cờ gặp một người bạn cũ. → D 遇见.",
     "21": "“一段一段地看，一个词一个词地看” → A 慢慢看.",
     "22": "“他想以后做个医生” → B.",
     "23": "“我吃了太多甜的东西” → B.",
     "24": "“有时间还要再去医院检查一下” → C."}),
)
