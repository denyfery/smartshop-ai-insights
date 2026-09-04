# app/models/transaction_model.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
    total_price = Column(Float, default=0.0)
    transaction_date = Column(DateTime, default=datetime.utcnow)