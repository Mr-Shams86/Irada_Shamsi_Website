#!/usr/bin/env sh
set -e

echo "▶ Running Alembic migrations against: $DATABASE_URL"
alembic upgrade head

echo "▶ Starting Uvicorn…"
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
