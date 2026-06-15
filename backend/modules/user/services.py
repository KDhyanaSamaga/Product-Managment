from sqlalchemy.orm import Session
from repository import UserRepository
from utils.security import verify_password, hash_password
from fastapi import HTTPException
from utils.tokenServices import create_access_token

class UserServices:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def login(self, email: str, password: str):
        user = self.repository.search_by_email(email)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="Email not found."
            )

        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Incorrect Password."
            )

        # Generate the JWT
        token_data = {
            "sub": str(user.id),
            "email": user.email
        }

        # Create the token payload data
        access_token = create_access_token(data=token_data)

        return access_token

    def signup(self, user_data: dict):
        existing_user = self.repository.search_by_email(user_data.get("email"))
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Hash the password
        user_data["hashed_password"] = hash_password(user_data["hashed_password"])
        
        # Save user to db
        new_user = self.repository.create_user(user_data)
        
        # Generate token
        token_data = {
            "sub": str(new_user.id),
            "email": new_user.email
        }
        access_token = create_access_token(data=token_data)
        
        return access_token, new_user

   # def reset_password(self,old_password:str,new_password:str):
