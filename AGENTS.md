# Quy Trình Vận Hành & Kiến Trúc 4 Agent - 9 Skills Của GMFinance

Hệ thống được thiết kế theo kiến trúc 4 Agent chuyên biệt làm việc phối hợp cùng bộ 9 Skills mở rộng, phục vụ thương hiệu **GMFinance - Đào tạo & Coaching ACCA**.

---

## 🤖 HỆ THỐNG 4 AGENT & 9 SKILLS CHUYÊN BIỆT

### 👑 AGENT 3: Orchestrator - Nhà Điều Phối Central Intelligence
Phụ trách tiếp nhận, chủ động khảo sát nhu cầu ngày mới và điều phối nhiệm vụ chính xác cho các Agent:
1. 🧠 **[orchestrator_dispatcher](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/orchestrator_dispatcher/SKILL.md)**: **BẮT BỤC hỏi rõ nhu cầu/định hướng chủ đề & dạng Output (Bài viết FB / Video ngắn / Repurpose) của người dùng trước khi bắt đầu**, sau đó phân bổ công việc cho Agent 1, Agent 2 và Agent 4.

---

### 🔵 AGENT 1: Content Writer & Marketing Thương Hiệu GMFinance
Phụ trách sáng tạo nội dung, thiết kế visual slide card / ảnh AI, định vị thương hiệu ACCA và tối ưu hóa tương tác:
1. ✍️ **[fb_copywriting_expert](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/fb_copywriting_expert/SKILL.md)**: Chuyên gia viết bài Facebook ngắn gọn (150-300 từ) áp dụng PAS, AIDA, HSO, BAB, Micro-learning với Hook 3 dòng đầu.
2. 🎨 **[fb_visual_creator](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/fb_visual_creator/SKILL.md)**: Thiết kế slide card kiến thức 1080x1080px (dựa trên mẫu logo & header line) + Sinh ảnh AI phong cách Chess King đẳng cấp.
3. 🏆 **[brand_awareness_gmfinance](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/brand_awareness_gmfinance/SKILL.md)**: Định vị thương hiệu **GMFinance**, slogan *"ELEVATE EXPERTISE, EXPAND CAREER HORIZONS"*.
4. 🚀 **[fb_reach_optimizer](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/fb_reach_optimizer/SKILL.md)**: Tối ưu hóa lượt xem organic, thuật toán Facebook, hashtags 3 tầng `#GMFinance #Productivity #WorkSmarter`.
5. 🔍 **[notion_content_analyzer](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/notion_content_analyzer/SKILL.md)**: Trích xuất dữ liệu Notion và gợi ý 5 góc nhìn bài viết cho ngành Năng suất & Làm việc hiệu quả.

---

### 🟢 AGENT 2: Chuyên Gia Cải Tiến Quy Trình & Bảo Tồn Bộ Nhớ (Process Improvement & Storage Maintenance)
Phụ trách giám sát chất lượng, bảo trì dung lượng bộ nhớ và liên tục nâng cấp hệ thống dựa trên phản hồi của người dùng:
1. 🔄 **[process_improvement_pdca](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/process_improvement_pdca/SKILL.md)**:
   - Ghi lại nhật ký cải tiến PDCA tại [pdca_backlog.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/logs/pdca_backlog.md).
   - Theo dõi thời gian tạo Asset/Output và tự động xóa các file Asset/Output cũ quá 7 ngày qua `scripts/cleanup_old_assets.py` để bảo toàn bộ nhớ máy tính.

---

### 🎬 AGENT 4: Video Director — Đạo Diễn Video Ngắn TikTok & FB Reels
Phụ trách viết kịch bản, thiết kế storyboard, hướng dẫn tự quay video ngắn bằng điện thoại và tối ưu phân phối video trên TikTok & FB Reels. Đồng bộ repurpose nội dung 2 chiều với Agent 1 (bài FB ↔ video):
1. 🎬 **[video_script_writer](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/video_script_writer/SKILL.md)**: Viết kịch bản video ngắn (hook 3 giây, script nói, storyboard từng cảnh, hướng dẫn góc quay/ánh sáng, text overlay 9:16, repurpose FB ↔ Video) cho 6 dạng video: Talking Head, B-Roll+Voiceover, Tutorial, Storytelling, Day-in-the-life, Reaction/Trend.
2. 📊 **[video_caption_optimizer](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.agents/skills/video_caption_optimizer/SKILL.md)**: Tối ưu caption TikTok/FB Reels, hashtag chiến lược 3 tầng, gợi ý nhạc nền trending, khung giờ đăng video tối ưu và SEO thuật toán đề xuất.

