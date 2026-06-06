from fastapi import APIRouter
from utils.security import hash_password,verify_password
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/login")
async def user_login():


@router.post("/signup")
async def user_signup():

@router.post("/logout")
async def logout():

@router.post("/forgot-password")
async def forgot_password():

@router.patch("/reset-password")
async def reset_password():


@router.get("/profile")
async def user_profile():

@router.patch("/profile")
async def update_profile():