import os
from dotenv import load_dotenv

load_dotenv()

# Админка
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "topsecret123")
ADMIN_IMAGE_SECRET = os.getenv("ADMIN_IMAGE_SECRET", "defaultsecret")

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8001")

# Redis
REDIS_HOST = os.getenv("REDISHOST", "localhost")
REDIS_PORT = int(os.getenv("REDISPORT", 6379))
REDIS_PASSWORD = os.getenv("REDISPASSWORD", None)

# База данных
DATABASE_URL = os.getenv("DATABASE_URL")
