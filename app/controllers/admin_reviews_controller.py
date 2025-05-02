from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import status
from fastapi import HTTPException

from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

from sqlalchemy import select
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.templating import Jinja2Templates

from app.database import get_db

from app.models.telegram_review import TelegramReview

from app.services.redis_client import redis_client


router = APIRouter(prefix="/admin/reviews", tags=["Admin Panel"])
templates = Jinja2Templates(directory="templates")


# Проверка авторизации через cookie
def check_admin_cookie(request: Request):
    if request.cookies.get("admin_auth") != "true":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


# Страница админки
@router.get("/", response_class=HTMLResponse)
async def admin_reviews_page(request: Request):
    if request.cookies.get("admin_auth") != "true":
        return RedirectResponse(url="/admin/login")
    return templates.TemplateResponse("admin_reviews.html", {"request": request})


# Получение отзывов на модерацию
@router.get("/list")
async def get_reviews_for_moderation(
    request: Request, db: AsyncSession = Depends(get_db)
):
    check_admin_cookie(request)
    result = await db.execute(
        select(TelegramReview)
        .where(TelegramReview.is_approved == False)
        .order_by(TelegramReview.created_at.desc())
    )
    return result.scalars().all()


# Одобрение отзыва
@router.post("/{review_id}/approve")
async def approve_review(
    review_id: int, request: Request, db: AsyncSession = Depends(get_db)
):
    check_admin_cookie(request)
    review = await db.get(TelegramReview, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    review.is_approved = True
    await db.commit()
    await redis_client.delete("latest_telegram_reviews")
    return {"message": "Одобрено"}


@router.delete("/clear-all", summary="Удалить ВСЕ отзывы")
async def clear_all_reviews(request: Request, db: AsyncSession = Depends(get_db)):
    check_admin_cookie(request)
    result = await db.execute(delete(TelegramReview))
    await db.commit()
    await redis_client.delete("latest_telegram_reviews")
    return {"detail": f"Удалено {result.rowcount} отзывов"}


# Удаление отзыва
@router.delete("/{review_id}")
async def delete_review(
    review_id: int, request: Request, db: AsyncSession = Depends(get_db)
):
    check_admin_cookie(request)
    review = await db.get(TelegramReview, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    await db.delete(review)
    await db.commit()
    await redis_client.delete("latest_telegram_reviews")
    return {"message": "Удалено"}
