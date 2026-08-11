#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động quét, ghi lại nhật ký thời gian tạo các Asset / Output
và dọn dẹp (xóa) các file Asset/Output cũ đã tạo hơn 7 ngày trước đó để bảo toàn dung lượng bộ nhớ.
"""

import os
import sys
import time
import datetime

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(PROJECT_DIR, "Output")
ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")
LOGS_DIR = os.path.join(PROJECT_DIR, "logs")

# Giới hạn tự động dọn dẹp: 7 ngày (7 * 24 * 3600 giây)
RETENTION_DAYS = 7
MAX_AGE_SECONDS = RETENTION_DAYS * 24 * 60 * 60


def clean_old_files(target_dir, is_assets=False):
    if not os.path.exists(target_dir):
        return [], []

    now = time.time()
    kept_files = []
    deleted_files = []

    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            # Bỏ qua file logo gốc để không xóa nhầm logo thương hiệu
            if "official_logo" in filename.lower() or "gmfinance_logo" in filename.lower():
                continue

            filepath = os.path.join(root, filename)
            try:
                file_mtime = os.path.getmtime(filepath)
                age_seconds = now - file_mtime
                age_days = age_seconds / (24 * 3600)
                created_date = datetime.datetime.fromtimestamp(file_mtime).strftime("%Y-%m-%d %H:%M")

                if age_seconds > MAX_AGE_SECONDS:
                    os.remove(filepath)
                    deleted_files.append((filename, created_date, round(age_days, 1)))
                else:
                    kept_files.append((filename, created_date, round(age_days, 1)))
            except Exception as e:
                print(f"[WARN] Lỗi khi xử lý {filepath}: {e}")

    return kept_files, deleted_files


def run_maintenance_log():
    os.makedirs(LOGS_DIR, exist_ok=True)
    log_file_path = os.path.join(LOGS_DIR, "storage_maintenance.log")

    print("=== AGENT 2: KIỂM TRA BỘ NHỚ & DỌN DẸP ASSETS CŨ (> 7 NGÀY) ===")
    
    kept_out, deleted_out = clean_old_files(OUTPUT_DIR)
    kept_asset, deleted_asset = clean_old_files(ASSETS_DIR, is_assets=True)

    total_deleted = len(deleted_out) + len(deleted_asset)
    timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp_str}] Quét dọn dẹp bộ nhớ (Giới hạn: {RETENTION_DAYS} ngày):\n"
    log_entry += f"• Tổng số file cũ >7 ngày đã xóa: {total_deleted}\n"
    
    if deleted_out or deleted_asset:
        log_entry += "  - Danh sách file đã xóa:\n"
        for name, dt, age in deleted_out + deleted_asset:
            log_entry += f"    ❌ {name} (Tạo ngày: {dt}, tuổi thọ: {age} ngày)\n"
    else:
        log_entry += "  - Không có file nào cũ quá 7 ngày cần xóa.\n"

    log_entry += f"• Số file Asset/Output đang bảo tồn: {len(kept_out) + len(kept_asset)} files.\n"
    log_entry += "-" * 60 + "\n"

    print(log_entry)

    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"[SUCCESS] Đã ghi nhật ký quản lý dung lượng tại: {log_file_path}")
    return total_deleted, len(kept_out) + len(kept_asset)


if __name__ == "__main__":
    run_maintenance_log()
