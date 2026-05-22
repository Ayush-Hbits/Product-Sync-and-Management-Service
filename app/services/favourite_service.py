from app.repositories.favourite_repository import add_favourite, delete_favourite, get_favourites


def fetch_favourites(db, user_id:int):
    favourites = get_favourites(db, user_id)
    return favourites

def add_favourite_by_id(db, user_id:int, product_id:int):
    add_favourite(db, user_id, product_id)
    return {"message": "Product added to favourites"}

def remove_favourite(db, user_id:int, product_id:int):
    delete_favourite(db, user_id, product_id)
    return {"message": "Product removed from favourites"}