---

## 📍 QUY TRÌNH TƯƠNG TÁC HẰNG NGÀY

### 🅰️ FLOW A: TẠO BÀI VIẾT FACEBOOK (Agent 1)

1. **Khảo Sát Nhu Cầu Mới**: Agent 3 chào ngày mới và hỏi rõ nhu cầu/định hướng chủ đề & dạng Output (Bài viết FB / Video / Repurpose).
2. **Thu Thập Dữ Liệu Notion**: Agent 3 gọi Agent 1 chạy `python notion_integration/read_knowledge_vault.py` đọc dữ liệu Notion.
3. **Đề Xuất 5 Nội Dung / Góc Nhìn**: Agent 1 hiển thị 5 gợi ý bám sát nhu cầu đã chọn.
4. **Người Dùng Lựa Chọn**: Người dùng chọn 1 phương án.
5. **Soạn Thảo Bài Viết & Tạo Visual GMFinance**: Áp dụng Knowledge Base + `generate_slide_cards.py` sinh bộ 3 Slide Card chuẩn logo.
6. **Xuất Kết Quả Ra HTML & Bảo Trì Bộ Nhớ**: Agent 1 xuất file HTML trong `./Output/`. Agent 2 quét dọn dẹp các Asset cũ hơn 7 ngày để giải phóng bộ nhớ.
7. **Tự Động Lưu Nháp (Draft) & Lên Lịch Đăng 2 Fanpage**: Hỗ trợ gọi `python fb_integration/fb_publisher.py` đẩy bài nháp hoặc hẹn giờ lên lịch đăng bài cho 2 Fanpage thương hiệu (`GMFinance` & `Giải Pháp Tài Chính`).
8. **Gợi Ý Repurpose → Video**: Agent 3 hỏi "Bạn có muốn chuyển bài viết này thành kịch bản video ngắn không?" → Nếu có, chuyển cho Agent 4.

### 🅱️ FLOW B: TẠO KỊCH BẢN VIDEO NGẮN (Agent 4)

1. **Khảo Sát Nhu Cầu**: Agent 3 xác nhận chủ đề + dạng video (Talking Head / B-Roll / Tutorial / Storytelling / Day-in-the-life / Reaction).
2. **Thu Thập Dữ Liệu**: Agent 4 nhận chủ đề từ Agent 3, hoặc nhận bài FB từ Agent 1 (nếu repurpose).
3. **Đề Xuất 3 Góc Kịch Bản**: Agent 4 hiển thị 3 gợi ý kịch bản video.
4. **Người Dùng Lựa Chọn**: Chọn 1 phương án.
5. **Viết Kịch Bản & Storyboard**: Agent 4 viết full script + storyboard + hướng dẫn quay + text overlay + caption + nhạc nền.
6. **Xuất HTML Preview**: Chạy `scripts/generate_video_script_html.py` sinh file HTML preview trong `./Output/`.
7. **Gợi Ý Repurpose → Bài FB**: Agent 3 hỏi "Bạn có muốn chuyển kịch bản video này thành bài viết FB không?" → Nếu có, chuyển cho Agent 1.

---

## 🎯 2 FANPAGE THƯƠNG HIỆU MỤC TIÊU

