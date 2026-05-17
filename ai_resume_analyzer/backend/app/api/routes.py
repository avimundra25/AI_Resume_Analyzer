from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from typing import Optional
import os

from app.utils.file_handler import save_upload_file, cleanup_file
from app.services.parser_service import parse_resume
from app.services.llm_service import generate_evaluation_report

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Upload a resume and a Job Description. 
    Returns parsed data, AI evaluation metrics, and generates a DOCX report.
    """
    file_path = None
    try:
        # 1. Securely save the uploaded file
        file_path = save_upload_file(file)
        
        # 2. Parse the resume (Your parser.py logic)
        parsed_data = parse_resume(file_path)
        
        # 3. Evaluate with LLM (Your ai_evaluator.py logic)
        report_filename = f"Report_{file.filename}.docx"
        evaluation_result = generate_evaluation_report(
            parsed_resume_data=parsed_data,
            job_description=job_description,
            output_filename=report_filename
        )
        
        # 4. Return everything the frontend needs
        return {
            "message": "Analysis complete",
            "candidate_data": parsed_data,
            "ai_evaluation": evaluation_result["data"],
            "report_download_url": f"/api/v1/download/{report_filename}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up the uploaded file to prevent server bloat
        if file_path:
            cleanup_file(file_path)

@router.get("/download/{filename}")
async def download_report(filename: str):
    """Endpoint to download the generated Word document."""
    from app.core.config import settings
    file_path = os.path.join(settings.REPORT_DIR, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Report not found")
        
    return FileResponse(path=file_path, filename=filename, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')