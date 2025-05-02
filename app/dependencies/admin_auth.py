import os
import secrets
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Request
from fastapi import Form
from fastapi import Response
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic
from fastapi.security import HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from app.config import ADMIN_USERNAME
from app.config import ADMIN_PASSWORD


load_dotenv()
security = HTTPBasic()


router = APIRouter()
templates = Jinja2Templates(directory="templates")


def admin_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(
        credentials.username, os.getenv("ADMIN_USERNAME", "admin")
    )
    correct_password = secrets.compare_digest(
        credentials.password, os.getenv("ADMIN_PASSWORD", "admin")
    )

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True


@router.post("/admin/login", response_class=HTMLResponse)
async def login_post(
    request: Request,
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        redirect = RedirectResponse(url="/admin/reviews", status_code=302)
        redirect.set_cookie("admin_auth", "true", httponly=True)
        return redirect

    # ❌ Неверные данные — возвращаем шаблон с ошибкой
    return templates.TemplateResponse(
        "admin_login.html",
        {"request": request, "error": "Неверный логин или пароль"},
        status_code=401,
    )


def require_admin_cookie(request: Request):
    auth_cookie = request.cookies.get("admin_auth")
    if auth_cookie != "true":
        raise HTTPException(status_code=401, detail="Нет доступа. Войдите в админку.")


@router.get("/admin/logout")
async def logout():
    response = RedirectResponse(url="/admin/login", status_code=302)
    response.delete_cookie("admin_auth")
    return response


@router.get("/admin/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})
