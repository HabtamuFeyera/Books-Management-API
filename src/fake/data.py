from typing import List, Dict

# Fake data for authors
authors_data: List[Dict] = [
    {"id": 1, "name": "J.K. Rowling", "biography": "Author of the Harry Potter series.", "birth_year": 1965},
    {"id": 2, "name": "George R.R. Martin", "biography": "Author of A Song of Ice and Fire.", "birth_year": 1948},
]

# Fake data for books
books_data: List[Dict] = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author_id": 1, "publication_year": 1997, "genre": "Fantasy", "summary": "A young wizard discovers his magical heritage."},
    {"id": 2, "title": "A Game of Thrones", "author_id": 2, "publication_year": 1996, "genre": "Fantasy", "summary": "Noble families vie for control of the Iron Throne."},
    {"id": 3, "title": "Harry Potter and the Chamber of Secrets", "author_id": 1, "publication_year": 1998, "genre": "Fantasy", "summary": "The young wizard returns to Hogwarts for his second year."},
]
