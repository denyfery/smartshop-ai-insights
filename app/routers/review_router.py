from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.review_model import Review
from app.schemas import ReviewCreate
from app.services.ai_sentiment_service import AISentimentService

router = APIRouter(prefix="/reviews", tags=["Reviews & Sentiment AI"])

@router.post("/")
def submit_review(review_data: ReviewCreate, db: Session = Depends(get_db)):
    # 1. Tembak AI Service untuk analisa ulasan
    ai_result = AISentimentService.analyze_review(review_data.review_text)
    
    # 2. Siapkan data untuk disimpan ke Database
    new_review = Review(
        product_id=review_data.product_id,
        customer_name=review_data.customer_name,
        review_text=review_data.review_text,
        rating=review_data.rating,
        sentiment_label=ai_result.get("sentiment_label"),
        ai_summary=ai_result.get("ai_summary")
    )
    
    # 3. Simpan ke Database
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    
    return new_review