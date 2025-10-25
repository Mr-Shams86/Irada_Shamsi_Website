from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.services.like_service import get_count, up, down

router = APIRouter(prefix="/api/likes", tags=["Likes"])

@router.get("/{work_id}")
async def api_get_likes(work_id: str, db: AsyncSession = Depends(get_db)):
    return {"id": work_id, "count": await get_count(db, work_id)}

@router.post("/{work_id}/up")
async def api_like_up(work_id: str, db: AsyncSession = Depends(get_db)):
    return {"id": work_id, "count": await up(db, work_id)}

@router.post("/{work_id}/down")
async def api_like_down(work_id: str, db: AsyncSession = Depends(get_db)):
    cnt = await down(db, work_id)
    if cnt < 0:
        raise HTTPException(status_code=400, detail="Invalid state")
    return {"id": work_id, "count": cnt}
