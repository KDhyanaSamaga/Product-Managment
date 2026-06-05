from sqlalchemy import Column,String,Text,DateTime,func,Integer
import uuid
from sqlalchemy.dialects.postgresql import UUID 

from database import get_db,Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)

    name = Column(String(20),nullable=False)
    phone_number = Column(String(12),nullable=False)

    shop_name = Column(String,nullable=False)
    shop_contact = Column(String(12),nullable=False)
    address = Column(Text,nullable=False)
    city = Column(String(15),nullable=True)
    gst = Column(Integer,nullable=False)

    created_at = Column(DateTime,nullable=False,default=func.now())
    updated_at = Column(DateTime,nullable=False,default=func.now(),onupdate=func.now())
