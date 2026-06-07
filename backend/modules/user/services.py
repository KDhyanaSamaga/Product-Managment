from repository import UserRepository
from utils.security import verify_password
from fastapi import HTTPException
class UserServices:
    def __init__(self):
        self.repository = UserRepository()

    def login(self,email:str,password:str):
        user = self.repository.search_by_email(email)

        if not user:
            raise  HTTPException(
                status_code=404,
                detail="Email not found."
            )

        if not verify_password(password,user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail="Incorrect Password."
            )


    def reset_password(self,old_password:str,new_password:str):
