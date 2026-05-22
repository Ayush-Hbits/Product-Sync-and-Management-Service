import requests
from fastapi import HTTPException
from app.repositories.sync_repository import upsert_product


def sync_products(db):
    try:
      response = requests.get("https://fakestoreapi.com/products")
      if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch products")
      products = response.json()
      
      if not isinstance(products, list):
        raise HTTPException(status_code=400, detail="Invalid products data")
                           
      inserted = 0

      for product in products:
        upsert_product(db, product)
        inserted += 1

      return {
        "status": "success",
        "total_processed": len(products),
        "inserted": inserted
      }
    except Exception as e:
      raise HTTPException(status_code=503, detail=str(e))


