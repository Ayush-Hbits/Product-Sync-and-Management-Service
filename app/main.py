from fastapi import FastAPI
from app.api.v1 import products, favorites, sync

app = FastAPI(title="FastAPI Product Sync Service", version="1.0.0")

app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(favorites.router, prefix="/api/v1/favorites", tags=["Favorites"])
app.include_router(sync.router, prefix="/api/v1/sync", tags=["Synchronization"])


@app.get("/")
def root():
    return {"message": "FastAPI Product Sync Service is running"}
