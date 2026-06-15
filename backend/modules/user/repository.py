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

    def reset_password(self, old_password: str, new_password: str):
        pass
