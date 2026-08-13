# 📋 Nhật Ký Cải Tiến Quy Trình & PDCA Backlog Log

Tài liệu này lưu trữ toàn bộ các cải tiến, bài học kinh nghiệm và phản hồi (Prompt Feedback) từ người dùng theo chu trình **PDCA (Plan - Do - Check - Act)** nhằm liên tục nâng cao chất lượng bài viết và hình ảnh.

---

## Danh Sách Bài Học & Cải Tiến Quy Trình (PDCA Backlog)

### 🔄 [2026-08-11] Khởi tạo Hệ thống & Thiết lập Nền tảng #001
- **Input của người dùng**: Xây dựng AI Agent đọc Notion Database, gợi ý 5 nội dung, viết bài ngắn gọn cuốn hút, sinh ảnh AI và xuất file HTML Facebook Preview.
- **Plan (Phân tích & Kế hoạch)**: Xây dựng 4 tài liệu Knowledge Base Copywriting + Bộ tích hợp Notion + Bộ sinh HTML preview + 5 Skills cho Agent 1 & Agent 2.
- **Do (Đã thực hiện)**: Khởi tạo hoàn chỉnh cấu trúc dự án, tạo file mẫu test và 5 Skills chuyên biệt.
- **Check (Kết quả)**: Đã test chạy thành công script Notion, sinh ảnh AI và tạo file HTML Facebook Preview.
- **Act (Bài học đưa vào quy tắc)**: Giữ vững quy chuẩn bài viết 150-300 từ, Hook 3 dòng đầu và nút Copy 1-click trên file HTML.

---

### 🔄 [2026-08-11] Điều Chỉnh Định Hướng Nội Dung (Generic Productivity) #002
- **Input của người dùng**: *"Tôi chưa muốn nhắm vào ACCA vội, tôi đang muốn Generic hơn, chỉ nói chung về phương pháp làm việc năng suất, đây cũng là định hướng phát triển kênh hiện tại của tôi."*
- **Plan (Phân tích & Kế hoạch)**: Chuyển dịch định hướng nội dung của Agent 1 từ xoáy sâu vào sản phẩm ACCA sang tập trung vào các phương pháp tối ưu hiệu suất, làm việc thông minh (Productivity, Work Smarter, High Performance Habits, Mental Models).
- **Do (Đã thực hiện)**: Cập nhật quy tắc gợi ý bài viết, ưu tiên các chủ đề rộng có tính lan tỏa (viral) cao về năng suất công việc.
- **Check (Kết quả)**: Đã tái cấu trúc 5 góc nhìn bài viết theo định hướng Generic Productivity.
- **Act (Bài học đưa vào quy tắc)**: Giữ nội dung bài viết mang tính rộng rãi, trao giá trị thực chiến về làm việc hiệu quả; lồng ghép thương hiệu GMFinance tinh tế.

---

### 🔄 [2026-08-11] Tối Ưu Hook Đối Lập & Minh Chứng Khoa Học #003
- **Input của người dùng**: *"Hook chưa đủ hấp dẫn, tôi muốn Hook kiểu đối lập, kiểu tại sao khoa học chứng minh làm càng ít thì lại càng thành công."*
- **Plan (Phân tích & Kế hoạch)**: Nâng cấp câu Hook lên cấp độ Contrarian + Scientific Proof. Đặt 2 vế đối lập gây sốc giữa tư duy cũ ("làm nhiều = thành công") và phát hiện của Khoa học Thần kinh ("làm ít việc hơn = thành công lớn hơn").
- **Do (Đã thực hiện)**: Áp dụng câu Hook đối lập khoa học vào bản draft bài viết chính thức.
- **Check (Kết quả)**: Hook 3 dòng ngắt dòng chuẩn mobile, tăng mạnh tỷ lệ kích thích bấm "Xem thêm".
- **Act (Bài học đưa vào quy tắc)**: Cập nhật mẫu Hook đối lập khoa học này vào `knowledge_base/viral_hooks_library.md` làm chuẩn mẫu ưu tiên.

---

