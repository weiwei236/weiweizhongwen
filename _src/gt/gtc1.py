# -*- coding: utf-8 -*-
# 发展汉语·初级综合(I) – Bài 21, 22 (lớp Giao tiếp sơ cấp 1, bài 21–30)
from gtb_gen import V, T, Q, F, G, pool, match, pick, posq, tf, opn
B = {}

B[21] = dict(zh="我把袋子放在桌子上了", en="I Put the Bag on the Table", vi="Tôi để cái túi trên bàn rồi",
intro="Người Trung Quốc đi ăn chung thường một người trả tiền, lần này tôi mời, lần sau bạn mời. Còn “AA制” (chia đều tiền) thì sao?",
vocab=V("""
付钱|fù qián|cum|trả tiền|吃完饭，谁付钱？~Ăn xong, ai trả tiền?
付|fù|dong|trả, thanh toán|我用手机付钱。~Tôi trả tiền bằng điện thoại.
国家|guójiā|dt|đất nước, quốc gia|你去过几个国家？~Bạn đã đi mấy nước rồi?
自己|zìjǐ|dai|tự mình, bản thân|这件事我自己做。~Việc này tôi tự làm.
做法|zuòfǎ|dt|cách làm|这个菜的做法很简单。~Cách làm món này rất đơn giản.
AA制|AA zhì|dt|chia đều tiền (mỗi người tự trả phần mình)|我们今天AA制吧。~Hôm nay chúng ta chia đều nhé.
年轻人|niánqīng rén|dt|người trẻ, thanh niên|年轻人都喜欢上网。~Người trẻ đều thích lên mạng.
年轻|niánqīng|tt|trẻ|我们的老师很年轻。~Thầy giáo chúng tôi rất trẻ.
影响|yǐngxiǎng|dong|ảnh hưởng|别影响别人休息。~Đừng ảnh hưởng người khác nghỉ ngơi.
愿意|yuànyì|nn|bằng lòng, muốn|你愿意跟我一起去吗？~Bạn có muốn đi cùng tôi không?
大多数|dàduōshù|dt|đại đa số|大多数同学都住在宿舍。~Đa số các bạn đều ở ký túc xá.
习惯|xíguàn|dong|quen, thói quen|我还不习惯早上起床。~Tôi vẫn chưa quen dậy sớm.
结账|jié zhàng|cum|thanh toán, tính tiền|服务员，结账！~Phục vụ ơi, tính tiền!
咱们|zánmen|dai|chúng ta (gồm cả người nghe)|咱们一起去吃饭吧。~Chúng ta cùng đi ăn đi.
小费|xiǎofèi|dt|tiền boa|在中国不用给小费。~Ở Trung Quốc không cần cho tiền boa.
这些|zhèxiē|dai|những … này|这些书都是我的。~Những quyển sách này đều là của tôi.
打包|dǎ bāo|dong|gói mang về (đồ ăn thừa)|这个菜没吃完，打包吧。~Món này ăn không hết, gói về đi.
把|bǎ|gioi|(giới từ, đưa tân ngữ lên trước động từ)|请把门关上。~Hãy đóng cửa lại.
饭盒|fànhé|dt|hộp cơm|我把饭盒放在包里了。~Tôi để hộp cơm trong túi rồi.
放|fàng|dong|đặt, để|书放在哪儿？~Sách để ở đâu?
袋子|dàizi|dt|cái túi|给我一个袋子，好吗？~Cho tôi một cái túi được không?
零钱|língqián|dt|tiền lẻ|你有零钱吗？~Bạn có tiền lẻ không?
收|shōu|dong|nhận, thu|这家店不收现金。~Cửa hàng này không nhận tiền mặt.
所有|suǒyǒu|tt|tất cả|所有的同学都来了。~Tất cả các bạn đều đến rồi.
宾馆|bīnguǎn|dt|khách sạn, nhà khách|我们住在学校旁边的宾馆。~Chúng tôi ở khách sạn cạnh trường.
酒吧|jiǔbā|dt|quán bar|周末我们去酒吧听音乐。~Cuối tuần chúng tôi đi bar nghe nhạc.
有的|yǒude|dai|có cái, có người, một số|有的同学喜欢唱歌，有的喜欢跳舞。~Có bạn thích hát, có bạn thích nhảy.
清楚|qīngchu|tt|rõ ràng, rõ|老师说得很清楚。~Thầy nói rất rõ ràng.
慢|màn|tt|chậm|请说慢一点儿。~Xin nói chậm một chút.
桌子|zhuōzi|dt|cái bàn|桌子上有一杯水。~Trên bàn có một cốc nước.
拿|ná|dong|cầm, lấy|我去拿一下我的书。~Tôi đi lấy sách một chút.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
中国人一起吃饭的时候，一般是一个人付钱，这次我请客，下次他请客。|Người Trung Quốc ăn cùng nhau thường một người trả tiền, lần này tôi mời, lần sau anh ấy mời.
很多国家跟中国不一样，大家一起喝完咖啡、吃完饭以后，自己付自己的钱。|Nhiều nước không giống Trung Quốc, mọi người uống cà phê, ăn cơm xong thì ai trả phần người nấy.
这种做法，中国人叫“AA制”。|Cách làm này, người Trung Quốc gọi là “AA制”.
“AA制”到了中国，对年轻人影响很大，|“AA制” đến Trung Quốc, ảnh hưởng rất lớn đến người trẻ,
很多年轻人也愿意这么做，但是大多数中国人还不习惯。|nhiều người trẻ cũng muốn làm như vậy, nhưng đại đa số người Trung Quốc vẫn chưa quen.
"""), q=Q("""
大家一起吃饭，付钱的时候中国人一般怎么做？|一般是一个人付钱，这次我请客，下次他请客。|Thường một người trả, lần này tôi mời, lần sau người kia mời.
中国人都习惯AA制吗？|不，很多年轻人愿意，但是大多数中国人还不习惯。|Không, nhiều người trẻ muốn nhưng đa số chưa quen.
""")),
 dict(t="课文二", scene="在饭馆", scene_vi="Ở nhà hàng", narr=False, lines=T("""
林娜>服务员，结账！|Phục vụ ơi, tính tiền!
服务员>一共180块钱。|Tổng cộng 180 tệ.
林娜>咱们六个人AA制，好吗？|Sáu người chúng ta chia đều nhé?
大家>好，每人30，再给点儿小费。|Được, mỗi người 30, cho thêm ít tiền boa.
林娜>这些菜请帮我们打包，把饭盒都放在袋子里。|Những món này xin gói giúp chúng tôi, để hết hộp cơm vào túi.
服务员>没问题。|Không vấn đề gì.
林娜>这是200块钱，零钱不用找了，是小费。|Đây là 200 tệ, tiền lẻ không cần thối, là tiền boa.
服务员>我们不收小费。|Chúng tôi không nhận tiền boa.
林娜>不收小费？所有的饭馆都不收小费吗？|Không nhận tiền boa? Tất cả nhà hàng đều không nhận à?
服务员>应该是这样吧。|Chắc là vậy.
林娜>宾馆和酒吧呢？|Còn khách sạn và quán bar thì sao?
服务员>一般也不收，是不是有的地方收，我不太清楚。|Thường cũng không nhận, có chỗ nào nhận hay không thì tôi không rõ lắm.
"""), q=Q("""
林娜他们每人付多少钱？|每人30块钱。|Mỗi người 30 tệ.
中国饭馆服务员一般收小费吗？|不收小费。|Không nhận tiền boa.
""")),
 dict(t="课文三", narr=False, lines=T("""
林娜>日本人都很习惯AA制吗？|Người Nhật đều rất quen AA chế à?
山田>当然习惯了。|Đương nhiên quen rồi.
林娜>我觉得大多数中国人不太习惯AA制，他们常一个人请客。|Mình thấy đa số người Trung Quốc không quen AA chế lắm, họ thường một người mời.
山田>他们经常这次你请客，下次他请客，这样也不错，和AA制一样。|Họ thường lần này bạn mời, lần sau người kia mời, thế cũng hay, giống như AA chế.
林娜>我们也要慢慢习惯中国人的做法。|Chúng ta cũng phải từ từ quen với cách làm của người Trung Quốc.
山田>我看见你打包了，你把东西放在哪儿了？|Mình thấy bạn gói đồ mang về rồi, bạn để đồ ở đâu rồi?
林娜>我把袋子放在旁边的桌子上了，我去拿。|Mình để cái túi trên bàn bên cạnh rồi, mình đi lấy.
"""), q=Q("""
日本人习惯AA制吗？|当然习惯了。|Đương nhiên quen.
林娜已经习惯中国人的做法了吗？|还没有，她说要慢慢习惯。|Chưa, cô ấy nói phải từ từ quen.
林娜把袋子放在哪儿了？|她把袋子放在旁边的桌子上了。|Để trên bàn bên cạnh.
"""))],
grammar=[
 G("gen_yiyang", "很多国家跟中国不一样。", "A 跟(和) B 一样 / 不一样",
   "“A跟(和)B不一样” biểu thị hai sự vật khác nhau; “A跟(和)B一样” biểu thị không khác nhau.",
   [F("A:A|kw:跟/和|B:B|kw2:(不)一样", [
      ("我的习惯|[跟]|他的习惯|[不一样]", "。", "Thói quen của tôi khác thói quen của anh ấy."),
      ("这本书|[跟]|那本书|[不一样]", "。", "Quyển sách này khác quyển kia."),
      ("我的兴趣|[跟]|她的|[一样]", "。", "Sở thích của tôi giống của cô ấy.")])],
   prac=["A:你的手机跟我的一样吗？\nB:{不一样}，我的是新的。", "A:越南菜和中国菜一样吗？\nB:{越南菜和中国菜不一样}。"]),
 G("haoma", "咱们六个人AA制，好吗？", "……，好吗？ – hỏi ý kiến người khác",
   "Người nói nêu ý kiến/đề nghị trước rồi dùng “好吗” để hỏi ý người nghe. Đồng ý: 好 / 好的 / 好啊 / 行. Không đồng ý thì thường nói ý kiến của mình, ít khi chỉ nói “不好”, “不行”.",
   [F("C:Đề nghị|kw:好吗", [("我们一起吃饭，|[好吗]", "？", "Chúng ta cùng ăn cơm nhé?"), ("我用一下你的自行车，|[好吗]", "？", "Tôi mượn xe đạp của bạn một chút nhé?")])],
   notes=["A：我用一下你的自行车，好吗？ B：上午不行，我要去一趟书店。– Buổi sáng thì không được, tôi phải đi hiệu sách."]),
 G("ba1", "把饭盒都放在袋子里。", "Câu chữ 把 (1): S + 把 + O1 + V + 在 + O2",
   "Thông qua một động tác làm cho O1 thay đổi vị trí, đến nằm ở O2. Từ phủ định 不/没/别 đặt TRƯỚC 把.",
   [F("S:Chủ ngữ|kw:把|O:O1|V:Động từ|kw2:在|P:O2 (vị trí)", [
      ("我|[把]|词典|放|[在]|桌子上了", "。", "Tôi để quyển từ điển trên bàn rồi."),
      ("我|[把]|自行车|放|[在]|家里了", "。", "Tôi để xe đạp ở nhà rồi."),
      ("我|[把]|袋子|放|[在]|旁边的桌子上了", "。", "Tôi để cái túi trên bàn bên cạnh rồi.")]),
    F("S:Chủ ngữ|kw:不/没/别|kw2:把|O:O1|V:V + 在|P:O2", [
      ("我|[没]|[把]|钱|放在|家里", "。", "Tôi không để tiền ở nhà."),
      ("我|[不想]|[把]|自行车|放在|教室前边", "。", "Tôi không muốn để xe đạp trước lớp học."),
      ("|[别]|[把]|自行车|放在|桌子上", "。", "Đừng để xe đạp lên bàn.")], cap="Phủ định đặt trước 把")],
   prac=["A:你的书呢？\nB:我{把书放在宿舍里了}。", "A:手机放在哪儿？\nB:{别把手机放在桌子上}，放在包里吧。"]),
],
ex=[
 pick("一、选择正确的拼音", "Đọc kỹ từ, chọn phiên âm đúng.", [
   (["fù qián", "fū qián"], ["付钱【fù qián】"]), (["xià cì", "xiā cì"], ["下次【xià cì】"]), (["xíguàn", "xīguàn"], ["习惯【xíguàn】"]),
   (["jié zhàng", "jiē zhàng"], ["结账【jié zhàng】"]), (["zuòfǎ", "zòufǎ"], ["做法【zuòfǎ】"]), (["suǒyǒu", "suóyǒu"], ["所有【suǒyǒu】"]),
   (["zhèxiē", "zhēxié"], ["这些【zhèxiē】"]), (["xiǎofèi", "xiāofèi"], ["小费【xiǎofèi】"]), (["zhuōzi", "zhōuzi"], ["桌子【zhuōzi】"]), (["zìjǐ", "cìjì"], ["自己【zìjǐ】"])]),
 opn("二、根据课文内容填空", "Điền vào chỗ trống theo nội dung bài khóa.", [
   ("很多国家的人（　　）“AA制”，他们常常自己付（　　）的钱。", "习惯 / 自己"), ("大家一起吃饭的时候，中国人经常（　　）付钱。", "一个人"),
   ("林娜认为中国人（　　）习惯“AA制”。", "不太"), ("在中国，饭馆服务员（　　）收小费。", "不 / 一般不"),
   ("日本人很（　　）“AA制”。", "习惯"), ("（　　）认为外国人应该慢慢习惯中国人的做法。", "林娜")]),
 pool("四、选择适当的词语填空", "Chọn từ thích hợp điền vào chỗ trống.", ["下次", "习惯", "把", "慢慢", "清楚", "拿", "自己", "所有", "一样", "影响"], [
   "这是我【自己】的事，我自己知道怎么办。", "别着急，请你【慢慢】说。", "我们班二十个人，今天【所有】的人都来了。", "这次我一个人去，【下次】我们一起去。",
   "这些东西你都要【拿】走吗？", "别【把】手机放在桌子上。", "我还不【习惯】吃中国菜。", "她的帽子跟我的【一样】。", "这件事对我【影响】很大。", "我不太【清楚】他来不来。"]),
 opn("五、把下面的句子改写成“把”字句", "Viết lại các câu sau thành câu chữ 把.", [
   ("书你放在桌子上。", "你把书放在桌子上。"), ("手机你放在背包里吧。", "你把手机放在背包里吧。"), ("词典我没放在桌子上。", "我没把词典放在桌子上。"),
   ("笔你放在哪儿了？", "你把笔放在哪儿了？"), ("你的自行车我放在宿舍前边了。", "我把你的自行车放在宿舍前边了。")]),
 opn("六、用“有的”完成句子", "Hoàn thành câu với “有的”.", [
   ("我的同学，______，______。", "我的同学，有的是韩国人，有的是日本人。"), ("我有很多书，______，______。", "我有很多书，有的是中文书，有的是英文书。"),
   ("在中国，______，______。", "在中国，有的人习惯AA制，有的人不习惯。"), ("这些东西______，______。", "这些东西有的是我的，有的是我同屋的。")]),
 opn("七、说一说，写一写", "Viết đoạn văn ngắn.", [
   ("你认为“AA制”怎么样？在你们国家，朋友们在一起吃饭要“AA制”吗？你觉得“AA制”好不好？为什么？",
    "（参考）在我们国家，年轻人常常AA制，跟家人一起吃饭的时候不用AA制。我觉得AA制挺好的，大家自己付自己的钱，很方便。可是中国人的做法也不错，这次我请客，下次你请客，和AA制一样。")]),
])

