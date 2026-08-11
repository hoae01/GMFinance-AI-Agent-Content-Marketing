@echo off
chcp 65001 > nul
echo ========================================================
echo   GMFINANCE - COPY TẤT CẢ 3 ẢNH SLIDE VÀO CLIPBOARD (FB)
echo ========================================================
echo.
powershell -Command "Set-Clipboard -Path '%~dp0assets\slide_01.png', '%~dp0assets\slide_02.png', '%~dp0assets\slide_03.png'"
echo [THÀNH CÔNG] Đã copy trọn bộ 3 file ảnh Slide vào Bộ nhớ tạm!
echo Hãy mở Facebook và nhấn Ctrl + V để dán CẢ 3 ẢNH CÙNG LÚC nhé.
echo.
pause
