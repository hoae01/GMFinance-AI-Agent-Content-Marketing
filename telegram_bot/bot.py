#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main Entry Point cho GMFinance Telegram Bot AI Agent.
Hỗ trợ Long Polling 24/7, Tự động kết nối lại khi mất mạng và ghi log chuẩn mực.
"""

import os
import sys
import time
import telebot

# Đảm bảo mã hóa UTF-8 trên Windows Console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Thêm thư mục gốc vào sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from telegram_bot import config, handlers

def print_banner():
    print("=" * 65)
    print(" 👑 GMFINANCE AI AGENT - TELEGRAM BOT SERVICE ")
    print(" 'ELEVATE EXPERTISE, EXPAND CAREER HORIZONS' ")
    print("=" * 65)
    
    # Kiểm tra trạng thái AI Engine
    if config.GEMINI_API_KEY:
        print(" [✓] AI Engine       : Google Gemini 2.5/Flash (Sẵn sàng)")
    elif config.OPENAI_API_KEY:
        print(" [✓] AI Engine       : OpenAI GPT-4o-mini (Sẵn sàng)")
    else:
        print(" [!] AI Engine       : Chế độ Fallback Mock (Chưa điền GEMINI_API_KEY)")

    # Kiểm tra trạng thái Fanpage
    fp1_status = "Đã kết nối" if config.FB_PAGE_1_ID and config.FB_PAGE_1_TOKEN else "Chưa có Token"
    fp2_status = "Đã kết nối" if config.FB_PAGE_2_ID and config.FB_PAGE_2_TOKEN else "Chưa có Token"
    print(f" [✓] Fanpage 1 (GM)  : {fp1_status}")
    print(f" [✓] Fanpage 2 (GP)  : {fp2_status}")
    
    # Kiểm tra Notion
    notion_status = "Đã kết nối" if config.NOTION_TOKEN else "Chế độ mẫu (Chưa có NOTION_TOKEN)"
    print(f" [✓] Notion Vault    : {notion_status}")
    
    # Kiểm tra User ID
    if config.TELEGRAM_ALLOWED_USER_ID:
        print(f" [✓] Quyền Admin     : User ID {config.TELEGRAM_ALLOWED_USER_ID}")
    else:
        print(" [!] Quyền Admin     : Chưa giới hạn User ID (Tất cả tin nhắn hợp lệ)")
    print("=" * 65)


import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"GMFinance Telegram Bot is LIVE and Running 24/7!")

    def log_message(self, format, *args):
        pass  # Không in log truy cập rác

def run_health_server():
    """Chạy web server siêu nhẹ để đáp ứng yêu cầu Health Check của Render Web Service (Gói Miễn Phí $0)."""
    port = int(os.environ.get("PORT", 10000))
    try:
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        server.serve_forever()
    except Exception as e:
        print(f"[WARN] Health server note: {e}")

def start_bot():
    token = config.TELEGRAM_BOT_TOKEN
    if not token or token == "your_telegram_bot_token_here":
        print("\n❌ LỖI: Chưa cấu hình TELEGRAM_BOT_TOKEN trong file .env!")
        print("👉 Vui lòng xem hướng dẫn tại: telegram_bot/HUONG_DAN_TELEGRAM_BOT.md")
        print("   1. Mở Telegram, chat với @BotFather để tạo Bot và lấy Token.")
        print("   2. Mở file .env và điền: TELEGRAM_BOT_TOKEN=xxxx:yyyy")
        print("   3. Chạy lại script này.\n")
        return

    print_banner()

    # Khởi động Healthcheck Web Server ngầm cho Render Free Web Service
    t = threading.Thread(target=run_health_server, daemon=True)
    t.start()

    bot = telebot.TeleBot(token, parse_mode=None)
    
    # Đăng ký các router xử lý
    handlers.register_handlers(bot)
    
    # Lấy thông tin Bot từ Telegram API
    try:
        bot_info = bot.get_me()
        print(f"\n🚀 Bot đang hoạt động với tên: @{bot_info.username} ({bot_info.first_name})")
        print("📱 Bạn có thể mở Telegram trên điện thoại/PC và nhắn tin cho Bot ngay bây giờ!")
        print("💡 Nhấn Ctrl + C để dừng Bot.\n")
    except Exception as e:
        print(f"❌ Không thể kết nối tới Telegram API: {e}")
        print("Vui lòng kiểm tra lại TELEGRAM_BOT_TOKEN trong file .env và kết nối mạng.")
        return

    # Chạy vòng lặp lắng nghe tin nhắn (Infinity Polling)
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except Exception as e:
            print(f"[!] Mất kết nối hoặc gặp sự cố: {e}. Đang tự động kết nối lại sau 5 giây...")
            time.sleep(5)


if __name__ == "__main__":
    start_bot()
