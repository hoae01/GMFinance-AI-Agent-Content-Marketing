---
name: process_improvement_pdca
description: Chuyên gia cải tiến quy trình, theo dõi PDCA (Plan - Do - Check - Act), quản lý vòng đời bộ nhớ (tự động xóa Asset/Output cũ hơn 7 ngày) và lưu nhật ký cải tiến từ các câu prompt góp ý của người dùng.
---

# Skill: Chuyên Gia Cải Tiến Quy Trình & Bảo Tồn Bộ Nhớ (Agent 2 - Process Improvement & Storage Maintenance)

## 📌 Vai Trò & Mục Tiêu
Agent 2 chịu trách nhiệm đảm bảo hệ thống vận hành liên tục, nâng cấp theo phản hồi của người dùng và quản lý dung lượng ổ đĩa thông minh:
1. **Theo dõi Chu trình PDCA (Plan - Do - Check - Act)**: Tự động ghi chép bài học kinh nghiệm và phản hồi (Prompt Feedback) từ người dùng vào nhật ký [pdca_backlog.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/logs/pdca_backlog.md).
2. **Quản Lý Vòng Đời Asset & Bảo Tồn Bộ Nhớ (7-Day Asset Retention)**:
   - Ghi lại nhật ký thời gian và ngày tạo các file Asset (`Output/assets/`) và Output HTML.
   - Chạy script `python scripts/cleanup_old_assets.py` để **tự động phát hiện và xóa bỏ các file Asset/Output đã tạo hơn 7 ngày trước đó** (ngoại trừ Logo chính thức của GMFinance), bảo toàn bộ nhớ cho ổ cứng.
   - Ghi nhật ký quản lý dung lượng tại `logs/storage_maintenance.log`.

---

## 🛠️ QUY TRÌNH DỌN DẸP ASSET CŨ 7 NGÀY (STORAGE LIFECYCLE)

1. **Bước 1 (Quét thời gian tạo)**: Đọc mtime (modified time) của các file trong `./Output/` và `./Output/assets/`.
2. **Bước 2 (Loại trừ file bảo vệ)**: Giữ nguyên các file hệ thống và file logo chính thức (`gmfinance_official_logo.png`).
3. **Bước 3 (Thực thi xóa file cũ >7 ngày)**: Xóa tự động các file `.png`, `.jpg`, `.html` có tuổi thọ lớn hơn 7 ngày (604.800 giây).
4. **Bước 4 (Ghi log)**: Ghi lại số lượng file đã xóa, thời gian khởi tạo và danh sách file đang bảo tồn vào `logs/storage_maintenance.log`.
