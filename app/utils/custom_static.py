from starlette.staticfiles import StaticFiles


class CustomStaticFiles(StaticFiles):
    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if path.endswith(".webp"):
            response.media_type = "image/webp"
        return response
