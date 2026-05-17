import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.parser_service import parse_resume

print("--- TESTING PARSER ---")

try:
    print("\nPDF OUTPUT:")
    print(parse_resume("tests/resume.pdf"))
except Exception as e:
    print(f"PDF Error: {e}")

try:
    print("\nDOCX OUTPUT:")
    print(parse_resume("tests/resume.docx"))
except Exception as e:
    print(f"DOCX Error: {e}")