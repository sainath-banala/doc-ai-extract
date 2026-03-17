import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from models.schemas import Question
from services.ai_service import ask_question_to_gemini
from services.pdf_service import parse_pdf

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome Msg": "Welcome to the beginning of new life"}

@app.post("/ask")
def ask_question(question: Question):
    if not question.text:
        raise HTTPException(status_code=400, detail="please pass a valid question")
    response = ask_question_to_gemini(question.text)
    return {f"{question.text}": f"{response}"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_content = parse_pdf(contents)
    if not pdf_content:
        raise HTTPException(status_code=400, detail="pdf appears to be empty or unreadable")
    return {"file_name": {file.filename}, "size": len(contents), "pdf_content": pdf_content}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), question: str = Form(...)):
    contents = await file.read()
    pdf_content = parse_pdf(contents)
    if not pdf_content:
        raise HTTPException(status_code=400, detail="pdf appears to be empty or unreadable")
    response = ask_question_to_gemini(f"{question}: {pdf_content}")
    return {"file_name": {file.filename}, "size": len(contents), "response": response}

@app.post("/extract-info")
async def extract_info(file: UploadFile = File(..., description="Upload any PDF document"), keywords: str = Form(..., description="Comma separated keywords to extract. Example: name, value1, value2")):
    contents = await file.read()
    pdf_content = parse_pdf(contents)
    if not pdf_content:
        raise HTTPException(status_code=400, detail="pdf appears to be empty or unreadable")
    response = ask_question_to_gemini(f"Extract the following keywords {keywords} from the document. Return only valid JSON with these exact keys. If a keyword is not found set its value to null. No explanation, no markdown, no code blocks: {pdf_content}")
    return {"file_name": {file.filename}, "size": len(contents), "response": response.replace("```json", "").replace("```", "")}
