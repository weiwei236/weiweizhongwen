/* Hội thoại theo bài – sơ cấp 2 (bài 11–20) */
const TALK_GB2 = {
 11: { title: "Kể chuyện cổ tích", turns: [
   { ai: ["你喜欢看童话故事吗？", "", "Bạn có thích đọc truyện cổ tích không?"], hint: "喜欢 / 不太喜欢 + lý do.", say: [
     { ans: ["我很喜欢看童话故事。"], re: "喜欢|爱", react: ["我也是！童话故事又有趣又简单。", "", "Mình cũng thế! Truyện cổ tích vừa thú vị vừa đơn giản."] },
     { ans: ["我不太喜欢。"], re: "不", react: ["没关系，那你喜欢看什么书？", "", "Không sao, thế bạn thích đọc sách gì?"] }] },
   { ai: ["你还记得《书本里的蚂蚁》吗？小蚂蚁是怎么进到书里的？", "", "Bạn còn nhớ chuyện “Chú kiến trong sách” không? Kiến vào sách thế nào?"], hint: "小女孩儿摘下一朵花，夹进了书里.", say: [{ ans: ["小女孩儿把一朵花夹进了书里，小蚂蚁正在花里睡觉。"], re: "花|夹|睡觉" }] },
   { ai: ["书里的字为什么羡慕小蚂蚁？", "", "Vì sao chữ trong sách ngưỡng mộ kiến?"], hint: "因为小蚂蚁会走路，想去哪儿就去哪儿.", say: [{ ans: ["因为小蚂蚁会走路，想去哪儿就去哪儿。"], re: "走|哪儿|自由" }] },
   { ai: ["要是你有一本这样的书，你想做什么？", "", "Nếu bạn có quyển sách như vậy, bạn muốn làm gì?"], hint: "我想每天看新的故事 / 我想……", say: [{ ans: ["我想每天都看新的故事。"], re: ".{3,}" }] },
   { ai: ["你能听出来我是哪儿人吗？", "", "Bạn nghe ra được mình là người ở đâu không?"], hint: "听出来了 / 听不出来.", say: [{ ans: ["我听不出来。", "我听出来了，你是北京人。"], re: "听" }] }] },
 12: { title: "Chuyện buồn cười khi nói sai", turns: [
   { ai: ["对你来说，汉语什么最难？", "", "Với bạn, tiếng Hán cái gì khó nhất?"], hint: "对我来说，……最难 (声调 / 汉字 / 语法).", say: [{ ans: ["对我来说，声调最难。", "对我来说，汉字最难。"], re: "难|对我来说" }] },
   { ai: ["你因为说错闹过笑话吗？", "", "Bạn đã bao giờ làm trò cười vì nói sai chưa?"], hint: "闹过 / 没闹过; 我把……说成了……", say: [
     { ans: ["闹过，我把“水饺”说成了“睡觉”。"], re: "闹过|说成|把", react: ["哈哈，太可笑了！", "", "Haha, buồn cười quá!"] },
     { ans: ["没闹过。"], re: "没", react: ["你的发音一定很准！", "", "Phát âm của bạn chắc chắn rất chuẩn!"] }] },
   { ai: ["别人听不懂的时候，你怎么办？", "", "Khi người khác nghe không hiểu, bạn làm sao?"], hint: "比画 / 写下来 / 说慢一点儿.", say: [{ ans: ["我一边说一边比画。", "我把字写下来。"], re: "比画|写|慢" }] },
   { ai: ["我想买一个软一点儿的枕头，你知道哪儿卖吗？", "", "Mình muốn mua cái gối mềm hơn, bạn biết chỗ nào bán không?"], hint: "超市 / 商店 + 层.", say: [{ ans: ["超市二层卖枕头。"], re: "超市|商店|层|卖" }] },
   { ai: ["这么多东西，我一个人拿得了吗？", "", "Nhiều đồ thế này, mình một mình cầm nổi sao?"], hint: "Câu hỏi tu từ = 拿不了 → 我帮你拿吧.", say: [{ ans: ["你拿不了，我帮你拿吧。"], re: "拿不了|帮" }] }] },
 13: { title: "Vì sao bạn học tiếng Hán?", turns: [
   { ai: ["除了汉语以外，你还会什么语言？", "", "Ngoài tiếng Hán, bạn còn biết ngôn ngữ nào?"], hint: "除了汉语以外，我还会……", say: [{ ans: ["除了汉语以外，我还会英语。"], re: "除了|还|会" }] },
   { ai: ["你为什么选择学习汉语？", "", "Vì sao bạn chọn học tiếng Hán?"], hint: "因为…… (有用 / 喜欢中国文化 / 工作需要).", say: [{ ans: ["因为汉语很有用。", "因为我喜欢中国文化。"], re: "因为|喜欢|有用|需要" }] },
   { ai: ["你学汉语多长时间了？", "", "Bạn học tiếng Hán bao lâu rồi?"], hint: "我学了……了.", say: [{ ans: ["我学了一年多了。"], re: "年|月|半" }] },
   { ai: ["下课以后，你一般做什么？", "", "Tan học bạn thường làm gì?"], hint: "不是……就是……", say: [{ ans: ["我不是在家做作业，就是去打球。"], re: "不是|就是|.{4,}" }] },
   { ai: ["你们班同学个个都很努力吗？", "", "Bạn trong lớp ai cũng chăm chỉ à?"], hint: "个个都……", say: [{ ans: ["对，我们班同学个个都很努力。"], re: "个个|都|努力" }] }] },
 14: { title: "Đi taxi và mất đồ", turns: [
   { ai: ["你常常打的吗？", "", "Bạn có hay đi taxi không?"], hint: "常常 / 很少 / 从来没……", say: [
     { ans: ["我很少打的，常坐地铁。"], re: "很少|不|没|地铁", react: ["坐地铁又便宜又快。", "", "Đi tàu điện vừa rẻ vừa nhanh."] },
     { ans: ["我常常打的。"], re: "常常|经常", react: ["打的挺方便的。", "", "Đi taxi khá tiện."] }] },
   { ai: ["你丢过东西吗？", "", "Bạn đã từng mất đồ chưa?"], hint: "我的……丢过 / 被……弄丢了.", say: [{ ans: ["我的手机丢过一次。", "我从来没丢过东西。"], re: "丢|没" }] },
   { ai: ["后来找回来了吗？", "", "Sau đó tìm lại được không?"], hint: "幸好…… / 没找回来.", say: [{ ans: ["幸好有人给我送回来了。", "没找回来。"], re: "幸好|找|没|送" }] },
   { ai: ["我的自行车不见了！", "", "Xe đạp của mình biến mất rồi!"], hint: "是不是被人骑走了？", say: [{ ans: ["是不是被人骑走了？"], re: "被|偷|骑走" }] },
   { ai: ["谢谢你帮我找到了！", "", "Cảm ơn bạn đã giúp mình tìm thấy!"], hint: "谢什么！这是我应该做的.", say: [{ ans: ["谢什么！这是我应该做的。"], re: "谢什么|不用谢|应该" }] }] },
 15: { title: "Thú cưng của bạn", turns: [
   { ai: ["你家养小动物吗？", "", "Nhà bạn có nuôi con vật nhỏ nào không?"], hint: "养了一只…… / 没养.", say: [
     { ans: ["我家养了一只小猫。"], re: "养了|有", react: ["真可爱！它叫什么名字？", "", "Dễ thương quá! Nó tên gì?"], next: "name" },
     { ans: ["我家没养。"], re: "没|不", react: ["你想养吗？", "", "Bạn có muốn nuôi không?"] }] },
   { id: "name", ai: [], hint: "它叫……", say: [{ ans: ["它叫咪咪。"], re: "叫|.{2,}" }] },
   { ai: ["养小动物好是好，可是有什么麻烦？", "", "Nuôi thú cưng tốt thì tốt, nhưng phiền ở chỗ nào?"], hint: "好是好，可是……", say: [{ ans: ["好是好，可是要天天照顾它。"], re: "好是好|可是|但是|就是" }] },
   { ai: ["朋友难过的时候，你怎么安慰他？", "", "Khi bạn bè buồn, bạn an ủi thế nào?"], hint: "我会说：别难过……", say: [{ ans: ["我会陪他聊聊天儿。", "我会说：别难过，耐心点儿。"], re: "安慰|陪|别|说" }] },
   { ai: ["作业写完了吗？", "", "Bài tập viết xong chưa?"], hint: "早就写完了 / 还没写完呢.", say: [{ ans: ["作业早就写完了。", "还没写完呢。"], re: "写完|没" }] }] },
 16: { title: "Đúng giờ", turns: [
   { ai: ["你是个守时的人吗？", "", "Bạn có phải người đúng giờ không?"], hint: "很守时 / 有时候迟到.", say: [
     { ans: ["我很守时，从来不迟到。"], re: "守时|不迟到", react: ["太好了，爱惜时间的人才能成功。", "", "Tốt quá, người quý thời gian mới thành công."] },
     { ans: ["我有时候会迟到。"], re: "迟到|有时", react: ["你为什么不把表拨快几分钟呢？", "", "Sao bạn không chỉnh đồng hồ nhanh vài phút?"] }] },
   { ai: ["明天的会几点开始？", "", "Cuộc họp mai mấy giờ bắt đầu?"], hint: "……点 + 我们提前……到吧.", say: [{ ans: ["九点开始，我们提前十分钟到吧。"], re: "点|提前" }] },
   { ai: ["对不起，我又迟到了。", "", "Xin lỗi, mình lại đến muộn rồi."], hint: "Câu hỏi tu từ: 你为什么不早点儿出门呢？", say: [{ ans: ["你为什么不早点儿出门呢？"], re: "为什么|难道|怎么" }] },
   { ai: ["路上堵车太严重了！", "", "Trên đường tắc khủng khiếp!"], hint: "那你应该改乘地铁.", say: [{ ans: ["那你下次改乘地铁吧。"], re: "地铁|提前|早" }] },
   { ai: ["你最大的优点是什么？", "", "Ưu điểm lớn nhất của bạn là gì?"], hint: "我最大的优点是……", say: [{ ans: ["我最大的优点是很认真。"], re: "优点|是" }] }] },
 17: { title: "Hẹn hò", turns: [
   { ai: ["这个周末我们约会吧，好吗？", "", "Cuối tuần này mình hẹn nhau nhé?"], hint: "好啊 / 对不起，我有事.", say: [
     { ans: ["好啊！在哪儿见面？"], re: "好|行|可以", react: ["市中心广场，晚上七点。", "", "Quảng trường trung tâm, 7 giờ tối."] },
     { ans: ["对不起，这个周末我有事。"], re: "对不起|有事|不行", react: ["那下个周末吧。", "", "Vậy cuối tuần sau nhé."] }] },
   { ai: ["你到底去不去？", "", "Rốt cuộc bạn có đi không?"], hint: "去 / 不去 + 到底.", say: [{ ans: ["去，我一定去。"], re: "去" }] },
   { ai: ["尽管很忙，你还会来吗？", "", "Dù bận, bạn vẫn đến chứ?"], hint: "尽管很忙，我还是会来.", say: [{ ans: ["尽管很忙，我还是会来的。"], re: "尽管|还是|会" }] },
   { ai: ["你一个人的时候会感到寂寞吗？", "", "Ở một mình bạn có thấy cô đơn không?"], hint: "有时候会 / 不会.", say: [{ ans: ["有时候会感到寂寞。", "不会，我喜欢一个人。"], re: "寂寞|会|不" }] },
   { ai: ["时间过得真快啊！", "", "Thời gian trôi nhanh thật!"], hint: "不知不觉……", say: [{ ans: ["是啊，不知不觉一年过去了。"], re: "不知不觉|快" }] }] },
 18: { title: "Làm tình nguyện viên", turns: [
   { ai: ["你做过志愿者吗？", "", "Bạn đã làm tình nguyện viên chưa?"], hint: "做过 / 没做过.", say: [
     { ans: ["做过，我去老人院帮过忙。"], re: "做过", react: ["你真了不起！", "", "Bạn giỏi thật!"] },
     { ans: ["没做过，以后想做。"], re: "没", react: ["我们周末一起去吧。", "", "Cuối tuần mình cùng đi nhé."] }] },
   { ai: ["即使下雨，你也去吗？", "", "Cho dù mưa bạn cũng đi chứ?"], hint: "即使……也……", say: [{ ans: ["即使下雨，我也去。"], re: "即使|也" }] },
   { ai: ["我们那儿有多少志愿者？", "", "Chỗ chúng ta có bao nhiêu tình nguyện viên?"], hint: "二十来个 / 三十左右.", say: [{ ans: ["有二十来个志愿者。"], re: "来|左右|多" }] },
   { ai: ["你能给盲人讲讲“绿色”是什么样子的吗？", "", "Bạn có thể nói cho người khiếm thị “màu xanh lá” trông thế nào không?"], hint: "绿色就是……的颜色.", say: [{ ans: ["绿色就是小草和蔬菜的颜色。"], re: "颜色|草|树|蔬菜" }] },
   { ai: ["今天天气怎么样？", "", "Hôm nay thời tiết thế nào?"], hint: "暖和得像……似的.", say: [{ ans: ["今天暖和得像春天似的。"], re: "像|似的|.{3,}" }] }] },
 19: { title: "Bạn qua thư, bạn qua mạng", turns: [
   { ai: ["你有笔友或者网友吗？", "", "Bạn có bạn qua thư hay bạn qua mạng không?"], hint: "有一个……网友 / 没有.", say: [
     { ans: ["我有一个中国网友。"], re: "有", react: ["你们常常聊天儿吗？", "", "Các bạn có hay trò chuyện không?"] },
     { ans: ["我没有。"], re: "没", react: ["找一个吧，可以练习汉语。", "", "Tìm một người đi, có thể luyện tiếng Hán."] }] },
   { ai: ["怎样才能提高汉语水平？", "", "Làm sao mới nâng cao được trình độ tiếng Hán?"], hint: "只有……才……", say: [{ ans: ["只有多听多说，才能提高。"], re: "只有|才" }] },
   { ai: ["你曾经给谁写过信？", "", "Bạn đã từng viết thư cho ai?"], hint: "我曾经给……写过信.", say: [{ ans: ["我曾经给妈妈写过信。"], re: "曾经|写过|给" }] },
   { ai: ["今天下大雨了，你没淋湿吧？", "", "Hôm nay mưa to, bạn không bị ướt chứ?"], hint: "好在我带了伞.", say: [{ ans: ["没有，好在我带了伞。"], re: "好在|幸好|带" }] },
   { ai: ["问别人的工资礼貌吗？", "", "Hỏi lương người khác có lịch sự không?"], hint: "是不礼貌的.", say: [{ ans: ["问别人的工资是不礼貌的。"], re: "礼貌|不" }] }] },
 20: { title: "Sống bằng lao động", turns: [
   { ai: ["你觉得女主人的做法怎么样？", "", "Bạn thấy cách làm của bà chủ thế nào?"], hint: "我觉得她很了不起 / ……", say: [{ ans: ["我觉得她很了不起。"], re: "了不起|好|对|觉得" }] },
   { ai: ["“靠劳动吃饭”是什么意思？", "", "“Sống bằng lao động” nghĩa là gì?"], hint: "就是用自己的劳动换来生活.", say: [{ ans: ["就是用自己的劳动生活。"], re: "劳动|自己|努力" }] },
   { ai: ["你从什么时候起开始工作或者学习汉语的？", "", "Bạn bắt đầu đi làm hay học tiếng Hán từ khi nào?"], hint: "从……起.", say: [{ ans: ["从去年起，我开始学汉语。"], re: "从|起|开始" }] },
   { ai: ["我明天一个人去爬山。", "", "Mai mình đi leo núi một mình."], hint: "千万要小心 / 千万别……", say: [{ ans: ["你千万要小心！"], re: "千万" }] },
   { ai: ["你妈妈明天来看你，你要做什么？", "", "Mai mẹ bạn đến thăm, bạn sẽ làm gì?"], hint: "我得把房间打扫打扫.", say: [{ ans: ["我得把房间打扫打扫。"], re: "把|打扫|收拾" }] }] },
};
Object.entries(TALK_GB2).forEach(([n, t]) => { if(GB_LESSONS2[n]) GB_LESSONS2[n].talk = t; });
