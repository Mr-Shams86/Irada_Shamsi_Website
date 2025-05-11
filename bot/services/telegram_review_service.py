# bot/services/telegram_review_service.py

from pathlib import Path
from os.path import basename

import aiohttp
from bot.config import BOT_TOKEN


STATIC_AVATARS_DIR = Path("static/images/review_avatars")


async def download_telegram_file(file_path: str, filename: str) -> str:
    """
    Скачивает файл с Telegram API и сохраняет локально.
    Возвращает путь для хранения в базе (относительно static)
    """
    url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

    filename = basename(filename)
    local_path = STATIC_AVATARS_DIR / filename

    STATIC_AVATARS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"📥 Скачивание файла из: {url}")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise Exception(f"Не удалось скачать файл: {resp.status}")
            with open(local_path, "wb") as f:
                f.write(await resp.read())

    print(f"✅ Файл сохранён: {local_path}")
    return f"/static/images/review_avatars/{filename}"
