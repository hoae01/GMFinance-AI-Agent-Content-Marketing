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
