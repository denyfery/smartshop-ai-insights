# 🛒 SmartShop AI Insights (E-Commerce AI Analytics & CBO Agent)

Backend service e-commerce cerdas berbasis **FastAPI**, **PostgreSQL**, dan **Groq LLM (Llama 3)**. Project ini dirancang untuk mengotomatisasi analisis ulasan pelanggan (Sentiment Analysis) dan bertindak sebagai *AI Chief Business Officer (CBO)* untuk menghasilkan laporan analitik bisnis secara *real-time*.

---

## 🚀 Tech Stack
* **Framework:** FastAPI (Python)
* **Database & ORM:** PostgreSQL, SQLAlchemy
* **AI / LLM Engine:** Groq API (Llama 3 / OpenAI SDK Wrapper)
* **Validation & Config:** Pydantic & Pydantic-Settings

---

## ✨ Core Features
1. **Automated Product Catalog:** Manajemen data produk dan stok secara *real-time*.
2. **AI Review Sentiment Analyzer:** Setiap ulasan (*review*) pelanggan yang masuk akan dicegat dan dianalisis otomatis oleh AI untuk melabeli sentimen (**Positif, Netral, Negatif**) beserta ringkasan keluhannya.
3. **Smart Inventory & Transaction:** Pencatatan transaksi penjualan yang otomatis memotong stok produk di database secara aman.
4. **AI Business Analytics CBO Agent:** Endpoint khusus yang membaca seluruh data produk, ulasan, dan transaksi untuk merumuskan laporan analitik bisnis dan rekomendasi strategis ala *Chief Business Officer*.

---

## 📁 Project Structure
```text
smartshop-ai-insights/
│
├── app/
│   ├── models/           # SQLAlchemy Database Models (Product, Review, Transaction)
│   ├── routers/          # FastAPI Endpoints (Products, Reviews, Transactions, Analytics)
│   ├── services/         # Business & AI Logic (Sentiment Analysis & Business Insights)
│   ├── database.py       # Database Connection Setup
│   ├── schemas.py        # Pydantic Validation Schemas
│   ├── config.py         # Environment Configuration
│   └── main.py           # FastAPI App Entry Point
│
├── .env                  # Environment Variables (Hidden)
├── .gitignore
├── requirements.txt
└── README.md



⚙️ Installation & Setup

    Clone Repository ini:
    Bash

    git clone [https://github.com/username/smartshop-ai-insights.git](https://github.com/username/smartshop-ai-insights.git)
    cd smartshop-ai-insights

    Buat dan Aktifkan Virtual Environment:
    Bash

    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Mac/Linux:
    source .venv/bin/activate

    Install Dependencies:
    Bash

    pip install -r requirements.txt

    Konfigurasi Environment (.env):
    Buat file .env di root folder dan sesuaikan kredensial berikut:
    Cuplikan kode

    DB_USER=postgres
    DB_PASSWORD=password_lu
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=smartshop_db

    OPENAI_API_KEY=gsk_api_key_groq_lu_disini
    OPENAI_BASE_URL=[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)
    AI_MODEL_NAME=llama3-8b-8192

    Jalankan Server:
    Bash

    uvicorn app.main:app --reload

    Akses Dokumentasi API (Swagger UI):
    Buka browser dan akses: http://localhost:8000/docs

📌 API Endpoints Summary

    POST /products/ - Menambahkan produk baru ke katalog

    GET /products/ - Melihat seluruh daftar produk

    POST /reviews/ - Mengirim ulasan (otomatis dianalisis AI sentimennya)

    POST /transactions/ - Membuat transaksi penjualan (otomatis potong stok)

    GET /analytics/insights - Menghasilkan laporan AI CBO Business Analytics