from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    publication_year: int
    genre: Optional[str] = None
    summary: Optional[str] = None

    class Config:
        orm_mode = True  # Enable compatibility with ORM objects
