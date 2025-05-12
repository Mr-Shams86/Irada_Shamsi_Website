import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.middleware import CSPMiddleware

# app.add_middleware(CSPMiddleware)

from app.middleware import (
    XFrameOptionsMiddleware,  # noqa: F401
    XContentTypeOptionsMiddleware,  # noqa: F401
    HSTSMiddleware,  # noqa: F401
)

from app.controllers.root_controller import router as root_router
from app.controllers.telegram_review_controller import router as telegram_review_router
from app.controllers.admin_reviews_controller import router as admin_reviews_router

from app.dependencies import admin_auth

# from app.utils.custom_static import CustomStaticFiles

from fastapi.staticfiles import StaticFiles

# from dotenv import load_dotenv

# load_dotenv()


# from app.database import Base
# from app.database import engine


# class CSPMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         # Обрабатываем запрос
#         response = await call_next(request)
#         # Убираем установку заголовка Content-Security-Policy
#         return response

IS_PROD = os.getenv("IS_PROD", "false").strip().lower() == "true"


# Создаём папку, если её нет
os.makedirs("/static/images/review_avatars", exist_ok=True)

app = FastAPI(
    title="Irade Shamsi Portfolio API",
    description="API для добавления и просмотра комментариев",
    version="1.0.0",
    docs_url=None if IS_PROD else "/docs",
    redoc_url=None if IS_PROD else "/redoc",
    openapi_url=None if IS_PROD else "/openapi.json",
)


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Подключение middleware
# app.add_middleware(CSPMiddleware)
app.add_middleware(XFrameOptionsMiddleware)
app.add_middleware(XContentTypeOptionsMiddleware)
app.add_middleware(HSTSMiddleware)


# Определение базовой директории
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Подключение статических файлов
if not IS_PROD:
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(BASE_DIR, "../static")),
        name="static",
    )
else:
    app.mount("/static", StaticFiles(directory="/static"), name="static")


# Подключение роутов
app.include_router(root_router)
app.include_router(telegram_review_router)
app.include_router(admin_reviews_router)
app.include_router(admin_auth.router)

# Создание базы данных автоматически
# Base.metadata.create_all(bind=engine)
