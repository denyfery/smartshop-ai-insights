from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.transaction_model import Transaction
from app.models.product_model import Product
from app.schemas import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["Transactions & Sales"])

@router.post("/")
def create_transaction(tx_data: TransactionCreate, db: Session = Depends(get_db)):
    # 1. Cek dulu apakah produknya ada di database
    product = db.query(Product).filter(Product.id == tx_data.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produk tidak ditemukan!")
    
    # 2. Cek apakah stok mencukupi
    if product.stock < tx_data.quantity:
        raise HTTPException(status_code=400, detail=f"Stok tidak cukup! Sisa stok: {product.stock}")
    
    # 3. Kurangi stok produk secara otomatis
    product.stock -= tx_data.quantity
    
    # 4. Buat record transaksi baru
    new_transaction = Transaction(
        product_id=tx_data.product_id,
        quantity=tx_data.quantity,
        total_price=tx_data.total_price
    )
    
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    return {
        "message": "Transaksi berhasil dicatat dan stok terupdate!",
        "transaction": new_transaction
    }

@router.get("/")
def get_all_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()