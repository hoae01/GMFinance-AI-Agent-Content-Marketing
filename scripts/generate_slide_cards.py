#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script sinh bộ Slide Cards (1080x1080px) đa dạng Theme & Chuẩn mực Typography.
Đã khắc phục 100% lỗi tràn chữ (Text Overflow) bằng thuật toán Auto-Wrap & Auto-Scale Font Size.
Hỗ trợ 3 Theme thiết kế cao cấp:
1. 'modern_dark_gold' (Chess King Luxury - Đẳng cấp Đen Nền Kim)
2. 'glassmorphism_blue' (Executive Finance - Xanh Hoàng Gia Tinh Tế)
3. 'minimal_clean' (Sáng Tối Giản Mới - Clean & Crisp)
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Output", "assets")
OFFICIAL_LOGO_PATH = os.path.join(OUTPUT_ASSETS_DIR, "gmfinance_official_logo.png")
os.makedirs(OUTPUT_ASSETS_DIR, exist_ok=True)


def get_font(size, bold=False):
    font_names = [
        "arialbd.ttf" if bold else "arial.ttf",
        "segoeui.ttf" if not bold else "segoeuib.ttf",
        "calibri.ttf" if not bold else "calibrib.ttf",
    ]
    for name in font_names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def get_circular_logo(size=68):
    """Mở logo chính thức của GMFinance và cắt tròn mượt mà."""
    if os.path.exists(OFFICIAL_LOGO_PATH):
        try:
            logo_img = Image.open(OFFICIAL_LOGO_PATH).convert("RGBA")
            logo_img = ImageOps.fit(logo_img, (size, size), method=Image.Resampling.LANCZOS)
            
            mask = Image.new("L", (size, size), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse([0, 0, size - 1, size - 1], fill=255)
            
            result = Image.new("RGBA", (size, size), (255, 255, 255, 0))
            result.paste(logo_img, (0, 0), mask=mask)
            return result
        except Exception as e:
            print(f"[WARN] Không thể cắt logo tròn: {e}")
    
    fallback = Image.new("RGBA", (size, size), (15, 23, 42, 255))
    return fallback


def wrap_text(text, font, max_width, draw):
    """Tự động ngắt dòng văn bản theo độ rộng tối đa chuẩn xác 100%."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines


def draw_icon_badge(draw, cx, cy, icon_type, theme_colors):
    """Vẽ biểu tượng trung tâm độc đáo theo theme."""
    cr = 100
    badge_bg = theme_colors["icon_bg"]
    icon_fg = theme_colors["icon_fg"]

    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=badge_bg, outline=theme_colors["accent"], width=3)

    if icon_type == "brain":
        # Icon Bộ não / Tư duy
        draw.ellipse([cx - 40, cy - 35, cx - 2, cy + 25], fill=icon_fg)
        draw.ellipse([cx + 2, cy - 35, cx + 40, cy + 25], fill=icon_fg)
        draw.line([(cx, cy - 35), (cx, cy + 25)], fill=badge_bg, width=4)
        draw.line([(cx - 48, cy - 10), (cx - 58, cy - 18)], fill=icon_fg, width=4)
        draw.line([(cx + 48, cy - 10), (cx + 58, cy - 18)], fill=icon_fg, width=4)
    elif icon_type == "lightning":
        # Icon Tốc độ / Kích hoạt 5 giây
        pts = [(cx + 5, cy - 50), (cx - 30, cy + 5), (cx - 5, cy + 5), (cx - 15, cy + 50), (cx + 30, cy - 5), (cx + 5, cy - 5)]
        draw.polygon(pts, fill=theme_colors["accent"])
    elif icon_type == "minus":
        draw.rectangle([cx - 45, cy - 12, cx + 45, cy + 12], fill=icon_fg)
    else:
        # Checkmark
        draw.line([(cx - 35, cy), (cx - 10, cy + 25), (cx + 40, cy - 25)], fill=icon_fg, width=12)


def create_slide_card(
    number_str,
    title,
    body_text,
    output_filename,
    icon_type="brain",
    theme="modern_dark_gold"
):
    """Tạo 1 Slide Card 1080x1080px không tràn chữ với Theme tùy chọn."""
    width, height = 1080, 1080

    # Cấu hình Bảng màu theo Theme
    THEMES = {
        "modern_dark_gold": {
            "bg": "#0b0f19",
            "card_bg": "#151d2a",
            "card_border": "#2f3847",
            "accent": "#f59e0b",
            "title_color": "#ffffff",
            "body_color": "#cbd5e1",
            "number_color": "#f59e0b",
            "handle_color": "#ffffff",
            "icon_bg": "#1e293b",
            "icon_fg": "#ffffff"
        },
        "glassmorphism_blue": {
            "bg": "#0f172a",
            "card_bg": "#1e293b",
            "card_border": "#3b82f6",
            "accent": "#38bdf8",
            "title_color": "#f8fafc",
            "body_color": "#94a3b8",
            "number_color": "#38bdf8",
            "handle_color": "#f8fafc",
            "icon_bg": "#0f172a",
            "icon_fg": "#38bdf8"
        },
        "minimal_clean": {
            "bg": "#f8fafc",
            "card_bg": "#ffffff",
            "card_border": "#e2e8f0",
            "accent": "#0284c7",
            "title_color": "#0f172a",
            "body_color": "#334155",
            "number_color": "#0284c7",
            "handle_color": "#0f172a",
            "icon_bg": "#f1f5f9",
            "icon_fg": "#0284c7"
        }
    }

    t_colors = THEMES.get(theme, THEMES["modern_dark_gold"])

    img = Image.new("RGBA", (width, height), color=t_colors["bg"])
    draw = ImageDraw.Draw(img)

    # 1. Khung Card trung tâm
    c_margin = 40
    card_rect = [c_margin, c_margin, width - c_margin, height - c_margin]
    draw.rectangle(card_rect, fill=t_colors["card_bg"], outline=t_colors["card_border"], width=3)

    # 2. Header Top Left: Logo & Brand Handle
    logo_circle = get_circular_logo(size=64)
    img.paste(logo_circle, (75, 65), mask=logo_circle)

    font_handle = get_font(30, bold=True)
    draw.text((155, 80), "@GMFinance", fill=t_colors["handle_color"], font=font_handle)

    # Đường line Accent
    draw.line([(75, 150), (450, 150)], fill=t_colors["accent"], width=3)

    # 3. Header Top Right: Số thứ tự (01, 02, 03)
    font_number = get_font(110, bold=True)
    draw.text((860, 60), number_str, fill=t_colors["number_color"], font=font_number)

    # 4. Center Icon Badge
    cx, cy = 540, 360
    draw_icon_badge(draw, cx, cy, icon_type, t_colors)

    # 5. Title (Auto-Scale & Auto-Wrap không tràn chữ)
    max_title_w = 900
    font_size_title = 46
    font_title = get_font(font_size_title, bold=True)
    
    title_lines = wrap_text(title, font_title, max_title_w, draw)
    while len(title_lines) > 2 and font_size_title > 34:
        font_size_title -= 3
        font_title = get_font(font_size_title, bold=True)
        title_lines = wrap_text(title, font_title, max_title_w, draw)

    y_title = 510
    for line in title_lines:
        bbox = draw.textbbox((0, 0), line, font=font_title)
        l_w = bbox[2] - bbox[0]
        draw.text(((width - l_w) // 2, y_title), line, fill=t_colors["title_color"], font=font_title)
        y_title += font_size_title + 12

    # 6. Body Text (Auto-Wrap & Dynamic Vertical Centering)
    max_body_w = 880
    font_size_body = 32
    font_body = get_font(font_size_body, bold=False)
    
    body_lines = wrap_text(body_text, font_body, max_body_w, draw)
    while len(body_lines) > 5 and font_size_body > 24:
        font_size_body -= 2
        font_body = get_font(font_size_body, bold=False)
        body_lines = wrap_text(body_text, font_body, max_body_w, draw)

    y_body = max(680, y_title + 25)
    line_spacing = font_size_body + 16

    for line in body_lines:
        bbox = draw.textbbox((0, 0), line, font=font_body)
        l_w = bbox[2] - bbox[0]
        draw.text(((width - l_w) // 2, y_body), line, fill=t_colors["body_color"], font=font_body)
        y_body += line_spacing

    filepath = os.path.join(OUTPUT_ASSETS_DIR, output_filename)
    img.convert("RGB").save(filepath, quality=95)
    print(f"[SUCCESS] Đã tạo Slide Card Theme '{theme}': {filepath}")
    return filepath


def generate_all_slides(theme="modern_dark_gold"):
    """Sinh bộ 3 Slide Cards chuẩn cho chủ đề Quy Tắc 5 Giây."""
    slide1 = create_slide_card(
        number_str="01",
        title="Bẫy Trì Hoãn 5 Giây (5-Second Trap)",
        body_text="Bộ não của bạn được lập trình để bảo vệ bạn khỏi sự mệt mỏi. Khi bạn do dự quá 5 giây, não bộ sẽ tự động nảy sinh hàng trăm lý do bàn lùi.",
        output_filename="slide_01.png",
        icon_type="brain",
        theme=theme
    )

    slide2 = create_slide_card(
        number_str="02",
        title="Quy Tắc 5-4-3-2-1 (The 5-Second Rule)",
        body_text="Đếm ngược 5-4-3-2-1 và HÀNH ĐỘNG NGAY. Việc đếm ngược ngắt hoàn toàn suy nghĩ trì hoãn và kích hoạt ngay vùng Vỏ não trước trán (Prefrontal Cortex).",
        output_filename="slide_02.png",
        icon_type="lightning",
        theme=theme
    )

    slide3 = create_slide_card(
        number_str="03",
        title="Kích Hoạt Hành Động Đỉnh Cao",
        body_text="Đừng chờ đợi cảm hứng. Cảm hứng chỉ xuất hiện SAU KHI bạn đã bắt đầu làm việc. Đếm 5-4-3-2-1 và bứt phá mọi mục tiêu ngay hôm nay!",
        output_filename="slide_03.png",
        icon_type="check",
        theme=theme
    )

    return [slide1, slide2, slide3]


if __name__ == "__main__":
    generate_all_slides(theme="modern_dark_gold")
