#!/usr/bin/env sh
set -e

echo "► Running Alembic migrations against: $DATABASE_URL"
# не валим контейнер, если миграция вдруг не прошла — пишем в лог и идём дальше
alembic upgrade head || echo "!!! Alembic failed (see logs), starting app anyway"

echo "► Starting Uvicorn…"
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
