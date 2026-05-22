from app.utils.stored_procedure import execute_sp


def get_products(db, offset: int, limit: int, sort_by: str = "id", order: str = "asc"):
    return execute_sp(
        db,
        "usp_GetProducts",
        {   
            "p_offset": offset,
            "p_limit": limit,
            "p_sort_by": sort_by,
            "p_order": order
        }
    )


def get_product_by_id(db, product_id):
    return execute_sp(
        db,
        "usp_GetProductById",
        {
            "p_product_id": product_id
        }
    )


def search_products(db, keyword, offset: int, limit: int, sort_by: str = "id", order: str = "asc"):
    return execute_sp(
        db,
        "usp_SearchProducts",
        {
            "p_keyword": keyword,
            "p_offset": offset,
            "p_limit": limit,
            "p_sort_by": sort_by,
            "p_order": order
        }
    )


def filter_products(db, category, offset: int, limit: int, sort_by: str = "id", order: str = "asc"):
    return execute_sp(
        db,
        "usp_filterProducts",
        {
            "p_category": category,
            "p_offset": offset,
            "p_limit": limit,
            "p_sort_by": sort_by,
            "p_order": order
        }
    )


def delete_product(db, product_id):
    execute_sp(
        db,
        "usp_DeleteProduct",
        {
            "p_product_id": product_id
        }
    )
    db.commit()