from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# from dotenv import load_dotenv

# load_dotenv()

if not DATABASE_URL:
    raise ValueError(
        "❌ DATABASE_URL не задан. Убедись, что он указан в Railway → Variables."
    )

# Заменяем async-драйвер на sync-драйвер
if DATABASE_URL.startswith("postgresql+asyncpg://"):
    sync_url = DATABASE_URL.replace(
        "postgresql+asyncpg://", "postgresql+psycopg2://", 1
    )
else:
    sync_url = DATABASE_URL

# Синхронный движок
engine = create_engine(sync_url)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
