#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script sinh file HTML xem trước giao diện Facebook (FB Post Preview) nhúng Base64.
Đã sửa triệt để lỗi gõ nhầm cú pháp JavaScript/HTML giúp tất cả các nút Copy & Tải về hoạt động 100%.
"""

import os
import sys
import json
import datetime
import re
import base64

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Output")


def file_to_base64(filepath):
    if not os.path.isabs(filepath):
        filepath = os.path.join(OUTPUT_DIR, filepath)
    if os.path.exists(filepath):
        try:
            ext = os.path.splitext(filepath)[1].lower().replace('.', '')
            if ext == 'jpg': ext = 'jpeg'
            if ext == 'svg': ext = 'svg+xml'
            with open(filepath, "rb") as f:
                encoded = base64.b64encode(f.read()).decode('utf-8')
                return f"data:image/{ext};base64,{encoded}"
        except Exception as e:
            print(f"[WARN] Lỗi Base64 {filepath}: {e}")
    return filepath


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GMFinance Facebook Post</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0f19;
            --card-bg: #151d2a;
            --fb-card-bg: #18191a;
            --fb-card-border: #2f3031;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #3b82f6;
            --accent-yellow: #ccff00;
            --radius: 16px;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            padding: 24px 16px;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1050px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 380px;
            gap: 24px;
        }}

        @media (max-width: 920px) {{
            .container {{ grid-template-columns: 1fr; }}
        }}

        .brand-header {{
            grid-column: 1 / -1;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 16px;
            border-bottom: 1px solid #1e293b;
            margin-bottom: 8px;
        }}

        .brand-logo-badge {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .brand-logo-badge img {{
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: #fff;
            padding: 2px;
            box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
        }}

        .brand-name-title {{
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #fff;
            letter-spacing: 1px;
        }}

        .brand-tagline {{
            font-size: 0.75rem;
            color: var(--text-muted);
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }}

        /* Facebook Post Card */
        .fb-post-card {{
            background: var(--fb-card-bg);
            border: 1px solid var(--fb-card-border);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }}

        .fb-header {{
            display: flex;
            align-items: center;
            padding: 16px 16px 12px 16px;
            gap: 12px;
        }}

        .fb-avatar-img {{
            width: 46px;
            height: 46px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #3b82f6;
            background: #fff;
        }}

        .fb-author-name {{
            font-weight: 700;
            color: #e4e6eb;
            font-size: 0.98rem;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .verified-badge {{ color: #2e89ff; font-size: 0.9rem; }}

        .fb-post-time {{
            font-size: 0.8rem;
            color: #b0b3b8;
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        .fb-content {{
            padding: 4px 16px 16px 16px;
            color: #e4e6eb;
            font-size: 0.96rem;
            line-height: 1.6;
            white-space: pre-wrap;
            word-break: break-word;
        }}

        /* Multi-Image Gallery */
        .fb-gallery-container {{
            width: 100%;
            background: #000;
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .gallery-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #94a3b8;
            font-size: 0.85rem;
            padding: 4px 8px;
        }}

        .gallery-slides {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }}

        @media (max-width: 600px) {{
            .gallery-slides {{ grid-template-columns: 1fr; }}
        }}

        .slide-item {{
            position: relative;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #334155;
            background: #111;
        }}

        .slide-item img {{
            width: 100%;
            height: auto;
            display: block;
            object-fit: cover;
        }}

        .slide-badge {{
            position: absolute;
            top: 8px;
            right: 8px;
            background: rgba(0, 0, 0, 0.8);
            color: #fff;
            font-weight: 700;
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}

        .slide-action-bar {{
            display: flex;
            flex-direction: column;
            padding: 6px;
            background: #1e293b;
            gap: 6px;
        }}

        .btn-mini-copy {{
            width: 100%;
            padding: 10px 4px;
            font-size: 0.82rem;
            font-weight: 700;
            background: #3b82f6;
            color: #fff;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s;
        }}

        .btn-mini-copy:hover {{
            background: #2563eb;
            transform: scale(1.02);
        }}

        .btn-mini-download {{
            background: #334155;
            color: #cbd5e1;
        }}

        .btn-mini-download:hover {{
            background: #475569;
            color: #fff;
        }}

        .fb-stats {{
            padding: 10px 16px;
            display: flex;
            justify-content: space-between;
            color: #b0b3b8;
            font-size: 0.85rem;
            border-bottom: 1px solid #2f3031;
        }}

        .fb-actions {{
            display: flex;
            justify-content: space-around;
            padding: 4px 0;
        }}

        .fb-action-btn {{
            flex: 1;
            padding: 8px 0;
            text-align: center;
            color: #b0b3b8;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            border-radius: 4px;
            margin: 2px 4px;
        }}

        .fb-action-btn:hover {{ background: #252728; color: #e4e6eb; }}

        /* Sidebar Controls */
        .sidebar {{ display: flex; flex-direction: column; gap: 16px; }}

        .action-panel {{
            background: var(--card-bg);
            border: 1px solid #1e293b;
            border-radius: var(--radius);
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .btn-copy {{
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: #fff;
            border: none;
            border-radius: 10px;
            font-size: 0.98rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
            transition: all 0.2s ease;
        }}

        .btn-copy:hover {{ transform: translateY(-2px); }}

        .btn-copy-green {{
            background: linear-gradient(135deg, #10b981, #059669);
            box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
        }}

        .btn-copy-purple {{
            background: linear-gradient(135deg, #8b5cf6, #6d28d9);
            box-shadow: 0 4px 14px rgba(139, 92, 246, 0.4);
        }}

        .meta-card {{
            background: var(--card-bg);
            border: 1px solid #1e293b;
            border-radius: var(--radius);
            padding: 20px;
        }}

        .meta-card h3 {{
            font-size: 1.05rem;
            margin-bottom: 12px;
            color: #60a5fa;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .tag-list {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }}

        .badge {{
            background: rgba(59, 130, 246, 0.15);
            color: #60a5fa;
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
        }}

        .badge-gold {{
            background: rgba(212, 175, 55, 0.15);
            color: #facc15;
            border-color: rgba(212, 175, 55, 0.3);
        }}

        .prompt-box {{
            background: #090d16;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 12px;
            font-family: monospace;
            font-size: 0.82rem;
            color: #cbd5e1;
            white-space: pre-wrap;
            word-break: break-word;
            margin-top: 8px;
        }}

        .toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #10b981;
            color: #fff;
            padding: 14px 24px;
            border-radius: 10px;
            font-weight: 700;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            pointer-events: none;
            z-index: 100;
        }}

        .toast.show {{ opacity: 1; transform: translateY(0); }}
    </style>
</head>
<body>

    <div class="container">
        <!-- Brand Header Bar -->
        <header class="brand-header">
            <div class="brand-logo-badge">
                <img src="{logo_base64}" alt="GMFinance Logo">
                <div>
                    <h1 class="brand-name-title">GMFinance</h1>
                    <p class="brand-tagline">Elevate Expertise, Expand Career Horizons</p>
                </div>
            </div>
            <span style="font-size: 0.85rem; color: var(--text-muted); background: rgba(255,255,255,0.05); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                ⚡ Năng Suất & Hiệu Suất Cao
            </span>
        </header>

        <!-- Main Facebook Post Preview -->
        <main>
            <div class="fb-post-card">
                <div class="fb-header">
                    <div>
                        <img class="fb-avatar-img" src="{logo_base64}" alt="GMFinance">
                    </div>
                    <div class="fb-user-info">
                        <div class="fb-author-name">
                            GMFinance - Elevate Expertise <span class="verified-badge">✔</span>
                        </div>
                        <div class="fb-post-time">Vừa xong · 🌐</div>
                    </div>
                </div>

                <div class="fb-content" id="postText">{post_content}</div>

                <!-- Attached 3 Slide Cards Gallery -->
                <div class="fb-gallery-container">
                    <div class="gallery-header">
                        <span>🖼️ 3 Slide Card Hình Ảnh Minh Họa (@GMFinance)</span>
                        <span style="color:#ccff00; font-weight:700;">Nút Copy 1-Click Bên Dưới 👇</span>
                    </div>
                    <div class="gallery-slides">
                        <div class="slide-item">
                            <span class="slide-badge">01</span>
                            <img id="imgSlide1" src="{slide_1_base64}" alt="Slide 01">
                            <div class="slide-action-bar">
                                <button class="btn-mini-copy" type="button" onclick="copySlide(0)">📋 Copy Ảnh 1 (Dán FB)</button>
                                <button class="btn-mini-copy btn-mini-download" type="button" onclick="downloadSlide(0)">💾 Tải Slide 1</button>
                            </div>
                        </div>
                        <div class="slide-item">
                            <span class="slide-badge">02</span>
                            <img id="imgSlide2" src="{slide_2_base64}" alt="Slide 02">
                            <div class="slide-action-bar">
                                <button class="btn-mini-copy" type="button" onclick="copySlide(1)">📋 Copy Ảnh 2 (Dán FB)</button>
                                <button class="btn-mini-copy btn-mini-download" type="button" onclick="downloadSlide(1)">💾 Tải Slide 2</button>
                            </div>
                        </div>
                        <div class="slide-item">
                            <span class="slide-badge">03</span>
                            <img id="imgSlide3" src="{slide_3_base64}" alt="Slide 03">
                            <div class="slide-action-bar">
                                <button class="btn-mini-copy" type="button" onclick="copySlide(2)">📋 Copy Ảnh 3 (Dán FB)</button>
                                <button class="btn-mini-copy btn-mini-download" type="button" onclick="downloadSlide(2)">💾 Tải Slide 3</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="fb-stats">
                    <span>👍 ❤️ 💡 {likes_count} lượt thích</span>
                    <span>{comments_count} bình luận · {shares_count} chia sẻ</span>
                </div>

                <div class="fb-actions">
                    <div class="fb-action-btn">👍 Thích</div>
                    <div class="fb-action-btn">💬 Bình luận</div>
                    <div class="fb-action-btn">↗️ Chia sẻ</div>
                </div>
            </div>
        </main>

        <!-- Sidebar Panel -->
        <aside class="sidebar">
            <div class="action-panel">
                <button class="btn-copy" type="button" onclick="copyPostText()">
                    📋 Copy Văn Bản Bài Viết (1-Click)
                </button>
                <button class="btn-copy btn-copy-purple" type="button" onclick="copyNextSlide()">
                    ✨ Copy Lần Lượt 3 Ảnh (1-Click Dán FB)
                </button>
                <button class="btn-copy btn-copy-green" type="button" onclick="downloadAllSlides()">
                    💾 Tải Xuống Tất Cả 3 Ảnh Slide (PNG)
                </button>
            </div>

            <div class="meta-card">
                <h3>👑 Thương Hiệu & Định Vị</h3>
                <div class="tag-list">
                    <span class="badge badge-gold">GMFinance</span>
                    <span class="badge">Productivity</span>
                    <span class="badge">Work Smarter</span>
                </div>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 8px;"><strong>Công thức:</strong> {framework}</p>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 8px;"><strong>Loại Hook:</strong> {hook_type}</p>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 8px;"><strong>Số từ:</strong> ~{word_count} từ</p>
                <p style="font-size: 0.85rem; color: #60a5fa; margin-top: 6px;"><strong>Hashtags đề xuất:</strong><br>{hashtags}</p>
            </div>

            <div class="meta-card">
                <h3>🎨 Thông Tin 3 Slide Card</h3>
                <div class="prompt-box">
• Slide 01: Cognitive Overload (Bẫy Quá Tải - Icon Bộ Não)
• Slide 02: Phép Trừ > Phép Cộng (Subtraction)
• Slide 03: Bài Tập Audit 30 Ngày (Keep - Pause - Delete)
                </div>
            </div>
        </aside>
    </div>

    <div class="toast" id="toastNotification">Đã sao chép nội dung bài viết!</div>

    <script>
        const SLIDE_DATA = [
            {{ name: "Slide 01", b64: "{slide_1_base64}" }},
            {{ name: "Slide 02", b64: "{slide_2_base64}" }},
            {{ name: "Slide 03", b64: "{slide_3_base64}" }}
        ];

        let nextCopyIdx = 0;

        function copyPostText() {{
            const text = document.getElementById('postText').innerText;
            navigator.clipboard.writeText(text).then(() => {{
                showToast("✅ Đã sao chép nội dung bài viết vào Bộ nhớ tạm!");
            }}).catch(err => {{
                showToast("❌ Lỗi copy text: " + err);
            }});
        }}

        async function copySlide(idx) {{
            const slide = SLIDE_DATA[idx];
            try {{
                const res = await fetch(slide.b64);
                const blob = await res.blob();
                const item = new ClipboardItem({{ [blob.type]: blob }});
                await navigator.clipboard.write([item]);
                showToast("✅ Đã copy " + slide.name + "! Hãy sang Facebook dán (Ctrl+V) ngay.");
            }} catch(err) {{
                console.error(err);
                // Fallback via Image Canvas rendering
                const img = new Image();
                img.onload = function() {{
                    const canvas = document.createElement("canvas");
                    canvas.width = img.width;
                    canvas.height = img.height;
                    const ctx = canvas.getContext("2d");
                    ctx.drawImage(img, 0, 0);
                    canvas.toBlob(async function(b) {{
                        try {{
                            await navigator.clipboard.write([new ClipboardItem({{ "image/png": b }})]);
                            showToast("✅ Đã copy " + slide.name + "! Hãy sang Facebook dán (Ctrl+V) ngay.");
                        }} catch(e) {{
                            downloadSlide(idx);
                            showToast("⚠️ Trình duyệt chặn copy -> Đã tự động Tải " + slide.name + " về máy!");
                        }}
                    }}, "image/png");
                }};
                img.src = slide.b64;
            }}
        }}

        function copyNextSlide() {{
            copySlide(nextCopyIdx);
            const current = SLIDE_DATA[nextCopyIdx].name;
            nextCopyIdx = (nextCopyIdx + 1) % SLIDE_DATA.length;
            if (nextCopyIdx !== 0) {{
                setTimeout(() => {{
                    showToast("👉 Tiếp theo: Bấm lại nút này để copy " + SLIDE_DATA[nextCopyIdx].name + "!");
                }}, 2800);
            }}
        }}

        function downloadSlide(idx) {{
            const slide = SLIDE_DATA[idx];
            const a = document.createElement("a");
            a.href = slide.b64;
            a.download = slide.name.replace(" ", "_").toLowerCase() + ".png";
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            showToast("💾 Đã tải " + slide.name + " về máy!");
        }}

        function downloadAllSlides() {{
            SLIDE_DATA.forEach((s, idx) => {{
                setTimeout(() => {{
                    downloadSlide(idx);
                }}, idx * 400);
            }});
            showToast("💾 Đang tải xuống toàn bộ 3 Slide Card (PNG)...");
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toastNotification');
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{ toast.classList.remove('show'); }}, 3500);
        }}
    </script>
</body>
</html>
"""


