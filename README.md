# 薇薇中文 · Weiwei HSK
Trang luyện HSK cho học viên: flashcard, luyện dịch, phát âm có chấm thanh điệu, bài tập HSK, trang trại xu và bảng theo dõi cho giáo viên.

- `index.html` – trang web (Netlify đăng file này). **Không sửa tay**, file được tạo từ `_src/`.
- `_src/src.html` – mã nguồn chính (nội dung bài học, giao diện).
- `_src/ex*/` – hình ảnh của phần Bài tập HSK.
- `_src/teacher_api.txt` – link Google Apps Script (để trống nếu chưa cài).
- `audio/` – file nghe .mp3 của Bài tập HSK.
- `giao-vien/apps-script-giao-vien.gs` – mã dán vào Google Sheet để theo dõi học viên.

Cập nhật: sửa `_src/` → chạy `python3 _src/build.py` → commit & push. Netlify tự đăng bản mới.
