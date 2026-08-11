# 🚀 Hướng Dẫn Sử Dụng AI Agent Tạo Bài Viết Facebook Từ Notion

Hệ thống AI Agent tự động giúp bạn chuyển đổi những ý tưởng/ghi chú thô trên Notion Database thành các bài viết Facebook chất lượng cao, súc tích (150-300 từ), giật Hook cuốn hút, tự động sinh ảnh minh họa AI và xuất ra file xem trước Facebook HTML chuyên nghiệp.

---

## 📁 Cấu Trúc Môi Trường Hệ Thống

```text
AI Agent - Hỗ trợ đăng bài FB tự động/
├── knowledge_base/               # Knowledge Base chuẩn Copywriting Facebook
│   ├── copywriting_frameworks.md # 5 công thức viết bài đỉnh cao (PAS, AIDA, HSO, BAB, Micro-learning)
│   ├── viral_hooks_library.md    # 50+ mẫu tiêu đề giật Hook 3 dòng đầu giữ chân đọc giả
│   ├── formatting_and_tone.md    # Quy chuẩn trình bày (khoảng trống, 150-300 từ, CTA, Emoji)
│   └── proven_templates.md       # Các bài viết mẫu đã chứng minh thành công
├── notion_integration/           # Bộ công cụ kết nối Notion
│   ├── HUONG_DAN_NOTION_MCP.md   # Hướng dẫn tạo Token Notion & cấu hình MCP Server
│   ├── notion_template_schema.md # Cấu trúc Database mẫu trên Notion
│   └── fetch_notion.py           # Script lấy dữ liệu Notion API (hoặc Mock Data)
├── scripts/
│   └── html_generator.py         # Script tạo trang HTML Facebook Preview chuyên nghiệp
├── Output/                       # Thư mục chứa bài viết đầu ra dạng HTML
├── AGENTS.md                     # Cấu hình quy trình 5 bước của Agent
└── HUONG_DAN_SU_DUNG.md          # Tài liệu hướng dẫn sử dụng này
```

---

## 🛠️ NÊN CHUẨN BỊ GÌ TRƯỚC KHI BẮT ĐẦU?

### 1. Chuẩn bị Notion Database
- Mở Notion và tạo 1 Database đơn giản (hoặc xem mẫu tại [notion_template_schema.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/notion_integration/notion_template_schema.md)).
- Thêm một vài ghi chú/ý tưởng thô mà bạn tích lũy được.

### 2. Kết nối Notion với Agent (Mất 2 phút)
- Xem hướng dẫn chi tiết tại [HUONG_DAN_NOTION_MCP.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20H%E1%BB%97%20tr%E1%BB%A3%20%C4%91%C4%83ng%20b%C3%A0i%20FB%20t%E1%BB%B1%20%C4%91%E1%BB%99ng/notion_integration/HUONG_DAN_NOTION_MCP.md).
- Bạn có thể đặt `NOTION_TOKEN` và `NOTION_DATABASE_ID` vào biến môi trường hoặc file `.env`.
- *Ghi chú*: Nếu chưa cài Token Notion ngay, Agent sẽ tự động chuyển sang chế độ dữ liệu mẫu (**Mock Data**) để bạn trải nghiệm ngay lập tức.

---

## 🔄 QUY TRÌNH SỬ DỤNG HẰNG NGÀY

### Bước 1: Mở Chat & Yêu Cầu
Mỗi ngày, bạn chỉ cần gõ vào ô chat:
> *"Hãy lấy dữ liệu từ Notion và gợi ý bài viết Facebook cho hôm nay."*

### Bước 2: Chọn 1 trong 5 Gợi Ý Nội Dung
Agent sẽ phân tích các ghi chú trên Notion và đề xuất **5 góc nhìn/nội dung** bài viết. Bạn chỉ cần chọn số (ví dụ: *"Tôi chọn ý tưởng số 2"*).

### Bước 3: Nhận Bài Viết Draft + Ảnh AI + File HTML Output
Agent sẽ:
1. Áp dụng công thức viết bài từ `knowledge_base/` để draft nội dung súc tích (150-300 từ).
2. Tự động sinh ảnh minh họa AI sang trọng.
3. Xuất file HTML vào thư mục `./Output/`.

### Bước 4: Mở File HTML & Copy Đăng Facebook
- Click mở file HTML xuất ra trong trình duyệt để xem trước giao diện bài viết như trên Facebook thật.
- Nhấn nút **"📋 Sao chép Bài Viết"** (1-click copy) để dán trực tiếp lên Facebook cá nhân / Fanpage!

---

## 🎨 ĐIỂM NỔI BẬT CỦA GIAO DIỆN OUTPUT HTML
- **Facebook Post Preview UI**: Mô phỏng chính xác giao diện Facebook (Dark mode), hiển thị avatar, thời gian đăng, bài viết chuẩn xuống dòng, emoji và ảnh minh họa.
- **Copy 1-Click**: Nút bấm sao chép tức thì toàn bộ nội dung văn bản.
- **Prompt AI đi kèm**: Cung cấp sẵn câu prompt tiếng Anh (Midjourney v6 / DALL-E 3) để bạn chủ động tái tạo ảnh nếu cần.
- **Thống kê chỉ số**: Hiển thị mô hình viết bài (PAS/AIDA/BAB), loại Hook, số từ và Hashtags đề xuất.
