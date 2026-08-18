@echo off
chcp 65001 >nul
title GMFinance AI Agent - Telegram Bot Service

echo =========================================================
echo    👑 GMFINANCE AI AGENT - TELEGRAM BOT SERVICE
echo    "ELEVATE EXPERTISE, EXPAND CAREER HORIZONS"
echo =========================================================
echo.
echo [*] Đang khởi động Telegram Bot Agent...
echo.

python telegram_bot\bot.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Đã dừng hoặc gặp lỗi khi chạy Bot.
    echo Vui lòng kiểm tra file .env hoặc kết nối mạng.
    pause
)
