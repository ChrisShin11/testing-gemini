import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load environment variables


class TrackPredictionAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel(os.getenv("GEMINI_MODEL_NAME"))

    def predict(self, prompt):
        response = self.model.generate_content([prompt])
        return response.text