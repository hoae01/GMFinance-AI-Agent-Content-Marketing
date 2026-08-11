#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script nạp trọn bộ 3 file ảnh Slide Card vào Bộ nhớ tạm (Windows Clipboard)."""

import os
import sys
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Output", "assets")
s1 = os.path.join(OUTPUT_ASSETS_DIR, "slide_01.png")
s2 = os.path.join(OUTPUT_ASSETS_DIR, "slide_02.png")
s3 = os.path.join(OUTPUT_ASSETS_DIR, "slide_03.png")

def copy_all_3_slides_to_clipboard():
    ps_cmd = f"Set-Clipboard -Path '{s1}', '{s2}', '{s3}'"
    try:
        subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        print("========================================================")
        print("  [SUCCESS] ĐÃ COPY CẢ 3 ẢNH SLIDE VÀO WINDOWS CLIPBOARD!")
        print("========================================================")
        print("👉 Bây giờ bạn chỉ cần mở Facebook và bấm Ctrl + V.")
        print("👉 Facebook sẽ TỰ ĐỘNG UPLOAD CẢ 3 ẢNH CÙNG MỘT LÚC!\n")
    except Exception as e:
        print(f"[ERROR] Không thể nạp ảnh vào Clipboard: {e}")

if __name__ == "__main__":
    copy_all_3_slides_to_clipboard()
