# Используем минимальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

# Копируем весь проект (bot + app)
COPY ./bot /bot
COPY ./app /app

# Указываем PYTHONPATH, чтобы bot и app были видны
ENV PYTHONPATH=/bot:/app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /bot/requirements.txt

# Запускаем бота
CMD ["python", "/bot/main_bot.py"]
