# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только папку bot (НЕ копируем app)
COPY bot/ ./bot/

# Переменные окружения (Railway сам подхватит)
ENV BOT_TOKEN=${BOT_TOKEN}
ENV BACKEND_URL=${BACKEND_URL}

# Стартуем Telegram-бот
CMD ["python", "-m", "bot.main_bot"]

