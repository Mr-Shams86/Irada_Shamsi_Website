import redis.asyncio as redis
from app.config import REDISHOST
from app.config import REDISPORT
from app.config import REDIS_PASSWORD


redis_client = redis.Redis(
    host=REDISHOST,
    port=REDISPORT,
    decode_responses=True,
    **({"password": REDIS_PASSWORD} if REDIS_PASSWORD else {})
)
