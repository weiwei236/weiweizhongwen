/**
 * 薇薇中文 – Máy chủ tài khoản học viên & theo dõi tiến độ (Google Apps Script)
 *
 * CÁCH CÀI (làm 1 lần):
 * 1. Tạo một Google Sheet mới, đặt tên ví dụ "Weiwei - Học viên".
 * 2. Menu Tiện ích mở rộng (Extensions) → Apps Script. Xoá hết mã mẫu, dán toàn bộ file này vào, bấm Lưu.
 * 3. Bên trái chọn Cài đặt dự án (Project Settings) → Thuộc tính tập lệnh (Script properties)
 *    → Thêm thuộc tính: Tên = TEACHER_KEY, Giá trị = mật khẩu giáo viên của bạn. Lưu.
 * 4. Bấm Triển khai (Deploy) → Tùy chọn triển khai mới (New deployment) → loại "Ứng dụng web" (Web app):
 *      - Thực thi dưới dạng (Execute as): Tôi (Me)
 *      - Người có quyền truy cập (Who has access): Bất kỳ ai (Anyone)
 *    Bấm Triển khai, cấp quyền, rồi sao chép "URL ứng dụng web" (kết thúc bằng /exec) gửi cho Claude.
 *
 * File nghe của bài đọc được lưu trong thư mục Google Drive "Weiwei - File nghe bài đọc" (tự tạo).
 * Lần đầu dùng: chọn hàm capQuyenDrive ở thanh trên cùng → bấm Chạy (Run) → cấp quyền truy cập Drive.
 *
 * Khi sửa mã này về sau: Triển khai → Quản lý các bản triển khai → biểu tượng bút chì → Phiên bản: "Phiên bản mới" → Triển khai.
 * (Làm như vậy để giữ nguyên URL.)
 *
 * Trang tính được tạo tự động:
 *   Accounts – mỗi học viên một dòng (tên đăng nhập, SĐT, họ tên, lớp, trình độ, mật khẩu đã mã hoá, dữ liệu học tập).
 *   Events   – nhật ký hoạt động học tập (dùng cho bảng theo dõi của giáo viên).
 *   Tests, TestAttempts, TestEvents – bài kiểm tra (đề + mật khẩu, bài làm của học viên, nhật ký cảnh báo gian lận).
 *   Readings – các bài đọc giáo viên soạn trên trang web (chỉ giáo viên có mật khẩu mới thêm/sửa/xoá được).
 * Mật khẩu KHÔNG được lưu dạng chữ thường, chỉ lưu bản mã hoá (SHA-256 + muối).
 */
const EVENTS = 'Events', ACCOUNTS = 'Accounts';
const EV_HEAD = ['Thời gian', 'Mã sự kiện', 'Mã học viên', 'Họ tên', 'Lớp', 'Trình độ', 'Loại', 'Bài', 'Chi tiết (JSON)'];
const AC_HEAD = ['Tên đăng nhập', 'Số điện thoại', 'Họ tên', 'Lớp', 'Trình độ', 'Muối', 'Mật khẩu (mã hoá)', 'Phiên đăng nhập', 'Ngày đăng ký', 'Đăng nhập gần nhất', 'Cập nhật dữ liệu', 'Dữ liệu học tập (JSON)'];
const C = { user: 1, phone: 2, name: 3, cls: 4, level: 5, salt: 6, hash: 7, tokens: 8, created: 9, last: 10, upd: 11, data: 12 };
const READINGS = 'Readings';
const RD_HEAD = ['Mã', 'Cấp', 'Bài', 'Tiêu đề', 'Cập nhật', 'Nội dung (JSON)'];
const MAX_DATA = 48000; // giới hạn 1 ô Google Sheet là 50.000 ký tự

