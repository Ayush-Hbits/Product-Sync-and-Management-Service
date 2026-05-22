from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.deps import require_role
from app.core.database import get_db
from app.services.product_service import (fetch_products,fetch_product_by_id,fetch_searched_products,fetch_filtered_products,remove_product)
from fastapi import Query

router = APIRouter()


@router.get("/")
def get_products_api(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(require_role(["Admin", "Subscriber"]))
):

   products_response = fetch_products(db,page,limit)
   product_list = products_response.get("data", [])

   return {
        "count": len(product_list),
        "metadata": products_response.get("metadata"),
        "data": product_list,
        "user": user
    }



@router.get("/search")
def search_products_api(
    page: int = 1,
    limit: int = 10,
    keyword: str = Query(...),
    db: Session = Depends(get_db),
    user = Depends(require_role(["Admin", "Subscriber"]))
):

    products_response = fetch_searched_products(db, keyword,page,limit)
    product_list = products_response.get("data", [])

    return {
        "count": len(product_list),
        "metadata": products_response.get("metadata"),
        "data": product_list,
        "user": user
    }



@router.get("/filter")
def filter_products_api(
    page: int = 1,
    limit: int = 10,
    category: str = Query(...),
    db: Session = Depends(get_db),
    user=Depends(require_role(["Admin", "Subscriber"]))
):

    products_response = fetch_filtered_products(db, category,page,limit)
    product_list = products_response.get("data", [])

    return {
        "count": len(product_list),
        "metadata": products_response.get("metadata"),
        "data": product_list,
        "user": user
    }



@router.get("/{product_id}")
def get_product_by_id_api(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role(["Admin", "Subscriber"]))
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


@router.delete("/{product_id}")
def delete_product_api(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_role(["Admin"]))
):

    return remove_product(db, product_id)
