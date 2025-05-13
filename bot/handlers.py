import httpx

from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

from services.telegram_review_service import upload_telegram_avatar_to_backend


from states import ReviewStates

from bot_instance import bot

from config import BACKEND_URL

# ================== НАСТРОЙКИ ==================
# Переводы по языкам
LANGUAGES = {
    "ru": {
        "start": "Привет 👋! Нажми на кнопку ниже, чтобы оставить отзыв 💬👇",
        "choose_language": "Пожалуйста, выбери язык 🌐",
        "leave_feedback": "💬 ⭐ Оставить отзыв",
        "restart_bot": "🔄 Перезапустить Бота",
        "start_menu": "🚀 Старт",
        "change_language": "🌐 Сменить язык",
        "language_selected": "✅ Язык выбран!",
        "rating_prompt": "⭐ Сколько звёзд ты поставишь? (1-5)",
        "comment_prompt": "💬 Пожалуйста, напишите отзыв!",
        "thank_you": "👏 Спасибо! Отзыв записан! ✅",
        "error_saving": "🚫 Ошибка при сохранении.",
        "server_error": "🚫 Сервер не отвечает...",
        "invalid_rating": "👇 Введите число от 1 до 5, пожалуйста!",
    },
    "en": {
        "start": "Hello 👋! Press the button below to leave a review 💬👇",
        "choose_language": "Please, choose a language 🌐",
        "leave_feedback": "💬 ⭐ Share your feedback",
        "restart_bot": "🔄 Restart Bot",
        "start_menu": "🚀 Start",
        "change_language": "🌐 Change language",
        "language_selected": "✅ Language selected!",
        "rating_prompt": "⭐ How many stars would you give? (1-5)",
        "comment_prompt": "💬 Please write a few words!",
        "thank_you": "👏 Thank you! Your review has been recorded ✅",
        "error_saving": "🚫 Error saving your review.",
        "server_error": "🚫 Server is not responding...",
        "invalid_rating": "👇 Please enter a number from 1 to 5!",
    },
    "uz": {
        "start": "Salom 👋! Quyidagi tugmani bosib sharh qoldiring 💬👇",
        "choose_language": "Iltimos, tilni tanlang 🌐",
        "leave_feedback": "💬 ⭐ Fikr bildiring",
        "restart_bot": "🔄 Botni qayta boshlash",
        "start_menu": "🚀 Start",
        "change_language": "🌐 Tilni almashtirish",
        "language_selected": "✅ Til tanlandi!",
        "rating_prompt": "⭐ Necha yulduz berasiz? (1-5)",
        "comment_prompt": "💬 Iltimos, fikringizni yozing!",
        "thank_you": "👏 Rahmat! Fikringiz yozib olindi ✅",
        "error_saving": "🚫 Saqlashda xatolik yuz berdi.",
        "server_error": "🚫 Server javob bermayapti...",
        "invalid_rating": "👇 Iltimos, 1 dan 5 gacha bo'lgan raqamni kiriting!",
    },
}


# ================== ФУНКЦИИ ==================


# Получение языка пользователя (пока запоминаем только в FSM)
async def get_user_lang(state: FSMContext) -> str:
    data = await state.get_data()
    return data.get("lang", "ru")  # по умолчанию русский


# Получение аватарки Telegram-пользователя
async def get_user_avatar_url(user_id: int) -> str | None:
    try:
        photos = await bot.get_user_profile_photos(user_id, limit=1)
        if photos.total_count == 0:
            return None
        file_id = photos.photos[0][-1].file_id
        file = await bot.get_file(file_id)
        return f"https://api.telegram.org/file/bot{bot.token}/{file.file_path}"
    except Exception as e:
        print(f"Ошибка при получении фото: {e}")
        return None


# Главное меню
async def show_main_menu(message: types.Message, state: FSMContext):
    lang = await get_user_lang(state)
    buttons = [
        [KeyboardButton(text=LANGUAGES[lang]["leave_feedback"])],
        [KeyboardButton(text=LANGUAGES[lang]["restart_bot"])],
        [KeyboardButton(text=LANGUAGES[lang]["start_menu"])],
        [KeyboardButton(text=LANGUAGES[lang]["change_language"])],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer(LANGUAGES[lang]["start"], reply_markup=keyboard)


# Старт /start
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await state.update_data(lang="ru")
    await show_main_menu(message, state)


# Перезапуск бота
async def restart(message: types.Message, state: FSMContext):
    await state.clear()
    await show_main_menu(message, state)


# Сменить язык
async def choose_language(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇷🇺 Русский"),
                KeyboardButton(text="🇬🇧 English"),
                KeyboardButton(text="🇺🇿 O'zbek"),
            ]
        ],
        resize_keyboard=True,
    )
    lang = await get_user_lang(state)
    await message.answer(LANGUAGES[lang]["choose_language"], reply_markup=keyboard)


