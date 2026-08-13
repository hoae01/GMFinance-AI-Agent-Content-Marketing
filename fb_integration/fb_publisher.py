#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Tích hợp Facebook Graph API (Meta for Developers v19.0+)
Chức năng: Upload Slide Cards, Tạo Bài Viết Bản Nháp (Draft) & Lên Lịch Đăng (Scheduled Post)
cho 2 Fanpage thương hiệu:
1. GMFinance - Đào Tạo & Coaching ACCA (financegm)
2. Giải Pháp Tài Chính & Kế Toán Việt Nam (giaiphaptaichinhvaketoanVietnam)
"""

import sys
import os
import json
import time
import argparse
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def load_env():
    """Tự động đọc file .env ở thư mục gốc dự án."""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(root_dir, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip())

load_env()

GRAPH_API_VERSION = "v19.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"

# Cấu hình 2 Fanpage từ .env
FANPAGES = {
    "1": {
        "name": "GMFinance - Đào Tạo & Coaching ACCA",
        "url": "https://www.facebook.com/financegm/",
        "id": os.environ.get("FB_PAGE_1_ID", ""),
        "token": os.environ.get("FB_PAGE_1_TOKEN", "")
    },
    "2": {
        "name": "Giải Pháp Tài Chính & Kế Toán Việt Nam",
        "url": "https://www.facebook.com/giaiphaptaichinhvaketoanVietnam/",
        "id": os.environ.get("FB_PAGE_2_ID", ""),
        "token": os.environ.get("FB_PAGE_2_TOKEN", "")
    }
}

def post_multipart(url, fields, files):
    """
    Gửi HTTP POST request với dạng multipart/form-data bằng thư viện chuẩn urllib.
    """
    boundary = "----WebKitFormBoundaryGMFinance" + str(int(time.time()))
    body = []

    # Bổ sung text fields
    for k, v in fields.items():
        body.append(f"--{boundary}".encode("utf-8"))
        body.append(f'Content-Disposition: form-data; name="{k}"'.encode("utf-8"))
        body.append(b"")
        body.append(str(v).encode("utf-8"))

    # Bổ sung binary files
    for field_name, filename, file_data in files:
        body.append(f"--{boundary}".encode("utf-8"))
        body.append(f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"'.encode("utf-8"))
        body.append(b"Content-Type: image/png")
        body.append(b"")
        body.append(file_data)

    body.append(f"--{boundary}--".encode("utf-8"))
    body.append(b"")

    payload = b"\r\n".join(body)

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        try:
            err_json = json.loads(err_body)
            err_msg = err_json.get("error", {}).get("message", err_body)
        except Exception:
            err_msg = err_body
        raise Exception(f"Graph API Error ({e.code}): {err_msg}")
    except Exception as e:
        raise Exception(f"Network Error: {str(e)}")

def upload_photo_unpublished(page_id, token, image_path):
    """Tải 1 file ảnh lên Fanpage ở chế độ ẩn (published=false) để lấy Photo ID."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Không tìm thấy file ảnh: {image_path}")

    with open(image_path, "rb") as f:
        file_bytes = f.read()

    url = f"{GRAPH_API_BASE}/{page_id}/photos"
    fields = {
        "access_token": token,
        "published": "false"
    }
    files = [("source", os.path.basename(image_path), file_bytes)]

    res = post_multipart(url, fields, files)
    return res.get("id")

def publish_or_schedule_post(page_key, message, image_paths=None, is_draft=True, schedule_time_str=None):
    """
    Đăng bài / Tạo bản nháp (Draft) / Lên lịch (Schedule) bài viết cho Fanpage.
    - is_draft = True -> Tạo bản nháp (Draft)
    - schedule_time_str = "YYYY-MM-DD HH:MM" -> Lên lịch đăng bài
    """
    page_info = FANPAGES.get(str(page_key))
    if not page_info:
        return {"success": False, "error": f"Mã Fanpage không hợp lệ: {page_key}"}

    page_id = page_info["id"]
    token = page_info["token"]
    page_name = page_info["name"]

    if not page_id or not token:
        return {
            "success": False,
            "error": f"Chưa cấu hình FB_PAGE_{page_key}_ID hoặc FB_PAGE_{page_key}_TOKEN trong file .env cho {page_name}.\nVui lòng xem hướng dẫn tại fb_integration/HUONG_DAN_FACEBOOK_API.md"
        }

    photo_ids = []
    if image_paths:
        print(f"📸 Đang tải {len(image_paths)} ảnh Slide Card lên {page_name}...")
        for idx, img_p in enumerate(image_paths, 1):
            try:
                pid = upload_photo_unpublished(page_id, token, img_p)
                photo_ids.append(pid)
                print(f"   [✓] Ảnh {idx}/{len(image_paths)}: Photo ID = {pid}")
            except Exception as e:
                print(f"   [✗] Lỗi upload ảnh {img_p}: {e}")

    url = f"{GRAPH_API_BASE}/{page_id}/feed"
    fields = {
        "access_token": token,
        "message": message
    }

    if photo_ids:
        attached_media = [{"media_fbid": pid} for pid in photo_ids]
        fields["attached_media"] = json.dumps(attached_media)

    # Cấu hình chế độ Nháp / Lên lịch
    if schedule_time_str:
        # Lên lịch đăng bài (Scheduled Post)
        try:
            dt = datetime.strptime(schedule_time_str, "%Y-%m-%d %H:%M")
            unix_ts = int(dt.timestamp())
            now_ts = int(time.time())

            # Quy tắc Facebook: thời gian lên lịch phải từ +10 phút đến +75 ngày
            if unix_ts < now_ts + 600:
                dt = datetime.now() + timedelta(minutes=15)
                unix_ts = int(dt.timestamp())
                print("   [!] Thời gian hẹn giờ quá sớm. Đã tự động điều chỉnh thành +15 phút kể từ hiện tại.")

            fields["published"] = "false"
            fields["scheduled_publish_time"] = str(unix_ts)
            mode_desc = f"LÊN LỊCH ĐĂNG (Scheduled) lúc {dt.strftime('%d/%m/%Y %H:%M')}"
        except ValueError:
            return {"success": False, "error": f"Định dạng thời gian không hợp lệ (Cần 'YYYY-MM-DD HH:MM'): {schedule_time_str}"}
    elif is_draft:
        fields["published"] = "false"
        mode_desc = "TẠO BẢN NHÁP (Draft)"
    else:
        fields["published"] = "true"
        mode_desc = "ĐĂNG BÀI NGAY (Publish Now)"

    print(f"🚀 Đang gửi bài viết ({mode_desc}) lên {page_name}...")
    try:
        res = post_multipart(url, fields, [])
        post_id = res.get("id")
        print(f"✅ Thành công! Post ID: {post_id}")
        return {
            "success": True,
            "page_name": page_name,
            "post_id": post_id,
            "mode": mode_desc,
            "url": page_info["url"]
        }
    except Exception as e:
        print(f"❌ Thất bại: {e}")
        return {"success": False, "error": str(e), "page_name": page_name}

