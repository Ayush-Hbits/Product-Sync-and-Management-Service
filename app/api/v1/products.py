from fastapi import APIRouter, Depends
from app.api.deps import require_role

router = APIRouter()


@router.get("/")
def get_products(user=Depends(require_role(["Admin", "Subscriber"]))):
    return {
        "message": "Get products endpoint",
        "user": user
    }


@router.get("/{product_id}")
def get_product(product_id: int, user=Depends(require_role(["Admin", "Subscriber"]))):
    return {
        "message": f"Get product {product_id}",
        "user": user
    }


@router.delete("/{product_id}")
def delete_product(product_id: int, user=Depends(require_role(["Admin"]))):
    return {
        "message": f"Delete product {product_id}",
        "user": user
    }
