# Используем официальный минимальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

# Копируем только requirements.txt (должен быть в папке bot/)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt && rm -rf ~/.cache

# Копируем весь код бота
COPY . .

# Указываем PYTHONPATH, чтобы видеть внутренние импорты (например, config)
ENV PYTHONPATH=/bot

# Запуск бота
CMD ["python", "main_bot.py"]
