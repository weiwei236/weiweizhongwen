# -*- coding: utf-8 -*-
# 发展汉语·初级综合(I) – Bài 29, 30
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[29] = dict(zh="晚会开得非常成功", en="The Party Is a Real Success", vi="Buổi tiệc rất thành công",
intro="Cuối học kỳ, cả lớp tổ chức tiệc để thư giãn. Ai hát hay, ai nhảy giỏi, ai bơi giỏi? Mỗi tháng sinh hoạt phí hết bao nhiêu?",
vocab=V("""
结束|jiéshù|dong|kết thúc|考试结束了，我们去玩儿吧。~Thi xong rồi, chúng ta đi chơi đi.
开|kāi|dong|mở, tổ chức (cuộc họp, tiệc)|明天我们开一个会。~Mai chúng ta họp một buổi.
轻松|qīngsōng|tt|thoải mái, nhẹ nhõm|考完试，大家都很轻松。~Thi xong ai cũng thấy nhẹ nhõm.
得|de|tro|(trợ từ, nối động từ với bổ ngữ trạng thái)|他说得很好。~Anh ấy nói rất giỏi.
成功|chénggōng|tt|thành công|这次活动非常成功。~Hoạt động lần này rất thành công.
男|nán|tt|nam|我们班男同学多。~Lớp tôi nhiều bạn nam.
饮料|yǐnliào|dt|đồ uống|你想喝什么饮料？~Bạn muốn uống gì?
女|nǚ|tt|nữ|那个女孩子是我妹妹。~Cô bé kia là em gái tôi.
痛快|tòngkuai|tt|thỏa thích, sảng khoái|今天玩儿得真痛快！~Hôm nay chơi thật thỏa thích!
表演|biǎoyǎn|dong|biểu diễn|她表演了一个节目。~Cô ấy biểu diễn một tiết mục.
讲|jiǎng|dong|kể, nói|奶奶给我讲了一个故事。~Bà kể cho tôi một câu chuyện.
故事|gùshi|dt|câu chuyện|这个故事很有意思。~Câu chuyện này rất thú vị.
哪里|nǎli|dai|đâu có (khiêm tốn khi được khen)|哪里，哪里，我说得不好。~Đâu có, đâu có, tôi nói chưa tốt.
游泳|yóu yǒng|cum|bơi|夏天我常去游泳。~Mùa hè tôi hay đi bơi.
游|yóu|dong|bơi|你游得真快！~Bạn bơi nhanh thật!
俩|liǎ|dai|hai (người)|咱们俩一起去吧。~Hai chúng ta cùng đi nhé.
比|bǐ|dong|thi, so tài|咱们比一比，看谁跑得快。~Chúng ta thi xem ai chạy nhanh.
水平|shuǐpíng|dt|trình độ|他的汉语水平很高。~Trình độ tiếng Hán của anh ấy rất cao.
高|gāo|tt|cao|他长得很高。~Anh ấy rất cao.
知识|zhīshi|dt|kiến thức|读书可以学到很多知识。~Đọc sách có thể học được nhiều kiến thức.
表扬|biǎoyáng|dong|khen ngợi|老师表扬了我。~Thầy khen tôi.
文章|wénzhāng|dt|bài văn|这篇文章写得很好。~Bài văn này viết rất hay.
花|huā|dong|tiêu (tiền), tốn (thời gian)|我这个月花了很多钱。~Tháng này tôi tiêu nhiều tiền.
包括|bāokuò|dong|bao gồm|房租包括水费和电费吗？~Tiền nhà có bao gồm tiền nước và tiền điện không?
电|diàn|dt|điện|宿舍停电了。~Ký túc xá mất điện rồi.
交通|jiāotōng|dt|giao thông|这儿的交通很方便。~Giao thông ở đây rất tiện.
加上|jiāshang|dong|cộng thêm|房租加上饭钱，一个月三千块。~Tiền nhà cộng tiền ăn, một tháng ba nghìn tệ.
零花钱|línghuāqián|dt|tiền tiêu vặt|妈妈每个月给我零花钱。~Mẹ cho tôi tiền tiêu vặt hằng tháng.
够|gòu|tt|đủ|我的钱不够了。~Tiền của tôi không đủ rồi.
可能|kěnéng|pho|có thể, có lẽ|明天可能下雨。~Ngày mai có thể mưa.
这里|zhèli|dai|ở đây|这里的天气很好。~Thời tiết ở đây rất đẹp.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
这个学期就要结束了。老师说，大家学习都很累，开个晚会轻松一下吧。|Học kỳ này sắp kết thúc. Thầy nói mọi người học đều rất mệt, tổ chức một buổi tiệc cho thư giãn nhé.
昨天晚上，我们开了一个晚会，晚会开得非常成功。|Tối qua chúng tôi tổ chức một buổi tiệc, buổi tiệc rất thành công.
男同学准备了水果和饮料，女同学做了很多好吃的。|Các bạn nam chuẩn bị hoa quả và đồ uống, các bạn nữ làm nhiều món ngon.
大家吃得很高兴，玩儿得也很痛快。|Mọi người ăn rất vui, chơi cũng rất thỏa thích.
很多同学表演了节目，有的唱歌，有的跳舞，有的讲故事，|Nhiều bạn biểu diễn tiết mục, có bạn hát, có bạn nhảy, có bạn kể chuyện,
大家一直玩儿到十一点多才结束。|mọi người chơi đến hơn 11 giờ mới kết thúc.
"""), q=Q("""
晚会开得怎么样？|晚会开得非常成功。|Rất thành công.
大家玩儿得怎么样？|大家吃得很高兴，玩儿得也很痛快。|Ăn rất vui, chơi rất thỏa thích.
""")),
 dict(t="课文二", narr=False, lines=T("""
马丁>阿明，我只知道你跑得快，没想到歌也唱得那么好。|A Minh, mình chỉ biết bạn chạy nhanh, không ngờ hát cũng hay thế.
阿明>哪里，哪里。你昨天晚上跳舞也跳得不错啊。|Đâu có, đâu có. Tối qua bạn nhảy cũng khá đấy chứ.
马丁>我喜欢跳舞，但是跳得不太好。|Mình thích nhảy nhưng nhảy chưa giỏi lắm.
崔浩>林娜，听说你游泳游得不错，什么时候咱们俩比一比？|Linna, nghe nói bạn bơi giỏi, khi nào hai đứa mình thi thử nhé?
林娜>行啊。|Được thôi.
崔浩>对了，你中国画学得怎么样了？|À này, tranh Trung Quốc bạn học thế nào rồi?
林娜>我刚学一年，水平不高，画得不好。|Mình mới học một năm, trình độ chưa cao, vẽ chưa đẹp.
崔浩>山田，你有什么爱好？|Yamada, bạn có sở thích gì?
山田>我呀，爱睡觉，每天睡得早，起得晚。|Mình à, thích ngủ, ngày nào cũng ngủ sớm dậy muộn.
崔浩>不对。你爱学习，知识丰富，老师经常表扬你文章写得好。|Không đúng. Bạn chăm học, kiến thức phong phú, thầy hay khen bạn viết văn hay.
山田>哪里，你们的汉语也都很好。|Đâu có, tiếng Hán của các bạn cũng đều rất giỏi.
"""), q=Q("""
谁唱歌唱得好？|阿明唱歌唱得好。|A Minh.
马丁跳舞跳得怎么样？|跳得不错，但是他说自己跳得不太好。|Khá, nhưng anh tự nói chưa giỏi.
""")),
 dict(t="课文三", narr=False, lines=T("""
山田>你今天怎么来得这么晚？是不是昨天晚上玩儿得太累了？|Hôm nay sao bạn đến muộn thế? Có phải tối qua chơi mệt quá không?
崔浩>不是。我这个月的生活费花得太快，又没钱了，我去取钱了。|Không phải. Tháng này mình tiêu sinh hoạt phí nhanh quá, lại hết tiền rồi, mình đi rút tiền.
山田>你每个月要花多少钱？|Mỗi tháng bạn tiêu bao nhiêu tiền?
崔浩>大概五六千吧。包括房租、水费、电费、电话费、交通费、吃饭，再加上一些零花钱。|Khoảng năm sáu nghìn. Bao gồm tiền nhà, nước, điện, điện thoại, đi lại, ăn uống, cộng thêm ít tiền tiêu vặt.
山田>我也差不多花五六千，有时候五六千还不够。|Mình cũng tiêu khoảng năm sáu nghìn, có lúc năm sáu nghìn còn không đủ.
崔浩>可能别的城市生活费便宜一些。|Có lẽ thành phố khác sinh hoạt phí rẻ hơn.
山田>可是我已经习惯这里了。|Nhưng mình đã quen ở đây rồi.
崔浩>我也一样。|Mình cũng vậy.
"""), q=Q("""
崔浩为什么来得那么晚？|因为他没钱了，去取钱了。|Vì hết tiền, đi rút tiền.
崔浩每个月大概花多少钱？|大概五六千。|Khoảng năm sáu nghìn.
"""))],
grammar=[
 G("qingtai", "晚会开得非常成功。", "Bổ ngữ trạng thái: V + 得 + Adj",
   "Miêu tả, đánh giá động tác hoặc trạng thái (thường xuyên, đã xảy ra hoặc đang diễn ra). Nếu động từ có tân ngữ thì lặp lại động từ: (V +) O + V + 得 + Adj (động từ thứ nhất thường lược). Phủ định: 不 đặt trước tính từ. Câu hỏi chính phản: V + 得 + Adj 不 Adj?",
   [F("S:Chủ ngữ|V:Động từ|kw:得|A:Tính từ", [("他|跑|[得]|很快", "。", "Anh ấy chạy rất nhanh."), ("我们|玩儿|[得]|很高兴", "。", "Chúng tôi chơi rất vui."), ("你|说|[得]|太对了", "！", "Bạn nói đúng quá!")]),
    F("S:Chủ ngữ|O:(V+) O|V:V|kw:得|A:Tính từ", [("他|(唱)歌|唱|[得]|很好", "。", "Anh ấy hát rất hay."), ("山田|(写)汉字|写|[得]|很好", "。", "Yamada viết chữ Hán rất đẹp."), ("她|(说)汉语|说|[得]|不快", "。", "Cô ấy nói tiếng Hán không nhanh.")], cap="Có tân ngữ: lặp lại động từ"),
    F("S:Chủ ngữ|O:(V+) O|V:V|kw:得|A:Adj 不 Adj", [("他|歌|唱|[得]|好不好", "？", "Anh ấy hát có hay không?"), ("他||跑|[得]|快不快", "？", "Anh ấy chạy có nhanh không?"), ("你们||玩|[得]|好不好", "？", "Các bạn chơi có vui không?")], cap="Câu hỏi chính phản")]),
 G("ai_like", "我呀，爱睡觉。", "爱 + V: thích, hay (làm gì)",
   "“爱” nghĩa là thích, ưa; cũng chỉ thói quen hay làm gì.",
   [F("S:Chủ ngữ|kw:爱|V:Động từ", [("我|[爱]|睡觉", "。", "Tôi thích ngủ."), ("她|[爱]|学习", "。", "Cô ấy chăm học."), ("我妹妹|[爱]|唱歌", "。", "Em gái tôi thích hát.")])],
   notes=["哪里，哪里: đâu có, đâu có – đáp lại một cách khiêm tốn khi được khen.", "可能: có lẽ – 可能别的城市生活费便宜一些。"]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["结束", "轻松", "成功", "痛快", "表演", "水平", "表扬", "包括", "够", "可能"], [
   "电影九点【结束】。", "放假了，大家都很【轻松】。", "这次比赛我们班很【成功】。", "今天玩儿得真【痛快】！", "她在晚会上【表演】了一个中国舞。",
   "你的汉语【水平】越来越高了。", "老师【表扬】他作业写得好。", "房租不【包括】电费。", "这些钱【够】不够？", "他今天没来，【可能】病了。"]),
 opn("二、用“得”回答问题", "Trả lời bằng bổ ngữ trạng thái V + 得 + Adj.", [
   ("你昨天睡得好吗？", "我昨天睡得很好。"), ("他汉语说得怎么样？", "他汉语说得很流利。"), ("你唱歌唱得好不好？", "我唱歌唱得不太好。"), ("晚会开得怎么样？", "晚会开得非常成功。")]),
 pick("三、选择正确的句子", "Chọn câu đúng.", [
   (["他说汉语说得很好。", "他说汉语很好得。"], ["选出正确的句子：【他说汉语说得很好。】"]), (["她跑得不快。", "她不跑得快。"], ["选出正确的句子：【她跑得不快。】"]),
   (["你写字写得好不好？", "你写字好不好得？"], ["选出正确的句子：【你写字写得好不好？】"]), (["我们玩儿得很痛快。", "我们很痛快玩儿得。"], ["选出正确的句子：【我们玩儿得很痛快。】"])]),
 tf("四、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("女同学准备了水果和饮料。", False), ("大家一直玩儿到十一点多。", True), ("林娜画中国画画得很好。", False), ("老师经常表扬山田文章写得好。", True), ("崔浩每个月大概花五六千。", True)]),
 opn("五、说一说，写一写", "Viết khoảng 60 chữ về một buổi tiệc hoặc sở thích của các bạn trong lớp.", [
   ("你们班开过晚会吗？晚会开得怎么样？谁唱歌唱得好？谁跳舞跳得好？（得　有的……有的……　哪里）",
    "（参考）上个周末我们班开了一个晚会，晚会开得很成功。有的同学唱歌，有的同学跳舞。玛丽唱歌唱得非常好，马克跳舞跳得也不错。大家吃得很高兴，玩儿得也很痛快。")]),
])

