from pydantic import Field
from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class CreateUser(BaseModel):
    name:str = Field(max_length=20,min_length=1)
    phone_number:str = Field(max_length=12,min_length=10)
    shop_name:str = Field(max_length=20)
    shop_contact:str = Field(max_length=12,min_length=10)
    address:str =Field(min_length=5)
    city:Optional[str] = Field(default=None,max_length=20)
    gst:Optional[str] = Field(default=None,max_length=15)


class UpdateUser(BaseModel):
    name:str = Field(max_length=20,min_length=1)
    phone_number:str = Field(max_length=12,min_length=10)
    shop_name:str = Field(max_length=20)
    shop_contact:str = Field(max_length=12,min_length=10)
    address:str =Field(min_length=5)
    city:Optional[str] = Field(default=None,max_length=20)
    gst:Optional[str] = Field(default=None,max_length=15)


