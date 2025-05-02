from pydantic import BaseModel
from pydantic import Field
from typing import Optional
from datetime import datetime


class TelegramReviewBase(BaseModel):
    telegram_id: int
    username: Optional[str] = None
    full_name: Optional[str] = None
    photo_url: Optional[str] = None
    rating: int
    message: str


class TelegramReviewCreate(TelegramReviewBase):
    pass


class TelegramReviewRead(TelegramReviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class TelegramReviewOut(TelegramReviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
