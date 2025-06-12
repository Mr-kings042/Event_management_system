from fastapi import HTTPException, status
from database import users


class UserService:
    @staticmethod
    def deactivate_user(id: int):
        if id not in users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found")
        
        if not users[id].is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already deactivated")
        users[id].is_active = False
        return {"detail": f"User {users[id].name} with ID {id} deactivated successfully"}
    
user_service = UserService()