function sheet_(name, head) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.appendRow(head); sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, head.length).setFontWeight('bold');
    if (name === ACCOUNTS) sh.getRange('A:B').setNumberFormat('@'); // giữ số 0 đầu SĐT
  }
  return sh;
}
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
function str_(v, n) { return String(v == null ? '' : v).slice(0, n); }
function hash_(salt, pw) {
  const raw = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, salt + '|' + pw, Utilities.Charset.UTF_8);
  return raw.map(b => ('0' + (b & 255).toString(16)).slice(-2)).join('');
}
function teacherOk_(key) { const k = PropertiesService.getScriptProperties().getProperty('TEACHER_KEY'); return !!k && key === k; }
function normPhone_(p) { p = String(p || '').replace(/[^\d+]/g, ''); if (p.indexOf('+84') === 0) p = '0' + p.slice(3); return p; }
/* tìm dòng theo tên đăng nhập hoặc số điện thoại; trả về số dòng (bắt đầu từ 2) hoặc 0 */
function findRow_(sh, id) {
  const n = sh.getLastRow() - 1; if (n < 1) return 0;
  const vals = sh.getRange(2, 1, n, 2).getDisplayValues();
  const u = String(id || '').trim().toLowerCase(), ph = normPhone_(id);
  for (let i = 0; i < vals.length; i++) {
    if (vals[i][0].toLowerCase() === u) return i + 2;
    if (ph.length >= 9 && normPhone_(vals[i][1]) === ph) return i + 2;
  }
  return 0;
}
function row_(sh, r) { return sh.getRange(r, 1, 1, AC_HEAD.length).getValues()[0]; }
function tokens_(v) { try { return JSON.parse(v || '[]'); } catch (e) { return []; } }
function authRow_(sh, u, token) {
  const r = findRow_(sh, u); if (!r) return 0;
  return tokens_(sh.getRange(r, C.tokens).getValue()).indexOf(token) >= 0 ? r : 0;
}
function newToken_(sh, r) {
  const t = Utilities.getUuid();
  const list = tokens_(sh.getRange(r, C.tokens).getValue()); list.push(t);
  sh.getRange(r, C.tokens).setValue(JSON.stringify(list.slice(-8))); // tối đa 8 thiết bị đăng nhập cùng lúc
  sh.getRange(r, C.last).setValue(new Date());
  return t;
}
function profileOf_(row) {
  return { username: String(row[C.user - 1]), phone: String(row[C.phone - 1]), name: String(row[C.name - 1]), cls: String(row[C.cls - 1]), level: String(row[C.level - 1]) };
}
function dataOf_(row) { try { return JSON.parse(row[C.data - 1] || '{}'); } catch (e) { return {}; } }

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const b = JSON.parse(e.postData.contents || '{}');
    const act = b.action || (b.events ? 'events' : '');
    const ac = sheet_(ACCOUNTS, AC_HEAD);

    if (act === 'events') {
      const events = (Array.isArray(b.events) ? b.events : []).slice(0, 100), sh = sheet_(EVENTS, EV_HEAD);
      const rows = events.map(x => [new Date(x.t || Date.now()), str_(x.eid, 40), str_(x.sid, 40), str_(x.name, 60), str_(x.cls, 10),
        str_(x.level, 10), str_(x.type, 20), str_(x.lesson, 20), str_(JSON.stringify(x.data || {}), 4000)]);
      if (rows.length) sh.getRange(sh.getLastRow() + 1, 1, rows.length, EV_HEAD.length).setValues(rows);
      return json_({ ok: true, saved: rows.length });
    }

    if (act === 'register') {
      const u = String(b.username || '').trim().toLowerCase(), ph = normPhone_(b.phone), pw = String(b.password || '');
      if (!/^[a-z0-9_.]{3,20}$/.test(u)) return json_({ ok: false, error: 'bad_username' });
      if (!/^0\d{9}$/.test(ph)) return json_({ ok: false, error: 'bad_phone' });
      if (pw.length < 6) return json_({ ok: false, error: 'bad_password' });
      if (findRow_(ac, u)) return json_({ ok: false, error: 'user_taken' });
      if (findRow_(ac, ph)) return json_({ ok: false, error: 'phone_taken' });
      const data = JSON.stringify(b.data || {});
      if (data.length > MAX_DATA) return json_({ ok: false, error: 'too_large' });
      const salt = Utilities.getUuid(), now = new Date();
      ac.appendRow([u, ph, str_(b.name, 60), str_(b.cls, 10), str_(b.level, 10), salt, hash_(salt, pw), '[]', now, now, now, data]);
      const r = ac.getLastRow(); ac.getRange(r, 1, 1, 2).setNumberFormat('@').setValues([[u, ph]]);
      return json_({ ok: true, token: newToken_(ac, r), profile: profileOf_(row_(ac, r)), updatedAt: now.getTime() });
    }

    if (act === 'login') {
      const r = findRow_(ac, b.id); if (!r) return json_({ ok: false, error: 'no_user' });
      const row = row_(ac, r);
      if (hash_(row[C.salt - 1], String(b.password || '')) !== row[C.hash - 1]) return json_({ ok: false, error: 'wrong_password' });
      const t = newToken_(ac, r);
      return json_({ ok: true, token: t, profile: profileOf_(row), data: dataOf_(row), updatedAt: new Date(row[C.upd - 1]).getTime() || 0 });
    }

    if (act === 'load') {
      const r = authRow_(ac, b.u, b.token); if (!r) return json_({ ok: false, error: 'auth' });
      const row = row_(ac, r);
      return json_({ ok: true, profile: profileOf_(row), data: dataOf_(row), updatedAt: new Date(row[C.upd - 1]).getTime() || 0 });
    }

    if (act === 'save') {
      const r = authRow_(ac, b.u, b.token); if (!r) return json_({ ok: false, error: 'auth' });
      const data = JSON.stringify(b.data || {});
      if (data.length > MAX_DATA) return json_({ ok: false, error: 'too_large' });
      const now = new Date(), p = (b.data && b.data.ww_profile) || {};
      if (p.name) ac.getRange(r, C.name, 1, 3).setValues([[str_(p.name, 60), str_(p.cls, 10), str_(p.level, 10)]]);
      ac.getRange(r, C.upd, 1, 2).setValues([[now, data]]);
      return json_({ ok: true, updatedAt: now.getTime() });
    }

    if (act === 'logout') {
      const r = authRow_(ac, b.u, b.token);
      if (r) ac.getRange(r, C.tokens).setValue(JSON.stringify(tokens_(ac.getRange(r, C.tokens).getValue()).filter(x => x !== b.token)));
      return json_({ ok: true });
    }

    if (act === 'changepw') {
      const r = authRow_(ac, b.u, b.token); if (!r) return json_({ ok: false, error: 'auth' });
      const row = row_(ac, r);
      if (hash_(row[C.salt - 1], String(b.old || '')) !== row[C.hash - 1]) return json_({ ok: false, error: 'wrong_password' });
      if (String(b.password || '').length < 6) return json_({ ok: false, error: 'bad_password' });
      const salt = Utilities.getUuid();
      ac.getRange(r, C.salt, 1, 3).setValues([[salt, hash_(salt, String(b.password)), JSON.stringify([b.token])]]);
      return json_({ ok: true });
    }

    /* ---------- giáo viên (cần TEACHER_KEY) ---------- */
    if (act === 'teacher') {
      if (!teacherOk_(b.key)) return json_({ ok: false, error: PropertiesService.getScriptProperties().getProperty('TEACHER_KEY') ? 'unauthorized' : 'no_key' });
      const ev = sheet_(EVENTS, EV_HEAD), n = ev.getLastRow() - 1;
      const events = n < 1 ? [] : ev.getRange(2, 1, n, EV_HEAD.length).getValues().map(r => {
        let data = {}; try { data = JSON.parse(r[8] || '{}'); } catch (err) {}
        return { t: r[0] instanceof Date ? r[0].toISOString() : String(r[0]), eid: r[1], sid: r[2], name: r[3], cls: r[4], level: r[5], type: r[6], lesson: r[7], data: data };
      });
      const m = ac.getLastRow() - 1;
      const accounts = m < 1 ? [] : ac.getRange(2, 1, m, AC_HEAD.length).getValues().map(row => {
        const p = profileOf_(row), d = dataOf_(row);
        p.created = new Date(row[C.created - 1]).getTime() || 0; p.lastLogin = new Date(row[C.last - 1]).getTime() || 0; p.updatedAt = new Date(row[C.upd - 1]).getTime() || 0;
        p.data = d; return p;
      });
      return json_({ ok: true, events: events, accounts: accounts });
    }

    /* xoá dữ liệu một học viên: nhật ký hoạt động (và tuỳ chọn cả tài khoản, bài kiểm tra) */
    if (act === 'deleteStudent') {
      if (!teacherOk_(b.key)) return json_({ ok: false, error: 'unauthorized' });
      const sid = String(b.sid || '').toLowerCase(); if (!sid) return json_({ ok: false, error: 'missing' });
      let removed = filterRows_(sheet_(EVENTS, EV_HEAD), EV_HEAD.length, r => String(r[2]).toLowerCase() !== sid);
      if (b.account) {
        const r = findRow_(ac, sid); if (r) ac.deleteRow(r);
        removed += filterRows_(sheet_(ATT, A_HEAD), A_HEAD.length, r => String(r[2]).toLowerCase() !== sid);
        removed += filterRows_(sheet_(TEV, E_HEAD), E_HEAD.length, r => String(r[2]).toLowerCase() !== sid);
      }
      return json_({ ok: true, removed: removed });
    }

    if (act === 'resetpw') {
      if (!teacherOk_(b.key)) return json_({ ok: false, error: 'unauthorized' });
      const r = findRow_(ac, b.u); if (!r) return json_({ ok: false, error: 'no_user' });
      if (String(b.password || '').length < 6) return json_({ ok: false, error: 'bad_password' });
      const salt = Utilities.getUuid();
      ac.getRange(r, C.salt, 1, 3).setValues([[salt, hash_(salt, String(b.password)), '[]']]); // đăng xuất mọi thiết bị
      return json_({ ok: true });
    }

    /* ---- Bài đọc: ai cũng đọc được; chỉ giáo viên (TEACHER_KEY) được thêm / sửa / xoá ---- */
    if (act === 'readings') {
      const sh = sheet_(READINGS, RD_HEAD), n = sh.getLastRow() - 1;
      const list = n < 1 ? [] : sh.getRange(2, 1, n, RD_HEAD.length).getValues().map(r => { try { return JSON.parse(r[5]); } catch (err) { return null; } }).filter(Boolean);
      return json_({ ok: true, readings: list });
    }
    if (act === 'saveReading') {
      if (!teacherOk_(b.key)) return json_({ ok: false, error: 'unauthorized' });
      const rd = b.reading || {};
      if (!rd.title || !rd.text) return json_({ ok: false, error: 'missing' });
      rd.id = rd.id ? str_(rd.id, 40) : Utilities.getUuid().slice(0, 12);
      rd.updated = Date.now();
      const js = JSON.stringify(rd);
      if (js.length > MAX_DATA) return json_({ ok: false, error: 'too_large' });
      const sh = sheet_(READINGS, RD_HEAD), n = sh.getLastRow() - 1;
      const ids = n < 1 ? [] : sh.getRange(2, 1, n, 1).getValues().map(r => String(r[0]));
      const row = [rd.id, str_(rd.level, 10), Number(rd.lesson) || 0, str_(rd.title, 200), new Date(), js];
      const i = ids.indexOf(rd.id);
      if (i >= 0) sh.getRange(i + 2, 1, 1, RD_HEAD.length).setValues([row]); else sh.appendRow(row);
      return json_({ ok: true, reading: rd });
    }
    if (act === 'deleteReading') {
      if (!teacherOk_(b.key)) return json_({ ok: false, error: 'unauthorized' });
      const sh = sheet_(READINGS, RD_HEAD), n = sh.getLastRow() - 1;
      const ids = n < 1 ? [] : sh.getRange(2, 1, n, 1).getValues().map(r => String(r[0]));
      const i = ids.indexOf(String(b.id || ''));
      if (i >= 0) sh.deleteRow(i + 2);
      return json_({ ok: true });
    }

    /* ---- File nghe bài đọc (Google Drive) ---- */
    if (act === 'uploadAudio') {
      if (!teacherOk_(b.key)) return json_({ ok: false, error: 'unauthorized' });
      if (!b.data) return json_({ ok: false, error: 'missing' });
      const blob = Utilities.newBlob(Utilities.base64Decode(b.data), str_(b.mime, 60) || 'audio/mpeg', str_(b.name, 120) || 'bai-doc.mp3');
      const f = audioFolder_().createFile(blob);
      try { f.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW); } catch (err) {}
      return json_({ ok: true, id: f.getId(), url: f.getUrl() });
    }
    if (act === 'audio') {
      try {
        const f = DriveApp.getFileById(String(b.id || ''));
        if (f.getParents().hasNext() && f.getParents().next().getName() !== AUDIO_FOLDER) return json_({ ok: false, error: 'forbidden' });
        const bl = f.getBlob();
        return json_({ ok: true, mime: bl.getContentType(), data: Utilities.base64Encode(bl.getBytes()) });
      } catch (err) { return json_({ ok: false, error: 'not_found' }); }
    }

    /* ---- Bài kiểm tra ---- */
    if (act.indexOf('test') === 0) { const out = testAction_(act, b, ac); if (out) return json_(out); }

    return json_({ ok: false, error: 'unknown_action' });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

