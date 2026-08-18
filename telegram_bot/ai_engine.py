# -*- coding: utf-8 -*-
"""
AI Engine: Trí tuệ trung tâm của GMFinance Telegram Bot.
Nạp toàn bộ Knowledge Base và điều phối LLM (Google Gemini / OpenAI).
"""

import os
import json
import re
from telegram_bot import config

def load_knowledge_base():
    """Tải nội dung tất cả các file kiến thức chuẩn từ thư mục knowledge_base/."""
    kb_files = [
        "brand_identity_gmfinance.md",
        "copywriting_frameworks.md",
        "formatting_and_tone.md",
        "proven_templates.md",
        "viral_hooks_library.md",
        "video_script_templates.md"
    ]
    combined_kb = []
    for fname in kb_files:
        fpath = os.path.join(config.KNOWLEDGE_BASE_DIR, fname)
        if os.path.exists(fpath):
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    combined_kb.append(f"=== {fname} ===\n" + f.read())
            except Exception as e:
                print(f"[WARN] Không thể đọc {fname}: {e}")
    return "\n\n".join(combined_kb)

KNOWLEDGE_BASE_TEXT = load_knowledge_base()

SYSTEM_PROMPT_CORE = f"""
Bạn là AI Lead Content & Creative Director của thương hiệu GMFinance - Đào tạo & Coaching ACCA chuẩn quốc tế.
Biểu tượng thương hiệu: Con cờ Vua (Chess King) - Đại diện cho tư duy chiến lược, vị thế dẫn đầu trong Kế toán - Tài chính.
Slogan: "ELEVATE EXPERTISE, EXPAND CAREER HORIZONS"

Dưới đây là bộ Knowledge Base chuẩn mực của GMFinance:
{KNOWLEDGE_BASE_TEXT}

Hãy luôn tuân thủ nghiêm ngặt:
1. Giọng văn: Chuyên gia, thực chiến, truyền cảm hứng, ngắn gọn, súc tích (150 - 300 từ cho bài FB).
2. Quy tắc ngắt dòng: Ngắt dòng đôi sau mỗi 1-2 câu, dùng bullet point và in đậm từ khóa quan trọng.
3. Không viết lý thuyết suông, luôn có ví dụ thực tế hoặc phương pháp hành động ngay.
4. Đầu ra phải luôn chuẩn xác, chuyên nghiệp và có giá trị cao cho người đi làm & sinh viên Kế - Tài - Kiểm.
"""

def call_llm(prompt: str, json_mode: bool = False) -> str:
    """Gọi LLM với Gemini 2.5 Flash / 1.5 Flash hoặc OpenAI GPT-4o-mini."""
    # 1. Thử Google Gemini API
    if config.GEMINI_API_KEY:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=config.GEMINI_API_KEY)
            
            # Thử model mới nhất Gemini Flash
            for model_name in ["gemini-3.6-flash", "gemini-3.7-flash", "gemini-3.5-flash", "gemini-flash-latest"]:
                try:
                    config_args = types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT_CORE,
                        temperature=0.7
                    )
                    if json_mode:
                        config_args.response_mime_type = "application/json"
                    
                    response = client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                        config=config_args
                    )
                    if response and response.text:
                        return response.text.strip()
                except Exception as e_model:
                    continue
        except Exception as e:
            print(f"[WARN] Lỗi gọi Gemini SDK: {e}")

    # 2. Thử OpenAI API
    if config.OPENAI_API_KEY:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=config.OPENAI_API_KEY)
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT_CORE},
                {"role": "user", "content": prompt}
            ]
            response_format = {"type": "json_object"} if json_mode else None
            
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                response_format=response_format,
                temperature=0.7
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            print(f"[WARN] Lỗi gọi OpenAI: {e}")

    # 3. Fallback Mock Generator nếu chưa điền API Key
    return generate_fallback_content(prompt, json_mode)


