from typing import List, Optional
from src.fake.crud import get_all, get_one, create, replace, modify, delete
from src.fake.data import books_data
from src.model.books import Book
# test_books.py or equivalent test file


def get_books() -> list[Book]:
    return [Book(**book) for book in books_data]  # Convert each dict to a Book object

def get_book(book_id: int) -> Optional[Book]:
    book_data = next((book for book in books_data if book["id"] == book_id), None)
    return Book(**book_data) if book_data else None

def replace_book(book_id: int, book_data: dict) -> Optional[Book]:
    # Find the book to replace
    existing_book = next((book for book in books_data if book["id"] == book_id), None)
    if not existing_book:
        return None  # Book not found
    # Replace the book data
    existing_book.update(book_data)
    # Ensure all fields are passed
    updated_book_data = {
        **existing_book,
        "genre": existing_book.get("genre", "Default Genre"),
        "summary": existing_book.get("summary", "No summary available.")
    }
    return Book(**updated_book_data)

def modify_book(book_id: int, update_data: dict) -> Optional[Book]:
    book = get_book(book_id)
    if not book:
        return None
    # Update the book data with the new fields
    updated_book_data = book.dict()  # Convert to dictionary
    updated_book_data.update(update_data)
    # Ensure the genre and summary are not missing
    updated_book_data.setdefault("genre", "Default Genre")
    updated_book_data.setdefault("summary", "No summary available.")
    return Book(**updated_book_data)

def delete_book(book_id: int) -> bool:
    global books_data  # Ensure we modify the original books_data
    book_to_delete = next((book for book in books_data if book["id"] == book_id), None)
    if book_to_delete:
        books_data = [book for book in books_data if book["id"] != book_id]  # Delete the book
        return True
    return False
