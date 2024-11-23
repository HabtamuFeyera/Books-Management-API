from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    id: int
    title: str
    author_id: Optional[int] = None  # Make optional or set default
    publication_year: Optional[int] = None  # Make optional or set default
    genre: str
    summary: str


    class Config:
        orm_mode = True  # Enable compatibility with ORM objects