const AUDIO_FOLDER = 'Weiwei - File nghe bài đọc';
function audioFolder_() {
  const it = DriveApp.getFoldersByName(AUDIO_FOLDER);
  return it.hasNext() ? it.next() : DriveApp.createFolder(AUDIO_FOLDER);
}
/* Chạy hàm này 1 lần trong trình soạn Apps Script để cấp quyền Google Drive (lưu file nghe bài đọc) */
function capQuyenDrive() { audioFolder_(); }

/* Bản cũ của bảng giáo viên đọc qua GET – vẫn giữ để tương thích */
function doGet(e) {
  if (!teacherOk_(e.parameter.key || '')) return json_({ ok: false, error: 'unauthorized' });
  return doPost({ postData: { contents: JSON.stringify({ action: 'teacher', key: e.parameter.key }) } });
}


/* ======================= BÀI KIỂM TRA =======================
   Đề (kèm đáp án) chỉ nằm ở Google Sheet này, không nằm trong mã trang web, nên học viên không xem trước được.
   Học viên phải đăng nhập + nhập đúng mật khẩu bài kiểm tra mới nhận được đề (đã bỏ đáp án). */
const TESTS = 'Tests', ATT = 'TestAttempts', TEV = 'TestEvents';
const T_HEAD = ['Mã', 'Tên bài kiểm tra', 'Đang mở', 'Công bố điểm', 'Mật khẩu', 'Cập nhật', 'Đề (JSON)'];
const A_HEAD = ['Khoá', 'Mã bài', 'Tên đăng nhập', 'Họ tên', 'Bắt đầu', 'Lưu gần nhất', 'Nộp bài', 'Bài làm (JSON)', 'Máy chấm (JSON)', 'GV chấm (JSON)', 'Tổng điểm', 'Nộp muộn', 'Số cảnh báo'];
const E_HEAD = ['Thời gian', 'Mã bài', 'Tên đăng nhập', 'Họ tên', 'Loại', 'Chi tiết'];
/* giữ lại các dòng thoả điều kiện, ghi lại một lượt (nhanh hơn xoá từng dòng); trả về số dòng đã xoá */
function filterRows_(sh, n, keep) {
  const rows = rowsOf_(sh, n); if (!rows.length) return 0;
  const kept = rows.filter(keep); if (kept.length === rows.length) return 0;
  sh.getRange(2, 1, rows.length, n).clearContent();
  if (kept.length) sh.getRange(2, 1, kept.length, n).setValues(kept);
  if (sh.getMaxRows() > kept.length + 50) sh.deleteRows(kept.length + 2, sh.getMaxRows() - kept.length - 1);
  return rows.length - kept.length;
}
function rowsOf_(sh, n) { const m = sh.getLastRow() - 1; return m < 1 ? [] : sh.getRange(2, 1, m, n).getValues(); }
function testRow_(id) { const sh = sheet_(TESTS, T_HEAD), rows = rowsOf_(sh, T_HEAD.length);
  for (let i = 0; i < rows.length; i++) if (String(rows[i][0]) === String(id)) return { sh: sh, r: i + 2, row: rows[i] }; return { sh: sh, r: 0, row: null }; }
