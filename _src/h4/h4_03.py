# -*- coding: utf-8 -*-
# HSK 4上 – Bài 3: 手机扫一下
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[3] = dict(zh="手机扫一下", vi="Quét bằng điện thoại là xong",
intro="Trần Thiên Trung hỏi đường, học cách dùng WeChat, Alipay để quét mã thanh toán, mua sắm online; các bạn du học sinh trải nghiệm cuộc sống mới và tìm hiểu cách bảo vệ thông tin cá nhân khi dùng điện thoại.",
vocab=V("""
十字路口|shízì lùkǒu|cum|ngã tư|到了十字路口你往左转。~Đến ngã tư thì bạn rẽ trái.
直接|zhíjiē|tt|trực tiếp, thẳng|你直接去三楼找他吧。~Bạn cứ lên thẳng tầng ba tìm anh ấy.
转|zhuǎn|dong|rẽ, chuyển|前边路口向右转就到了。~Đến ngã rẽ phía trước rẽ phải là tới.
正好|zhènghǎo|pho|vừa đúng lúc, vừa khéo|你来得正好，我们正要吃饭。~Bạn đến đúng lúc, chúng tôi đang định ăn cơm.
熟悉|shúxi|dong|quen thuộc, thông thạo|我对这个城市还不太熟悉。~Tôi vẫn chưa quen thành phố này lắm.
正|zhèng|tt|chính, thẳng (hướng)|学校的大门是正南方向。~Cổng trường nhìn đúng hướng chính nam.
目的地|mùdìdì|dt|nơi đến, đích đến|还有十分钟就到目的地了。~Còn mười phút nữa là đến nơi.
下载|xiàzài|dong|tải xuống|你可以在手机上下载这个软件。~Bạn có thể tải phần mềm này về điện thoại.
进行|jìnxíng|dong|tiến hành|会议正在进行。~Cuộc họp đang được tiến hành.
支付|zhīfù|dong|chi trả, thanh toán|现在很多人用手机支付。~Bây giờ nhiều người thanh toán bằng điện thoại.
软件|ruǎnjiàn|dt|phần mềm, ứng dụng|这个学习软件很好用。~Phần mềm học tập này rất dễ dùng.
不仅|bùjǐn|lien|không những, không chỉ|她不仅会说中文，还会说日语。~Cô ấy không những nói được tiếng Trung mà còn nói được tiếng Nhật.
扫码|sǎomǎ|dong|quét mã|进门前请先扫码。~Trước khi vào vui lòng quét mã.
结账|jiézhàng|dong|tính tiền, thanh toán|服务员，我们要结账。~Phục vụ ơi, chúng tôi muốn tính tiền.
购物|gòuwù|dong|mua sắm|周末我常常和朋友去购物。~Cuối tuần tôi thường đi mua sắm với bạn.
订|dìng|dong|đặt (vé, phòng, hàng)|我已经订好了明天的机票。~Tôi đã đặt xong vé máy bay ngày mai.
快递|kuàidì|dt|chuyển phát nhanh, bưu phẩm|我的快递今天下午到。~Bưu phẩm của tôi chiều nay đến.
微信|Wēixìn|rieng|WeChat|你有微信吗？我们加一下吧。~Bạn có WeChat không? Kết bạn nhé.
支付宝|Zhīfùbǎo|rieng|Alipay|这家店可以用支付宝付钱。~Cửa hàng này có thể trả tiền bằng Alipay.
现金|xiànjīn|dt|tiền mặt|现在出门很少带现金。~Bây giờ ra ngoài ít khi mang tiền mặt.
网购|wǎnggòu|dong|mua sắm trực tuyến|她很喜欢网购衣服。~Cô ấy rất thích mua quần áo trên mạng.
寄|jì|dong|gửi (thư, bưu phẩm)|我想给妈妈寄一个礼物。~Tôi muốn gửi cho mẹ một món quà.
等|děng|tro|vân vân, v.v.|我喜欢苹果、香蕉等水果。~Tôi thích táo, chuối v.v.
货|huò|dt|hàng hóa|你订的货明天送到。~Hàng bạn đặt ngày mai giao tới.
甚至|shènzhì|lien|thậm chí|他忙得甚至忘了吃饭。~Anh ấy bận đến mức thậm chí quên cả ăn cơm.
改变|gǎibiàn|dong|thay đổi|这次旅行改变了我的想法。~Chuyến đi này đã thay đổi suy nghĩ của tôi.
手指|shǒuzhǐ|dt|ngón tay|动动手指就能买东西。~Động ngón tay là mua được đồ.
乱|luàn|pho|bừa bãi, linh tinh; lộn xộn|别乱花钱。~Đừng tiêu tiền linh tinh.
管|guǎn|dong|quản, kiểm soát|妈妈管得很严。~Mẹ quản rất nghiêm.
提供|tígōng|dong|cung cấp|酒店为客人提供早餐。~Khách sạn cung cấp bữa sáng cho khách.
身份证|shēnfènzhèng|dt|chứng minh thư, căn cước|坐火车要带身份证。~Đi tàu hỏa phải mang căn cước.
个人|gèrén|dt|cá nhân|这是我个人的想法。~Đây là suy nghĩ cá nhân của tôi.
能否|néngfǒu|dong|có thể… hay không|我不知道能否按时完成。~Tôi không biết có hoàn thành đúng hạn được không.
保护|bǎohù|dong|bảo vệ|我们要保护环境。~Chúng ta phải bảo vệ môi trường.
于是|yúshì|lien|thế là, vì vậy|天下雨了，于是我们回家了。~Trời mưa, thế là chúng tôi về nhà.
密码|mìmǎ|dt|mật khẩu|别把密码告诉别人。~Đừng nói mật khẩu cho người khác.
随便|suíbiàn|tt|tùy tiện, tùy ý|你想吃什么？——随便。~Bạn muốn ăn gì? — Gì cũng được.
技术|jìshù|dt|kỹ thuật, công nghệ|这家公司的技术很先进。~Công nghệ của công ty này rất tiên tiến.
法律|fǎlǜ|dt|pháp luật|每个人都应该遵守法律。~Mọi người đều nên tuân thủ pháp luật.
手段|shǒuduàn|dt|thủ đoạn, biện pháp|学习的手段越来越多了。~Phương tiện học tập ngày càng nhiều.
保证|bǎozhèng|dong|bảo đảm|我保证明天不迟到。~Tôi đảm bảo ngày mai không đến muộn.
网络|wǎngluò|dt|mạng internet|这里的网络不太好。~Mạng ở đây không tốt lắm.
"""),
texts=[dict(t="课文1", scene="一天，陈天中从学校出来迷路了，就向一位同学问路。", scene_vi="Một hôm, Trần Thiên Trung ra khỏi trường thì bị lạc đường, bèn hỏi đường một bạn học.", narr=False, lines=T("""
陈天中>请问，花园小区怎么走？|Xin hỏi, khu Hoa Viên đi thế nào?
同学>你往前走，到十字路口不要过马路，直接右转就到小区门口了。正好我也去那边，一起走吧。|Bạn đi thẳng, đến ngã tư thì đừng qua đường, rẽ phải luôn là tới cổng khu. Vừa hay mình cũng đi bên đó, đi cùng nhé.
陈天中>好的。我刚来中国，不熟悉路。北京真是太大了。|Được. Mình mới đến Trung Quốc, chưa quen đường. Bắc Kinh lớn quá.
同学>北京大是大，不过这边的路基本上都是正南正北、正东正西的，很好找。你也可以用手机地图，很容易就能找到目的地。|Bắc Kinh lớn thì lớn thật, nhưng đường bên này về cơ bản đều theo hướng chính nam chính bắc, chính đông chính tây, rất dễ tìm. Bạn cũng có thể dùng bản đồ trên điện thoại, rất dễ tìm được nơi cần đến.
陈天中>嗯，不过很多中文地名我还不认识。|Ừ, nhưng nhiều tên địa danh tiếng Trung mình vẫn chưa biết.
同学>没关系，你很快就会熟悉的。|Không sao, bạn sẽ quen nhanh thôi.
"""), q=Q("""
陈天中到十字路口后，应该怎么走？|直接右转。|Rẽ phải luôn.
陈天中为什么找不到花园小区了？|因为他刚来中国，不熟悉路。|Vì cậu mới đến Trung Quốc, chưa quen đường.
陈天中为什么没用手机地图？|因为很多中文地名他还不认识。|Vì nhiều tên địa danh tiếng Trung cậu vẫn chưa biết.
""")),
 dict(t="课文2", scene="中午下课后，白家月和陈天中在学校食堂相遇，两人边吃饭边聊天儿。", scene_vi="Trưa tan học, Bạch Gia Nguyệt và Trần Thiên Trung gặp nhau ở căng tin, vừa ăn vừa trò chuyện.", narr=False, lines=T("""
陈天中>前两天和李文喝咖啡时，他帮我下载了微信和支付宝，教我认识里边的汉字，还教我用手机进行支付。|Mấy hôm trước lúc uống cà phê với Lý Văn, cậu ấy giúp mình tải WeChat và Alipay, dạy mình nhận mặt chữ Hán trong đó, còn dạy mình thanh toán bằng điện thoại.
白家月>他也教了我怎么用这两个软件。|Cậu ấy cũng dạy mình cách dùng hai ứng dụng này.
陈天中>现在我不仅会扫码结账，还会用手机在网上购物了。昨天我就在网上订了一台电脑，今天下午一点送到。|Giờ mình không chỉ biết quét mã thanh toán mà còn biết mua sắm online bằng điện thoại. Hôm qua mình đặt một chiếc máy tính trên mạng, một giờ chiều nay giao tới.
白家月>学会了这些，我们在中国生活真是方便了不少。|Học được những thứ này, cuộc sống của chúng ta ở Trung Quốc thật sự tiện hơn nhiều.
陈天中>对。快递员要到了，我得马上回去！家月，明天见！|Đúng. Người giao hàng sắp tới rồi, mình phải về ngay! Gia Nguyệt, mai gặp nhé!
白家月>好的，天中，再见。|Ừ, Thiên Trung, tạm biệt.
"""), q=Q("""
李文帮陈天中下载了什么软件？|微信和支付宝。|WeChat và Alipay.
前几天李文帮陈天中做什么了？|帮他下载了微信和支付宝，教他认识里边的汉字，还教他用手机支付。|Giúp cậu tải WeChat, Alipay, dạy nhận chữ Hán trong đó và dạy thanh toán bằng điện thoại.
陈天中现在会用手机做什么了？|不仅会扫码结账，还会在网上购物了。|Không chỉ biết quét mã thanh toán mà còn biết mua sắm online.
陈天中为什么着急回去？|因为快递员快到了。|Vì người giao hàng sắp tới.
""")),
 dict(t="课文3", scene="生活新体验", scene_vi="Trải nghiệm cuộc sống mới", narr=True, lines=T("""
白家月和陈天中刚到北京时就发现，中国人在饭馆或超市结账时，几乎都用手机支付，只有他们用现金结账。|Vừa đến Bắc Kinh, Bạch Gia Nguyệt và Trần Thiên Trung đã phát hiện người Trung Quốc khi thanh toán ở quán ăn hay siêu thị hầu như đều dùng điện thoại, chỉ có họ trả bằng tiền mặt.
在李文的帮助下，白家月和陈天中也都学会了用手机支付、网购、寄快递等等。|Nhờ Lý Văn giúp đỡ, Bạch Gia Nguyệt và Trần Thiên Trung cũng đã học được cách thanh toán bằng điện thoại, mua sắm online, gửi chuyển phát nhanh v.v.
在中国网购，不仅选择多、价格不高，而且送货很快，很多留学生甚至改变了自己的购物习惯。|Mua sắm online ở Trung Quốc không chỉ nhiều lựa chọn, giá không cao mà giao hàng còn rất nhanh, nhiều du học sinh thậm chí đã thay đổi thói quen mua sắm của mình.
不过，由于网购太方便了，动动手指就能买到想要的东西，他们也开始担心自己在网购时会乱花钱。|Có điều, vì mua online quá tiện, động ngón tay là mua được thứ mình muốn, họ cũng bắt đầu lo mình sẽ tiêu tiền linh tinh khi mua online.
怎么才能管住自己不乱花钱呢？|Làm thế nào mới kiểm soát được bản thân không tiêu tiền bừa bãi đây?
"""), q=Q("""
白家月和陈天中发现中国人在饭馆吃饭有什么习惯？|结账时几乎都用手机支付。|Khi thanh toán hầu như đều dùng điện thoại.
白家月和陈天中学会用手机做什么了？|学会了用手机支付、网购、寄快递等等。|Thanh toán bằng điện thoại, mua sắm online, gửi chuyển phát nhanh v.v.
留学生为什么也喜欢网购？|因为在中国网购不仅选择多、价格不高，而且送货很快。|Vì mua online ở Trung Quốc nhiều lựa chọn, giá không cao và giao hàng nhanh.
留学生网购时会担心什么？|担心自己会乱花钱。|Lo mình sẽ tiêu tiền linh tinh.
""")),
 dict(t="课文4", scene="用手机时如何保护个人信息", scene_vi="Làm thế nào bảo vệ thông tin cá nhân khi dùng điện thoại", narr=True, lines=T("""
网上购物或者订票时，我们经常需要提供姓名、手机号、身份证号等个人信息。|Khi mua sắm trên mạng hoặc đặt vé, chúng ta thường phải cung cấp các thông tin cá nhân như họ tên, số điện thoại, số căn cước.
在提供这些信息时，我们也会担心：我的个人信息能否得到保护？|Khi cung cấp những thông tin này, chúng ta cũng lo lắng: thông tin cá nhân của tôi có được bảo vệ hay không?
于是，有人在网上说出了自己的担心，很快就有人给出了一些建议。|Thế là có người nói ra nỗi lo của mình trên mạng, rất nhanh đã có người đưa ra một số lời khuyên.
比如，别把密码随便告诉别人，不在网上发自己的车票、机票信息……|Ví dụ, đừng tùy tiện nói mật khẩu cho người khác, không đăng thông tin vé tàu, vé máy bay của mình lên mạng…
现在，很多国家也通过技术、法律等手段来保证个人信息安全。|Hiện nay, nhiều quốc gia cũng đảm bảo an toàn thông tin cá nhân bằng các biện pháp kỹ thuật, pháp luật v.v.
比如中国的网络安全法、个人信息保护法等就很好地保护了人们的个人信息。|Ví dụ Luật An ninh mạng, Luật Bảo vệ thông tin cá nhân của Trung Quốc đã bảo vệ tốt thông tin cá nhân của mọi người.
"""), q=Q("""
网上购物或者订票时，经常需要提供哪些信息？|姓名、手机号、身份证号等个人信息。|Họ tên, số điện thoại, số căn cước và các thông tin cá nhân khác.
人们为什么会担心个人信息安全问题？|因为网上购物或订票时需要提供很多个人信息。|Vì khi mua sắm hoặc đặt vé trên mạng phải cung cấp nhiều thông tin cá nhân.
国家会通过什么手段来保证个人信息安全？|通过技术、法律等手段。|Bằng các biện pháp kỹ thuật, pháp luật v.v.
""")),
],
grammar=[
 G("shishi", "转折复句“……×是×，就是/不过……”", "Câu phức chuyển ngoặt “× 是 ×，就是 / 不过……”",
   "“× 是 ×” là cấu trúc cố định, khẳng định một tình huống hay tính chất (“… thì đúng là …”); phía sau dùng “就是、不过” để chuyển ý hoặc bổ sung, chỉ ra hạn chế của vế trước.",
   [F("S:Chủ ngữ|A:×|kw:是|A2:×|kw2:就是 / 不过|V:Chuyển ý / bổ sung".replace("A2", "B"), [
     ("北京|大|[是]|大|[不过]|这边的路基本上都是正南正北、正东正西的，很好找", "。", "Bắc Kinh lớn thì lớn thật, nhưng đường bên này về cơ bản đều theo hướng chính nam chính bắc, chính đông chính tây, rất dễ tìm."),
     ("这个房子|便宜|[是]|便宜|[就是]|离我的公司太远了", "。", "Căn nhà này rẻ thì rẻ thật, chỉ là cách công ty tôi xa quá."),
     ("我们|想|[是]|想了|[就是]|没想出更好的办法", "。", "Chúng tôi nghĩ thì có nghĩ rồi, chỉ là chưa nghĩ ra cách nào hay hơn.")])]),
 G("bujin", "递进复句“不仅/不光……，还/而且……”", "Câu phức tăng tiến “不仅 / 不光……，还 / 而且……”",
   "Biểu thị quan hệ tăng tiến: vế sau là sự mở rộng hay bổ sung cho vế trước, ý nghĩa tiến thêm một bước. Bài này học dạng hai vế cùng một chủ ngữ: Chủ ngữ + 不仅/不光 (bùguāng)……，还/而且……",
   [F("S:Chủ ngữ|kw:不仅 / 不光|X:Vế 1|kw2:还 / 而且|V:Vế 2 (tiến thêm)", [
     ("现在我|[不仅]|会扫码结账|[还]|会用手机在网上购物了", "。", "Bây giờ tôi không chỉ biết quét mã thanh toán mà còn biết mua sắm online bằng điện thoại."),
     ("王老师|[不光]|教我们说中文|[而且]|带我们了解中国文化", "。", "Thầy Vương không chỉ dạy chúng tôi nói tiếng Trung mà còn đưa chúng tôi tìm hiểu văn hóa Trung Quốc."),
     ("现在很多书店|[不仅]|卖书|[还]|卖咖啡和奶茶", "。", "Bây giờ nhiều hiệu sách không chỉ bán sách mà còn bán cà phê và trà sữa.")])]),
 G("shenzhi", "连词“甚至”", "Liên từ “甚至”",
   "“甚至” (thậm chí) nhấn mạnh một tình huống nổi bật hơn, vượt ngoài dự đoán thông thường; thường đứng trước vế / thành phần được nhấn mạnh.",
   [F("X:Tình huống thông thường|kw:甚至|V:Tình huống vượt mức", [
     ("在中国网购，不仅选择多、价格不高，而且送货很快，很多留学生|[甚至]|改变了自己的购物习惯", "。", "Mua online ở Trung Quốc nhiều lựa chọn, giá không cao, giao hàng nhanh, nhiều du học sinh thậm chí thay đổi cả thói quen mua sắm."),
     ("高铁速度真快|[甚至]|还没看清楚，它就已经开过去了", "。", "Tàu cao tốc nhanh thật, thậm chí chưa kịp nhìn rõ nó đã chạy qua rồi."),
     ("这个小区真不错，有小花园、球场|[甚至]|还有一个超市", "。", "Khu dân cư này thật không tệ, có vườn hoa nhỏ, sân bóng, thậm chí còn có một siêu thị.")])]),
 G("yushi", "承接复句“……，于是……”", "Câu phức nối tiếp “……，于是……”",
   "Hai vế kể các hành động / sự việc liên tiếp theo thứ tự, “于是” đứng đầu vế sau: “thế là, vì vậy (nên)”. Giữa hai vế có quan hệ trước sau, nối tiếp về logic.",
   [F("X:Sự việc trước|kw:于是|V:Sự việc tiếp theo", [
     ("在提供这些信息时，我们也会担心：我的个人信息能否得到保护？|[于是]|有人在网上说出了自己的担心", "。", "Khi cung cấp những thông tin này, ta cũng lo: thông tin cá nhân có được bảo vệ không? Thế là có người nói ra nỗi lo của mình trên mạng."),
     ("她从小就想当医生|[于是]|上大学时就选择了学医", "。", "Cô ấy từ nhỏ đã muốn làm bác sĩ, vì vậy lên đại học chọn học y."),
     ("最近总感冒|[于是]|他决定病好后就开始锻炼身体", "。", "Dạo này hay bị cảm, thế là anh ấy quyết định khỏi bệnh sẽ bắt đầu rèn luyện thân thể.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["结账", "于是", "转", "寄", "正好"], [
   "丽丽去快递站拿快递时，又【寄】了一个快递。", "从这儿走到十字路口，再向左【转】，就是超市了。", "在十字路口等了半个小时，他们也没来，【于是】我就一个人去图书馆了。",
   "在商场购物的时候，我喜欢用信用卡【结账】。", "我们到电影院的时候，电影【正好】开始了。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["保证", "现金", "购物", "提供", "技术"], [
   "A：我用【现金】结账可以吗？ B：当然，这些一共125块。", "A：这个工作要求对网络【技术】很了解，你可以吗？ B：没问题，我做这方面的工作已经有五年了。",
   "A：你们能【保证】这些货下午就送到吗？ B：您放心，我们有“闪送”服务，下午两点前就能送到。", "A：这个商场特别漂亮，在这里【购物】很舒服。 B：是啊，周末过来走走、看看，累了还可以坐下来喝喝咖啡或者茶。",
   "A：您好，办入住需要您【提供】身份证和手机号后四位。 B：好的，这是我的身份证，手机号后四位是5063。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["马上给她提供帮助", "爱丽觉得太方便了", "第一次点外卖时", "爱丽刚来北京留学时"], [
   "在中国，用手机支付、网购和寄快递都很方便，所以很多人觉得自己快要离不开手机了。【爱丽刚来北京留学时】，还不会用中国人常用的手机App，她很着急。她的中国朋友知道后，【马上给她提供帮助】，教她怎么用，她很快就学会用手机支付和网购了。【第一次点外卖时】，不到40分钟，外卖员就把饭送来了，【爱丽觉得太方便了】。现在，她几乎每天都用手机点外卖或网购。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：网购真是太方便了！ B：方便是方便，______。", "方便是方便，就是有时候会乱花钱。"),
   ("A：她中文怎么说得这么好了？ B：她不仅每天认真听课，______。", "她不仅每天认真听课，还经常和中国朋友聊天儿。"),
   ("他太了解我了，______，他就知道我想做什么。（甚至 / 说话）", "他太了解我了，我甚至还没说话，他就知道我想做什么。"),
   ("我昨天一天都在看书，很累，______。（于是）", "我昨天一天都在看书，很累，于是很早就睡觉了。")]),
 opn("用词语造句", "Dùng từ cho sẵn đặt câu.", [
   ("结账", "吃完饭以后，我用手机扫码结账。"), ("密码", "别把手机密码告诉别人。"), ("身份证", "坐高铁的时候要带身份证。")]),
])
