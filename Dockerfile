
# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Копируем static отдельно в корень контейнера
COPY static /static

# Указываем порт
EXPOSE 8000

# Передаём переменные окружения в контейнер
ENV DATABASE_URL=${DATABASE_URL}
ENV REDISHOST=${REDISHOST}
ENV REDISPORT=${REDISPORT}
ENV REDIS_PASSWORD=${REDIS_PASSWORD}

# Запуск FastAPI-приложения через Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
