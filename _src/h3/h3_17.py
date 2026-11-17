# -*- coding: utf-8 -*-
# HSK 3 – Bài 17: 我要多向认真的人学习
from gtb_gen import V, T, Q, F, G
B = {}

B[17] = dict(zh="我要多向认真的人学习", vi="Tôi phải học hỏi nhiều hơn từ những người nghiêm túc",
intro="Bạn của Tiểu Tuyết sợ gặp cô Lý vì làm sai mấy việc; Trần Thiên Trung sắp tốt nghiệp, đang băn khoăn nên đi làm hay tiếp tục học, du học nước nào.",
vocab=V("""
向|xiàng|gioi|hướng về|孩子一看见妈妈，就向她跑过去了。~Đứa bé vừa thấy mẹ đã chạy về phía mẹ.
楼梯|lóutī|dt|cầu thang bộ|电梯坏了，我们走楼梯吧。~Thang máy hỏng rồi, chúng ta đi cầu thang bộ đi.
害怕|hàipà|dong|sợ, sợ hãi|我小时候害怕打针。~Hồi nhỏ tôi sợ tiêm.
生气|shēngqì|dong|giận, tức giận|妈妈为什么生气了？~Sao mẹ lại giận rồi?
常见|cháng jiàn|tt|thường thấy|这是一种很常见的花。~Đây là một loài hoa rất thường gặp.
聪明|cōngming|tt|thông minh|这个孩子又聪明又可爱。~Đứa bé này vừa thông minh vừa đáng yêu.
错|cuò|dt|sai, lỗi, lỗi sai|这次考试我只有一个错。~Bài thi lần này tôi chỉ sai một lỗi.
认为|rènwéi|dong|cho rằng, nhận thấy|我认为这个办法很好。~Tôi cho rằng cách này rất tốt.
到处|dàochù|pho|mọi nơi, khắp nơi|春天到了，到处都是花。~Mùa xuân đến, khắp nơi đều là hoa.
继续|jìxù|dong|tiếp tục|休息一下，我们再继续。~Nghỉ một lát rồi chúng ta tiếp tục.
同意|tóngyì|dong|đồng ý|爸爸同意我去旅游了。~Bố đồng ý cho tôi đi du lịch rồi.
可|kě|lien|nhưng, nhưng mà|我想去，可没有时间。~Tôi muốn đi nhưng không có thời gian.
屋子|wūzi|dt|phòng, căn phòng, ngôi nhà|屋子里有点儿热。~Trong phòng hơi nóng.
有关|yǒuguān|dong|liên quan, có liên quan|这本书跟中国历史有关。~Cuốn sách này liên quan đến lịch sử Trung Quốc.
关机|guānjī|dong|tắt máy|上课的时候请关机。~Lúc lên lớp xin tắt máy.
前天|qiántiān|dt|hôm kia|我前天去了一趟上海。~Hôm kia tôi đi Thượng Hải một chuyến.
留学|liúxué|dong|du học|她想去中国留学。~Cô ấy muốn đi Trung Quốc du học.
国家|guójiā|dt|quốc gia, đất nước|你去过哪些国家？~Bạn đã đi những nước nào?
比如|bǐrú|dong|ví dụ|我喜欢运动，比如游泳、跑步。~Tôi thích thể thao, ví dụ như bơi, chạy bộ.
查|chá|dong|tra, tìm|这个字我不认识，查一下词典吧。~Chữ này tôi không biết, tra từ điển đi.
有用|yǒuyòng|tt|hữu ích|这本书对我很有用。~Cuốn sách này rất có ích với tôi.
容易|róngyì|tt|dễ, dễ dàng|这个问题很容易回答。~Câu hỏi này rất dễ trả lời.
回答|huídá|dong|trả lời|请回答我的问题。~Hãy trả lời câu hỏi của tôi.
方向|fāngxiàng|dt|phương hướng|你走错方向了。~Bạn đi nhầm hướng rồi.
只有|zhǐyǒu|lien|chỉ có|只有多练习，才能说好汉语。~Chỉ có luyện tập nhiều mới nói giỏi tiếng Hán.
真正|zhēnzhèng|pho|thực sự|这才是真正的朋友。~Đây mới là người bạn thực sự.
难题|nántí|dt|vấn đề khó, vấn đề nan giải|这个难题终于解决了。~Vấn đề khó này cuối cùng cũng được giải quyết.
"""),
texts=[dict(t="课文1", scene="在教学楼里，刘小雪和同学边走边聊。", scene_vi="Trong giảng đường, Lưu Tiểu Tuyết và bạn học đang vừa đi vừa trò chuyện.", narr=False, lines=T("""
刘小雪>别再向前走了，李老师的办公室已经到了。|Đừng đi về phía trước nữa, đến văn phòng cô Lý rồi.
同学>你进去吧，我在楼梯那儿等你。我害怕见李老师。|Cậu vào đi, mình đợi cậu ở chỗ cầu thang. Mình sợ gặp cô Lý.
刘小雪>怎么回事？|Sao vậy?
同学>最近我做错了好几件事，我怕李老师生气。|Gần đây mình làm sai mấy việc, mình sợ cô Lý giận.
刘小雪>你想多了，做错事情是很常见的。|Cậu nghĩ nhiều quá, làm sai là chuyện rất thường gặp.
同学>我把简单的事情做错了，李老师一定觉得我不认真。|Mình làm sai cả những việc đơn giản, cô Lý chắc chắn nghĩ mình không nghiêm túc.
刘小雪>有的人虽然很聪明，但是会在简单的事情中出错，因为他们认为事情简单，就不会认真去做了。|Có người tuy rất thông minh, nhưng lại sai ở những việc đơn giản, vì họ cho rằng việc đơn giản nên không làm nghiêm túc.
同学>你说的就是我，以后我要多向认真的人学习。|Cậu nói đúng là mình rồi, sau này mình phải học hỏi nhiều hơn từ những người nghiêm túc.
"""), q=Q("""
小雪的同学为什么害怕见李老师？|因为最近他做错了好几件事，怕李老师生气。|Vì gần đây cậu ấy làm sai mấy việc, sợ cô giận.
小雪认为她的同学为什么做错事？|因为他认为事情简单，就不认真去做了。|Vì cậu ấy cho rằng việc đơn giản nên không làm nghiêm túc.
小雪的同学打算以后怎么做？|多向认真的人学习。|Học hỏi nhiều hơn từ người nghiêm túc.
""")),
 dict(t="课文2", scene="在阅览室门口，白家月碰到了陈天中。", scene_vi="Bạch Gia Nguyệt gặp Trần Thiên Trung ở cửa phòng đọc sách.", narr=False, lines=T("""
白家月>太阳从西边出来了？这几天怎么总是在图书馆看见你？|Mặt trời mọc đằng tây à? Mấy hôm nay sao cứ thấy cậu ở thư viện thế?
陈天中>这有什么奇怪的？我是来学习的。|Có gì lạ đâu? Mình đến để học mà.
白家月>你怎么还来图书馆学习？同学们都在到处找工作呢。|Sao cậu còn đến thư viện học? Các bạn đều đang đi khắp nơi tìm việc kìa.
陈天中>我不想现在就工作，还想继续学习，我爸妈也同意。可我还没想好学什么，所以来图书馆看看。|Mình không muốn đi làm ngay, còn muốn học tiếp, bố mẹ mình cũng đồng ý. Nhưng mình chưa nghĩ ra học gì, nên đến thư viện xem thử.
白家月>你不是喜欢玩电脑吗？你可以去看看跟电脑有关系的书。|Chẳng phải cậu thích chơi máy tính sao? Cậu có thể xem sách liên quan đến máy tính.
陈天中>你说得对，我记得那个屋子里有些跟电脑有关的书，我去找找。|Cậu nói đúng, mình nhớ phòng kia có ít sách liên quan đến máy tính, mình đi tìm xem.
"""), q=Q("""
白家月为什么说“太阳从西边出来了”？|因为这几天总是在图书馆看见陈天中，她觉得很奇怪。|Vì mấy hôm nay cứ thấy Thiên Trung ở thư viện, cô thấy lạ.
陈天中为什么不去找工作？|因为他还想继续学习。|Vì cậu ấy muốn học tiếp.
白家月觉得陈天中可以学什么？|跟电脑有关系的东西。|Những thứ liên quan đến máy tính.
""")),
 dict(t="课文3", scene="在校园里，李文和陈天中在聊天儿。", scene_vi="Lý Văn và Trần Thiên Trung đang trò chuyện trong khuôn viên trường.", narr=False, lines=T("""
李文>天中，你的手机怎么关机了？|Thiên Trung, sao điện thoại cậu tắt máy thế?
陈天中>我的手机没电了。你找我有事吗？|Điện thoại mình hết pin. Cậu tìm mình có việc gì không?
李文>前天我看见家月了，她告诉我你打算继续留学？|Hôm kia mình gặp Gia Nguyệt, cô ấy nói cậu định tiếp tục du học?
陈天中>是，可是我还没想好学什么，更没想好去哪个国家。|Ừ, nhưng mình chưa nghĩ ra học gì, càng chưa nghĩ ra đi nước nào.
李文>你可以去中国学中文啊。比如可以去北京、上海这样的大城市，那里有很多好大学，也有很多留学生。|Cậu có thể sang Trung Quốc học tiếng Trung. Ví dụ đến những thành phố lớn như Bắc Kinh, Thượng Hải, ở đó có nhiều trường đại học tốt, cũng có nhiều du học sinh.
陈天中>好，那我上网查一查。|Được, vậy mình lên mạng tra thử.
李文>我给你介绍几个有用的网站。|Mình giới thiệu cho cậu mấy trang web hữu ích.
"""), q=Q("""
陈天中打算做什么？|继续留学。|Tiếp tục du học.
李文给他出了什么主意？|去中国学中文，比如去北京、上海这样的大城市。|Sang Trung Quốc học tiếng Trung, ví dụ ở Bắc Kinh, Thượng Hải.
李文为什么给陈天中介绍几个网站？|因为陈天中要上网查一查。|Vì Thiên Trung muốn lên mạng tra cứu.
""")),
 dict(t="课文4", scene="在家里，陈天中在写日记。", scene_vi="Trần Thiên Trung đang ngồi viết nhật ký ở trong nhà.", narr=True, lines=T("""
大学生活马上就要结束了，我最近经常被问到一个问题——“你以后想做什么”，|Cuộc sống đại học sắp kết thúc rồi, dạo này tôi hay bị hỏi một câu — “Sau này bạn muốn làm gì?”,
这个问题真不容易回答。|câu hỏi này thật không dễ trả lời.
我也问了几个同学，大家选择的方向都不同。|Tôi cũng hỏi mấy bạn học, hướng đi mọi người chọn đều khác nhau.
有的想继续在学校学习，有的打算出国留学，还有的决定先找工作。|Có người muốn tiếp tục học ở trường, có người định ra nước ngoài du học, còn có người quyết định tìm việc trước.
我认为只有想清楚自己真正喜欢什么，才能做出最合适的选择。|Tôi cho rằng chỉ khi nghĩ rõ mình thực sự thích gì mới có thể đưa ra lựa chọn phù hợp nhất.
对我来说，想清楚“真正喜欢什么”是个难题。|Với tôi, nghĩ cho rõ “thực sự thích gì” là một bài toán khó.
"""), q=Q("""
陈天中最近经常被问到什么问题？|“你以后想做什么”。|“Sau này bạn muốn làm gì?”
同学们有哪些不同的选择？|有的继续在学校学习，有的出国留学，还有的先找工作。|Có người học tiếp, có người du học, có người đi làm trước.
陈天中知道自己真正喜欢什么吗？|还不知道，对他来说这是个难题。|Chưa biết, với cậu ấy đó là bài toán khó.
"""))],
grammar=[
 G("xiang", "介词“向”", "Giới từ “向”",
   "Giới từ “向” đứng trước đại từ, danh từ hoặc cụm danh từ để chỉ phương hướng hoặc đối tượng của hành động (về phía, hướng về, với).",
   [F("S:(Chủ ngữ)|kw:向|O:Phương hướng / đối tượng|V:Động từ", [
     ("别再|[向]|前|走了", "。", "Đừng đi về phía trước nữa."),
     ("以后我要多|[向]|认真的人|学习", "。", "Sau này tôi phải học hỏi nhiều hơn từ những người nghiêm túc."),
     ("孩子一看见妈妈，就|[向]|她|跑过去了", "。", "Đứa bé vừa thấy mẹ đã chạy về phía mẹ.")])]),
 G("bushima", "反问句“不是……吗？”", "Câu phản vấn “不是……吗？”",
   "Câu phản vấn “不是……吗？” thường dùng để biểu đạt người nói không hiểu hoặc không hài lòng, có lúc là nhắc nhở hoặc xác nhận. Tuy hình thức phủ định nhưng mang ý nghĩa khẳng định (chẳng phải… sao?).",
   [F("S:Chủ ngữ|kw:不是|X:Sự việc (khẳng định)|kw2:吗？|C:Phần sau", [
     ("你|[不是]|喜欢玩电脑|[吗？]|你可以去看看跟电脑有关系的书", "。", "Chẳng phải cậu thích chơi máy tính sao? Cậu có thể xem sách về máy tính."),
     ("你|[不是]|说今天有事|[吗？]|为什么来了", "？", "Chẳng phải bạn nói hôm nay có việc sao? Sao lại đến?"),
     ("考试|[不是]|下个月|[吗？]|你怎么今天就开始复习了", "？", "Chẳng phải tháng sau mới thi sao? Sao hôm nay bạn đã ôn rồi?")])]),
 G("geng", "递进复句“……，更……”", "Câu ghép tăng tiến “……，更……”",
   "Trong câu ghép tăng tiến “……，更……”, vế thứ hai biểu thị mức độ cao hơn, sâu hơn (… , càng / lại càng …).",
   [F("C:Vế 1|kw:更|X:Vế 2 (mức độ cao hơn)", [
     ("我还没想好学什么，|[更]|没想好去哪个国家", "。", "Tôi chưa nghĩ ra học gì, càng chưa nghĩ ra đi nước nào."),
     ("想提高中文水平要多听多看，|[更]|要多说多练", "。", "Muốn nâng cao tiếng Trung phải nghe nhiều đọc nhiều, càng phải nói nhiều luyện nhiều."),
     ("来中国学习，我学会了中文，|[更]|了解了中国文化", "。", "Sang Trung Quốc học, tôi học được tiếng Trung, lại càng hiểu thêm văn hóa Trung Quốc.")])]),
 G("zhiyoucai", "条件复句“只有……，才……”", "Câu ghép điều kiện “只有……，才……”",
   "Trong câu ghép “只有……，才……”, thành phần sau “只有” là điều kiện duy nhất để đạt được kết quả; nếu không có điều kiện này, kết quả sau “才” không thể xảy ra (chỉ có… mới…).",
   [F("kw:只有|C:Điều kiện duy nhất|S:(Chủ ngữ)|kw2:才|V:Kết quả", [
     ("[只有]|想清楚自己真正喜欢什么，||[才]|能做出最合适的选择", "。", "Chỉ khi nghĩ rõ mình thực sự thích gì mới đưa ra được lựa chọn phù hợp nhất."),
     ("[只有]|每天锻炼身体，||[才]|会越来越健康", "。", "Chỉ có tập thể dục mỗi ngày mới ngày càng khỏe mạnh."),
     ("[只有]|多听、多说、多看，|你的中文水平|[才]|能提高", "。", "Chỉ có nghe nhiều, nói nhiều, đọc nhiều, trình độ tiếng Trung của bạn mới nâng cao được.")])]),
],
test=dict(
 l2=["是最好的|能解决问题|客人不会满意", "非常重要|让女的很生气|经理都同意了", "牙疼|生气了|对工作不满意"],
 l3=["别害怕|记得带笔|快点儿回答", "早上上班时|想锻炼身体时|拿很多东西时", "床|面包|饺子", "每天都有比赛|打累了可以吃冰激凌|只有朋友才能一起玩"],
 r1=(["是的，大家都很喜欢她。", "公司遇到的难题终于被我解决了。", "对，前面过马路，马路西边就是。", "不好意思，我查对了，可写错了。", "当然。我们先坐公交车，然后换地铁。", "我同意。只有这样，才能把事情做好。"],
     ["你今天怎么这么高兴？", "张先生做事很认真，我认为我们要向他学习。", "那个小女孩儿真是又聪明又可爱！", "你不是查词典了吗？怎么还写错了？", "您好，请问去动物园是往这个方向走吗？"]),
 r2=(["前天", "有关", "常见", "国家", "鞋", "可"],
     ["这件衬衫大小合适，（　　）颜色我不喜欢。", "虽然这些花很（　　），但是我不知道它们的名字。", "现在很多人不常做饭了，这可能和人们工作越来越忙（　　）。", "A：你是来自哪个（　　）的留学生？\nB：我是法国人，很高兴能来中国留学。", "A：不好意思，（　　）借了你的伞，昨天忘记还给你了。\nB：没关系，你把伞放在我桌子上就行了。"]),
 r3=[("我认为，一个人做事的时候，虽然聪明和认真都很重要，但是只有相信自己，才能真正把事情做好。", "他认为要想把事情做好，什么最重要？", "聪明|认真|相信自己"),
     ("王老师告诉我一个学习汉语、了解中国的好办法，就是读中文报纸，这样能学到有用的句子，更能知道很多中国的新闻。", "王老师介绍的方法是什么？", "去中国旅游|读中文报纸|多写课本上的句子"),
     ("妈妈让我和弟弟学游泳。弟弟一个星期就能自己游了，可我一个月还没学会。我觉得很奇怪，妈妈告诉我：弟弟总是在水里玩，所以学得快；我因为害怕，只在旁边听别人讲、看别人游，那是学不会的。只有到水里多练习，才能真正学会游泳。",
      ("谁学会游泳了？", "我|妈妈|弟弟"), ("妈妈认为学游泳什么最重要？", "多练习|认真听别人讲|多看别人怎么游"))],
 w1=["你先慢慢（xiàng）前走，我买好票就去找你。", "年轻的时候，我一有机会就到（chù）旅游。", "这句话是什么意思？哪位同学来回（dá）一下？"],
 w2=[("生气", "他一直在玩手机，女朋友很生气。"), ("容易", "这次考试很容易，她考得很好。"), ("留学", "这些留学生在中国的大学里学习中文。")],
 gl={"11": "Sao hôm nay bạn vui thế? → B: Vấn đề khó của công ty cuối cùng cũng được mình giải quyết.",
     "12": "Anh Trương làm việc rất nghiêm túc, tôi cho rằng chúng ta phải học hỏi anh ấy. → F: Tôi đồng ý. Chỉ có như vậy mới làm tốt mọi việc.",
     "13": "Cô bé kia thật vừa thông minh vừa đáng yêu! → A: Đúng vậy, mọi người đều rất quý cô bé.",
     "14": "Chẳng phải bạn đã tra từ điển sao? Sao vẫn viết sai? → D: Ngại quá, mình tra đúng rồi nhưng lại viết sai.",
     "15": "Xin chào, cho hỏi đến vườn bách thú có phải đi hướng này không? → C: Đúng, phía trước qua đường, bên tây đường là tới.",
     "16": "可颜色我不喜欢 – nhưng màu thì tôi không thích. → F 可.",
     "17": "这些花很常见 – những bông hoa này rất thường gặp. → C 常见.",
     "18": "和……有关 – có liên quan đến… → B 有关.",
     "19": "哪个国家 – nước nào. → D 国家.",
     "20": "前天借了你的伞 – hôm kia mượn ô của bạn. → A 前天.",
     "21": "“只有相信自己，才能真正把事情做好” → C.",
     "22": "“就是读中文报纸” → B.",
     "23": "“弟弟一个星期就能自己游了” → C.",
     "24": "“只有到水里多练习，才能真正学会游泳” → A."}),
)
