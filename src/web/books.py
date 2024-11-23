from fastapi import APIRouter, HTTPException
from typing import List, Optional

# Import the fake CRUD functions and models
from src.fake.crud import get_all, get_one, create, replace, modify, delete
from src.fake.data import books_data
from src.model.books import Book

router = APIRouter()

# Get all books
@router.get("/books", response_model=List[Book])
async def get_books():
    return get_all(books_data)

# Get one book by ID
@router.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    book = get_one(books_data, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Create a new book
@router.post("/books", response_model=Book)
async def create_book(book: Book):
    new_book = book.dict()
    return create(books_data, new_book)

# Replace an existing book by ID
@router.put("/books/{book_id}", response_model=Book)
async def replace_book(book_id: int, book: Book):
    new_book = book.dict()
    updated_book = replace(books_data, book_id, new_book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

# Modify an existing book partially
@router.patch("/books/{book_id}", response_model=Book)
async def modify_book(book_id: int, book: Book):
    updated_book = modify(books_data, book_id, book.dict(exclude_unset=True))
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

# Delete a book by ID
@router.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    if not delete(books_data, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
