# -*- coding: utf-8 -*-
"""
Bộ xử lý tin nhắn, câu lệnh và nút bấm Inline tương tác cho GMFinance Telegram Bot.
"""

import os
import sys
import telebot
from telebot import types
from datetime import datetime

from telegram_bot import config, ai_engine, notion_reader, fb_workflow, video_workflow

# Lưu bộ nhớ đệm bài viết gần nhất của từng user: {user_id: fb_package}
USER_LAST_FB_POST = {}
USER_CACHED_SUGGESTIONS = {}

def register_handlers(bot: telebot.TeleBot):
    """Đăng ký toàn bộ router lệnh và sự kiện cho Telegram Bot."""

    # 1. Bộ lọc kiểm tra bảo mật (User whitelist)
    def check_auth(message_or_call) -> bool:
        user_id = message_or_call.from_user.id
        if not config.is_user_allowed(user_id):
            if hasattr(message_or_call, "chat"):
                bot.reply_to(
                    message_or_call,
                    f"⛔ Bạn không có quyền truy cập Bot này.\n"
                    f"User ID của bạn: `{user_id}`.\n"
                    f"Vui lòng thêm User ID này vào biến `TELEGRAM_ALLOWED_USER_ID` trong file `.env`.",
                    parse_mode="Markdown"
                )
            return False
        return True

    # 2. Lệnh /start và /help
    @bot.message_handler(commands=["start", "help"])
    def handle_start(message):
        if not check_auth(message):
            return
        
        user_name = message.from_user.first_name or "bạn"
        welcome_text = (
            f"👑 **Chào mừng {user_name} đến với GMFinance AI Agent!**\n"
            f"Slogan: _'ELEVATE EXPERTISE, EXPAND CAREER HORIZONS'_\n\n"
            f"Hệ thống hỗ trợ 3 quy trình tự động hóa mạnh mẽ:\n\n"
            f"🔍 **1. Đọc Notion & Đề xuất chủ đề**\n"
            f"• Gõ `/notion` để quét Knowledge Vault và nhận 4 gợi ý bài viết chọn nhanh.\n\n"
            f"📝 **2. Soạn bài Facebook & Tạo Slide Cards**\n"
            f"• Gõ `/fb <chủ đề>` hoặc chat tự do: _'Viết bài FB về Ma trận Eisenhower'_\n"
            f"• Bot tự viết bài chuẩn GMFinance + Sinh 3 Slide Card (1080x1080px) + Phím Lưu nháp/Lên lịch Fanpage.\n\n"
            f"🎬 **3. Phỏng vấn lên Kịch bản Video ngắn (TikTok/Reels)**\n"
            f"• Gõ `/video <chủ đề>`: Bot sẽ đóng vai Đạo diễn phỏng vấn bạn 3 câu hỏi ngắn và tự ráp thành kịch bản hoàn chỉnh.\n\n"
            f"⚙️ **Lệnh khác**: `/status` (Xem kết nối API), `/cancel` (Hủy phỏng vấn)"
        )
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_notion = types.InlineKeyboardButton("🔍 Đọc Notion & Gợi Ý", callback_data="cmd_notion")
        btn_status = types.InlineKeyboardButton("📊 Kiểm Tra Kết Nối", callback_data="cmd_status")
        markup.add(btn_notion, btn_status)
        
        bot.reply_to(message, welcome_text, parse_mode="Markdown", reply_markup=markup)

    # 3. Lệnh /status
    @bot.message_handler(commands=["status"])
    def handle_status(message):
        if not check_auth(message):
            return
        
        fp1_ok = "✅ Đã kết nối" if config.FB_PAGE_1_ID and config.FB_PAGE_1_TOKEN else "⚠️ Chưa cấu hình Token"
        fp2_ok = "✅ Đã kết nối" if config.FB_PAGE_2_ID and config.FB_PAGE_2_TOKEN else "⚠️ Chưa cấu hình Token"
        notion_ok = "✅ Đã kết nối" if config.NOTION_TOKEN else "⚠️ Dùng chế độ mẫu (Chưa điền Token)"
        
        ai_engine_name = "Chưa có Key (Mock Mode)"
        if config.GEMINI_API_KEY:
            ai_engine_name = "⚡ Google Gemini Flash (Miễn phí & Cực nhanh)"
        elif config.OPENAI_API_KEY:
            ai_engine_name = "🧠 OpenAI GPT-4o-mini"

        status_text = (
            f"📊 **TRẠNG THÁI HỆ THỐNG GMFINANCE AI AGENT**\n\n"
            f"🤖 **AI Engine**: {ai_engine_name}\n"
            f"📓 **Notion Vault**: {notion_ok}\n"
            f"🏢 **Fanpage 1 (GMFinance)**: {fp1_ok}\n"
            f"🏢 **Fanpage 2 (Giải Pháp Tài Chính)**: {fp2_ok}\n"
            f"👤 **Telegram User ID của bạn**: `{message.from_user.id}`\n"
        )
        bot.reply_to(message, status_text, parse_mode="Markdown")

    # 4. Lệnh /cancel
    @bot.message_handler(commands=["cancel"])
    def handle_cancel(message):
        if not check_auth(message):
            return
        video_workflow.cancel_session(message.from_user.id)
        bot.reply_to(message, "✅ Đã hủy phiên làm việc hiện tại. Bạn có thể bắt đầu yêu cầu mới bất kỳ lúc nào!")

    # 5. Lệnh /notion
    @bot.message_handler(commands=["notion"])
    def handle_notion(message):
        if not check_auth(message):
            return
        
        msg_waiting = bot.reply_to(message, "🔄 Đang kết nối Notion Knowledge Vault và chọn lọc 4 góc nhìn sắc bén...")
        suggestions = notion_reader.get_daily_topic_suggestions()
        USER_CACHED_SUGGESTIONS[message.from_user.id] = suggestions
        
        text_lines = ["🔍 **GỢI Ý 4 CHỦ ĐỀ NGÀY MỚI TỪ NOTION KNOWLEDGE VAULT:**\n"]
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons_fb = []
        buttons_vid = []
        
        for idx, item in enumerate(suggestions, 1):
            title = item.get("title", f"Chủ đề {idx}")
            angle = item.get("angle", "")
            summary = item.get("summary", "")
            text_lines.append(f"**{idx}. {title}**\n   • _Góc nhìn_: {angle}\n   • _Tóm tắt_: {summary}\n")
            
            buttons_fb.append(types.InlineKeyboardButton(f"📝 Viết bài FB #{idx}", callback_data=f"sel_fb_{idx}"))
            buttons_vid.append(types.InlineKeyboardButton(f"🎬 Kịch bản Video #{idx}", callback_data=f"sel_vid_{idx}"))

        text_lines.append("👉 Bấm nút bên dưới để tạo bài viết FB hoặc khởi động phỏng vấn video ngay!")
        
        # Thêm nút bấm
        for b_fb, b_vid in zip(buttons_fb, buttons_vid):
            markup.row(b_fb, b_vid)
        markup.row(types.InlineKeyboardButton("🔄 Quét lại Notion", callback_data="cmd_notion"))
        
        try:
            bot.delete_message(message.chat.id, msg_waiting.message_id)
        except Exception:
            pass
        bot.send_message(message.chat.id, "\n".join(text_lines), parse_mode="Markdown", reply_markup=markup)

    # 6. Lệnh /fb <chủ đề>
    @bot.message_handler(commands=["fb"])
    def handle_fb_command(message):
        if not check_auth(message):
            return
        topic = message.text.replace("/fb", "").strip()
        if not topic:
            bot.reply_to(message, "⚠️ Vui lòng nhập chủ đề bài viết. Ví dụ: `/fb Ma trận Eisenhower trong quản trị thời gian`", parse_mode="Markdown")
            return
        process_create_fb_post(bot, message.chat.id, message.from_user.id, topic)

    # 7. Lệnh /video <chủ đề>
    @bot.message_handler(commands=["video"])
    def handle_video_command(message):
        if not check_auth(message):
            return
        topic = message.text.replace("/video", "").strip()
        if not topic:
            bot.reply_to(message, "⚠️ Vui lòng nhập chủ đề video. Ví dụ: `/video Lộ trình học ACCA cho người bận rộn`", parse_mode="Markdown")
            return
        process_start_video_interview(bot, message.chat.id, message.from_user.id, topic)

    # 8. Xử lý tin nhắn văn bản tự do (Natural Chat & Interview Q&A)
    @bot.message_handler(func=lambda msg: True, content_types=["text"])
    def handle_free_text(message):
        if not check_auth(message):
            return
        
        user_id = message.from_user.id
        chat_id = message.chat.id
        text = message.text.strip()
        
        # Kiểm tra xem người dùng có đang trong phiên phỏng vấn Video không
        active_session = video_workflow.get_active_session(user_id)
        if active_session and not active_session.is_completed:
            # Ghi nhận câu trả lời
            next_question = active_session.submit_answer(text)
            
            if next_question:
                # Gửi câu hỏi tiếp theo
                step_num = active_session.step + 1
                total_steps = len(active_session.questions)
                msg_q = (
                    f"🎙️ **[CÂU HỎI {step_num}/{total_steps} - ĐẠO DIỄN GMFINANCE]**\n\n"
                    f"💬 *{next_question}*\n\n"
                    f"_(Bạn hãy gõ câu trả lời hoặc gửi voice note bên dưới)_"
                )
                bot.send_message(chat_id, msg_q, parse_mode="Markdown")
            else:
                # Đã trả lời xong cả 3 câu -> Ráp kịch bản hoàn chỉnh
                msg_waiting = bot.send_message(chat_id, "⏳ Đang tổng hợp các câu trả lời và đóng gói Kịch Bản Video hoàn chỉnh...")
                script_data = active_session.build_final_script()
                video_workflow.cancel_session(user_id)
                
                title = script_data.get("title", active_session.topic)
                hook_3s = script_data.get("hook_3s", "")
                caption = script_data.get("caption", "")
                hashtags = " ".join(script_data.get("hashtags", []))
                full_md = script_data.get("full_script_markdown", "")
                file_path = script_data.get("file_path", "")
                
                response_text = (
                    f"🎬 **KỊCH BẢN VIDEO HOÀN CHỈNH: {title}**\n\n"
                    f"⚡ **Hook 3s đầu**: _{hook_3s}_\n\n"
                    f"📝 **Caption đề xuất**: {caption}\n\n"
                    f"🏷️ **Hashtags**: {hashtags}\n\n"
                    f"📄 **Nội dung Storyboard chi tiết**:\n\n"
                    f"{full_md[:2000]}..."  # Cắt ngắn nếu dài quá giới hạn telegram
                )
                
                try:
                    bot.delete_message(chat_id, msg_waiting.message_id)
                except Exception:
                    pass
                
                bot.send_message(chat_id, response_text, parse_mode="Markdown")
                
                # Gửi kèm file Markdown kịch bản
                if file_path and os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        bot.send_document(chat_id, f, caption=f"📄 File kịch bản đầy đủ: {os.path.basename(file_path)}")
            return

        # Nếu không trong phiên phỏng vấn, phân tích ý định chat tự nhiên
        lower_text = text.lower()
        if lower_text in ["notion", "gợi ý", "hôm nay đăng gì", "đăng bài gì"]:
            handle_notion(message)
        elif lower_text.startswith("viết bài") or lower_text.startswith("bài viết") or lower_text.startswith("post fb"):
            topic = text.replace("viết bài", "").replace("bài viết", "").replace("post fb", "").strip()
            topic = topic.lstrip(":")
            if not topic:
                topic = "Quy tắc 80/20 trong quản trị tài chính"
            process_create_fb_post(bot, chat_id, user_id, topic)
        elif lower_text.startswith("video") or lower_text.startswith("kịch bản") or lower_text.startswith("tiktok"):
            topic = text.replace("video", "").replace("kịch bản", "").replace("tiktok", "").strip()
            topic = topic.lstrip(":")
            if not topic:
                topic = "Cách vượt qua kỳ thi ACCA dễ dàng"
            process_start_video_interview(bot, chat_id, user_id, topic)
        else:
            # Mặc định coi là chủ đề bài viết FB
            process_create_fb_post(bot, chat_id, user_id, text)

    # 9. Bộ xử lý Callback Queries từ nút bấm Inline
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback_query(call):
        if not check_auth(call):
            return
        
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        data = call.data
        
        bot.answer_callback_query(call.id)
        
        if data == "cmd_notion":
            handle_notion(call.message)
        elif data == "cmd_status":
            handle_status(call.message)
            
        elif data.startswith("sel_fb_"):
            idx = int(data.replace("sel_fb_", ""))
            suggestions = USER_CACHED_SUGGESTIONS.get(user_id, [])
            if 0 < idx <= len(suggestions):
                topic = suggestions[idx - 1].get("title", "")
                process_create_fb_post(bot, chat_id, user_id, topic)
                
        elif data.startswith("sel_vid_"):
            idx = int(data.replace("sel_vid_", ""))
            suggestions = USER_CACHED_SUGGESTIONS.get(user_id, [])
            if 0 < idx <= len(suggestions):
                topic = suggestions[idx - 1].get("title", "")
                process_start_video_interview(bot, chat_id, user_id, topic)

        # Xử lý các nút Publishing / Scheduling Facebook
        elif data.startswith("act_"):
            last_package = USER_LAST_FB_POST.get(user_id)
            if not last_package:
                bot.send_message(chat_id, "⚠️ Không tìm thấy bài viết gần đây để thực hiện thao tác. Vui lòng tạo bài mới!")
                return
            
            post_text = last_package.get("post_text", "")
            image_paths = last_package.get("image_paths", [])
            action = data.replace("act_", "")
            
            msg_proc = bot.send_message(chat_id, "⏳ Đang thực thi thao tác lên Fanpage Facebook...")
            
            if action == "draft_fp1":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="draft", page_choice="1")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "draft_fp2":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="draft", page_choice="2")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "draft_both":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="draft", page_choice="all")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "sched_830":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="schedule_830", page_choice="1")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "sched_1130":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="schedule_1130", page_choice="1")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "sched_2000":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="schedule_2000", page_choice="1")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "publish_now":
                res = fb_workflow.execute_fb_action(post_text, image_paths, action_type="publish_now", page_choice="1")
                report_fb_result(bot, chat_id, res, msg_proc.message_id)
            elif action == "repurpose_vid":
                topic = last_package.get("topic", "Nâng tầm tư duy tài chính")
                process_start_video_interview(bot, chat_id, user_id, topic)


