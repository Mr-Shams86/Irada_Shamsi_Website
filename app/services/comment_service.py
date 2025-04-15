import os
import json
from redis import Redis
from app.models.comment import CommentDB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


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


def clear_comments_cache():
    redis_client.delete(CACHE_KEY)
