from app.utils.stored_procedure import execute_sp


def get_products(db, offset: int, limit: int):
    # Pass offset and limit inside a parameters dictionary
    return execute_sp(
        db,
        "sp_GetProducts",
        {   
            "p_offset": offset,
            "p_limit": limit
        }
    )


def get_product_by_id(db, product_id):
    # UNTOUCHED: Single record lookups do not require pagination parameters
    return execute_sp(
        db,
        "sp_GetProductById",
        {
            "p_product_id": product_id
        }
    )


def search_products(db, keyword, offset: int, limit: int):
    # Added offset and limit parameters
    return execute_sp(
        db,
        "sp_SearchProducts",
        {
            "p_keyword": keyword,
            "p_offset": offset,
            "p_limit": limit
        }
    )


def filter_products(db, category, offset: int, limit: int):
    # Added offset and limit parameters
    return execute_sp(
        db,
        "sp_filterProducts",
        {
            "p_category": category,
            "p_offset": offset,
            "p_limit": limit
        }
    )


def delete_product(db, product_id):
    execute_sp(
        db,
        "sp_DeleteProduct",
        {
            "p_product_id": product_id
        }
    )
    db.commit()