# --- Helper Functions ---

def process_create_fb_post(bot: telebot.TeleBot, chat_id: int, user_id: int, topic: str):
    """Quy trình tạo bài viết FB + Sinh 3 Slide Card + Gửi ảnh và phím hành động."""
    msg_waiting = bot.send_message(chat_id, f"✍️ Đang soạn bài viết chuẩn GMFinance & Sinh bộ 3 Slide Cards cho chủ đề: *{topic}*...", parse_mode="Markdown")
    
    # 1. Sinh trọn gói FB Post + 3 Slide Cards
    fb_package = fb_workflow.generate_fb_package(topic)
    USER_LAST_FB_POST[user_id] = fb_package
    
    # 2. Gửi 3 ảnh Slide Card lên Telegram
    image_paths = fb_package.get("image_paths", [])
    if image_paths:
        media_group = []
        for idx, img_p in enumerate(image_paths, 1):
            if os.path.exists(img_p):
                with open(img_p, "rb") as f_img:
                    media_group.append(types.InputMediaPhoto(f_img.read(), caption=f"Slide 0{idx}" if idx == 1 else None))
        
        if media_group:
            bot.send_media_group(chat_id, media_group)

    # 3. Gửi nội dung bài viết kèm nút bấm hành động
    post_text = fb_package.get("post_text", "")
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    b1 = types.InlineKeyboardButton("💾 Draft FP 1 (GMFinance)", callback_data="act_draft_fp1")
    b2 = types.InlineKeyboardButton("💾 Draft FP 2 (Giải Pháp TC)", callback_data="act_draft_fp2")
    b3 = types.InlineKeyboardButton("💾 Lưu Nháp Cả 2 Fanpage", callback_data="act_draft_both")
    
    s1 = types.InlineKeyboardButton("⏰ Lên lịch 08:30", callback_data="act_sched_830")
    s2 = types.InlineKeyboardButton("⏰ Lên lịch 11:30", callback_data="act_sched_1130")
    s3 = types.InlineKeyboardButton("⏰ Lên lịch 20:00", callback_data="act_sched_2000")
    
    pub = types.InlineKeyboardButton("🚀 Đăng Ngay FP 1", callback_data="act_publish_now")
    rep = types.InlineKeyboardButton("🎬 Chuyển Thành Kịch Bản Video", callback_data="act_repurpose_vid")
    
    markup.row(b1, b2)
    markup.row(b3)
    markup.row(s1, s2, s3)
    markup.row(pub, rep)
    
    try:
        bot.delete_message(chat_id, msg_waiting.message_id)
    except Exception:
        pass
    
    bot.send_message(
        chat_id,
        f"👑 **BÀI VIẾT FACEBOOK ĐÃ HOÀN THIỆN:**\n\n{post_text}\n\n"
        f"👇 **Chọn hành động 1-chạm bên dưới:**",
        reply_markup=markup
    )


