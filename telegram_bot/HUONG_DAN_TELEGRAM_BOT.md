# 📱 Hướng Dẫn Thiết Lập Telegram Bot AI Agent GMFinance (Miễn Phí 100%)

Tài liệu này hướng dẫn bạn từng bước thiết lập Telegram Bot chỉ trong vòng **3 phút**, hoàn toàn **MIỄN PHÍ 100%** không cần mua token hay nhập thẻ visa.

---

## 🚀 BƯỚC 1: Tạo Bot Telegram & Lấy Token (1 Phút)

1. Mở ứng dụng Telegram trên điện thoại hoặc máy tính.
2. Tìm kiếm **`@BotFather`** (chọn tài khoản có **tích xanh chính chủ**).
3. Nhấn **Start** (hoặc gửi lệnh `/start`).
4. Gửi lệnh:
   ```
   /newbot
   ```
5. Nhập tên hiển thị cho Bot (Ví dụ: `GMFinance Assistant`).
6. Nhập username cho Bot (phải kết thúc bằng chữ `bot`, ví dụ: `gmfinance_content_bot`).
7. `@BotFather` sẽ gửi lại tin nhắn chúc mừng kèm một chuỗi mã **HTTP API Token** có dạng:
   ```
   7890123456:AAFlk..._ví_dụ_chuỗi_token_ở_đây
   ```
8. **Copy chuỗi token này** để sử dụng ở Bước 4.

---

## 🆔 BƯỚC 2: Lấy Telegram User ID Của Bạn (30 Giây)
*Mục đích: Chỉ cho phép tài khoản Telegram của riêng bạn điều khiển Bot, ngăn chặn người ngoài can thiệp vào Fanpage.*

1. Trên Telegram, tìm kiếm **`@userinfobot`**.
2. Nhấn **Start**.
3. Bot sẽ gửi lại thông tin của bạn. Hãy copy con số ở dòng **`Id`** (Ví dụ: `1234567890`).

---

## 🧠 BƯỚC 3: Lấy Google Gemini API Key Miễn Phí (1 Phút)

1. Mở trình duyệt và truy cập: **[https://aistudio.google.com/](https://aistudio.google.com/)**
2. Đăng nhập bằng tài khoản Google cá nhân của bạn.
3. Nhấn vào nút xanh **"Get API key"** ở góc trên bên trái.
4. Nhấn **"Create API key"** $\rightarrow$ Chọn một dự án mặc định (hoặc tạo mới) $\rightarrow$ Nhấn **"Create API key in new project"**.
5. Copy chuỗi API Key vừa sinh ra (có dạng bắt đầu bằng `AIzaSy...`).

*(Hạn mức miễn phí: 15 yêu cầu/phút và 1.500 yêu cầu/ngày — hoàn toàn dư dả cho mọi nhu cầu).*

---

## ⚙️ BƯỚC 4: Điền Cấu Hình Vào File `.env`

Mở file **`.env`** trong thư mục dự án và cập nhật các dòng sau:

```env
# 1. Telegram Bot Token & Admin User ID
TELEGRAM_BOT_TOKEN=chuỗi_token_lấy_từ_BotFather
TELEGRAM_ALLOWED_USER_ID=chuỗi_id_lấy_từ_userinfobot

# 2. Google Gemini API Key (Miễn phí)
GEMINI_API_KEY=chuỗi_api_key_lấy_từ_Google_AI_Studio

# 3. Fanpage Facebook Token (Đã cấu hình trước đó)
FB_PAGE_1_ID=your_page_1_id
FB_PAGE_1_TOKEN=your_page_1_token
FB_PAGE_2_ID=your_page_2_id
FB_PAGE_2_TOKEN=your_page_2_token

# 4. Notion Vault (Đã cấu hình trước đó)
NOTION_TOKEN=ntn_your_secret_token
NOTION_DATABASE_ID=2d946051-a014-8031-b54f-c5d2d82fa52b
```

---

## 🏃 BƯỚC 5: Khởi Chạy Bot

Bạn có thể chạy bot theo một trong 2 cách:

- **Cách 1 (Nhanh nhất trên Windows)**: Nhấp đúp chuột vào file **`run_telegram_bot.bat`** ở thư mục gốc dự án.
- **Cách 2 (Qua Terminal)**:
  ```powershell
  python telegram_bot/bot.py
  ```

Màn hình hiển thị:
```text
=================================================================
 👑 GMFINANCE AI AGENT - TELEGRAM BOT SERVICE 
 'ELEVATE EXPERTISE, EXPAND CAREER HORIZONS' 
=================================================================
 [✓] AI Engine       : Google Gemini 2.5/Flash (Sẵn sàng)
 [✓] Fanpage 1 (GM)  : Đã kết nối
 [✓] Fanpage 2 (GP)  : Đã kết nối
 [✓] Notion Vault    : Đã kết nối
 [✓] Quyền Admin     : User ID 1234567890
=================================================================

🚀 Bot đang hoạt động với tên: @gmfinance_content_bot
```

---

## 📱 BƯỚC 6: Trải Nghiệm Trên Điện Thoại / Máy Tính

Mở Telegram, vào ô chat với Bot của bạn và thử các lệnh:

1. **`/start`** hoặc **`/help`**: Xem menu tổng quan.
2. **`/notion`**: Quét Knowledge Vault Notion $\rightarrow$ Nhận 4 chủ đề bài viết ngày mới $\rightarrow$ Bấm nút `[📝 Viết bài FB]` hoặc `[🎬 Phỏng vấn Video]`.
3. **`/fb Ma trận Eisenhower cho kế toán`**: Tự động viết bài Facebook chuẩn GMFinance + Tự động sinh **3 Slide Cards (1080x1080px)** gửi thẳng vào chat $\rightarrow$ Bấm nút `[💾 Lưu Nháp]` hoặc `[⏰ Lên Lịch 08:30]` để đẩy lên Fanpage!
4. **`/video Lộ trình học ACCA 2026`**: Đạo diễn AI sẽ hỏi bạn **3 câu hỏi tương tác ngắn** lần lượt $\rightarrow$ Nhận câu trả lời của bạn rồi tự ráp thành **Kịch Bản Video TikTok/Reels** hoàn chỉnh (Hook 3s, Storyboard 4 cảnh, Góc quay, Text overlay)!
