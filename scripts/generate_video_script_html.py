#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script sinh file HTML xem trước Kịch Bản Video Ngắn (TikTok / FB Reels) cho GMFinance.
Output: File HTML self-contained với đầy đủ Script nói, Storyboard, Hướng dẫn quay,
Edit Guide, Caption TikTok/Reels, Nhạc nền — tất cả có nút Copy 1-Click.
Design system đồng bộ với html_generator.py (FB Post Preview).
"""

import os
import sys
import datetime
import re
import base64

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Output")


def file_to_base64(filepath):
    if not os.path.isabs(filepath):
        filepath = os.path.join(OUTPUT_DIR, filepath)
    if os.path.exists(filepath):
        try:
            ext = os.path.splitext(filepath)[1].lower().replace('.', '')
            if ext == 'jpg': ext = 'jpeg'
            if ext == 'svg': ext = 'svg+xml'
            with open(filepath, "rb") as f:
                encoded = base64.b64encode(f.read()).decode('utf-8')
                return f"data:image/{ext};base64,{encoded}"
        except Exception as e:
            print(f"[WARN] Lỗi Base64 {filepath}: {e}")
    return filepath


VIDEO_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GMFinance Video Script</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0f19;
            --card-bg: #151d2a;
            --card-bg-alt: #1a2332;
            --border: #1e293b;
            --border-accent: #2f3847;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-dim: #64748b;
            --primary: #3b82f6;
            --primary-glow: rgba(59, 130, 246, 0.15);
            --accent-yellow: #f59e0b;
            --accent-yellow-glow: rgba(245, 158, 11, 0.15);
            --accent-green: #10b981;
            --accent-green-glow: rgba(16, 185, 129, 0.15);
            --accent-purple: #8b5cf6;
            --accent-purple-glow: rgba(139, 92, 246, 0.15);
            --accent-red: #ef4444;
            --accent-pink: #ec4899;
            --radius: 16px;
            --radius-sm: 10px;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            padding: 24px 16px;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        /* Brand Header */
        .brand-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border);
            margin-bottom: 24px;
        }}

        .brand-logo-badge {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}

        .brand-logo-badge img {{
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: #fff;
            padding: 2px;
            box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
        }}

        .brand-name-title {{
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.35rem;
            font-weight: 700;
            color: #fff;
            letter-spacing: 1px;
        }}

        .brand-tagline {{
            font-size: 0.72rem;
            color: var(--text-muted);
            letter-spacing: 1.8px;
            text-transform: uppercase;
        }}

        .header-badge {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            color: var(--accent-yellow);
            background: var(--accent-yellow-glow);
            padding: 8px 18px;
            border-radius: 24px;
            border: 1px solid rgba(245, 158, 11, 0.25);
            font-weight: 600;
        }}

        /* Video Meta Card */
        .video-meta-card {{
            background: linear-gradient(135deg, var(--card-bg) 0%, var(--card-bg-alt) 100%);
            border: 1px solid var(--border-accent);
            border-radius: var(--radius);
            padding: 28px;
            margin-bottom: 24px;
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr;
            gap: 20px;
        }}

        @media (max-width: 768px) {{
            .video-meta-card {{ grid-template-columns: 1fr 1fr; }}
        }}

        .meta-item {{
            text-align: center;
        }}

        .meta-label {{
            font-size: 0.72rem;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 6px;
        }}

        .meta-value {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .meta-value.highlight-blue {{ color: var(--primary); }}
        .meta-value.highlight-yellow {{ color: var(--accent-yellow); }}
        .meta-value.highlight-green {{ color: var(--accent-green); }}
        .meta-value.highlight-purple {{ color: var(--accent-purple); }}

        /* Main Grid */
        .main-grid {{
            display: grid;
            grid-template-columns: 1fr 380px;
            gap: 24px;
        }}

        @media (max-width: 920px) {{
            .main-grid {{ grid-template-columns: 1fr; }}
        }}

        /* Section Cards */
        .section-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 24px;
            margin-bottom: 20px;
        }}

        .section-title {{
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--text-main);
        }}

        .section-title .icon {{ font-size: 1.2rem; }}

        .section-title .badge-accent {{
            font-size: 0.7rem;
            background: var(--primary-glow);
            color: var(--primary);
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 3px 10px;
            border-radius: 12px;
            font-weight: 600;
            margin-left: auto;
        }}

        /* Script Block */
        .script-block {{
            background: #090d16;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 20px;
            font-size: 0.92rem;
            line-height: 1.8;
            white-space: pre-wrap;
            word-break: break-word;
            color: #e2e8f0;
            position: relative;
        }}

        .script-block .timestamp {{
            color: var(--accent-yellow);
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.82rem;
        }}

        .script-block .hook-highlight {{
            background: rgba(245, 158, 11, 0.12);
            border-left: 3px solid var(--accent-yellow);
            padding: 8px 12px;
            margin: 8px 0;
            border-radius: 0 6px 6px 0;
        }}

        .script-block .label-tag {{
            display: inline-block;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 2px 8px;
            border-radius: 4px;
            margin-right: 6px;
        }}

        .tag-hook {{ background: rgba(239, 68, 68, 0.2); color: #f87171; }}
        .tag-context {{ background: rgba(59, 130, 246, 0.2); color: #60a5fa; }}
        .tag-point {{ background: rgba(16, 185, 129, 0.2); color: #34d399; }}
        .tag-cta {{ background: rgba(139, 92, 246, 0.2); color: #a78bfa; }}

        /* Storyboard Table */
        .storyboard-table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            font-size: 0.85rem;
        }}

        .storyboard-table thead th {{
            background: var(--card-bg-alt);
            color: var(--text-muted);
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 12px 14px;
            text-align: left;
            border-bottom: 2px solid var(--border-accent);
        }}

        .storyboard-table thead th:first-child {{ border-radius: 8px 0 0 0; }}
        .storyboard-table thead th:last-child {{ border-radius: 0 8px 0 0; }}

        .storyboard-table tbody td {{
            padding: 12px 14px;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
            color: #cbd5e1;
        }}

        .storyboard-table tbody tr:hover td {{
            background: rgba(59, 130, 246, 0.04);
        }}

        .storyboard-table .shot-number {{
            font-weight: 800;
            color: var(--accent-yellow);
            font-family: 'JetBrains Mono', monospace;
        }}

        .storyboard-table .time-cell {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: var(--primary);
        }}

        /* Shooting Guide */
        .guide-block {{
            background: #090d16;
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 18px;
            font-size: 0.88rem;
            line-height: 1.9;
            color: #cbd5e1;
        }}

        .guide-block .guide-section-title {{
            color: var(--accent-yellow);
            font-weight: 700;
            font-size: 0.9rem;
            margin: 12px 0 6px 0;
        }}

        .guide-block .guide-section-title:first-child {{ margin-top: 0; }}

        .guide-block ul {{
            list-style: none;
            padding-left: 4px;
        }}

        .guide-block ul li::before {{
            content: "•";
            color: var(--text-dim);
            margin-right: 8px;
        }}

        /* Sidebar */
        .sidebar {{ display: flex; flex-direction: column; gap: 16px; }}

        .btn-copy {{
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: #fff;
            border: none;
            border-radius: var(--radius-sm);
            font-size: 0.95rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
            transition: all 0.2s ease;
            font-family: inherit;
        }}

        .btn-copy:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5); }}

        .btn-tiktok {{
            background: linear-gradient(135deg, #000000, #25f4ee);
            box-shadow: 0 4px 14px rgba(37, 244, 238, 0.3);
        }}
        .btn-tiktok:hover {{ box-shadow: 0 6px 20px rgba(37, 244, 238, 0.4); }}

        .btn-reels {{
            background: linear-gradient(135deg, #833ab4, #fd1d1d, #fcb045);
            box-shadow: 0 4px 14px rgba(131, 58, 180, 0.4);
        }}
        .btn-reels:hover {{ box-shadow: 0 6px 20px rgba(131, 58, 180, 0.5); }}

        .btn-green {{
            background: linear-gradient(135deg, #10b981, #059669);
            box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
        }}

        .btn-purple {{
            background: linear-gradient(135deg, #8b5cf6, #6d28d9);
            box-shadow: 0 4px 14px rgba(139, 92, 246, 0.4);
        }}

        .action-panel {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .sidebar-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 20px;
        }}

        .sidebar-card h3 {{
            font-size: 1rem;
            margin-bottom: 14px;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .tag-list {{ display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }}

        .tag {{
            font-size: 0.78rem;
            font-weight: 600;
            padding: 4px 10px;
            border-radius: 6px;
        }}

        .tag-blue {{ background: var(--primary-glow); color: var(--primary); border: 1px solid rgba(59,130,246,0.3); }}
        .tag-gold {{ background: var(--accent-yellow-glow); color: var(--accent-yellow); border: 1px solid rgba(245,158,11,0.3); }}
        .tag-green-badge {{ background: var(--accent-green-glow); color: var(--accent-green); border: 1px solid rgba(16,185,129,0.3); }}

        .music-item {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 12px;
            background: #090d16;
            border: 1px solid var(--border);
            border-radius: 8px;
            margin-bottom: 8px;
            font-size: 0.85rem;
        }}

        .music-icon {{ font-size: 1.2rem; }}

        .music-name {{ color: var(--text-main); font-weight: 600; }}
        .music-keyword {{ color: var(--text-dim); font-size: 0.78rem; }}

        .caption-box {{
            background: #090d16;
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 14px;
            font-size: 0.88rem;
            color: #cbd5e1;
            white-space: pre-wrap;
            word-break: break-word;
            line-height: 1.7;
        }}

        /* Toast */
        .toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: var(--accent-green);
            color: #fff;
            padding: 14px 24px;
            border-radius: var(--radius-sm);
            font-weight: 700;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            pointer-events: none;
            z-index: 100;
            font-family: inherit;
        }}

        .toast.show {{ opacity: 1; transform: translateY(0); }}
    </style>
</head>
<body>

    <div class="container">
        <!-- Brand Header -->
        <header class="brand-header">
            <div class="brand-logo-badge">
                <img src="{logo_base64}" alt="GMFinance Logo">
                <div>
                    <h1 class="brand-name-title">GMFinance</h1>
                    <p class="brand-tagline">Elevate Expertise, Expand Career Horizons</p>
                </div>
            </div>
            <div class="header-badge">
                🎬 Video Director — Agent 4
            </div>
        </header>

        <!-- Video Meta Card -->
        <div class="video-meta-card">
            <div class="meta-item">
                <div class="meta-label">Dạng Video</div>
                <div class="meta-value highlight-blue">{video_type}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Độ Dài</div>
                <div class="meta-value highlight-yellow">{duration}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Nền Tảng</div>
                <div class="meta-value highlight-green">TikTok + Reels</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Mood Nhạc</div>
                <div class="meta-value highlight-purple">{music_mood}</div>
            </div>
        </div>

        <!-- Main Content Grid -->
        <div class="main-grid">
            <main>
                <!-- Script Section -->
                <div class="section-card">
                    <div class="section-title">
                        <span class="icon">📜</span>
                        Script Nói — Kịch Bản Video
                        <span class="badge-accent">HOOK 3 GIÂY</span>
                    </div>
                    <div class="script-block" id="scriptText">{script_content}</div>
                </div>

                <!-- Storyboard Section -->
                <div class="section-card">
                    <div class="section-title">
                        <span class="icon">🎬</span>
                        Storyboard — Phân Cảnh Chi Tiết
                    </div>
                    <div style="overflow-x: auto;">
                        <table class="storyboard-table">
                            <thead>
                                <tr>
                                    <th>Shot</th>
                                    <th>Thời Lượng</th>
                                    <th>Góc Quay</th>
                                    <th>Nội Dung</th>
                                    <th>Text Overlay</th>
                                    <th>Chuyển Cảnh</th>
                                </tr>
                            </thead>
                            <tbody>
                                {storyboard_rows}
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Shooting Guide Section -->
                <div class="section-card">
                    <div class="section-title">
                        <span class="icon">📱</span>
                        Hướng Dẫn Tự Quay (Điện Thoại + Chân Máy)
                    </div>
                    <div class="guide-block">
                        {shooting_guide}
                    </div>
                </div>

                <!-- Edit Guide Section -->
                <div class="section-card">
                    <div class="section-title">
                        <span class="icon">✂️</span>
                        Hướng Dẫn Edit — CapCut Pro
                    </div>
                    <div class="guide-block">
                        {edit_guide}
                    </div>
                </div>
            </main>

            <!-- Sidebar -->
            <aside class="sidebar">
                <!-- Action Buttons -->
                <div class="action-panel">
                    <button class="btn-copy" type="button" onclick="copyScript()">
                        📋 Copy Toàn Bộ Script Nói
                    </button>
                    <button class="btn-copy btn-tiktok" type="button" onclick="copyCaption('tiktok')">
                        🎵 Copy Caption TikTok
                    </button>
                    <button class="btn-copy btn-reels" type="button" onclick="copyCaption('reels')">
                        📸 Copy Caption FB Reels
                    </button>
                    <button class="btn-copy btn-green" type="button" onclick="copyStoryboard()">
                        🎬 Copy Storyboard (Text)
                    </button>
                </div>

                <!-- Caption TikTok -->
                <div class="sidebar-card">
                    <h3>🎵 Caption TikTok</h3>
                    <div class="caption-box" id="captionTiktok">{caption_tiktok}</div>
                </div>

                <!-- Caption FB Reels -->
                <div class="sidebar-card">
                    <h3>📸 Caption FB Reels</h3>
                    <div class="caption-box" id="captionReels">{caption_reels}</div>
                </div>

                <!-- Hashtags -->
                <div class="sidebar-card">
                    <h3>#️⃣ Hashtags Chiến Lược</h3>
                    <div class="tag-list">
                        {hashtag_badges}
                    </div>
                </div>

                <!-- Music Suggestions -->
                <div class="sidebar-card">
                    <h3>🎵 Gợi Ý Nhạc Nền</h3>
                    {music_items}
                </div>

                <!-- Posting Schedule -->
                <div class="sidebar-card">
                    <h3>⏰ Khung Giờ Đăng Đề Xuất</h3>
                    <div style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.8;">
                        <strong style="color: var(--accent-green);">TikTok:</strong> {tiktok_time}<br>
                        <strong style="color: var(--accent-purple);">FB Reels:</strong> {reels_time}
                    </div>
                </div>

                <!-- Brand Info -->
                <div class="sidebar-card">
                    <h3>👑 Thương Hiệu & Định Vị</h3>
                    <div class="tag-list">
                        <span class="tag tag-gold">GMFinance</span>
                        <span class="tag tag-blue">ACCA Coaching</span>
                        <span class="tag tag-green-badge">Chess King</span>
                    </div>
                    <p style="font-size: 0.82rem; color: var(--text-dim); margin-top: 8px;">
                        <em>"Elevate Expertise, Expand Career Horizons"</em>
                    </p>
                </div>
            </aside>
        </div>
    </div>

    <div class="toast" id="toastNotification">Đã sao chép!</div>

    <script>
        function copyScript() {{
            const text = document.getElementById('scriptText').innerText;
            navigator.clipboard.writeText(text).then(() => {{
                showToast("✅ Đã copy toàn bộ Script Nói vào Clipboard!");
            }}).catch(err => {{
                showToast("❌ Lỗi copy: " + err);
            }});
        }}

        function copyCaption(platform) {{
            const id = platform === 'tiktok' ? 'captionTiktok' : 'captionReels';
            const label = platform === 'tiktok' ? 'TikTok' : 'FB Reels';
            const text = document.getElementById(id).innerText;
            navigator.clipboard.writeText(text).then(() => {{
                showToast("✅ Đã copy Caption " + label + "! Dán vào app để đăng.");
            }}).catch(err => {{
                showToast("❌ Lỗi copy: " + err);
            }});
        }}

        function copyStoryboard() {{
            const rows = document.querySelectorAll('.storyboard-table tbody tr');
            let text = "STORYBOARD — PHÂN CẢNH CHI TIẾT\\n\\n";
            rows.forEach((row, i) => {{
                const cells = row.querySelectorAll('td');
                text += `Shot ${{cells[0].innerText}} | ${{cells[1].innerText}} | ${{cells[2].innerText}}\\n`;
                text += `  Nội dung: ${{cells[3].innerText}}\\n`;
                text += `  Text overlay: ${{cells[4].innerText}}\\n`;
                text += `  Chuyển cảnh: ${{cells[5].innerText}}\\n\\n`;
            }});
            navigator.clipboard.writeText(text).then(() => {{
                showToast("✅ Đã copy Storyboard dạng text!");
            }}).catch(err => {{
                showToast("❌ Lỗi copy: " + err);
            }});
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toastNotification');
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{ toast.classList.remove('show'); }}, 3500);
        }}
    </script>
</body>
</html>
"""


