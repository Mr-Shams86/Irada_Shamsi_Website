from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.comment import Comment
from app.database import get_db
from app.models.comment import CommentDB

router = APIRouter()


@router.post(
    "/comments",
    response_model=Comment,
    summary="Добавить комментарий",
    description="Добавляет новый комментарий с рейтингом (1-5) и текстом.",
)
def create_comment(comment: Comment, db: Session = Depends(get_db)):
    if not (1 <= comment.rating <= 5):
        raise HTTPException(status_code=400, detail="Рейтинг должен быть от 1 до 5.")

    db_comment = CommentDB(rating=comment.rating, comment=comment.comment)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.get(
    "/comments",
    response_model=List[Comment],
    summary="Получить комментарии",
    description="Возвращает список всех комментариев.",
)
def get_comments(db: Session = Depends(get_db)):
    return db.query(CommentDB).all()


@router.delete(
    "/comments",
    summary="Удалить все комментарии",
    description="Очищает таблицу комментариев в базе данных.",
)
def delete_all_comments(db: Session = Depends(get_db)):
    db.query(CommentDB).delete()
    db.commit()
    return {"message": "Все комментарии удалены."}