def process_start_video_interview(bot: telebot.TeleBot, chat_id: int, user_id: int, topic: str):
    """Khởi động phiên phỏng vấn tương tác 3 câu hỏi cho Video ngắn."""
    first_question = video_workflow.start_interview(user_id, topic)
    session = video_workflow.get_active_session(user_id)
    
    intro_text = (
        f"🎬 **KHỞI ĐỘNG PHỎNG VẤN KỊCH BẢN VIDEO (TIKTOK / REELS)**\n"
        f"📌 **Chủ đề**: *{topic}*\n\n"
        f"Tôi sẽ đóng vai Đạo diễn và hỏi bạn **3 câu hỏi tương tác ngắn** để khai thác chất liệu thực tế của bạn.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎙️ **[CÂU HỎI 1/{len(session.questions)}]:**\n"
        f"👉 *{first_question}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"_(Bạn hãy gõ câu trả lời hoặc gửi voice note để tiếp tục, hoặc gõ `/cancel` để hủy)_"
    )
    bot.send_message(chat_id, intro_text, parse_mode="Markdown")


def report_fb_result(bot: telebot.TeleBot, chat_id: int, res_data: dict, waiting_msg_id: int = None):
    """Báo cáo kết quả đăng / lên lịch lên Telegram."""
    if waiting_msg_id:
        try:
            bot.delete_message(chat_id, waiting_msg_id)
        except Exception:
            pass
            
    results = res_data.get("results", [])
    report_lines = ["📢 **KẾT QUẢ THỰC THI FACEBOOK API:**\n"]
    
    for r in results:
        page_name = r.get("page_name", "Fanpage")
        if r.get("success"):
            post_id = r.get("post_id", "N/A")
            mode = r.get("mode", "Đăng bài")
            url = r.get("url", "https://facebook.com")
            report_lines.append(f"✅ **{page_name}**: Thành công!\n   • Chế độ: {mode}\n   • Post ID: `{post_id}`\n   • Link: [Xem Page]({url})\n")
        else:
            err = r.get("error", "Lỗi không xác định")
            report_lines.append(f"❌ **{page_name}**: Thất bại!\n   • Chi tiết lỗi: `{err}`\n")
            
    bot.send_message(chat_id, "\n".join(report_lines), parse_mode="Markdown")
