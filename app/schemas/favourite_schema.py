from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.schemas.product_schema import ProductSchema


class FavouriteListResponseSchema(BaseModel):
    count: int
    data : List[ProductSchema]
    user: Dict[str, Any]


class MessageResponseSchema(BaseModel):
    message: str