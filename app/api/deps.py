from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.user_repository import get_user_role

def require_role(allowed_roles: list[str]):
    def dependency(db: Session = Depends(get_db),x_user_id: int = Header(..., alias="X-User-Id")):
        user = get_user_role(db, x_user_id)
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized")
        role = user["user_role"]
        if role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return {
            "user_id": user["id"],
            "role": role
        }
    return dependency