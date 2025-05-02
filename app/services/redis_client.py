import redis.asyncio as redis
from app.config import REDIS_HOST
from app.config import REDIS_PORT
from app.config import REDIS_PASSWORD


redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    **({"password": REDIS_PASSWORD} if REDIS_PASSWORD else {})
)
