# -*- coding: utf-8 -*-
# HSK 3 – Bài 8: 今天我出院了
from gtb_gen import V, T, Q, F, G
B = {}

B[8] = dict(zh="今天我出院了", vi="Hôm nay tôi xuất viện rồi",
intro="Trần Thiên Trung chăm chạy bộ để giảm cân, rồi bị đau tai, sốt nhẹ, đau chân phải nằm viện. Hôm nay cậu được xuất viện với lời dặn của bác sĩ.",
vocab=V("""
最近|zuìjìn|dt|gần đây|最近你忙不忙？~Dạo này bạn có bận không?
常|cháng|pho|thường, thường xuyên|我常去那家饭馆吃饭。~Tôi thường đến quán đó ăn cơm.
体育馆|tǐyùguǎn|dt|nhà thi đấu|学校的体育馆很大。~Nhà thi đấu của trường rất lớn.
习惯|xíguàn|dt|thói quen; quen với|早睡早起是个好习惯。~Ngủ sớm dậy sớm là một thói quen tốt.
胖|pàng|tt|béo|我最近胖了两公斤。~Gần đây tôi béo lên hai cân.
健康|jiànkāng|tt|khoẻ mạnh|祝你身体健康！~Chúc bạn sức khỏe dồi dào!
以后|yǐhòu|dt|sau, sau này, về sau|下课以后我们去打球吧。~Tan học xong chúng ta đi chơi bóng đi.
羽毛球|yǔmáoqiú|dt|cầu lông|你会打羽毛球吗？~Bạn biết chơi cầu lông không?
耳朵|ěrduo|dt|tai|我的耳朵有点儿疼。~Tai tôi hơi đau.
感冒|gǎnmào|dong|bị cảm, cảm|天冷了，小心感冒。~Trời lạnh rồi, cẩn thận bị cảm.
发烧|fāshāo|dong|sốt|孩子发烧了，要去医院。~Con bị sốt rồi, phải đi bệnh viện.
低|dī|tt|thấp|今天的温度很低。~Nhiệt độ hôm nay rất thấp.
关心|guānxīn|dong|quan tâm|谢谢你的关心！~Cảm ơn sự quan tâm của bạn!
注意|zhùyì|dong|chú ý|过马路要注意车。~Qua đường phải chú ý xe.
突然|tūrán|tt|đột nhiên, đột ngột|外面突然下雨了。~Bên ngoài đột nhiên mưa.
住院|zhùyuàn|dong|nằm viện|爷爷住院一个星期了。~Ông nội nằm viện một tuần rồi.
担心|dānxīn|dong|lo lắng|别担心，我没事。~Đừng lo, tôi không sao.
腿|tuǐ|dt|chân|跑完步，我的腿很累。~Chạy bộ xong, chân tôi rất mỏi.
病人|bìngrén|dt|bệnh nhân|医生正在给病人检查。~Bác sĩ đang khám cho bệnh nhân.
差不多|chàbuduō|pho|gần như, tương tự, xấp xỉ|我们差不多高。~Chúng tôi cao xấp xỉ nhau.
得|děi|nn|phải, cần|太晚了，我得回家了。~Muộn quá rồi, tôi phải về nhà thôi.
开心|kāixīn|tt|vui vẻ|今天我玩得很开心。~Hôm nay tôi chơi rất vui.
出院|chūyuàn|dong|xuất viện|医生说他明天可以出院了。~Bác sĩ nói mai anh ấy có thể xuất viện.
开|kāi|dong|kê (đơn thuốc)|医生给我开了一些药。~Bác sĩ kê cho tôi ít thuốc.
种|zhǒng|lg|loại|这种水果很好吃。~Loại hoa quả này rất ngon.
方法|fāngfǎ|dt|phương pháp|你学汉语有什么好方法？~Bạn học tiếng Hán có phương pháp gì hay?
其他|qítā|dai|khác|其他同学都回家了。~Các bạn khác đều về nhà rồi.
心里|xīnli|dt|trong lòng|他心里很高兴。~Trong lòng anh ấy rất vui.
"""),
texts=[dict(t="课文1", scene="在学校的体育馆，李文遇到了陈天中。", scene_vi="Lý Văn đã gặp Trần Thiên Trung ở nhà thi đấu của trường.", narr=False, lines=T("""
李文>天中，最近常看见你来体育馆。|Thiên Trung, dạo này hay thấy cậu đến nhà thi đấu.
陈天中>我每天下午都来跑一个小时步。|Chiều nào mình cũng đến chạy bộ một tiếng.
李文>你的运动习惯真不错。|Thói quen tập thể thao của cậu tốt thật.
陈天中>因为我今年胖了十多斤，不能再胖下去了，有点儿不健康。|Vì năm nay mình béo lên hơn mười cân, không thể béo thêm nữa, hơi không khỏe.
李文>我下课以后常去打羽毛球，你也来玩吧。|Mình tan học hay đi đánh cầu lông, cậu cũng đến chơi nhé.
陈天中>我知道，但是你们的水平太高了，我打得不怎么样。|Mình biết, nhưng trình độ các cậu cao quá, mình đánh không ra sao cả.
李文>没关系，我可以教你。|Không sao, mình có thể dạy cậu.
"""), q=Q("""
陈天中每天下午去体育馆做什么？|跑一个小时步。|Chạy bộ một tiếng.
李文下课以后经常做什么？|打羽毛球。|Đánh cầu lông.
陈天中羽毛球打得怎么样？|打得不怎么样。|Đánh không ra sao cả.
""")),
 dict(t="课文2", scene="在教室，安妮问候陈天中。", scene_vi="Annie hỏi thăm Trần Thiên Trung ở trong lớp học.", narr=False, lines=T("""
安妮>你怎么了？看上去有点儿不舒服。|Cậu sao vậy? Trông có vẻ hơi mệt.
陈天中>昨天游完泳以后，耳朵一直有点儿疼。|Hôm qua bơi xong, tai cứ đau đau suốt.
安妮>是不是感冒了？发烧吗？|Có phải bị cảm rồi không? Có sốt không?
陈天中>好像发低烧了。|Hình như sốt nhẹ rồi.
安妮>我送你去医院，让医生检查一下吧。|Mình đưa cậu đi bệnh viện, để bác sĩ khám xem.
陈天中>我先回去睡一觉，可能休息休息就好了。|Mình về ngủ một giấc trước đã, có lẽ nghỉ ngơi là khỏi.
安妮>好吧，如果下午还发烧，就一定要去看医生。|Thôi được, nếu chiều vẫn còn sốt thì nhất định phải đi khám bác sĩ.
陈天中>谢谢关心，我会注意的。|Cảm ơn đã quan tâm, mình sẽ chú ý.
"""), q=Q("""
陈天中是什么时候开始不舒服的？|昨天游完泳以后。|Sau khi bơi xong hôm qua.
安妮想怎么帮助他？|送他去医院，让医生检查一下。|Đưa cậu ấy đi bệnh viện để bác sĩ khám.
陈天中想不想去医院？他想做什么？|不想，他想先回去睡一觉。|Không, cậu ấy muốn về ngủ một giấc trước.
""")),
 dict(t="课文3", scene="在医院病房，安妮探望陈天中。", scene_vi="Annie đến thăm Trần Thiên Trung ở phòng bệnh của bệnh viện.", narr=False, lines=T("""
安妮>你怎么突然住院了？大家都很担心你。|Sao cậu đột nhiên phải nằm viện vậy? Mọi người đều rất lo cho cậu.
陈天中>我的腿疼了几个星期了，医生说需要住院做检查。|Chân mình đau mấy tuần rồi, bác sĩ nói cần nằm viện làm kiểm tra.
安妮>你看起来一点儿也不像病人。|Trông cậu chẳng giống người bệnh chút nào.
陈天中>是啊，我很少生病。我上次来医院已经过去差不多两年了。|Đúng vậy, mình rất ít khi ốm. Lần trước mình đến bệnh viện đã gần hai năm rồi.
安妮>你每天跑步，有时候还去游泳，是不是运动太多了？|Ngày nào cậu cũng chạy bộ, có lúc còn đi bơi, có phải vận động nhiều quá không?
陈天中>医生也这么说，但是还得做完检查才能知道。|Bác sĩ cũng nói vậy, nhưng còn phải kiểm tra xong mới biết được.
安妮>别担心！听医生的话，好好休息，你的腿一定能好。|Đừng lo! Nghe lời bác sĩ, nghỉ ngơi cho tốt, chân cậu nhất định sẽ khỏi.
陈天中>谢谢。有人来看我，我就开心多了。|Cảm ơn. Có người đến thăm, mình vui hơn nhiều rồi.
"""), q=Q("""
陈天中为什么住院了？|他的腿疼了几个星期了，医生说需要住院做检查。|Chân đau mấy tuần, bác sĩ bảo cần nằm viện kiểm tra.
安妮觉得陈天中为什么腿疼？|可能是运动太多了。|Có thể do vận động quá nhiều.
医生是怎么说陈天中的腿的？|医生也说可能是运动太多了，但还得做完检查才能知道。|Bác sĩ cũng nói có thể do vận động nhiều, nhưng phải kiểm tra xong mới biết.
""")),
 dict(t="课文4", scene="在家里，陈天中吃药、休息。", scene_vi="Trần Thiên Trung uống thuốc và nghỉ ngơi ở nhà.", narr=True, lines=T("""
今天我出院了。|Hôm nay tôi xuất viện rồi.
出院前，医生给我开了几种药，而且告诉了我吃药的方法。|Trước khi xuất viện, bác sĩ kê cho tôi mấy loại thuốc, còn dặn tôi cách uống thuốc.
有一种药需要每天睡前吃一次，其他几种每天吃三次，饭后吃。|Có một loại cần uống mỗi tối trước khi ngủ một lần, mấy loại khác mỗi ngày uống ba lần, sau bữa ăn.
除了吃药，医生还说最重要的是多休息。|Ngoài uống thuốc, bác sĩ còn nói quan trọng nhất là nghỉ ngơi nhiều.
我都记在心里了，回家以后一定会多注意。|Tôi đều ghi nhớ trong lòng rồi, về nhà nhất định sẽ chú ý nhiều hơn.
希望我的腿能快一点儿好。|Mong chân tôi mau khỏi.
"""), q=Q("""
陈天中出院前，医生做什么了？|给他开了几种药，而且告诉了他吃药的方法。|Kê mấy loại thuốc và dặn cách uống thuốc.
医生给陈天中开的药应该怎么吃？|一种每天睡前吃一次，其他几种每天吃三次，饭后吃。|Một loại uống trước khi ngủ, các loại khác ngày ba lần sau ăn.
陈天中回家以后应该注意什么？|按时吃药，多休息。|Uống thuốc đúng cách, nghỉ ngơi nhiều.
"""))],
grammar=[
 G("xiaqu", "趋向补语的引申用法（1）：……下去", "Cách dùng mở rộng của bổ ngữ xu hướng (1) – “……下去”",
   "Bổ ngữ xu hướng “下去” đặt sau động từ hoặc tính từ, biểu thị hành động hoặc trạng thái đã bắt đầu và sẽ tiếp tục diễn ra (… tiếp, … mãi).",
   [F("S:Chủ ngữ|X:(不能再 / 如果再…)|V:Động từ / tính từ|kw:下去", [
     ("我今年胖了十多斤，|不能再|胖|[下去]", "了。", "Năm nay tôi béo lên hơn mười cân, không thể béo thêm nữa."),
     ("她读完了第一个问题，后面的|你|读|[下去]", "。", "Cô ấy đọc xong câu hỏi đầu, phần sau bạn đọc tiếp đi."),
     ("这几天太热了，|如果再|热|[下去]", "就不能出门了。", "Mấy hôm nay nóng quá, nếu cứ nóng mãi thì không ra ngoài được."),
     ("这本书太有意思了，我|想一直|看|[下去]", "。", "Cuốn sách này hay quá, tôi muốn đọc mãi.")])]),
 G("lihe2", "离合词（2）", "Từ li hợp (2)",
   "Từ li hợp (游泳, 下雨, 结婚, 睡觉, 跑步…) thường không trực tiếp mang tân ngữ. Nếu có bổ ngữ (kết quả, số lượng, thời lượng), bổ ngữ thường đặt ở giữa hai phần của từ li hợp; đối tượng thì đưa lên trước bằng giới từ (跟…结婚).",
   [F("A:Phần 1 của từ li hợp|X:Bổ ngữ / thành phần chen giữa|B:Phần 2", [
     ("游|完|泳", "以后，我的耳朵一直有点儿疼。", "Bơi xong, tai tôi cứ đau đau suốt."),
     ("今年夏天只下|了两次|雨", "。", "Mùa hè năm nay chỉ mưa có hai lần."),
     ("我每天下午都来跑|一个小时|步", "。", "Chiều nào tôi cũng đến chạy bộ một tiếng."),
     ("我先回去睡|一|觉", "。", "Tôi về ngủ một giấc trước đã.")]),
    F("S:Chủ ngữ|kw:跟|O:Đối tượng|V:Từ li hợp", [
     ("小张下个月|[跟]|他女朋友|结婚", "。", "Tháng sau Tiểu Trương cưới bạn gái.")], cap="Đối tượng đưa lên trước bằng 跟")]),
 G("shiliang2", "时量补语（2）", "Bổ ngữ thời lượng (2)",
   "Bổ ngữ thời lượng đặt sau động từ biểu thị thời gian hành động kéo dài. Với một số động từ không thể kéo dài (来, 去, 回, 结婚, 开学, 过去…), bổ ngữ thời lượng sau động từ biểu thị khoảng thời gian từ lúc hành động hoàn thành đến lúc nói.",
   [F("S:Chủ ngữ|V:Động từ không kéo dài|T:Thời lượng|kw:了", [
     ("我上次来医院已经|过去|差不多两年|[了]", "。", "Lần trước tôi đến bệnh viện đã gần hai năm rồi."),
     ("她|回家|两个月|[了]", "。", "Cô ấy về nhà được hai tháng rồi."),
     ("|开学已经|三个多星期|[了]", "。", "Khai giảng đã hơn ba tuần rồi."),
     ("我|来中国|一年多|[了]", "。", "Tôi đến Trung Quốc hơn một năm rồi.")])]),
 G("yiqianhou", "固定格式“……以前/以后/前/后”", "Cấu trúc cố định “……以前 / 以后 / 前 / 后”",
   "“Thời gian / sự việc + 以前 / 前” biểu thị trước một thời điểm hoặc sự việc nào đó; “Thời gian / sự việc + 以后 / 后” biểu thị sau một thời điểm hoặc sự việc nào đó.",
   [F("X:Thời gian / sự việc|kw:以前 / 前 / 以后 / 后|C:Phần còn lại", [
     ("这种药需要每天睡|[前]|吃一次", "。", "Loại thuốc này cần uống mỗi ngày một lần trước khi ngủ."),
     ("我们决定下班|[后]|一起去看个电影", "。", "Chúng tôi quyết định tan làm xong cùng đi xem phim."),
     ("考完试|[以后]|咱们一起去旅游吧", "。", "Thi xong chúng ta cùng đi du lịch nhé."),
     ("出院|[以前]|好好问一下医生这些药怎么吃", "。", "Trước khi xuất viện hãy hỏi kỹ bác sĩ cách uống mấy loại thuốc này.")])]),
],
test=dict(
 l2=["住院|出院|看病", "还可以|生病了|去医院了", "去看老师|给同学们写信|在家休息一周"],
 l3=["身体不好|一直喜欢运动|现在会跑步和游泳", "生病了|发高烧|回学校了", "家里没药了|头也开始疼了|晚上睡得不好", "不用来医院|不用做检查|不要自己吃药"],
 r1=(["我知道，咱们两点半以前走就行。", "好的，我少吃一点儿。", "她们都喜欢这么说，因为关心我们。", "我记住了，我一定不会吃错的。", "当然。我们先坐公交车，然后换地铁。", "有个好的习惯，身体一定会越来越好的。"],
     ["你不能再吃冰激凌了，吃多了会不舒服。", "明天下午三点要去医院做检查。", "我差不多运动了半年，现在健康多了。", "这种药饭前吃，那种药饭后吃。", "我妈妈常说，多吃饭身体才能健康。"]),
 r2=(["其他", "常", "注意", "心里", "鞋", "担心"],
     ["医生说吃药的时候要（　　）时间和方法。", "你别（　　），我没事，睡一觉就好了。", "虽然她没说，但我知道她（　　）一定很难过。", "A：我发现你（　　）来体育馆跑步。\nB：对，我每天下课以后都来跑一个小时步。", "A：除了羽毛球以外，你还喜欢（　　）运动吗？\nB：我什么运动都喜欢。"]),
 r3=[("前几天妈妈发烧了，这几天她头疼，也没睡好。今天早上妈妈去医院了，医生给她开了药，让她多休息。", "妈妈为什么去医院？", "一直不舒服|孩子生病了|今天发烧了"),
     ("张先生感冒以后没有去医院，他吃了两天药，今天觉得身体好多了。他准备明天去上班。", "关于张先生，可以知道什么？", "感冒了|去医院了|明天不上班"),
     ("我爸爸以前不太喜欢运动，喜欢吃肉、喝饮料，今年他突然胖了不少。检查身体的时候医生告诉他，如果再胖下去，就会生病。最近他开始每天早上跑步，晚上也不吃太多。他现在不但自己运动，而且还常告诉我们要注意健康。",
      ("爸爸为什么开始跑步？", "他喜欢运动|他不想生病|家人让他跑步"), ("关于爸爸，可以知道什么？", "生病了|不吃肉了|开始注意健康了"))],
 w1=["我一直很担（xīn）爷爷的身体。", "虽然问题有很多，但是方（fǎ）更多。", "医生说我不能吃这种药，（qí）他的药都可以吃。"],
 w2=[("差不多", "哥哥和妹妹差不多高。"), ("发烧", "他发烧了，三十八度五。"), ("健康", "他们一家人每天一起跑步，身体都很健康。")],
 gl={"11": "Con không được ăn kem nữa, ăn nhiều sẽ khó chịu. → B: Vâng, con ăn ít thôi.",
     "12": "Ba giờ chiều mai phải đến bệnh viện kiểm tra. → A: Mình biết, chúng ta đi trước hai rưỡi là được.",
     "13": "Mình tập thể thao gần nửa năm, giờ khỏe hơn nhiều rồi. → F: Có thói quen tốt, sức khỏe nhất định sẽ ngày càng tốt.",
     "14": "Loại thuốc này uống trước ăn, loại kia uống sau ăn. → D: Mình nhớ rồi, nhất định không uống nhầm.",
     "15": "Mẹ mình hay nói ăn nhiều cơm thì mới khỏe. → C: Mẹ nào cũng thích nói vậy, vì quan tâm chúng ta.",
     "16": "注意时间和方法 – chú ý thời gian và cách uống. → C 注意.",
     "17": "你别担心 – bạn đừng lo. → F 担心.",
     "18": "她心里一定很难过 – trong lòng cô ấy nhất định rất buồn. → D 心里.",
     "19": "常来体育馆跑步 – thường đến nhà thi đấu chạy bộ. → B 常.",
     "20": "其他运动 – môn thể thao khác. → A 其他.",
     "21": "Mẹ sốt mấy hôm trước, mấy hôm nay đau đầu, ngủ không ngon → A 一直不舒服.",
     "22": "“张先生感冒以后……” → A 感冒了.",
     "23": "“医生告诉他，如果再胖下去，就会生病” → B 他不想生病.",
     "24": "“还常告诉我们要注意健康” → C 开始注意健康了."}),
)
