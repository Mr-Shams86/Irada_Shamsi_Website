# app/services/like_service.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.like import PortfolioLike

async def get_count(db: AsyncSession, work_id: str) -> int:
    row = await db.get(PortfolioLike, work_id)
    return row.count if row else 0

async def up(db: AsyncSession, work_id: str) -> int:
    row = await db.get(PortfolioLike, work_id)
    if row:
        row.count += 1
    else:
        row = PortfolioLike(id=work_id, count=1)
        db.add(row)
    await db.commit()
    await db.refresh(row)
    return row.count

async def down(db: AsyncSession, work_id: str) -> int:
    row = await db.get(PortfolioLike, work_id)
    if not row:
        return 0
    if row.count > 0:
        row.count -= 1
        await db.commit()
        await db.refresh(row)
    return row.count


async def add_like(db: AsyncSession, like_id: str) -> int:
    return await up(db, like_id)

