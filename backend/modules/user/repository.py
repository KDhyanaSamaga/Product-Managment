#repository.py $\rightarrow$ Handle how data is fetched from or written to PostgreSQL.
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models import User

class UserRepository:
    def __init__(self,db:Session = Depends(get_db)):
        self.db = db

    def search_by_email(self,email:str):
        return self.db.query(User).filter(User.email==email).first()


