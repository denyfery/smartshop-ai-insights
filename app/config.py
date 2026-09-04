# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    
    # Tambahkan ini biar terbaca dari .env
    openai_api_key: str | None = None
    openai_base_url: str | None = "https://api.groq.com/openai/v1"
    ai_model_name: str | None = "openai/gpt-oss-120b" # ganti defaultnya sesuai model yang lu temuin

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()