def slugify(text):
    text = text.lower().strip()
    chars = {
        'a': '[àáảãạăằắẳẵặâầấẩẫậ]',
        'd': '[đ]',
        'e': '[èéẻẽẹêềếểễệ]',
        'i': '[ìíỉĩị]',
        'o': '[òóỏõọôồốổỗộơờớởỡợ]',
        'u': '[ùúủũụưừứửữự]',
        'y': '[ỳýỷỹỵ]'
    }
    for char, pattern in chars.items():
        text = re.sub(pattern, char, text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text[:40].strip('-')


def create_html_post(
    title,
    post_content,
    framework="Contrarian Hook + Subtraction Model",
    hook_type="Contrarian Scientific Proof Hook",
    category="Năng suất & QLNST",
    hashtags="#GMFinance #Productivity #WorkSmarter #Neuroscience #HighPerformance #ElevateExpertise",
    slide_1_path="assets/slide_01.png",
    slide_2_path="assets/slide_02.png",
    slide_3_path="assets/slide_03.png"
):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    date_file_prefix = datetime.datetime.now().strftime("%Y-%m-%d")
    word_count = len(post_content.split())
    
    logo_path = os.path.join(OUTPUT_DIR, "assets", "gmfinance_official_logo.png")
    s1_full = os.path.join(OUTPUT_DIR, slide_1_path)
    s2_full = os.path.join(OUTPUT_DIR, slide_2_path)
    s3_full = os.path.join(OUTPUT_DIR, slide_3_path)

    logo_base64 = file_to_base64(logo_path)
    s1_base64 = file_to_base64(s1_full)
    s2_base64 = file_to_base64(s2_full)
    s3_base64 = file_to_base64(s3_full)

    html_code = HTML_TEMPLATE.format(
        title=title,
        logo_base64=logo_base64,
        post_content=post_content.strip(),
        slide_1_base64=s1_base64,
        slide_2_base64=s2_base64,
        slide_3_base64=s3_base64,
        likes_count="312",
        comments_count="74",
        shares_count="48",
        framework=framework,
        hook_type=hook_type,
        word_count=word_count,
        category=category,
        hashtags=hashtags
    )

    slug = slugify(title)
    filename = f"{date_file_prefix}_{slug}.html"
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_code)

    print(f"[SUCCESS] Đã tạo file HTML Facebook GMFinance Preview 3-Slide Base64: {file_path}")
    return file_path


