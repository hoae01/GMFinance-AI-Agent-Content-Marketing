# ☁️ Hướng Dẫn Đưa Bot Lên Cloud Chạy 24/7 (Đóng Máy Vẫn Hoạt Động)

Tài liệu này hướng dẫn bạn 2 giải pháp để **đóng máy tính hoặc tắt nguồn mà Bot vẫn hoạt động 100% trên điện thoại**, hoàn toàn **MIỄN PHÍ 0 ĐỒNG**.

---

## 🌟 GIẢI PHÁP 1: Deploy Lên Render.com (Miễn Phí Vĩnh Viễn - Khuyên Dùng Nhất)

Khi đưa lên Render.com, code của bạn sẽ chạy trên máy chủ đám mây của Render 24/7/365. Bạn có thể tắt nguồn máy tính, đi ngủ hoặc đi công tác mà Bot vẫn trả lời tin nhắn và đăng bài bình thường trên điện thoại.

### 🔹 Bước 1: Đăng nhập Render bằng GitHub
1. Mở trình duyệt và truy cập: **[https://render.com/](https://render.com/)**
2. Nhấn **"GET STARTED FOR FREE"** $\rightarrow$ Chọn **"Sign in with GitHub"** (đăng nhập bằng tài khoản GitHub của bạn).

---

### 🔹 Bước 2: Tạo một Background Worker mới
1. Trên giao diện Dashboard của Render, nhấn nút xanh **"New +"** ở góc trên bên phải.
2. Chọn mục **"Background Worker"** (hoặc Web Service).
3. Tìm và chọn repository của bạn: **`hoae01/GMFinance-AI-Agent-Content-Marketing`** $\rightarrow$ Nhấn **"Connect"**.

---

### 🔹 Bước 3: Điền Cấu Hình Cơ Bản
Điền các thông tin sau:
- **Name**: `gmfinance-telegram-bot`
- **Region**: Chọn **`Singapore (Southeast Asia)`** *(để phản hồi về Việt Nam nhanh nhất)*
- **Branch**: `main`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python telegram_bot/bot.py`
- **Instance Type**: Chọn **`Free`** ($0/month)

---

### 🔹 Bước 4: Thêm Biến Môi Trường (Environment Variables)
Cuộn xuống phần **"Environment Variables"** $\rightarrow$ Nhấn **"Add Environment Variable"** và điền lần lượt các thông tin từ file `.env`:

| Key (Tên biến) | Value (Giá trị) |
| :--- | :--- |
| `TELEGRAM_BOT_TOKEN` | *(Copy từ dòng `TELEGRAM_BOT_TOKEN` trong file `.env` của bạn)* |
| `TELEGRAM_ALLOWED_USER_ID` | `6612237519` *(User ID của bạn)* |
| `GEMINI_API_KEY` | *(Copy từ dòng `GEMINI_API_KEY` trong file `.env` của bạn)* |
| `NOTION_TOKEN` | *(Copy từ dòng `NOTION_TOKEN` trong file `.env` của bạn)* |
| `NOTION_DATABASE_ID` | `2d946051-a014-8031-b54f-c5d2d82fa52b` |
| `FB_PAGE_1_ID` | `553023051221662` |
| `FB_PAGE_1_TOKEN` | *(Copy từ dòng `FB_PAGE_1_TOKEN` trong file `.env` của bạn)* |
| `FB_PAGE_2_ID` | `640197582852560` |
| `FB_PAGE_2_TOKEN` | *(Copy từ dòng `FB_PAGE_2_TOKEN` trong file `.env` của bạn)* |

---

### 🔹 Bước 5: Kích Hoạt & Tận Hưởng
1. Nhấn nút **"Create Background Worker"** ở cuối trang.
2. Render sẽ tự động kéo code từ GitHub về, cài đặt và chạy Bot trong ~1 phút.
3. Khi màn hình hiện chữ **`Live` (Màu xanh lá)**, chúc mừng bạn! Bot đã hoạt động vĩnh viễn trên đám mây!
4. Giờ đây bạn có thể **tắt máy tính hoàn toàn**, mở điện thoại lên chat với **`@Marketing_FinanceGMBot`** để tạo bài viết và lên lịch Fanpage bất kỳ lúc nào!

---

## 💻 GIẢI PHÁP 2: Cài Đặt Windows Để Gập Màn Hình Vẫn Chạy Ngầm (Không Cần Cloud)

Nếu bạn chưa muốn tạo tài khoản Render ngay mà muốn gập laptop lại nhưng máy vẫn chạy ngầm bot ở nhà:

1. Nhấn phím `Windows` $\rightarrow$ Gõ **`Control Panel`** và mở lên.
2. Chọn **`Power Options`** (hoặc gõ tìm `Power Options` trong ô tìm kiếm).
3. Ở cột bên trái, nhấn vào **`Choose what closing the lid does`** (Chọn tác vụ khi gập nắp máy).
4. Tại dòng **"When I close the lid"**:
   - Ở cột **`Plugged in` (Khi cắm sạc)**: Chuyển từ *Sleep* sang **`Do nothing`** (Không làm gì cả).
5. Nhấn nút **"Save changes"** ở dưới.
6. Giờ đây, chỉ cần bạn cắm sạc laptop và chạy file `run_telegram_bot.bat`, bạn có thể **gập nắp laptop lại cất ở góc bàn**, máy vẫn chạy êm ái ngầm và Bot vẫn nhận lệnh từ điện thoại 24/24!
