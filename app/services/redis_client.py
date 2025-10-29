import redis.asyncio as redis
from app.config import REDISHOST
from app.config import REDISPORT
from app.config import REDIS_PASSWORD


redis_client = redis.Redis(
    host=REDISHOST,
    port=REDISPORT,
    encoding="utf-8",
    decode_responses=True,
    socket_connect_timeout=2.0,
    socket_timeout=2.0,
    retry_on_timeout=True,
    **({"password": REDIS_PASSWORD} if REDIS_PASSWORD else {})
)
