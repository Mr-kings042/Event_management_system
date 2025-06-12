from fastapi import HTTPException,status
from schemas.user import UserCreate, UserUpdate
from database import users
from models import User 


class UserCRUD:
    @staticmethod
    def create_user(user_data: UserCreate):
        if any(u.name == user_data.name for u in users.values()):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
            )
        if any(u.email == user_data.email for u in users.values()):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )
        user_id = len(users)+1
        new_user = User(id=user_id, **user_data.model_dump())
        users[user_id] = new_user
        return {"detail": "User created successfully", "user": new_user}                                                                 
    @staticmethod
    def get_users():
        return {"users": list(users.values())}
    

    @staticmethod
    def get_user_by_id(id: int):
        if id not in users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return{"user retrived successfully": users[id]}
    
    @staticmethod
    def update_user(id: int, user: UserUpdate):
        update_user = users.get(id)
        if not update_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {id} not found"
            )
        for field, value in user.model_dump(exclude_unset=True).items():
            setattr(update_user, field, value)
        
        return {"detail": "User updated successfully", "user": update_user}
    @staticmethod
    def delete_user(id: int):
        if id not in users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        del users[id]
        return {"detail": "User deleted successfully"}
   

user_crud = UserCRUD()


    