from google import genai
from dotenv import load_dotenv
from fastapi import HTTPException
import os


load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY") -- not required, as it is being read already by env variables

client = genai.Client()

def ask_question_to_gemini(question):
    try:
        response = client.models.generate_content(model="gemini-3-flash-preview", contents=f"{question}")
        return response.text
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error occurred while fetching the response from Gemini")