from .image_analysis import ImageAnalysisAgent

class SceneAnalysisAgent(ImageAnalysisAgent):
    def analyze_scene(self, image_path):
        prompt = """
        Analyze this image and identify:
        1. The overall scene type (e.g., indoor, outdoor, nature, urban).
        2. The dominant features of the scene (e.g., architecture, vegetation, water bodies).
        3. The general mood or atmosphere of the scene (e.g., calm, bustling, festive).
        4. Any notable details or points of interest.
        Provide the output in a structured JSON format like this:
        {
            "scene_type": "Description of the overall scene type",
            "dominant_features": [
                {"feature": "Feature Name", "details": "Additional details"}
            ],
            "mood": "Description of the general mood or atmosphere",
            "notable_details": [
                {"detail": "Description of notable detail"}
            ]
        }
        """
        return self.analyze(image_path, prompt)