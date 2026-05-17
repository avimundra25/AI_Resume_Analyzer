# Backend API Module

This module is responsible for handling file uploads, orchestrating the document parsing, communicating with the Gemini AI, and generating downloadable reports. It is built using FastAPI for high performance and asynchronous request handling.

**Files**
* `app/main.py` – The main entry point that initializes the FastAPI application.
* `app/api/routes.py` – Contains the API endpoints (`/analyze` and `/download`).
* `app/services/parser_service.py` – Extracts structured data (skills, experience, etc.) from uploaded PDFs and DOCX files.
* `app/services/llm_service.py` – Sends parsed data to Gemini AI and creates the Word document report.
* `app/utils/file_handler.py` – Securely saves and deletes temporary file uploads.
* `app/core/config.py` – Centralized management of environment variables.
* `.env` – Securely stores the `GEMINI_API_KEY` (ignored by Git).
* `requirements.txt` – Required Python libraries (FastAPI, google-generativeai, pdfplumber, etc.).

**Working**
1. The API receives a file and job description via a `POST` request.
2. `file_handler.py` saves the file securely to a `temp_uploads` directory.
3. `parser_service.py` reads the file and extracts text, skills, and contact info into a dictionary.
4. `llm_service.py` formats a strict prompt and sends the dictionary to Gemini AI.
5. Gemini returns a JSON object containing the score, interview probability, strengths, and weaknesses.
6. A `.docx` report is generated and saved in the `reports` directory.
7. The API returns the AI JSON data and the download URL to the frontend, and the temp file is deleted.

**Main Endpoints**
* `POST /api/v1/analyze` – Accepts form data (file and job_description) and returns analysis data.
* `GET /api/v1/download/{filename}` – Serves the generated `.docx` file to the user.

**Sample Output (API Response)**
```json
{
  "message": "Analysis complete",
  "candidate_data": { "name": "John Doe", "skills": ["python", "sql"] },
  "ai_evaluation": {
    "score": 85,
    "interview_probability": 75,
    "overall_summary": "Strong candidate with solid backend experience...",
    "strengths": ["Python expertise", "API design"],
    "weaknesses": ["Missing cloud deployment experience"]
  },
  "report_download_url": "/api/v1/download/Report_resume.docx"
}