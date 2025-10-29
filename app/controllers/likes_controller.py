# app/controllers/likes_controller.py
from fastapi import APIRouter, Depends, HTTPException, Request
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Dict, List

from app.database import get_db
from app.models.like import PortfolioLike
from app.services.redis_client import redis_client as redis
from app.services.like_service import get_count, up, down

from redis.exceptions import RedisError

router = APIRouter(prefix="/api/likes", tags=["Likes"])
logger = logging.getLogger(__name__)

TTL = 300  # 5 минут
ANTI_SPAM_TTL = 24 * 60 * 60  # 24 часа

def key_like(pid: str) -> str:
    return f"likes:{pid}"

def key_vote_guard(pid: str, fp: str, action: str) -> str:
    # action: "up" or "down"
    return f"like-guard:{pid}:{fp}:{action}"

async def cache_set_many(pairs: Dict[str, int], ttl: int = TTL) -> None:
    if not pairs:
        return
    # безопасно закрываем асинхронный пайплайн
    async with redis.pipeline(transaction=False) as pipe:
        for k, v in pairs.items():
            pipe.setex(k, ttl, int(v))
        await pipe.execute()

@router.get("/bulk")
async def api_get_likes_bulk(ids: str, db: AsyncSession = Depends(get_db)) -> Dict[str, int]:
    # 1) нормализуем вход: убираем пустые и дубликаты, сохраняем порядок
    raw_ids = [i.strip() for i in (ids or "").split(",") if i.strip()]
    uniq_ids = list(dict.fromkeys(raw_ids))
    if not uniq_ids:
        return {}

    # 2) пробуем достать из Redis
    keys = [key_like(i) for i in uniq_ids]
    cached = await redis.mget(keys)  # list[str|None]
    result: Dict[str, int] = {}
    missing: List[str] = []

    for pid, val in zip(uniq_ids, cached):
        if val is None:
            missing.append(pid)
        else:
            try:
                result[pid] = int(val)
            except (TypeError, ValueError):
                # мусор в кеше — считаем как отсутствующий, подтянем из БД
                missing.append(pid)

    # 3) достать из БД недостающие
    if missing:
        rows = (await db.execute(
            select(PortfolioLike.id, PortfolioLike.count)
            .where(PortfolioLike.id.in_(missing))
        )).all()

        to_cache: Dict[str, int] = {}
        present = set()
        for pid, cnt in rows:
            c = int(cnt or 0)
            result[pid] = c
            to_cache[key_like(pid)] = c
            present.add(pid)

        # тех, кого нет в БД — считаем нулями и тоже кладём в кеш
        for pid in missing:
            if pid not in present:
                result[pid] = 0
                to_cache[key_like(pid)] = 0

        await cache_set_many(to_cache, TTL)

    return result

@router.get("/{work_id}")
async def api_get_like(work_id: str, db: AsyncSession = Depends(get_db)):
    try:
        val = await redis.get(key_like(work_id))
        if val is not None:
            return {"id": work_id, "count": int(val)}
    except RedisError as e:
        logger.warning("Redis GET failed for %s: %s", work_id, e)

    cnt = await get_count(db, work_id)
    # необязательно: пробуем прогреть кеш, но ошибки игнорим
    try:
        await redis.setex(key_like(work_id), TTL, cnt)
    except RedisError:
        pass
    return {"id": work_id, "count": cnt}

def _fingerprint(req: Request) -> str:
    # лёгкий отпечаток (без PII): ip + ua, можно усилить HMAC(secret)
    ip = (req.headers.get("x-forwarded-for") or (req.client.host if req.client else "") or "").split(",")[0].strip()
    ua = (req.headers.get("user-agent") or "").lower()[:80]
    return f"{ip}:{ua}"

async def _guard_once_per_day(pid: str, fp: str, action: str) -> bool:
    # True -> действие разрешено (ключ поставлен впервые для этого pid+fp+action)
    # False -> уже голосовал сегодня
    return bool(await redis.set(key_vote_guard(pid, fp, action), "1", ex=ANTI_SPAM_TTL, nx=True))

async def _touch_cache(pid: str, cnt: int) -> None:
    try:
        await redis.setex(key_like(pid), TTL, int(cnt))
    except Exception as e:
        # Логируем и не валим запрос
        logger.warning("Failed to touch cache for %s: %s", pid, e)
        pass

@router.post("/{work_id}/up")
async def api_like_up(work_id: str, request: Request, db: AsyncSession = Depends(get_db)):
    fp = _fingerprint(request)
    if not await _guard_once_per_day(work_id, fp, "up"):
        # мягко возвращаем текущий счётчик — без 400
        cnt = await get_count(db, work_id)
        await _touch_cache(work_id, cnt)
        return {"id": work_id, "count": cnt, "guard": "already-voted"}

    cnt = await up(db, work_id)
    await _touch_cache(work_id, cnt)
    return {"id": work_id, "count": cnt}

@router.post("/{work_id}/down")
async def api_like_down(work_id: str, request: Request, db: AsyncSession = Depends(get_db)):
    fp = _fingerprint(request)
    if not await _guard_once_per_day(work_id, fp, "down"):
        cnt = await get_count(db, work_id)
        await _touch_cache(work_id, cnt)
        return {"id": work_id, "count": cnt, "guard": "already-voted"}

    cnt = await down(db, work_id)
    if cnt < 0:
        # на всякий — не даём уйти в минус
        raise HTTPException(status_code=400, detail="Invalid state")
    await _touch_cache(work_id, cnt)
    return {"id": work_id, "count": cnt}

