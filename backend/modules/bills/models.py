import uuid

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    Numeric,
    Text,
    String,
    func
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Bill(Base):
    __tablename__ = "bills"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    customer_name = Column(
        String(50),
        nullable=True,
        default="Customer"
    )

    customer_phone = Column(
        String(12),
        nullable=True
    )

    customer_address = Column(
        Text,
        nullable=True
    )

    total_amount = Column(
        Numeric(10, 2),
        nullable=False,
        default=0.00
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=func.now()
    )

    # Relationships
    shopkeeper = relationship(
        "User",
        back_populates="bills"
    )

    items = relationship(
        "BillItem",
        back_populates="bill",
        cascade="all, delete-orphan"
    )


class BillItem(Base):
    __tablename__ = "bill_items"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    bill_id = Column(
        UUID(as_uuid=True),
        ForeignKey("bills.id"),
        nullable=False
    )

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    price_at_sale = Column(
        Numeric(10, 2),
        nullable=False
    )

    bill = relationship(
        "Bill",
        back_populates="items"
    )

    product = relationship(
        "Product",
        back_populates="bill_items"
    )