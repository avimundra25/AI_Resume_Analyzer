# AI Resume Analyzer — Full Stack Platform

This project is a complete, full-stack AI-powered resume analysis tool. It allows users to upload their resumes, compares the extracted text against a target job role using Google's Gemini AI, and provides a detailed visual breakdown and a downloadable Word report.

**Folders**
* `backend/` – Contains the FastAPI Python server, parsing logic, and AI integration.
* `frontend/` – Contains the HTML, CSS, and JavaScript user interface.

**Working**
1. The user opens the frontend in their browser and uploads a PDF or DOCX resume.
2. The user specifies their target job role (e.g., "Software Engineer") and clicks Analyze.
3. The frontend sends the file securely to the backend via a `fetch` API request.
4. The backend temporarily saves the file, parses the text, and asks Gemini AI to evaluate it against the job role.
5. The backend generates a detailed `.docx` report and sends the AI's JSON data back to the frontend.
6. The frontend dynamically updates progress bars, scores, and the interview probability badge.
7. The user can view their results, copy an AI-generated cover letter, and download the Word document.

**How to Run the Project**
To use this application, you must run both the backend and frontend simultaneously.

* **Backend:** Open a terminal in the `backend/` folder and run `uvicorn app.main:app --reload`.
* **Frontend:** Open a terminal in the `frontend/` folder and run `python -m http.server 3000`, then visit `http://localhost:3000/index.html` in your browser.

**Summary**
This full-stack project bridges a highly interactive, responsive user interface with a powerful, asynchronous Python backend to deliver professional resume feedback in seconds.
