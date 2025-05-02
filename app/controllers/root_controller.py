from fastapi import APIRouter
from fastapi import Query
from fastapi import Request
from fastapi import Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.telegram_review_service import get_latest_reviews


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(
    "/api",
    summary="Главная страница API",
    description="Возвращает приветственное сообщение.",
)
def read_root():
    return {"message": "Добро пожаловать на API комментариев Irade Shamsi!"}


@router.get("/", response_class=HTMLResponse, summary="Главная страница")
async def index(
    request: Request,
    lang: str = Query("ru"),
    db: AsyncSession = Depends(get_db),
):
    telegram_reviews = await get_latest_reviews(db=db, limit=10)
    file_name = f"index-{lang}.html"
    return templates.TemplateResponse(
        file_name,
        {
            "request": request,
            "telegram_reviews": telegram_reviews,
        },
    )


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/images/favicon.ico")


@router.get("/robots.txt", include_in_schema=False)
async def robots():
    return FileResponse("static/robots.txt", media_type="text/plain")


@router.get("/sitemap.xml", include_in_schema=False)
async def sitemap():
    return FileResponse("static/sitemap.xml", media_type="application/xml")
