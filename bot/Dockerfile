# Используем официальный минимальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

# Копируем только requirements (новый requirements должен быть в корне бота)
COPY requirements.txt .

# Устанавливаем зависимости без кеша
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код бота (только bot-папку)
COPY . .

# Жестко НЕ задаём ENV здесь, Railway их всё равно пробрасывает!
# ENV BOT_TOKEN=${BOT_TOKEN}
# ENV BACKEND_URL=${BACKEND_URL}

# Указываем явный запуск бота
CMD ["python", "main_bot.py"]
