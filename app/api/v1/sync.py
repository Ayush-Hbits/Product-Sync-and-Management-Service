from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import require_role
from app.core.database import get_db
from app.services.sync_service import sync_products
from app.schemas.sync_schema import SyncResponseSchema
router = APIRouter()


@router.post("/products", response_model=SyncResponseSchema)
def sync_products_api(
    db: Session = Depends(get_db),
    user=Depends(require_role(["administrator"]))
):
    return sync_products(db)