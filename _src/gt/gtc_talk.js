/* Hội thoại theo bài – sơ cấp 1, bài 21–30 (phiên âm tự điền) */
const TALK_GC = {
 21: { title: "Ăn xong ai trả tiền?", turns: [
   { ai: ["今天的菜真好吃！服务员，结账！", "", "Món hôm nay ngon thật! Phục vụ ơi, tính tiền!"], hint: "Đề nghị chia tiền: 咱们AA制，好吗？", say: [{ ans: ["咱们AA制，好吗？", "今天我请客。"], re: "AA|请客|付|好吗" }] },
   { ai: ["好啊。一共两百块，每人五十。", "", "Được. Tổng cộng 200 tệ, mỗi người 50."], hint: "Đưa tiền: 给你五十块。", say: [{ ans: ["给你五十块。"], re: "给|五十|块|钱" }] },
   { ai: ["这些菜没吃完，打包吗？", "", "Những món này ăn chưa hết, gói về không?"], hint: "打包吧 / 不用了.", say: [
     { ans: ["打包吧。"], re: "^(好|行)?.?打包", react: ["好，我请服务员把饭盒放在袋子里。", "", "Được, mình nhờ phục vụ để hộp cơm vào túi."], next: "where" },
     { ans: ["不用了。"], re: "不", react: ["好吧。", "", "Được thôi."], next: "tip" }] },
   { id: "where", ai: ["袋子你放在哪儿了？", "", "Cái túi bạn để đâu rồi?"], hint: "Dùng 把: 我把袋子放在……了.", say: [{ ans: ["我把袋子放在桌子上了。"], re: "把.*放在|放在" }] },
   { id: "tip", ai: ["你们国家吃饭要给小费吗？", "", "Ở nước bạn ăn cơm có phải cho tiền boa không?"], hint: "要给 / 不用给.", say: [{ ans: ["一般不用给小费。", "要给一点儿小费。"], re: "小费|给|不" }] },
   { ai: ["你习惯中国人的做法吗？", "", "Bạn quen cách làm của người Trung Quốc chưa?"], hint: "习惯了 / 还不太习惯.", say: [{ ans: ["我已经习惯了。", "我还不太习惯，要慢慢习惯。"], re: "习惯" }] }] },
 22: { title: "Đi mua quần áo", turns: [
   { ai: ["欢迎光临！您想买什么？", "", "Chào mừng quý khách! Anh/chị muốn mua gì?"], hint: "我想买一件上衣 / 一条裤子.", say: [{ ans: ["我想买一件上衣。", "我想买一条裤子。"], re: "买|件|条|双" }] },
   { ai: ["您喜欢什么颜色的？", "", "Anh/chị thích màu gì?"], hint: "我喜欢……色的.", say: [{ ans: ["我喜欢蓝色的。", "红色的。"], re: "色|红|蓝|黑|白|黄|绿" }] },
   { ai: ["这件怎么样？您试试吧，那边有试衣间。", "", "Chiếc này thế nào? Anh/chị thử đi, đằng kia có phòng thử đồ."], hint: "Nhận xét: 有点儿瘦 / 有点儿短 / 正好.", say: [
     { ans: ["有点儿瘦，能不能换一件肥点儿的？"], re: "有点儿|瘦|短|肥|长|换", react: ["您再试试这件。", "", "Anh/chị thử chiếc này xem."], next: "ok" },
     { ans: ["不大不小，正好。"], re: "正好|合适|不错", react: ["这件您穿特别合适。", "", "Chiếc này anh/chị mặc rất hợp."], next: "price" }] },
   { id: "ok", ai: [], hint: "这件正好.", say: [{ ans: ["这件正好。"], re: ".{2,}" }] },
   { id: "price", ai: ["您还需要什么？", "", "Anh/chị còn cần gì nữa không?"], hint: "Hỏi giá: 多少钱？", say: [{ ans: ["不要了，多少钱？"], re: "多少钱|几块|不要" }] },
   { ai: ["三百块。", "", "Ba trăm tệ."], hint: "Nhận xét giá: 太贵了 / 才三百，不贵.", say: [{ ans: ["太贵了，便宜点儿吧。", "才三百，不贵。"], re: "贵|便宜|才" }] }] },
 23: { title: "Thời tiết và sức khỏe", turns: [
   { ai: ["今天真冷啊！现在多少度？", "", "Hôm nay lạnh thật! Bây giờ bao nhiêu độ?"], hint: "零下……度左右.", say: [{ ans: ["零下五度左右。"], re: "度|左右|零下" }] },
   { ai: ["你们国家冬天也这么冷吗？", "", "Mùa đông nước bạn cũng lạnh thế này à?"], hint: "没有这么冷 / 不冷 / 差不多.", say: [{ ans: ["我们那儿冬天不冷。", "差不多一样冷。"], re: "冷|热|暖|差不多" }] },
   { ai: ["你习惯北京的气候了吗？", "", "Bạn quen khí hậu Bắc Kinh chưa?"], hint: "习惯了 / 还没习惯.", say: [
     { ans: ["我已经习惯了。"], re: "^(我)?(已经)?习惯了", react: ["那就好。", "", "Vậy thì tốt."], next: "ex" },
     { ans: ["还没习惯，我常常感冒。"], re: "没|感冒|不", react: ["出门的时候多穿点儿衣服。", "", "Ra ngoài thì mặc nhiều áo vào."], next: "ex" }] },
   { id: "ex", ai: ["你常常锻炼身体吗？", "", "Bạn có thường tập thể dục không?"], hint: "常常锻炼 / 不常锻炼.", say: [{ ans: ["我每天早上锻炼。", "我不常锻炼。"], re: "锻炼|跑|不" }] },
   { ai: ["你最近身体怎么样？", "", "Dạo này sức khỏe bạn thế nào?"], hint: "还可以 / 很好 / 好点儿了.", say: [{ ans: ["还可以。", "好点儿了。"], re: "还可以|好|不错" }] },
   { ai: ["你最喜欢哪个季节？", "", "Bạn thích mùa nào nhất?"], hint: "我最喜欢……天.", say: [{ ans: ["我最喜欢秋天，不冷也不热。"], re: "春|夏|秋|冬" }] }] },
 24: { title: "Lời mời dự tiệc", turns: [
   { ai: ["喂，你看到我的邮件了吗？", "", "Alô, bạn xem email của mình chưa?"], hint: "看到了 / 还没看.", say: [{ ans: ["看到了。", "还没看呢。"], re: "看到|看了|没" }] },
   { ai: ["下个星期六我们举行晚会，你能来参加吗？", "", "Thứ Bảy tuần sau chúng mình tổ chức tiệc, bạn đến dự được không?"], hint: "能 / 不能 (nói lý do).", say: [
     { ans: ["能，我一定去。"], re: "^(能|好|行|一定|当然)", react: ["太好了！你可以带朋友一起来。", "", "Tốt quá! Bạn có thể dẫn bạn bè đến cùng."], next: "where" },
     { ans: ["对不起，那天我有事。"], re: "不|有事|对不起", react: ["真可惜，下次吧。", "", "Tiếc thật, lần sau nhé."], next: "end" }] },
   { id: "where", ai: [], hint: "Hỏi địa điểm: 晚会在哪儿举行？", say: [{ ans: ["晚会在哪儿举行？"], re: "哪儿|地址|在" }] },
   { ai: ["在国际大厦四层，友谊宾馆东边就是。", "", "Ở tầng 4 Tòa nhà Quốc tế, ngay phía đông khách sạn Hữu Nghị."], hint: "Nếu không biết đường: 我不知道怎么走.", say: [{ ans: ["我不知道怎么走。", "我知道，谢谢！"], re: ".{2,}" }] },
   { ai: ["这样吧，下午四点你到我宿舍来，跟我一起过去。", "", "Thế này nhé, 4 giờ chiều bạn đến ký túc xá mình, cùng mình đi qua đó."], hint: "Đồng ý: 好啊！", say: [{ ans: ["好啊！"], re: "好|行|没问题" }] },
   { id: "end", ai: ["如果有问题，就给我发短信。", "", "Nếu có gì thì nhắn tin cho mình."], hint: "好的 / 没问题.", say: [{ ans: ["好的，再见！"], re: "好|行|再见|没问题" }] }] },
 25: { title: "Thăm bạn ốm", turns: [
   { ai: ["你现在感觉怎么样了？", "", "Bây giờ bạn cảm thấy thế nào rồi?"], hint: "好点儿了 / 还不太好.", say: [{ ans: ["好点儿了。", "还不太好。"], re: "好|不" }] },
   { ai: ["别着急，你应该好好儿休息休息。这是你喜欢的水果。", "", "Đừng vội, bạn nên nghỉ ngơi cho tốt. Đây là hoa quả bạn thích."], hint: "Cảm ơn: 谢谢你的关心！", say: [{ ans: ["谢谢你的关心！"], re: "谢" }] },
   { ai: ["在医院里，你能听懂医生说的话吗？", "", "Ở bệnh viện, bạn nghe hiểu bác sĩ nói không?"], hint: "听得懂 / 听不懂.", say: [
     { ans: ["他们说得很慢，我都能听懂。"], re: "听得懂|能听懂|都懂|懂", react: ["你的汉语进步真大！", "", "Tiếng Hán bạn tiến bộ thật!"] },
     { ans: ["有的听不懂。"], re: "听不懂|不懂", react: ["没关系，慢慢就好了。", "", "Không sao, từ từ sẽ ổn."] }] },
   { ai: ["你常跟中国人聊天儿吗？你们都谈些什么？", "", "Bạn hay nói chuyện với người Trung Quốc không? Thường nói gì?"], hint: "我们谈…… (生活 / 文化 / 学习).", say: [{ ans: ["我们常谈中国人的生活。"], re: "谈|聊|生活|文化|学习|.{4,}" }] },
   { ai: ["虽然你学汉语的时间不长，但是说得很好。", "", "Tuy bạn học tiếng Hán chưa lâu nhưng nói rất giỏi."], hint: "Khiêm tốn: 哪里，哪里 / 谢谢.", say: [{ ans: ["哪里，哪里。", "谢谢！"], re: "哪里|谢" }] },
   { ai: ["你觉得练习汉语最好的方法是什么？", "", "Bạn thấy cách luyện tiếng Hán tốt nhất là gì?"], hint: "多听、多说.", say: [{ ans: ["多听、多说是最好的方法。"], re: "多|方法|.{3,}" }] }] },
 26: { title: "Kỳ nghỉ sắp đến", turns: [
   { ai: ["圣诞节快要到了，你们那儿过圣诞节吗？", "", "Giáng sinh sắp đến rồi, chỗ bạn có đón Giáng sinh không?"], hint: "过 / 不过 (我们过春节).", say: [{ ans: ["我们也过圣诞节。", "我们不过圣诞节，我们过春节。"], re: "过" }] },
   { ai: ["过节以前，你们要准备什么？", "", "Trước ngày lễ các bạn chuẩn bị gì?"], hint: "准备礼物、好吃的…", say: [{ ans: ["我们要准备礼物和好吃的。"], re: "准备|礼物|吃|买" }] },
   { ai: ["听说要放五天假，你打算怎么过？", "", "Nghe nói được nghỉ năm ngày, bạn định đón thế nào?"], hint: "我打算……", say: [
     { ans: ["我打算去外地旅游。"], re: "旅游|旅行|去", react: ["真好！祝你玩儿得愉快。", "", "Hay quá! Chúc bạn chơi vui."] },
     { ans: ["我想在家学习。"], re: "学习|在家|休息", react: ["放假也不休息啊？你学习太认真了。", "", "Nghỉ mà cũng không nghỉ à? Bạn học chăm quá."] }] },
   { ai: ["你给家人买礼物了吗？", "", "Bạn mua quà cho gia đình chưa?"], hint: "买了 / 还没买.", say: [{ ans: ["买了，我已经寄去了。", "还没买呢。"], re: "买|寄|没" }] },
   { ai: ["要是不放假，你会怎么样？", "", "Nếu không được nghỉ thì bạn sẽ thế nào?"], hint: "要是不放假，我就……", say: [{ ans: ["要是不放假，我就不能去旅游了。"], re: "就|不能|没意思|.{3,}" }] }] },
 27: { title: "Bạn đang làm gì?", turns: [
   { ai: ["喂，你在忙什么呢？", "", "Alô, bạn đang bận gì thế?"], hint: "我正在……呢.", say: [{ ans: ["我正在看电视呢。", "我在写作业呢。"], re: "在|正|呢" }] },
   { ai: ["我刚才给你打电话，你怎么没接？", "", "Vừa nãy mình gọi sao bạn không nghe?"], hint: "对不起，我没听见.", say: [{ ans: ["对不起，我没听见。"], re: "没听见|对不起|没" }] },
   { ai: ["明天早上六点，咱们一起去公园打太极拳，怎么样？", "", "Sáng mai 6 giờ, chúng mình cùng ra công viên tập thái cực quyền nhé?"], hint: "好啊 / 太早了.", say: [
     { ans: ["好啊！"], re: "^(好|行|没问题)", react: ["别忘了，草地旁边见。", "", "Đừng quên nhé, gặp ở cạnh bãi cỏ."] },
     { ans: ["六点，太早了！"], re: "早|不", react: ["不早，很多人五点半就起床了。", "", "Không sớm đâu, nhiều người 5 rưỡi đã dậy rồi."] }] },
   { ai: ["你喜欢一边做什么一边做什么？", "", "Bạn thích vừa làm gì vừa làm gì?"], hint: "我喜欢一边……一边……", say: [{ ans: ["我喜欢一边吃饭一边看电视。"], re: "一边" }] },
   { ai: ["你们那儿现在几点了？", "", "Chỗ bạn bây giờ mấy giờ rồi?"], hint: "我们这儿……点.", say: [{ ans: ["我们这儿十点。"], re: "点" }] },
   { ai: ["不早了，晚安！", "", "Muộn rồi, chúc ngủ ngon!"], hint: "晚安！", say: [{ ans: ["晚安！"], re: "晚安|再见" }] }] },
 28: { title: "Đi Trường Thành", turns: [
   { ai: ["你去过长城吗？", "", "Bạn đã đến Trường Thành chưa?"], hint: "去过 / 没去过.", say: [
     { ans: ["我去过八达岭长城。"], re: "^(我)?去过", react: ["你是怎么去的？", "", "Bạn đi bằng gì?"], next: "how" },
     { ans: ["还没去过。"], re: "没", react: ["这个周末我们一起去吧！", "", "Cuối tuần này chúng mình cùng đi nhé!"], next: "how" }] },
   { id: "how", ai: [], hint: "坐火车 / 坐旅游车 / 坐公共汽车.", say: [{ ans: ["坐火车去的。", "坐火车去吧。"], re: "坐|火车|汽车|旅游车" }] },
   { ai: ["从市区到八达岭要多长时间？", "", "Từ nội thành đến Bát Đạt Lĩnh mất bao lâu?"], hint: "两个多小时 / 四十多分钟.", say: [{ ans: ["坐火车两个多小时。"], re: "小时|分钟|多" }] },
   { ai: ["车票多少钱？", "", "Vé bao nhiêu tiền?"], hint: "十几块钱 / 五十元.", say: [{ ans: ["十几块钱。"], re: "块|元|钱|几|多" }] },
   { ai: ["你知道长城有多长吗？", "", "Bạn biết Trường Thành dài bao nhiêu không?"], hint: "八千八百五十多公里.", say: [{ ans: ["长城有八千八百五十多公里。"], re: "公里|八千|万|不知道" }] },
   { ai: ["为什么叫“万里长城”呢？", "", "Sao lại gọi là “Vạn Lý Trường Thành”?"], hint: "一公里是二里…… / 不知道.", say: [{ ans: ["因为一公里是二里，长城有一万多里。", "我不知道。"], re: "里|因为|不知道" }] }] },
 29: { title: "Sau buổi tiệc", turns: [
   { ai: ["昨天的晚会开得怎么样？", "", "Buổi tiệc hôm qua thế nào?"], hint: "开得非常成功.", say: [{ ans: ["晚会开得非常成功。"], re: "得|成功|好" }] },
   { ai: ["大家玩儿得怎么样？", "", "Mọi người chơi thế nào?"], hint: "玩儿得很痛快 / 很高兴.", say: [{ ans: ["大家玩儿得很痛快。"], re: "得|高兴|痛快" }] },
   { ai: ["你唱歌唱得真好！", "", "Bạn hát hay thật!"], hint: "Khiêm tốn: 哪里，哪里.", say: [{ ans: ["哪里，哪里。"], re: "哪里|谢|不" }] },
   { ai: ["你有什么爱好？", "", "Bạn có sở thích gì?"], hint: "我爱…… / 我喜欢…….", say: [{ ans: ["我爱游泳。", "我喜欢跳舞。"], re: "爱|喜欢" }] },
   { ai: ["你游泳游得怎么样？", "", "Bạn bơi thế nào?"], hint: "游得不错 / 游得不太好 / 不会.", say: [{ ans: ["我游得还不错。", "我游得不太好。", "我不会游泳。"], re: "得|不会" }] },
   { ai: ["你每个月生活费要花多少钱？", "", "Mỗi tháng bạn tiêu bao nhiêu sinh hoạt phí?"], hint: "大概……块.", say: [{ ans: ["大概三千块。"], re: "块|千|百|元|钱" }] }] },
 30: { title: "Trải nghiệm của bạn", turns: [
   { ai: ["你去过哪些地方？", "", "Bạn từng đến những nơi nào?"], hint: "我去过……", say: [{ ans: ["我去过北京和上海。"], re: "去过|没去过" }] },
   { ai: ["你打过工吗？", "", "Bạn từng làm thêm chưa?"], hint: "打过 / 没打过.", say: [
     { ans: ["打过，我当过翻译。"], re: "^(我)?打过|当过", react: ["真不错！你觉得怎么样？", "", "Tốt quá! Bạn thấy thế nào?"], next: "feel" },
     { ans: ["没打过。"], re: "没", react: ["你想打工吗？", "", "Bạn có muốn làm thêm không?"], next: "feel" }] },
   { id: "feel", ai: [], hint: "Nói cảm nhận hoặc mong muốn.", say: [{ ans: ["很有意思，也很累。", "我想打工。"], re: ".{2,}" }] },
   { ai: ["你刚来的时候，遇到过什么困难？", "", "Lúc mới đến bạn từng gặp khó khăn gì?"], hint: "因为汉语不好，交流很困难…", say: [{ ans: ["因为汉语说得不好，跟中国人交流很困难。"], re: "困难|麻烦|听不懂|.{4,}" }] },
   { ai: ["当你想家的时候，你做什么？", "", "Khi nhớ nhà bạn làm gì?"], hint: "当我想家的时候，我就……", say: [{ ans: ["当我想家的时候，我就给妈妈打电话。"], re: "打电话|看|.{4,}" }] },
   { ai: ["以后你想做什么工作？", "", "Sau này bạn muốn làm việc gì?"], hint: "我想当……", say: [{ ans: ["我想当翻译。", "我想当汉语老师。"], re: "想|当|做" }] }] },
};
Object.entries(TALK_GC).forEach(([n, t]) => { if(GC_LESSONS3[n]) GC_LESSONS3[n].talk = t; });
