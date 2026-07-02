from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from decimal import Decimal

class AddProduct(BaseModel):
    """ this is to validate the add product"""
    name: str
    description: Optional[str] = None
    cost_price: Decimal
    selling_price: Decimal

class UpdateProduct(BaseModel):
    """ This is used to update the existing product"""
    name: Optional[str] = None
    description: Optional[str] = None
    cost_price: Optional[Decimal] = None
    selling_price: Optional[Decimal] = None

class ListProduct(BaseModel):
    """ This is used to list all the product """
    id: UUID
    name: str
    selling_price: Decimal
    
    model_config = ConfigDict(from_attributes=True)

class ProductResponse(BaseModel):
    """ Complete product response schema """
    id: UUID
    user_id: UUID
    name: str
    description: Optional[str] = None
    cost_price: Decimal
    selling_price: Decimal
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
