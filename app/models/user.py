# In a real application, this would contain SQLAlchemy or other ORM models.
# For this in-memory demo, we just store the data structure here.
from typing import Dict, Any

# Mock database table
users_db: Dict[int, Dict[str, Any]] = {
    1: {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "is_active": True},
    2: {"id": 2, "name": "Bob Jones", "email": "bob@example.com", "is_active": False}
}

# Auto-incrementing ID tracker
def get_next_id() -> int:
    if not users_db:
        return 1
    return max(users_db.keys()) + 1
