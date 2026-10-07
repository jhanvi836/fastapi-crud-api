from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

# Shared properties
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="Wireless Mouse")
    description: Optional[str] = Field(None, max_length=255, example="Ergonomic optical mouse")
    price: float = Field(..., gt=0, example=29.99)
    in_stock: bool = Field(True, example=True)

# Schema for creating a product
class ProductCreate(ProductBase):
    pass

# Schema for updating a product (all fields optional for partial updates)
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    price: Optional[float] = Field(None, gt=0)
    in_stock: Optional[bool] = None

# Schema for reading/returning a product
class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)