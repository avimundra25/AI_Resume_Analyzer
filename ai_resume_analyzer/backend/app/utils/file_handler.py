import os
import shutil
from fastapi import UploadFile, HTTPException
from app.core.config import settings

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".doc"}

def save_upload_file(upload_file: UploadFile) -> str:
    """Validates and securely saves an uploaded file to the temp directory."""
    # 1. Validation
    _, ext = os.path.splitext(upload_file.filename)
    if ext.lower() not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}. Use PDF or DOCX.")
    
    # 2. Secure Save
    file_path = os.path.join(settings.UPLOAD_DIR, upload_file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {e}")
        
    return file_path

def cleanup_file(file_path: str):
    """Removes the file after processing to save space and ensure privacy."""
    if os.path.exists(file_path):
        os.remove(file_path)