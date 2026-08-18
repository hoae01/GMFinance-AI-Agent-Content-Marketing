# -*- coding: utf-8 -*-
"""
Workflow xử lý Bài viết Facebook, Sinh ảnh Slide Card và Đăng bài/Lên lịch Fanpage cho Telegram Bot.
"""

import os
import sys
import time
from datetime import datetime, timedelta
from telegram_bot import config, ai_engine

# Import module sinh slide và module publisher
sys.path.insert(0, config.BASE_DIR)
from scripts import generate_slide_cards
from fb_integration import fb_publisher

def render_slide_cards(slides_data: list, theme: str = "modern_dark_gold") -> list:
    """
    Nhận dữ liệu 3 slides từ AI và tạo ra 3 file ảnh 1080x1080px thực tế.
    """
    image_paths = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for idx, slide in enumerate(slides_data, 1):
        num_str = f"0{idx}" if idx < 10 else str(idx)
        title = slide.get("title", f"Luận điểm {num_str}")
        body = slide.get("body", "")
        icon_type = slide.get("icon", "brain")
        
        filename = f"slide_{timestamp}_{num_str}.png"
        img_path = generate_slide_cards.create_slide_card(
            number_str=num_str,
            title=title,
            body_text=body,
            output_filename=filename,
            icon_type=icon_type,
            theme=theme
        )
        image_paths.append(img_path)
        
    return image_paths


def generate_fb_package(topic: str, custom_instructions: str = "", theme: str = "modern_dark_gold") -> dict:
    """
    Tạo trọn gói: Bài viết FB + Bộ 3 Slide Cards (1080x1080px).
    """
    ai_result = ai_engine.generate_fb_post_and_slides(topic, custom_instructions)
    post_text = ai_result.get("post_text", "")
    slides_data = ai_result.get("slides", [])
    
    # Sinh 3 ảnh slide card thật bằng Pillow
    image_paths = render_slide_cards(slides_data, theme=theme)
    
    # Lưu bài viết vào file text lưu trữ
    timestamp = datetime.now().strftime("%Y-%m-%d")
    output_txt = os.path.join(config.OUTPUT_DIR, f"{timestamp}_fb_post.txt")
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(post_text)
        
    return {
        "topic": topic,
        "post_text": post_text,
        "image_paths": image_paths,
        "slides_data": slides_data,
        "theme": theme,
        "hashtags": ai_result.get("hashtags", [])
    }


def execute_fb_action(post_text: str, image_paths: list, action_type: str, page_choice: str = "1", custom_datetime_str: str = None) -> dict:
    """
    Thực thi hành động đăng bài / lưu nháp / lên lịch lên Fanpage.
    - action_type: 'draft', 'publish_now', 'schedule_830', 'schedule_1130', 'schedule_2000', 'schedule_custom'
    - page_choice: '1' (GMFinance), '2' (Giải Pháp Tài Chính), 'all' (Cả 2)
    """
    is_draft = True
    schedule_time_str = None
    
    now = datetime.now()
    if action_type == "publish_now":
        is_draft = False
    elif action_type == "draft":
        is_draft = True
    elif action_type == "schedule_830":
        # 08:30 sáng mai
        target_date = now + timedelta(days=1)
        schedule_time_str = target_date.strftime("%Y-%m-%d 08:30")
        is_draft = False
    elif action_type == "schedule_1130":
        # 11:30 trưa nay (hoặc trưa mai nếu đã qua 11:30)
        target_date = now if now.hour < 11 else now + timedelta(days=1)
        schedule_time_str = target_date.strftime("%Y-%m-%d 11:30")
        is_draft = False
    elif action_type == "schedule_2000":
        # 20:00 tối nay (hoặc tối mai nếu đã qua 20:00)
        target_date = now if now.hour < 20 else now + timedelta(days=1)
        schedule_time_str = target_date.strftime("%Y-%m-%d 20:00")
        is_draft = False
    elif action_type == "schedule_custom" and custom_datetime_str:
        schedule_time_str = custom_datetime_str
        is_draft = False

    pages_to_publish = ["1", "2"] if page_choice == "all" else [page_choice]
    results = []
    
    for pk in pages_to_publish:
        res = fb_publisher.publish_or_schedule_post(
            page_key=pk,
            message=post_text,
            image_paths=image_paths,
            is_draft=is_draft,
            schedule_time_str=schedule_time_str
        )
        results.append(res)
        
    return {
        "action_type": action_type,
        "schedule_time": schedule_time_str,
        "results": results
    }
