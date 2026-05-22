from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class ProductSchema(BaseModel):

    id: int
    external_product_id: int
    title: str
    price: float
    description: Optional[str]
    category: Optional[str]
    image_url: Optional[str]
    rating_rate: Optional[float]
    rating_count: Optional[int]


class PaginationSchema(BaseModel):

    current_page: int
    total_pages: int
    total_records: int
    page_size: int


class ProductListResponseSchema(BaseModel):

   
    metadata: PaginationSchema
    data: List[ProductSchema]
  


class ProductResponseSchema(BaseModel):

    data: ProductSchema