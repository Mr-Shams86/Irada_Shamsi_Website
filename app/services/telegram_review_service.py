from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.telegram_review import TelegramReview
from app.schemas.telegram_review import TelegramReviewCreate
from app.schemas.telegram_review import TelegramReviewRead
from app.services.redis_client import redis_client

from datetime import datetime

import json


CACHE_KEY = "latest_telegram_reviews"
CACHE_TTL = 60 * 5  # 5 минут


async def create_review(
    db: AsyncSession, review_data: TelegramReviewCreate
) -> TelegramReview:
    review = TelegramReview(**review_data.dict())
    db.add(review)
    await db.commit()
    await db.refresh(review)
    await redis_client.delete(CACHE_KEY)
    return review


async def get_latest_reviews(db: AsyncSession, offset: int = 0, limit: int = 10):
    # Только если offset == 0 — можно использовать кэш
    if offset == 0:
        cached = await redis_client.get(CACHE_KEY)
        if cached:
            cached_reviews = json.loads(cached)
            return [TelegramReviewRead(**cr) for cr in cached_reviews]

    # В остальных случаях — обычный запрос без кэша
    result = await db.execute(
        select(TelegramReview)
        .where(TelegramReview.is_approved == True)
        .order_by(TelegramReview.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    reviews = result.scalars().all()

    # Кэшируем только первую страницу
    if offset == 0:

        def json_serial(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Type {type(obj)} not serializable")

        serialized = [
            {
                "id": r.id,
                "telegram_id": r.telegram_id,
                "username": r.username,
                "full_name": r.full_name,
                "rating": r.rating,
                "message": r.message,
                "photo_url": r.photo_url,
                "created_at": r.created_at,
            }
            for r in reviews
        ]
        await redis_client.set(
            CACHE_KEY, json.dumps(serialized, default=json_serial), ex=CACHE_TTL
        )

    return [TelegramReviewRead.from_orm(r) for r in reviews]
