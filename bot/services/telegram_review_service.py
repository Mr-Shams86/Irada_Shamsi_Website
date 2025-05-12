import aiohttp
import os


BOT_TOKEN = os.getenv("BOT_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не установлен в переменных окружения!")

TELEGRAM_API = f"https://api.telegram.org"


async def upload_telegram_avatar_to_backend(
    telegram_id: int, file_path: str
) -> str | None:
    """
    Получает файл из Telegram и отправляет его на бэкенд.
    Возвращает строку пути (photo_url), сохранённого на сервере.
    """
    filename = f"{telegram_id}.jpg"
    url = f"{TELEGRAM_API}/file/bot{BOT_TOKEN}/{file_path}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                print(f"[❌] Не удалось получить файл Telegram: {resp.status}")
                return None

            file_bytes = await resp.read()

        # Отправка на бэкенд
        form = aiohttp.FormData()
        form.add_field("file", file_bytes, filename=filename, content_type="image/jpeg")
        form.add_field("filename", filename)

        async with session.post(
            f"{BACKEND_URL}/api/telegram-reviews/avatar", data=form
        ) as backend_resp:
            if backend_resp.status != 200:
                print(f"[❌] Backend не принял аватар: {backend_resp.status}")
                return None

            result = await backend_resp.json()
            return result.get("photo_url")
