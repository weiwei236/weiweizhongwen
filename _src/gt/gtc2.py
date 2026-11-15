# -*- coding: utf-8 -*-
# 发展汉语·初级综合(I) – Bài 23, 24
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[23] = dict(zh="今年冬天变冷了", en="The Winter Is Getting Colder This Year", vi="Mùa đông năm nay lạnh hơn rồi",
intro="Mùa đông năm nay rất đặc biệt: từ Bắc xuống Nam đều có tuyết, nhiệt độ rất thấp. Trái Đất đang lạnh đi hay ấm lên?",
vocab=V("""
特别|tèbié|tt|đặc biệt|今天是一个特别的日子。~Hôm nay là một ngày đặc biệt.
北方|běifāng|dt|miền Bắc, phương Bắc|北方的冬天很冷。~Mùa đông miền Bắc rất lạnh.
南方|nánfāng|dt|miền Nam, phương Nam|我家在越南南方。~Nhà tôi ở miền Nam Việt Nam.
下雪|xià xuě|cum|tuyết rơi|北京下雪了，真漂亮！~Bắc Kinh có tuyết rồi, đẹp thật!
雪|xuě|dt|tuyết|我从来没见过雪。~Tôi chưa bao giờ thấy tuyết.
场|cháng|lg|trận, cơn (mưa, tuyết, bệnh…)|昨天下了一场大雨。~Hôm qua có một trận mưa to.
气温|qìwēn|dt|nhiệt độ (không khí)|今天气温很高。~Hôm nay nhiệt độ rất cao.
低|dī|tt|thấp|晚上气温比较低。~Buổi tối nhiệt độ khá thấp.
零下|líng xià|cum|dưới 0 độ, âm|明天零下五度。~Ngày mai âm năm độ.
度|dù|dt|độ (nhiệt độ)|今天三十五度，太热了！~Hôm nay 35 độ, nóng quá!
左右|zuǒyòu|dt|khoảng, chừng|我十点左右到。~Tôi đến khoảng 10 giờ.
差不多|chàbuduō|pho|gần như, xấp xỉ|我们差不多一样高。~Chúng tôi cao gần như nhau.
老人|lǎorén|dt|người già|公园里有很多老人在锻炼。~Trong công viên có nhiều người già đang tập thể dục.
年|nián|dt|năm|我学汉语一年了。~Tôi học tiếng Hán một năm rồi.
寒冷|hánlěng|tt|giá lạnh, rét|这是最寒冷的一天。~Đây là ngày giá lạnh nhất.
人们|rénmen|dt|mọi người, người ta|春节的时候，人们都回家过年。~Dịp Tết mọi người đều về nhà ăn Tết.
突然|tūrán|tt|đột nhiên, bất ngờ|天突然黑了。~Trời đột nhiên tối sầm.
变|biàn|dong|thay đổi, trở nên|她变漂亮了。~Cô ấy trở nên xinh hơn.
专家|zhuānjiā|dt|chuyên gia|他是汉语专家。~Ông ấy là chuyên gia tiếng Hán.
地球|dìqiú|dt|Trái Đất|我们要保护地球。~Chúng ta phải bảo vệ Trái Đất.
暖|nuǎn|tt|ấm|春天来了，天气变暖了。~Mùa xuân đến, trời ấm lên rồi.
注意|zhùyì|dong|chú ý|过马路要注意安全。~Qua đường phải chú ý an toàn.
气候|qìhòu|dt|khí hậu|越南的气候很热。~Khí hậu Việt Nam rất nóng.
爱|ài|dong|hay, dễ (bị); thích|她爱感冒。~Cô ấy hay bị cảm.
锻炼|duànliàn|dong|rèn luyện, tập thể dục|我每天早上锻炼身体。~Sáng nào tôi cũng tập thể dục.
出门|chū mén|cum|ra ngoài, ra khỏi nhà|出门的时候别忘了带钥匙。~Lúc ra ngoài đừng quên mang chìa khóa.
季节|jìjié|dt|mùa|你最喜欢哪个季节？~Bạn thích mùa nào nhất?
下雨|xià yǔ|cum|mưa|外面下雨了，带把伞吧。~Ngoài trời mưa rồi, mang ô đi.
雨|yǔ|dt|mưa|这场雨下得很大。~Trận mưa này rất to.
正常|zhèngcháng|tt|bình thường|他的身体很正常。~Sức khỏe anh ấy bình thường.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
今年冬天很特别，从北方到南方，已经下了四场大雪，气温也非常低。|Mùa đông năm nay rất đặc biệt, từ miền Bắc đến miền Nam đã có bốn trận tuyết lớn, nhiệt độ cũng rất thấp.
在北京，冬天的最低气温一般在零下十度左右。|Ở Bắc Kinh, nhiệt độ thấp nhất mùa đông thường khoảng âm mười độ.
可是今年冬天才冷呢，最冷的一天差不多有零下十七度。|Nhưng mùa đông năm nay mới lạnh làm sao, ngày lạnh nhất gần âm mười bảy độ.
老人们都说，这是最近四十年最寒冷的冬天。|Các cụ già đều nói, đây là mùa đông giá lạnh nhất bốn mươi năm gần đây.
人们觉得冬天突然变冷了，可是有的专家说地球变暖了。|Mọi người thấy mùa đông đột nhiên lạnh đi, nhưng có chuyên gia nói Trái Đất đang ấm lên.
你们说，地球是变冷了，还是变暖了呢？|Các bạn nói xem, Trái Đất lạnh đi hay ấm lên?
"""), q=Q("""
今年冬天最冷的时候是多少度？|差不多零下十七度。|Gần âm 17 độ.
这样冷的冬天经常有吗？|不常有，这是最近四十年最寒冷的冬天。|Không thường có, là mùa đông lạnh nhất 40 năm.
""")),
 dict(t="课文二", scene="下课时，李老师和学生们聊天儿。", scene_vi="Giờ ra chơi, thầy Lý nói chuyện với học sinh.", narr=False, lines=T("""
李一民>现在天气冷了，大家要注意身体，别感冒了。|Bây giờ trời lạnh rồi, mọi người phải chú ý sức khỏe, đừng để bị cảm.
林娜>老师，阿明又感冒了，我觉得他还没习惯北京的气候。|Thưa thầy, A Minh lại bị cảm rồi, em thấy bạn ấy vẫn chưa quen khí hậu Bắc Kinh.
李一民>他现在怎么样了？|Bây giờ cậu ấy thế nào rồi?
林娜>他现在好点儿了。|Bây giờ bạn ấy đỡ hơn rồi.
李一民>你们怎么样？|Các em thế nào?
学生们>还可以。|Cũng được ạ.
林娜>以前我爱感冒。现在常常锻炼，不爱感冒了。|Trước đây em hay bị cảm. Bây giờ thường xuyên tập thể dục nên không hay bị cảm nữa.
李一民>出门的时候多穿点儿衣服，平时多吃水果，多喝水。|Ra ngoài thì mặc nhiều áo vào, ngày thường ăn nhiều hoa quả, uống nhiều nước.
学生们>谢谢老师！|Cảm ơn thầy!
"""), q=Q("""
阿明习惯北京的气候了吗？|还没习惯，他又感冒了。|Chưa quen, lại bị cảm.
阿明现在身体怎么样？|他现在好点儿了。|Đỡ hơn rồi.
林娜现在还爱感冒吗？|不爱感冒了，因为她常常锻炼。|Không hay bị cảm nữa vì thường tập luyện.
""")),
 dict(t="课文三", narr=False, lines=T("""
山田>阿明，最近泰国天气怎么样？|A Minh, dạo này thời tiết Thái Lan thế nào?
阿明>一般这个季节我们那儿不常下雨，可是最近也下了两场大雨。|Thường mùa này chỗ mình ít mưa, nhưng gần đây cũng có hai trận mưa to.
山田>冷吗？|Có lạnh không?
阿明>听妈妈说，今年很冷，很多人都穿棉衣了。|Nghe mẹ nói năm nay rất lạnh, nhiều người đều mặc áo bông rồi.
山田>是吗？以前也是这样吗？|Vậy à? Trước đây cũng như vậy à?
阿明>不是这样，以前这个季节不冷也不热，是最舒服的时候，今年很不正常。|Không phải, trước đây mùa này không lạnh cũng không nóng, là lúc dễ chịu nhất, năm nay rất bất thường.
"""), q=Q("""
今年冬天泰国气候怎么样？|下了两场大雨，很冷。|Có hai trận mưa to, rất lạnh.
今年泰国的气候跟以前一样吗？|不一样，以前不冷也不热，今年很不正常。|Không, năm nay rất bất thường.
"""))],
grammar=[
 G("zuoyou", "冬天的最低气温一般在零下十度左右。", "Số lượng + 左右: khoảng, chừng",
   "“Từ số lượng + 左右” chỉ nhiều hơn hoặc ít hơn con số đó một chút.",
   [F("S:Chủ ngữ|N:Số lượng|kw:左右", [("这件衣服|三百块钱|[左右]", "。", "Bộ quần áo này khoảng ba trăm tệ."), ("我们|十点|[左右]", "到学校。", "Khoảng 10 giờ chúng tôi đến trường."), ("今天|二十度|[左右]", "。", "Hôm nay khoảng hai mươi độ.")])]),
 G("cai3", "可是今年冬天才冷呢。", "才 (3) … 呢: nhấn mạnh",
   "“才” biểu thị nhấn mạnh, thường có “呢” ở cuối câu: … mới thật là …",
   [F("S:Chủ ngữ|kw:才|A:Vị ngữ|kw2:呢", [("这本书|[才]|有意思|[呢]", "。", "Quyển sách này mới thú vị chứ."), ("我的汉语一般，他的汉语|[才]|好|[呢]", "。", "Tiếng Hán của tôi bình thường, của anh ấy mới giỏi."), ("那是我同学，这|[才]|是我们老师|[呢]", "。", "Đó là bạn tôi, đây mới là thầy giáo chúng tôi.")])]),
 G("chabuduo", "最冷的一天差不多有零下十七度。", "差不多: gần như, xấp xỉ",
   "Phó từ, biểu thị chênh lệch rất ít, gần như; cũng có thể đứng một mình làm vị ngữ.",
   [F("S:Chủ ngữ|kw:差不多|V:Vị ngữ", [("这两条裤子|[差不多]|长", "。", "Hai chiếc quần này dài gần bằng nhau."), ("我|[差不多]|等了两个小时", "。", "Tôi đợi gần hai tiếng."), ("这两件衣服一样吗？|[差不多]|", "。", "Hai bộ này giống nhau không? – Gần như vậy.")])]),
 G("le3", "人们觉得冬天突然变冷了。", "了 (3) cuối câu: sự thay đổi trạng thái",
   "Trợ từ ngữ khí đặt cuối câu, biểu thị tình hình đã thay đổi. 还可以: tạm được, không tốt nhất cũng không tệ nhất.",
   [F("S:Câu|kw:了", [("已经十点|[了]", "。", "Đã 10 giờ rồi."), ("下雨|[了]", "。", "Mưa rồi."), ("今年冬天突然变冷|[了]", "。", "Mùa đông năm nay đột nhiên lạnh đi rồi."), ("他现在好点儿|[了]", "。", "Bây giờ anh ấy đỡ hơn rồi.")])],
   notes=["还可以: 今天天气还可以。/ 这儿的菜还可以。/ 我身体还可以。"]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["特别", "左右", "差不多", "突然", "注意", "气候", "锻炼", "季节", "正常", "低"], [
   "今天是我的生日，是一个【特别】的日子。", "从这儿到学校要二十分钟【左右】。", "这两个孩子【差不多】高。", "刚才天气还很好，【突然】下起雨来了。", "天冷了，要【注意】身体。",
   "我还不习惯北京的【气候】。", "我每天早上去公园【锻炼】身体。", "秋天是北京最好的【季节】。", "今年冬天这么冷，很不【正常】。", "晚上的气温比较【低】。"]),
 pick("二、选择“才”的意思", "“才” trong mỗi câu nghĩa là gì?", [
   (["mới (ít/sớm/rẻ)", "mới thật là (nhấn mạnh)"], ["这双鞋才一百块。【mới (ít/sớm/rẻ)】", "今年冬天才冷呢。【mới thật là (nhấn mạnh)】", "他的汉语才好呢。【mới thật là (nhấn mạnh)】", "现在才七点，还早呢。【mới (ít/sớm/rẻ)】"])]),
 opn("三、用所给词语回答问题", "Trả lời câu hỏi với từ cho sẵn.", [
   ("你每天几点起床？（左右）", "我每天七点左右起床。"), ("你们班有多少人？（差不多）", "我们班差不多有二十个人。"),
   ("你最近身体怎么样？（还可以）", "我最近身体还可以。"), ("天气怎么样了？（变……了）", "天气变冷了。")]),
 tf("四、根据课文判断对错", "Dựa vào bài khóa, phán đoán đúng / sai.", [
   ("今年冬天北京最冷的一天差不多是零下十七度。", True), ("老人们说今年冬天跟以前一样。", False), ("阿明已经习惯北京的气候了。", False),
   ("林娜现在不爱感冒了，因为她常常锻炼。", True), ("泰国这个季节一般常常下雨。", False)]),
 opn("五、说一说，写一写", "Giới thiệu thời tiết, khí hậu quê bạn (khoảng 60 chữ).", [
   ("你们国家的气候怎么样？现在是什么季节？天气怎么样？你最喜欢哪个季节？为什么？",
    "（参考）我的家乡在越南南方，一年只有两个季节：雨季和旱季。现在是雨季，常常下雨，气温在三十度左右。北京的冬天才冷呢，常常零下十度左右。我最喜欢秋天，因为不冷也不热，最舒服。")]),
])

