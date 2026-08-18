# AI Agent - Hỗ Trợ Đăng Bài Facebook Tự Động Từ Notion

Hệ thống AI Agent cá nhân hóa giúp bạn chuyển đổi những ý tưởng/ghi chú thô từ Database của Notion thành những bài viết Facebook chất lượng cao, súc tích (150-300 từ), giật Hook cuốn hút, kèm ảnh minh họa AI và xuất file HTML giao diện Facebook Preview.

## 📖 Tài Liệu Hướng Dẫn

- 📱 **Hướng dẫn tạo Telegram Bot (1 phút)**: Xem [telegram_bot/HUONG_DAN_TELEGRAM_BOT.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/telegram_bot/HUONG_DAN_TELEGRAM_BOT.md)
- 🚀 **Khởi chạy Telegram Bot**: Nhấp đúp vào [run_telegram_bot.bat](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/run_telegram_bot.bat)
- 📘 **Kiến trúc 4 Agent & 9 Skills**: Xem [AGENTS.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/AGENTS.md)
- 🌐 **Hướng dẫn kết nối Facebook API**: Xem [fb_integration/HUONG_DAN_FACEBOOK_API.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/fb_integration/HUONG_DAN_FACEBOOK_API.md)
- 📓 **Hướng dẫn kết nối Notion**: Xem [notion_integration/HUONG_DAN_NOTION_MCP.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/notion_integration/HUONG_DAN_NOTION_MCP.md)
- 📚 **Knowledge Base GMFinance**: Xem thư mục [knowledge_base/](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/knowledge_base/)

## ⚡ 3 Tính Năng Chính Điều Khiển Qua Telegram Bot

1. 🔍 **Đọc Notion & Gợi ý bài viết**: Gõ `/notion` $\rightarrow$ Nhận 4 chủ đề kèm nút chọn nhanh `[1]`...`[4]`
2. 📝 **Tự draft bài & Lên lịch Fanpage**: Gõ `/fb <chủ đề>` $\rightarrow$ Sinh bài viết + Bộ 3 Slide Card (1080x1080px) gửi vào chat $\rightarrow$ Nút bấm Lưu Nháp / Lên lịch (08:30, 11:30, 20:00).
3. 🎬 **Phỏng vấn lên Kịch bản Video**: Gõ `/video <chủ đề>` $\rightarrow$ Bot hỏi 3 câu phỏng vấn tương tác $\rightarrow$ Ráp thành kịch bản TikTok/Reels hoàn chỉnh.
