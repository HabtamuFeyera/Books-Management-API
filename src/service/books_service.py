from typing import List, Optional
from src.fake.crud import get_all, get_one, create, replace, modify, delete
from src.fake.data import books_data
from src.model.books import Book

# Service for fetching all books
def get_books() -> List[Book]:
    return get_all(books_data)

# Service for fetching one book by ID
def get_book(book_id: int) -> Optional[Book]:
    return get_one(books_data, book_id)

# Service for creating a new book
def create_book(book_data: dict) -> Book:
    return create(books_data, book_data)

# Service for replacing an existing book by ID
def replace_book(book_id: int, book_data: dict) -> Optional[Book]:
    return replace(books_data, book_id, book_data)

# Service for partially modifying an existing book by ID
def modify_book(book_id: int, update_data: dict) -> Optional[Book]:
    return modify(books_data, book_id, update_data)

# Service for deleting a book by ID
def delete_book(book_id: int) -> bool:
    return delete(books_data, book_id)