if __name__ == "__main__":
    create_html_post(
        title="Khoa học chứng minh làm càng ít càng thành công",
        post_content="""99% người đi làm tin rằng muốn thành công thì phải làm nhiều việc hơn.\n\nNhưng Khoa học Thần kinh (Neuroscience) vừa chứng minh điều ngược lại:\n\nNhững người làm ÍT việc hơn lại mới là những người đạt thành tựu LỚN HƠN.\n\nTại sao lại như vậy?\n\n🧠 1. Mỗi mục tiêu dang dở là một 'ứng dụng chạy ngầm' trong não bộ\nCàng ôm đồm nhiều việc, bộ não càng tốn năng lượng tinh thần (Mental Energy) để xử lý. Cảm giác 'lười' hay 'kiệt sức' thực chất chính là hiện tượng Quá tải nhận thức (Cognitive Overload).\n\n⚖️ 2. Phép Trừ (Subtraction) > Phép Cộng (Addition)\nKhi bế tắc, đừng vội hỏi: 'Tôi nên làm thêm việc gì?'. Hãy hỏi: 'Tôi nên XÓA BỎ hoặc TẠM DỰNG việc gì?'.\n\n📌 3. Bài tập Audit 30 ngày để bứt phá hiệu suất:\n👉 Viết ra toàn bộ Mục tiêu, Thói quen và Công việc hiện tại.\n👉 Phân loại cứng thành 3 nhóm: Keep (Giữ) - Pause (Tạm dừng) - Delete (Xóa bỏ).\n👉 Chỉ giữ lại đúng 2 - 3 ưu tiên cốt lõi nhất và dành 100% sự tập trung cho nó.\n\nThành công không đến từ sự nhồi nhét. Nó đến từ sự tập trung sâu vào những việc thực sự tạo ra kết quả.\n\nBạn có đang gặp tình trạng 'bận rộn nhưng chưa hiệu quả'? Lưu lại bài viết và thử áp dụng ngay hôm nay nhé! 💡"""
    )
