import uuid

from sqlalchemy import (
    Column,
    String,
    Numeric,
    DateTime,
    func,
    ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = "products"

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


    name = Column(String(50), nullable=False)

    description = Column(
        String(200),
        nullable=True
    )

    cost_price = Column(
        Numeric(10, 2),
        nullable=False
    )

    selling_price = Column(
        Numeric(10, 2),
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

    # Relationships
    shopkeeper = relationship(
        "User",
        back_populates="products"
    )

    bill_items = relationship(
        "BillItem",
        back_populates="product"
    )