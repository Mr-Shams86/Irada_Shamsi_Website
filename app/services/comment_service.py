import json
from redis import Redis
from app.models.comment import CommentDB
from sqlalchemy.orm import Session


redis_client = Redis(host="redis", port=6379, decode_responses=True)

CACHE_KEY = "comments_cache"


def get_cached_comments(db: Session):
    cached = redis_client.get(CACHE_KEY)
    if cached:
        return json.loads(cached)

    comments = db.query(CommentDB).all()
    serialized = [{"rating": c.rating, "comment": c.comment} for c in comments]
    redis_client.set(CACHE_KEY, json.dumps(serialized), ex=60)  # Кеш на 60 секунд
    return serialized


def clear_comments_cache():
    redis_client.delete(CACHE_KEY)
