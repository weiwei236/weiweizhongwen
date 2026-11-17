# -*- coding: utf-8 -*-
# HSK 3 – Bài 1: 我们去机场接你们
from gtb_gen import V, T, Q, F, G
B = {}

B[1] = dict(zh="我们去机场接你们", vi="Anh chị sẽ đến sân bay đón các em",
intro="Bạch Gia Nguyệt và Lý Văn bay sang Bắc Kinh. Ở sân bay, va li của Gia Nguyệt không thấy đâu, còn Lưu Minh và Vương Nhất Tuyết thì đang tìm cách nhận ra hai người bạn chưa từng gặp.",
vocab=V("""
以为|yǐwéi|dong|cho rằng, nghĩ rằng (mà thực tế không phải)|我以为今天是星期五。~Tôi cứ tưởng hôm nay là thứ Sáu.
像|xiàng|dong|giống, giống như|你长得很像你爸爸。~Bạn trông rất giống bố bạn.
长|zhǎng|dong|phát triển, lớn lên|这个孩子长得真快。~Đứa bé này lớn nhanh thật.
身高|shēngāo|dt|chiều cao|他的身高是一米七五。~Chiều cao của anh ấy là 1 mét 75.
米|mǐ|lg|mét (đơn vị đo lường)|我家离学校只有五百米。~Nhà tôi cách trường chỉ 500 mét.
瘦|shòu|tt|gầy, ốm|你最近瘦了很多。~Dạo này bạn gầy đi nhiều.
接|jiē|dong|đón|明天我去火车站接你。~Ngày mai tôi ra ga đón bạn.
行李|xíngli|dt|hành lý|你的行李多不多？~Hành lý của bạn có nhiều không?
丢|diū|dong|làm mất, bị mất|我的手机丢了。~Điện thoại của tôi mất rồi.
箱子|xiāngzi|dt|va li, cái thùng|这个箱子太重了。~Cái va li này nặng quá.
号码|hàomǎ|dt|số, mã số|你的手机号码是多少？~Số điện thoại của bạn là bao nhiêu?
好像|hǎoxiàng|pho|dường như, có vẻ như|外面好像下雨了。~Bên ngoài hình như mưa rồi.
重要|zhòngyào|tt|quan trọng|明天的考试很重要。~Kỳ thi ngày mai rất quan trọng.
着急|zháojí|tt|lo lắng, sốt ruột|别着急，我们慢慢找。~Đừng sốt ruột, chúng ta từ từ tìm.
护照|hùzhào|dt|hộ chiếu|出国要带护照。~Ra nước ngoài phải mang hộ chiếu.
服务台|fúwùtái|dt|quầy phục vụ|有问题可以去服务台问问。~Có vấn đề thì có thể ra quầy phục vụ hỏi.
应该|yīnggāi|nn|nên, phải (đáng lẽ)|你应该早点儿睡觉。~Bạn nên đi ngủ sớm một chút.
站|zhàn|dong|đứng|他站在门口等我。~Anh ấy đứng ở cửa đợi tôi.
中间|zhōngjiān|dt|ở giữa, trung gian|照片中间的人是我妈妈。~Người ở giữa bức ảnh là mẹ tôi.
短|duǎn|tt|ngắn|这条裤子有点儿短。~Cái quần này hơi ngắn.
头发|tóufa|dt|tóc|她的头发又黑又长。~Tóc cô ấy vừa đen vừa dài.
年轻|niánqīng|tt|trẻ, trẻ tuổi|我们的老师很年轻。~Cô giáo của chúng tôi rất trẻ.
发现|fāxiàn|dong|phát hiện, tìm thấy|我发现钱包不在包里。~Tôi phát hiện ví không có trong túi.
不见|bújiàn|dong|bị mất, không thấy|我的钥匙不见了。~Chìa khóa của tôi không thấy đâu nữa.
带|dài|dong|mang, dẫn, đưa|周末我带你去公园玩儿。~Cuối tuần tôi dẫn bạn đi công viên chơi.
帮助|bāngzhù|dong|giúp, giúp đỡ|谢谢你的帮助！~Cảm ơn sự giúp đỡ của bạn!
照片|zhàopiàn|dt|ảnh (chụp)|这张照片是在哪儿照的？~Bức ảnh này chụp ở đâu vậy?
"""),
texts=[dict(t="课文1", scene="在家里，刘明和王一雪在沙发上聊天儿。", scene_vi="Lưu Minh và Vương Nhất Tuyết đang trò chuyện trên ghế sofa ở nhà.", narr=False, lines=T("""
刘明>这是杨同乐吗？他怎么跟白家月在一起？|Đây là Dương Đồng Lạc à? Sao cậu ấy lại ở cùng Bạch Gia Nguyệt?
王一雪>他不是杨同乐，他叫李文，是白家月的好朋友。|Đó không phải Dương Đồng Lạc, cậu ấy tên Lý Văn, là bạn thân của Bạch Gia Nguyệt.
刘明>我还以为是同乐呢，他们看上去有点儿像。|Anh còn tưởng là Đồng Lạc chứ, hai người trông hơi giống nhau.
王一雪>是长得有点儿像，但是他比同乐高，身高有一米八。|Đúng là trông hơi giống, nhưng cậu ấy cao hơn Đồng Lạc, cao một mét tám.
刘明>看起来也比同乐瘦一点儿。|Trông cũng gầy hơn Đồng Lạc một chút.
王一雪>下个星期家月和李文要来北京，我去机场接他们。|Tuần sau Gia Nguyệt và Lý Văn sẽ đến Bắc Kinh, em ra sân bay đón họ.
刘明>他们哪天到北京？我跟你一起去机场接他们吧。|Họ đến Bắc Kinh ngày nào? Anh đi cùng em ra sân bay đón họ nhé.
"""), q=Q("""
刘明为什么以为李文是杨同乐？|因为他们看上去有点儿像。|Vì họ trông hơi giống nhau.
李文长什么样？|他比同乐高，身高有一米八，也比同乐瘦一点儿。|Cậu ấy cao hơn Đồng Lạc, cao 1m80, cũng gầy hơn một chút.
白家月什么时候来中国？|下个星期。|Tuần sau.
""")),
 dict(t="课文2", scene="在机场，李文和白家月在行李领取处。", scene_vi="Lý Văn và Bạch Gia Nguyệt đang ở khu vực nhận hành lý tại sân bay.", narr=False, lines=T("""
白家月>我的行李怎么还没出来？是不是丢了？|Sao hành lý của mình vẫn chưa ra? Có phải bị mất rồi không?
李文>你的行李箱是什么样的？|Va li của cậu trông thế nào?
白家月>是一个黑色的箱子，上面写着我的名字和电话号码。|Là một chiếc va li màu đen, trên đó có ghi tên và số điện thoại của mình.
李文>我好像在哪儿看到过这个箱子，是不是有人拿错了？|Hình như mình đã thấy chiếc va li này ở đâu đó, có phải ai đó cầm nhầm rồi không?
白家月>我们快找谁问一下吧，箱子里有不少重要的东西。|Chúng ta mau tìm ai đó hỏi thử đi, trong va li có khá nhiều đồ quan trọng.
李文>别着急，我们拿着护照和机票，去服务台问问吧。|Đừng sốt ruột, chúng ta cầm hộ chiếu và vé máy bay ra quầy phục vụ hỏi xem.
"""), q=Q("""
白家月的箱子是什么样的？|是一个黑色的箱子，上面写着她的名字和电话号码。|Là va li màu đen, có ghi tên và số điện thoại của cô ấy.
李文看到过白家月的箱子吗？|他好像在哪儿看到过。|Hình như cậu ấy đã thấy ở đâu đó.
他们现在要做什么？|他们要拿着护照和机票去服务台问问。|Họ sẽ cầm hộ chiếu và vé máy bay ra quầy phục vụ hỏi.
""")),
 dict(t="课文3", scene="在机场大厅，刘明和王一雪接机。", scene_vi="Lưu Minh và Vương Nhất Tuyết đang đón người tại sảnh sân bay.", narr=False, lines=T("""
刘明>飞机早就到了，你看见白家月他们了吗？|Máy bay đến từ lâu rồi, em thấy nhóm Bạch Gia Nguyệt chưa?
王一雪>没有，他们应该快出来了。|Chưa, chắc họ sắp ra rồi.
刘明>我们站到中间去吧，这样他们好找一些。|Chúng ta ra đứng ở giữa đi, như vậy họ dễ tìm hơn.
王一雪>你看那个高个子的人是李文吗？|Anh xem người cao cao kia có phải Lý Văn không?
刘明>你说的是哪个？那个穿着黑衣服的短头发的年轻人？|Em nói người nào? Cậu thanh niên tóc ngắn mặc áo đen kia à?
王一雪>对，那个人就是李文！你看，家月在他后面呢。|Đúng, người đó chính là Lý Văn! Anh xem, Gia Nguyệt ở phía sau cậu ấy kìa.
"""), q=Q("""
王一雪为什么说白家月他们应该快出来了？|因为飞机早就到了。|Vì máy bay đã đến từ lâu.
刘明看见的年轻人长什么样？|个子很高，短头发，穿着黑衣服。|Người cao, tóc ngắn, mặc áo đen.
王一雪怎么知道那个年轻人就是李文？|因为家月在他后面。|Vì Gia Nguyệt đi phía sau cậu ấy.
""")),
 dict(t="课文4", scene="在宾馆房间，李文在写日记。", scene_vi="Lý Văn đang viết nhật ký trong phòng khách sạn.", narr=True, lines=T("""
昨天我到北京了。|Hôm qua tôi đã đến Bắc Kinh.
虽然路上花了十几个小时，但是跟家月坐在一起，我觉得时间过得很快。|Tuy trên đường mất hơn mười tiếng, nhưng ngồi cùng Gia Nguyệt, tôi thấy thời gian trôi rất nhanh.
到机场的时候，家月发现行李箱不见了，我带她去服务台，帮助她找到了行李箱。|Lúc đến sân bay, Gia Nguyệt phát hiện va li không thấy đâu, tôi đưa cô ấy ra quầy phục vụ, giúp cô ấy tìm được va li.
走出机场的时候，已经八点多了，我们一出来就看见了王老师的姐姐，|Khi bước ra khỏi sân bay đã hơn tám giờ, chúng tôi vừa ra đã thấy chị gái của cô Vương,
她看起来比照片上年轻。|chị ấy trông trẻ hơn trong ảnh.
晚上，一雪姐带我们去吃了一家很好吃的中国菜。|Buổi tối, chị Nhất Tuyết đưa chúng tôi đi ăn ở một quán món Trung Quốc rất ngon.
"""), q=Q("""
李文为什么觉得时间过得很快？|因为他跟家月坐在一起。|Vì cậu ấy ngồi cùng Gia Nguyệt.
到机场的时候，白家月发现了什么问题？|她发现行李箱不见了。|Cô ấy phát hiện va li không thấy đâu.
王一雪带他们去做什么了？|带他们去吃了一家很好吃的中国菜。|Đưa họ đi ăn món Trung Quốc rất ngon.
"""))],
grammar=[
 G("kanshangqu", "固定短语“看上去/看起来”", "Cụm từ cố định “看上去 / 看起来”",
   "“看上去” và “看起来” dùng để miêu tả ngoại hình hoặc trạng thái của người hay sự vật theo những gì nhìn thấy (trông có vẻ…). Thường đứng sau chủ ngữ, trước tính từ / cụm vị ngữ.",
   [F("S:Chủ ngữ|kw:看上去 / 看起来|V:Miêu tả (tính từ, cụm từ)", [
     ("他们|[看上去]|有点儿像", "。", "Họ trông hơi giống nhau."),
     ("这些菜|[看起来]|都很好吃", "。", "Những món này trông đều rất ngon."),
     ("那个新来的老师|[看上去]|很年轻", "。", "Thầy giáo mới đến kia trông rất trẻ."),
     ("她|[看起来]|比照片上年轻", "。", "Chị ấy trông trẻ hơn trong ảnh.")])]),
 G("yiwen1", "疑问代词的非疑问用法（1）", "Cách dùng linh hoạt của đại từ nghi vấn (1) – chỉ cái không xác định",
   "Các đại từ nghi vấn “哪儿、什么、谁、哪” dùng trong câu trần thuật (không phải để hỏi), biểu thị nơi chốn, sự vật hoặc người không biết rõ hoặc không cần nói rõ: 哪儿 = ở đâu đó, 什么 = cái gì đó, 谁 = ai đó, 哪天 = hôm nào đó.",
   [F("S:Chủ ngữ|V:Động từ / phần trước|kw:哪儿 / 什么 / 谁 / 哪|X:Phần sau", [
     ("我好像|在|[哪儿]|看到过这个箱子", "。", "Hình như tôi đã thấy chiếc va li này ở đâu đó."),
     ("你|吃点儿|[什么]|再走吧", "。", "Bạn ăn chút gì đó rồi hãy đi."),
     ("我们||[哪天]|一起去踢足球吧", "。", "Hôm nào đó chúng ta cùng đi đá bóng nhé."),
     ("我们快|找|[谁]|问一下吧", "。", "Chúng ta mau tìm ai đó hỏi thử đi.")])]),
 G("duoxiang", "多项定语", "Định ngữ đa tầng",
   "Trước danh từ trung tâm có thể có nhiều định ngữ cùng lúc. Thứ tự thường gặp: thời gian / nơi chốn → hành động / trạng thái → đặc điểm. Cụm số lượng hoặc chỉ lượng (这/那 + lượng từ) có vị trí tương đối linh hoạt, có thể đứng trước hoặc sau định ngữ chỉ hành động / trạng thái.",
   [F("A:Số lượng / chỉ lượng|B:Hành động / trạng thái|C:Đặc điểm|N:Danh từ trung tâm", [
     ("那个|穿着黑衣服的|短头发的|年轻人", "", "cậu thanh niên tóc ngắn mặc áo đen kia"),
     ("那本|你昨天买的|很有意思的|书", "", "cuốn sách rất hay mà bạn mua hôm qua"),
     ("我那件|新买的|白色的|衣服", "", "chiếc áo màu trắng mới mua của tôi"),
     ("一个|上面写着名字的|黑色的|箱子", "", "một chiếc va li màu đen trên có ghi tên")])]),
],
test=dict(
 l2=["买箱子|找箱子|拿箱子", "男孩儿|女孩儿|最高的人", "接人|画画|等行李"],
 l3=["去考试|去国外|接朋友", "一个|两个|三个", "看照片|坐公交车|接新老师", "比照片上瘦|比照片上年轻|头发比照片上短"],
 r1=(["我们身高都是一米七，但是她比我瘦。", "别着急，我去服务台问问，会找到的。", "左边第二个。他跟我长得不像。", "那是我妹妹，我带她来的。", "当然。我们先坐公交车，然后换地铁。", "不客气，我可以看一下您的护照吗？"],
     ("你知道怎么去国家图书馆吗？", "E", "Bạn có biết đi Thư viện Quốc gia thế nào không? → E: Tất nhiên. Mình đi xe buýt trước rồi đổi tàu điện ngầm."),
     ["那是谁？我怎么没有见过她？", "照片上哪个是你哥哥？我没找到。", "谢谢您，这就是我的箱子。", "她看起来好像比你高一些。", "我的箱子不见了，里面有很多重要的东西。"]),
 r2=(["像", "以为", "重要", "帮助", "鞋", "应该"], ("中间那双（　　）是谁的？", "E", "Đôi giày ở giữa là của ai?"),
     ["我的手机在国外不能用，你有（　　）的事情可以给我妈妈打电话。", "箱子就放在这里吧，谢谢你们的（　　）。", "别着急，你的箱子（　　）可以找到。", "A：这是我爱人的弟弟，叫刘东，在电脑公司工作。\nB：他们长得很（　　）。", "A：你怎么这么高兴？\nB：我（　　）钱包丢了，但是在书包里找到了。"]),
 r3=[("照片上的人个子不高，穿着一件红色的上衣，头发很长也很黑。我好像在哪儿见过她。", "照片上的人：", "个子很高|长得很黑|他好像见过"),
     ("李先生以为护照不见了，着急地找了很长时间。没想到妻子一回家就帮他找到了，他忘了护照在箱子里了。", "关于李先生，可以知道什么？", "护照在妻子那儿|他的东西找到了|他的行李箱丢了"),
     ("你们看，照片里那个短头发的男孩儿就是我，我站在中间。我左边是一个头发很长的年轻女孩儿，她穿着黑色的上衣、红色的裤子，正在看书；我右边是一个个子很高的男孩儿，他穿着白色的上衣，手里拿着一个大包，看起来有点儿不高兴。",
      ("关于照片，可以知道什么？", "照片里有四个人|女孩儿穿着红裤子|男孩儿的个子不高"), ("关于他右边的男孩儿，可以知道什么？", "头发很短|站在中间|拿着一个大包"))],
 w1=["他看上去很着（jí）。", "这是我的（hù）照号码。", "这件事很（zhòng）要，你不要忘了。"],
 w2=[("以为", "我以为她们是姐妹，原来她们是好朋友。"), ("应该", "他的行李箱应该快出来了。"), ("好像", "她好像丢了什么重要的东西，看起来很着急。")],
 gl={"11": "那是谁？我怎么没有见过她？ – Đó là ai? Sao mình chưa từng gặp cô ấy? → D: Đó là em gái mình, mình dẫn nó đến.",
     "12": "Trong ảnh ai là anh trai bạn? Mình không tìm thấy. → C: Người thứ hai bên trái. Anh ấy trông không giống mình.",
     "13": "Cảm ơn anh, đây chính là va li của tôi. → F: Không có gì, tôi có thể xem hộ chiếu của chị được không?",
     "14": "Cô ấy trông hình như cao hơn bạn một chút. → A: Bọn mình đều cao 1m70, nhưng cô ấy gầy hơn mình.",
     "15": "Va li của tôi không thấy đâu, bên trong có nhiều đồ quan trọng. → B: Đừng sốt ruột, tôi ra quầy phục vụ hỏi, sẽ tìm được thôi.",
     "16": "重要的事情 – việc quan trọng: Có việc gì quan trọng thì bạn có thể gọi cho mẹ mình. → C 重要.",
     "17": "谢谢你们的帮助 – cảm ơn sự giúp đỡ của các bạn. → D 帮助.",
     "18": "应该可以找到 – chắc chắn (lẽ ra) sẽ tìm được. → F 应该.",
     "19": "长得很像 – trông rất giống nhau. → A 像.",
     "20": "我以为钱包丢了 – tôi cứ tưởng mất ví (thực ra không mất). → B 以为.",
     "21": "“我好像在哪儿见过她” – hình như tôi đã gặp cô ấy ở đâu đó → C.",
     "22": "Vợ vừa về đã giúp anh tìm thấy hộ chiếu → B: đồ của anh ấy đã tìm thấy.",
     "23": "Cô gái “穿着黑色的上衣、红色的裤子” → B: cô gái mặc quần đỏ.",
     "24": "Cậu bé bên phải “手里拿着一个大包” → C."}),
)
