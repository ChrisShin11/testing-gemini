import google.generativeai as genai
from PIL import Image
import os

# Configure the API
genai.configure(api_key="")

class ImageAnalysisAgent:
    def __init__(self, model_name="gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)
    
    def analyze(self, image_path, prompt):
        img = Image.open(image_path)
        response = self.model.generate_content([prompt, img])
        return response.text

class ObjectDetectionAgent(ImageAnalysisAgent):
    def analyze_objects(self, image_path):
        prompt = """
        Analyze this image and identify:
        1. Main objects present
        2. Their spatial relationships
        3. Any notable interactions between objects
        Be specific but concise.
        """
        return self.analyze(image_path, prompt)

class ColorAnalysisAgent(ImageAnalysisAgent):
    def analyze_colors(self, image_path):
        prompt = """
        Analyze the colors in this image:
        1. Dominant colors
        2. Color palette
        3. Color harmony
        Be specific but concise.
        """
        return self.analyze(image_path, prompt)

class MoodAnalysisAgent(ImageAnalysisAgent):
    def analyze_mood(self, image_path):
        prompt = """
        Analyze the mood and atmosphere of this image:
        1. Overall emotional tone
        2. Contributing visual elements
        3. Emotional impact
        Be specific but concise.
        """
        return self.analyze(image_path, prompt)

class TimeAnalysisAgent(ImageAnalysisAgent):
    def analyze_time(self, image_path):
        prompt = """
        Analyze the image to determine:
        1. Time of day (if possible)
        2. Lighting conditions
        3. Any temporal indicators
        Be specific but concise.
        """
        return self.analyze(image_path, prompt)

def main():
    # Initialize agents
    object_agent = ObjectDetectionAgent()
    color_agent = ColorAnalysisAgent()
    mood_agent = MoodAnalysisAgent()
    time_agent = TimeAnalysisAgent()
    
    # Path to your image
    image_path = "images/blue-clubbing.jpg"
    
    # Analyze image with all agents
    print("🔍 Object Analysis:")
    print(object_agent.analyze_objects(image_path))
    print("\n🎨 Color Analysis:")
    print(color_agent.analyze_colors(image_path))
    print("\n😊 Mood Analysis:")
    print(mood_agent.analyze_mood(image_path))
    print("\n⏰ Time Analysis:")
    print(time_agent.analyze_time(image_path))

if __name__ == "__main__":
    main()