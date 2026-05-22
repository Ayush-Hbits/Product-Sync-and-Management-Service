from app.repositories.product_repository import (get_products,get_product_by_id,search_products,filter_products, delete_product)
import math

def build_meta_response(rows_and_count, page, limit):
    """
    Safely reads database results whether they come back as a 
    dictionary, a combined list, or a raw list of items.
    """
    total_records = 0
    rows = []

    # 1. If execute_sp returned a dictionary (like we planned)
    if isinstance(rows_and_count, dict):
        total_records = rows_and_count.get("total_records", 0)
        rows = rows_and_count.get("data", [])

    # 2. If execute_sp returned a raw flat list (Why it crashed)
    elif isinstance(rows_and_count, list):

        rows = rows_and_count

        if len(rows) > 0 and "total_records" in rows[0]:
            total_records = rows[0]["total_records"]
        else:
            total_records = len(rows)

    # Calculate dynamic metadata pages safely
    total_pages = math.ceil(total_records / limit) if total_records > 0 else 0
    
    return {
        "metadata": {
            "current_page": page,
            "total_pages": total_pages,
            "total_records": total_records,
            "page_size": limit
        },
        "data": rows
    }




def fetch_products(db, page: int = 1, limit: int = 10):
    offset = (page-1) * limit
    result = get_products(db,offset, limit)
    return build_meta_response(result, page, limit)
  



def fetch_product_by_id(db, product_id):
    
    products = get_product_by_id(
        db,
        product_id
    )

    if not products:
        return None
    
    if isinstance(products, list):
        return products[0] if len(products) >0 else None

    return products


def fetch_searched_products(db, keyword, page: int = 1, limit: int = 10):
    offset = (page-1) * limit
    result = search_products(db, keyword, offset=offset, limit=limit)
    return build_meta_response(result, page, limit)


def fetch_filtered_products(db, category, page: int=1, limit: int=10):
    offset = (page-1) * limit
    result = filter_products(
        db,
        category,
        limit=limit,
        offset=offset
    )
    return build_meta_response(result, page, limit)
    

def remove_product(db, product_id):
    delete_product(db, product_id)
    return {"message": f"Product {product_id} removed successfully"}
