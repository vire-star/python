# API - application programming interface

from dotenv import load_dotenv
import os
from google import genai


# .env file ko load karna

load_dotenv()


# api key lo

api_key = os.getenv("GEMINI_API")

# client banao

client = genai.Client(api_key=api_key)

# sawal puchoo

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="python kya hai? 3 line mai explain karo"


)

print(response.text)