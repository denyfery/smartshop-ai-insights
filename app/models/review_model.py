# app/models/review_model.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    customer_name = Column(String(100))
    review_text = Column(Text) # Teks ulasan asli dari pelanggan
    rating = Column(Integer)   # Bintang 1 sampai 5
    
    # 🤖 Kolom yang akan dieksekusi oleh AI Service kita:
    sentiment_label = Column(String(20), nullable=True) # Positif, Netral, Negatif
    ai_summary = Column(String(255), nullable=True)     # Intisari keluhan/pujian