from fastapi import APIRouter, Query
from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

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
def serve_homepage(request: Request, lang: str = Query("en")):
    file_name = f"index-{lang}.html"
    try:
        return templates.TemplateResponse(file_name, {"request": request})
    except FileExistsError:
        return HTMLResponse(content="Page not found", status_code=404)


@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/images/favicon.ico")
