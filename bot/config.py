import os
from dotenv import load_dotenv

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL", "").strip().rstrip("/")


print(f"🔎 BACKEND_URL={BACKEND_URL}")

print(f"🌍 RAW BACKEND_URL: {os.environ.get('BACKEND_URL')}")
