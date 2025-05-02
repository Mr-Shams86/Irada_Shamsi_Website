from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import BigInteger
from sqlalchemy.sql import func

# from app.database_sync import Base

from app.database import Base


class TelegramReview(Base):
    __tablename__ = "telegram_reviews"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, nullable=False)
    username = Column(String(100), nullable=True)
    full_name = Column(String(100), nullable=True)
    photo_url = Column(String(255), nullable=True)
    rating = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    is_approved = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
