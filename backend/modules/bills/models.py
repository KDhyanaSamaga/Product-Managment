import uuid
from sqlalchemy import Column, Integer, DateTime, func, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from backend.database import Base


class Bill(Base):
    __tablename__ = "bills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Multi-tenant link: Which shopkeeper generated this bill?
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Relationship link: Who bought it?
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False)

    total_amount = Column(Numeric(10, 2), nullable=False, default=0.00)
    created_at = Column(DateTime, nullable=False, default=func.now())

    # Relationships
    shopkeeper = relationship("User", back_populates="bills")
    customer = relationship("Customer", back_populates="bills")
    items = relationship("BillItem", back_populates="bill", cascade="all, delete-orphan")


class BillItem(Base):
    """
    Intermediate Association Table for Many-to-Many (Bill <-> Product).
    Tracks exact units sold and locks down the price at transaction time.
    """
    __tablename__ = "bill_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bill_id = Column(UUID(as_uuid=True), ForeignKey("bills.id"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)

    quantity = Column(Integer, nullable=False, default=1)

    # Snapshot of price at the time of purchase (in case shopkeeper changes product price later)
    price_at_sale = Column(Numeric(10, 2), nullable=False)

    # Relationships
    bill = relationship("Bill", back_populates="items")
    product = relationship("Product", back_populates="bill_items")