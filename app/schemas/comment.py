from pydantic import BaseModel


class Comment(BaseModel):
    rating: int
    comment: str

    class Config:
        from_attributes = True
