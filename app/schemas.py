from pydantic import BaseModel
from datetime import date

class ProductBase(BaseModel):
    name: str
    category: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    product_id: int
    quantity: int
    total_price: float
    date: date

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    product_id: int
    quantity: int
    last_updated: date

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    class Config:
        orm_mode = True
