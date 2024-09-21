from flask import request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

class ChatbotController:
    @staticmethod
    def handle_message():
        data = request.json
        user_message = data.get('message')
        
        # Generate content using the Generative AI client
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_message)
        
        return jsonify({'response': response.text})