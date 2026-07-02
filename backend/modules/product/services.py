from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from product.repository import ProductRepository
from product.schemas import AddProduct, UpdateProduct, ProductResponse, ListProduct
from uuid import UUID
from utils.pagination import pagination

class ProductServices:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def add_product(self, user_id: UUID, product_data: AddProduct) -> ProductResponse:
        product = self.repo.add_product(user_id, product_data)
        return product

    def update_product(self, product_id: UUID, user_id: UUID, update_data: UpdateProduct) -> ProductResponse:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        if product.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this product")
        updated_product = self.repo.update_product(product, update_data)
        return updated_product

    def delete_product(self, product_id: UUID, user_id: UUID) -> dict:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        if product.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this product")
        self.repo.delete_product(product)
        return {"detail": "Product deleted successfully"}

    def get_product_details(self, product_id: UUID) -> ProductResponse:
        product = self.repo.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return product

    def list_products(self, offset: int, limit: int) -> list[ListProduct]:
        products = self.repo.list_products(offset, limit)
        return products