B[30] = dict(zh="我当过英语老师", en="I Used to Be an English Teacher", vi="Tôi từng làm giáo viên tiếng Anh",
intro="Ba năm trước, “tôi” tốt nghiệp đại học rồi chọn sang Trung Quốc rèn luyện. Học tiếng Hán, làm thêm, dạy ngoại ngữ ở nông thôn Tây Bắc… những trải nghiệm đó đã thay đổi cuộc đời “tôi”.",
vocab=V("""
毕业|bì yè|dong|tốt nghiệp|我明年大学毕业。~Năm sau tôi tốt nghiệp đại học.
其他|qítā|dai|khác|其他同学都回家了。~Các bạn khác đều về nhà rồi.
选择|xuǎnzé|dong|chọn, lựa chọn|你选择哪一个？~Bạn chọn cái nào?
熟悉|shúxī|tt|quen thuộc|我对这个城市不太熟悉。~Tôi không quen thuộc thành phố này lắm.
离开|lí kāi|dong|rời khỏi|我明天就要离开北京了。~Mai tôi sẽ rời Bắc Kinh.
所|suǒ|lg|(lượng từ cho trường học, bệnh viện, nhà…)|这是一所很有名的大学。~Đây là một trường đại học rất nổi tiếng.
语言|yǔyán|dt|ngôn ngữ|学习一门语言不容易。~Học một ngôn ngữ không dễ.
最初|zuìchū|dt|lúc đầu, ban đầu|最初我一句汉语也不会说。~Lúc đầu tôi không nói được câu tiếng Hán nào.
因为|yīnwèi|lien|bởi vì|因为下雨，我没去公园。~Vì trời mưa nên tôi không đi công viên.
交流|jiāoliú|dong|giao lưu, trao đổi|我常跟中国朋友用汉语交流。~Tôi thường giao tiếp với bạn Trung Quốc bằng tiếng Hán.
困难|kùnnan|tt|khó khăn|有困难就告诉我。~Có khó khăn thì nói với tôi.
遇到|yùdào|dong|gặp phải|在路上我遇到了老师。~Trên đường tôi gặp thầy giáo.
哭|kū|dong|khóc|孩子哭了，快去看看。~Đứa bé khóc rồi, mau đi xem.
过|guo|tro|đã từng (sau động từ)|我去过上海。~Tôi đã từng đến Thượng Hải.
坚持|jiānchí|dong|kiên trì|学汉语要坚持每天练习。~Học tiếng Hán phải kiên trì luyện tập mỗi ngày.
留|liú|dong|ở lại|放假的时候我留在学校。~Kỳ nghỉ tôi ở lại trường.
地|de|tro|(trợ từ, nối trạng ngữ với động từ)|他高兴地说：“谢谢！”~Anh ấy vui vẻ nói: “Cảm ơn!”
发现|fāxiàn|dong|phát hiện|我发现我的手机不见了。~Tôi phát hiện điện thoại không thấy đâu.
出去|chūqu|dong|đi ra ngoài|周末我们出去玩儿吧。~Cuối tuần chúng ta ra ngoài chơi nhé.
钱包|qiánbāo|dt|ví tiền|我的钱包丢了。~Ví tiền của tôi bị mất.
极|jí|pho|cực kỳ (Adj + 极了)|这个菜好吃极了。~Món này ngon cực kỳ.
翻译|fānyì|dt|phiên dịch, người phiên dịch|我想当一名翻译。~Tôi muốn làm phiên dịch.
意义|yìyì|dt|ý nghĩa|这件事很有意义。~Việc này rất có ý nghĩa.
决定|juédìng|dong|quyết định|我决定明年去中国留学。~Tôi quyết định năm sau sang Trung Quốc du học.
农村|nóngcūn|dt|nông thôn|我爷爷住在农村。~Ông tôi sống ở nông thôn.
外语|wàiyǔ|dt|ngoại ngữ|你会说几门外语？~Bạn biết mấy ngoại ngữ?
穷|qióng|tt|nghèo|以前这儿是个穷地方。~Trước đây đây là một nơi nghèo.
见|jiàn|dong|thấy, gặp|我从来没见过雪。~Tôi chưa từng thấy tuyết.
热情|rèqíng|tt|nhiệt tình|这儿的人很热情。~Người ở đây rất nhiệt tình.
友好|yǒuhǎo|tt|thân thiện|他们对我很友好。~Họ rất thân thiện với tôi.
当……的时候|dāng……de shíhou|cum|khi …, lúc …|当我到家的时候，妈妈已经睡了。~Khi tôi về đến nhà, mẹ đã ngủ rồi.
经验|jīngyàn|dt|kinh nghiệm|他有很多工作经验。~Anh ấy có nhiều kinh nghiệm làm việc.
经历|jīnglì|dt|trải nghiệm|这是一次难忘的经历。~Đây là một trải nghiệm khó quên.
西北|Xīběi|rieng|vùng Tây Bắc (Trung Quốc)|西北的冬天很冷。~Mùa đông Tây Bắc rất lạnh.
"""),
texts=[dict(t="课文", narr=True, lines=T("""
三年以前，我大学毕业了。和其他同学一样，我没有马上去工作，我选择了到自己不熟悉的地方去锻炼。|Ba năm trước, tôi tốt nghiệp đại học. Giống các bạn khác, tôi không đi làm ngay mà chọn đến một nơi mình không quen để rèn luyện.
去哪儿呢？最后我决定去中国。当然，去中国就要先学会汉语。|Đi đâu đây? Cuối cùng tôi quyết định sang Trung Quốc. Đương nhiên, sang Trung Quốc thì phải học tiếng Hán trước.
为了学会汉语，我离开了家，离开了父母，来到了北京。|Để học tiếng Hán, tôi rời nhà, rời bố mẹ, đến Bắc Kinh.
我先在一所语言学校学习。最初的几个月，因为我的汉语说得不好，跟中国人交流很困难，遇到了不少麻烦。|Đầu tiên tôi học ở một trường ngôn ngữ. Mấy tháng đầu, vì nói tiếng Hán chưa tốt nên giao tiếp với người Trung Quốc rất khó khăn, gặp không ít phiền phức.
我哭过，也想过回去，但是最后还是坚持留在了这里。慢慢地，我发现我开始喜欢这里了。|Tôi đã từng khóc, cũng từng nghĩ quay về, nhưng cuối cùng vẫn kiên trì ở lại. Dần dần, tôi phát hiện mình bắt đầu thích nơi này.
有一次，我出去玩儿。回来的时候，我把钱包忘在了出租汽车里。|Có một lần tôi đi chơi. Lúc về, tôi để quên ví trên taxi.
到家以后才发现钱包没了，我非常着急，但是也没有办法。|Về đến nhà mới phát hiện mất ví, tôi rất sốt ruột nhưng cũng không có cách nào.
没想到，第二天，那个司机到学校找到了我。他还我钱包的时候，我高兴极了。|Không ngờ, hôm sau người tài xế ấy đến trường tìm tôi. Lúc anh trả ví cho tôi, tôi vui cực kỳ.
我问他：“你怎么能找到我？”他说：“是你的学生证帮了我的忙。”我很高兴遇到了一个好人。|Tôi hỏi: “Sao anh tìm được tôi?” Anh nói: “Là thẻ sinh viên của cô đã giúp tôi.” Tôi rất vui vì gặp được một người tốt.
一年以后，我开始一边学习，一边打工。我当过翻译，也当过英语老师，我还去过许多地方旅行。|Một năm sau, tôi bắt đầu vừa học vừa làm thêm. Tôi từng làm phiên dịch, từng làm giáo viên tiếng Anh, còn từng đi du lịch nhiều nơi.
但是我觉得这些都不是我想要的，我应该去做更有意义的事情。后来我决定去西北农村当外语老师。|Nhưng tôi thấy đó đều không phải điều mình muốn, tôi nên làm việc có ý nghĩa hơn. Sau đó tôi quyết định đến nông thôn Tây Bắc làm giáo viên ngoại ngữ.
我去的是个穷地方，这里的人们没见过外国人，但是他们对我很热情，也很友好。|Nơi tôi đến là vùng nghèo, người ở đây chưa từng thấy người nước ngoài, nhưng họ rất nhiệt tình và thân thiện với tôi.
去年，当我要离开这里回国的时候，我的学生都哭了……|Năm ngoái, khi tôi sắp rời nơi đó về nước, học sinh của tôi đều khóc…
现在我已经是一家大公司的职员了。公司最后选择了我，我想就是因为我有在中国的工作经验和生活经历吧。|Bây giờ tôi đã là nhân viên một công ty lớn. Công ty cuối cùng chọn tôi, tôi nghĩ chính là vì tôi có kinh nghiệm làm việc và trải nghiệm sống ở Trung Quốc.
"""), q=Q("""
大学毕业以后，“我”马上工作了吗？|没有，“我”选择了到不熟悉的地方去锻炼。|Không, chọn đến nơi lạ để rèn luyện.
刚开始来中国的时候，“我”过得好吗？|不好，汉语说得不好，交流很困难，遇到了不少麻烦。|Không tốt, giao tiếp khó, gặp nhiều phiền phức.
“我”的钱包找到了吗？|找到了，司机第二天到学校还给了“我”。|Tìm được, tài xế mang trả.
“我”做过什么工作？|当过翻译，也当过英语老师。|Phiên dịch và giáo viên tiếng Anh.
“我”为什么离开北京去西北工作？|“我”想去做更有意义的事情。|Muốn làm việc có ý nghĩa hơn.
“我”现在在哪儿工作？|在一家大公司工作。|Ở một công ty lớn.
"""))],
grammar=[
 G("jile", "我高兴极了。", "Adj/V + 极了: cực kỳ",
   "“极” biểu thị mức độ cao nhất, phía sau thường có “了”; hay dùng trong khẩu ngữ.",
   [F("S:Chủ ngữ|A:Tính từ / động từ|kw:极了", [("这个|容易|[极了]", "。", "Cái này dễ cực kỳ."), ("你说得|对|[极了]", "。", "Bạn nói đúng quá."), ("他对这件衣服|满意|[极了]", "。", "Anh ấy cực kỳ hài lòng với bộ quần áo này.")])]),
 G("guo_exp", "我当过翻译。", "V + 过: đã từng (kinh nghiệm)",
   "Biểu thị động tác hoặc trạng thái đã xảy ra trong quá khứ, nhấn mạnh kinh nghiệm. Phủ định: 没(有) + V + 过. Câu hỏi chính phản: thêm “没有” cuối câu.",
   [F("S:Chủ ngữ|V:Động từ|kw:过|O:Tân ngữ", [("我|坐|[过]|那种车", "。", "Tôi đã từng đi loại xe đó."), ("我|去|[过]|很多地方", "。", "Tôi đã từng đến nhiều nơi."), ("我|吃|[过]|烤鸭", "。", "Tôi đã từng ăn vịt quay.")]),
    F("S:Chủ ngữ|kw:没(有)|V:Động từ|kw2:过|O:Tân ngữ", [("他们|[没]|见|[过]|外国人", "。", "Họ chưa từng thấy người nước ngoài."), ("我|[没]|去|[过]|西北", "。", "Tôi chưa từng đến Tây Bắc."), ("我|[没有]|学|[过]|日语", "。", "Tôi chưa từng học tiếng Nhật.")], cap="Phủ định"),
    F("S:Chủ ngữ|V:Động từ|kw:过|O:Tân ngữ|kw2:没有", [("你|当|[过]|翻译|[没有]", "？", "Bạn từng làm phiên dịch chưa?"), ("你|看|[过]|中国电影|[没有]", "？", "Bạn từng xem phim Trung Quốc chưa?"), ("你|吃|[过]|法国菜|[没有]", "？", "Bạn từng ăn món Pháp chưa?")], cap="Câu hỏi chính phản")]),
 G("dang_shihou", "当我要离开这里回国的时候，我的学生都哭了。", "当……的时候: khi …, lúc …",
   "Biểu thị thời gian xảy ra sự việc, thường đặt ở đầu câu.",
   [F("kw:当|C:Sự việc|kw2:的时候|B:Mệnh đề chính", [("[当]|我回来|[的时候]|，他已经睡了", "。", "Khi tôi về, anh ấy đã ngủ rồi."), ("[当]|我发现|[的时候]|，已经晚了", "。", "Khi tôi phát hiện ra thì đã muộn rồi.")])]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["熟悉", "离开", "交流", "困难", "遇到", "坚持", "发现", "决定", "热情", "经验"], [
   "我对这儿还不太【熟悉】。", "我【离开】家已经一年了。", "我常常和同学用汉语【交流】。", "学汉字有点儿【困难】。", "昨天在超市我【遇到】了我的老师。",
   "每天跑步不容易，你要【坚持】。", "到家以后我才【发现】钥匙丢了。", "我【决定】暑假去云南旅行。", "中国朋友对我很【热情】。", "他有很多教汉语的【经验】。"]),
 opn("二、根据课文内容填空", "Điền vào chỗ trống theo nội dung bài khóa.", [
   ("“我”大学毕业以后选择到中国（　　）。", "锻炼"), ("“我”因为汉语不好，遇到了很多（　　）。", "麻烦"), ("最初的几个月，“我”遇到很多麻烦，后来开始（　　）北京了。", "喜欢"),
   ("有一次“我”在（　　）丢了钱包。", "出租汽车里"), ("后来司机把钱包送（　　）了。", "回来"), ("后来“我”到西北去（　　）英语。", "教"),
   ("西北人对“我”很（　　）、很（　　）。", "热情 / 友好"), ("“我”现在在（　　）工作。", "一家大公司")]),
 opn("三、把下面的句子改写成疑问句和否定句", "Viết lại thành câu hỏi và câu phủ định. Ví dụ: 我去过上海。→ 你去过上海吗？/ 你去过上海没有？→ 我没去过上海。", [
   ("我学过这本书。", "你学过这本书吗？/ 你学过这本书没有？→ 我没学过这本书。"), ("我当过翻译。", "你当过翻译吗？/ 你当过翻译没有？→ 我没当过翻译。"),
   ("我听过中国音乐。", "你听过中国音乐吗？/ 你听过中国音乐没有？→ 我没听过中国音乐。"), ("我打过工。", "你打过工吗？/ 你打过工没有？→ 我没打过工。"), ("我吃过饺子。", "你吃过饺子吗？/ 你吃过饺子没有？→ 我没吃过饺子。")]),
 tf("四、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("“我”大学毕业以后马上去工作了。", False), ("“我”最初在一所语言学校学习。", True), ("“我”把钱包忘在了学校里。", False), ("司机通过学生证找到了“我”。", True), ("西北农村的人以前没见过外国人。", True)]),
 opn("五、说一说，写一写", "Viết khoảng 80 chữ kể về trải nghiệm của bạn.", [
   ("你去过哪些地方？当过什么？有什么难忘的经历？（V+过　当……的时候　极了　因为　坚持）",
    "（参考）我去过很多地方，比如上海、西安和云南。我还当过汉语老师的助手。当我第一次来中国的时候，因为汉语说得不好，我遇到过很多困难。但是我坚持学习，现在我的汉语好极了。这是我最难忘的经历。")]),
])
