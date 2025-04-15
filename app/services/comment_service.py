import os
import json
import asyncio
from redis import Redis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.comment import CommentDB

# Подключение к Redis
redis_client = Redis(
    host=os.getenv("REDISHOST", "localhost"),
    port=int(os.getenv("REDISPORT", 6379)),
    password=os.getenv("REDIS_PASSWORD", None),
    decode_responses=True,
)

CACHE_KEY = "comments_cache"


async def get_cached_comments(db: AsyncSession):
    cached = redis_client.get(CACHE_KEY)
    if cached:
        return json.loads(cached)

    result = await db.execute(select(CommentDB))
    comments = result.scalars().all()
    serialized = [{"rating": c.rating, "comment": c.comment} for c in comments]

    redis_client.set(CACHE_KEY, json.dumps(serialized), ex=60)  # Кеш на 60 секунд

    return serialized


# Очистить кеш асинхронно
async def clear_comments_cache():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, redis_client.delete, CACHE_KEY)
