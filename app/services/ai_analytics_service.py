from openai import OpenAI
from sqlalchemy.orm import Session
from app.config import settings
from app.models.product_model import Product
from app.models.review_model import Review
from app.models.transaction_model import Transaction

client = OpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_base_url
)
MODEL_NAME = settings.ai_model_name

class AIAnalyticsService:
    @staticmethod
    def generate_business_insights(db: Session) -> str:
        # 1. Tarik semua data dari database
        products = db.query(Product).all()
        reviews = db.query(Review).all()
        transactions = db.query(Transaction).all()
        
        # 2. Susun data produk & stok
        prod_data = [f"- {p.name} (Kategori: {p.category}, Harga: Rp{p.price}, Sisa Stok: {p.stock})" for p in products]
        
        # 3. Susun data ulasan & sentimen AI
        rev_data = [f"- Produk ID {r.product_id}: [{r.sentiment_label}] {r.ai_summary} (Rating: {r.rating}/5)" for r in reviews]
        
        # 4. Susun data transaksi penjualan
        tx_data = [f"- Transaksi Produk ID {t.product_id}: Terjual {t.quantity} pcs, Total: Rp{t.total_price}" for t in transactions]
        
        # Gabungkan menjadi konteks yang kaya
        context = f"""
        DATA KATALOG PRODUK:
        {'\n'.join(prod_data) if prod_data else 'Belum ada produk.'}

        DATA ULASAN & SENTIMEN PELANGGAN:
        {'\n'.join(rev_data) if rev_data else 'Belum ada ulasan.'}

        DATA TRANSAKSI PENJUALAN:
        {'\n'.join(tx_data) if tx_data else 'Belum ada transaksi.'}
        """
        
        system_prompt = """
        Kamu adalah AI Chief Business Officer (CBO) untuk platform E-commerce. 
        Tugasmu adalah menganalisis data toko online di bawah ini dan memberikan laporan analitik bisnis yang profesional.
        Berikan poin-poin berikut dalam bahasa Indonesia:
        1. Ringkasan Performa Penjualan & Stok Produk.
        2. Analisis Kepuasan Pelanggan (berdasarkan sentimen ulasan).
        3. Rekomendasi / Saran Actionable untuk pemilik toko ke depannya.
        Jangan mengarang data di luar konteks yang diberikan.
        """
        
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Berikut adalah data toko saat ini:\n{context}"}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Gagal menghasilkan analitik bisnis: {str(e)}"