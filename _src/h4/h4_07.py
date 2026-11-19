# -*- coding: utf-8 -*-
# HSK 4上 – Bài 7: 在工作中学习
from gtb_gen import V, T, Q, F, G, pool, opn
B = {}

B[7] = dict(zh="在工作中学习", vi="Học hỏi trong công việc",
intro="Vương Nhất Tuyết góp ý cho đồng nghiệp về bản kế hoạch khảo sát thị trường, Dương Đồng Lạc chia sẻ kinh nghiệm đi công tác; bài học bàn về cách tiếp cận từng loại khách hàng và lựa chọn, phát triển nghề nghiệp của người trẻ.",
vocab=V("""
打扰|dǎrǎo|dong|làm phiền|对不起，打扰您一下。~Xin lỗi, làm phiền anh một chút.
市场|shìchǎng|dt|thị trường; chợ|妈妈每天早上去菜市场买菜。~Sáng nào mẹ cũng đi chợ mua rau.
调查|diàochá|dong|điều tra, khảo sát|我们要做一次市场调查。~Chúng ta phải làm một cuộc khảo sát thị trường.
计划|jìhuà|dt|kế hoạch|你的假期有什么计划？~Kỳ nghỉ của bạn có kế hoạch gì?
内容|nèiróng|dt|nội dung|这本书的内容很有意思。~Nội dung cuốn sách này rất thú vị.
改|gǎi|dong|sửa, thay đổi|这个句子有错，请改一下。~Câu này có lỗi, hãy sửa lại.
细心|xìxīn|tt|cẩn thận, tỉ mỉ|她做事很细心。~Cô ấy làm việc rất cẩn thận.
客户|kèhù|dt|khách hàng|经理今天要见一个重要的客户。~Hôm nay giám đốc phải gặp một khách hàng quan trọng.
真正|zhēnzhèng|tt|thật sự, chân chính|他是我真正的朋友。~Anh ấy là người bạn thật sự của tôi.
想法|xiǎngfǎ|dt|ý nghĩ, ý tưởng|你有什么想法，可以说说。~Bạn có suy nghĩ gì thì cứ nói.
任务|rènwù|dt|nhiệm vụ|这个任务今天必须完成。~Nhiệm vụ này hôm nay phải hoàn thành.
及时|jíshí|pho|kịp thời|有问题要及时告诉老师。~Có vấn đề phải báo cho thầy cô kịp thời.
出差|chūchāi|dong|đi công tác|爸爸下周要去上海出差。~Tuần sau bố phải đi công tác Thượng Hải.
经验|jīngyàn|dt|kinh nghiệm|他有十年的工作经验。~Anh ấy có mười năm kinh nghiệm làm việc.
采访|cǎifǎng|dong|phỏng vấn|记者采访了那位有名的演员。~Phóng viên đã phỏng vấn diễn viên nổi tiếng đó.
产品|chǎnpǐn|dt|sản phẩm|这家公司的产品质量很好。~Sản phẩm của công ty này chất lượng rất tốt.
看法|kànfǎ|dt|cách nhìn, quan điểm|你对这件事有什么看法？~Bạn có quan điểm gì về việc này?
提前|tíqián|dong|trước (thời hạn), sớm hơn|我们提前十分钟到了。~Chúng tôi đến sớm mười phút.
便于|biànyú|dong|tiện cho, thuận tiện cho|把书放在这儿，便于大家看。~Để sách ở đây cho mọi người tiện xem.
既然|jìrán|lien|đã… thì…, một khi đã|既然你不舒服，就回家休息吧。~Bạn đã không khỏe thì về nhà nghỉ đi.
谈|tán|dong|nói chuyện, bàn bạc|我想跟你谈谈这件事。~Tôi muốn nói chuyện với bạn về việc này.
笔|bǐ|lg|khoản, món (tiền, giao dịch)|他赚了一笔钱。~Anh ấy kiếm được một khoản tiền.
生意|shēngyi|dt|việc buôn bán, làm ăn|这家店的生意很好。~Cửa hàng này buôn bán rất đắt.
困难|kùnnan|dt|khó khăn|遇到困难不要怕。~Gặp khó khăn đừng sợ.
优点|yōudiǎn|dt|ưu điểm|他的优点是很认真。~Ưu điểm của anh ấy là rất chăm chỉ.
缺点|quēdiǎn|dt|khuyết điểm|每个人都有缺点。~Ai cũng có khuyết điểm.
实际|shíjì|tt|thực tế|这个办法不太实际。~Cách này không thực tế lắm.
效果|xiàoguǒ|dt|hiệu quả|这种药的效果很好。~Loại thuốc này hiệu quả rất tốt.
点|diǎn|dt|điểm, mặt|这一点我同意你的看法。~Điểm này tôi đồng ý với bạn.
一下|yíxià|pho|liền, ngay lập tức (một cái)|天一下就黑了。~Trời tối sầm lại ngay.
份|fèn|lg|phần, bản, công việc (lượng từ)|她找到了一份新工作。~Cô ấy đã tìm được một công việc mới.
积累|jīlěi|dong|tích lũy|工作可以积累很多经验。~Đi làm có thể tích lũy nhiều kinh nghiệm.
使|shǐ|dong|làm cho, khiến|这件事使我很感动。~Việc này khiến tôi rất cảm động.
进入|jìnrù|dong|đi vào, bước vào|毕业后他进入了一家大公司。~Tốt nghiệp xong anh ấy vào làm ở một công ty lớn.
社会|shèhuì|dt|xã hội|年轻人刚进入社会时会遇到很多问题。~Người trẻ mới bước vào xã hội sẽ gặp nhiều vấn đề.
管理|guǎnlǐ|dong|quản lý|他在公司负责管理工作。~Anh ấy phụ trách công việc quản lý ở công ty.
基础|jīchǔ|dt|nền tảng, cơ sở|学外语要先打好基础。~Học ngoại ngữ phải xây nền tảng vững trước.
能力|nénglì|dt|năng lực|她的工作能力很强。~Năng lực làm việc của cô ấy rất giỏi.
今后|jīnhòu|dt|từ nay về sau, sau này|今后我会更加努力。~Từ nay về sau tôi sẽ cố gắng hơn.
"""),
texts=[dict(t="课文1", scene="在王一雪办公室，同事向她汇报工作。", scene_vi="Tại văn phòng của Vương Nhất Tuyết, đồng nghiệp báo cáo công việc với cô.", narr=False, lines=T("""
同事>经理，打扰您一下。市场调查的计划书我昨天发到您邮箱了。在内容方面，您觉得有需要改的吗？|Chị giám đốc, làm phiền chị một chút. Bản kế hoạch khảo sát thị trường hôm qua em đã gửi vào email của chị. Về mặt nội dung, chị thấy có chỗ nào cần sửa không ạ?
王一雪>我看过了，写得不错，就是调查的地点只有超市，不太够。|Chị xem rồi, viết khá tốt, chỉ là địa điểm khảo sát chỉ có siêu thị, chưa đủ lắm.
同事>好的，那我再加一些网店。|Vâng, vậy em thêm một số cửa hàng online.
王一雪>行。做调查的时候要细心，注意了解客户真正的想法。|Được. Khi khảo sát phải cẩn thận, chú ý tìm hiểu suy nghĩ thật sự của khách hàng.
同事>明白了，我会认真准备，按时完成任务。|Em hiểu rồi, em sẽ chuẩn bị kỹ, hoàn thành nhiệm vụ đúng hạn.
王一雪>嗯，如果遇到什么问题，及时跟我联系。|Ừ, nếu gặp vấn đề gì thì kịp thời liên hệ với chị.
"""), q=Q("""
同事把什么发到王一雪的邮箱了？|市场调查的计划书。|Bản kế hoạch khảo sát thị trường.
同事交的计划书有什么问题？|调查的地点只有超市，不太够。|Địa điểm khảo sát chỉ có siêu thị, chưa đủ.
除了超市，同事还打算在哪儿进行调查？|网店。|Cửa hàng online.
王一雪建议调查的时候要怎么做？|要细心，注意了解客户真正的想法。|Phải cẩn thận, chú ý tìm hiểu suy nghĩ thật sự của khách hàng.
""")),
 dict(t="课文2", scene="在公司，同事向杨同乐征求建议。", scene_vi="Ở công ty, đồng nghiệp xin lời khuyên của Dương Đồng Lạc.", narr=False, lines=T("""
同事>杨哥，经理让我下周去上海出差，做市场调查，你有这方面的经验吗？|Anh Dương, giám đốc bảo em tuần sau đi công tác Thượng Hải làm khảo sát thị trường, anh có kinh nghiệm về mặt này không ạ?
杨同乐>你要去几天？主要调查什么内容？|Em đi mấy ngày? Chủ yếu khảo sát nội dung gì?
同事>去四天，打算采访一些客户，了解他们对新产品的看法。|Đi bốn ngày, em định phỏng vấn một số khách hàng, tìm hiểu quan điểm của họ về sản phẩm mới.
杨同乐>那你要提前准备好问题，便于和客户交流。|Vậy em phải chuẩn bị câu hỏi trước, để tiện trao đổi với khách hàng.
同事>好的，我已经准备了一些问题。|Vâng, em đã chuẩn bị một số câu hỏi rồi.
杨同乐>很好。既然出差时间不长，就要安排好时间，多获得有用的信息。|Tốt lắm. Thời gian công tác đã không dài thì phải sắp xếp thời gian hợp lý, thu thập thêm nhiều thông tin hữu ích.
"""), q=Q("""
同事要去上海做什么？|出差，做市场调查。|Đi công tác, làm khảo sát thị trường.
同事要调查什么内容？|采访一些客户，了解他们对新产品的看法。|Phỏng vấn khách hàng, tìm hiểu quan điểm của họ về sản phẩm mới.
同事已经准备好什么了？|一些要问的问题。|Một số câu hỏi.
杨同乐提了什么建议？|提前准备好问题，安排好时间，多获得有用的信息。|Chuẩn bị câu hỏi trước, sắp xếp thời gian hợp lý, thu thập nhiều thông tin hữu ích.
""")),
 dict(t="课文3", scene="不同客户，不同方法", scene_vi="Khách hàng khác nhau, cách làm khác nhau", narr=True, lines=T("""
前段时间，杨同乐的同事谈成了一笔不错的生意。|Thời gian trước, đồng nghiệp của Dương Đồng Lạc đã chốt được một hợp đồng khá tốt.
刚开始，这位同事也遇到了一些困难。|Lúc đầu, người đồng nghiệp này cũng gặp một số khó khăn.
拿和客户交流来说，虽然她能把产品的优缺点说得很清楚，但实际效果并不理想。|Lấy việc trao đổi với khách hàng mà nói, tuy cô ấy nói rất rõ ưu nhược điểm của sản phẩm, nhưng hiệu quả thực tế lại không như mong muốn.
杨同乐告诉她，这是因为她介绍的方式都一样。|Dương Đồng Lạc nói với cô ấy, đó là vì cách giới thiệu của cô ấy lúc nào cũng giống nhau.
其实，不同年龄、不同性别的客户对产品的关注点是不一样的。|Thật ra, khách hàng ở độ tuổi khác nhau, giới tính khác nhau thì điểm quan tâm về sản phẩm cũng khác nhau.
于是，这位同事又认真地进行了几次市场调查，了解不同客户的想法。|Thế là, người đồng nghiệp đó lại nghiêm túc làm thêm vài cuộc khảo sát thị trường, tìm hiểu suy nghĩ của từng loại khách hàng.
后来她在面对不同客户时，能根据他们的情况介绍产品，效果一下就好了很多。|Về sau khi đối diện với các khách hàng khác nhau, cô ấy có thể giới thiệu sản phẩm theo tình hình của từng người, hiệu quả lập tức tốt lên rất nhiều.
"""), q=Q("""
前段时间，杨同乐的同事怎么了？|谈成了一笔不错的生意。|Chốt được một hợp đồng khá tốt.
刚开始的时候，同事遇到了什么困难？|她能把产品的优缺点说得很清楚，但实际效果并不理想。|Cô nói rõ ưu nhược điểm sản phẩm nhưng hiệu quả thực tế không như mong muốn.
同事是通过什么办法解决问题的？|做市场调查，了解不同客户的想法。|Làm khảo sát thị trường, tìm hiểu suy nghĩ của từng loại khách hàng.
后来同事是怎么做的？|面对不同客户时，根据他们的情况介绍产品。|Giới thiệu sản phẩm theo tình hình của từng khách hàng.
""")),
 dict(t="课文4", scene="工作的选择与发展", scene_vi="Lựa chọn công việc và phát triển nghề nghiệp", narr=True, lines=T("""
有的年轻人经常换工作，总觉得下一份工作会更好。|Có người trẻ thường xuyên đổi việc, luôn cảm thấy công việc tiếp theo sẽ tốt hơn.
但是，适应新工作往往需要比较长的时间。|Nhưng thích nghi với công việc mới thường cần khá nhiều thời gian.
如果总是换工作，不但很难积累经验，还可能会使自己的发展受到影响。|Nếu cứ đổi việc mãi, không những khó tích lũy kinh nghiệm mà còn có thể khiến sự phát triển của bản thân bị ảnh hưởng.
我认为，年轻人刚进入社会时，不能只关心工资的高低，更要重视学习。|Tôi cho rằng, người trẻ khi mới bước vào xã hội không thể chỉ quan tâm lương cao hay thấp, mà càng phải coi trọng việc học hỏi.
比如，学习课本中没有的专业知识，了解公司的管理方式，学会和同事有效交流，等等。|Ví dụ, học những kiến thức chuyên môn không có trong sách vở, tìm hiểu cách quản lý của công ty, học cách giao tiếp hiệu quả với đồng nghiệp, v.v.
只有把这些基础打好，提高工作能力，今后才会有更好的发展机会。|Chỉ có xây chắc những nền tảng này, nâng cao năng lực làm việc, sau này mới có cơ hội phát triển tốt hơn.
"""), q=Q("""
为什么有的年轻人经常换工作？|总觉得下一份工作会更好。|Luôn cảm thấy công việc tiếp theo sẽ tốt hơn.
为什么不建议年轻人总换工作？|因为很难积累经验，还可能会使自己的发展受到影响。|Vì khó tích lũy kinh nghiệm, còn có thể ảnh hưởng đến sự phát triển của bản thân.
作者认为，年轻人刚进入社会时，应该更重视什么？|学习。|Việc học hỏi.
年轻人怎样才能获得更好的发展机会？|把基础打好，提高工作能力。|Xây chắc nền tảng, nâng cao năng lực làm việc.
""")),
],
grammar=[
 G("zaifangmian", "固定格式“在……方面”", "Cấu trúc cố định “在……方面”",
   "Dùng để giới hạn phạm vi hoặc lĩnh vực đang bàn: “về mặt…, trong lĩnh vực…”.",
   [F("kw:在|X:Lĩnh vực|kw2:方面|V:Nội dung", [
     ("[在]|内容|[方面]|您觉得有需要改的吗", "？", "Về mặt nội dung, chị thấy có chỗ nào cần sửa không?"),
     ("[在]|时间安排|[方面]|你可以再想一想", "。", "Về mặt sắp xếp thời gian, bạn có thể nghĩ thêm."),
     ("他才来中国两个月，[在]|生活|[方面]|还不太习惯", "。", "Anh ấy mới đến Trung Quốc hai tháng, về mặt sinh hoạt vẫn chưa quen lắm.")])]),
 G("jiran", "因果复句“既然……，就……”", "Câu phức nhân quả “既然……，就……”",
   "Vế trước nêu một tiền đề (sự thật đã biết), vế sau nói kết luận suy ra từ tiền đề đó: “đã… thì…”.",
   [F("kw:既然|X:Tiền đề|kw2:就|V:Kết luận", [
     ("[既然]|出差时间不长|[就]|要安排好时间，多获得有用的信息", "。", "Thời gian công tác đã không dài thì phải sắp xếp thời gian hợp lý, thu thập nhiều thông tin hữu ích."),
     ("[既然]|大家都同意|我们[就]|这么做吧", "。", "Mọi người đã đồng ý thì chúng ta làm như vậy nhé."),
     ("[既然]|你们已经决定了|[就]|不要再改了", "。", "Các bạn đã quyết định rồi thì đừng thay đổi nữa.")])]),
 G("nalaishuo", "固定格式“拿……来说”", "Cấu trúc cố định “拿……来说”",
   "Dùng để dẫn ra một phương diện cụ thể hoặc một ví dụ: “lấy… mà nói, ví dụ như…”.",
   [F("kw:拿|X:Ví dụ / phương diện|kw2:来说|V:Nội dung cụ thể", [
     ("[拿]|和客户交流|[来说]|虽然她能把产品的优缺点说得很清楚，但实际效果并不理想", "。", "Lấy việc trao đổi với khách hàng mà nói, tuy cô ấy nói rõ ưu nhược điểm sản phẩm nhưng hiệu quả thực tế không như mong muốn."),
     ("现在的生活很方便。[拿]|购物|[来说]|人们不出门就能买到想要的东西", "。", "Cuộc sống bây giờ rất tiện. Lấy mua sắm mà nói, không cần ra khỏi nhà người ta cũng mua được thứ mình muốn."),
     ("在中国，南北方的生活习惯不同。[拿]|吃饭|[来说]|一般南方人更爱吃米饭", "。", "Ở Trung Quốc, thói quen sinh hoạt miền Nam và miền Bắc khác nhau. Lấy chuyện ăn uống mà nói, người miền Nam thường thích ăn cơm hơn.")])]),
 G("shi", "兼语句“主语+使+宾语+动词短语”", "Câu kiêm ngữ “Chủ ngữ + 使 + Tân ngữ + Cụm động từ”",
   "Biểu thị một tình huống hay nguyên nhân nào đó khiến người hoặc sự vật thay đổi hay sinh ra kết quả: “… làm cho / khiến …”.",
   [F("S:Chủ ngữ (nguyên nhân)|kw:使|O:Tân ngữ|V:Cụm động từ (kết quả)", [
     ("如果总是换工作，可能会|[使]|自己的发展|受到影响", "。", "Nếu cứ đổi việc mãi, có thể khiến sự phát triển của bản thân bị ảnh hưởng."),
     ("这个新方法|[使]|工作|变得更加简单了", "。", "Phương pháp mới này khiến công việc trở nên đơn giản hơn."),
     ("参加这些交流活动|[使]|留学生|更快适应了大学生活", "。", "Tham gia các hoạt động giao lưu này giúp du học sinh thích nghi nhanh hơn với cuộc sống đại học.")])]),
],
ex=[
 pool("选词填空（一）", "Chọn từ thích hợp điền vào chỗ trống.", ["改", "想法", "便于", "打扰", "及时"], [
   "发现问题以后，我们要【及时】解决。", "不好意思，这么晚还来【打扰】您休息。", "我刚才把家庭地址写错了，可以【改】一下吗？",
   "他和同事交流了一下，了解了大家的【想法】。", "老师把学习材料放到了网上，【便于】学生们复习。"]),
 pool("选词填空（二）", "Chọn từ thích hợp điền vào chỗ trống.", ["一下", "基础", "优点", "效果", "管理"], [
   "A：听说你最近一直坚持跑步。 B：是的，我觉得【效果】很好，身体比以前好多了。", "A：经理为什么让小王去做市场调查？ B：经理说他的【优点】是很会和别人交流。",
   "A：我想学好中文，有什么建议吗？ B：刚开始的时候别太着急，先把【基础】打好。", "A：你在大学学的是什么专业？ B：我学的是酒店【管理】专业，现在在一家酒店工作。",
   "A：您讲得真好，讲完我【一下】就明白了。谢谢您！ B：别客气，还有不懂的就来问我。"]),
 pool("选择合适的内容完成短文", "Chọn nội dung thích hợp hoàn thành đoạn văn.", ["按时完成了任务", "也积累了不少经验", "去几家公司做市场调查了", "了解他们对新产品的看法"], [
   "上周，小张接到经理的任务，【去几家公司做市场调查了】。她和一些客户交流了一下，【了解他们对新产品的看法】。有的客户觉得价格有点儿高，有的客户更关心产品好用不好用。昨天，小张按照客户的年龄和性别，写好了调查结果，并交给了经理，【按时完成了任务】。通过这次调查，她对客户的想法有了更多了解，【也积累了不少经验】。"], inline=False),
 opn("用所给的词语完成句子", "Hoàn thành câu với từ ngữ / cấu trúc cho sẵn.", [
   ("A：为什么现在很多人都喜欢骑电动车？ B：______。（在……方面）", "因为在速度方面，电动车比自行车快多了。"),
   ("A：外面下雨了，咱们还出去吗？ B：______，______。（既然……，就……）", "既然下雨了，我们就在家看电影吧。"),
   ("我很喜欢这个小区。______。（拿……来说 / 环境）", "我很喜欢这个小区。拿环境来说，这里到处是花，还很安静。"),
   ("长时间不休息______。（使）", "长时间不休息会使身体越来越差。")]),
 opn("看图，用词语造句", "Nhìn hình, dùng từ cho sẵn đặt câu (tự luận – so với đáp án gợi ý).", pics="h4_l7", items=[
   ("调查", "她拿着本子在做问卷调查。"), ("能力", "他们的工作能力很强，大家都很满意。"), ("细心", "他写作业很细心，每个字都写得很认真。")]),
])
