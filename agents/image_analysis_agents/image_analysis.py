import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()  # Load environment variables

class ImageAnalysisAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel(os.getenv('GEMINI_MODEL_NAME'))

    def analyze(self, image_path, prompt):
        img = Image.open(image_path)
        response = self.model.generate_content([prompt, img])
        return response.text