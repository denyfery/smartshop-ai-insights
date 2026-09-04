from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.product_model import Product
from app.schemas import ProductCreate

router = APIRouter(prefix="/products", tags=["Products Catalog"])

@router.post("/")
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        category=product_data.category,
        price=product_data.price,
        stock=product_data.stock
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product

@router.get("/")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()