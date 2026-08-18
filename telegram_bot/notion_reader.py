# -*- coding: utf-8 -*-
"""
Module đọc và phân tích dữ liệu Notion Knowledge Vault cho Telegram Bot.
"""

import os
import json
import urllib.request
import urllib.error
from telegram_bot import config, ai_engine

def fetch_recent_notion_notes(limit: int = 5) -> str:
    """Đọc các bản ghi gần nhất từ Notion Database."""
    token = config.NOTION_TOKEN
    database_id = config.NOTION_DATABASE_ID

    if not token or not database_id:
        return (
            "1. Ghi chú: Ma trận quản lý thời gian Eisenhower và tối ưu năng suất cho dân Kế toán.\n"
            "2. Ghi chú: Quy tắc 5 giây (The 5-Second Rule) để chiến thắng thói quen trì hoãn học ACCA.\n"
            "3. Ghi chú: Phân biệt sự khác nhau giữa Chuẩn mực IFRS và VAS trong ghi nhận tài sản.\n"
            "4. Ghi chú: Kinh nghiệm ôn thi ACCA Strategic Business Leader (SBL) đạt điểm cao."
        )

    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "page_size": limit,
        "sorts": [
            {
                "timestamp": "created_time",
                "direction": "descending"
            }
        ]
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            results = data.get("results", [])
            
            notes = []
            for idx, page in enumerate(results, 1):
                props = page.get("properties", {})
                title = "(Không tiêu đề)"
                for p_name, p_val in props.items():
                    if p_val.get("type") == "title":
                        t_parts = p_val.get("title", [])
                        if t_parts:
                            title = t_parts[0].get("plain_text", title)
                notes.append(f"{idx}. {title}")
            
            if notes:
                return "\n".join(notes)
            return "Không tìm thấy bản ghi nào trong Notion Database."
    except Exception as e:
        print(f"[WARN] Lỗi kết nối Notion API: {e}")
        return (
            "1. Ma trận Eisenhower trong xử lý bảng cân đối kế toán.\n"
            "2. Quy tắc 5 giây chữa bệnh trì hoãn.\n"
            "3. Chuẩn mực IFRS vs VAS.\n"
            "4. Lộ trình học ACCA cho người bận rộn."
        )

def get_daily_topic_suggestions():
    """Lấy dữ liệu Notion và sinh 4 gợi ý chủ đề ngày mới."""
    raw_notes = fetch_recent_notion_notes()
    suggestions = ai_engine.generate_topic_suggestions_from_notion(raw_notes)
    return suggestions
