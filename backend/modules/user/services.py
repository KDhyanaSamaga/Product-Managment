from sqlalchemy.orm import Session
from modules.user.repository import UserRepository
from utils.security import verify_password, hash_password
from fastapi import HTTPException
from utils.tokenServices import create_access_token,verify_token

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
        
        # Extract password and generate the hash
        password = user_data.pop("password")
        user_data["hashed_password"] = hash_password(password)
        
        # Save user to db
        new_user = self.repository.create_user(user_data)
        
        # Generate token
        token_data = {
            "sub": str(new_user.id),
            "email": new_user.email
        }
        access_token = create_access_token(data=token_data)
        
        return access_token, new_user

    def reset_password(self, token: str, old_password: str, new_password: str, confirm_password: str):
        if new_password != confirm_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")

        payload = verify_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        email = payload.get("email")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        user = self.repository.search_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not verify_password(old_password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect old password")

        new_hashed_password = hash_password(new_password)
        self.repository.update_password(user, new_hashed_password)

        return {"message": "Password updated successfully"}

    def get_profile(self, token: str):
        payload = verify_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid or expired token")

        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user

    def update_profile(self, token: str, update_data: dict):
        user = self.get_profile(token)
        filtered_data = {k: v for k, v in update_data.items() if v is not None}
        updated_user = self.repository.update_user(user, filtered_data)
        return updated_user
