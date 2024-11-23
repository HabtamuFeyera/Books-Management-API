from fastapi import APIRouter, HTTPException
from typing import List, Optional

# Import the fake CRUD functions and models
from src.fake.crud import get_all, get_one, create, replace, modify, delete
from src.fake.data import authors_data
from src.model.authors import Author

router = APIRouter()

# Get all authors
@router.get("/authors", response_model=List[Author])
async def get_authors():
    return get_all(authors_data)

# Get one author by ID
@router.get("/authors/{author_id}", response_model=Author)
async def get_author(author_id: int):
    author = get_one(authors_data, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

# Create a new author
@router.post("/authors", response_model=Author)
async def create_author(author: Author):
    new_author = author.dict()
    return create(authors_data, new_author)

# Replace an existing author by ID
@router.put("/authors/{author_id}", response_model=Author)
async def replace_author(author_id: int, author: Author):
    new_author = author.dict()
    updated_author = replace(authors_data, author_id, new_author)
    if updated_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated_author

# Modify an existing author partially
@router.patch("/authors/{author_id}", response_model=Author)
async def modify_author(author_id: int, author: Author):
    updated_author = modify(authors_data, author_id, author.dict(exclude_unset=True))
    if updated_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated_author

# Delete an author by ID
@router.delete("/authors/{author_id}", response_model=Author)
async def delete_author(author_id: int):
    if not delete(authors_data, author_id):
        raise HTTPException(status_code=404, detail="Author not found")
    return {"message": "Author deleted successfully"}
