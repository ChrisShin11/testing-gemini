from .track_prediction import TrackPredictionAgent
import json

class EnergyPredictionAgent(TrackPredictionAgent):
    def predict_energy_with_confidence(self, analysis_jsons):
        prompt = """
        You are a visual analysis expert. Analyze the following image analysis results and suggest the most appropriate energy level based on the visual elements, mood, colors, and scene context.

        Instructions:
        1. Consider all aspects of the image analysis:
           - Objects and scene elements
           - Color palette and visual mood
           - Time of day/lighting
           - Overall atmosphere and context

        2. Select exactly 3 genres that best match the visual elements:
           - Primary genre: Should strongly align with the dominant visual elements
           - Secondary genre: Should complement the primary genre and reflect secondary elements
           - Tertiary genre: Can be more experimental or reflect subtle nuances

        3. Assign confidence scores (0.0 to 1.0) based on:
           - How well the genre matches the visual elements
           - The presence of genre-typical visual indicators
           - The overall context and mood alignment

        Return ONLY a JSON object in this exact format:
        {{
            "primary_genre": {{"name": "Genre1", "confidence": 0.9}},
            "secondary_genre": {{"name": "Genre2", "confidence": 0.7}},
            "tertiary_genre": {{"name": "Genre3", "confidence": 0.5}}
        }}
        """

        try:
            response = self.predict(analysis_jsons, prompt)
            result = json.loads(response)
            return result
        except json.JSONDecodeError:
            return {
                "primary_genre": {"name": "unknown", "confidence": 0.0},
                "secondary_genre": {"name": "unknown", "confidence": 0.0},
                "tertiary_genre": {"name": "unknown", "confidence": 0.0}
            }
