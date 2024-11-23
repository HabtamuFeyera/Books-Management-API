import pytest
from src.service.authors_service import get_authors, get_author, create_author, replace_author, modify_author, delete_author
from src.fake.data import authors_data
from src.model.authors import Author

# Sample author data for testing
sample_author = {
    "name": "Sample Author",
    "birth_year": 1980
}

# Test get_authors() service method
def test_get_authors():
    authors = get_authors()
    assert len(authors) > 0  # Ensure authors list is not empty

# Test get_author() service method
def test_get_author():
    # Create an author first
    created_author = create_author(sample_author)
    author = get_author(created_author.id)
    assert author is not None  # Ensure the author exists
    assert author.id == created_author.id  # Ensure correct author is fetched

def test_get_author_not_found():
    author = get_author(999)  # ID that doesn't exist
    assert author is None  # Author should not be found

# Test create_author() service method
def test_create_author():
    created_author = create_author(sample_author)
    assert created_author.name == sample_author['name']  # Check if name matches
    assert created_author.birth_year == sample_author['birth_year']  # Check if birth_year matches

# Test replace_author() service method
def test_replace_author():
    created_author = create_author(sample_author)
    replacement_data = {
        "name": "Replaced Author",
        "birth_year": 1975
    }
    replaced_author = replace_author(created_author.id, replacement_data)
    assert replaced_author is not None
    assert replaced_author.name == "Replaced Author"  # Ensure name was replaced

def test_replace_author_not_found():
    replacement_data = {
        "name": "Replaced Author",
        "birth_year": 1975
    }
    replaced_author = replace_author(999, replacement_data)  # ID that doesn't exist
    assert replaced_author is None  # No author should be replaced

# Test modify_author() service method
def test_modify_author():
    created_author = create_author(sample_author)
    update_data = {
        "birth_year": 1985
    }
    updated_author = modify_author(created_author.id, update_data)
    assert updated_author is not None
    assert updated_author.birth_year == 1985  # Ensure birth_year was updated

# Test delete_author() service method
def test_delete_author():
    created_author = create_author(sample_author)
    deletion_result = delete_author(created_author.id)
    assert deletion_result is True  # Ensure author was deleted successfully
    author = get_author(created_author.id)
    assert author is None  # Ensure author is not found after deletion

def test_delete_author_not_found():
    deletion_result = delete_author(999)  # ID that doesn't exist
    assert deletion_result is False  # No author should be deleted
