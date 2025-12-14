import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application configuration settings."""
    
    # Pinecone
    pinecone_api_key: str = os.getenv("PINECONE_API_KEY", "")
    pinecone_index_name: str = os.getenv("PINECONE_INDEX_NAME", "patentguard")
    
    # Groq
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    groq_model: str = "llama-3.3-70b-versatile"  # Latest Llama 3.3 model (Dec 2024)
    
    # Google Cloud
    google_credentials: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")
    google_cloud_project: str = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    
    # Embedding Model
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_dimension: int = 384
    
    # Server
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    
    # CORS
    cors_origins: list = ["http://localhost:5173", "http://localhost:5174", "http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # Allow extra fields in .env without validation errors


settings = Settings()
