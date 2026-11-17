# -*- coding: utf-8 -*-
# HSK 3 – Bài 12: 这个季节天气变化很快
from gtb_gen import V, T, Q, F, G
B = {}

B[12] = dict(zh="这个季节天气变化很快", vi="Thời tiết mùa này thay đổi rất nhanh",
intro="Hoa nở khắp phố, Bạch Gia Nguyệt và cô Vương Nhất Phi định đi công viên chèo thuyền, thì trời bỗng nổi gió, đổ mưa. Hai người trò chuyện về thời tiết và bốn mùa ở Bắc Kinh.",
vocab=V("""
街|jiē|dt|phố, đường phố|这条街上有很多饭馆。~Trên con phố này có rất nhiều quán ăn.
开花|kāihuā|dong|nở hoa, trổ hoa|春天到了，花都开花了。~Mùa xuân đến rồi, hoa đều nở cả.
公园|gōngyuán|dt|công viên|我常去公园跑步。~Tôi hay ra công viên chạy bộ.
船|chuán|dt|thuyền|我们去湖上坐船吧。~Chúng ta lên hồ ngồi thuyền đi.
工作日|gōngzuòrì|dt|ngày làm việc|工作日地铁上人很多。~Ngày làm việc trên tàu điện ngầm rất đông người.
地方|dìfang|dt|địa điểm, nơi|这是一个很漂亮的地方。~Đây là một nơi rất đẹp.
刚才|gāngcái|dt|vừa rồi, lúc nãy|刚才谁给我打电话了？~Lúc nãy ai gọi điện cho tôi vậy?
刮|guā|dong|(gió) thổi|外面刮大风了。~Bên ngoài nổi gió to rồi.
风|fēng|dt|gió|今天的风很大。~Hôm nay gió rất to.
新闻|xīnwén|dt|tin tức|爸爸每天晚上看新闻。~Bố tối nào cũng xem thời sự.
伞|sǎn|dt|ô, dù|下雨了，别忘了带伞。~Trời mưa rồi, đừng quên mang ô.
借|jiè|dong|mượn|我可以借你的书看看吗？~Mình mượn sách của bạn xem được không?
把|bǎ|lg|cái, chiếc (vật có tay cầm)|我买了一把新雨伞。~Tôi mua một chiếc ô mới.
雨衣|yǔyī|dt|áo mưa|骑车的时候要穿雨衣。~Lúc đạp xe phải mặc áo mưa.
变|biàn|dong|thay đổi|他变得越来越瘦了。~Anh ấy ngày càng gầy đi.
季节|jìjié|dt|mùa|你最喜欢哪个季节？~Bạn thích mùa nào nhất?
变化|biànhuà|dt|thay đổi, sự thay đổi|这几年北京的变化很大。~Mấy năm nay Bắc Kinh thay đổi rất nhiều.
冬天|dōngtiān|dt|mùa đông|北方的冬天很冷。~Mùa đông ở miền Bắc rất lạnh.
常常|chángcháng|pho|thường xuyên|我常常和朋友一起打球。~Tôi thường chơi bóng với bạn bè.
关注|guānzhù|dong|quan tâm|我很关注天气的变化。~Tôi rất quan tâm đến sự thay đổi thời tiết.
四季|sìjì|dt|bốn mùa|这里四季都很漂亮。~Ở đây bốn mùa đều đẹp.
春天|chūntiān|dt|mùa xuân|春天的花特别多。~Mùa xuân hoa đặc biệt nhiều.
夏天|xiàtiān|dt|mùa hè|夏天我喜欢去海边。~Mùa hè tôi thích ra biển.
凉快|liángkuai|tt|mát mẻ|今天比昨天凉快。~Hôm nay mát hơn hôm qua.
秋天|qiūtiān|dt|mùa thu|北京的秋天最舒服。~Mùa thu Bắc Kinh dễ chịu nhất.
叶子|yèzi|dt|lá|秋天的叶子变黄了。~Lá mùa thu chuyển vàng rồi.
变成|biànchéng|dong|trở thành, biến thành|水变成了冰。~Nước biến thành băng.
"""),
texts=[dict(t="课文1", scene="在街上，王一飞和白家月边走边聊。", scene_vi="Vương Nhất Phi và Bạch Gia Nguyệt vừa đi vừa trò chuyện trên đường phố.", narr=False, lines=T("""
白家月>王老师，您看，这条街上的树都开花了。|Cô Vương, cô xem, cây trên con phố này đều nở hoa rồi.
王一飞>上周我去公园坐船了，公园里的花也开了。|Tuần trước cô đi công viên ngồi thuyền, hoa trong công viên cũng nở rồi.
白家月>天气这么好，下午我也想去公园坐船。|Trời đẹp thế này, chiều nay em cũng muốn đi công viên ngồi thuyền.
王一飞>去吧！今天是工作日，人应该不多。|Đi đi! Hôm nay là ngày làm việc, chắc không đông người.
白家月>您有时间吗？我想跟您一起去。|Cô có thời gian không? Em muốn đi cùng cô.
王一飞>我今天下午有课，不能去太远的地方。|Chiều nay cô có tiết dạy, không đi xa được.
白家月>那咱们换一天去？|Vậy chúng ta đổi ngày khác đi nhé?
王一飞>行。或者明天去，或者后天去，我给你打电话。|Được. Hoặc mai đi, hoặc ngày kia đi, cô sẽ gọi điện cho em.
"""), q=Q("""
上周王一飞去公园做什么了？|坐船了。|Ngồi thuyền.
白家月今天想做什么？|下午去公园坐船。|Chiều đi công viên ngồi thuyền.
她们可能什么时候去公园？|明天或者后天。|Ngày mai hoặc ngày kia.
""")),
 dict(t="课文2", scene="在街上，王一飞和白家月一起散步。", scene_vi="Vương Nhất Phi và Bạch Gia Nguyệt đang đi dạo cùng nhau trên đường phố.", narr=False, lines=T("""
白家月>刚才还是大晴天呢，怎么突然就刮起风来了？|Lúc nãy còn nắng to, sao đột nhiên lại nổi gió thế?
王一飞>好像新闻里说今天有雨。|Hình như tin tức nói hôm nay có mưa.
白家月>啊？我每天书包里都放着雨伞，就今天没带。|Hả? Ngày nào em cũng để ô trong cặp, riêng hôm nay không mang.
王一飞>我可以借给你，我车里有一把伞和一件雨衣。|Cô cho em mượn, trong xe cô có một chiếc ô và một cái áo mưa.
白家月>谢谢，希望下午天气能变好。|Cảm ơn cô, mong chiều nay trời đẹp trở lại.
王一飞>这个季节天气变化很快。|Mùa này thời tiết thay đổi rất nhanh.
白家月>雨已经下起来了，咱们快点儿走吧。|Mưa bắt đầu rơi rồi, chúng ta đi nhanh lên thôi.
"""), q=Q("""
白家月今天带雨伞了吗？|没带，她每天都带，就今天没带。|Không, ngày nào cũng mang, riêng hôm nay không.
王一飞可以借给白家月什么？|一把伞和一件雨衣。|Một chiếc ô và một áo mưa.
她们现在要做什么？为什么？|快点儿走，因为雨已经下起来了。|Đi nhanh lên, vì mưa đã bắt đầu rơi.
""")),
 dict(t="课文3", scene="在教室里，王一飞和白家月躲雨。", scene_vi="Vương Nhất Phi và Bạch Gia Nguyệt đang trú mưa trong lớp học.", narr=False, lines=T("""
白家月>您来这里已经一年多了，习惯了吧？|Cô đến đây hơn một năm rồi, quen rồi chứ ạ?
王一飞>别的早就习惯了，就是天气我还不太习惯。|Những thứ khác thì quen từ lâu rồi, chỉ có thời tiết là cô vẫn chưa quen lắm.
白家月>为什么？您不喜欢这里的天气吗？|Sao vậy ạ? Cô không thích thời tiết ở đây sao?
王一飞>我觉得冬天太冷了。|Cô thấy mùa đông lạnh quá.
白家月>冬天虽然冷，但是下雪的时候特别漂亮。|Mùa đông tuy lạnh, nhưng lúc tuyết rơi đẹp lắm.
王一飞>我也喜欢雪。北京常常下雪，但听说今年就下了一次。|Cô cũng thích tuyết. Bắc Kinh hay có tuyết, nhưng nghe nói năm nay chỉ rơi có một lần.
白家月>我没关注过北京的天气，但是新闻里说过，今年冬天很多地方雪下得都少了。|Em chưa để ý thời tiết Bắc Kinh, nhưng tin tức có nói, mùa đông năm nay nhiều nơi tuyết rơi ít đi.
"""), q=Q("""
王一飞对什么还不太习惯？|这里的天气。|Thời tiết ở đây.
白家月为什么喜欢冬天？|因为下雪的时候特别漂亮。|Vì lúc tuyết rơi rất đẹp.
新闻里说过什么？|今年冬天很多地方雪下得都少了。|Mùa đông năm nay nhiều nơi tuyết rơi ít đi.
""")),
 dict(t="课文4", scene="在家里，王一飞在写日记。", scene_vi="Vương Nhất Phi đang ngồi viết nhật ký ở trong nhà.", narr=True, lines=T("""
我离开北京到这里工作一年多了。|Tôi rời Bắc Kinh đến đây làm việc đã hơn một năm.
这一年多住下来，我还是更喜欢北京的四季。|Sống ở đây hơn một năm, tôi vẫn thích bốn mùa của Bắc Kinh hơn.
北京的春天最舒服，天气不冷不热。|Mùa xuân Bắc Kinh dễ chịu nhất, thời tiết không lạnh không nóng.
夏天白天很热，但是晚上比较凉快。|Mùa hè ban ngày rất nóng, nhưng buổi tối khá mát mẻ.
秋天树上的叶子都变成了红色、黄色，非常漂亮。|Mùa thu lá trên cây đều chuyển sang màu đỏ, màu vàng, vô cùng đẹp.
冬天不但冷，而且风很大，我最不喜欢冬天。|Mùa đông không những lạnh mà gió còn to, tôi ghét mùa đông nhất.
每个人都有自己最喜欢的季节，你最喜欢哪个季节呢？|Ai cũng có mùa mình thích nhất, bạn thích mùa nào nhất?
"""), q=Q("""
北京的夏天是什么样的？|白天很热，但是晚上比较凉快。|Ban ngày rất nóng, tối khá mát.
北京的秋天是什么样的？|树上的叶子都变成了红色、黄色，非常漂亮。|Lá cây chuyển đỏ, vàng, rất đẹp.
王一飞为什么最不喜欢冬天？|因为冬天不但冷，而且风很大。|Vì mùa đông không những lạnh mà gió còn to.
"""))],
grammar=[
 G("huozhe2", "选择复句“或者……，或者……”", "Câu ghép lựa chọn “或者……，或者……”",
   "Câu ghép lựa chọn “或者……，或者……” thường dùng trong văn nói, biểu thị lựa chọn một trong hai hoặc nhiều phương án khác nhau (hoặc… hoặc…).",
   [F("kw:或者|A:Phương án 1|kw2:或者|B:Phương án 2|X:Phần sau", [
     ("[或者]|明天去，|[或者]|后天去，|我给你打电话", "。", "Hoặc mai đi, hoặc ngày kia đi, cô sẽ gọi cho em."),
     ("我们|[或者]|今天去电影院看电影，|[或者]|明天在家看电影", "。", "Chúng ta hoặc hôm nay ra rạp xem phim, hoặc mai ở nhà xem phim."),
     ("晚饭你自己选，|[或者]|吃中国菜，|[或者]|吃日本菜", "。", "Bữa tối bạn tự chọn, hoặc ăn món Trung, hoặc ăn món Nhật.")])]),
 G("qilai2", "趋向补语的引申用法（2）：……起来", "Cách dùng mở rộng của bổ ngữ xu hướng (2) – “……起来”",
   "Bổ ngữ xu hướng “起来” đặt sau động từ hoặc tính từ, biểu thị hành động bắt đầu hoặc chuyển sang trạng thái mới. Nếu động từ có tân ngữ, tân ngữ đặt giữa “起” và “来”.",
   [F("S:Chủ ngữ|V:Động từ / tính từ|kw:起|O:(Tân ngữ)|kw2:来", [
     ("雨已经|下|[起]||[来]", "了。", "Mưa đã bắt đầu rơi rồi."),
     ("最近天气|热|[起]||[来]", "了。", "Gần đây trời bắt đầu nóng lên rồi."),
     ("怎么突然|刮|[起]|风|[来]", "了？", "Sao đột nhiên lại nổi gió thế?"),
     ("看到那张照片，大家都|笑|[起]||[来]", "了。", "Nhìn thấy bức ảnh đó, mọi người đều bật cười.")])]),
 G("jiu_fanwei", "范围副词“就”", "Phó từ chỉ phạm vi “就”",
   "“就” đặt trước động từ mang số lượng để biểu thị số lượng ít, mức độ thấp hoặc thời gian ngắn (chỉ). “就” cũng có thể đặt trước danh từ / cụm danh từ làm chủ ngữ để biểu thị trường hợp ngoại lệ (chỉ riêng).",
   [F("S:Chủ ngữ|kw:就|V:Động từ + số lượng", [
     ("北京常常下雪，但听说今年|[就]|下了一次", "。", "Bắc Kinh hay có tuyết, nhưng nghe nói năm nay chỉ rơi một lần."),
     ("他昨天|[就]|看了十分钟书", "。", "Hôm qua anh ấy chỉ đọc sách có mười phút.")], cap="Số lượng ít, thời gian ngắn"),
    F("C:Tình huống chung|kw:就|X:Ngoại lệ", [
     ("我每天书包里都放着雨伞，|[就]|今天没带", "。", "Ngày nào tôi cũng để ô trong cặp, riêng hôm nay không mang."),
     ("你们点的菜都挺好吃的，|[就]|我点的这个菜不太好吃", "。", "Các món các bạn gọi đều ngon, riêng món tôi gọi là không ngon lắm.")], cap="Ngoại lệ")]),
 G("xialai3", "趋向补语的引申用法（3）：……下来", "Cách dùng mở rộng của bổ ngữ xu hướng (3) – “……下来”",
   "Bổ ngữ xu hướng “下来” đặt sau động từ, biểu thị một hành động cần nhiều thời gian, công sức hoặc phải vượt qua khó khăn mới hoàn thành.",
   [F("T:Thời gian / việc|V:Động từ|kw:下来|C:Kết quả", [
     ("这一年多|住|[下来]|，我还是更喜欢北京的四季", "。", "Sống ở đây hơn một năm, tôi vẫn thích bốn mùa Bắc Kinh hơn."),
     ("这半年|练|[下来]|，他画画的水平提高了不少", "。", "Luyện tập nửa năm, trình độ vẽ của anh ấy tiến bộ khá nhiều."),
     ("5000米的长跑比赛，没想到我|跑|[下来]|了", "。", "Cuộc thi chạy 5000 mét, không ngờ tôi chạy hết được.")])]),
],
test=dict(
 l2=["她想休息|她想工作日去|今天天气不好", "四季都不一样|每天都是夏天|一年有两个季节", "给她一把雨伞|让她早点儿回家|告诉她已经下雨了"],
 l3=["天气热|太阳很早下山|很多人出去吃饭", "下大雨|刮大风|一直阴天", "常常刮风|不冷也不热|每天都很冷", "一年都很冷|每天都很热|王老师还不习惯"],
 r1=(["是啊，每天都热得不想出门，还是房间里凉快。", "李老师把雨伞借给我了，咱们一起走吧。", "希望越来越多的人关注这个问题。", "不一定，去年一次也没下。", "当然。我们先坐公交车，然后换地铁。", "医生也这么说，但是我已经习惯了。"],
     ["这里冬天常下雪吗？", "雨越下越大，一会儿怎么回家？", "最近天气太热，空调都快要卖完了。", "环境越来越差，我们得想想办法。", "虽然夏天运动完很热，但是你也不应该马上喝很多冰水。"]),
 r2=(["变成", "刚才", "常常", "关注", "鞋", "地方"],
     ["这个花园很安静，我吃完早饭（　　）一个人来这里走走。", "（　　）还晴天呢，怎么突然就下起雨来了？", "他每天早上都看新闻，非常（　　）天气的变化。", "A：你在这儿住了好几年了，早就习惯了吧？\nB：是的。这里已经（　　）我的第二个家了，我会一直住下去。", "A：咱们找个（　　）休息一会儿吧，雨可能要下起来了。\nB：好。前面有一家咖啡店，马上就到了。"]),
 r3=[("今天早上一出门，我就发现比昨天冷得多。走了一会儿天突然黑了，我马上决定回家去拿雨伞了。", "今天早上的天气怎么样？", "下雨了|一直阴天|比昨天冷多了"),
     ("下了好几天的雨，今天下午终于出太阳了，天气很舒服。我和朋友一起去公园走了走，公园里的花都开了，来看花的人挺多的。", "他为什么和朋友一起去公园？", "天气很舒服|公园里人不多|想找凉快的地方"),
     ("这张照片很有意思，是我跟同学们爬山的时候照的。那天我们爬完山就住在山上了。虽然是夏天，但太阳下山以后天气特别冷，风也很大。别的同学或者带了长裤，或者带了大衣，我只穿了一条短裤和一件衬衫。因为太冷了，同学们把雨衣都借给我了。你看，照片上就我一个人穿着好几件雨衣。",
      ("那天山上的天气怎么样？", "很热|下雨了|太阳下山后很冷"), ("同学们为什么把雨衣借给他？", "因为拍照有意思|因为他没带大衣|因为他雨衣丢了"))],
 w1=["今天（fēng）刮得很大，我们别去坐船了。", "这几年住下来，我最喜欢的（jì）节还是秋天。", "秋天来了，天气变（liáng）快了。"],
 w2=[("刚才", "刚才下雨了，她打着伞在公园里走。"), ("常常", "爷爷常常坐在公园里看书。"), ("关注", "她每天都很关注天气的变化。")],
 gl={"11": "Ở đây mùa đông hay có tuyết không? → D: Không chắc, năm ngoái chẳng rơi lần nào.",
     "12": "Mưa càng lúc càng to, lát nữa về nhà thế nào? → B: Thầy Lý cho mình mượn ô rồi, chúng ta cùng về nhé.",
     "13": "Dạo này nóng quá, điều hòa sắp bán hết rồi. → A: Đúng vậy, ngày nào cũng nóng không muốn ra khỏi nhà, ở trong phòng vẫn mát hơn.",
     "14": "Môi trường ngày càng tệ, chúng ta phải nghĩ cách. → C: Mong ngày càng nhiều người quan tâm đến vấn đề này.",
     "15": "Tuy mùa hè tập thể thao xong rất nóng, nhưng bạn cũng không nên uống ngay nhiều nước đá. → F: Bác sĩ cũng nói vậy, nhưng mình quen rồi.",
     "16": "常常一个人来这里走走 – thường một mình đến đây đi dạo. → C 常常.",
     "17": "刚才还晴天呢 – lúc nãy còn nắng mà. → B 刚才.",
     "18": "非常关注天气的变化 – rất quan tâm thay đổi thời tiết. → D 关注.",
     "19": "已经变成我的第二个家了 – đã trở thành ngôi nhà thứ hai của tôi. → A 变成.",
     "20": "找个地方休息 – tìm chỗ nghỉ. → F 地方.",
     "21": "“我就发现比昨天冷得多” → C.",
     "22": "“今天下午终于出太阳了，天气很舒服” → A.",
     "23": "“太阳下山以后天气特别冷” → C.",
     "24": "Các bạn khác có quần dài hoặc áo khoác, còn “我只穿了一条短裤和一件衬衫” → B 因为他没带大衣."}),
)
