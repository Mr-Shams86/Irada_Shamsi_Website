import asyncio
import sys
import os
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from dotenv import load_dotenv


# Загружаем .env
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# Добавляем путь к app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Импортируем базу и модели
from app.models.comment import ComentDB
from app.database import Base

# Получаем конфигурацию Alembic
config = context.config

# Интерпретируем config file для логирования
fileConfig(config.config_file_name)

# Метаданные моделей
target_metadata = Base.metadata

# Получаем async URL
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Создаем асинхронное движение
engine = create_async_engine(DATABASE_URL, echo=False)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode with async engine."""
    # Используем engine из проекта (тот же, что и FastAPI)
    async with engine.begin() as conn:
        await conn.run_sync(
            lambda sync_conn: context.cofigure(
                connection=sync_conn,
                target_metadata=target_metadata,
                compare_type=True,
            )
        )

        await conn.run_sync(context.run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
