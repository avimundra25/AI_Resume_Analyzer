import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Resume Analyzer API"
    VERSION: str = "1.0.0"
    
    # Secrets
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Directories
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "temp_uploads")
    REPORT_DIR: str = os.getenv("REPORT_DIR", "reports")
    
    class Config:
        case_sensitive = True

settings = Settings()

# Ensure directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.REPORT_DIR, exist_ok=True)