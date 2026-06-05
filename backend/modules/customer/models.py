from backend.database import get_db,Base

from sqlalchemy import Column,String,Text,DateTime,func,Integer
import uuid
from sqlalchemy.dialects.postgresql import UUID 

class Customer(Base):
    __tablename__ = "customers"

    id  = Column(UUID(as_uuid=True),primary_key=True,nullable=False,default=uuid.uuid4)

    name = Column(String(20),nullable=False)
    phone_number = Column(String(12),nullable=True)

    created_at = Column(DateTime,nullable=False,default=func.now())
    updated_at = Column(DateTime,nullable=False,default=func.now(),onupdate=func.now())