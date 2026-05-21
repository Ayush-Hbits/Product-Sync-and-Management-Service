from fastapi import APIRouter, Depends
from app.api.deps import require_role

router = APIRouter()


@router.get("/")
def get_favorites(user=Depends(require_role(["Subscriber"]))):
    return {"message": "Get favorites", "user": user}


@router.post("/{product_id}")
def add_favorite(product_id: int, user=Depends(require_role(["Subscriber"]))):
    return {"message": f"Added {product_id} to favorites", "user": user}


@router.delete("/{product_id}")
def remove_favorite(product_id: int, user=Depends(require_role(["Subscriber"]))):
    return {"message": f"Removed {product_id} from favorites", "user": user}
