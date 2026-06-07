from fastapi import APIRouter
from utils.security import hash_password,verify_password
from schemas import LoginUser,ResetPasswordUser,SignupUser
from repository import UserRepository
from database import  get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/login")
async def user_login(payload:LoginUser,):


@router.post("/signup")
async def user_signup():

@router.post("/logout")
async def logout():

@router.post("/forgot-password")
async def forgot_password():

@router.patch("/reset-password")
async def reset_password(payload:ResetPasswordUser):


@router.get("/profile")
async def user_profile():

@router.patch("/profile")
async def update_profile():