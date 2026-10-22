/**
 * 薇薇中文 – Máy chủ lưu tiến độ học viên (Google Apps Script)
 *
 * CÁCH CÀI (làm 1 lần):
 * 1. Tạo một Google Sheet mới, đặt tên ví dụ "Weiwei - Tiến độ học viên".
 * 2. Menu Tiện ích mở rộng (Extensions) → Apps Script. Xoá hết mã mẫu, dán toàn bộ file này vào, bấm Lưu.
 * 3. Bên trái chọn Cài đặt dự án (Project Settings) → Thuộc tính tập lệnh (Script properties)
 *    → Thêm thuộc tính: Tên = TEACHER_KEY, Giá trị = mật khẩu giáo viên của bạn. Lưu.
 * 4. Bấm Triển khai (Deploy) → Tùy chọn triển khai mới (New deployment) → loại "Ứng dụng web" (Web app):
 *      - Thực thi dưới dạng (Execute as): Tôi (Me)
 *      - Người có quyền truy cập (Who has access): Bất kỳ ai (Anyone)
 *    Bấm Triển khai, cấp quyền cho tài khoản Google của bạn, rồi sao chép "URL ứng dụng web" (kết thúc bằng /exec).
 * 5. Gửi URL đó cho Claude, hoặc tự dán vào dòng  const TEACHER_API = "";  trong file index.html.
 *
 * Học viên chỉ GHI được dữ liệu. Muốn ĐỌC dữ liệu phải có đúng mật khẩu TEACHER_KEY.
 * Bạn cũng có thể mở trực tiếp trang tính "Events" để xem toàn bộ dữ liệu thô.
 */
const SHEET_NAME = 'Events';
const HEADERS = ['Thời gian', 'Mã sự kiện', 'Mã học viên', 'Họ tên', 'Lớp', 'Trình độ', 'Loại', 'Bài', 'Chi tiết (JSON)'];

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) {
    sh = ss.insertSheet(SHEET_NAME);
    sh.appendRow(HEADERS);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  }
  return sh;
}
function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
function str_(v, n) { return String(v == null ? '' : v).slice(0, n); }

/* Học viên gửi tiến độ lên (không cần mật khẩu, chỉ được ghi thêm) */
function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const body = JSON.parse(e.postData.contents || '{}');
    const events = (Array.isArray(body.events) ? body.events : []).slice(0, 100);
    const sh = sheet_();
    const rows = events.map(x => [
      new Date(x.t || Date.now()), str_(x.eid, 40), str_(x.sid, 40), str_(x.name, 60), str_(x.cls, 10),
      str_(x.level, 10), str_(x.type, 20), str_(x.lesson, 20), str_(JSON.stringify(x.data || {}), 4000)
    ]);
    if (rows.length) sh.getRange(sh.getLastRow() + 1, 1, rows.length, HEADERS.length).setValues(rows);
    return json_({ ok: true, saved: rows.length });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

/* Giáo viên đọc dữ liệu (bắt buộc đúng mật khẩu) */
function doGet(e) {
  const key = PropertiesService.getScriptProperties().getProperty('TEACHER_KEY');
  if (!key) return json_({ ok: false, error: 'no_key' });
  if ((e.parameter.key || '') !== key) return json_({ ok: false, error: 'unauthorized' });
  const sh = sheet_();
  const n = sh.getLastRow() - 1;
  if (n < 1) return json_({ ok: true, events: [] });
  const vals = sh.getRange(2, 1, n, HEADERS.length).getValues();
  const events = vals.map(r => {
    let data = {};
    try { data = JSON.parse(r[8] || '{}'); } catch (err) {}
    return {
      t: r[0] instanceof Date ? r[0].toISOString() : String(r[0]),
      eid: r[1], sid: r[2], name: r[3], cls: r[4], level: r[5], type: r[6], lesson: r[7], data: data
    };
  });
  return json_({ ok: true, events: events });
}