B[24] = dict(zh="妈妈给我寄来了礼物", en="My Mom Has Sent Me a Gift", vi="Mẹ gửi quà cho tôi",
intro="Martin gửi email mời các bạn dự tiệc Lễ Tạ ơn ở Đại sứ quán Mỹ. Mẹ Martin còn gửi quà sang, nhưng Martin chưa biết bưu điện ở đâu.",
vocab=V("""
亲爱|qīn'ài|tt|thân yêu, thân mến|亲爱的妈妈，您好！~Mẹ thân yêu, con chào mẹ!
为了|wèile|gioi|để, vì (mục đích)|为了学好汉语，我来到中国。~Để học tốt tiếng Hán, tôi đã đến Trung Quốc.
庆祝|qìngzhù|dong|chúc mừng, ăn mừng|我们一起庆祝你的生日吧！~Chúng ta cùng mừng sinh nhật bạn nhé!
大使馆|dàshǐguǎn|dt|đại sứ quán|越南大使馆在哪儿？~Đại sứ quán Việt Nam ở đâu?
层|céng|lg|tầng|我住在五层。~Tôi ở tầng năm.
举行|jǔxíng|dong|tổ chức (hội nghị, lễ…)|晚会在哪儿举行？~Buổi tiệc tổ chức ở đâu?
晚会|wǎnhuì|dt|buổi dạ hội, tiệc tối|新年晚会很热闹。~Tiệc mừng năm mới rất náo nhiệt.
地址|dìzhǐ|dt|địa chỉ|请写一下你的地址。~Xin viết địa chỉ của bạn.
联系|liánxì|dong|liên lạc|有事给我打电话联系。~Có việc thì gọi điện liên lạc với tôi.
如果|rúguǒ|lien|nếu|如果明天下雨，我们就不去了。~Nếu mai mưa thì chúng ta không đi nữa.
活动|huódòng|dt|hoạt động|周末学校有很多活动。~Cuối tuần trường có nhiều hoạt động.
就|jiù|pho|thì (kết quả tự nhiên)|你不舒服就休息吧。~Bạn không khỏe thì nghỉ đi.
短信|duǎnxìn|dt|tin nhắn|到了给我发个短信。~Đến nơi thì nhắn tin cho tôi.
喂|wèi|than|alô, này|喂，你好！请问你找谁？~Alô, xin chào! Xin hỏi bạn tìm ai?
全|quán|pho|toàn bộ, đều|我们全去了。~Chúng tôi đi hết rồi.
让|ràng|dong|bảo, để cho|妈妈让我早点儿回家。~Mẹ bảo tôi về nhà sớm.
过|guò|dong|qua, đi qua|过了马路就是银行。~Qua đường là đến ngân hàng.
寄|jì|dong|gửi (thư, đồ)|我给朋友寄了一封信。~Tôi gửi cho bạn một lá thư.
邮局|yóujú|dt|bưu điện|邮局几点关门？~Bưu điện mấy giờ đóng cửa?
深|shēn|tt|đậm (màu); sâu|我喜欢深蓝色。~Tôi thích màu xanh đậm.
灰色|huīsè|dt|màu xám|他穿着一件灰色的上衣。~Anh ấy mặc một chiếc áo màu xám.
后边|hòubian|dt|phía sau|学校后边有一个公园。~Phía sau trường có một công viên.
书店|shūdiàn|dt|hiệu sách|我常去书店买书。~Tôi thường đi hiệu sách mua sách.
浅|qiǎn|tt|nhạt (màu)|这件衣服是浅黄色的。~Bộ quần áo này màu vàng nhạt.
绿色|lǜsè|dt|màu xanh lá|春天到处都是绿色。~Mùa xuân khắp nơi đều xanh.
上边|shàngbian|dt|phía trên, bên trên|桌子上边有一本书。~Trên bàn có một quyển sách.
护照|hùzhào|dt|hộ chiếu|别忘了带护照。~Đừng quên mang hộ chiếu.
忘不了|wàng bu liǎo|cum|không quên được|这次旅行我永远忘不了。~Chuyến du lịch này tôi mãi không quên được.
平安大街|Píng'ān Dàjiē|rieng|phố Bình An|我家在平安大街。~Nhà tôi ở phố Bình An.
感恩节|Gǎn'ēn Jié|rieng|Lễ Tạ ơn|感恩节是美国的节日。~Lễ Tạ ơn là ngày lễ của Mỹ.
国际大厦|Guójì Dàshà|rieng|Tòa nhà Quốc tế|国际大厦在友谊宾馆东边。~Tòa nhà Quốc tế ở phía đông khách sạn Hữu Nghị.
友谊宾馆|Yǒuyì Bīnguǎn|rieng|khách sạn Hữu Nghị|我在友谊宾馆等你。~Tôi đợi bạn ở khách sạn Hữu Nghị.
"""),
texts=[dict(t="课文一", scene="马丁给同学们发邮件，请大家参加他们的晚会。", scene_vi="Martin gửi email mời các bạn dự buổi tiệc tối.", narr=True, lines=T("""
亲爱的朋友：|Các bạn thân mến:
下个星期四是美国的感恩节。|Thứ Năm tuần sau là Lễ Tạ ơn của Mỹ.
为了庆祝这个重要的节日，美国大使馆在国际大厦四层举行晚会。|Để chúc mừng ngày lễ quan trọng này, Đại sứ quán Mỹ tổ chức tiệc tối ở tầng bốn Tòa nhà Quốc tế.
我们很希望您能来参加我们的晚会，也非常欢迎您带朋友一起来。|Chúng tôi rất mong bạn có thể đến dự tiệc, cũng rất hoan nghênh bạn đưa bạn bè cùng đến.
时间：11月25日晚上18:00到23:00|Thời gian: tối 25/11 từ 18:00 đến 23:00
联系人：马丁　地址：平安大街25号|Người liên hệ: Martin. Địa chỉ: số 25 phố Bình An
如果您愿意参加这个活动，就给我们发个短信、打个电话或者发个电子邮件。|Nếu bạn muốn tham gia hoạt động này, hãy nhắn tin, gọi điện hoặc gửi email cho chúng tôi.
"""), q=Q("""
下星期四美国大使馆有什么活动？|为了庆祝感恩节，美国大使馆举行晚会。|Đại sứ quán tổ chức tiệc mừng Lễ Tạ ơn.
活动在哪儿举行？|在国际大厦四层。|Ở tầng bốn Tòa nhà Quốc tế.
""")),
 dict(t="课文二", narr=False, lines=T("""
崔浩>喂，是马丁吗？我是崔浩。|Alô, Martin à? Mình là Thôi Hạo.
马丁>是你呀，你看到我的邮件了吗？你知道我们班有几个人去吗？|Là bạn à, bạn xem email của mình chưa? Bạn biết lớp mình có mấy người đi không?
崔浩>我们班所有的同学都去。|Tất cả các bạn lớp mình đều đi.
马丁>大家全去？|Mọi người đi hết à?
崔浩>对呀。|Đúng vậy.
马丁>太好了！|Tốt quá!
崔浩>对了，你能告诉我国际大厦在哪儿吗？|À, bạn có thể cho mình biết Tòa nhà Quốc tế ở đâu không?
马丁>友谊宾馆东边就是国际大厦。你知道友谊宾馆吧？|Phía đông khách sạn Hữu Nghị chính là Tòa nhà Quốc tế. Bạn biết khách sạn Hữu Nghị chứ?
崔浩>不知道。|Không biết.
马丁>这样吧，下午四点你让大家到我宿舍来，跟我一起过去，怎么样？|Thế này nhé, 4 giờ chiều bạn bảo mọi người đến ký túc xá mình, cùng mình đi qua đó, thế nào?
崔浩>好啊！|Được thôi!
马丁>晚上用不用我送你们回来呀？|Buổi tối có cần mình đưa các bạn về không?
崔浩>不用。|Không cần.
"""), q=Q("""
马丁的班谁去参加晚会？|所有的同学都去。|Tất cả các bạn đều đi.
国际大厦在哪儿？|在友谊宾馆东边。|Ở phía đông khách sạn Hữu Nghị.
""")),
 dict(t="课文三", narr=False, lines=T("""
马丁>我妈妈给我寄来了感恩节礼物，可是我还不知道邮局在哪儿。你知道吗？|Mẹ mình gửi quà Lễ Tạ ơn cho mình, nhưng mình vẫn chưa biết bưu điện ở đâu. Bạn biết không?
崔浩>知道。你看见前边那个深灰色的大楼了吗？|Biết. Bạn có thấy tòa nhà màu xám đậm phía trước kia không?
马丁>看见了。|Thấy rồi.
崔浩>大楼后边是一个书店和一个超市，邮局就在超市东边，那个楼是浅绿色的，上边还有英文，你一看就知道了。|Phía sau tòa nhà là một hiệu sách và một siêu thị, bưu điện ở ngay phía đông siêu thị, tòa nhà đó màu xanh lá nhạt, bên trên còn có chữ tiếng Anh, bạn nhìn là biết ngay.
马丁>谢谢了！|Cảm ơn nhé!
崔浩>不客气。你快去吧，别忘了把护照带去。|Không có gì. Bạn đi nhanh đi, đừng quên mang hộ chiếu.
马丁>忘不了。|Không quên được đâu.
"""), q=Q("""
马丁去邮局干什么？|妈妈给他寄来了礼物，他去邮局拿。|Đi nhận quà mẹ gửi.
邮局在哪儿？|在超市东边，那个楼是浅绿色的。|Ở phía đông siêu thị, tòa nhà màu xanh lá nhạt.
"""))],
grammar=[
 G("weile", "为了庆祝这个重要的节日，美国大使馆举行晚会。", "为了 + mục đích",
   "Giới từ “为了” biểu thị mục đích, thường đặt ở đầu câu.",
   [F("kw:为了|P:Mục đích|C:Hành động", [("[为了]|学好汉语，|我来到中国", "。", "Để học tốt tiếng Hán, tôi đến Trung Quốc."), ("[为了]|练习听力，|我每天都要听两个小时收音机", "。", "Để luyện nghe, ngày nào tôi cũng nghe đài hai tiếng."), ("学习是|[为了]|以后更好地工作", "。", "Học là để sau này làm việc tốt hơn.")])]),
 G("ruguo_jiu", "如果您愿意参加这个活动，就给我们发个短信。", "如果……，就……: nếu … thì …",
   "“如果” biểu thị giả thiết, phía sau thường dùng “就”. Có khi lược “如果”.",
   [F("kw:如果|C:Giả thiết|kw2:就|B:Kết quả", [("[如果]|你想参加晚会，|[就]|给我打电话", "。", "Nếu bạn muốn dự tiệc thì gọi cho tôi."), ("[(如果)]|天气好，我|[就]|去爬山", "。", "Nếu trời đẹp thì tôi đi leo núi."), ("[(如果)]|不太贵，|[就]|可以买", "。", "Nếu không đắt lắm thì có thể mua.")])]),
 G("shi_cunzai", "友谊宾馆东边就是国际大厦。", "Câu tồn tại (2): Nơi chốn + 是 + người/vật",
   "“是” có thể biểu thị sự tồn tại: ở vị trí đó là ai/cái gì.",
   [F("P:Nơi chốn|kw:是|N:Người / vật", [("大楼后边|[是]|书店和超市", "。", "Phía sau tòa nhà là hiệu sách và siêu thị."), ("林娜左边|[是]|山田", "。", "Bên trái Linna là Yamada.")])]),
 G("lai_qu", "我妈妈给我寄来了感恩节礼物。", "V + 来/去: bổ ngữ xu hướng đơn",
   "“来” chỉ động tác hướng về phía người nói, “去” ngược lại. Tân ngữ nơi chốn đặt GIỮA động từ và 来/去 (他回宿舍去了); tân ngữ thường thường đặt sau 来/去 (寄来了礼物).",
   [F("S:Chủ ngữ|V:Động từ|O:Nơi chốn|kw:来/去|X:", [("他|回|宿舍|[去]|了", "。", "Anh ấy về ký túc xá rồi."), ("他|下|楼|[来]|了", "。", "Anh ấy xuống lầu rồi."), ("你们|进|教室|[去]|吧", "。", "Các bạn vào lớp đi.")]),
    F("S:Chủ ngữ|V:Động từ|kw:来/去|O:Tân ngữ", [("妈妈给我|寄|[来]了|礼物", "。", "Mẹ gửi quà đến cho tôi."), ("别忘了把护照|带|[去]|", "。", "Đừng quên mang hộ chiếu đi.")], cap="Tân ngữ thường")]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["为了", "庆祝", "举行", "地址", "联系", "如果", "寄", "全", "让", "忘不了"], [
   "【为了】学好汉语，我每天看中文电影。", "我们一起去饭馆【庆祝】你的生日吧。", "晚会在国际大厦【举行】。", "请告诉我你的【地址】，我给你寄礼物。", "我们常常用电子邮件【联系】。",
   "【如果】你有时间，就来我家玩儿吧。", "我想给妈妈【寄】一张照片。", "我们班的同学【全】来了。", "老师【让】我们读课文。", "这次旅行我永远【忘不了】。"]),
 pick("二、选择“来”或“去”", "Chọn 来 hoặc 去.", [
   (["来", "去"], ["（你在楼下，我在楼上）你上【来】吧。", "他不在宿舍，回家【去】了。", "妈妈给我寄【来】了很多衣服。", "（我在教室里）请进【来】！", "你们先过【去】，我马上就到。"])]),
 opn("三、用“如果……就……”完成句子", "Hoàn thành câu với 如果……就…….", [
   ("如果明天不下雨，______。", "如果明天不下雨，我们就去爬山。"), ("如果你不舒服，______。", "如果你不舒服，就去医院看看吧。"), ("______，就给我打电话。", "如果你有问题，就给我打电话。")]),
 opn("四、根据课文回答问题", "Trả lời câu hỏi theo bài khóa.", [
   ("晚会什么时候举行？", "11月25日晚上18:00到23:00。"), ("马丁让崔浩做什么？", "让大家下午四点到他宿舍来，一起过去。"), ("邮局的大楼是什么颜色的？", "浅绿色的。"), ("崔浩让马丁别忘了什么？", "别忘了把护照带去。")]),
 opn("五、说一说，写一写", "Viết một email ngắn mời bạn bè tham gia một hoạt động.", [
   ("给朋友写一封邀请邮件。（亲爱的　为了　举行　时间　地址　如果……就……）",
    "（参考）亲爱的朋友：下星期六是我的生日。为了庆祝我的生日，我在学校旁边的饭馆举行晚会。时间：晚上六点到九点。地址：学院路12号。如果你愿意来，就给我发个短信。")]),
])
