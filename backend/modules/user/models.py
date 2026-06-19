import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    func, ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String(20), nullable=False)
    phone_number = Column(String(12), nullable=False,unique=True)
    email = Column(String(50), nullable=False,unique=True)
    hashed_password = Column(Text, nullable=False)

    shop_name = Column(String(50), nullable=False)
    shop_contact = Column(String(12), nullable=False,unique=True)

    address = Column(Text, nullable=False)
    city = Column(String(30), nullable=True)

    gst = Column(String(15), nullable=True)

    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now()
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    products = relationship(
        "Product",
        back_populates="shopkeeper",
        cascade="all, delete-orphan"
    )

    bills = relationship(
        "Bill",
        back_populates="shopkeeper",
        cascade="all, delete-orphan"
    )

    refresh_tokens = relationship(
        "RefreshToken",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4()
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id",ondelete='CASCADE'),
        nullable=False
    )
    token = Column(
        Text,
        nullable=False
    )
    expires_at = Column(
        DateTime,
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now()
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.now(),
        onupdate=func.now()
    )

    user = relationship(
        "User",
        back_populates="refresh_tokens"
    )