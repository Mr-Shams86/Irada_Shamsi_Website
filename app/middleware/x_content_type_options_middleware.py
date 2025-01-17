from starlette.middleware.base import BaseHTTPMiddleware


# Middleware для X-Content-Type-Options
class XContentTypeOptionsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response