def delete_post(post_id, page_key="1"):
    """Xóa 1 bài viết hoặc bài nháp/lên lịch bằng Post ID qua Facebook Graph API."""
    page_info = FANPAGES.get(str(page_key))
    token = page_info["token"] if page_info else ""
    if not token:
        # Thử dùng token của Fanpage 1 hoặc 2
        token = FANPAGES["1"]["token"] or FANPAGES["2"]["token"]

    url = f"{GRAPH_API_BASE}/{post_id}?access_token={token}"
    req = urllib.request.Request(url, method="DELETE")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("success"):
                print(f"🗑️ Đã xóa thành công bài viết (Post ID: {post_id}) trên Facebook!")
                return True
            else:
                print(f"⚠️ Kết quả xóa bài viết {post_id}: {data}")
                return False
    except Exception as e:
        print(f"❌ Lỗi xóa bài viết {post_id}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Tool Đăng/Lên lịch bài viết Facebook Fanpage GMFinance")
    parser.add_argument("--page", choices=["1", "2", "all"], default="all", help="Chọn Fanpage (1: GMFinance, 2: Giải Pháp Tài Chính, all: Cả 2)")
    parser.add_argument("--message", type=str, help="Nội dung bài viết")
    parser.add_argument("--message-file", type=str, help="Path tới file chứa nội dung bài viết")
    parser.add_argument("--images", nargs="*", help="Danh sách các đường dẫn file ảnh")
    parser.add_argument("--draft", action="store_true", default=True, help="Tạo bản nháp (Draft - mặc định)")
    parser.add_argument("--publish-now", action="store_true", help="Đăng trực tiếp ngay lập tức")
    parser.add_argument("--schedule", type=str, help="Lên lịch đăng bài dạng 'YYYY-MM-DD HH:MM'")
    parser.add_argument("--delete", type=str, help="Xóa bài viết/bản nháp/bài lên lịch bằng Post ID")
    parser.add_argument("--test", action="store_true", help="Kiểm tra cấu hình API và kết nối Token")

    args = parser.parse_args()

    if args.delete:
        print(f"🗑️ Đang gửi yêu cầu xóa Post ID: {args.delete}...")
        delete_post(args.delete, page_key=args.page)
        return

    if args.test:
        print("🔍 Đang kiểm tra cấu hình Facebook API trong file .env...")
        for key in ["1", "2"]:
            p = FANPAGES[key]
            print(f"\n--- Fanpage {key}: {p['name']} ---")
            print(f"URL: {p['url']}")
            print(f"Page ID: {p['id'] if p['id'] else '[Chưa cấu hình FB_PAGE_' + key + '_ID]'}")
            print(f"Access Token: {'[Đã cấu hình ' + str(len(p['token'])) + ' ký tự]' if p['token'] else '[Chưa cấu hình FB_PAGE_' + key + '_TOKEN]'}")
        return

    # Xác định nội dung bài viết
    message = args.message or ""
    if not message and args.message_file and os.path.exists(args.message_file):
        with open(args.message_file, "r", encoding="utf-8") as f:
            message = f.read()

    if not message:
        print("⚠️ Vui lòng cung cấp nội dung bài viết qua --message hoặc --message-file.")
        print("Ví dụ kiểm tra cấu hình:")
        print("python fb_integration/fb_publisher.py --test")
        return

    pages_to_run = ["1", "2"] if args.page == "all" else [args.page]
    is_draft = not args.publish_now and not args.schedule

    results = []
    for p_key in pages_to_run:
        res = publish_or_schedule_post(
            page_key=p_key,
            message=message,
            image_paths=args.images,
            is_draft=is_draft,
            schedule_time_str=args.schedule
        )
        results.append(res)

    print("\n--- BÁO CÁO KẾT QUẢ ---")
    for r in results:
        if r.get("success"):
            print(f"🟢 [{r['page_name']}]: {r['mode']} thành công! ID = {r['post_id']}")
        else:
            print(f"🔴 [{r.get('page_name', 'Fanpage')}]: Lỗi - {r.get('error')}")

if __name__ == "__main__":
    main()

