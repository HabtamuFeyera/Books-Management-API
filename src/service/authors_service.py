from typing import List, Optional
from src.fake.crud import get_all, get_one, create, replace, modify, delete
from src.fake.data import authors_data
from src.model.authors import Author

# Service for fetching all authors
def get_authors() -> List[Author]:
    return get_all(authors_data)

# Service for fetching one author by ID
def get_author(author_id: int) -> Optional[Author]:
    return get_one(authors_data, author_id)

# Service for creating a new author
def create_author(author_data: dict) -> Author:
    return create(authors_data, author_data)

# Service for replacing an existing author by ID
def replace_author(author_id: int, author_data: dict) -> Optional[Author]:
    return replace(authors_data, author_id, author_data)

# Service for partially modifying an existing author by ID
def modify_author(author_id: int, update_data: dict) -> Optional[Author]:
    return modify(authors_data, author_id, update_data)

# Service for deleting an author by ID
def delete_author(author_id: int) -> bool:
    return delete(authors_data, author_id)