def generate_fallback_content(prompt: str, json_mode: bool = False) -> str:
    """Fallback tự động khi người dùng chưa cấu hình API Key để test bot."""
    if json_mode:
        return json.dumps({
            "post_text": (
                "🎯 90% DÂN TÀI CHÍNH BẾ TẮC VÌ THIẾU TƯ DUY NÀY\n\n"
                "Bạn có bao giờ cảm thấy mình làm việc quần quật 10 tiếng mỗi ngày nhưng mức lương và vị trí vẫn giậm chân tại chỗ?\n\n"
                "Sự thật là: Chăm chỉ không tạo nên bứt phá. Chiến lược mới là chìa khóa.\n\n"
                "💡 3 BƯỚC THAY ĐỔI VỊ THẾ BẰNG TƯ DUY CON CỜ VUA:\n"
                "• 1. Tối ưu hóa 80/20: Tập trung 20% công việc mang lại 80% kết quả cốt lõi.\n"
                "• 2. Chuẩn hóa chuyên môn ACCA: Nâng cấp bằng cấp và tư duy quản trị chuẩn quốc tế.\n"
                "• 3. Định vị bản thân: Trở thành Strategic Advisor thay vì chỉ là Data Entry.\n\n"
                "👑 Hãy để GMFinance đồng hành cùng bạn nâng tầm sự nghiệp!\n\n"
                "#GMFinance #ACCA #CareerGrowth #WorkSmarter"
            ),
            "slides": [
                {
                    "number": "01",
                    "title": "Bẫy Làm Việc Chăm Chỉ",
                    "body": "90% người làm tài chính bị cuốn vào việc nhập liệu cơ bản mà quên đi việc nâng tầm tư duy chiến lược.",
                    "icon": "brain"
                },
                {
                    "number": "02",
                    "title": "Tư Duy Con Cờ Vua",
                    "body": "Người chơi cờ giỏi không di chuyển nhiều quân nhất. Họ di chuyển quân cờ mang tính quyết định nhất.",
                    "icon": "lightning"
                },
                {
                    "number": "03",
                    "title": "Bứt Phá Cùng ACCA",
                    "body": "Đầu tư vào chứng chỉ quốc tế và phương pháp quản trị hiện đại để mở rộng chân trời sự nghiệp.",
                    "icon": "target"
                }
            ],
            "hashtags": ["#GMFinance", "#ACCA", "#Productivity", "#ElevateExpertise"]
        }, ensure_ascii=False)
    
    return "💡 Đây là nội dung mẫu từ hệ thống AI Agent GMFinance."


def generate_fb_post_and_slides(topic: str, custom_instructions: str = "") -> dict:
    """
    Sinh bài viết Facebook hoàn chỉnh (150-300 từ) và dữ liệu cho bộ 3 Slide Card (1080x1080px).
    """
    prompt = f"""
Hãy tạo một bài viết Facebook hoàn chỉnh và nội dung cho 3 Slide Card cho thương hiệu GMFinance theo chủ đề sau:
CHỦ ĐỀ: {topic}
YÊU CẦU BỔ SUNG: {custom_instructions if custom_instructions else "Tuân thủ chuẩn PAS/AIDA và Bộ nhận diện GMFinance"}

Bạn BẮT BUỘC trả về định dạng JSON thuần túy (không bọc trong markdown codeblock) với schema sau:
{{
  "post_text": "Nội dung bài viết Facebook hoàn chỉnh (150-300 từ), có Hook 3 dòng đầu viral, chia đoạn rõ ràng, emoji chuyên nghiệp, CTA rõ ràng và hashtags GMFinance ở cuối",
  "slides": [
    {{
      "number": "01",
      "title": "Tiêu đề Slide 1 (Ngắn gọn, súc tích dưới 35 ký tự)",
      "body": "Nội dung giải thích slide 1 (2-3 câu ngắn gọn, xúc tích, cô đọng)",
      "icon": "brain" (chọn 1 trong các icon: brain, lightning, target, chart, check)
    }},
    {{
      "number": "02",
      "title": "Tiêu đề Slide 2 (Ngắn gọn, súc tích dưới 35 ký tự)",
      "body": "Nội dung giải thích slide 2 (2-3 câu ngắn gọn, xúc tích, cô đọng)",
      "icon": "lightning"
    }},
    {{
      "number": "03",
      "title": "Tiêu đề Slide 3 (Ngắn gọn, súc tích dưới 35 ký tự)",
      "body": "Nội dung giải thích slide 3 (2-3 câu ngắn gọn, xúc tích, cô đọng)",
      "icon": "target"
    }}
  ],
  "hashtags": ["#GMFinance", "#ACCA", "#Productivity"]
}}
"""
    raw_res = call_llm(prompt, json_mode=True)
    try:
        # Làm sạch nếu có markdown ```json
        cleaned = re.sub(r"^```json\s*", "", raw_res.strip())
        cleaned = re.sub(r"\s*```$", "", cleaned)
        data = json.loads(cleaned)
        return data
    except Exception as e:
        print(f"[ERROR] Lỗi parse JSON bài viết FB: {e}\nRaw: {raw_res}")
        return json.loads(generate_fallback_content("", json_mode=True))


