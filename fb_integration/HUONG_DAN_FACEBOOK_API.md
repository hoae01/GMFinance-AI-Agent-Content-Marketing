# 📖 Hướng Dẫn Cấu Hình Facebook Graph API Cho Fanpage GMFinance

Tài liệu này hướng dẫn bạn từng bước lấy **Page ID** và **Page Access Token (Token Quản trị Fanpage)** để kết nối tính năng **Tự động lưu bản nháp (Draft)** & **Lên lịch đăng bài (Scheduled Post)** cho 2 Fanpage:
1. **Fanpage 1**: GMFinance - Đào Tạo & Coaching ACCA (`https://www.facebook.com/financegm/`)
2. **Fanpage 2**: Giải Pháp Tài Chính & Kế Toán Việt Nam (`https://www.facebook.com/giaiphaptaichinhvaketoanVietnam/`)

---

## 🛠️ Bước 1: Tạo Meta App (Ứng dụng Developer trên Meta)

1. Truy cập [Meta for Developers](https://developers.facebook.com/) và đăng nhập bằng tài khoản Facebook quản trị 2 Fanpage.
2. Nhấp chọn **My Apps (Ứng dụng của tôi)** $\rightarrow$ Bấm nút **Create App (Tạo ứng dụng)**.
3. Chọn loại ứng dụng: **Other (Khác)** hoặc **Business (Doanh nghiệp)** $\rightarrow$ Bấm **Next**.
4. Điền tên ứng dụng (Ví dụ: `GMFinance Content Manager`) $\rightarrow$ Bấm **Create app**.

---

## 🔑 Bước 2: Lấy Page ID & Page Access Token qua Graph API Explorer

1. Truy cập công cụ [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Tại ô **Meta App**, chọn App bạn vừa tạo ở Bước 1 (`GMFinance Content Manager`).
3. Tại mục **User or Page**, chọn **Get Page Access Token**.
4. Hệ thống sẽ hiển thị cửa sổ ủy quyền Facebook:
   - Tích chọn cả 2 Fanpage: **GMFinance** và **Giải Pháp Tài Chính & Kế Toán Việt Nam**.
   - Cấp các quyền (Permissions) sau:
     - `pages_manage_posts` (Đăng bài & Lưu bản nháp)
     - `pages_read_engagement` (Đọc thông tin Fanpage)
     - `pages_show_list` (Hiển thị danh sách trang)
5. Nhấn **Save / Done** để hoàn tất ủy quyền.

---

## 📌 Bước 3: Đổi Sang Token Vĩnh Viễn (Never-Expiring Page Token)

Mặc định Token thu được ở Graph API Explorer chỉ có hiệu lực 1 giờ. Để lấy Token dài hạn không hết hạn:

1. Copy chuỗi Token thu được.
2. Truy cập [Access Token Tool](https://developers.facebook.com/tools/debug/accesstoken/).
3. Dán Token vào và bấm **Debug** $\rightarrow$ Bấm nút **Extend Access Token** ở cuối trang.
4. Copy chuỗi **Long-Lived Page Access Token** thu được.

---

## ⚙️ Bước 4: Lưu Thông Tin Vào File `.env` Dự Án

Mở file `.env` tại thư mục gốc của dự án `GMFinance-AI-Agent-Content-Marketing` và điền thông tin:

```env
# Fanpage 1: GMFinance - Đào Tạo & Coaching ACCA
FB_PAGE_1_ID=your_page_1_id_here
FB_PAGE_1_TOKEN=your_page_1_access_token_here

# Fanpage 2: Giải Pháp Tài Chính & Kế Toán Việt Nam
FB_PAGE_2_ID=your_page_2_id_here
FB_PAGE_2_TOKEN=your_page_2_access_token_here
```

---

## 🧪 Bước 5: Kiểm Tra Kết Nối

Mở Terminal tại thư mục dự án và chạy lệnh sau để kiểm tra:

```bash
python fb_integration/fb_publisher.py --test
```

Nếu cấu hình đúng, màn hình sẽ báo trạng thái đã nhận diện 2 Fanpage cùng độ dài Token!

---

## 🚀 Cách Sử Dụng Đăng Bài / Lên Lịch

### 1. Tạo Bản Nháp (Draft) cho cả 2 Fanpage (Mặc định):
```bash
python fb_integration/fb_publisher.py --message-file Output/baiviet_moi.txt --images Output/assets/slide_01.png Output/assets/slide_02.png Output/assets/slide_03.png --page all --draft
```

### 2. Lên Lịch Đăng Bài (Scheduled Post) lúc 20:00 tối:
```bash
python fb_integration/fb_publisher.py --message-file Output/baiviet_moi.txt --images Output/assets/slide_01.png Output/assets/slide_02.png Output/assets/slide_03.png --page 1 --schedule "2026-08-14 20:00"
```

### 3. Đăng cho riêng Fanpage 1 hoặc Fanpage 2:
- Cả 2 trang: `--page all`
- Fanpage GMFinance: `--page 1`
- Fanpage Giải Pháp Tài Chính: `--page 2`
