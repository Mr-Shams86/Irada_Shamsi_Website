import aiohttp
import os


BOT_TOKEN = os.getenv("BOT_TOKEN")
STATIC_AVATAR_URL = os.getenv("STATIC_AVATAR_URL", "/static/images/review_avatars")

BACKEND_URL = os.getenv("BACKEND_URL")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не установлен в переменных окружения!")

TELEGRAM_API = f"https://api.telegram.org"


async def download_telegram_file(telegram_id: int, file_path: str) -> str | None:
    """
    Скачивает аватарку пользователя и сохраняет в static/images/review_avatars.
    Возвращает путь photo_url, который можно использовать на сайте.
    """
    filename = f"{telegram_id}.jpg"
    url = f"{TELEGRAM_API}/file/bot{BOT_TOKEN}/{file_path}"

    static_dir = os.getenv("STATIC_DIR", "/app/static")  # по Railway
    save_path = os.path.join(static_dir, "images", "review_avatars", filename)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    print(f"[❌] Не удалось получить файл Telegram: {resp.status}")
                    return None
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, "wb") as f:
                    f.write(await resp.read())

        return f"{STATIC_AVATAR_URL}/{filename}"
    except Exception as e:
        print(f"[❌] Ошибка при скачивании файла: {e}")
        return None
