from typing import List, Optional
from app.models.user import users_db, get_next_id
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.logger import logger

class UserService:
    @staticmethod
    def get_all_users() -> List[UserResponse]:
        logger.info("Fetching all users")
        return [UserResponse(**user) for user in users_db.values()]

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[UserResponse]:
        logger.info(f"Fetching user with id: {user_id}")
        user = users_db.get(user_id)
        if not user:
            return None
        return UserResponse(**user)

    @staticmethod
    def create_user(user: UserCreate) -> UserResponse:
        logger.info(f"Creating new user with email: {user.email}")
        new_id = get_next_id()
        new_user = {"id": new_id, **user.model_dump()}
        users_db[new_id] = new_user
        return UserResponse(**new_user)

    @staticmethod
    def update_user(user_id: int, user_update: UserUpdate) -> Optional[UserResponse]:
        logger.info(f"Updating user with id: {user_id}")
        if user_id not in users_db:
            return None
            
        existing_user = users_db[user_id]
        update_data = user_update.model_dump(exclude_unset=True)
        existing_user.update(update_data)
        
        return UserResponse(**existing_user)

    @staticmethod
    def delete_user(user_id: int) -> bool:
        logger.info(f"Deleting user with id: {user_id}")
        if user_id in users_db:
            del users_db[user_id]
            return True
        return False
