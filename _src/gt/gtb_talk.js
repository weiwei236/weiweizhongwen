/* Hội thoại theo bài – sơ cấp 2 (bài 1–10). Phiên âm để trống, trang tự điền bằng pinyin-pro (gbFillPy) */
const TALK_GB = {
 1: { title: "Làm quen với cuộc sống mới", turns: [
   { ai: ["你来中国多长时间了？", "", "Bạn đến Trung Quốc bao lâu rồi?"], hint: "我来中国 + thời gian + 了 (半年多 / 三个月 / 一年).", say: [{ ans: ["我来中国半年多了。", "我来中国三个月了。"], re: "年|月|星期|天|半" }] },
   { ai: ["你已经习惯这里的生活了吗？", "", "Bạn đã quen với cuộc sống ở đây chưa?"], hint: "已经渐渐地习惯了 / 还不太习惯.", say: [
     { ans: ["我已经渐渐地习惯了。"], re: "^(我)?(已经|渐渐|差不多)", react: ["太好了！你真是入乡随俗了。", "", "Tốt quá! Bạn đúng là nhập gia tùy tục rồi."], next: "late" },
     { ans: ["我还不太习惯。"], re: "不|没", react: ["别着急，慢慢就习惯了。你最不习惯什么？", "", "Đừng vội, từ từ sẽ quen. Bạn không quen nhất điều gì?"], next: "what" }] },
   { id: "what", ai: [], hint: "我最不习惯的是…… (早上八点上课 / 吃饭 / 天气).", say: [{ ans: ["我最不习惯的是早上八点上课。", "我最不习惯这里的天气。"], re: "不习惯|是|.{3,}" }] },
   { id: "late", ai: ["你上课常常迟到吗？", "", "Bạn có hay đi học muộn không?"], hint: "很少迟到 / 常常迟到 / 从来不迟到.", say: [
     { ans: ["我很少迟到。", "我从来不迟到。"], re: "很少|不迟到|从来", react: ["你真棒！", "", "Bạn giỏi thật!"] },
     { ans: ["我常常迟到。"], re: "常常|有时|经常", react: ["为了不迟到，你应该买一个闹钟。", "", "Để không đến muộn, bạn nên mua một cái đồng hồ báo thức."] }] },
   { ai: ["外面正下着雨呢，你带伞了吗？", "", "Bên ngoài đang mưa, bạn mang ô chưa?"], hint: "带着呢 / 没带.", say: [
     { ans: ["谢谢，我带着呢。"], re: "带着|带了", react: ["那就好。", "", "Vậy thì tốt."] },
     { ans: ["我没带伞。"], re: "没", react: ["我有两把，给你一把吧。", "", "Mình có hai cái, cho bạn một cái."] }] },
   { ai: ["吃了吗？", "", "Ăn chưa?"], hint: "Đây là câu chào của người quen: 吃了 / 还没吃呢.", say: [{ ans: ["吃了，你呢？", "还没吃呢。"], re: "吃|没" }] }] },
 2: { title: "Căn phòng của bạn", turns: [
   { ai: ["听说你快毕业了，恭喜恭喜！", "", "Nghe nói bạn sắp tốt nghiệp, chúc mừng chúc mừng!"], hint: "Đáp lại lời chúc: 谢谢！/ 还早呢.", say: [{ ans: ["谢谢！", "还早呢，我明年才毕业。"], re: "谢|早|毕业|.{2,}" }] },
   { ai: ["你的房间大不大？", "", "Phòng của bạn có to không?"], hint: "不大不小 / 很大 / 有点儿小.", say: [{ ans: ["不大不小。", "我的房间有点儿小。"], re: "大|小" }] },
   { ai: ["你的桌子上放着什么？", "", "Trên bàn bạn để những gì?"], hint: "桌子上放着 + số lượng + đồ vật (一台电脑、几本书…).", say: [{ ans: ["桌子上放着一台电脑和几本书。"], re: "放着|摆着|有" }] },
   { ai: ["你常常打扫房间吗？", "", "Bạn có thường dọn phòng không?"], hint: "每个星期打扫…次 / 从来不打扫.", say: [
     { ans: ["我每个星期打扫一次。"], re: "次|每|常常|天天", react: ["你真是个好孩子！", "", "Bạn đúng là đứa trẻ ngoan!"], next: "never" },
     { ans: ["我从来不打扫房间。"], re: "从来|不|很少", react: ["你的房间一定乱七八糟的吧？", "", "Phòng bạn chắc là bừa bộn lắm nhỉ?"], next: "mess" }] },
   { id: "mess", ai: [], hint: "是啊，有点儿乱 / 还可以.", say: [{ ans: ["是啊，有点儿乱。", "还可以。"], re: ".{2,}" }] },
   { id: "never", ai: ["你从来没去过什么地方？", "", "Có nơi nào bạn chưa từng đến không?"], hint: "我从来没去过 + nơi chốn.", say: [{ ans: ["我从来没去过上海。"], re: "从来没|没去过" }] },
   { ai: ["毕业以后你想做什么工作？", "", "Tốt nghiệp xong bạn muốn làm việc gì?"], hint: "我想做和……有关系的工作 / 我想当…….", say: [{ ans: ["我想做和汉语有关系的工作。", "我想当老师。"], re: "想|当|做" }] }] },
 3: { title: "Đi chợ mua ớt", turns: [
   { ai: ["您好！您要买点儿什么？", "", "Chào anh/chị! Anh/chị muốn mua gì ạ?"], hint: "我想买…… (辣椒 / 水果 / 青菜).", say: [{ ans: ["我想买点儿辣椒。"], re: "买|要" }] },
   { ai: ["您喜欢辣的还是甜的？", "", "Anh/chị thích loại cay hay ngọt?"], hint: "Chọn một: 我喜欢辣的 / 甜的 / 既不辣也不甜的.", say: [
     { ans: ["我喜欢辣的。"], re: "辣", react: ["您是四川人吧？不怕辣？", "", "Anh/chị là người Tứ Xuyên à? Không sợ cay ư?"], next: "pa" },
     { ans: ["我喜欢甜的。", "我要既不辣也不甜的。"], re: "甜|不辣", react: ["好，左边的篮子里是甜的。", "", "Được, giỏ bên trái là ớt ngọt."], next: "fresh" }] },
   { id: "pa", ai: [], hint: "我不怕辣 / 我不是四川人，可是我不怕辣.", say: [{ ans: ["我不怕辣，就怕不辣。"], re: "怕|辣|不是|是" }] },
   { id: "fresh", ai: ["这些辣椒都是今天早上刚摘的，又新鲜又好看。", "", "Ớt này đều mới hái sáng nay, vừa tươi vừa đẹp."], hint: "Hỏi giá: 多少钱一斤？", say: [{ ans: ["多少钱一斤？"], re: "多少|钱|几块" }] },
   { ai: ["五块钱一斤。您要几斤？", "", "Năm tệ một cân. Anh/chị lấy mấy cân?"], hint: "我要 + số + 斤.", say: [{ ans: ["我要两斤。"], re: "斤|[一二两三四五]" }] },
   { ai: ["好的，一共十块。还要别的吗？", "", "Vâng, tổng cộng mười tệ. Còn cần gì khác không?"], hint: "不要了，谢谢 / 我还要……", say: [{ ans: ["不要了，谢谢！"], re: "不要|谢|还要|没有" }] }] },
 4: { title: "Bạn và tiếng Hán", turns: [
   { ai: ["你是从哪儿来的？", "", "Bạn từ đâu đến?"], hint: "我是从……来的.", say: [{ ans: ["我是从越南来的。"], re: "从.+来|越南|是" }] },
   { ai: ["你是什么时候开始学汉语的？", "", "Bạn bắt đầu học tiếng Hán từ khi nào?"], hint: "我是 + thời gian + 开始学的.", say: [{ ans: ["我是两年前开始学的。"], re: "年|月|岁|前|开始|的" }] },
   { ai: ["你为什么选择学汉语？", "", "Vì sao bạn chọn học tiếng Hán?"], hint: "因为…… (喜欢中国文化 / 想去中国工作).", say: [{ ans: ["因为我喜欢中国文化。", "因为我想去中国工作。"], re: "因为|喜欢|想|为了" }] },
   { ai: ["有人说学汉语没用，你后悔吗？", "", "Có người nói học tiếng Hán vô ích, bạn có hối hận không?"], hint: "我一点儿也不后悔.", say: [
     { ans: ["我一点儿也不后悔。"], re: "不后悔|一点儿也不|没有", react: ["对，汉语越学越有意思！", "", "Đúng, tiếng Hán càng học càng thú vị!"] },
     { ans: ["有一点儿后悔，汉语太难了。"], re: "后悔|难", react: ["其实汉语没有那么难，加油！", "", "Thật ra tiếng Hán không khó đến thế, cố lên!"] }] },
   { ai: ["你有中国朋友吗？你们常一起做什么？", "", "Bạn có bạn người Trung Quốc không? Các bạn thường cùng làm gì?"], hint: "我们一起 + 吃中国菜 / 喝茶 / 聊天儿.", say: [{ ans: ["有，我们常一起吃中国菜、聊天儿。", "我还没有中国朋友。"], re: "一起|有|没有" }] },
   { ai: ["你会说哪些外语？", "", "Bạn biết nói những ngoại ngữ nào?"], hint: "我不但会说……，而且会说…….", say: [{ ans: ["我不但会说英语，而且会说汉语。"], re: "不但|而且|会" }] },
   { ai: ["你将来想做什么工作？", "", "Sau này bạn muốn làm gì?"], hint: "我想当 导游 / 厨师 / 老师 / 翻译.", say: [{ ans: ["我想当导游。", "我想当翻译。"], re: "想|当|做" }] }] },
 5: { title: "Bữa sáng kiểu Trung Quốc", turns: [
   { ai: ["你早饭一般吃什么？", "", "Bữa sáng bạn thường ăn gì?"], hint: "我一般吃…… (面包 / 豆浆油条 / 河粉).", say: [{ ans: ["我一般吃面包，喝牛奶。", "我吃豆浆油条。"], re: "吃|喝" }] },
   { ai: ["你吃过油条吗？", "", "Bạn ăn quẩy bao giờ chưa?"], hint: "吃过 / 没吃过.", say: [
     { ans: ["我吃过，很好吃。"], re: "^(我)?吃过|好吃", react: ["油条最好蘸着豆浆吃。", "", "Quẩy tốt nhất là chấm sữa đậu nành mà ăn."], next: "zhan" },
     { ans: ["我没吃过。"], re: "没", react: ["明天我请你吃吧，要蘸着豆浆吃。", "", "Mai mình mời bạn ăn nhé, phải chấm sữa đậu nành."], next: "zhan" }] },
   { id: "zhan", ai: [], hint: "Hỏi lại cho rõ: 是“蘸着吃”还是“站着吃”？", say: [{ ans: ["是“蘸着吃”还是“站着吃”？", "好，我试试。"], re: ".{2,}" }] },
   { ai: ["你喜欢一边吃饭一边做什么？", "", "Bạn thích vừa ăn cơm vừa làm gì?"], hint: "我喜欢 看着电视 / 听着音乐 吃饭.", say: [{ ans: ["我喜欢看着电视吃饭。", "我喜欢一边吃饭一边聊天儿。"], re: "着|一边" }] },
   { ai: ["周末你想去哪儿玩儿？", "", "Cuối tuần bạn muốn đi đâu chơi?"], hint: "我想去…… / 哪儿都可以 / 哪儿也不想去.", say: [
     { ans: ["我想去游览故宫。"], re: "^(我)?想去|游览", react: ["好啊，我陪着你去。", "", "Được thôi, mình đi cùng bạn."] },
     { ans: ["去哪儿都可以。", "我哪儿也不想去。"], re: "哪儿", react: ["那我们一起去公园吧。", "", "Vậy chúng ta cùng đi công viên nhé."] }] },
   { ai: ["你跟中国人交流有问题吗？", "", "Bạn giao tiếp với người Trung Quốc có vấn đề gì không?"], hint: "没问题 / 有时候听不懂.", say: [{ ans: ["没什么问题。", "有时候听不懂。"], re: "问题|听不懂|没|有" }] }] },
 6: { title: "Gọi điện về nhà", turns: [
   { ai: ["喂，孩子，最近身体怎么样？", "", "Alo, con à, dạo này sức khỏe thế nào?"], hint: "我很好，别担心.", say: [{ ans: ["我很好，别担心。", "挺好的，妈妈放心吧。"], re: "好|担心|放心" }] },
   { ai: ["中国菜你吃得惯吗？", "", "Món Trung Quốc con ăn có quen không?"], hint: "吃得惯 / 吃不惯.", say: [
     { ans: ["我已经吃惯了。"], re: "吃得惯|吃惯|惯了", react: ["那就好。你会做中国菜吗？", "", "Vậy thì tốt. Con biết nấu món Trung Quốc không?"], next: "cook" },
     { ans: ["我还吃不惯。"], re: "不惯|不习惯", react: ["慢慢就吃惯了。", "", "Từ từ sẽ quen thôi."], next: "class" }] },
   { id: "cook", ai: [], hint: "我会做西红柿炒鸡蛋 / 还不会.", say: [{ ans: ["我会做西红柿炒鸡蛋，好吃极了。"], re: "会|不会|做" }], next: "class" },
   { id: "class", ai: ["老师讲课你听得懂吗？", "", "Thầy cô giảng bài con nghe hiểu không?"], hint: "听得懂 / 听不懂 / 有的听得懂.", say: [{ ans: ["老师说的话我都听得懂。", "有的听得懂，有的听不懂。"], re: "听得懂|听不懂|懂" }] },
   { ai: ["这个假期你回得来吗？", "", "Kỳ nghỉ này con có về được không?"], hint: "回得去 / 回不去 (đứng ở chỗ con: 回去).", say: [
     { ans: ["我回得去。"], re: "回得去|回得来|能回", react: ["太好了！妈妈给你做好吃的。", "", "Tốt quá! Mẹ nấu món ngon cho con."] },
     { ans: ["对不起，我回不去了，我得努力学习。"], re: "回不去|回不来|不能", react: ["没关系，有空儿常给我们发邮件。", "", "Không sao, có thời gian thường xuyên gửi email cho bố mẹ nhé."] }] },
   { ai: ["祝你快乐！", "", "Chúc con vui vẻ!"], hint: "Chúc lại: 祝您和爸爸身体健康！", say: [{ ans: ["祝您和爸爸身体健康！"], re: "祝|健康|谢" }] }] },
 7: { title: "Ước mơ thời thơ ấu", turns: [
   { ai: ["你小时候有什么理想？", "", "Hồi nhỏ bạn có ước mơ gì?"], hint: "小时候我想当 / 想去…….", say: [{ ans: ["小时候我想当医生。", "我想去埃及看金字塔。"], re: "想|当|去" }] },
   { ai: ["你的理想实现了吗？", "", "Ước mơ của bạn đã thành hiện thực chưa?"], hint: "实现了 / 还没实现，我还要努力下去.", say: [
     { ans: ["实现了。"], re: "^(已经)?实现了|^(我)?实现", react: ["真了不起！", "", "Thật đáng nể!"] },
     { ans: ["还没有，我还要继续努力下去。"], re: "没|下去|继续|努力", react: ["加油！我相信你一定能实现。", "", "Cố lên! Mình tin bạn nhất định làm được."] }] },
   { ai: ["今天轮到谁打扫房间？", "", "Hôm nay đến lượt ai dọn phòng?"], hint: "轮到我了 / 轮到我同屋了.", say: [{ ans: ["今天轮到我了。", "轮到我同屋了。"], re: "轮到|我|同屋" }] },
   { ai: ["这么多作业，你今天写得完吗？", "", "Nhiều bài tập thế này, hôm nay bạn viết xong không?"], hint: "写得完 / 写不完 / 写不了.", say: [{ ans: ["写得完。", "太多了，我写不了。"], re: "写得完|写不完|写不了|写得了" }] },
   { ai: ["我们出去玩儿玩儿吧！", "", "Chúng mình ra ngoài chơi đi!"], hint: "Từ chối bằng V+什么: 玩儿什么！我还得写作业.", say: [{ ans: ["玩儿什么！我还得写作业呢。", "好啊，走吧！"], re: "什么|好|走|不" }] },
   { ai: ["你最讨厌什么样的人？", "", "Bạn ghét nhất kiểu người nào?"], hint: "我最讨厌……的人.", say: [{ ans: ["我最讨厌做事不认真的人。"], re: "讨厌" }] }] },
 8: { title: "So sánh và kỷ niệm", turns: [
   { ai: ["你比你的好朋友高吗？", "", "Bạn có cao hơn bạn thân không?"], hint: "我比他高一点儿 / 我没有他高 / 我们一样高.", say: [{ ans: ["我比他高一点儿。", "我没有他高。"], re: "比|没有|一样|差不多" }] },
   { ai: ["今天比昨天冷吗？", "", "Hôm nay có lạnh hơn hôm qua không?"], hint: "比昨天冷 / 没有昨天冷 / 不比昨天冷.", say: [{ ans: ["今天比昨天冷多了。", "今天没有昨天冷。"], re: "比|没有|不比|一样" }] },
   { ai: ["这儿的东西比你们国家贵吗？", "", "Đồ ở đây có đắt hơn nước bạn không?"], hint: "比……贵一点儿 / 不比……贵 / 没有……贵.", say: [{ ans: ["这儿的东西比我们国家贵一点儿。", "这儿的东西不比我们国家贵。"], re: "比|没有|一样|差不多" }] },
   { ai: ["在你的一生中，什么最难忘？", "", "Trong cuộc đời bạn, điều gì khó quên nhất?"], hint: "最难忘的是…….", say: [{ ans: ["最难忘的是小时候的朋友。"], re: "难忘|是" }] },
   { ai: ["你还记得小学同学的名字吗？", "", "Bạn còn nhớ tên bạn học tiểu học không?"], hint: "还记得 / 有的想不起来了.", say: [
     { ans: ["我还记得。"], re: "^(我)?(还)?记得", react: ["你的记性真好！", "", "Trí nhớ của bạn tốt thật!"] },
     { ans: ["有的名字我已经想不起来了。"], re: "想不起来|忘", react: ["人老了也会这样的。", "", "Người ta già đi cũng sẽ như vậy."] }] },
   { ai: ["你们现在还有联系吗？", "", "Bây giờ các bạn còn liên lạc không?"], hint: "还有联系 / 没有联系了，我想打听他的消息.", say: [{ ans: ["我们还有联系。", "没有了，我想打听他的消息。"], re: "联系|消息|有|没" }] }] },
 9: { title: "Buổi tiệc chia tay", turns: [
   { ai: ["考试结束了，你的心情怎么样？", "", "Thi xong rồi, tâm trạng bạn thế nào?"], hint: "又高兴又难过 / 很轻松.", say: [{ ans: ["我的心情又高兴又难过。", "很轻松。"], re: "高兴|难过|轻松|紧张|好" }] },
   { ai: ["你考试的时候紧张吗？", "", "Lúc thi bạn có căng thẳng không?"], hint: "很紧张 / 一点儿也不紧张.", say: [{ ans: ["我特别紧张。", "我一点儿也不紧张。"], re: "紧张" }] },
   { ai: ["你喜欢运动吗？", "", "Bạn có thích thể thao không?"], hint: "很喜欢，特别是…….", say: [{ ans: ["很喜欢，特别是游泳。"], re: "特别是|喜欢|不" }] },
   { ai: ["你的汉语比你同屋的好吗？", "", "Tiếng Hán của bạn có giỏi hơn bạn cùng phòng không?"], hint: "我的汉语不如他的好 / 比他的好一点儿.", say: [{ ans: ["我的汉语不如他的好。", "比他的好一点儿。"], re: "不如|比|没有|一样" }] },
   { ai: ["你父母让你做什么？不让你做什么？", "", "Bố mẹ bảo bạn làm gì? Không cho bạn làm gì?"], hint: "他们让我……，不让我…….", say: [{ ans: ["他们让我好好儿学习，不让我晚上出去玩儿。"], re: "让|叫" }] },
   { ai: ["什么时候你觉得最幸福？", "", "Lúc nào bạn thấy hạnh phúc nhất?"], hint: "……的时候我觉得最幸福.", say: [{ ans: ["和家人在一起的时候，我觉得最幸福。"], re: "幸福|时候" }] }] },
 10: { title: "Niềm vui giản đơn", turns: [
   { ai: ["你最近过得快乐吗？", "", "Dạo này bạn sống có vui không?"], hint: "很快乐 / 不太快乐.", say: [
     { ans: ["我过得很快乐。"], re: "^(我)?(过得)?(很|挺|非常)?(快乐|开心|好)", react: ["真好！什么事使你这么快乐？", "", "Tốt quá! Chuyện gì khiến bạn vui thế?"], next: "why" },
     { ans: ["不太快乐，最近太累了。"], re: "不|累", react: ["别太辛苦了，好好儿休息休息。", "", "Đừng vất vả quá, nghỉ ngơi cho tốt nhé."], next: "why" }] },
   { id: "why", ai: [], hint: "……使我快乐 / ……能让我开心.", say: [{ ans: ["和朋友聊天儿使我快乐。", "睡够了就能让我开心。"], re: "使|让|快乐|开心|.{3,}" }] },
   { ai: ["你每天学习几个小时？", "", "Mỗi ngày bạn học mấy tiếng?"], hint: "我每天学习 + số + 个小时.", say: [{ ans: ["我每天学习五个小时。"], re: "小时|钟头" }] },
   { ai: ["你的汉语一天比一天好了吧？", "", "Tiếng Hán của bạn ngày càng tốt lên nhỉ?"], hint: "是啊，一天比一天好 / 还差得远呢.", say: [{ ans: ["是啊，一天比一天好。", "还差得远呢。"], re: "一天比一天|是|差|好" }] },
   { ai: ["你受不了什么样的天气？", "", "Bạn không chịu nổi kiểu thời tiết nào?"], hint: "我受不了……的天气.", say: [{ ans: ["我受不了太热的天气。"], re: "受不了" }] },
   { ai: ["你觉得快乐难不难？", "", "Bạn thấy hạnh phúc có khó không?"], hint: "快乐其实很简单.", say: [{ ans: ["我觉得快乐其实很简单。"], re: "简单|难|容易" }] }] },
};
Object.entries(TALK_GB).forEach(([n, t]) => { if(GB_LESSONS1[n]) GB_LESSONS1[n].talk = t; });
