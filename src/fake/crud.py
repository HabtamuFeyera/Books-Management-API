from typing import List, Dict, Optional

# Import the fake data
from src.fake.data import books_data, authors_data

# Get all records
def get_all(data: List[Dict]) -> List[Dict]:
    return data

# Get one record by ID
def get_one(data: List[Dict], record_id: int) -> Optional[Dict]:
    return next((item for item in data if item["id"] == record_id), None)

# Create a new record
def create(data: List[Dict], new_record: Dict) -> Dict:
    data.append(new_record)
    return new_record

# Replace a record completely
def replace(data: List[Dict], record_id: int, new_record: Dict) -> Optional[Dict]:
    for index, item in enumerate(data):
        if item["id"] == record_id:
            data[index] = new_record
            return new_record
    return None

# Modify a record partially
def modify(data: List[Dict], record_id: int, updates: Dict) -> Optional[Dict]:
    for item in data:
        if item["id"] == record_id:
            item.update(updates)
            return item
    return None

# Delete a record by ID
def delete(data: List[Dict], record_id: int) -> bool:
    for index, item in enumerate(data):
        if item["id"] == record_id:
            del data[index]
            return True
    return False
