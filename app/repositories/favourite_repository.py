from app.utils.stored_procedure import execute_sp

def add_favourite(db, user_id: int, product_id: int):
    return execute_sp(
        db,
        "usp_AddFavorite",
        {
            "p_user_id": user_id,
            "p_product_id": product_id
        }
    )
    

def delete_favourite(db, user_id: int, product_id: int):
    return execute_sp(
        db,
        "usp_RemoveFavorite",
        {
            "p_user_id": user_id,
            "p_product_id": product_id
        }
    )
    

def get_favourites(db, user_id: int):
    return execute_sp(
        db,
        "usp_GetFavorites",    
        {
            "p_user_id": user_id
        }
    )