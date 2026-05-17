import sys
import os

# This line ensures Python can find your 'app' folder from inside the 'tests' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.parser_service import parse_resume
from app.services.llm_service import generate_evaluation_report

def run_test():
    print("--- STARTING INTEGRATION TEST ---")
    
    sample_jd = """
    Looking for a Python Backend Developer. 
    Required skills: Python, REST APIs, JSON data handling, basic NLP or AI integration experience.
    Must be able to write clean, modular code.
    """
    
    print("Step 1: Parsing PDF...")
    try:
        # Make sure you have a dummy resume.pdf inside the tests/ folder
        parsed_data = parse_resume("tests/resume.pdf")
        print(f"Successfully extracted data for: {parsed_data.get('name')}")
    except Exception as e:
        print(f"Failed to parse resume: {e}")
        return

    print("\nStep 2: Sending to Gemini and Generating Report...")
    try:
        result = generate_evaluation_report(
            parsed_resume_data=parsed_data, 
            job_description=sample_jd,
            output_filename="Test_Result.docx"
        )
        
        # We access 'report_path' because our function now returns a dictionary
        if result and result.get("status") == "success":
            print(f"\nSUCCESS! Open {result['report_path']} to see the result.")
            print(f"AI Score: {result['data'].get('score_out_of_10')}/10")
        else:
            print("\nFAILED to generate report.")
    except Exception as e:
        print(f"Error during evaluation: {e}")

if __name__ == "__main__":
    run_test()