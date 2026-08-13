#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script sinh 3 ảnh Slide Card chuẩn 1080x1080px theo đúng mẫu thiết kế người dùng cung cấp.
Sử dụng LOGO THỰC TẾ CỦA GMFINANCE (Chính xác 100% từ ảnh đính kèm của người dùng).
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


def get_circular_logo(size=64):
    """Mở logo chính thức của GMFinance và cắt tròn mượt mà."""
    if os.path.exists(OFFICIAL_LOGO_PATH):
        try:
            logo_img = Image.open(OFFICIAL_LOGO_PATH).convert("RGBA")
            logo_img = ImageOps.fit(logo_img, (size, size), method=Image.Resampling.LANCZOS)
            
            # Cắt theo khung tròn
            mask = Image.new("L", (size, size), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse([0, 0, size - 1, size - 1], fill=255)
            
            result = Image.new("RGBA", (size, size), (255, 255, 255, 0))
            result.paste(logo_img, (0, 0), mask=mask)
            return result
        except Exception as e:
            print(f"[WARN] Không thể cắt logo tròn: {e}")
    
    # Mặc định tạo vòng đen nếu thiếu ảnh
    fallback = Image.new("RGBA", (size, size), (0, 0, 0, 255))
    return fallback


def draw_brain_icon(draw, cx, cy):
    """Vẽ biểu tượng BỘ NÃO (Cognitive Overload) rõ nét ở giữa tròn."""
    draw.ellipse([cx - 50, cy - 45, cx - 2, cy + 35], fill="#ffffff")
    draw.ellipse([cx + 2, cy - 45, cx + 50, cy + 35], fill="#ffffff")
    draw.arc([cx - 40, cy - 30, cx - 10, cy], start=30, end=200, fill="#2b1a2f", width=5)
    draw.arc([cx - 38, cy - 5, cx - 12, cy + 25], start=40, end=220, fill="#2b1a2f", width=5)
    draw.arc([cx + 10, cy - 30, cx + 40, cy], start=340, end=150, fill="#2b1a2f", width=5)
    draw.arc([cx + 12, cy - 5, cx + 38, cy + 25], start=320, end=140, fill="#2b1a2f", width=5)
    draw.line([(cx, cy - 45), (cx, cy + 35)], fill="#2b1a2f", width=4)
    draw.line([(cx - 60, cy - 20), (cx - 72, cy - 28)], fill="#ffffff", width=4)
    draw.line([(cx + 60, cy - 20), (cx + 72, cy - 28)], fill="#ffffff", width=4)
    draw.line([(cx - 55, cy + 20), (cx - 68, cy + 28)], fill="#ffffff", width=4)
    draw.line([(cx + 55, cy + 20), (cx + 68, cy + 28)], fill="#ffffff", width=4)


def create_slide_card(number_str, title, body_text, output_filename, icon_type="brain"):
    width, height = 1080, 1080
    img = Image.new("RGBA", (width, height), color=(246, 246, 248, 255))
    draw = ImageDraw.Draw(img)

    # Thanh đen nhỏ góc trái trên cùng
    draw.rectangle([50, 50, 150, 62], fill="#000000")

    # Font sizes
    font_handle = get_font(32, bold=True)
    font_number = get_font(130, bold=True)
    font_title = get_font(52, bold=True)
    font_body = get_font(34, bold=False)

    # 1. Header Top Left: LOGO CHÍNH THỨC CỦA GMFINANCE (Cắt tròn 64x64px)
    logo_circle = get_circular_logo(size=68)
    img.paste(logo_circle, (160, 38), mask=logo_circle)
    draw.text((240, 52), "@GMFinance", fill="#000000", font=font_handle)

    # Đường kẻ ngang có mũi tên dẫn hướng
    draw.line([(50, 170), (580, 170)], fill="#000000", width=4)
    draw.polygon([(575, 163), (590, 170), (575, 177)], fill="#000000")

    # 2. Header Top Right: Số thứ tự (01, 02, 03)
    draw.text((840, 50), number_str, fill="#000000", font=font_number)

    # 3. Center Icon Circle
    cx, cy = 540, 430
    cr = 130
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill="#2b1a2f")

    if icon_type == "brain":
        draw_brain_icon(draw, cx, cy)
    elif icon_type == "minus":
        draw.rectangle([cx - 60, cy - 15, cx + 60, cy + 15], fill="#ffffff")
    else:
        draw.line([(cx - 40, cy), (cx - 10, cy + 30), (cx + 50, cy - 30)], fill="#ffffff", width=16)

    # 4. Title
    title_bbox = font_title.getbbox(title)
    t_w = title_bbox[2] - title_bbox[0]
    draw.text(((width - t_w) // 2, 600), title, fill="#000000", font=font_title)

    # 5. Body Text
    margin = 100
    max_w = width - (margin * 2)

    words = body_text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = font_body.getbbox(test_line)
        w = bbox[2] - bbox[0]
        if w <= max_w:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))

    y_text = 710
    for line in lines:
        l_bbox = font_body.getbbox(line)
        l_w = l_bbox[2] - l_bbox[0]
        draw.text(((width - l_w) // 2, y_text), line, fill="#2c2c2e", font=font_body)
        y_text += 52

    # Border
    draw.rectangle([0, 0, width - 1, height - 1], outline="#d0d0d5", width=2)

    filepath = os.path.join(OUTPUT_ASSETS_DIR, output_filename)
    img.convert("RGB").save(filepath, quality=95)
    print(f"[SUCCESS] Đã tạo Slide Card với Logo Chính Thức GMFinance: {filepath}")
    return filepath


def generate_all_slides():
    slide1 = create_slide_card(
        number_str="01",
        title="Bẫy Trì Hoãn 5 Giây (5-Second Trap)",
        body_text="Bộ não của bạn được lập trình để bảo vệ bạn khỏi sự mệt mỏi. Khi bạn do dự quá 5 giây, não bộ sẽ tự động nảy sinh hàng trăm lý do để lùi bước.",
        output_filename="slide_01.png",
        icon_type="brain"
    )

    slide2 = create_slide_card(
        number_str="02",
        title="Quy Tắc 5-4-3-2-1 (The 5-Second Rule)",
        body_text="Đếm ngược 5-4-3-2-1 và HÀNH ĐỘNG NGAY. Việc đếm ngược giúp ngắt dòng suy nghĩ do dự và kích hoạt ngay vùng Vỏ não trước trán (Prefrontal Cortex).",
        output_filename="slide_02.png",
        icon_type="minus"
    )

    slide3 = create_slide_card(
        number_str="03",
        title="Kích Hoạt Hành Động Đỉnh Cao (Action Trigger)",
        body_text="Đừng chờ đợi cảm hứng. Cảm hứng chỉ xuất hiện SAU KHI bạn đã bắt đầu làm việc. Đếm 5-4-3-2-1 và bứt phá mọi mục tiêu ngay hôm nay!",
        output_filename="slide_03.png",
        icon_type="check"
    )

    return [slide1, slide2, slide3]


if __name__ == "__main__":
    generate_all_slides()
