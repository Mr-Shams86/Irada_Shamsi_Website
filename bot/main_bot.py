import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.bot_instance import bot
from bot.handlers import register_handlers


logging.basicConfig(level=logging.INFO)


dp = Dispatcher(storage=MemoryStorage())
register_handlers(dp)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    print("🤖 Irada Feedback Bot запущен и ждёт ваших отзывов! Добро пожаловать! 🚀")