# Обработка выбора языка
async def process_language(message: types.Message, state: FSMContext):
    lang_map = {
        "Русский": "ru",
        "English": "en",
        "O'zbek": "uz",
    }
    text = message.text.replace("🇷🇺 ", "").replace("🇬🇧 ", "").replace("🇺🇿 ", "")
    lang = lang_map.get(text)

    if lang:
        await state.update_data(lang=lang)
        await message.answer(LANGUAGES[lang]["language_selected"])
        await show_main_menu(message, state)
    else:
        await message.answer("❗ Пожалуйста, выбери язык из предложенных вариантов.")


# Нажал Оставить отзыв
async def begin_feedback(message: types.Message, state: FSMContext):
    lang = await get_user_lang(state)
    await message.answer(LANGUAGES[lang]["rating_prompt"])
    await state.set_state(ReviewStates.waiting_for_rating)


# Ввод рейтинга
async def process_rating(message: types.Message, state: FSMContext):
    lang = await get_user_lang(state)
    if not message.text.isdigit() or not (1 <= int(message.text) <= 5):
        await message.answer(LANGUAGES[lang]["invalid_rating"])
        return
    await state.update_data(rating=int(message.text))
    await message.answer(LANGUAGES[lang]["comment_prompt"])
    await state.set_state(ReviewStates.waiting_for_comment)


# Ввод комментария
async def process_comment(message: types.Message, state: FSMContext):
    lang = await get_user_lang(state)
    user_data = await state.get_data()
    photo_url = None

    # Получаем URL аватарки Telegram
    try:
        photos = await bot.get_user_profile_photos(
            user_id=message.from_user.id, limit=1
        )
        if photos.total_count > 0:
            file_id = photos.photos[0][-1].file_id
            file = await bot.get_file(file_id)
            photo_url = await upload_telegram_avatar_to_backend(
                telegram_id=message.from_user.id, file_path=file.file_path
            )
    except Exception as e:
        print(f"[AVATAR ERROR] ⚠️ Ошибка при загрузке авы на backend: {e}")

    # Получаем текст отзыва и очищаем пробелы
    text = message.text.strip() if message.text else ""

    # Проверяем, что пользователь действительно что-то ввёл (включая эмодзи)
    if not text:
        await message.answer(LANGUAGES[lang]["comment_prompt"])
        return

    data = {
        "telegram_id": message.from_user.id,
        "username": message.from_user.username,
        "full_name": message.from_user.full_name,
        "photo_url": photo_url,
        "rating": user_data["rating"],
        "message": message.text,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BACKEND_URL}/api/telegram-reviews/", json=data
            )
        if response.status_code == 200:
            await message.answer(LANGUAGES[lang]["thank_you"])
        else:
            await message.answer(LANGUAGES[lang]["error_saving"])
    except Exception as e:
        print(f"[BOT ERROR]: {e}")
        await message.answer(LANGUAGES[lang]["server_error"])

    await show_main_menu(message, state)


# ================== Регистрация ==================
def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())
    dp.message.register(restart, lambda m: m.text.lower() == "/restart")
    dp.message.register(start, lambda m: m.text.lower() == "/start")
    dp.message.register(
        restart, lambda m: "Перезапустить" in m.text or "Restart" in m.text
    )
    dp.message.register(show_main_menu, lambda m: "🚀" in m.text)
    dp.message.register(
        choose_language,
        lambda m: any(
            m.text == LANGUAGES[lang]["change_language"] for lang in LANGUAGES
        ),
    )
    dp.message.register(
        process_language,
        lambda m: m.text.startswith("🇷")
        or m.text.startswith("🇬")
        or m.text.startswith("🇺"),
    )
    dp.message.register(
        begin_feedback,
        lambda m: any(
            word in m.text for word in ["Оставить", "Share", "Fikr", "💬", "⭐"]
        ),
    )
    dp.message.register(process_rating, ReviewStates.waiting_for_rating)
    dp.message.register(process_comment, ReviewStates.waiting_for_comment)
