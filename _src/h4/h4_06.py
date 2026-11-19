# -*- coding: utf-8 -*-
# HSK 4上 – Bài 6: 我陪你去看病
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[6] = dict(zh="我陪你去看病", vi="Mình đi khám bệnh cùng bạn",
intro="Bạch Gia Nguyệt bị cảm nặng, Lý Văn đưa cô đến bệnh viện, giúp điền thông tin và xếp hàng đăng ký khám; bài học còn giới thiệu quy trình khám bệnh ở Trung Quốc.",
vocab=V("""
咳嗽|késou|dong|ho|他感冒了，一直咳嗽。~Anh ấy bị cảm, ho suốt.
咳|ké|dong|ho|她咳了一个晚上。~Cô ấy ho cả một đêm.
厉害|lìhai|tt|ghê gớm, dữ dội; giỏi|今天的风刮得很厉害。~Hôm nay gió thổi rất dữ.
严重|yánzhòng|tt|nghiêm trọng|他的病不太严重。~Bệnh của anh ấy không nghiêm trọng lắm.
赶快|gǎnkuài|pho|mau chóng, nhanh lên|要下雨了，赶快回家吧。~Sắp mưa rồi, mau về nhà thôi.
陪|péi|dong|đi cùng, ở bên|周末我陪妈妈去买东西。~Cuối tuần tôi đi mua sắm cùng mẹ.
翻译|fānyì|dong|phiên dịch, dịch; người phiên dịch|你能帮我翻译一下这句话吗？~Bạn dịch giúp tôi câu này được không?
护士|hùshi|dt|y tá|护士让我在这儿等一下。~Y tá bảo tôi đợi ở đây một lát.
表|biǎo|dt|bảng, mẫu đơn|请先填一下这张表。~Vui lòng điền mẫu đơn này trước.
性别|xìngbié|dt|giới tính|表上要写姓名和性别。~Trên mẫu đơn phải ghi họ tên và giới tính.
国籍|guójí|dt|quốc tịch|你的国籍是哪国？~Quốc tịch của bạn là nước nào?
家庭|jiātíng|dt|gia đình|他有一个幸福的家庭。~Anh ấy có một gia đình hạnh phúc.
地址|dìzhǐ|dt|địa chỉ|请告诉我你家的地址。~Hãy cho tôi biết địa chỉ nhà bạn.
挂号|guàhào|dong|đăng ký khám (lấy số)|看病要先挂号。~Đi khám bệnh phải đăng ký lấy số trước.
排队|páiduì|dong|xếp hàng|买票的人都在排队。~Người mua vé đều đang xếp hàng.
大厅|dàtīng|dt|đại sảnh, sảnh|我在酒店大厅等你。~Tôi đợi bạn ở sảnh khách sạn.
偶尔|ǒu'ěr|pho|thỉnh thoảng|我偶尔也会去健身房。~Thỉnh thoảng tôi cũng đi phòng gym.
身|shēn|dt|thân, người; (lượng từ) bộ (quần áo)|跑完步出了一身汗。~Chạy xong ra cả người mồ hôi.
结果|jiéguǒ|dt|kết quả|考试结果明天出来。~Kết quả thi ngày mai có.
性|xìng|hau|tính (hậu tố: tính chất)|这是一种流行性感冒。~Đây là một loại cảm cúm lây lan theo mùa.
体温|tǐwēn|dt|nhiệt độ cơ thể|护士给我量了体温。~Y tá đo nhiệt độ cho tôi.
降|jiàng|dong|hạ, giảm|吃了药以后，体温降下来了。~Uống thuốc xong, nhiệt độ đã hạ xuống.
光|guāng|pho|chỉ, chỉ riêng|光说不做是不行的。~Chỉ nói mà không làm là không được.
打针|dǎzhēn|dong|tiêm|小孩子都怕打针。~Trẻ con đều sợ tiêm.
有效|yǒuxiào|dong|có hiệu quả|这种药对感冒很有效。~Loại thuốc này rất hiệu quả với cảm cúm.
按时|ànshí|pho|đúng giờ, đúng hạn|请按时吃药。~Hãy uống thuốc đúng giờ.
汗|hàn|dt|mồ hôi|天太热了，我出了很多汗。~Trời nóng quá, tôi ra rất nhiều mồ hôi.
醒|xǐng|dong|tỉnh dậy, thức dậy|我今天早上六点就醒了。~Sáng nay sáu giờ tôi đã tỉnh dậy.
感觉|gǎnjué|dong|cảm thấy; cảm giác|我感觉好多了。~Tôi cảm thấy đỡ nhiều rồi.
低|dī|tt|thấp|今天的气温很低。~Nhiệt độ hôm nay rất thấp.
难受|nánshòu|tt|khó chịu|我头疼，很难受。~Tôi đau đầu, rất khó chịu.
通|tōng|dong|thông, hiểu (ngôn ngữ); thông suốt|语言不通是留学生常见的问题。~Bất đồng ngôn ngữ là vấn đề thường gặp của du học sinh.
过程|guòchéng|dt|quá trình|学习的过程很重要。~Quá trình học tập rất quan trọng.
部|bù|dt|bộ phận, khoa|医院的国际部在三楼。~Khoa quốc tế của bệnh viện ở tầng ba.
收费|shōufèi|dong|thu phí|这个停车场不收费。~Bãi đỗ xe này không thu phí.
情况|qíngkuàng|dt|tình hình, tình trạng|你最近的情况怎么样？~Tình hình dạo này của bạn thế nào?
好|hǎo|dong|để (tiện cho), để có thể|你带上伞，下雨时好用。~Bạn mang ô theo để lúc mưa có mà dùng.
治疗|zhìliáo|dong|điều trị, chữa trị|他在医院治疗了一个月。~Anh ấy điều trị ở bệnh viện một tháng.
步|bù|dt|bước|我们一步一步来，别着急。~Chúng ta làm từng bước một, đừng vội.
"""),
texts=[dict(t="课文1", scene="在家里，白家月躺在床上给李文打电话。", scene_vi="Ở nhà, Bạch Gia Nguyệt nằm trên giường gọi điện cho Lý Văn.", narr=False, lines=T("""
白家月>喂，李文，我身体不舒服。|Alô, Lý Văn, mình thấy không khỏe.
李文>你怎么了？听你的声音，好像感冒了。|Cậu sao thế? Nghe giọng cậu hình như bị cảm rồi.
白家月>对，我还发烧，一直咳嗽，咳得很厉害。|Ừ, mình còn sốt, ho suốt, ho dữ lắm.
李文>那挺严重的，最好赶快去医院检查一下。|Vậy là khá nghiêm trọng đấy, tốt nhất mau đến bệnh viện kiểm tra.
白家月>我也这么想，不过我来中国后还没去过医院，不知道怎么在中国的医院看病。|Mình cũng nghĩ vậy, nhưng từ khi đến Trung Quốc mình chưa đi bệnh viện lần nào, không biết khám bệnh ở bệnh viện Trung Quốc thế nào.
李文>没关系，我陪你一起去，还能帮你翻译。你在家等一下，我现在就去接你。|Không sao, mình đi cùng cậu, còn có thể phiên dịch giúp cậu. Cậu ở nhà đợi một chút, mình qua đón ngay.
白家月>太好了！有你陪着，我就放心多了。|Tốt quá! Có cậu đi cùng, mình yên tâm hơn nhiều rồi.
"""), q=Q("""
白家月怎么了？|她感冒了，还发烧，一直咳嗽，咳得很厉害。|Cô bị cảm, còn sốt, ho suốt, ho rất dữ.
李文让白家月做什么？|赶快去医院检查一下。|Mau đến bệnh viện kiểm tra.
白家月担心什么？|不知道怎么在中国的医院看病。|Không biết khám bệnh ở bệnh viện Trung Quốc thế nào.
李文为什么要陪白家月去医院？|因为白家月不知道怎么看病，他还能帮她翻译。|Vì Gia Nguyệt không biết cách khám bệnh, cậu còn có thể phiên dịch giúp.
""")),
 dict(t="课文2", scene="在医院大厅，李文帮白家月办理看病手续。", scene_vi="Ở sảnh bệnh viện, Lý Văn giúp Bạch Gia Nguyệt làm thủ tục khám bệnh.", narr=False, lines=T("""
李文>护士，您好，我的这位外国朋友生病了，第一次来这里看病，需要怎么做？|Chào chị y tá, người bạn nước ngoài này của tôi bị ốm, lần đầu đến đây khám bệnh, cần làm thế nào ạ?
护士>请在这张表上写上病人的姓名、性别、国籍、年龄、电话号码和家庭地址。|Anh ghi họ tên, giới tính, quốc tịch, tuổi, số điện thoại và địa chỉ nhà của bệnh nhân vào mẫu đơn này.
李文>我写好了，您看看，这样可以吗？|Tôi ghi xong rồi, chị xem như vậy được chưa ạ?
护士>没问题，您拿着病人的护照去挂号吧。|Được rồi, anh cầm hộ chiếu của bệnh nhân đi đăng ký khám nhé.
李文>家月，我去排队挂号，你先在大厅休息，别着急。|Gia Nguyệt, mình đi xếp hàng đăng ký, cậu ngồi nghỉ ở sảnh trước, đừng sốt ruột.
白家月>好的，真是太谢谢你了！|Ừ, thật sự cảm ơn cậu nhiều lắm!
李文>你跟我有什么好客气的。|Cậu với mình thì có gì phải khách sáo.
"""), q=Q("""
护士让李文做什么？|在表上写病人的信息。|Ghi thông tin bệnh nhân vào mẫu đơn.
李文要在表上写什么？|病人的姓名、性别、国籍、年龄、电话号码和家庭地址。|Họ tên, giới tính, quốc tịch, tuổi, số điện thoại và địa chỉ nhà của bệnh nhân.
李文要去做什么？|挂号。|Đăng ký khám.
李文让白家月做什么？|先在大厅休息，别着急。|Ngồi nghỉ ở sảnh trước, đừng sốt ruột.
""")),
 dict(t="课文3", scene="一次看病的经历", scene_vi="Một lần đi khám bệnh", narr=True, lines=T("""
下午白家月去看病了，她告诉医生，自己平时身体不错，偶尔才会生一次病。|Buổi chiều Bạch Gia Nguyệt đi khám bệnh, cô nói với bác sĩ rằng bình thường mình khá khỏe, thỉnh thoảng mới ốm một lần.
这次她病得很厉害，头也一直疼，身上一点儿力气都没有。|Lần này cô ốm rất nặng, đầu cũng đau suốt, người không còn chút sức lực nào.
医生给她做了检查，检查结果出来后，发现她得了比较严重的流行性感冒。|Bác sĩ kiểm tra cho cô, khi có kết quả thì phát hiện cô bị cúm mùa khá nặng.
医生告诉她，现在需要把体温降下来，光吃药恐怕不够，打针会更有效。|Bác sĩ nói với cô, bây giờ cần hạ nhiệt độ xuống, chỉ uống thuốc e là không đủ, tiêm sẽ hiệu quả hơn.
医生还让她回家以后按时吃药，多喝水，多休息。|Bác sĩ còn dặn cô về nhà uống thuốc đúng giờ, uống nhiều nước, nghỉ ngơi nhiều.
晚上，白家月睡觉时出了一身汗。|Buổi tối, lúc ngủ Bạch Gia Nguyệt ra một thân mồ hôi.
第二天醒来时，她感觉头不那么疼了，体温也低了一些，身体不那么难受了。|Hôm sau tỉnh dậy, cô cảm thấy đầu không đau như trước nữa, nhiệt độ cũng hạ bớt, người không còn khó chịu như vậy.
"""), q=Q("""
白家月告诉医生什么了？|她平时身体不错，偶尔才会生一次病。|Bình thường cô khá khỏe, thỉnh thoảng mới ốm.
白家月得了什么病？|比较严重的流行性感冒。|Cúm mùa khá nặng.
医生让白家月做什么？|打针，回家以后按时吃药，多喝水，多休息。|Tiêm, về nhà uống thuốc đúng giờ, uống nhiều nước, nghỉ ngơi nhiều.
第二天，白家月怎么样了？|头不那么疼了，体温也低了一些，身体不那么难受了。|Đầu đỡ đau, nhiệt độ hạ bớt, người đỡ khó chịu.
""")),
 dict(t="课文4", scene="怎么在中国看病", scene_vi="Khám bệnh ở Trung Quốc như thế nào", narr=True, lines=T("""
外国人第一次在中国看病，可能会担心语言不通，或者觉得看病的过程和自己的国家不同。|Người nước ngoài lần đầu khám bệnh ở Trung Quốc có thể lo bất đồng ngôn ngữ, hoặc thấy quy trình khám bệnh khác với nước mình.
其实，这些问题都有办法解决。|Thật ra, những vấn đề này đều có cách giải quyết.
有的医院有国际部，那里的医生一般会说英文，交流比较方便，但是国际部的收费比较高。|Có bệnh viện có khoa quốc tế, bác sĩ ở đó thường nói được tiếng Anh, giao tiếp khá thuận tiện, nhưng chi phí ở khoa quốc tế khá cao.
如果没有特别需要，可以选择普通部，用简单的中文和医生交流。|Nếu không có nhu cầu đặc biệt, có thể chọn khoa thường, dùng tiếng Trung đơn giản để trao đổi với bác sĩ.
在中国看病要先挂号，然后再去找医生。|Khám bệnh ở Trung Quốc phải đăng ký lấy số trước, sau đó mới đi gặp bác sĩ.
医生会问病人的情况，有时还会做一些检查，好给出合适的治疗方法。|Bác sĩ sẽ hỏi tình trạng của bệnh nhân, có khi còn làm một số xét nghiệm để đưa ra cách điều trị phù hợp.
只要按照医生说的一步一步来，一般都可以顺利得到治疗。|Chỉ cần làm từng bước theo lời bác sĩ, thường đều có thể được điều trị thuận lợi.
"""), q=Q("""
外国人第一次在中国看病，可能会担心什么问题？|担心语言不通，或者觉得看病的过程和自己的国家不同。|Lo bất đồng ngôn ngữ, hoặc thấy quy trình khám khác với nước mình.
关于国际部里的医生，可以知道什么？|一般会说英文。|Thường nói được tiếng Anh.
在中国的医院，看病的过程是怎样的？|先挂号，然后找医生，医生会问病人的情况，有时还会做一些检查。|Đăng ký lấy số trước, rồi gặp bác sĩ, bác sĩ hỏi tình trạng, có khi làm xét nghiệm.
在中国看病，怎么做能顺利得到治疗？|按照医生说的一步一步来。|Làm từng bước theo lời bác sĩ.
""")),
],
grammar=[
 G("lihai", "形容词“厉害”", "Tính từ “厉害”",
   "“厉害” đặt sau động từ hoặc tính từ để biểu thị mức độ rất cao (… dữ, … lắm). Cấu trúc: “Động từ + 得 + (phó từ) + 厉害”, “Tính từ + 得 + 厉害”.",
   [F("S:Chủ ngữ|V:Động từ / tính từ|kw:得|D:(Phó từ)|kw2:厉害", [
     ("我还发烧，一直咳嗽，|咳|[得]|很|[厉害]", "。", "Mình còn sốt, ho suốt, ho dữ lắm."),
     ("我昨天跑步跑多了，今天腿|疼|[得]||[厉害]", "。", "Hôm qua tôi chạy bộ nhiều quá, hôm nay chân đau ghê lắm."),
     ("这道菜|辣|[得]||[厉害]", "，我吃了一口就不敢再吃了。", "Món này cay kinh khủng, tôi ăn một miếng là không dám ăn nữa.")])]),
 G("youshenme", "固定格式“（没）有什么（好）×的”", "Cấu trúc cố định “(没)有什么(好) × 的”",
   "Biểu thị không cần thiết phải làm việc gì đó, hoặc không cần có một cảm giác / trạng thái nào đó: “có gì đâu mà…”, “chẳng có gì phải…”.",
   [F("S:Chủ ngữ|kw:（没）有什么（好）|V:×|kw2:的", [
     ("你跟我|[有什么好]|客气|[的]", "。", "Cậu với mình thì có gì phải khách sáo."),
     ("这种事在网上有很多，|[没有什么]|奇怪|[的]", "。", "Chuyện kiểu này trên mạng nhiều lắm, chẳng có gì lạ."),
     ("我觉得这家商场里的东西都很一般，|[没有什么好]|买|[的]", "。", "Tôi thấy đồ trong trung tâm thương mại này đều bình thường, chẳng có gì đáng mua.")])]),
 G("ouer", "频率副词“偶尔”", "Phó từ tần suất “偶尔”",
   "“偶尔” (thỉnh thoảng) biểu thị hành động hoặc tình huống xảy ra rất ít lần.",
   [F("X:Thói quen thường ngày|kw:偶尔|V:Việc ít khi xảy ra", [
     ("她告诉医生，自己平时身体不错，|[偶尔]|才会生一次病", "。", "Cô nói với bác sĩ, bình thường mình khá khỏe, thỉnh thoảng mới ốm một lần."),
     ("他经常在家看电影，|[偶尔]|才去电影院看", "。", "Anh ấy thường xem phim ở nhà, thỉnh thoảng mới ra rạp."),
     ("我一般都在学校食堂吃饭，|[偶尔]|会跟朋友一起出去吃", "。", "Tôi thường ăn ở căng tin trường, thỉnh thoảng đi ăn ngoài với bạn.")])]),
 G("hao", "目的复句“……，好……”", "Câu phức chỉ mục đích “……，好……”",
   "Vế trước nêu một hành động hay tình huống, vế sau (bắt đầu bằng “好”) nói mục đích của nó: “để (có thể / tiện)…”.",
   [F("X:Hành động / tình huống|kw:好|V:Mục đích", [
     ("医生有时还会做一些检查|[好]|给出合适的治疗方法", "。", "Bác sĩ có khi còn làm một số xét nghiệm để đưa ra cách điều trị phù hợp."),
     ("你们先了解一下情况|[好]|做出决定", "。", "Các bạn tìm hiểu tình hình trước để đưa ra quyết định."),
     ("我把电话号码告诉你，以后有什么事|[好]|联系我", "。", "Tôi cho bạn số điện thoại, sau này có việc gì để còn liên lạc với tôi.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["地址", "咳嗽", "赶快", "护士", "严重"], [
   "咱们过去问问【护士】，看牙应该去几楼。", "我这两天有点儿【咳嗽】，不知道是不是感冒了。", "把你的【地址】给我吧，我给你寄点儿东西。",
   "这个问题很【严重】，我们必须马上想办法解决。", "你都发烧好几天了，【赶快】去医院检查一下吧。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["光", "醒", "有效", "过程", "情况"], [
   "A：这道菜是怎么做的？ B：下次我把做菜的【过程】拍下来发给你。", "A：你今天怎么这么饿？ B：白天太忙了，【光】喝了点儿水，一口饭都没吃。",
   "A：经理叫你过去，要了解一下最近的工作【情况】。 B：好的，我现在就去他的办公室。", "A：我早上给你打电话，你怎么没接啊？ B：昨天睡得太晚了，今天10点才【醒】。",
   "A：你觉得看电影学中文怎么样？ B：我觉得这种方法很【有效】，不但能学语言，还能了解中国文化。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["按时吃药", "帮你翻译", "如果感觉身体不舒服", "检查结果出来以后"], [
   "【如果感觉身体不舒服】，最好赶快去医院看看。第一次在中国的医院看病，可以先问护士应该怎么做。一般来说，顺序是先挂号，然后去找医生看病。要是怕听不懂医生说的话，可以找个中国朋友陪你一起去医院，【帮你翻译】。看病时，医生会先问你哪儿不舒服，然后给你做一些检查。【检查结果出来以后】，医生会给出治疗的方法。按照医生说的做，【按时吃药】，多休息，病就会好得更快。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：我已经咳嗽好几天了，今天还有点儿发烧。 B：我看你______，快去医院看看吧。（厉害）", "我看你病得挺厉害的，快去医院看看吧。"),
   ("A：你的病严重吗？我特别担心。 B：放心吧，我得的只是小感冒，______。（没有什么）", "没有什么好担心的。"),
   ("我一般坐公交车，______来学校。（偶尔 / 自行车）", "我一般坐公交车，偶尔骑自行车来学校。"),
   ("你要早点儿准备好材料，______。（好）", "你要早点儿准备好材料，好按时交给老师。")]),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l6", items=[
   ("排队", "大家在大厅里排队等着办手续。"), ("体温", "护士正在给他量体温。"), ("难受", "他发烧了，躺在床上很难受。")]),
])
