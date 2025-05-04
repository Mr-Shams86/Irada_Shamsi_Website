# Используем официальный минимальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt (новый, облегчённый)
COPY requirements.txt .

# Устанавливаем зависимости (чистая установка без кеша)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем папку bot (только бот, не весь app)
COPY . .

# Указываем переменные окружения (Railway их подхватит автоматически)
ENV BOT_TOKEN=${BOT_TOKEN}
ENV BACKEND_URL=${BACKEND_URL}

# Запускаем Telegram-бот
CMD ["python", "-m", "main_bot"]
