from .image_analysis import ImageAnalysisAgent

class TimeAnalysisAgent(ImageAnalysisAgent):
    def analyze_time(self, image_path):
        prompt = """
        Analyze the image to determine:
        1. Time of day (if possible)
        2. Lighting conditions
        3. Any temporal indicators
        Provide the output in a structured JSON format like this:
        {
            "time_of_day": "Description of the time of day",
            "lighting_conditions": "Description of the lighting conditions",
            "temporal_indicators": [
                {"indicator": "Indicator Name", "details": "Additional details"}
            ]
        }
        """
        return self.analyze(image_path, prompt)