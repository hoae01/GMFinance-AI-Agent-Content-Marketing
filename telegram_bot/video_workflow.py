# -*- coding: utf-8 -*-
"""
Workflow phỏng vấn tương tác từng bước (Interactive Interview) & Sinh Kịch Bản Video TikTok/Reels cho Telegram Bot.
"""

import os
from datetime import datetime
from telegram_bot import config, ai_engine

class VideoInterviewSession:
    def __init__(self, user_id: int, topic: str):
        self.user_id = user_id
        self.topic = topic
        self.step = 0  # 0, 1, 2 (đang hỏi câu 1, 2, 3)
        self.questions = ai_engine.generate_video_interview_questions(topic)
        self.qa_pairs = []
        self.is_completed = False

    def get_current_question(self) -> str:
        """Lấy câu hỏi hiện tại để gửi cho người dùng."""
        if self.step < len(self.questions):
            return self.questions[self.step]
        return ""

    def submit_answer(self, answer_text: str):
        """Ghi nhận câu trả lời và chuyển sang câu hỏi kế tiếp."""
        if self.step < len(self.questions):
            current_q = self.questions[self.step]
            self.qa_pairs.append({"q": current_q, "a": answer_text})
            self.step += 1
            
            if self.step >= len(self.questions):
                self.is_completed = True
                return None  # Đã hoàn thành hết câu hỏi
            return self.questions[self.step]
        return None

    def build_final_script(self) -> dict:
        """Tổng hợp toàn bộ kịch bản hoàn chỉnh từ các câu trả lời."""
        script_data = ai_engine.generate_video_script_from_interview(self.topic, self.qa_pairs)
        
        # Lưu file kịch bản Markdown vào thư mục Output
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = f"{timestamp}_video_script.md"
        filepath = os.path.join(config.OUTPUT_DIR, filename)
        
        markdown_content = (
            f"# KỊCH BẢN VIDEO NGẮN: {script_data.get('title', self.topic)}\n"
            f"- **Chủ đề**: {self.topic}\n"
            f"- **Hook 3s**: {script_data.get('hook_3s', '')}\n"
            f"- **Caption**: {script_data.get('caption', '')}\n"
            f"- **Hashtags**: {' '.join(script_data.get('hashtags', []))}\n\n"
            f"## NỘI DUNG CHI TIẾT & STORYBOARD:\n"
            f"{script_data.get('full_script_markdown', '')}\n"
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        script_data["file_path"] = filepath
        return script_data


# Quản lý các phiên phỏng vấn đang diễn ra theo user_id
ACTIVE_SESSIONS = {}

def start_interview(user_id: int, topic: str) -> str:
    """Bắt đầu một phiên phỏng vấn video mới và trả về câu hỏi đầu tiên."""
    session = VideoInterviewSession(user_id, topic)
    ACTIVE_SESSIONS[user_id] = session
    q1 = session.get_current_question()
    return q1

def get_active_session(user_id: int) -> VideoInterviewSession:
    """Lấy phiên phỏng vấn đang active của user."""
    return ACTIVE_SESSIONS.get(user_id)

def cancel_session(user_id: int):
    """Hủy phiên phỏng vấn hiện tại."""
    if user_id in ACTIVE_SESSIONS:
        del ACTIVE_SESSIONS[user_id]
