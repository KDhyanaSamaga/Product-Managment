from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from modules.user.models import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def search_by_email(self, email: str):
        return self.db.query(User).filter(User.email==email).first()

    def create_user(self, user_data: dict):
        new_user = User(**user_data)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def update_password(self, user: User, hashed_password: str):
        user.hashed_password = hashed_password
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: str):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user: User, update_data: dict):
        for key, value in update_data.items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user