| # | Fanpage | URL | Mô tả |
|:--|:--------|:----|:------|
| 1 | **GMFinance** | [facebook.com/financegm](https://www.facebook.com/financegm/) | Fanpage chính — Đào tạo & Coaching ACCA |
| 2 | **Giải Pháp Tài Chính & Kế Toán Việt Nam** | [facebook.com/giaiphaptaichinhvaketoanVietnam](https://www.facebook.com/giaiphaptaichinhvaketoanVietnam/) | Fanpage mở rộng — Cộng đồng Kế-Tài-Kiểm |

Cấu hình Token trong file `.env` (tham khảo [.env.example](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/.env.example) và hướng dẫn tại [HUONG_DAN_FACEBOOK_API.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/fb_integration/HUONG_DAN_FACEBOOK_API.md)).

---

## 📂 CẤU TRÚC THƯ MỤC DỰ ÁN

```
📁 AI Agent - Hỗ trợ đăng bài FB tự động/
│
├── 📄 AGENTS.md                         ← (File này) Quy trình vận hành & kiến trúc hệ thống
├── 📄 README.md                         ← Giới thiệu dự án
├── 📄 HUONG_DAN_SU_DUNG.md              ← Hướng dẫn sử dụng chi tiết
├── 📄 .env / .env.example               ← Cấu hình Token (Notion + Facebook API)
│
├── 📁 .agents/skills/                   ← 9 SKILLS CHUYÊN BIỆT
│   ├── orchestrator_dispatcher/         ← Agent 3: Điều phối & khảo sát nhu cầu
│   ├── fb_copywriting_expert/           ← Agent 1: Viết bài FB 150-300 từ
│   ├── fb_visual_creator/               ← Agent 1: Thiết kế slide card / ảnh AI
│   ├── brand_awareness_gmfinance/       ← Agent 1: Định vị thương hiệu GMFinance
│   ├── fb_reach_optimizer/              ← Agent 1: Tối ưu reach & hashtags
│   ├── notion_content_analyzer/         ← Agent 1: Phân tích dữ liệu Notion
│   ├── process_improvement_pdca/        ← Agent 2: Cải tiến PDCA & bảo trì bộ nhớ
│   ├── video_script_writer/             ← Agent 4: Kịch bản + storyboard video
│   └── video_caption_optimizer/         ← Agent 4: Caption + hashtags + nhạc nền
│
├── 📁 knowledge_base/                   ← TÀI LIỆU KIẾN THỨC
│   ├── brand_identity_gmfinance.md      ← Nhận diện thương hiệu GMFinance
│   ├── copywriting_frameworks.md        ← Framework viết bài (PAS, AIDA, HSO, BAB)
│   ├── formatting_and_tone.md           ← Quy chuẩn format & giọng văn
│   ├── proven_templates.md              ← Mẫu bài viết đã chứng minh hiệu quả
│   ├── viral_hooks_library.md           ← Thư viện 50+ Hook viral Facebook
│   └── video_script_templates.md        ← Template kịch bản video + 30 hook video
│
├── 📁 scripts/                          ← SCRIPTS TỰ ĐỘNG
│   ├── html_generator.py                ← Sinh HTML Facebook Post Preview (nhúng Base64)
│   ├── generate_slide_cards.py          ← Sinh bộ 3 Slide Card 1080x1080px (3 themes)
│   ├── generate_video_script_html.py    ← Sinh HTML Video Script Preview (copy 1-click)
│   ├── copy_slides_to_clipboard.py      ← Copy ảnh slide vào clipboard
│   └── cleanup_old_assets.py            ← Xóa Asset/Output cũ > 7 ngày
│
├── 📁 fb_integration/                   ← TÍCH HỢP FACEBOOK API
│   ├── fb_publisher.py                  ← Đẩy Draft / Lên lịch đăng 2 Fanpage
│   └── HUONG_DAN_FACEBOOK_API.md        ← Hướng dẫn lấy Page Token vĩnh viễn
│
├── 📁 notion_integration/               ← TÍCH HỢP NOTION API
│   ├── read_knowledge_vault.py          ← Đọc & lọc ghi chú từ Notion Database
│   ├── fetch_notion.py                  ← Fetch raw data từ Notion API
│   ├── search_databases.py              ← Tìm kiếm database Notion
│   ├── notion_template_schema.md        ← Cấu trúc Database Notion mẫu
│   └── HUONG_DAN_NOTION_MCP.md          ← Hướng dẫn kết nối Notion
│
├── 📁 logs/                             ← NHẬT KÝ HỆ THỐNG
│   ├── pdca_backlog.md                  ← Nhật ký cải tiến PDCA (Plan-Do-Check-Act)
│   └── storage_maintenance.log          ← Log dọn dẹp bộ nhớ tự động
│
├── 📁 Output/                           ← KẾT QUẢ ĐẦU RA
│   ├── assets/                          ← Ảnh slide card, logo GMFinance
│   ├── YYYY-MM-DD_*.html               ← File HTML FB Post Preview
│   └── YYYY-MM-DD_video_*.html         ← File HTML Video Script Preview
│
└── 📁 Brand/                            ← TÀI NGUYÊN THƯƠNG HIỆU
    └── (Logo gốc, hình ảnh mẫu...)
```

---

## 🔗 BẢN ĐỒ SCRIPTS & LỆNH CHẠY

| Script | Lệnh Chạy | Gọi Tại Bước | Chức Năng |
|:-------|:----------|:-------------|:---------|
| [read_knowledge_vault.py](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/notion_integration/read_knowledge_vault.py) | `python notion_integration/read_knowledge_vault.py` | Flow A Bước 2 | Đọc & lọc ghi chú Notion Database |
| [generate_slide_cards.py](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/scripts/generate_slide_cards.py) | `python scripts/generate_slide_cards.py` | Flow A Bước 5 | Sinh bộ 3 Slide Card 1080x1080px |
| [html_generator.py](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/scripts/html_generator.py) | `python scripts/html_generator.py` | Flow A Bước 6 | Xuất HTML FB Post Preview (Base64) |
| [fb_publisher.py](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/fb_integration/fb_publisher.py) | `python fb_integration/fb_publisher.py` | Flow A Bước 7 | Đẩy Draft / Lên lịch 2 Fanpage |
| [generate_video_script_html.py](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/scripts/generate_video_script_html.py) | `python scripts/generate_video_script_html.py` | Flow B Bước 6 | Xuất HTML Video Script Preview |
| [cleanup_old_assets.py](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/scripts/cleanup_old_assets.py) | `python scripts/cleanup_old_assets.py` | Sau mỗi Flow | Dọn dẹp file Output/Assets > 7 ngày |

---

## 📚 KNOWLEDGE BASE — TÀI LIỆU KIẾN THỨC

Agent 1 & Agent 4 **BẮT BUỘC** tra cứu Knowledge Base trước khi soạn thảo nội dung:

| File | Agent Sử Dụng | Nội Dung |
|:-----|:-------------|:---------|
| [brand_identity_gmfinance.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/knowledge_base/brand_identity_gmfinance.md) | Agent 1, 4 | Nhận diện thương hiệu, Chess King, tông màu, slogan |
| [copywriting_frameworks.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/knowledge_base/copywriting_frameworks.md) | Agent 1 | Framework PAS, AIDA, HSO, BAB, Micro-learning |
| [formatting_and_tone.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/knowledge_base/formatting_and_tone.md) | Agent 1, 4 | Quy chuẩn format, giọng văn, emoji, ngắt dòng |
| [proven_templates.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/knowledge_base/proven_templates.md) | Agent 1 | Mẫu bài viết đã viral, cấu trúc bài chuẩn |
| [viral_hooks_library.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/knowledge_base/viral_hooks_library.md) | Agent 1 | 50+ Hook viral Facebook theo 10 nhóm |
| [video_script_templates.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/knowledge_base/video_script_templates.md) | Agent 4 | 30 hook video + 3 kịch bản mẫu + pacing guide |

---

## 📖 TÀI LIỆU THAM KHẢO

- [README.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/README.md) — Giới thiệu dự án
- [HUONG_DAN_SU_DUNG.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/HUONG_DAN_SU_DUNG.md) — Hướng dẫn sử dụng chi tiết
- [HUONG_DAN_FACEBOOK_API.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/fb_integration/HUONG_DAN_FACEBOOK_API.md) — Hướng dẫn lấy Facebook Page Token
- [HUONG_DAN_NOTION_MCP.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/notion_integration/HUONG_DAN_NOTION_MCP.md) — Hướng dẫn kết nối Notion API
- [pdca_backlog.md](file:///c:/Users/PC/OneDrive%20-%20FPT%20Corporation/Documents/AI%20Agent%20-%20Hỗ%20trợ%20đăng%20bài%20FB%20tự%20động/logs/pdca_backlog.md) — Nhật ký cải tiến PDCA
