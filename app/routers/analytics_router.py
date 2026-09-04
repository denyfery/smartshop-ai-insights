from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.ai_analytics_service import AIAnalyticsService

router = APIRouter(prefix="/analytics", tags=["AI Business Analytics"])

@router.get("/insights")
def get_store_insights(db: Session = Depends(get_db)):
    # Panggil service AI Analytics
    report = AIAnalyticsService.generate_business_insights(db)
    
    return {
        "status": "success",
        "business_insights_report": report
    }