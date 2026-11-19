# -*- coding: utf-8 -*-
# HSK 4下 – Bài 13: 美好的日子
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[13] = dict(zh="美好的日子", vi="Những ngày tươi đẹp",
intro="Gia đình Lưu Minh đến Vườn thú hoang dã Bắc Kinh dịp Quốc tế Thiếu nhi; vợ chồng Vương Nhất Phi mời các bạn đón Trung thu; câu chuyện “đoàn viên ngược chiều” của Chu Lực; ký ức đẹp về Tết Nguyên đán.",
vocab=V("""
熊|xióng|dt|con gấu|动物园里的熊在吃东西。~Con gấu trong sở thú đang ăn.
老虎|lǎohǔ|dt|con hổ|老虎是一种很危险的动物。~Hổ là một loài động vật rất nguy hiểm.
喊|hǎn|dong|hét, gọi to|妈妈在楼下喊我吃饭。~Mẹ gọi to ở dưới nhà bảo tôi ăn cơm.
级|jí|lg|cấp, bậc|他已经通过了HSK四级考试。~Anh ấy đã thi đỗ HSK cấp 4.
树林|shùlín|dt|rừng cây|树林里有很多小鸟。~Trong rừng cây có nhiều chim nhỏ.
景区|jǐngqū|dt|khu danh thắng, khu du lịch|这个景区每年有很多游客。~Khu du lịch này mỗi năm có rất nhiều du khách.
区|qū|dt|khu, khu vực|这个区的环境很好。~Môi trường khu này rất tốt.
美|měi|tt|đẹp|这里的风景真美！~Phong cảnh ở đây đẹp quá!
节假日|jiéjiàrì|dt|ngày lễ, ngày nghỉ|节假日去旅游的人特别多。~Ngày lễ người đi du lịch đặc biệt đông.
千万|qiānwàn|pho|nhất định, nhất thiết (phải/không)|你千万别忘了带护照。~Bạn nhất định đừng quên mang hộ chiếu.
开玩笑|kāi wánxiào|dong|nói đùa, đùa giỡn|别生气，我跟你开玩笑呢。~Đừng giận, tôi đùa với bạn thôi.
东北虎|Dōngběihǔ|rieng|hổ Đông Bắc (hổ Siberia)|东北虎是国家一级保护动物。~Hổ Đông Bắc là động vật được bảo vệ cấp một quốc gia.
北京野生动物园|Běijīng Yěshēng Dòngwùyuán|rieng|Vườn thú hoang dã Bắc Kinh|周末我们去北京野生动物园看动物。~Cuối tuần chúng tôi đến Vườn thú hoang dã Bắc Kinh xem động vật.
月饼|yuèbing|dt|bánh trung thu|中秋节我们一起吃月饼。~Tết Trung thu chúng ta cùng ăn bánh trung thu.
葡萄|pútao|dt|quả nho|这些葡萄又大又甜。~Những quả nho này vừa to vừa ngọt.
香|xiāng|tt|thơm|厨房里的饭菜好香啊！~Đồ ăn trong bếp thơm quá!
街道|jiēdào|dt|đường phố|过年时街道上很热闹。~Dịp Tết đường phố rất náo nhiệt.
剧院|jùyuàn|dt|nhà hát|今晚剧院有一场演出。~Tối nay nhà hát có một buổi biểu diễn.
演出|yǎnchū|dong|biểu diễn|她在学校的晚会上演出了。~Cô ấy đã biểu diễn trong buổi dạ hội của trường.
赶|gǎn|dong|trùng vào, gặp đúng (lúc)|今年春节正好赶上周末。~Tết năm nay vừa đúng vào cuối tuần.
巧|qiǎo|tt|khéo, trùng hợp, đúng lúc|真巧，我们又见面了！~Trùng hợp quá, chúng ta lại gặp nhau!
中秋节|Zhōngqiūjié|rieng|Tết Trung thu|中秋节是中国的传统节日。~Tết Trung thu là ngày lễ truyền thống của Trung Quốc.
加拿大|Jiānádà|rieng|Canada|安妮是从加拿大来的。~Annie đến từ Canada.
之中|zhīzhōng|dt|trong, trong số|他是我们之中最高的。~Anh ấy cao nhất trong số chúng tôi.
铁路|tiělù|dt|đường sắt|这条铁路通到上海。~Tuyến đường sắt này đi đến Thượng Hải.
人员|rényuán|dt|nhân viên, nhân sự|工作人员正在检查车票。~Nhân viên đang kiểm tra vé.
反向|fǎnxiàng|dong|ngược chiều|很多父母来大城市和孩子“反向团圆”。~Nhiều bố mẹ lên thành phố lớn “đoàn viên ngược chiều” với con cái.
团圆|tuányuán|dong|đoàn tụ, đoàn viên|春节是全家团圆的日子。~Tết là ngày cả nhà đoàn tụ.
左右|zuǒyòu|dt|khoảng, chừng|我晚上十点左右睡觉。~Tôi đi ngủ khoảng mười giờ tối.
大约|dàyuē|pho|khoảng, chừng|从这儿到机场大约要一个小时。~Từ đây ra sân bay mất khoảng một tiếng.
烤|kǎo|dong|nướng|晚上我们去吃烤鸭吧。~Tối nay chúng ta đi ăn vịt quay nhé.
西红柿|xīhóngshì|dt|cà chua|我最喜欢吃西红柿炒鸡蛋。~Tôi thích nhất món trứng xào cà chua.
出现|chūxiàn|dong|xuất hiện|天上出现了一道彩虹。~Trên trời xuất hiện một cầu vồng.
作为|zuòwéi|gioi|là, với tư cách là|作为学生，我们应该认真学习。~Là học sinh, chúng ta nên học tập chăm chỉ.
传统|chuántǒng|tt|truyền thống|端午节是中国的传统节日。~Tết Đoan Ngọ là ngày lễ truyền thống của Trung Quốc.
有着|yǒuzhe|dong|có (văn viết)|这座城市有着悠久的历史。~Thành phố này có lịch sử lâu đời.
意义|yìyì|dt|ý nghĩa|这次旅行对我很有意义。~Chuyến đi này rất có ý nghĩa với tôi.
到来|dàolái|dong|đến, tới|新年就要到来了。~Năm mới sắp đến rồi.
美食|měishí|dt|món ngon, ẩm thực|成都有很多有名的美食。~Thành Đô có nhiều món ngon nổi tiếng.
年夜饭|niányèfàn|dt|bữa cơm tất niên|除夕晚上全家一起吃年夜饭。~Tối giao thừa cả nhà cùng ăn cơm tất niên.
回忆|huíyì|dong|nhớ lại, hồi tưởng|爷爷常常回忆年轻时的生活。~Ông thường nhớ lại cuộc sống thời trẻ.
童年|tóngnián|dt|thời thơ ấu|我的童年是在农村过的。~Tuổi thơ tôi sống ở nông thôn.
记忆|jìyì|dt|ký ức, trí nhớ|这是我最美好的记忆。~Đây là ký ức đẹp nhất của tôi.
已|yǐ|pho|đã|他已离开北京三年了。~Anh ấy đã rời Bắc Kinh ba năm rồi.
中年|zhōngnián|dt|trung niên|他已经是中年人了。~Ông ấy đã là người trung niên.
仍然|réngrán|pho|vẫn, vẫn như cũ|多年过去了，他仍然记得那件事。~Nhiều năm trôi qua, anh ấy vẫn nhớ chuyện đó.
兄弟|xiōngdì|dt|anh em trai|他们兄弟俩长得很像。~Hai anh em họ trông rất giống nhau.
元宵节|Yuánxiāojié|rieng|Tết Nguyên tiêu|元宵节要吃汤圆。~Tết Nguyên tiêu phải ăn bánh trôi.
端午节|Duānwǔjié|rieng|Tết Đoan Ngọ|端午节人们会吃粽子。~Tết Đoan Ngọ mọi người ăn bánh ú.
除夕|Chúxī|rieng|đêm giao thừa|除夕晚上，一家人在一起看春晚。~Đêm giao thừa cả nhà cùng xem Xuân Vãn.
春晚|Chūnwǎn|rieng|Gala đêm hội mùa xuân (Xuân Vãn)|每年春晚都有很多精彩的节目。~Xuân Vãn năm nào cũng có nhiều tiết mục đặc sắc.
"""),
texts=[dict(t="课文1", scene="六一儿童节，刘明、王一雪带刘小明到北京野生动物园看动物，他们先坐车进入猛兽区。", scene_vi="Ngày Quốc tế Thiếu nhi 1/6, Lưu Minh và Vương Nhất Tuyết đưa Lưu Tiểu Minh đến Vườn thú hoang dã Bắc Kinh, họ đi xe vào khu thú dữ trước.", narr=False, lines=T("""
刘小明>爸爸、妈妈，快看，熊和老虎都在这儿呢！|Bố ơi, mẹ ơi, mau nhìn kìa, gấu và hổ đều ở đây!
王一雪>小明，注意安全，不要一直大喊！|Tiểu Minh, chú ý an toàn, đừng la to mãi thế!
刘明>你们看，那个叫东北虎，是国家一级保护动物。那边树林里还有很多动物呢。|Mọi người xem, con kia gọi là hổ Đông Bắc, là động vật được bảo vệ cấp một quốc gia. Trong rừng cây bên kia còn nhiều động vật lắm.
刘小明>咱们都能看到吧？|Chúng ta đều xem được hết chứ ạ?
王一雪>对。景区的车每到一个动物区都会停一会儿，让人们能近距离看看这些动物。|Đúng. Xe của khu du lịch mỗi khi đến một khu động vật đều dừng một lúc, để mọi người được xem gần những con vật này.
刘明>真不错，这景区真大、真美！我知道北京野生动物园很大，可怎么也没想到这么大！|Hay thật, khu này vừa rộng vừa đẹp! Anh biết Vườn thú hoang dã Bắc Kinh rất rộng, nhưng thế nào cũng không ngờ lại rộng đến vậy!
王一雪>这里有几千只动物呢，能不大吗？现在是节假日，人多。小明，一会儿千万别跑丢了，我可不是开玩笑呢。|Ở đây có mấy nghìn con thú, sao mà không rộng được? Bây giờ là ngày lễ, đông người. Tiểu Minh, lát nữa nhất định đừng chạy lạc, mẹ không đùa đâu.
"""), q=Q("""
王一雪提醒小明什么？|注意安全，不要一直大喊。|Chú ý an toàn, đừng la to mãi.
小明在北京野生动物园里先看到了什么动物？|熊和老虎。|Gấu và hổ.
刘明觉得景区怎么样？|又大又美。|Vừa rộng vừa đẹp.
北京野生动物园有多少只动物？|几千只。|Mấy nghìn con.
""")),
 dict(t="课文2", scene="在王一飞家，王一飞夫妇邀请白家月、安妮和陈天中过中秋节。", scene_vi="Ở nhà Vương Nhất Phi, vợ chồng cô mời Bạch Gia Nguyệt, Annie và Trần Thiên Trung đón Tết Trung thu.", narr=False, lines=T("""
王一飞>来，大家快吃月饼，这儿还有葡萄、西瓜。|Nào, mọi người ăn bánh trung thu đi, ở đây còn có nho, dưa hấu.
杨同乐>这是今年的新茶，你们也尝尝。|Đây là trà mới năm nay, các em cũng nếm thử.
陈天中>好的。这茶闻着真香！|Vâng. Trà này ngửi thơm thật!
白家月>我还是第一次在中国过中秋节呢。|Đây là lần đầu tiên em đón Trung thu ở Trung Quốc.
安妮>我在加拿大时和中国朋友一起过过中秋节。我记得那天，外面的街道、剧院有很多演出活动。|Hồi ở Canada em đã đón Trung thu cùng bạn Trung Quốc. Em nhớ hôm đó ngoài đường phố, nhà hát có rất nhiều hoạt động biểu diễn.
王一飞>在中国，每年中秋节都会举办很多活动，而且这几年一年比一年热闹。对了，家月，今天是李文爷爷的生日，李文来不了了，你就多吃一块月饼吧。|Ở Trung Quốc, Trung thu năm nào cũng tổ chức nhiều hoạt động, mấy năm nay năm sau náo nhiệt hơn năm trước. À đúng rồi, Gia Nguyệt, hôm nay là sinh nhật ông của Lý Văn, Lý Văn không đến được, em ăn thêm một miếng bánh nhé.
白家月>谢谢，那我就不客气了。|Cảm ơn chị, vậy em không khách sáo nữa.
杨同乐>中秋节和生日赶在了一块儿，真巧、真好！中秋节多陪陪家人也是应该的。|Trung thu trùng với sinh nhật, thật trùng hợp, thật tốt! Trung thu ở bên gia đình nhiều hơn cũng là nên.
"""), q=Q("""
王一飞和杨同乐准备了什么？|月饼、葡萄、西瓜和茶。|Bánh trung thu, nho, dưa hấu và trà.
白家月以前在中国过过中秋节吗？|没有，这是第一次。|Chưa, đây là lần đầu.
在加拿大，安妮和中国朋友过中秋节时那里有什么活动？|外面的街道、剧院有很多演出活动。|Đường phố, nhà hát có nhiều hoạt động biểu diễn.
李文为什么没来？|因为今天是他爷爷的生日。|Vì hôm nay là sinh nhật ông cậu.
""")),
 dict(t="课文3", scene="中秋节的“反向团圆”", scene_vi="“Đoàn viên ngược chiều” dịp Trung thu", narr=True, lines=T("""
中秋节时中国人一般都会回家过节。|Dịp Trung thu người Trung Quốc thường về nhà đón Tết.
但是有些人由于工作需要，不能回家，只能一个人留在工作的地方过节。|Nhưng có người vì yêu cầu công việc không thể về nhà, chỉ có thể một mình ở lại nơi làm việc đón Tết.
周力就是这些人之中的一位。他是一名铁路工作人员，今年中秋假期，要负责铁路安全检查。|Chu Lực là một người trong số đó. Anh là nhân viên ngành đường sắt, kỳ nghỉ Trung thu năm nay phải phụ trách kiểm tra an toàn đường sắt.
周力的父母知道儿子这次不能回家后，就决定来一次“反向团圆”。|Bố mẹ Chu Lực biết con trai lần này không về được, liền quyết định làm một cuộc “đoàn viên ngược chiều”.
早上五点左右他们就坐上了高铁，大约七点就来到了儿子工作的城市。|Khoảng năm giờ sáng họ đã lên tàu cao tốc, khoảng bảy giờ đã đến thành phố nơi con trai làm việc.
在儿子家，他们做了一桌儿子爱吃的饭菜，有烤肉、烤鱼、饺子等等，还有西红柿鸡蛋汤。|Ở nhà con, họ nấu một bàn đầy món con thích, có thịt nướng, cá nướng, sủi cảo v.v., còn có canh cà chua trứng.
周力下班回家，看到一桌子饭菜和突然出现的父母，他感觉特别幸福。|Chu Lực tan làm về nhà, thấy cả bàn đồ ăn và bố mẹ bất ngờ xuất hiện, anh cảm thấy vô cùng hạnh phúc.
这个中秋节，地点变了，但爱没变。|Trung thu năm nay, địa điểm đã thay đổi, nhưng tình yêu thương thì không.
"""), q=Q("""
周力不能回家过中秋节，是因为什么？|工作需要，要负责铁路安全检查。|Vì yêu cầu công việc, phải phụ trách kiểm tra an toàn đường sắt.
“反向团圆”是什么意思？|父母去孩子工作的城市和孩子一起过节。|Bố mẹ đến thành phố con làm việc để đón Tết cùng con.
中秋节这天，周力的父母为儿子做了什么？|做了一桌儿子爱吃的饭菜。|Nấu một bàn món con thích.
周力为什么感觉特别幸福？|因为下班回家看到一桌子饭菜和突然出现的父母。|Vì tan làm về thấy cả bàn đồ ăn và bố mẹ bất ngờ xuất hiện.
""")),
 dict(t="课文4", scene="节日的美好记忆", scene_vi="Ký ức đẹp về ngày lễ", narr=True, lines=T("""
中国有很多节日，比如春节、元宵节、端午节、中秋节等。|Trung Quốc có nhiều ngày lễ, ví dụ Tết Nguyên đán, Tết Nguyên tiêu, Tết Đoan Ngọ, Tết Trung thu v.v.
作为一年里最重要的传统节日，春节对中国人来说有着特别的意义。|Là ngày lễ truyền thống quan trọng nhất trong năm, Tết Nguyên đán có ý nghĩa đặc biệt với người Trung Quốc.
春节到来时，人们不管在哪里，都想回家过年。|Khi Tết đến, dù ở đâu mọi người cũng muốn về nhà ăn Tết.
春节前也最忙，既要收拾房子、打扫卫生，又要准备各种美食。|Trước Tết cũng bận nhất, vừa phải dọn nhà, quét dọn vệ sinh, vừa phải chuẩn bị đủ món ngon.
除夕这天晚上，一家人一边吃年夜饭，一边看春晚。|Tối giao thừa, cả nhà vừa ăn cơm tất niên vừa xem Xuân Vãn.
零点一到，大家互相祝新年快乐，到处都是幸福的笑声。|Vừa đến không giờ, mọi người chúc nhau năm mới vui vẻ, đâu đâu cũng là tiếng cười hạnh phúc.
每当回忆起童年，我最美好的记忆很多也发生在过年时。|Mỗi khi nhớ lại tuổi thơ, nhiều ký ức đẹp nhất của tôi cũng diễn ra vào dịp Tết.
虽然现在已人到中年，离开了家，但是春节仍然是我最喜欢的节日，过年时也更想父母、兄弟姐妹。|Tuy giờ tôi đã đến tuổi trung niên, rời xa nhà, nhưng Tết vẫn là ngày lễ tôi thích nhất, dịp Tết càng nhớ bố mẹ, anh chị em hơn.
"""), q=Q("""
课文中没有提到哪个节日？|六一儿童节。|Ngày Quốc tế Thiếu nhi.
为什么说春节对中国人来说有着特别的意义？|因为它是一年里最重要的传统节日。|Vì đó là ngày lễ truyền thống quan trọng nhất trong năm.
春节到来时，人们会做什么？|回家过年，收拾房子、打扫卫生、准备各种美食。|Về nhà ăn Tết, dọn nhà, quét dọn, chuẩn bị món ngon.
春节为什么一直是他最喜欢的节日？|因为他童年最美好的记忆很多都发生在过年时。|Vì nhiều ký ức đẹp nhất tuổi thơ của anh diễn ra vào dịp Tết.
""")),
],
grammar=[
 G("zenmedou", "固定格式“怎么都/也+不/没……”", "Cấu trúc cố định “怎么都 / 也 + 不 / 没……”",
   "Biểu thị đã nghĩ mọi cách mà vẫn không đạt được kết quả nào đó; đôi khi dùng để bày tỏ sự ngạc nhiên, không ngờ: “thế nào cũng không…”.",
   [F("S:Chủ ngữ|kw:怎么都 / 怎么也|D:不 / 没|V:Vị ngữ", [
     ("我知道北京野生动物园很大，可|[怎么也]|没|想到这么大", "！", "Tôi biết vườn thú rất rộng, nhưng thế nào cũng không ngờ rộng đến vậy!"),
     ("她在包里找了半天，|[怎么都]|没|找到，真奇怪", "。", "Cô ấy tìm trong túi cả buổi mà thế nào cũng không thấy, lạ thật."),
     ("我们想看那只熊猫，在动物园等了两个多小时，可是它|[怎么都]|不|出来", "。", "Chúng tôi muốn xem con gấu trúc, đợi ở sở thú hơn hai tiếng mà nó thế nào cũng không chịu ra.")])]),
 G("yiyibiyi", "固定格式“一+量词+比+一+量词”", "Cấu trúc cố định “一 + lượng từ + 比 + 一 + lượng từ”",
   "Biểu thị so sánh giữa hai hay nhiều sự vật, nhấn mạnh cái sau hơn cái trước. Thường kết hợp với tính từ: “一 + lượng từ + 比 + 一 + lượng từ + tính từ” (… sau hơn … trước, càng ngày càng…).",
   [F("S:Chủ ngữ|kw:一+量词+比+一+量词|A:Tính từ", [
     ("这几年|[一年比一年]|热闹", "。", "Mấy năm nay năm sau náo nhiệt hơn năm trước."),
     ("夏天快到了，天气也|[一天比一天]|热", "。", "Mùa hè sắp đến, trời cũng ngày càng nóng."),
     ("这家店里的杯子|[一个比一个]|漂亮", "，我都不知道选哪个了。", "Cốc trong cửa hàng này cái nào cũng đẹp hơn cái nào, tôi chẳng biết chọn cái nào.")])]),
 G("dayue_zuoyou", "用“大约”“左右”表示概数", "Dùng “大约”, “左右” biểu thị số ước lượng",
   "“大约”, “左右” biểu thị ước chừng, không chắc chắn. Bài này dùng với từ chỉ thời gian: “大约” đứng trước từ chỉ thời gian, “左右” đứng sau.",
   [F("kw:大约|X:Thời gian|kw2:左右|V:Sự việc", [
     ("早上|五点|[左右]|他们就坐上了高铁", "，", "Khoảng năm giờ sáng họ đã lên tàu cao tốc,"),
     ("[大约]|七点||就来到了儿子工作的城市", "。", "khoảng bảy giờ đã đến thành phố con làm việc."),
     ("我中午|十二点|[左右]|到你们学校", "，和大家一起去食堂吃饭。", "Khoảng mười hai giờ trưa tôi đến trường các bạn, cùng mọi người đi ăn ở căng tin."),
     ("昨天飞机晚点，我晚上[大约]|十点半||才到家", "。", "Hôm qua máy bay trễ, khoảng mười giờ rưỡi tối tôi mới về đến nhà.")])]),
 G("zuowei", "介词“作为”", "Giới từ “作为”",
   "“作为” biểu thị thân phận nào đó của người hoặc tính chất nào đó của sự vật: “là, với tư cách là”. Không thể đứng một mình làm thành phần câu, phải kết hợp với từ ngữ phía sau.",
   [F("kw:作为|N:Thân phận / tính chất|V:Nội dung", [
     ("[作为]|一年里最重要的传统节日|春节对中国人来说有着特别的意义", "。", "Là ngày lễ truyền thống quan trọng nhất trong năm, Tết có ý nghĩa đặc biệt với người Trung Quốc."),
     ("[作为]|新产品|这个手机不仅样子好看，价格也不高", "。", "Là sản phẩm mới, chiếc điện thoại này không chỉ đẹp mà giá cũng không cao."),
     ("[作为]|好朋友|我们一直互相关心、互相帮助", "。", "Là bạn tốt, chúng tôi luôn quan tâm, giúp đỡ lẫn nhau.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["仍然", "已", "香", "之中", "有着", "出现"], [
   "西安也是一座【有着】三千多年历史的城市，欢迎您参观游玩。", "他【已】在中国生活二十年了，生活习惯和我们没什么不同。", "有妈妈细心照顾，孩子们每天都生活在幸福【之中】。",
   "妈妈终于【出现】在车站出口，孩子们开心极了。", "虽然遇到了很大困难，他【仍然】坚持下来了。", "这是什么咖啡？闻起来真【香】！"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["到来", "老虎", "喊", "回忆", "千万", "巧"], [
   "A：你去的那家动物园有【老虎】吗？ B：有，还有熊、大熊猫等好多种动物呢。", "A：虽然离开家已四十年，但我还会经常【回忆】起小时候在家时的生活。 B：我也是，年龄越大越想家。",
   "A：明天的活动你们一定要来，【千万】别忘了。 B：好的，放心吧，我们会来的。", "A：我刚才【喊】了你几遍，你都没看我。 B：对不起，我戴着耳机呢，没听见。",
   "A：没想到咱们在机场遇见了，真是太【巧】了。我去北京，你呢？ B：是啊，我也去北京出差。", "A：小雨，你的生日快到了。生日【到来】时，你想要什么礼物？ B：我想要一个大蛋糕。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["兄弟姐妹都离开了家", "很难见面", "小时候喜欢过节", "一家人聚在一起"], [
   "冬冬从小到大都喜欢过节，特别是春节和元宵节。【小时候喜欢过节】，是因为可以吃到很多好吃的。长大后，【兄弟姐妹都离开了家】，去外地上大学、工作。平时大家很忙，【很难见面】，但一到重要节日，在外地的兄弟姐妹就都回来了，和父母一起过节。【一家人聚在一起】，特别热闹，也特别开心。"], inline=False),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l13", items=[
   ("剧院", "今天晚上我们去剧院听音乐会。"), ("景区", "节假日的时候，长城景区的游客特别多。"), ("节假日", "节假日街上到处都是人，非常热闹。")]),
])
