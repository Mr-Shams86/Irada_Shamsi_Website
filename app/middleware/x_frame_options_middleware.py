from starlette.middleware.base import BaseHTTPMiddleware


# Middleware для X-Frame-Options
class XFrameOptionsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Frame-Options"] = "DENY"
        return response
