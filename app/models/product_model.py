# app/models/product_model.py
from sqlalchemy import Column, Integer, String, Float, Text
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), index=True)
    description = Column(Text, nullable=True)
    category = Column(String(50), index=True) # Contoh: Gadget, Audio, Wearable
    price = Column(Float, default=0.0)
    stock = Column(Integer, default=0)