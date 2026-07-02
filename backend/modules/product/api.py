from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from uuid import UUID
from database import get_db
from product.schemas import AddProduct, UpdateProduct, ProductResponse, ListProduct
from product.services import ProductServices
from utils.tokenServices import verify_token
from utils.pagination import pagination

router = APIRouter(
    prefix='/product',
    tags=['Product']
)

def get_current_user_id(authorization: str = Header(None)) -> UUID:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid or missing Authorization header"
        )
    token = authorization.split(" ")[1]
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid token or expired"
        )
    
    # Try fetching 'user_id' or standard 'sub' from the JWT payload
    user_id_str = payload.get("user_id") or payload.get("sub")
    if not user_id_str:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Token does not contain user identification"
        )
    try:
        user_id = UUID(str(user_id_str))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid user ID format in token"
        )
    return user_id

@router.put("/add-product", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_product(
    product_data: AddProduct,
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """First the token is verified if true then add the product
    Every time when add product check every time if sucessful 
    product added sucessfully verify the schema if correct then only """
    service = ProductServices(db)
    return service.add_product(user_id, product_data)


@router.put("/update-product/{id}", response_model=ProductResponse)
async def update_product(
    id: UUID,
    update_data: UpdateProduct,
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """This is for updating the product information if token verifed then only update the product
    else return error.If the identity is true then search that product by id if found  then show the
    existing data and user changes or doesnot then send it to for update during this again token check for
    security"""
    service = ProductServices(db)
    return service.update_product(id, user_id, update_data)


@router.delete("/delete-product/{id}", status_code=status.HTTP_200_OK)
async def delete_product(
    id: UUID,
    user_id: UUID = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    """This is for deleting the product information if token verifed then only delete the product
    else return error.If the identity is true then search that product by id if found  then show the
    existing data and user changes or doesnot then send it to for update during this again token check for
    security.peremently delete the product"""
    service = ProductServices(db)
    return service.delete_product(id, user_id)


@router.get("/list", response_model=list[ListProduct])
async def list_product(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """This is useed to list the entire product apply pagination and use the pagination code present int
    the utils/pagination.py code in this dont return every details just the basic details to see in the screen"""
    offset = pagination(page, limit)
    service = ProductServices(db)
    return service.list_products(offset, limit)


@router.get("/product-info/{id}", response_model=ProductResponse)
async def get_product_details(
    id: UUID,
    db: Session = Depends(get_db)
):
    """so when the owner wants to know the product details he can just click on that and see the details
    like product name,description and other details """
    service = ProductServices(db)
    return service.get_product_details(id)