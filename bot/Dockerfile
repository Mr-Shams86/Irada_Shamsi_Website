# Используем официальный минимальный образ Python 3.10
FROM python:3.10-slim

WORKDIR /bot

COPY ./bot /bot
COPY ./app /app

ENV PYTHONPATH=/bot:/bot/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main_bot.py"]

