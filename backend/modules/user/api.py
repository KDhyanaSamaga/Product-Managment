from fastapi import APIRouter, Response, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import LoginUser, ResetPasswordUser, SignupUser
from database import get_db
from services import UserServices


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/login")
async def user_login(payload: LoginUser, response: Response, db: Session = Depends(get_db)):

    services = UserServices(db)
    # The payload.hashed_password contains the plain password entered by user for login
    token = services.login(payload.email, payload.hashed_password)
    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
    return {"message": "Login successful", "access_token": token}


@router.post("/signup")
async def user_signup(payload: SignupUser, response: Response, db: Session = Depends(get_db)):

    services = UserServices(db)
    token, user = services.signup(payload.dict())
    response.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
    return {"message": "Signup successful", "access_token": token, "user_id": user.id}


@router.post("/logout")
async def logout(response: Response):

    response.delete_cookie(key="access_token")
    return {"message": "Logout successful"}

@router.post("/forgot-password")
async def forgot_password():
    pass

@router.patch("/reset-password")
async def reset_password(payload: ResetPasswordUser):
    pass


@router.get("/profile")
async def user_profile():
    pass

@router.patch("/profile")
async def update_profile():
    pass