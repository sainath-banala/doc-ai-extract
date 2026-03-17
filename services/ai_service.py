from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client()

def ask_question_to_gemini(question):
    response = client.models.generate_content(model="gemini-3-flash-preview", contents=f"{question}")
    return response.text
