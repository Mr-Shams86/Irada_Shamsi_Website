# from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# Проверка переменной окружения
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL не задан. Проверь Railway → Variables")

# Если формат "postgresql://" — заменим на async
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Создаём async engine
engine = create_async_engine(DATABASE_URL, echo=False)

# Базовый класс моделей
Base = declarative_base()

# Асинхронная сессия
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


# Зависимость FastAPI
async def get_db():
    async with async_session() as session:
        yield session
