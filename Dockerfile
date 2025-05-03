# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только папку bot + app (если бот использует app.config)
COPY bot/ ./bot/
COPY app/config.py ./app/

# Переменные окружения (Railway их подхватит сам, но можно оставить на всякий случай)
ENV BOT_TOKEN=${BOT_TOKEN}
ENV BACKEND_URL=${BACKEND_URL}

# Стартуем Telegram-бот
CMD ["python", "-m", "bot.main_bot"]

