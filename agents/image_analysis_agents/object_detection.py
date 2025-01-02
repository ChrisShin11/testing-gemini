from .image_analysis import ImageAnalysisAgent

class ObjectDetectionAgent(ImageAnalysisAgent):
    def analyze_objects(self, image_path):
        prompt = """
        Analyze this image and identify:
        1. Main objects present
        2. Their spatial relationships
        3. Any notable interactions between objects
        Provide the output in a structured JSON format like this:
        {
            "main_objects": [
                {"object": "Object Name", "details": "Details about the object"}
            ],
            "spatial_relationships": [
                {"relationship": "Description of spatial relationship"}
            ],
            "interactions": [
                {"interaction": "Description of interaction"}
            ]
        }
        
        """
        return self.analyze(image_path, prompt)