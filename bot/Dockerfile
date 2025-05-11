# Используем минимальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /bot

# Копируем содержимое папки bot/
COPY . .

# Указываем путь к внешней папке app — Railway клонирует весь репозиторий
ENV PYTHONPATH=/bot:/bot/../app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем бота
CMD ["python", "main_bot.py"]
