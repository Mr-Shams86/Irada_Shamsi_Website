# bot/services/telegram_review_service.py
import os
import aiohttp
import httpx
import mimetypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")  # например: https://irada-shamsi.com  (без / в конце)
TELEGRAM_API = "https://api.telegram.org"

async def download_telegram_file(telegram_id: int, file_path: str) -> str | None:
    """
    Качаем аватар из Telegram и ЗАГРУЖАЕМ его на backend в /api/telegram-reviews/avatar.
    Возвращаем относительный URL вида: /static/images/review_avatars/<telegram_id>.<ext>
    """
    if not BOT_TOKEN or not BACKEND_URL:
        print("[⚠️] BOT_TOKEN/BACKEND_URL не заданы")
        return None

    # Определим расширение и mime
    ext = os.path.splitext(file_path)[1].lower() or ".jpg"
    if ext not in (".jpg", ".jpeg", ".png", ".webp"):
        ext = ".jpg"
    mime = mimetypes.types_map.get(ext, "image/jpeg")

    tg_file_url = f"{TELEGRAM_API}/file/bot{BOT_TOKEN}/{file_path}"
    filename = f"{telegram_id}{ext}"

    try:
        # 1) Скачиваем байты из Telegram
        async with aiohttp.ClientSession() as session:
            async with session.get(tg_file_url) as resp:
                if resp.status != 200:
                    print(f"[⚠️] TG download failed: {resp.status} for {tg_file_url}")
                    return None
                content = await resp.read()

        # 2) Отправляем на backend (FastAPI-эндпоинт /api/telegram-reviews/avatar)
        upload_url = f"{BACKEND_URL}/api/telegram-reviews/avatar"
        files = {"file": (filename, content, mime)}
        data = {"filename": filename}  # у тебя эндпоинт это ждёт

        async with httpx.AsyncClient(timeout=20.0) as client:
            r = await client.post(upload_url, files=files, data=data)
            if r.status_code != 200:
                print(f"[⚠️] Backend upload failed: {r.status_code} {r.text}")
                return None
            j = r.json()
            return j.get("photo_url")

    except Exception as e:
        print(f"[⚠️] Avatar pipeline error: {e}")
        return None
