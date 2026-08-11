#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kết nối Notion REST API để lấy dữ liệu ghi chú/ý tưởng từ Notion Database.
Sử dụng thư viện chuẩn của Python (urllib.request, json, os), không cần cài đặt thêm package ngoài.
"""

import os
import sys
import json
import urllib.request
import urllib.error

# Khắc phục lỗi mã hóa UTF-8 trên Windows Terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Thông tin mặc định hoặc đọc từ file .env / biến môi trường
NOTION_TOKEN = os.getenv("NOTION_TOKEN", "")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID", "")

# Mock data dự phòng nếu chưa kết nối API Notion thật
MOCK_NOTION_IDEAS = [
    {
        "id": "mock-1",
        "title": "Bí quyết áp dụng mô hình Time-Blocking để x2 năng suất làm việc",
        "category": "Năng suất & QLNST",
        "status": "Sẵn sàng viết",
        "notes": "Đừng chia nhỏ thời gian quá nhiều. Hãy phân 3 khối lớn: Sáng 2 tiếng làm việc sâu (Deep work), Chiều xử lý họp hành, Tối học hỏi. Kết quả: Làm xong việc quan trọng nhất trước 11h sáng."
    },
    {
        "id": "mock-2",
        "title": "5 sai lầm phổ biến khi dùng Prompt AI khiến kết quả luôn vô hồn",
        "category": "AI & Công nghệ",
        "status": "Sẵn sàng viết",
        "notes": "1. Không giao vai trò (Role)\n2. Ra lệnh quá chung chung\n3. Không đưa bối cảnh sản phẩm\n4. Không quy định những từ cấm dùng\n5. Bỏ qua bước yêu cầu AI đóng vai người kiểm duyệt."
    },
    {
        "id": "mock-3",
        "title": "Tại sao làm việc chăm chỉ không giúp bạn giàu lên mà cần tư duy leverage",
        "category": "Tư duy & Sự nghiệp",
        "status": "Sẵn sàng viết",
        "notes": "Lao động chân tay/thời gian có giới hạn 24h. Muốn bứt phá phải có đòn bẩy: Đòn bẩy công nghệ (AI/Automation), Đòn bẩy nội dung (Bài viết/Media), Đòn bẩy vốn và Đòn bẩy con người."
    },
    {
        "id": "mock-4",
        "title": "Cách thiết lập hệ thống ghi chú Second Brain bằng Notion trong 15 phút",
        "category": "Hệ thống & Notion",
        "status": "Sẵn sàng viết",
        "notes": "Phương pháp CODE: Capture (Ghi chép), Organize (Phân loại theo CODE/PARA), Distill (Tóm tắt ý chính), Express (Tạo ra sản phẩm/bài viết). Đừng chỉ lưu trữ mà hãy biến thành bài viết."
    },
    {
        "id": "mock-5",
        "title": "Bài học xương máu từ dự án thất bại đầu tiên khi làm Freelancer/Solopreneur",
        "category": "Trải nghiệm cá nhân",
        "status": "Sẵn sàng viết",
        "notes": "Quá tập trung làm sản phẩm hoàn hảo mà quên mất bước Validate thị trường. Bài học: Bán trước - Làm sau (Pre-sell). Nhận phản hồi thật của khách hàng trước khi tốn 3 tháng xây dựng."
    }
]


def parse_page_properties(page):
    """Phân tích các thuộc tính của một trang Notion."""
    props = page.get("properties", {})
    
    # Lấy Tiêu đề (Title)
    title = "Không có tiêu đề"
    for prop_name, prop_val in props.items():
        if prop_val.get("type") == "title":
            title_parts = prop_val.get("title", [])
            if title_parts:
                title = "".join([t.get("plain_text", "") for t in title_parts])
            break
            
    # Lấy Category
    category = "Tổng hợp"
    for prop_name, prop_val in props.items():
        p_type = prop_val.get("type")
        if p_type == "select" and prop_val.get("select"):
            category = prop_val["select"].get("name", category)
        elif p_type == "multi_select" and prop_val.get("multi_select"):
            category = ", ".join([s.get("name", "") for s in prop_val["multi_select"]])
            
    # Lấy Status
    status = "Nháp"
    for prop_name, prop_val in props.items():
        p_type = prop_val.get("type")
        if p_type == "status" and prop_val.get("status"):
            status = prop_val["status"].get("name", status)
        elif p_type == "select" and prop_name.lower() in ["status", "trạng thái"]:
            if prop_val.get("select"):
                status = prop_val["select"].get("name", status)

    # Lấy Notes/Rich Text
    notes = ""
    for prop_name, prop_val in props.items():
        if prop_name.lower() in ["notes", "nội dung", "ghi chú", "description", "content"]:
            if prop_val.get("type") == "rich_text":
                text_parts = prop_val.get("rich_text", [])
                notes = "".join([t.get("plain_text", "") for t in text_parts])
            break
            
    return {
        "id": page.get("id"),
        "title": title,
        "category": category,
        "status": status,
        "notes": notes or "Nội dung ghi chú trong trang Notion."
    }


def fetch_notion_database(token=None, db_id=None):
    """Gửi HTTP POST request đến Notion REST API để lấy dữ liệu."""
    api_token = token or NOTION_TOKEN
    database_id = db_id or NOTION_DATABASE_ID

    if not api_token or not database_id:
        print("[INFO] Chưa cấu hình NOTION_TOKEN hoặc NOTION_DATABASE_ID. Đang sử dụng dữ liệu mẫu (Mock Data).")
        return MOCK_NOTION_IDEAS

    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(url, data=json.dumps({}).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            data = json.loads(res_body)
            results = data.get("results", [])
            ideas = [parse_page_properties(page) for page in results]
            print(f"[SUCCESS] Lấy thành công {len(ideas)} ý tưởng từ Notion Database.")
            return ideas
    except urllib.error.HTTPError as e:
        print(f"[ERROR] Lỗi kết nối Notion API ({e.code}): {e.reason}")
        print("[INFO] Chuyển sang dùng dữ liệu mẫu (Mock Data).")
        return MOCK_NOTION_IDEAS
    except Exception as e:
        print(f"[ERROR] Lỗi không xác định: {str(e)}")
        print("[INFO] Chuyển sang dùng dữ liệu mẫu (Mock Data).")
        return MOCK_NOTION_IDEAS


if __name__ == "__main__":
    print("=== DỤNG CỤ LẤY DỮ LIỆU NOTION DATABASE ===")
    ideas = fetch_notion_database()
    for idx, idea in enumerate(ideas, 1):
        print(f"\n[{idx}] {idea['title']} | Thể loại: {idea['category']}")
        print(f"    Ghi chú: {idea['notes'][:100]}...")
