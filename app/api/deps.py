from fastapi import Header, HTTPException


def require_role(allowed_roles: list[str]):
    def dependency(x_user_id: int = Header(..., alias="X-User-Id")):
        # TODO: Replace with DB lookup via spFastAPIGetUserRole
        mock_role = "Admin" if x_user_id == 1 else "Subscriber"
        if mock_role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return {"user_id": x_user_id, "role": mock_role}
    return dependency



