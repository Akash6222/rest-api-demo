from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=List[UserResponse])
def get_users():
    """Retrieve all users."""
    return UserService.get_all_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Retrieve a specific user by ID."""
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    """Create a new user."""
    return UserService.create_user(user)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    """Update an existing user."""
    updated_user = UserService.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    """Delete a user."""
    deleted = UserService.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None
