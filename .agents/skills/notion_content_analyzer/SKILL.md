---
name: notion_content_analyzer
description: Chuyên gia phân tích, lọc và tổng hợp dữ liệu ghi chú/ý tưởng thô từ Notion Database thành 5 góc nhìn/nội dung độc đáo cho ngày mới.
---

# Skill: Phân Tích Dữ Liệu Notion Database (Notion Content Analyzer)

## 📌 Vai Trò & Mục Tiêu
Skill này đại diện cho năng lực phân tích dữ liệu đầu vào từ Notion của Agent:
- **Đọc & Trích Xuất Dữ Liệu**: Gọi script `fetch_notion.py` hoặc các công cụ Notion MCP Server để quét các trang ghi chú, ý tưởng thô trong Notion Database.
- **Phân Loại & Lọc Ý Tưởng**: Loại bỏ các ghi chú đã đăng, lọc ra các ý tưởng "đáng tiền" có tiềm năng tạo giá trị nhất cho độc giả.
- **Tạo 5 Gợi Ý Đa Dạng Góc Nhìn**: Tổng hợp dữ liệu thô thành 5 phương án bài viết với 5 góc nhìn khác nhau (Nỗi đau, Tư duy ngược, Câu chuyện cá nhân, Checklist kiến thức, Trải nghiệm bài học).

---

## 📋 Quy Trình Thực Hiện 5 Bước Gợi Ý Nội Dung

### Bước 1: Thu Thập Dữ Liệu
Chạy `python notion_integration/fetch_notion.py` để lấy danh sách ý tưởng chưa sử dụng từ Notion.

### Bước 2: Phân Tích Ý Tưởng Thô
Duyệt qua từng trang ghi chú để xác định:
- Giá trị cốt lõi (Core message).
- Nỗi đau độc giả tương ứng.
- Loại tư liệu hiện có (có con số không, có câu chuyện không, có checklist không).

### Bước 3: Xây Dựng 5 Phương Án Đề Xuất
Hiển thị cho người dùng danh sách 5 phương án theo định dạng chuẩn:

```text
1. 📌 [Tiêu đề gợi ý 1] - Thể loại: [Thể loại]
   - Góc nhìn (Angle): [Góc nhìn xoáy vào nỗi đau/tư duy ngược...]
   - Công thức: PAS
   - Ý tưởng ảnh: [Mô tả ảnh 3D/Minimalist...]

2. 📌 [Tiêu đề gợi ý 2] - Thể loại: [Thể loại]
   - Góc nhìn (Angle): [Góc nhìn...]
   - Công thức: Micro-learning / AIDA
   - Ý tưởng ảnh: [...]
...
```

### Bước 4: Tiếp Nhận Phản Hồi
Chờ người dùng chọn số từ 1 đến 5 hoặc yêu cầu kết hợp/điều chỉnh góc nhìn trước khi chuyển sang giai đoạn draft bài viết.
