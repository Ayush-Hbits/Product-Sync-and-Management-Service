from app.repositories.product_repository import (get_products,get_product_by_id,search_products,filter_products, delete_product)
import math

def build_meta_response(rows_and_count, page, limit):
  
    total_records = 0
    rows = []

   
    if isinstance(rows_and_count, dict):
        total_records = rows_and_count.get("total_records", 0)
        rows = rows_and_count.get("data", [])

    elif isinstance(rows_and_count, list):

        rows = rows_and_count

        if len(rows) > 0 and "total_records" in rows[0]:
            total_records = rows[0]["total_records"]
        else:
            total_records = len(rows)

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



def fetch_products(db, page: int = 1, limit: int = 10, sort_by: str = "id", order: str = "asc"):
    offset = (page-1) * limit
    result = get_products(db,offset, limit, sort_by, order)
    return build_meta_response(result, page, limit)

  

def fetch_product_by_id(db, product_id):
    product = get_product_by_id(
        db,
        product_id
    )
    if not product:
        return None
    
    if isinstance(product, list):
        product = product[0] if product else None
    
    return {"data": product}


def fetch_searched_products(db, keyword, page: int = 1, limit: int = 10, sort_by: str = "id", order: str = "asc"):
    offset = (page-1) * limit
    result = search_products(db, keyword, offset=offset, limit=limit, sort_by=sort_by, order=order)
    return build_meta_response(result, page, limit)


def fetch_filtered_products(db, category, page: int=1, limit: int=10, sort_by: str = "id", order: str = "asc"):
    offset = (page-1) * limit
    result = filter_products(db,category,offset=offset,limit=limit,sort_by=sort_by,order=order)
    return build_meta_response(result, page, limit)
    

def remove_product(db, product_id):
    delete_product(db, product_id)
    return {"message": f"Product {product_id} removed successfully"}
