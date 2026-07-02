from sqlalchemy.orm import Session
from product.models import Product
from product.schemas import AddProduct, UpdateProduct
from uuid import UUID

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_product(self, user_id: UUID, product_data: AddProduct) -> Product:
        new_product = Product(user_id=user_id, **product_data.model_dump())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def get_product_by_id(self, product_id: UUID) -> Product | None:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def update_product(self, product: Product, update_data: UpdateProduct) -> Product:
        update_dict = update_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product: Product):
        self.db.delete(product)
        self.db.commit()

    def list_products(self, offset: int, limit: int) -> list[Product]:
        return self.db.query(Product).offset(offset).limit(limit).all()