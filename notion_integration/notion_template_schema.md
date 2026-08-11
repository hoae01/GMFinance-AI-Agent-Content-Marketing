# Mẫu Cấu Trúc Database Notion Khuyến Nghị (Notion Database Schema)

Để Agent lấy dữ liệu và phân loại ý tưởng chính xác nhất, bạn có thể tạo một Database trên Notion với các cột (Properties) khuyến nghị dưới đây:

---

## Các Cột (Properties) Trong Notion Database:

| Tên Cột (Property) | Kiểu Dữ Liệu (Type) | Mô Tả / Giá Trị Mẫu |
| :--- | :--- | :--- |
| **Tiêu đề (Name / Title)** | `Title` | Tên ý tưởng hoặc chủ đề chính (Vd: *"Cách dùng AI viết email nhanh"*) |
| **Nội dung / Ghi chú (Notes)** | `Text / Rich Text` | Ghi chú thô, gạch đầu dòng ý chính, liên kết tham khảo hoặc đoạn chat nháp |
| **Trạng thái (Status)** | `Select / Status` | `Ý tưởng mới`, `Sẵn sàng viết`, `Đã đăng`, `Bỏ qua` |
| **Chủ đề (Category)** | `Multi-select` | `AI / Công nghệ`, `Kỹ năng sống`, `Marketing`, `Bài học kinh doanh` |
| **Ngày tạo (Created Time)** | `Created time` | Tự động sinh ra khi tạo trang |

---

## Ví Dụ 1 Trang Dữ Liệu Mẫu:
- **Title**: *Thói quen 15 phút lập kế hoạch mỗi tối*
- **Status**: *Sẵn sàng viết*
- **Category**: *Năng suất*
- **Notes**:
  - Dành 15 phút trước khi ngủ viết ra 3 việc lớn nhất ngày mai.
  - Sáng dậy không cần suy nghĩ làm gì trước -> Đỡ tốn năng lượng ra quyết định.
  - Kết quả: Giảm stress 50%, làm việc tập trung ngay từ 8h sáng.
