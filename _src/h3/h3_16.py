# -*- coding: utf-8 -*-
# HSK 3 – Bài 16: 我听说有的熊猫出国了
from gtb_gen import V, T, Q, F, G
B = {}

B[16] = dict(zh="我听说有的熊猫出国了", vi="Tôi nghe nói có những chú gấu trúc đã ra nước ngoài",
intro="Vương Nhất Tuyết đưa hai con đi xem mèo ở trung tâm nhận nuôi thú cưng, rồi đến vườn bách thú Bắc Kinh xem gấu trúc. Tiểu Minh hỏi liên tục, đúng là “mười vạn câu hỏi vì sao”.",
vocab=V("""
脏|zāng|tt|bẩn|你的鞋太脏了。~Giày của bạn bẩn quá.
可爱|kě'ài|tt|đáng yêu, dễ thương|这只小狗真可爱！~Con chó nhỏ này đáng yêu thật!
一会儿|yíhuìr|pho|một lúc, một lát|他一会儿看书，一会儿看手机。~Anh ấy lúc thì đọc sách, lúc thì xem điện thoại.
脚|jiǎo|dt|chân, bàn chân|我的脚有点儿疼。~Chân tôi hơi đau.
照顾|zhàogù|dong|chăm sóc|她每天照顾生病的奶奶。~Ngày nào cô ấy cũng chăm sóc bà bị ốm.
认得|rènde|dong|nhận ra|你还认得我吗？~Bạn còn nhận ra tôi không?
周末|zhōumò|dt|cuối tuần|周末你有什么打算？~Cuối tuần bạn có dự định gì?
动物园|dòngwùyuán|dt|vườn bách thú, sở thú|孩子们喜欢去动物园。~Bọn trẻ thích đi sở thú.
动物|dòngwù|dt|động vật|你最喜欢什么动物？~Bạn thích con vật nào nhất?
大熊猫|dàxióngmāo|dt|gấu trúc, gấu mèo|大熊猫是中国的国宝。~Gấu trúc là quốc bảo của Trung Quốc.
奇怪|qíguài|tt|kỳ lạ, kỳ quái|这个名字很奇怪。~Cái tên này rất kỳ lạ.
其实|qíshí|pho|thực ra|这个问题其实不难。~Câu hỏi này thực ra không khó.
竹子|zhúzi|dt|tre|熊猫最爱吃竹子。~Gấu trúc thích ăn tre nhất.
国宝|guóbǎo|dt|quốc bảo, bảo vật quốc gia|大熊猫是中国的国宝。~Gấu trúc là bảo vật quốc gia của Trung Quốc.
全|quán|tt|toàn bộ|全班同学都来了。~Cả lớp đều đến rồi.
野生|yěshēng|tt|hoang dã|野生大熊猫越来越多了。~Gấu trúc hoang dã ngày càng nhiều.
关于|guānyú|gioi|về…, có liên quan tới|这是一本关于中国历史的书。~Đây là cuốn sách về lịch sử Trung Quốc.
饱|bǎo|tt|no|我吃饱了，谢谢。~Tôi ăn no rồi, cảm ơn.
张|zhāng|dong|mở (miệng)|请张开嘴。~Hãy há miệng ra.
嘴|zuǐ|dt|miệng|小鸟张着嘴等吃的。~Chú chim nhỏ há miệng chờ ăn.
身边|shēnbiān|dt|bên cạnh|妈妈一直在我身边。~Mẹ luôn ở bên cạnh tôi.
半天|bàntiān|sl|nửa ngày, một lúc lâu|我等了你半天了。~Tôi đợi bạn cả buổi rồi.
脸|liǎn|dt|mặt, khuôn mặt|他的脸红了。~Mặt anh ấy đỏ lên.
大人|dàren|dt|người lớn|这个电影大人和孩子都喜欢。~Bộ phim này người lớn và trẻ con đều thích.
喜爱|xǐ'ài|dong|yêu thích|这首歌很受年轻人喜爱。~Bài hát này được người trẻ yêu thích.
"""),
texts=[dict(t="课文1", scene="在一家宠物领养店，王一雪和孩子们在看动物。", scene_vi="Tại một trung tâm nhận nuôi thú cưng, Vương Nhất Tuyết và các con đang xem động vật.", narr=False, lines=T("""
刘小雪>这只小猫你们养了多久了？|Con mèo nhỏ này các anh chị nuôi bao lâu rồi?
服务员>已经一年多了。第一天看见它的时候，它又脏又小。|Hơn một năm rồi. Ngày đầu tiên nhìn thấy nó, nó vừa bẩn vừa nhỏ.
刘小雪>现在它变得又干净又漂亮了。|Bây giờ nó trở nên vừa sạch vừa xinh rồi.
服务员>是啊。它还特别可爱，一会儿在你脚边睡觉，一会儿在你身上爬。|Đúng vậy. Nó còn cực kỳ đáng yêu, lúc thì ngủ dưới chân bạn, lúc thì bò lên người bạn.
刘小雪>你们把它照顾得真好。|Các anh chị chăm sóc nó tốt thật.
服务员>它就好像我们的孩子，我们照顾它，它也认得我们了。|Nó giống như con của chúng tôi vậy, chúng tôi chăm sóc nó, nó cũng nhận ra chúng tôi rồi.
刘小雪>妈妈，我们家也养一只小猫吧。|Mẹ ơi, nhà mình cũng nuôi một con mèo nhỏ đi.
王一雪>咱们没时间照顾，还是别养了，我周末带你们去北京动物园看动物吧。|Nhà mình không có thời gian chăm sóc, thôi đừng nuôi, cuối tuần mẹ đưa các con đi vườn bách thú Bắc Kinh xem động vật nhé.
"""), q=Q("""
服务员第一天看见这只小猫的时候，它是什么样的？|又脏又小。|Vừa bẩn vừa nhỏ.
服务员为什么觉得小猫很可爱？|它一会儿在你脚边睡觉，一会儿在你身上爬。|Lúc ngủ dưới chân, lúc bò lên người.
服务员和小猫的关系怎么样？|它就好像他们的孩子，也认得他们了。|Nó như con của họ, cũng nhận ra họ.
""")),
 dict(t="课文2", scene="在动物园，王一雪和孩子们边走边聊。", scene_vi="Vương Nhất Tuyết và các con vừa đi vừa trò chuyện ở vườn bách thú.", narr=False, lines=T("""
刘小明>妈妈，大熊猫这个名字很奇怪，它们跟猫有什么关系？|Mẹ ơi, cái tên “đại hùng miêu” (gấu mèo) lạ quá, chúng có liên quan gì đến mèo không?
王一雪>这个问题问得好，它们跟猫没什么关系，其实应该叫大猫熊。|Câu hỏi hay lắm, chúng chẳng liên quan gì đến mèo, thực ra nên gọi là “mèo gấu” mới đúng.
刘小明>大熊猫为什么只吃竹子不吃肉？|Gấu trúc sao chỉ ăn tre mà không ăn thịt?
王一雪>它们跟人一样，也可以吃肉，但是对肉不感兴趣。|Chúng cũng giống người, có thể ăn thịt, nhưng không hứng thú với thịt.
刘小明>大熊猫为什么是中国的国宝？|Vì sao gấu trúc là quốc bảo của Trung Quốc?
王一雪>全世界只有中国有野生大熊猫，中国是大熊猫的家。|Cả thế giới chỉ Trung Quốc có gấu trúc hoang dã, Trung Quốc là nhà của gấu trúc.
刘小明>我听说有的熊猫出国了，他们去哪儿了？|Con nghe nói có những chú gấu trúc ra nước ngoài, chúng đi đâu vậy?
王一雪>关于这个问题，我得慢慢给你讲。|Về câu hỏi này, mẹ phải từ từ kể cho con.
刘小雪>弟弟，你真是“十万个为什么”。|Em trai, em đúng là “mười vạn câu hỏi vì sao”.
"""), q=Q("""
大熊猫跟猫有关系吗？|没什么关系，其实应该叫大猫熊。|Chẳng liên quan gì, thực ra nên gọi là mèo gấu.
大熊猫为什么只吃竹子不吃肉？|它们可以吃肉，但是对肉不感兴趣。|Chúng ăn được thịt nhưng không hứng thú.
大熊猫为什么是中国的国宝？|全世界只有中国有野生大熊猫。|Cả thế giới chỉ Trung Quốc có gấu trúc hoang dã.
""")),
 dict(t="课文3", scene="在熊猫馆，王一雪和孩子们在看大熊猫。", scene_vi="Vương Nhất Tuyết và các con đang xem gấu trúc tại nhà của chúng.", narr=False, lines=T("""
刘小雪>这只大熊猫一会儿爬上去，一会儿跳下来，可爱极了！|Con gấu trúc này lúc thì trèo lên, lúc thì nhảy xuống, đáng yêu cực kỳ!
王一雪>它好像还没吃饱，站起来张着嘴找吃的呢。|Hình như nó chưa ăn no, đang đứng dậy há miệng tìm đồ ăn kìa.
刘小雪>它身边那只熊猫半天没动，是不是在睡觉呢？|Con gấu trúc bên cạnh nó nằm im cả buổi, có phải đang ngủ không?
王一雪>我看不见它的脸，可能是吧。一般来说，熊猫每天要睡很多次觉。|Mẹ không thấy mặt nó, có lẽ vậy. Thông thường, gấu trúc mỗi ngày ngủ rất nhiều lần.
刘小雪>对，除了睡觉以外，很多时间都在吃东西。|Đúng rồi, ngoài ngủ ra, phần lớn thời gian chúng đều ăn.
刘小明>大熊猫的生活真舒服啊！|Cuộc sống của gấu trúc sướng thật!
刘小雪>妈妈，您帮我和这两只大熊猫照一张照片吧。|Mẹ ơi, mẹ chụp cho con một tấm ảnh với hai con gấu trúc này nhé.
"""), q=Q("""
刘小雪为什么觉得这只大熊猫可爱极了？|因为它一会儿爬上去，一会儿跳下来。|Vì nó lúc trèo lên, lúc nhảy xuống.
王一雪为什么觉得它没吃饱？|因为它站起来张着嘴找吃的。|Vì nó đứng dậy há miệng tìm đồ ăn.
刘小明觉得大熊猫的生活怎么样？|真舒服。|Thật sướng.
""")),
 dict(t="课文4", scene="在家里，王一雪在写日记。", scene_vi="Vương Nhất Tuyết đang ngồi viết nhật ký ở trong nhà.", narr=True, lines=T("""
今天我带小雪和小明去动物园玩了。|Hôm nay tôi đưa Tiểu Tuyết và Tiểu Minh đi vườn bách thú chơi.
北京动物园是中国很有名的动物园，里面有非常多的动物，|Vườn bách thú Bắc Kinh là vườn bách thú rất nổi tiếng của Trung Quốc, bên trong có rất nhiều loài động vật,
当然，大人和孩子最喜爱的还是大熊猫。|đương nhiên, người lớn và trẻ con yêu thích nhất vẫn là gấu trúc.
每天有很多游客去熊猫馆，他们带着相机去给可爱的大熊猫拍照。|Ngày nào cũng có nhiều du khách đến nhà gấu trúc, họ mang máy ảnh đi chụp những chú gấu trúc đáng yêu.
动物园早上七点半开门，晚上七点关门，|Vườn bách thú mở cửa lúc bảy rưỡi sáng, đóng cửa lúc bảy giờ tối,
冬天比夏天游客少，所以也比平时早关门一个小时。|mùa đông ít du khách hơn mùa hè, nên cũng đóng cửa sớm hơn ngày thường một tiếng.
如果第一次来北京旅游，跟家人一起去北京动物园是个不错的选择。|Nếu lần đầu đến Bắc Kinh du lịch, cùng gia đình đến vườn bách thú Bắc Kinh là một lựa chọn không tồi.
"""), q=Q("""
今天王一雪带孩子们去哪儿了？|北京动物园。|Vườn bách thú Bắc Kinh.
很多游客去动物园做什么？|带着相机去熊猫馆给大熊猫拍照。|Mang máy ảnh đến nhà gấu trúc chụp ảnh.
北京动物园夏天和冬天的关门时间有什么不同？|冬天比夏天早关门一个小时。|Mùa đông đóng cửa sớm hơn mùa hè một tiếng.
"""))],
grammar=[
 G("yihuir", "并列复句“一会儿……，一会儿……”", "Câu ghép đẳng lập “一会儿……，一会儿……”",
   "Câu ghép “一会儿……，一会儿……” dùng để biểu thị nhiều hành động khác nhau xảy ra trong thời gian ngắn hoặc một tình huống đối lập (lúc thì…, lúc thì…).",
   [F("S:Chủ ngữ|kw:一会儿|A:Hành động / trạng thái 1|kw2:一会儿|B:Hành động / trạng thái 2", [
     ("它|[一会儿]|在你脚边睡觉，|[一会儿]|在你身上爬", "。", "Nó lúc thì ngủ dưới chân bạn, lúc thì bò lên người bạn."),
     ("他|[一会儿]|进来，|[一会儿]|出去，忙得很", "。", "Anh ấy lúc thì vào, lúc thì ra, bận lắm."),
     ("最近天气变化很快，|[一会儿]|冷，|[一会儿]|热", "。", "Gần đây thời tiết thay đổi nhanh, lúc lạnh lúc nóng.")])]),
 G("guanyu", "介词“关于”", "Giới từ “关于”",
   "Sau giới từ “关于” có thể thêm danh từ, dùng để dẫn nhập nội dung / đối tượng được đề cập đến (về…, liên quan đến…).",
   [F("kw:关于|O:Nội dung|C:Phần còn lại", [
     ("[关于]|这个问题，|我得慢慢给你讲", "。", "Về câu hỏi này, mẹ phải từ từ kể cho con."),
     ("[关于]|他的要求，|我们还要开会以后再决定", "。", "Về yêu cầu của anh ấy, chúng ta phải họp xong mới quyết định."),
     ("[关于]|比赛的时间，|我明天一定告诉大家", "。", "Về thời gian thi đấu, ngày mai tôi nhất định báo mọi người.")])]),
 G("yibanlaishuo", "固定短语“一般来说”", "Cụm từ cố định “一般来说”",
   "“一般来说” là cụm từ cố định thường dùng ở đầu câu, có nghĩa là trong hầu hết các trường hợp đều như vậy (thông thường, nói chung).",
   [F("kw:一般来说，|C:Nhận định chung", [
     ("[一般来说，]|熊猫每天要睡很多次觉", "。", "Thông thường, gấu trúc mỗi ngày ngủ rất nhiều lần."),
     ("[一般来说，]|这种树每年开一次花", "。", "Thông thường, loại cây này mỗi năm nở hoa một lần."),
     ("[一般来说，]|学习外语需要多练习", "。", "Nói chung, học ngoại ngữ cần luyện tập nhiều.")])]),
 G("bi11", "比较句（11）", "Câu so sánh (11) – “A 比 B + 多/少/早/晚 + động từ + số lượng”",
   "Trong câu so sánh với “比”, khi vị ngữ là động từ thường thì phía trước có thể thêm “多、少、早、晚” để biểu thị sự khác biệt về số lượng hoặc thời gian giữa hai đối tượng. Cấu trúc: A 比 B + 多/少/早/晚 + động từ + cụm số lượng.",
   [F("A:A|kw:比|B:B|kw2:多 / 少 / 早 / 晚|V:Động từ + số lượng", [
     ("冬天|[比]|夏天|[早]|关门一个小时", "。", "Mùa đông đóng cửa sớm hơn mùa hè một tiếng."),
     ("哥哥|[比]|弟弟|[多]|吃了三个饺子", "。", "Anh trai ăn nhiều hơn em trai ba cái sủi cảo."),
     ("我|[比]|他|[晚]|到了十分钟", "。", "Tôi đến muộn hơn anh ấy mười phút.")])]),
],
test=dict(
 l2=["初中|高中|大学", "不喜欢猫|没时间照顾它们|她在小猫咖啡馆工作", "不安全|天气不好|动物太少"],
 l3=["不喜欢小动物|对动物很了解|在动物园工作", "非常可爱|吃得很少|不喜欢爬树", "只能住在中国|去过很多地方|喜欢它的人不多", "一年多|十多年|二十年"],
 r1=(["一般来说，它吃饱了的话就睡觉了。", "医院就在前面那条街上，带它去看看吧。", "不是，这是我去中国西南看大熊猫的时候照的。", "它一边动一边听，它能听见我们听不见的声音。", "当然。我们先坐公交车，然后换地铁。", "公园和动物园我都想去。"],
     ["这张照片是在北京动物园照的吗？", "你怎么知道它还想吃东西？", "它看上去有点儿奇怪，半天没动了。", "这个周末你想去哪儿玩？", "这只小狗真可爱，它的耳朵为什么一直动？"]),
 r2=(["其实", "好像", "关于", "认得", "鞋", "身边"],
     ["大家都以为他的工作不累，（　　）他每天早上五点多就起床，去照顾这些小动物。", "我看了一个（　　）大熊猫的节目，现在非常想去动物园看大熊猫。", "虽然我不能每天在它（　　），但是一有时间我就回家看它。", "A：前面那只猫（　　）你家的猫。\nB：不是，那是我邻居的猫。", "A：你家的狗看见你以后为什么一直叫？\nB：我离开家时间太久了，它已经不（　　）我了。"]),
 r3=[("这几只小鸟现在什么都不会做，只会张着嘴等吃的，差不多一个星期以后才能用眼睛看这个世界。", "小鸟现在怎么样？", "会自己找吃的|能看清楚东西|只会等着吃东西"),
     ("这种鱼很奇怪，嘴像鸟一样，长长的，还有两只大大的眼睛，它在水里游的时候，一会儿快一会儿慢，好像在做游戏。", "这种鱼：", "喜欢做游戏|游得一直很快|看起来很奇怪"),
     ("丽丽发现她的小猫好像生病了，它一直在沙发上，不吃东西也不愿意动。丽丽很担心，决定带它去家附近的动物医院看看。到了医院门口，她才知道医院冬天比夏天早关门一个小时，现在医生都下班了。丽丽只能先把小猫带回家照顾，明天早上再带它去看医生。",
      ("丽丽带小猫去医院时，发现：", "医生很忙|小猫病好了|医院关门了"), ("丽丽什么时候再带小猫去医院？", "今天晚上|明天早上|明天中午"))],
 w1=["它已经吃（bǎo）了，现在在我脚边睡觉呢。", "我妹妹从小就喜欢小动（wù），她一直想养一条小狗。", "这只小鸟一直（zhāng）着嘴，等着吃东西。"],
 w2=[("脏", "小男孩儿和小狗在地上玩，衣服都玩脏了。"), ("脸", "她每天早上起床后先洗脸。"), ("照顾", "她每天都照顾这些小狗，它们都认得她。")],
 gl={"11": "Bức ảnh này chụp ở vườn bách thú Bắc Kinh à? → C: Không, đây là lúc mình đi Tây Nam Trung Quốc xem gấu trúc chụp.",
     "12": "Sao bạn biết nó vẫn muốn ăn? → A: Thông thường, nếu nó ăn no thì sẽ đi ngủ.",
     "13": "Trông nó hơi lạ, nằm im cả buổi rồi. → B: Bệnh viện ở ngay con phố phía trước, đưa nó đi khám đi.",
     "14": "Cuối tuần này bạn muốn đi đâu chơi? → F: Công viên và vườn bách thú mình đều muốn đi.",
     "15": "Con chó nhỏ này đáng yêu thật, sao tai nó cứ động đậy mãi? → D: Nó vừa động vừa nghe, nó nghe được âm thanh mà chúng ta không nghe thấy.",
     "16": "其实 – thực ra (công việc không hề nhẹ). → A 其实.",
     "17": "关于大熊猫的节目 – chương trình về gấu trúc. → C 关于.",
     "18": "在它身边 – ở bên cạnh nó. → F 身边.",
     "19": "好像你家的猫 – hình như là mèo nhà bạn. → B 好像.",
     "20": "它已经不认得我了 – nó không nhận ra tôi nữa. → D 认得.",
     "21": "“只会张着嘴等吃的” → C.",
     "22": "“这种鱼很奇怪” → C 看起来很奇怪.",
     "23": "“现在医生都下班了”, bệnh viện đã đóng cửa → C.",
     "24": "“明天早上再带它去看医生” → B."}),
)
