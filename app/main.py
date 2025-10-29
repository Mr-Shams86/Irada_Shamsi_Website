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
from app.controllers.likes_controller import router as likes_router

from app.services.redis_client import redis_client

from contextlib import asynccontextmanager

from app.dependencies import admin_auth

# from app.database import Base
# from app.database import engine

# from app.utils.custom_static import CustomStaticFiles

from fastapi.staticfiles import StaticFiles

# from dotenv import load_dotenv

# load_dotenv()

# class CSPMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         # Обрабатываем запрос
#         response = await call_next(request)
#         # Убираем установку заголовка Content-Security-Policy
#         return response

IS_PROD = os.getenv("IS_PROD", "false").strip().lower() == "true"

# Определение базовой директории
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Подключение статических файлов
STATIC_DIR = os.getenv("STATIC_DIR", os.path.join(BASE_DIR, "../static"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup — ничего не делаем, клиент уже создан лениво
    yield
    # shutdown — закрыть соединение
    try:
        await redis_client.aclose()
    except Exception:
        pass

app = FastAPI(
    title="Irade Shamsi Portfolio API",
    description="API для добавления и просмотра комментариев",
    version="1.0.0",
    docs_url=None if IS_PROD else "/docs",
    redoc_url=None if IS_PROD else "/redoc",
    openapi_url=None if IS_PROD else "/openapi.json",
    lifespan=lifespan,
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Создаём папку, если её нет
os.makedirs(os.path.join(STATIC_DIR, "images", "review_avatars"), exist_ok=True)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Middleware
app.add_middleware(XFrameOptionsMiddleware)
app.add_middleware(XContentTypeOptionsMiddleware)
app.add_middleware(HSTSMiddleware)

# Роуты
app.include_router(root_router)
app.include_router(telegram_review_router)
app.include_router(admin_reviews_router)
app.include_router(admin_auth.router)
app.include_router(likes_router)


# Создание базы данных автоматически
# Base.metadata.create_all(bind=engine)
