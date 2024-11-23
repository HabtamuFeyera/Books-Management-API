import pytest
import sys
import os

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))

import pytest
from src.service.books_service import get_books, replace_book, modify_book, delete_book
from src.fake.data import books_data  # Assuming you have some fake data for testing
# test_books.py or equivalent test file

from src.service.books_service import get_books, get_book, replace_book, modify_book, delete_book

# Test for fetching books
def test_get_books():
    books_data.clear()  # Ensure the data is in a known state for the test
    books_data.extend([
        {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author_id": 1, "publication_year": 1997, "genre": "Fantasy", "summary": "A young wizard discovers his magical heritage."},
        {"id": 2, "title": "The Hobbit", "author_id": 2, "publication_year": 1937, "genre": "Fantasy", "summary": "Bilbo Baggins goes on an unexpected adventure."},
    ])
    books = get_books()
    assert len(books) == 2  # Should return two books

# Test for replacing a book
def test_replace_book():
    new_data = {"id": 1, "title": "Updated Book One", "author_id": 1, "publication_year": 2023, "genre": "Fantasy", "summary": "Updated summary of the book."}
    updated_book = replace_book(1, new_data)
    assert updated_book is not None
    assert updated_book.title == "Updated Book One"
    assert updated_book.summary == "Updated summary of the book."

# Test for modifying a book
def test_modify_book():
    update_data = {"title": "Partially Updated Book One", "genre": "Adventure", "summary": "Partially updated summary"}
    modified_book = modify_book(1, update_data)
    assert modified_book is not None
    assert modified_book.title == "Partially Updated Book One"
    assert modified_book.genre == "Adventure"
    assert modified_book.summary == "Partially updated summary"

# Test for deleting a book
def test_delete_book():
    book_id_to_delete = 1
    result = delete_book(book_id_to_delete)
    assert result is True
    # Verify deletion
    book = get_book(book_id_to_delete)
    assert book is None
