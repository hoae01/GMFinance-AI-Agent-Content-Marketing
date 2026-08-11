#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script tìm kiếm tất cả Database trên Notion Workspace mà Integration có quyền truy cập."""

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

def search_databases():
    url = "https://api.notion.com/v1/search"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "filter": {"value": "database", "property": "object"}
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            results = data.get("results", [])
            print(f"[SUCCESS] Tìm thấy {len(results)} Database(s) trên Notion Workspace!\n")
            for idx, db in enumerate(results, 1):
                db_id = db.get("id", "N/A")
                title_parts = db.get("title", [])
                title = "".join([t.get("plain_text", "") for t in title_parts]) if title_parts else "(Không có tiêu đề)"
                props = list(db.get("properties", {}).keys())
                print(f"[{idx}] Database: {title}")
                print(f"    ID: {db_id}")
                print(f"    Các cột (Properties): {', '.join(props[:10])}")
                print()
            return results
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else ""
        print(f"[ERROR] Lỗi kết nối Notion API ({e.code}): {e.reason}")
        print(f"    Chi tiết: {body[:300]}")
        return []
    except Exception as e:
        print(f"[ERROR] Lỗi không xác định: {str(e)}")
        return []

if __name__ == "__main__":
    print("=== TÌM KIẾM NOTION DATABASES ===\n")
    search_databases()
