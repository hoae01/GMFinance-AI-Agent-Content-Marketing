# -*- coding: utf-8 -*-
"""
Cấu hình tập trung cho Telegram Bot AI Agent GMFinance.
Đọc các biến môi trường từ file .env ở thư mục gốc.
"""

import os
import sys

# Thư mục gốc dự án
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

def load_env():
    """Tải các biến môi trường từ file .env."""
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip())

load_env()

# 1. Telegram Bot Credentials
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_ALLOWED_USER_ID = os.environ.get("TELEGRAM_ALLOWED_USER_ID", "").strip()

# 2. AI Engine (Gemini & OpenAI)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "").strip()

# 3. Notion Integration
NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "2d946051-a014-8031-b54f-c5d2d82fa52b").strip()

# 4. Facebook Fanpages
FB_PAGE_1_ID = os.environ.get("FB_PAGE_1_ID", "").strip()
FB_PAGE_1_TOKEN = os.environ.get("FB_PAGE_1_TOKEN", "").strip()
FB_PAGE_2_ID = os.environ.get("FB_PAGE_2_ID", "").strip()
FB_PAGE_2_TOKEN = os.environ.get("FB_PAGE_2_TOKEN", "").strip()

# 5. Đường dẫn thư mục quan trọng
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "knowledge_base")
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
OUTPUT_ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

# Đảm bảo các thư mục đầu ra tồn tại
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_ASSETS_DIR, exist_ok=True)

def is_user_allowed(user_id) -> bool:
    """Kiểm tra quyền của người dùng Telegram gửi tin nhắn."""
    if not TELEGRAM_ALLOWED_USER_ID:
        # Nếu chưa set ID cụ thể thì cho phép (hoặc cảnh báo trong log)
        return True
    allowed_ids = [uid.strip() for uid in TELEGRAM_ALLOWED_USER_ID.split(",") if uid.strip()]
    return str(user_id) in allowed_ids
