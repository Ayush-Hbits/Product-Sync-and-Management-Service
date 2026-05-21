from fastapi import APIRouter, Depends
from app.api.deps import require_role

router = APIRouter()


@router.post("/products")
def sync_products(user=Depends(require_role(["Admin"]))):
    return {
        "message": "Sync products from Fake Store API",
        "user": user
    }
