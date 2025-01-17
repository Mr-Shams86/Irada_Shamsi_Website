# Content-Security-Policy Middleware
# from starlette.middleware.base import BaseHTTPMiddleware

# class CSPMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         # Обрабатываем запрос
#         response = await call_next(request)
#         # Убираем установку заголовка Content-Security-Policy
#         return response
