---
name: fb_visual_creator
description: Chuyên gia thiết kế ý tưởng hình ảnh và viết prompt sinh ảnh AI (Midjourney/DALL-E 3/Flux) đi kèm nội dung bài viết Facebook ngắn gọn, trực quan, phù hợp ngữ cảnh.
---

# Skill: Chuyên Gia Tạo Hình Ảnh Minh Họa Facebook (FB Visual Creator)

## 📌 Vai Trò & Mục Tiêu
Skill này hỗ trợ Agent tự động chuyển hóa ý tưởng bài viết thành hình ảnh minh họa giàu tính thẩm mỹ và chuyên nghiệp:
- **Tạo ảnh minh họa AI**: Gọi công cụ `generate_image` tạo ảnh 3D Digital Art / Minimalist / Modern Art phù hợp với nội dung bài viết.
- **Viết Prompt tiếng Anh chuẩn AI Image Generator**: Viết prompt cho DALL-E 3 / Midjourney v6 / Flux bao gồm: Chủ đề chính, Phong cách nghệ thuật (Style), Màu sắc (Color palette), Ánh sáng (Lighting), Tỷ lệ khung hình và Độ phân giải.
- **Tối ưu hiển thị Bố cục**: Đảm bảo hình ảnh đồng bộ với tông giọng bài viết và lưu ảnh chuẩn vào `./Output/assets/`.

---

## 🎨 Quy Trình Tạo Ảnh Minh Họa

### Bước 1: Phân Tích Thông Điệp Bài Viết
Xác định từ khóa biểu tượng chính của bài viết (Vd: Năng suất -> Đồng hồ 3D/Lịch làm việc; AI -> Bộ não robot phát sáng/Giao diện tương lai; Sự nghiệp -> Nấc thang/Ngọn núi).

### Bước 2: Xây Dựng Prompt AI Tiếng Anh Cực Chuẩn
Sử dụng cấu trúc Prompt 5 thành phần:
`[Subject] + [Environment/Context] + [Art Style] + [Color & Lighting] + [Parameters]`

*Ví dụ Prompt*:
> "A high-end 3D digital artwork illustration representing time management, glowing futuristic glass calendar blocks floating in dark space, neon blue and violet gradient lighting, clean minimalist aesthetic, octane render, 8k resolution"

### Bước 3: Thực Thi & Lưu Sản Phẩm
1. Gọi công cụ `generate_image` với prompt đã chuẩn bị.
2. Lưu ảnh tạo được vào `./Output/assets/`.
3. Nhúng ảnh vào file HTML Facebook Preview và lưuPrompt gốc vào khung Prompt trên giao diện HTML để người dùng dễ dàng tùy chỉnh lại khi cần.