function testDef_(row) { try { return JSON.parse(row[6]); } catch (e) { return null; } }
function attRow_(id, u) { const sh = sheet_(ATT, A_HEAD), rows = rowsOf_(sh, A_HEAD.length), k = id + '|' + String(u).toLowerCase();
  for (let i = 0; i < rows.length; i++) if (rows[i][0] === k) return { sh: sh, r: i + 2, row: rows[i] }; return { sh: sh, r: 0, row: null, key: k }; }
function pj_(v, d) { try { return v ? JSON.parse(v) : d; } catch (e) { return d; } }
function eachQ_(T, fn) { (T.sections || []).forEach(sec => (sec.parts || []).forEach(p => (p.qs || []).forEach(q => fn(q, p, sec)))); }
function normZh_(s) { return String(s || '').replace(/[\s，。？！、,.?!：:；;“”"'（）()]/g, '').replace(/[０-９]/g, c => String.fromCharCode(c.charCodeAt(0) - 65248)); }
/* máy chấm: trắc nghiệm & sắp xếp chấm hẳn; dịch đúng mẫu thì cho đủ điểm, sai để trống chờ giáo viên; đặt câu chờ giáo viên */
function gradeTest_(T, ans) {
  const auto = {}; let max = 0;
  eachQ_(T, (q, p) => { const pts = Number(p.pts) || 1, a = ans[q.n]; max += pts;
    if (p.type === 'order') auto[q.n] = a && [q.ans].concat(q.alt || []).some(x => normZh_(x) === normZh_(a)) ? pts : 0;
    else if (p.type === 'translate') auto[q.n] = a && (q.ans || []).some(x => normZh_(x) === normZh_(a)) ? pts : null;
    else if (p.type === 'compose') auto[q.n] = null;
    else auto[q.n] = a === q.ans ? pts : 0; });
  return { auto: auto, max: max };
}
function totalOf_(auto, manual) { let t = 0; Object.keys(auto).forEach(n => { const m = manual[n]; t += Number(m != null && m !== '' ? m : (auto[n] || 0)) || 0; }); return Math.round(t * 10) / 10; }
function publicTest_(T) { const c = JSON.parse(JSON.stringify(T)); eachQ_(c, q => { delete q.ans; delete q.alt; delete q.sample; }); return c; }
function testAction_(act, b, ac) {
  const now = new Date();
  if (act === 'testList') {
    const user = b.u && b.token ? (authRow_(ac, b.u, b.token) ? String(b.u).toLowerCase() : '') : '';
    const atts = user ? rowsOf_(sheet_(ATT, A_HEAD), A_HEAD.length).filter(r => String(r[2]).toLowerCase() === user) : [];
    return { ok: true, tests: rowsOf_(sheet_(TESTS, T_HEAD), T_HEAD.length).map(r => { const T = testDef_(r) || {}, a = atts.filter(x => x[1] === r[0])[0];
      return { id: r[0], title: r[1], open: r[2] === true, released: r[3] === true, minutes: T.minutes || 60, level: T.level || '',
        mine: a ? { started: a[4] ? new Date(a[4]).getTime() : 0, submitted: a[6] ? new Date(a[6]).getTime() : 0 } : null }; }) };
  }
  if (act === 'testStart' || act === 'testSave' || act === 'testSubmit' || act === 'testEvent' || act === 'testResult') {
    const r = authRow_(ac, b.u, b.token); if (!r) return { ok: false, error: 'auth' };
    const name = String(ac.getRange(r, C.name).getValue()), u = String(ac.getRange(r, C.user).getValue()).toLowerCase();
    const tr = testRow_(b.id); if (!tr.r) return { ok: false, error: 'no_test' };
    const T = testDef_(tr.row), mins = Number(T.minutes) || 60; let at = attRow_(b.id, u);
    if (act === 'testEvent') {
      const ev = (Array.isArray(b.events) ? b.events : []).slice(0, 30), sh = sheet_(TEV, E_HEAD);
      if (ev.length) sh.getRange(sh.getLastRow() + 1, 1, ev.length, E_HEAD.length).setValues(ev.map(x => [new Date(x.t || now), b.id, u, name, str_(x.type, 30), str_(x.detail, 300)]));
      if (at.r) at.sh.getRange(at.r, 13).setValue((Number(at.row[12]) || 0) + ev.length);
      return { ok: true };
    }
    if (act === 'testResult') {
      if (!at.r || !at.row[6]) return { ok: false, error: 'not_submitted' };
      if (tr.row[3] !== true) return { ok: true, released: false };
      const auto = pj_(at.row[8], {}), manual = pj_(at.row[9], {});
      return { ok: true, released: true, test: T, answers: pj_(at.row[7], {}), auto: auto, manual: manual, total: at.row[10], max: gradeTest_(T, {}).max };
    }
    if (act === 'testStart') {
      if (at.r && at.row[6]) return { ok: true, submitted: true, released: tr.row[3] === true };
      if (!at.r) {
        if (tr.row[2] !== true) return { ok: false, error: 'closed' };
        if (String(b.pass || '').trim() !== String(tr.row[4]).trim() || !String(tr.row[4]).trim()) return { ok: false, error: 'bad_pass' };
        at.sh.appendRow([at.key, b.id, u, name, now, now, '', '{}', '', '', '', '', 0]); at = attRow_(b.id, u);
        sheet_(TEV, E_HEAD).appendRow([now, b.id, u, name, 'start', 'Bắt đầu làm bài']);
      } else sheet_(TEV, E_HEAD).appendRow([now, b.id, u, name, 'resume', 'Mở lại bài đang làm']);
      const start = new Date(at.row[4]).getTime();
      return { ok: true, test: publicTest_(T), answers: pj_(at.row[7], {}), start: start, now: now.getTime(), endsAt: start + mins * 60000 };
    }
    if (!at.r) return { ok: false, error: 'not_started' };
    if (at.row[6]) return { ok: false, error: 'submitted' };
    const ans = b.answers && typeof b.answers === 'object' ? b.answers : {}, js = JSON.stringify(ans);
    if (js.length > MAX_DATA) return { ok: false, error: 'too_large' };
    const late = now.getTime() > new Date(at.row[4]).getTime() + mins * 60000 + 90000;
    if (act === 'testSave') { if (late) return { ok: false, error: 'time_up' }; at.sh.getRange(at.r, 6, 1, 3).setValues([[now, '', js]]); return { ok: true }; }
    const g = gradeTest_(T, ans);
    at.sh.getRange(at.r, 6, 1, 7).setValues([[now, now, js, JSON.stringify(g.auto), '{}', totalOf_(g.auto, {}), late ? 'Có' : '']]);
    sheet_(TEV, E_HEAD).appendRow([now, b.id, u, name, 'submit', late ? 'Nộp bài (muộn)' : (b.auto ? 'Hết giờ – tự nộp' : 'Nộp bài')]);
    return { ok: true, submitted: true };
  }
  /* ---- phần giáo viên ---- */
  if (!teacherOk_(b.key)) return { ok: false, error: 'unauthorized' };
  if (act === 'testAdmin') {
    const ev = rowsOf_(sheet_(TEV, E_HEAD), E_HEAD.length);
    return { ok: true, now: now.getTime(),
      tests: rowsOf_(sheet_(TESTS, T_HEAD), T_HEAD.length).map(r => ({ id: r[0], title: r[1], open: r[2] === true, released: r[3] === true, pass: String(r[4]), test: testDef_(r) })),
      attempts: rowsOf_(sheet_(ATT, A_HEAD), A_HEAD.length).map(r => ({ id: r[1], u: r[2], name: r[3], start: r[4] ? new Date(r[4]).getTime() : 0, last: r[5] ? new Date(r[5]).getTime() : 0,
        submit: r[6] ? new Date(r[6]).getTime() : 0, answers: pj_(r[7], {}), auto: pj_(r[8], {}), manual: pj_(r[9], {}), total: r[10], late: r[11] === 'Có', warns: Number(r[12]) || 0 })),
      events: ev.slice(-600).map(r => ({ t: new Date(r[0]).getTime(), id: r[1], u: r[2], name: r[3], type: r[4], detail: r[5] })) };
  }
  if (act === 'testDef') {
    const T = b.test || {}; if (!T.id || !T.sections) return { ok: false, error: 'missing' };
    const js = JSON.stringify(T); if (js.length > MAX_DATA) return { ok: false, error: 'too_large' };
    const tr = testRow_(T.id);
    if (tr.r) tr.sh.getRange(tr.r, 2).setValue(str_(T.title, 200)), tr.sh.getRange(tr.r, 6, 1, 2).setValues([[now, js]]);
    else tr.sh.appendRow([T.id, str_(T.title, 200), false, false, '', now, js]);
    return { ok: true };
  }
  if (act === 'testMeta') {
    const tr = testRow_(b.id); if (!tr.r) return { ok: false, error: 'no_test' };
    if (b.open != null) tr.sh.getRange(tr.r, 3).setValue(!!b.open);
    if (b.released != null) tr.sh.getRange(tr.r, 4).setValue(!!b.released);
    if (b.pass != null) tr.sh.getRange(tr.r, 5).setValue(str_(b.pass, 40));
    return { ok: true };
  }
  if (act === 'testClearEvents') {
    const removed = filterRows_(sheet_(TEV, E_HEAD), E_HEAD.length, r => r[1] !== b.id);
    const sh = sheet_(ATT, A_HEAD), rows = rowsOf_(sh, A_HEAD.length);
    rows.forEach((r, i) => { if (r[1] === b.id && r[12]) sh.getRange(i + 2, 13).setValue(0); });
    return { ok: true, removed: removed };
  }
  if (act === 'testGrade' || act === 'testReset') {
    const at = attRow_(b.id, b.user); if (!at.r) return { ok: false, error: 'no_attempt' };
    if (act === 'testReset') { at.sh.deleteRow(at.r);
      filterRows_(sheet_(TEV, E_HEAD), E_HEAD.length, r => !(r[1] === b.id && String(r[2]).toLowerCase() === String(b.user).toLowerCase())); return { ok: true }; }
    const manual = b.manual || {}, auto = pj_(at.row[8], {});
    at.sh.getRange(at.r, 10, 1, 2).setValues([[JSON.stringify(manual), totalOf_(auto, manual)]]);
    return { ok: true, total: totalOf_(auto, manual) };
  }
  return null;
}
