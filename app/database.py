import os

# from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Загрузка .env
# load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не задан в .env файле")

# Проверка на наличие async-драйвера
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=False)

# Базовый класс для моделей
Base = declarative_base()

# Асинхронная сессия
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


# Зависимость для FastAPI
async def get_db():
    async with async_session() as session:
        yield session
