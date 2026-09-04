import json
from openai import OpenAI
from app.config import settings

client = OpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_base_url
)

MODEL_NAME = settings.ai_model_name

class AISentimentService:
    @staticmethod
    def analyze_review(review_text: str) -> dict:
        system_prompt = """
        Kamu adalah AI E-commerce Analyst. Tugasmu menganalisis teks ulasan pelanggan.
        Berikan output HANYA dalam format JSON murni dengan dua key berikut:
        1. "sentiment_label": (pilih salah satu secara akurat: Positif, Netral, atau Negatif)
        2. "ai_summary": (rangkum inti ulasan tersebut maksimal dalam 10 kata)
        """
        
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Ulasan Pelanggan: {review_text}"}
                ],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            print(f"Error AI: {e}")
            return {"sentiment_label": "Netral", "ai_summary": "Gagal dianalisis AI"}