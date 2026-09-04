# app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import review_router, product_router, transaction_router, analytics_router

# Import semua model di sini agar terdeteksi oleh SQLAlchemy saat create_all
from app.models import product_model, review_model, transaction_model

# Generate tabel ke database (jika belum ada)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartShop AI Insights API",
    description="E-Commerce AI Analytics Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Selamat datang di SmartShop AI API, guruu! 🚀"}

app.include_router(review_router.router)
app.include_router(product_router.router)
app.include_router(transaction_router.router)
app.include_router(analytics_router.router)