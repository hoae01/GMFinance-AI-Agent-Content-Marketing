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

