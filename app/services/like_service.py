# app/services/like_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.dialects.postgresql import insert

from app.models.like import PortfolioLike

async def get_count(db: AsyncSession, work_id: str) -> int:
    stmt = select(PortfolioLike.count).where(PortfolioLike.id == work_id)
    val = await db.scalar(stmt)
    return int(val or 0)

async def up(db: AsyncSession, work_id: str) -> int:
    stmt = (
        insert(PortfolioLike)
        .values(id=work_id, count=1)
        .on_conflict_do_update(
            index_elements=[PortfolioLike.id],
            set_={"count": PortfolioLike.count + 1},
        )
        .returning(PortfolioLike.count)
    )
    new_count = await db.scalar(stmt)
    await db.commit()
    return int(new_count)

async def down(db: AsyncSession, work_id: str) -> int:
    # создаём запись при первом «down», но не уходим в минус
    stmt = (
        insert(PortfolioLike)
        .values(id=work_id, count=0)
        .on_conflict_do_update(
            index_elements=[PortfolioLike.id],
            set_={"count": func.greatest(PortfolioLike.count - 1, 0)},
        )
        .returning(PortfolioLike.count)
    )
    new_count = await db.scalar(stmt)
    await db.commit()
    return int(new_count)
