from pydantic import BaseModel

class ReviewCreate(BaseModel):
    product_id: int
    customer_name: str
    review_text: str
    rating: int

class ProductCreate(BaseModel):
    name: str
    description: str
    category: str
    price: float
    stock: int

class TransactionCreate(BaseModel):
    product_id: int
    quantity: int
    total_price: float