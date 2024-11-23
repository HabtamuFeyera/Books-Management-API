import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

import pytest
from src.service.books_service import get_books, get_book, create_book, replace_book, modify_book, delete_book
from src.fake.data import books_data
from src.model.books import Book


# Sample book data for testing
sample_book = {
    "title": "Sample Book",
    "author_id": 1,
    "published_year": 2021,
    "genre": "Fiction"
}

# Test get_books() service method
def test_get_books():
    books = get_books()
    assert len(books) > 0  # Ensure books list is not empty

# Test get_book() service method
def test_get_book():
    # Create a book first
    created_book = create_book(sample_book)
    book = get_book(created_book.id)
    assert book is not None  # Ensure the book exists
    assert book.id == created_book.id  # Ensure correct book is fetched

def test_get_book_not_found():
    book = get_book(999)  # ID that doesn't exist
    assert book is None  # Book should not be found

# Test create_book() service method
def test_create_book():
    created_book = create_book(sample_book)
    assert created_book.title == sample_book['title']  # Check if title matches
    assert created_book.author_id == sample_book['author_id']  # Check if author_id matches

# Test replace_book() service method
def test_replace_book():
    created_book = create_book(sample_book)
    replacement_data = {
        "title": "Replaced Book",
        "author_id": 2,
        "published_year": 2022,
        "genre": "Mystery"
    }
    replaced_book = replace_book(created_book.id, replacement_data)
    assert replaced_book is not None
    assert replaced_book.title == "Replaced Book"  # Ensure title was replaced

def test_replace_book_not_found():
    replacement_data = {
        "title": "Replaced Book",
        "author_id": 2,
        "published_year": 2022,
        "genre": "Mystery"
    }
    replaced_book = replace_book(999, replacement_data)  # ID that doesn't exist
    assert replaced_book is None  # No book should be replaced

# Test modify_book() service method
def test_modify_book():
    created_book = create_book(sample_book)
    update_data = {
        "genre": "Science Fiction"
    }
    updated_book = modify_book(created_book.id, update_data)
    assert updated_book is not None
    assert updated_book.genre == "Science Fiction"  # Ensure genre was updated

# Test delete_book() service method
def test_delete_book():
    created_book = create_book(sample_book)
    deletion_result = delete_book(created_book.id)
    assert deletion_result is True  # Ensure book was deleted successfully
    book = get_book(created_book.id)
    assert book is None  # Ensure book is not found after deletion

def test_delete_book_not_found():
    deletion_result = delete_book(999)  # ID that doesn't exist
    assert deletion_result is False  # No book should be deleted
