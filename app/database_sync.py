# app/database_sync.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# from dotenv import load_dotenv

# load_dotenv()

# Получаем переменную из окружения
DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL не задан. Убедись, что он указан в Railway → Variables."
    )


# Подмена asyncpg на psycopg2
if DATABASE_URL.startswith("postgresql+asyncpg://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql+asyncpg://", "postgresql+psycopg2://", 1
    )


# Создание движка и сессии
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
