from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import os
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin Image Management"])

# 💡 Путь к static/images независимо от запуска
IMAGES_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../static/images")
)
SECRET_KEY = "iradeadmin2024"  # Временный ключ для аутентификации


@router.get("/images", response_class=HTMLResponse)
def admin_panel(request: Request):
    try:
        image_files = [
            f
            for f in os.listdir(IMAGES_DIR)
            if f.endswith((".png", ".jpg", ".jpeg", ".webp"))
        ]
        html_content = f"""
        <html><head><title>Управление изображениями</title></head><body>
        <h1>Добавить фото</h1>
        <form action='/admin/upload-image' method='post' enctype='multipart/form-data'>
            <input type='file' name='file'>
            <input type='hidden' name='secret' value='{SECRET_KEY}'>
            <button type='submit'>Загрузить</button>
        </form>
        <h2>Список изображений</h2>
        <ul>
        {''.join(f'<li>{img} <a href="/admin/delete-image/{img}?secret={SECRET_KEY}" style="color:red">Удалить</a></li>' for img in image_files)}
        </ul>
        <a href="/">Вернуться на сайт</a>
        </body></html>
        """
        return HTMLResponse(content=html_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload-image")
def upload_image(secret: str = Form(...), file: UploadFile = File(...)):
    if secret != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Нет доступа")
    try:
        file_location = os.path.join(IMAGES_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        return {"message": f"Файл '{file.filename}' успешно загружен."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/delete-image/{filename}")
def delete_image(filename: str, secret: str = ""):
    if secret != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Нет доступа")
    file_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Файл не найден")
    try:
        os.remove(file_path)
        return JSONResponse(content={"message": f"Файл '{filename}' удален."})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