def generate_video_interview_questions(topic: str) -> list:
    """
    Sinh 3 câu hỏi phỏng vấn tương tác ngắn dành riêng cho chủ đề video được chọn.
    """
    prompt = f"""
Bạn là Đạo diễn Video ngắn (TikTok/Reels) của GMFinance.
Chủ đề video người dùng muốn thực hiện: "{topic}".

Hãy tạo đúng 3 câu hỏi phỏng vấn tương tác ngắn, sắc bén, thân thiện để hỏi người dùng qua tin nhắn chat, giúp trích xuất trải nghiệm thực tế của họ:
- Câu 1: Hỏi về góc nhìn cá nhân / case study thực tế hoặc nỗi đau lớn nhất mà họ từng gặp với chủ đề này.
- Câu 2: Hỏi về bí quyết / phương pháp cốt lõi nhất mà họ muốn chia sẻ để giải quyết vấn đề đó.
- Câu 3: Hỏi về 1 lời khuyên đắt giá nhất (Takeaway) hoặc thông điệp muốn người xem hành động ngay.

Trả về định dạng JSON thuần túy:
{{
  "questions": [
    "Câu hỏi 1...",
    "Câu hỏi 2...",
    "Câu hỏi 3..."
  ]
}}
"""
    raw = call_llm(prompt, json_mode=True)
    try:
        cleaned = re.sub(r"^```json\s*", "", raw.strip())
        cleaned = re.sub(r"\s*```$", "", cleaned)
        data = json.loads(cleaned)
        return data.get("questions", [
            f"Trải nghiệm thực tế hoặc tình huống điển hình nhất của bạn về '{topic}' là gì?",
            "Giải pháp hoặc bí quyết quan trọng nhất để xử lý vấn đề này theo kinh nghiệm của bạn?",
            "Lời khuyên 1 câu cốt lõi (Actionable Takeaway) bạn muốn gửi gắm tới khán giả?"
        ])
    except Exception:
        return [
            f"Tình huống thực tế hoặc sai lầm phổ biến nhất liên quan đến '{topic}' mà bạn từng thấy?",
            "Phương pháp 3 bước cụ thể mà bạn áp dụng để giải quyết vấn đề này là gì?",
            "Một câu đúc kết đắt giá nhất bạn muốn khán giả ghi nhớ ngay sau khi xem video?"
        ]


def generate_video_script_from_interview(topic: str, qa_pairs: list) -> dict:
    """
    Ráp các câu trả lời phỏng vấn thành Kịch bản Video hoàn chỉnh (Hook 3s, Storyboard 4 cảnh, Góc quay, Voiceover).
    """
    qa_text = "\n".join([f"- Câu hỏi: {item['q']}\n  -> Trả lời: {item['a']}" for item in qa_pairs])
    
    prompt = f"""
Hãy đóng vai Đạo diễn Video GMFinance, chuyển đổi cuộc phỏng vấn sau thành một Kịch bản Video ngắn (TikTok / FB Reels) dài 45-60 giây:

CHỦ ĐỀ: {topic}
NỘI DUNG PHỎNG VẤN TỪ CHUYÊN GIA:
{qa_text}

Yêu cầu kịch bản chuẩn:
1. Hook 3 giây đầu: Cực kỳ giật gân, đánh trúng tâm lý người làm Kế - Tài - Kiểm.
2. Storyboard 4 cảnh:
   - Cảnh 1 (0-5s): Hook + Vấn đề nhức nhối.
   - Cảnh 2 (5-20s): Bóc tách nguyên nhân / Sai lầm phổ biến.
   - Cảnh 3 (20-45s): Giải pháp thực chiến (từ câu trả lời phỏng vấn).
   - Cảnh 4 (45-60s): Lời khuyên vàng + CTA theo dõi GMFinance.
3. Hướng dẫn quay cho 1 người tự quay bằng điện thoại (Góc máy, biểu cảm, ánh sáng).
4. Text Overlay tỉ lệ 9:16.
5. Caption + Hashtags tối ưu thuật toán.

Trả về JSON:
{{
  "title": "Tiêu đề video",
  "hook_3s": "Câu hook 3 giây đầu",
  "full_script_markdown": "Toàn bộ kịch bản chi tiết trình bày đẹp mắt bằng Markdown với bảng Storyboard từng cảnh, lời thoại, góc quay và text overlay",
  "caption": "Caption ngắn gọn đăng TikTok/Reels",
  "hashtags": ["#GMFinance", "#ACCA", "#LearnOnTikTok", "#TaiChinh"]
}}
"""
    raw = call_llm(prompt, json_mode=True)
    try:
        cleaned = re.sub(r"^```json\s*", "", raw.strip())
        cleaned = re.sub(r"\s*```$", "", cleaned)
        data = json.loads(cleaned)
        if data.get("title") and data.get("full_script_markdown"):
            return data
    except Exception as e:
        print(f"[WARN] Lỗi parse video script: {e}")

    return {
        "title": f"Video ngắn: {topic}",
        "hook_3s": "Đừng bao giờ làm điều này nếu bạn muốn thăng tiến trong ngành tài chính!",
        "full_script_markdown": (
            f"# KỊCH BẢN VIDEO: {topic}\n\n"
            f"## 🎬 HOOK (0-5s)\n"
            f"- **Hình ảnh**: Nhìn thẳng camera, biểu cảm nghiêm túc.\n"
            f"- **Lời thoại**: 'Đừng bao giờ bỏ qua tư duy này nếu bạn muốn thăng tiến trong Kế toán - Tài chính!'\n\n"
            f"## 💡 NỘI DUNG CHÍNH & GIẢI PHÁP (5-45s)\n"
            f"{qa_text}\n\n"
            f"## 🎯 KẾT LUẬN & CTA (45-60s)\n"
            f"- **Lời thoại**: 'Follow @GMFinance để nâng tầm sự nghiệp ACCA ngay hôm nay!'"
        ),
        "caption": f"Bí quyết làm chủ {topic} cho dân Tài chính - Kế toán! 🚀",
        "hashtags": ["#GMFinance", "#ACCA", "#LearnOnTikTok", "#KienThucTaiChinh"]
    }


