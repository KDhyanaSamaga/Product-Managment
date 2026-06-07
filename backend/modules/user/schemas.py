from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class SignupUser(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    phone_number: str = Field(..., min_length=10, max_length=12)
    email: str = Field(..., min_length=1, max_length=20)
    hashed_password: str = Field(..., min_length=1, max_length=20)
    shop_name: str = Field(..., min_length=1, max_length=20)
    shop_contact: str = Field(..., min_length=10, max_length=12)
    address: str = Field(..., min_length=5)
    city: Optional[str] = Field(default=None, max_length=20)
    gst: str = Field(..., min_length=15, max_length=15) # GST is usually exactly 15 chars and required for businesses


class UpdateUser(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=20)
    phone_number: Optional[str] = Field(default=None, min_length=10, max_length=12)
    email: Optional[str] = Field(default=None, min_length=1, max_length=20)
    hashed_password: Optional[str] = Field(default=None, min_length=1, max_length=20)
    shop_name: Optional[str] = Field(default=None, min_length=1, max_length=20)
    shop_contact: Optional[str] = Field(default=None, min_length=10, max_length=12)
    address: Optional[str] = Field(default=None, min_length=5)
    city: Optional[str] = Field(default=None, max_length=20)
    gst: Optional[str] = Field(default=None, min_length=15, max_length=15)


class LoginUser(BaseModel):
    email: str = Field(..., min_length=1, max_length=20)
    hashed_password: str = Field(..., min_length=1, max_length=20)

class ResetPasswordUser(BaseModel):
    hashed_password: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    phone_number: str
    shop_name: str
    shop_contact: str
    address: str
    city: Optional[str]
    gst: str
    created_at: datetime
    updated_at: datetime
    #
    # class Config:
    #     # Crucial for Pydantic v1 / v2 compatibility to read SQLAlchemy objects directly
    #     from_attributes = True