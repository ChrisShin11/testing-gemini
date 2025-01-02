from .image_analysis import ImageAnalysisAgent

class MoodAnalysisAgent(ImageAnalysisAgent):
    def analyze_mood(self, image_path):
        prompt = """
        Analyze the mood and atmosphere of this image:
        1. Overall emotional tone
        2. Contributing visual elements
        3. Emotional impact
        Provide the output in a structured JSON format like this:
        {
            "emotional_tone": "Description of the overall emotional tone",
            "visual_elements": [
                {"element": "Visual Element Name", "details": "Additional details"}
            ],
            "emotional_impact": "Description of the emotional impact"
        }
        """
        return self.analyze(image_path, prompt)