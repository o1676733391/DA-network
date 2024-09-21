import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure the API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Generate content
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)