FROM python:3.10-slim
WORKDIR /srv

COPY bot/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm -rf ~/.cache

# Копируем код бота и бэкенда в один образ
COPY bot/ ./bot
COPY app/ ./app

# Чтобы импорты видели и bot, и app
ENV PYTHONPATH=/srv

WORKDIR /srv/bot
CMD ["python", "main_bot.py"]
