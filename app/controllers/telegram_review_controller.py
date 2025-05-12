from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import Form
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi.responses import JSONResponse

import shutil

from sqlalchemy.ext.asyncio import AsyncSession

from pathlib import Path

from typing import List

from app.schemas.telegram_review import TelegramReviewCreate
from app.schemas.telegram_review import TelegramReviewRead
from app.services.telegram_review_service import create_review
from app.services.telegram_review_service import get_latest_reviews
from app.database import get_db

router = APIRouter(prefix="/api/telegram-reviews", tags=["Telegram Reviews"])


@router.post("/", response_model=TelegramReviewRead)
async def add_review(review: TelegramReviewCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_review(db, review)
    except Exception as e:
        print(f"🔥 Ошибка при добавлении отзыва: {e}")
        raise HTTPException(
            status_code=500, detail=f"Ошибка при сохранении отзыва: {str(e)}"
        )


@router.get("/", response_model=List[TelegramReviewRead])
async def list_reviews(
    db: AsyncSession = Depends(get_db),
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50),
):
    try:
        return await get_latest_reviews(db, offset=offset, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Ошибка при получении отзывов: {str(e)}"
        )


@router.post("/avatar")
async def upload_avatar(file: UploadFile, filename: str = Form(...)):
    avatars_dir = Path("/static/images/review_avatars")
    avatars_dir.mkdir(parents=True, exist_ok=True)

    save_path = avatars_dir / filename

    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"photo_url": f"/static/images/review_avatars/{filename}"}
