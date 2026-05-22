from sqlalchemy import text
from app.utils.stored_procedure import execute_sp

def get_user_role(db, user_id: int):
    result = execute_sp(
        db,
        "usp_GetUserRole",
        {
            "p_user_id": user_id
        }
     )
    
    if result:
        return result[0]
    return None