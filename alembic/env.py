import os
import sys
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy import create_engine

# from dotenv import load_dotenv

# === 🔧 Загрузка .env ===
# load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# === 📁 Добавление пути к папке app ===
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# === 📦 Импорт базы и моделей из sync-версии ===
from app.database_sync import Base, DATABASE_URL
from app.models.comment import CommentDB  # если используется в metadata

# === ⚙️ Alembic config и логирование ===
config = context.config
fileConfig(config.config_file_name)

# === 🧠 Метаданные моделей ===
target_metadata = Base.metadata

# === 🔄 Получение DATABASE_URL и принудительная замена asyncpg → psycopg2 ===
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не найден в .env")

# Заменяем драйвер async → sync
if DATABASE_URL.startswith("postgresql+asyncpg://"):
    sync_url = DATABASE_URL.replace(
        "postgresql+asyncpg://", "postgresql+psycopg2://", 1
    )
else:
    sync_url = DATABASE_URL

# === 🚂 Sync engine для Alembic ===
engine = create_engine(sync_url)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=sync_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
