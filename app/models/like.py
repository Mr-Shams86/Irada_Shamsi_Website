# app/models/like.py
from sqlalchemy import Column, Integer, String, CheckConstraint
from app.database_sync import Base

class PortfolioLike(Base):
    __tablename__ = "portfolio_likes"

    # используем имя файла/идентификатор карточки как PK (напр. "portfolio_1.webp")
    id    = Column(String(64), primary_key=True, index=True)
    count = Column(Integer, nullable=False, server_default="0")

    __table_args__ = (
        CheckConstraint('count >= 0', name='ck_portfolio_likes_count_nonneg'),
    )

    def __repr__(self) -> str:
        return f"<PortfolioLike id={self.id!r} count={self.count}>"

