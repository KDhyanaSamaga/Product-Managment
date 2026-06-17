from fastapi import APIRouter, Response, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.user.schemas import LoginUser, SignupUser,PasswordChangeUser
from database import get_db
from modules.user.services import UserServices


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/login")
async def user_login(payload: LoginUser, response: Response, db: Session = Depends(get_db)):
    services = UserServices(db)
    # The payload.password contains the plain password entered by user for login
    token = services.login(payload.email, payload.password)
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

# @router.post("/forgot-password")
# async def forgot_password():
#     pass

@router.patch("/reset-password")
async def reset_password(payload: PasswordChangeUser, request: Request, response: Response, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        # Check authorization header as fallback
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header
        else:
            raise HTTPException(status_code=401, detail="Not authenticated")
    
    if token.startswith("Bearer "):
        token = token[7:]

    services = UserServices(db)
    return services.reset_password(
        token=token,
        old_password=payload.old_password,
        new_password=payload.new_password,
        confirm_password=payload.confirm_password
    )


# @router.get("/profile")
# async def user_profile():
#     pass

# @router.patch("/profile")
# async def update_profile():
#     pass