FROM python:3.11-slim

WORKDIR /app

# Cài đặt font chữ hệ thống hỗ trợ tiếng Việt cho Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-dejavu-core \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt thư viện Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn
COPY . .

# Chạy bot ngầm
CMD ["python", "telegram_bot/bot.py"]