### 🔄 [2026-08-11] Chuẩn Hóa Bộ 3 Ảnh Slide Card Theo Thiết Kế Mẫu #004
- **Input của người dùng**: *"Ảnh minh họa chưa đủ tốt... hãy tạo ra 3 ảnh đi kèm nội dung... Đây hãy dùng ví dụ này để làm ảnh minh họa đi kèm nội dung, chèn nội dung liên quan đến bài viết cho phù hợp."* -> *"Tốt lắm, bạn đã làm đúng ý tôi."*
- **Plan (Phân tích & Kế hoạch)**: Phân tích và lập trình bộ sinh ảnh Slide Card (`scripts/generate_slide_cards.py`) chuẩn 1080x1080px theo đúng mẫu layout người dùng cung cấp (Header line, `@GMFinance`, Top-right big index `01/02/03`, center icon badge, title & body text).
- **Do (Đã thực hiện)**: Đã sinh 3 file ảnh `slide_01.png`, `slide_02.png`, `slide_03.png` và nhúng thành công vào bộ sinh HTML Facebook Preview.
- **Check (Kết quả)**: Người dùng duyệt và khen ngợi đúng 100% mong muốn!
- **Act (Bài học đưa vào quy tắc)**: Đưa bộ sinh 3 Slide Card (`generate_slide_cards.py`) làm chuẩn mực mặc định cho các bài đăng dạng Slide Card sắp tới.

---

### 🔄 [2026-08-13] Tích Hợp Đăng Bản Nháp (Draft) & Lên Lịch (Scheduled Post) 2 Fanpage #005
- **Input của người dùng**: *"Đây là 2 fanpage của tôi (https://www.facebook.com/financegm/ và https://www.facebook.com/giaiphaptaichinhvaketoanVietnam/). Tôi muốn bạn bổ sung tính năng sau khi bạn đã tạo nội dung bài xong, draft nội dung lên Fanpage và lên lịch đăng luôn có được không?"*
- **Plan (Phân tích & Kế hoạch)**: Xây dựng module `fb_integration/fb_publisher.py` kết nối Facebook Graph API v19.0+ chính thức. Tự động upload 3 ảnh Slide Card ở chế độ ẩn để gắn ID, hỗ trợ 2 chế độ (Tạo bản nháp Draft và Lên lịch Scheduled Post theo khung giờ vàng) cho 2 Fanpage thương hiệu.
- **Do (Đã thực hiện)**: Tạo module `fb_integration/fb_publisher.py`, file hướng dẫn lấy Token vĩnh viễn `HUONG_DAN_FACEBOOK_API.md`, cập nhật file cấu hình `.env` & `.env.example`.
- **Check (Kết quả)**: Chạy test lệnh CLI `python fb_integration/fb_publisher.py --test` hoạt động hoàn hảo.
- **Act (Bài học đưa vào quy tắc)**: Mọi bài viết sau khi xuất bản nội dung & 3 Slide Cards sẽ sẵn sàng lệnh tự động đẩy nháp (Draft) hoặc hẹn giờ (Schedule) lên 2 Fanpage qua Graph API.

---

### 🔄 [2026-08-13] Sửa Triệt Để Lỗi Tràn Chữ & Đa Dạng Hóa Theme Thiết Kế Slide Cards #006
- **Input của người dùng**: *"Hay đó, nhưng slide bạn làm bị tràn chữ ra bên ngoài rồi, với cả bạn có thể đối thiết kế slide để tránh bị nhàm chán và giống như bài đăng trước không?"*
- **Plan (Phân tích & Kế hoạch)**:
  1. Viết thuật toán Auto-Wrap & Auto-Scale Font Size trong `scripts/generate_slide_cards.py` để tính toán chính xác `bbox` tiêu đề và nội dung, co giãn kích thước chữ tự động, đảm bảo 100% không bao giờ tràn lề.
  2. Bổ sung 3 Theme thiết kế cao cấp: `modern_dark_gold` (Chess King Luxury), `glassmorphism_blue` (Executive Finance) và `minimal_clean` (Minimalist Classic) để tạo sự tươi mới cho mỗi bài viết.
- **Do (Đã thực hiện)**: Cập nhật `scripts/generate_slide_cards.py`, sinh lại bộ 3 Slide Cards với Theme `modern_dark_gold` cực đẹp, tự động điều chỉnh font size.
- **Check (Kết quả)**: Kiểm tra ảnh tạo ra hoàn toàn sạch lỗi tràn chữ, khoảng cách lề và dòng phân bổ hài hòa, sang trọng.
- **Act (Bài học đưa vào quy tắc)**: Áp dụng thuật toán Auto-Wrap & luân chuyển các Theme thiết kế cho mỗi bài đăng mới để tạo sự mới mẻ liên tục cho kênh.


