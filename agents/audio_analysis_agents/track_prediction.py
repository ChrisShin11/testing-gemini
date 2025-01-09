import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

class TrackPredictionAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel(os.getenv("GEMINI_MODEL_NAME"))

    def predict(self, json_data, prompt):
        # Convert the JSON data to a string representation
        json_str = json.dumps(json_data, indent=2)
        # Combine prompt and data into a single string
        full_prompt = f"{prompt}\n\nAnalysis Data:\n{json_str}"
        response = self.model.generate_content(full_prompt)
        return response.text