B[22] = dict(zh="我的自行车是红色的", en="My Bike Is Red", vi="Xe đạp của tôi màu đỏ",
intro="Mẹ Linna từ Pháp sang thăm, mang cho cô nhiều đồ ăn và quần áo. Hai mẹ con đi mua áo. Nhưng xe đạp của Linna lại bị mất…",
vocab=V("""
黄色|huángsè|dt|màu vàng|我喜欢黄色的衬衫。~Tôi thích áo sơ mi màu vàng.
黄|huáng|tt|vàng|秋天的树叶黄了。~Lá cây mùa thu vàng rồi.
衬衫|chènshān|dt|áo sơ mi|这件衬衫多少钱？~Chiếc áo sơ mi này bao nhiêu tiền?
蓝色|lánsè|dt|màu xanh lam|天是蓝色的。~Bầu trời màu xanh lam.
蓝|lán|tt|xanh lam|今天的天很蓝。~Hôm nay trời rất xanh.
上衣|shàngyī|dt|áo (mặc ngoài)|这件上衣有点儿长。~Chiếc áo này hơi dài.
条|tiáo|lg|(lượng từ cho vật dài: quần, váy, đường, cá…)|我买了一条裤子。~Tôi mua một chiếc quần.
黑色|hēisè|dt|màu đen|他穿着一件黑色的上衣。~Anh ấy mặc một chiếc áo màu đen.
黑|hēi|tt|đen|天黑了，我们回家吧。~Trời tối rồi, chúng ta về nhà thôi.
裤子|kùzi|dt|cái quần|这条裤子太短了。~Chiếc quần này ngắn quá.
那些|nàxiē|dai|những … kia|那些人是我的同学。~Những người kia là bạn học của tôi.
尝|cháng|dong|nếm, thử|你尝尝我做的菜。~Bạn nếm thử món tôi nấu đi.
丢|diū|dong|mất, đánh mất|我的钱包丢了。~Ví tiền của tôi mất rồi.
有点儿|yǒudiǎnr|pho|hơi, có chút (thường điều không vừa ý)|今天有点儿冷。~Hôm nay hơi lạnh.
生气|shēng qì|dong|tức giận|你别生气了。~Bạn đừng giận nữa.
好看|hǎokàn|tt|đẹp, ưa nhìn|这件衣服真好看！~Bộ quần áo này đẹp thật!
颜色|yánsè|dt|màu sắc|你喜欢什么颜色？~Bạn thích màu gì?
那边|nàbian|dai|bên kia, đằng kia|洗手间在那边。~Nhà vệ sinh ở đằng kia.
试衣间|shìyījiān|dt|phòng thử đồ|请问，试衣间在哪儿？~Xin hỏi phòng thử đồ ở đâu?
瘦|shòu|tt|chật (quần áo); gầy|这件衣服有点儿瘦。~Bộ này hơi chật.
短|duǎn|tt|ngắn|我的头发很短。~Tóc tôi rất ngắn.
换|huàn|dong|đổi, thay|能换一件大点儿的吗？~Có thể đổi một chiếc to hơn không?
肥|féi|tt|rộng (quần áo)|这条裤子太肥了。~Chiếc quần này rộng quá.
正好|zhènghǎo|tt|vừa đúng, vừa vặn|这双鞋我穿正好。~Đôi giày này tôi đi vừa đúng.
双|shuāng|lg|đôi|我想买一双鞋。~Tôi muốn mua một đôi giày.
鞋|xié|dt|giày|这双鞋很舒服。~Đôi giày này rất êm.
便宜|piányi|tt|rẻ|这儿的水果很便宜。~Hoa quả ở đây rất rẻ.
会|huì|nn|sẽ, có thể (khả năng)|明天会下雨吗？~Mai có mưa không nhỉ?
记|jì|dong|nhớ, ghi nhớ|你记一下我的电话号码。~Bạn ghi nhớ số điện thoại của tôi nhé.
错|cuò|tt|sai|对不起，我说错了。~Xin lỗi, tôi nói sai rồi.
样子|yàngzi|dt|kiểu dáng, hình dáng|这个包的样子很好看。~Kiểu dáng chiếc túi này rất đẹp.
红色|hóngsè|dt|màu đỏ|中国人喜欢红色。~Người Trung Quốc thích màu đỏ.
红|hóng|tt|đỏ|她的脸红了。~Mặt cô ấy đỏ lên.
旧|jiù|tt|cũ|这是我的旧手机。~Đây là điện thoại cũ của tôi.
算了|suàn le|cum|thôi, bỏ đi|太远了，算了，不去了。~Xa quá, thôi không đi nữa.
"""),
texts=[dict(t="课文一", narr=True, lines=T("""
我妈妈从法国来看我了。她给我带了很多好吃的，还带了一些衣服。|Mẹ tôi từ Pháp sang thăm tôi. Mẹ mang cho tôi nhiều đồ ăn ngon, còn mang ít quần áo.
她给我买了一件黄色的衬衫、一件蓝色的上衣和一条黑色的裤子。|Mẹ mua cho tôi một chiếc áo sơ mi vàng, một chiếc áo khoác xanh và một chiếc quần đen.
那件蓝上衣是我最喜欢的，衬衫和裤子也是我现在需要的。|Chiếc áo xanh là cái tôi thích nhất, áo sơ mi và quần cũng là thứ tôi đang cần.
那些吃的，我要带给大家尝一尝。|Những đồ ăn kia, tôi sẽ mang cho mọi người nếm thử.
妈妈来了，我当然很高兴。可是我的自行车丢了，我有点儿生气。|Mẹ đến, tôi đương nhiên rất vui. Nhưng xe đạp của tôi bị mất, tôi hơi bực.
"""), q=Q("""
妈妈给“我”带了什么东西？|带了很多好吃的，还带了一些衣服。|Nhiều đồ ăn ngon và ít quần áo.
“我”最喜欢的是什么东西？|那件蓝上衣。|Chiếc áo xanh lam.
“我”为什么生气？|因为“我”的自行车丢了。|Vì xe đạp bị mất.
""")),
 dict(t="课文二", scene="在商店里", scene_vi="Trong cửa hàng", narr=False, lines=T("""
林娜>妈妈，您看，这件上衣好看吗？|Mẹ ơi, mẹ xem, chiếc áo này đẹp không?
妈妈>好看。|Đẹp.
林娜>您喜欢吗？|Mẹ thích không?
妈妈>喜欢。|Thích.
林娜>我觉得这个颜色您穿特别合适，您试试吧。|Con thấy màu này mẹ mặc rất hợp, mẹ thử đi.
妈妈>好。|Được.
营业员>那边有试衣间。|Đằng kia có phòng thử đồ.
林娜>这件有点儿瘦，还有点儿短，能不能换一件肥点儿的、长点儿的？|Chiếc này hơi chật, lại hơi ngắn, có thể đổi chiếc rộng hơn, dài hơn chút không?
营业员>您再试试这件。|Chị thử lại chiếc này.
林娜>这件不长不短，不肥不瘦，正好。多少钱？|Chiếc này không dài không ngắn, không rộng không chật, vừa đúng. Bao nhiêu tiền?
营业员>490块钱。|490 tệ.
林娜>太贵了。|Đắt quá.
营业员>这么好的衣服才490块，不贵。|Quần áo tốt thế này mới 490 tệ, không đắt.
林娜>你看，我这双鞋又好看又舒服，才300。这件衣服当然不便宜了。|Chị xem, đôi giày này của tôi vừa đẹp vừa êm mà mới 300. Bộ này đương nhiên không rẻ rồi.
"""), q=Q("""
那件上衣怎么样？|颜色很好看，妈妈穿特别合适。|Màu rất đẹp, mẹ mặc rất hợp.
林娜觉得那件上衣贵不贵？|她觉得太贵了。|Cô ấy thấy đắt quá.
""")),
 dict(t="课文三", scene="林娜的自行车不见了，同学们帮她找车。", scene_vi="Xe đạp của Linna không thấy đâu, các bạn giúp cô tìm.", narr=False, lines=T("""
崔浩>你把自行车放在哪儿了？|Bạn để xe đạp ở đâu?
林娜>我就放在这儿了。|Mình để ngay ở đây.
崔浩>你不会记错吧？|Bạn không nhớ nhầm chứ?
林娜>不会。|Không đâu.
崔浩>你的自行车是什么样子的？|Xe đạp của bạn trông thế nào?
林娜>是红色的，比较大的那种。|Màu đỏ, loại tương đối to.
马丁>这辆自行车是你的吗？|Chiếc xe này là của bạn à?
林娜>不是。我的是红的，不是黄的。|Không phải. Của mình màu đỏ, không phải màu vàng.
山田>这辆呢？|Chiếc này thì sao?
林娜>也不是。这辆是旧的，我的是新的。算了，咱们别找了。|Cũng không phải. Chiếc này cũ, của mình mới. Thôi, chúng ta đừng tìm nữa.
"""), q=Q("""
林娜的自行车是什么样子的？|是红色的，比较大的那种，是新的。|Màu đỏ, khá to, còn mới.
林娜的自行车找到了吗？|没找到。|Không tìm thấy.
"""))],
grammar=[
 G("de_phrase", "她给我带了很多好吃的。", "Cụm chữ 的: N/Đại từ/V/Adj + 的 = danh từ",
   "Danh từ, đại từ, động từ, tính từ… thêm “的” tạo thành cụm chữ 的, có chức năng như danh từ (lược bỏ danh từ trung tâm đã rõ).",
   [F("S:Chủ ngữ|V:是|D:Cụm 的", [
      ("这|是|[你的]", "，那是我的。", "Cái này là của bạn, cái kia là của tôi."),
      ("你的车|是|[红的]", "还是黑的？", "Xe của bạn màu đỏ hay màu đen?"),
      ("这本书|是|[图书馆的]", "。", "Quyển sách này là của thư viện."),
      ("|[吃的、穿的、用的]|我都买了", "。", "Đồ ăn, đồ mặc, đồ dùng tôi đều mua rồi.")])],
   notes=["N+的: 外国的 · 老师的 · 妈妈的", "Pron+的: 我的 · 他们的", "V+的: 吃的 · 穿的 · 开车的", "Adj+的: 红色的 · 短的 · 旧的 · 新的"]),
 G("youdianr", "我有点儿生气。", "有点儿 + Adj/V: hơi… (không vừa ý)",
   "Phó từ, đặt trước tính từ hoặc động từ, chỉ mức độ không cao, thường dùng cho điều không như ý.",
   [F("S:Chủ ngữ|kw:有点儿|A:Tính từ / động từ", [("今天|[有点儿]|热", "。", "Hôm nay hơi nóng."), ("这条裤子|[有点儿]|短", "。", "Chiếc quần này hơi ngắn."), ("他|[有点儿]|不太高兴", "。", "Anh ấy hơi không vui.")])],
   notes=["Phân biệt: 有点儿 + Adj (trước tính từ) ↔ Adj + 一点儿 (sau tính từ, dùng khi so sánh)."]),
 G("adj_dianr", "能不能换一件肥点儿的、长点儿的？", "Adj + (一)点儿: … hơn một chút (so sánh)",
   "Dùng trong câu có ý so sánh, chỉ mức độ chênh lệch ít.",
   [F("V:Phần trước|A:Tính từ|kw:(一)点儿", [("帮我换件|长|[一点儿]的", "。", "Đổi giúp tôi chiếc dài hơn chút."), ("这条太瘦，能不能换一条|肥|[点儿]的", "？", "Chiếc này chật quá, đổi chiếc rộng hơn được không?"), ("你今天|好|[点儿]了吗", "？", "Hôm nay bạn đỡ hơn chưa?")])]),
 G("cai2", "这么好的衣服才490块。", "才 (2) + số lượng: chỉ, mới (ít, sớm, rẻ)",
   "Đặt trước cụm số lượng, biểu thị số lượng ít, thời gian sớm, giá rẻ…",
   [F("S:Chủ ngữ|kw:才|N:Số lượng", [("我们班一共|[才]|十个人", "。", "Lớp chúng tôi tổng cộng mới có mười người."), ("|[才]|星期二", "，还早呢。", "Mới thứ Ba, còn sớm mà."), ("这双鞋|[才]|300元", "。", "Đôi giày này chỉ 300 tệ.")])],
   notes=["算了: thôi, bỏ qua, không so đo nữa – 这么麻烦，算了，不吃了。/ 太冷了，算了，今天不去了。"]),
],
ex=[
 pool("一、选词填空", "Chọn từ thích hợp điền vào chỗ trống.", ["尝", "丢", "生气", "颜色", "换", "正好", "便宜", "记", "旧", "算了"], [
   "这是我做的菜，你【尝】一下。", "我的钥匙【丢】了，怎么办？", "他迟到了，老师有点儿【生气】。", "你喜欢什么【颜色】的衣服？", "这件太小了，能【换】一件大点儿的吗？",
   "这双鞋不大不小，【正好】。", "这儿的水果很【便宜】。", "我没【记】住她的电话号码。", "这是我的【旧】手机，新的丢了。", "【算了】，太远了，咱们别去了。"]),
 opn("二、用“的”字短语回答问题", "Trả lời câu hỏi bằng cụm chữ “的”.", [
   ("你的自行车是什么颜色的？", "我的自行车是红色的。"), ("这本书是谁的？", "这本书是图书馆的。"), ("你的手机是新的还是旧的？", "我的手机是新的。"), ("你想买什么样的衣服？", "我想买蓝色的、长一点儿的。")]),
 pick("三、选择“有点儿”或“一点儿”", "Chọn 有点儿 hoặc 一点儿.", [
   (["有点儿", "一点儿"], ["今天【有点儿】冷，多穿点儿衣服吧。", "这件太瘦了，有没有肥【一点儿】的？", "我【有点儿】累，想休息一下。", "请说慢【一点儿】。", "这个菜【有点儿】辣。", "你今天好【一点儿】了吗？"])]),
 opn("四、用“才”完成句子", "Hoàn thành câu với “才”.", [
   ("这件衣服很便宜，______。", "这件衣服很便宜，才五十块。"), ("还早呢，______。", "还早呢，才七点。"), ("我们班人很少，______。", "我们班人很少，才八个人。")]),
 opn("五、根据课文回答问题", "Trả lời câu hỏi theo bài khóa.", [
   ("妈妈给林娜买了什么衣服？", "一件黄色的衬衫、一件蓝色的上衣和一条黑色的裤子。"), ("第一件上衣怎么样？", "有点儿瘦，还有点儿短。"),
   ("林娜的鞋多少钱？", "才300块。"), ("林娜的自行车是什么样子的？", "是红色的、比较大的、新的。")]),
 opn("六、说一说，写一写", "Viết đoạn văn ngắn tả quần áo của bạn hoặc bạn cùng lớp.", [
   ("用“……的”说一说你同学衣服的颜色和样子。", "（参考）玛丽的衣服是红色的，她的裤子是黑色的。马丁的上衣是蓝色的，有点儿肥。我的鞋是白色的，是新的，才两百块。")]),
])
