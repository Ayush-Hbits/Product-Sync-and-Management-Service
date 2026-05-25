from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.deps import require_role
from app.core.database import get_db
from app.services.product_service import (fetch_products,fetch_product_by_id,fetch_searched_products,fetch_filtered_products,remove_product)
from fastapi import Query, Path
from app.schemas.product_schema import (ProductListResponseSchema, ProductResponseSchema)
router = APIRouter()


@router.get("/", response_model=ProductListResponseSchema)
def get_products_api(
    page: int = 1,
    limit: int = 10,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db),
    user=Depends(require_role(["administrator", "subscriber"]))
):

   products_response = fetch_products(db,page,limit,sort_by,order)
   product_list = products_response.get("data", [])
      
   return {
        "count": len(product_list),
        "metadata": products_response.get("metadata"),
        "data": product_list,
        "user": user
    }
    



@router.get("/search", response_model=ProductListResponseSchema)
def search_products_api(
    page: int = 1,
    limit: int = 10,
    sort_by: str = "id",
    order: str = "asc",
    keyword: str = Query(..., description="Keyword to search by"),
    db: Session = Depends(get_db),
    user = Depends(require_role(["administrator", "subscriber"]))
):

    products_response = fetch_searched_products(db, keyword,page,limit,sort_by,order)
    product_list = products_response.get("data", [])

    return {
        "count": len(product_list),
        "metadata": products_response.get("metadata"),
        "data": product_list,
        "user": user
    }



@router.get("/filter", response_model=ProductListResponseSchema)
def filter_products_api(
    page: int = 1,
    limit: int = 10,
    category: str = Query(..., description="Category to filter by"),
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db),
    user=Depends(require_role(["administrator", "subscriber"]))
):

    products_response = fetch_filtered_products(db, category,page,limit,sort_by,order)
    product_list = products_response.get("data", [])

    return {
        "count": len(product_list),
        "metadata": products_response.get("metadata"),
        "data": product_list,
        "user": user
    }



@router.get("/{product_id}", response_model=ProductResponseSchema)
def get_product_by_id_api(
    product_id: int=Path(..., description="Product ID to get"),
    db: Session = Depends(get_db),
    user=Depends(require_role(["administrator", "subscriber"]))
):

    product = fetch_product_by_id(
        db,
        product_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.delete("/{product_id}", response_model=dict)
def delete_product_api(
    product_id: int=Path(..., description="Product ID to delete"),
    db: Session = Depends(get_db),
    user=Depends(require_role(["administrator"]))
):

    return remove_product(db, product_id)


