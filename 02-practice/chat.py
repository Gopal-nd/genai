from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# zero short prompting

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='what is 2+2',
    config={
        'max_output_tokens': 40,
        'temperature': 0.9
    }
)

print(response.text)

