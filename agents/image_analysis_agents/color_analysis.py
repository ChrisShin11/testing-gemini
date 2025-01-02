from .image_analysis import ImageAnalysisAgent

class ColorAnalysisAgent(ImageAnalysisAgent):
    def analyze_colors(self, image_path):
        prompt = """
        Analyze the colors in this image:
        1. Dominant colors
        2. Color palette
        3. Color harmony
        Provide the output in a structured JSON format like this:
        {
            "dominant_colors": [
                {"color": "Color Name/Hex Code", "details": "Additional details"}
            ],
            "color_palette": ["Color Hex Code 1", "Color Hex Code 2", "..."],
            "color_harmony": "Description of the harmony or contrast in colors"
        }
        """
        return self.analyze(image_path, prompt)