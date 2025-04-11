import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# from app.middleware import CSPMiddleware

# app.add_middleware(CSPMiddleware)

from app.middleware import (
    XFrameOptionsMiddleware,  # noqa: F401
    XContentTypeOptionsMiddleware,  # noqa: F401
    HSTSMiddleware,  # noqa: F401
)

from app.controllers.comment_controller import router as comment_router
from app.controllers.root_controller import router as root_router
from app.controllers.admin_controller import router as admin_router
from app.database import Base
from app.database import engine


# class CSPMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         # Обрабатываем запрос
#         response = await call_next(request)
#         # Убираем установку заголовка Content-Security-Policy
#         return response

app = FastAPI(
    title="Irade Shamsi Portfolio API",
    description="API для добавления и просмотра комментариев",
    version="1.0.0",
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
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "../static")),
    name="static",
)


# Подключение роутов
app.include_router(comment_router)
app.include_router(root_router)
app.include_router(admin_router)


# Создание базы данных автоматически
Base.metadata.create_all(bind=engine)
