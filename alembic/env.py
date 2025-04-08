import sys
import os
from logging.config import fileConfig
from alembic import context
from sqlalchemy import pool
from dotenv import load_dotenv
from pathlib import Path

# Загружаем .env
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# Добавляем путь к app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Импортируем базу и модели
from app.database import engine
from app.database import Base
from app.models.comment import CommentDB

# Получаем конфигурацию Alembic
config = context.config
# Интерпретируем config file для логирования
fileConfig(config.config_file_name)

# Целевая мета — наши модели
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = os.getenv("DATABASE_URL")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Используем engine из проекта (тот же, что и FastAPI)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
