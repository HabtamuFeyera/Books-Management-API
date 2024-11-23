from pydantic import BaseModel
from typing import Optional

class Author(BaseModel):
    id: int
    name: str
    biography: Optional[str] = None
    birth_year: Optional[int] = None

    class Config:
        orm_mode = True  # Enable compatibility with ORM objects
