# DocAI Extract

This is an AI powered document question and answer API.
You can upload any PDF file and ask any question about it.
The API will read the PDF and give you an intelligent answer.

Built with Python, FastAPI, PyMuPDF and Google Gemini AI.

How to run this project

Step 1 - Clone the repository
Step 2 - Create a virtual environment and activate it
Step 3 - Install dependencies using: pip install -r requirements.txt
Step 4 - Create a .env file and add your GEMINI_API_KEY
Step 5 - Run the server using: `uvicorn main:app --reload`
Step 6 - Open browser and go to localhost:8000/docs

Available endpoints

GET  /               - Welcome message
POST /ask            - Ask any general question to Gemini AI
POST /upload         - Upload a PDF and get the extracted text
POST /analyze        - Upload a PDF and ask any question about it
POST /extract-info   - Upload a PDF and ask for any keywords, get the keywords with its values in a json format

Example

Upload your salary slip and ask "what is my net pay"
The API will read the document and answer accurately.
