from fastapi import APIRouter, Depends, Header, Path
from app.api.deps import require_role
from app.core.database import get_db
from app.schemas.favourite_schema import FavouriteListResponseSchema, MessageResponseSchema
from sqlalchemy.orm import Session
from app.services.favourite_service import fetch_favourites, add_favourite_by_id, remove_favourite
router = APIRouter()


@router.get("/", response_model=FavouriteListResponseSchema)
def get_favourites(db: Session = Depends(get_db),user=Depends(require_role(["subscriber"]))):
    favourites = fetch_favourites(db, user["user_id"])
    return {
        "count": len(favourites),
        "data": favourites,
        "user": user
    }

@router.post("/{product_id}", response_model=MessageResponseSchema, summary="Add a product to favourites")
def add_favourite_by_id_api(product_id: int = Path(..., description="Product ID to add into favourites"),db: Session = Depends(get_db),user=Depends(require_role(["subscriber"]))):
    return add_favourite_by_id(db=db, product_id=product_id, user_id=user["user_id"])


@router.delete("/{product_id}", response_model=MessageResponseSchema)
def delete_favourite_by_id_api(product_id: int = Path(..., description="Product ID to remove from favourites"),db: Session = Depends(get_db),user=Depends(require_role(["subscriber"]))):
    return remove_favourite(db,user["user_id"],product_id)