def generate_topic_suggestions_from_notion(notes_summary: str) -> list:
    """
    Gợi ý 3-5 chủ đề sắc bén từ dữ liệu ghi chú Notion.
    """
    prompt = f"""
Dựa trên các ghi chú thu thập từ Notion Knowledge Vault sau đây:
{notes_summary}

Hãy chọn lọc và đề xuất 4 chủ đề bài viết Facebook / Video ngắn có tiềm năng tương tác cao nhất cho GMFinance.
Mỗi chủ đề cần có:
1. Tiêu đề hấp dẫn có tính gợi mở.
2. Góc nhìn tiếp cận (Ví dụ: Tâm lý học, Phương pháp thực chiến, Lộ trình ACCA, Phân tích sai lầm).
3. Lý do độc giả quan tâm.

Trả về JSON:
{{
  "suggestions": [
    {{
      "id": 1,
      "title": "Tên chủ đề 1",
      "angle": "Góc nhìn tiếp cận",
      "summary": "Tóm tắt ngắn gọn 1 câu"
    }},
    {{
      "id": 2,
      "title": "Tên chủ đề 2",
      "angle": "Góc nhìn tiếp cận",
      "summary": "Tóm tắt ngắn gọn 1 câu"
    }},
    {{
      "id": 3,
      "title": "Tên chủ đề 3",
      "angle": "Góc nhìn tiếp cận",
      "summary": "Tóm tắt ngắn gọn 1 câu"
    }},
    {{
      "id": 4,
      "title": "Tên chủ đề 4",
      "angle": "Góc nhìn tiếp cận",
      "summary": "Tóm tắt ngắn gọn 1 câu"
    }}
  ]
}}
"""
    raw = call_llm(prompt, json_mode=True)
    try:
        cleaned = re.sub(r"^```json\s*", "", raw.strip())
        cleaned = re.sub(r"\s*```$", "", cleaned)
        data = json.loads(cleaned)
        suggs = data.get("suggestions")
        if suggs and isinstance(suggs, list) and len(suggs) > 0:
            return suggs
    except Exception as e:
        print(f"[WARN] Lỗi parse suggestions: {e}")

    return [
        {"id": 1, "title": "Ma Trận Eisenhower Cho Dân Kế Toán", "angle": "Tối ưu hiệu suất", "summary": "Phân loại việc khẩn cấp vs quan trọng để thoát bẫy OT."},
        {"id": 2, "title": "Quy Tắc 5 Giây Chữa Bệnh Trì Hoãn Học ACCA", "angle": "Khai phá động lực", "summary": "Đếm 5-4-3-2-1 để bắt đầu học ngay lập tức."},
        {"id": 3, "title": "Phân Biệt Chuẩn Mực IFRS vs VAS Thực Chiến", "angle": "Chuyên môn sâu", "summary": "3 điểm khác biệt cốt lõi sinh viên và người đi làm cần nắm vững."},
        {"id": 4, "title": "Chiến Lược Vượt Qua Môn ACCA Financial Management", "angle": "Luyện thi ACCA", "summary": "Bí quyết giải đề và quản trị thời gian trong phòng thi."}
    ]
