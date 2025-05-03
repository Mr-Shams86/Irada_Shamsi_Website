import os
from pathlib import Path
from dotenv import load_dotenv


dotenv_path = Path(__file__).resolve().parent.parent / ".env"

if not load_dotenv(dotenv_path):
    print(f"⚠️ WARNING: .env file not found at {dotenv_path}")
else:
    print(f"✅ Loaded .env from {dotenv_path}")

# Админка
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
ADMIN_IMAGE_SECRET = os.getenv("ADMIN_IMAGE_SECRET", "defaultsecret")

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

if not BACKEND_URL:
    raise ValueError("❌ BACKEND_URL is not set! Please check your environment.")

print(f"[DEBUG] BACKEND_URL = {BACKEND_URL}")


# Redis
REDISHOST = os.getenv("REDISHOST", "localhost")
try:
    REDISPORT = int(os.getenv("REDISPORT") or 6379)
except ValueError:
    print("⚠️ REDISPORT is invalid, defaulting to 6379")
    REDISPORT = 6379

REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

# База данных
DATABASE_URL = os.getenv("DATABASE_URL")
