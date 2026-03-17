import os
from fastapi import FastAPI, UploadFile, File, Form
from models.schemas import Question
from services.ai_service import ask_question_to_gemini
from services.pdf_service import parse_pdf

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome Msg": "Welcome to the beginning of new life"}

@app.post("/ask")
def ask_question(question: Question):
    response = ask_question_to_gemini(question.text)
    return {f"{question.text}": f"{response}"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    pdf_content = parse_pdf(contents)
    return {"file_name": {file.filename}, "size": len(contents), "pdf_content": pdf_content}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), question: str = Form(...)):
    contents = await file.read()
    pdf_content = parse_pdf(contents)
    response = ask_question_to_gemini(f"{question}: {pdf_content}")
    return {"file_name": {file.filename}, "size": len(contents), "response": response}