def slugify(text):
    text = text.lower().strip()
    chars = {
        'a': '[àáảãạăằắẳẵặâầấẩẫậ]',
        'd': '[đ]',
        'e': '[èéẻẽẹêềếểễệ]',
        'i': '[ìíỉĩị]',
        'o': '[òóỏõọôồốổỗộơờớởỡợ]',
        'u': '[ùúủũụưừứửữự]',
        'y': '[ỳýỷỹỵ]'
    }
    for char, pattern in chars.items():
        text = re.sub(pattern, char, text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text[:40].strip('-')


def build_storyboard_rows(storyboard):
    """
    storyboard: list of dicts with keys:
        shot, time, angle, content, text_overlay, transition
    """
    rows = ""
    for scene in storyboard:
        rows += f"""
                                <tr>
                                    <td class="shot-number">{scene.get('shot', '')}</td>
                                    <td class="time-cell">{scene.get('time', '')}</td>
                                    <td>{scene.get('angle', '')}</td>
                                    <td>{scene.get('content', '')}</td>
                                    <td>{scene.get('text_overlay', '—')}</td>
                                    <td>{scene.get('transition', 'Cut')}</td>
                                </tr>"""
    return rows


def build_hashtag_badges(hashtags_list):
    badges = ""
    for i, tag in enumerate(hashtags_list):
        if i < 2:
            cls = "tag tag-gold"
        elif i < 5:
            cls = "tag tag-blue"
        else:
            cls = "tag tag-green-badge"
        badges += f'<span class="{cls}">{tag}</span>\n'
    return badges


def build_music_items(music_suggestions):
    """
    music_suggestions: list of dicts with keys: name, keyword, mood_icon
    """
    items = ""
    for m in music_suggestions:
        items += f"""
                    <div class="music-item">
                        <span class="music-icon">{m.get('mood_icon', '🎵')}</span>
                        <div>
                            <div class="music-name">{m.get('name', '')}</div>
                            <div class="music-keyword">Tìm: "{m.get('keyword', '')}"</div>
                        </div>
                    </div>"""
    return items


def create_video_script_html(
    title,
    video_type="Talking Head",
    duration="45 giây",
    music_mood="Motivational",
    script_content="",
    storyboard=None,
    shooting_guide="",
    edit_guide="",
    caption_tiktok="",
    caption_reels="",
    hashtags=None,
    music_suggestions=None,
    tiktok_time="20:30 – 22:00 tối",
    reels_time="20:00 – 21:30 tối"
):
    """
    Sinh file HTML preview kịch bản video ngắn GMFinance.

    Args:
        title: Tên video
        video_type: Dạng video (Talking Head, B-Roll, Tutorial, etc.)
        duration: Độ dài đề xuất
        music_mood: Mood nhạc nền
        script_content: Nội dung script nói (HTML formatted)
        storyboard: List of scene dicts
        shooting_guide: HTML formatted shooting guide
        edit_guide: HTML formatted edit guide
        caption_tiktok: Caption cho TikTok
        caption_reels: Caption cho FB Reels
        hashtags: List of hashtag strings
        music_suggestions: List of music dicts
        tiktok_time: Khung giờ đăng TikTok
        reels_time: Khung giờ đăng FB Reels

    Returns:
        Path to created HTML file
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if storyboard is None:
        storyboard = []
    if hashtags is None:
        hashtags = ["#GMFinance", "#ACCA", "#ElevateExpertise"]
    if music_suggestions is None:
        music_suggestions = []

    logo_path = os.path.join(OUTPUT_DIR, "assets", "gmfinance_official_logo.png")
    logo_base64 = file_to_base64(logo_path)

    storyboard_rows = build_storyboard_rows(storyboard)
    hashtag_badges = build_hashtag_badges(hashtags)
    music_items = build_music_items(music_suggestions)

    html_code = VIDEO_HTML_TEMPLATE.format(
        title=title,
        logo_base64=logo_base64,
        video_type=video_type,
        duration=duration,
        music_mood=music_mood,
        script_content=script_content,
        storyboard_rows=storyboard_rows,
        shooting_guide=shooting_guide,
        edit_guide=edit_guide,
        caption_tiktok=caption_tiktok,
        caption_reels=caption_reels,
        hashtag_badges=hashtag_badges,
        music_items=music_items,
        tiktok_time=tiktok_time,
        reels_time=reels_time
    )

    date_prefix = datetime.datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_prefix}_video_{slug}.html"
    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_code)

    print(f"[SUCCESS] Đã tạo file HTML Video Script Preview: {file_path}")
    return file_path


if __name__ == "__main__":
    # Demo: Tạo 1 kịch bản mẫu Talking Head
    demo_script = """<div class="hook-highlight"><span class="label-tag tag-hook">HOOK</span> <span class="timestamp">[0:00 - 0:03]</span>
"90% người thi ACCA trượt vì 3 sai lầm này."</div>

<span class="label-tag tag-context">CONTEXT</span> <span class="timestamp">[0:03 - 0:08]</span>
"Và mình đã từng mắc cả 3. Đây là bài học đắt giá nhất…"

<span class="label-tag tag-point">POINT 1</span> <span class="timestamp">[0:08 - 0:18]</span>
"Thứ nhất — Cày đề cũ mà không hiểu examiner muốn gì.
Đề ACCA kiểm tra tư duy, không kiểm tra trí nhớ."

<span class="label-tag tag-point">POINT 2</span> <span class="timestamp">[0:18 - 0:28]</span>
"Thứ hai — Tự học một mình mà không có feedback.
Bạn không biết mình sai ở đâu cho đến khi nhận kết quả thi."

<span class="label-tag tag-point">POINT 3</span> <span class="timestamp">[0:28 - 0:38]</span>
"Thứ ba — Ôm đồm quá nhiều môn cùng lúc.
Tập trung 1-2 môn mỗi kỳ, pass rate sẽ tăng đáng kể."

<span class="label-tag tag-cta">CTA</span> <span class="timestamp">[0:38 - 0:45]</span>
"Bạn đang mắc sai lầm nào? Comment số 1, 2 hoặc 3 bên dưới!
Follow GMFinance để xem thêm tips ACCA mỗi ngày nhé."
"""

    demo_storyboard = [
        {"shot": "01", "time": "0:00–0:03", "angle": "Medium Shot", "content": "Hook — Nhìn thẳng camera, biểu cảm nghiêm túc", "text_overlay": "90% TRƯỢT ACCA VÌ 3 SAI LẦM NÀY (bold, top 1/3)", "transition": "—"},
        {"shot": "02", "time": "0:03–0:08", "angle": "Medium Shot", "content": "Context — Chia sẻ trải nghiệm cá nhân", "text_overlay": "—", "transition": "Cut"},
        {"shot": "03", "time": "0:08–0:18", "angle": "Medium Shot", "content": "Sai lầm #1 — Cày đề không hiểu đề", "text_overlay": "❌ SAI LẦM 1: Cày đề không hiểu đề (giữa)", "transition": "Cut"},
        {"shot": "04", "time": "0:18–0:28", "angle": "Medium Shot", "content": "Sai lầm #2 — Không có feedback", "text_overlay": "❌ SAI LẦM 2: Không có người review (giữa)", "transition": "Cut"},
        {"shot": "05", "time": "0:28–0:38", "angle": "Medium Shot", "content": "Sai lầm #3 — Ôn quá nhiều môn", "text_overlay": "❌ SAI LẦM 3: Ôn quá nhiều môn (giữa)", "transition": "Zoom In"},
        {"shot": "06", "time": "0:38–0:45", "angle": "Close-up", "content": "CTA — Kêu gọi comment + follow", "text_overlay": "COMMENT 1, 2 hoặc 3 👇 + @GMFinance", "transition": "Fade Out"},
    ]

    demo_shooting = """<div class="guide-section-title">📱 SETUP QUAY</div>
<ul>
<li>Điện thoại: Chế độ Camera 1080p, tỷ lệ 9:16 (dọc)</li>
<li>Chân máy: Đặt ngang tầm mắt, cách 60–80cm</li>
<li>Mắt nhìn: Nhìn thẳng ống kính, KHÔNG nhìn màn hình</li>
<li>Micro: Micro tích hợp (phòng yên tĩnh)</li>
</ul>

<div class="guide-section-title">💡 ÁNH SÁNG</div>
<ul>
<li>Ưu tiên: Ngồi đối diện cửa sổ (ánh sáng tự nhiên)</li>
<li>Backup: 1 đèn LED đặt trước mặt, góc 45°</li>
<li>Tránh: Không ngồi quay lưng vào cửa sổ</li>
</ul>

<div class="guide-section-title">🎨 BACKGROUND</div>
<ul>
<li>Kệ sách gọn gàng hoặc tường trắng có cây xanh</li>
<li>Bàn làm việc tối giản, sạch sẽ</li>
<li>Tránh: Giường ngủ, quần áo phơi, nền lộn xộn</li>
</ul>"""

    demo_edit = """<div class="guide-section-title">✂️ CẮT GHÉP</div>
<ul>
<li>Cắt mọi khoảng lặng > 0.5 giây</li>
<li>Mỗi cut mới khi chuyển ý (Point 1 → Point 2)</li>
<li>Zoom in nhẹ (105–110%) khi nói điểm quan trọng</li>
</ul>

<div class="guide-section-title">📝 TEXT & CAPTION</div>
<ul>
<li>Bật Auto-Caption tiếng Việt</li>
<li>Font: Montserrat Bold, chữ trắng viền đen</li>
<li>Highlight keyword bằng màu vàng (#f59e0b)</li>
<li>Text overlay mỗi 5–8 giây tại key points</li>
</ul>

<div class="guide-section-title">🎵 NHẠC & HIỆU ỨNG</div>
<ul>
<li>Nhạc nền volume 10–15%, không có lời</li>
<li>Transition: Cut thẳng (chuyên nghiệp)</li>
<li>Watermark: Logo GMFinance góc trên phải, opacity 40%</li>
</ul>"""

    create_video_script_html(
        title="3 Sai Lầm Phổ Biến Khi Ôn ACCA",
        video_type="Talking Head",
        duration="45 giây",
        music_mood="Motivational",
        script_content=demo_script,
        storyboard=demo_storyboard,
        shooting_guide=demo_shooting,
        edit_guide=demo_edit,
        caption_tiktok="90% người thi ACCA trượt vì 3 sai lầm này 😱 Bạn đang mắc lỗi nào? Comment 1, 2 hoặc 3! 👇\n\n#LearnOnTikTok #ACCA #ACCATips #FinanceTikTok #GMFinance #ElevateExpertise",
        caption_reels="Tại sao 90% thí sinh ACCA trượt từ lần thi đầu tiên? 🤔\n\nKhông phải vì thiếu kiến thức — mà vì 3 sai lầm phương pháp mà đa số người học đều mắc phải.\n\nTrong video này, mình chia sẻ 3 lỗi mình từng mắc và cách khắc phục đã giúp mình đỗ 3 môn cùng 1 kỳ thi.\n\n💬 Bạn đang chinh phục môn ACCA nào? Comment chia sẻ nhé!\n\n#GMFinance #ACCA #ACCACoaching #FinanceCareer #ElevateExpertise #Big4Careers #StudyTips",
        hashtags=["#GMFinance", "#ElevateExpertise", "#LearnOnTikTok", "#ACCA", "#ACCATips", "#FinanceTikTok", "#Big4Careers", "#StudyTips"],
        music_suggestions=[
            {"name": "Inspiring Corporate", "keyword": "motivational corporate background", "mood_icon": "🔥"},
            {"name": "Epic Motivation", "keyword": "epic motivation cinematic", "mood_icon": "⚡"},
            {"name": "Modern Upbeat", "keyword": "modern upbeat positive", "mood_icon": "🎯"},
        ],
        tiktok_time="20:30 – 22:00 tối",
        reels_time="20:00 – 21:30 tối"
    )
