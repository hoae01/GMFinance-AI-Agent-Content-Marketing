#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script xem bài viết gần đây nhất từ Knowledge Vault Notion Database."""

import sys
import os
import json
import urllib.request
import urllib.error

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def load_env():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip())

load_env()
NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "2d946051-a014-8031-b54f-c5d2d82fa52b")

def get_page_blocks(page_id):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28"
    }
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            blocks = data.get("results", [])
            text_content = []
            for b in blocks:
                b_type = b.get("type")
                if b_type in b:
                    text_parts = b[b_type].get("rich_text", [])
                    plain_text = "".join([t.get("plain_text", "") for t in text_parts])
                    if plain_text:
                        if b_type.startswith("heading"):
                            text_content.append(f"\n### {plain_text}")
                        elif b_type == "bulleted_list_item":
                            text_content.append(f"• {plain_text}")
                        elif b_type == "numbered_list_item":
                            text_content.append(f"1. {plain_text}")
                        elif b_type == "to_do":
                            checked = "[x]" if b[b_type].get("checked") else "[ ]"
                            text_content.append(f"{checked} {plain_text}")
                        elif b_type == "quote":
                            text_content.append(f"> {plain_text}")
                        else:
                            text_content.append(plain_text)
            return "\n".join(text_content)
    except Exception as e:
        return f"(Không thể lấy nội dung chi tiết: {str(e)})"

def query_recent_entry():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "page_size": 3,
        "sorts": [
            {
                "timestamp": "created_time",
                "direction": "descending"
            }
        ]
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            results = data.get("results", [])
            print(f"=== ĐÃ KẾT NỐI THÀNH CÔNG VÀO KNOWLEDGE VAULT ===")
            print(f"Tổng số bài gần đây: {len(results)}\n")
            
            for idx, page in enumerate(results, 1):
                page_id = page.get("id")
                props = page.get("properties", {})
                created_time = page.get("created_time", "")[:10]
                
                title = "(Không tiêu đề)"
                for p_name, p_val in props.items():
                    if p_val.get("type") == "title":
                        t_parts = p_val.get("title", [])
                        if t_parts:
                            title = "".join([t.get("plain_text", "") for t in t_parts])
                        break
                
                core_topic = "N/A"
                for p_name, p_val in props.items():
                    if p_name.lower() == "core topic":
                        if p_val.get("type") == "select" and p_val.get("select"):
                            core_topic = p_val["select"].get("name")
                        elif p_val.get("type") == "multi_select" and p_val.get("multi_select"):
                            core_topic = ", ".join([s.get("name") for s in p_val["multi_select"]])
                        elif p_val.get("type") == "rich_text" and p_val.get("rich_text"):
                            core_topic = "".join([t.get("plain_text") for t in p_val["rich_text"]])
                
                content = get_page_blocks(page_id)
                
                print(f"📌 [BÀI VIẾT NỔI BẬT #{idx}]")
                print(f"• Tiêu đề: {title}")
                print(f"• Ngày đăng/tạo: {created_time}")
                print(f"• Core Topic: {core_topic}")
                print(f"• Nội dung ghi chú thô:\n{content}\n")
                print("-" * 70 + "\n")
                
    except Exception as e:
        print(f"[ERROR] Lỗi: {str(e)}")

if __name__ == "__main__":
    query_recent_entry()
