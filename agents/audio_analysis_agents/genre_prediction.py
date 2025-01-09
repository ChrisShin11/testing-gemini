from .track_prediction import TrackPredictionAgent
import json

class GenrePredictionAgent(TrackPredictionAgent):
    def predict_genres_with_confidence(self, analysis_jsons):
        genres = {
            "genres": [
                { "name": "Pop", "weight": 0.9 },
                { "name": "Rock", "weight": 0.85 },
                { "name": "Jazz", "weight": 0.8 },
                { "name": "Hip-Hop", "weight": 0.87 },
                { "name": "Classical", "weight": 0.75 },
                { "name": "Electronic", "weight": 0.8 },
                { "name": "Lofi", "weight": 0.7 },
                { "name": "Ambient", "weight": 0.6 },
                { "name": "Indie", "weight": 0.8 },
                { "name": "Folk", "weight": 0.7 },
                { "name": "Reggae", "weight": 0.75 },
                { "name": "Country", "weight": 0.8 },
                { "name": "Blues", "weight": 0.75 },
                { "name": "Metal", "weight": 0.8 },
                { "name": "Punk", "weight": 0.7 },
                { "name": "Soul", "weight": 0.8 },
                { "name": "R&B", "weight": 0.85 },
                { "name": "Latin", "weight": 0.75 },
                { "name": "Dance", "weight": 0.85 },
                { "name": "K-Pop", "weight": 0.9 },
                { "name": "J-Pop", "weight": 0.85 },
                { "name": "Trap", "weight": 0.8 },
                { "name": "House", "weight": 0.75 },
                { "name": "Techno", "weight": 0.8 },
                { "name": "Trance", "weight": 0.7 },
                { "name": "Synthwave", "weight": 0.7 },
                { "name": "Chillwave", "weight": 0.65 },
                { "name": "World", "weight": 0.7 },
                { "name": "New Age", "weight": 0.6 },
                { "name": "Soundtrack", "weight": 0.8 },
                { "name": "Acoustic", "weight": 0.65 },
                { "name": "Experimental", "weight": 0.65 },
                { "name": "Industrial", "weight": 0.6 },
                { "name": "Dubstep", "weight": 0.75 },
                { "name": "Garage", "weight": 0.7 },
                { "name": "Grunge", "weight": 0.7 },
                { "name": "Gospel", "weight": 0.65 },
                { "name": "Ska", "weight": 0.6 },
                { "name": "Afrobeat", "weight": 0.8 },
                { "name": "Disco", "weight": 0.7 },
                { "name": "Chiptune", "weight": 0.5 },
                { "name": "Post-Rock", "weight": 0.65 },
                { "name": "Progressive Rock", "weight": 0.75 },
                { "name": "Baroque", "weight": 0.7 },
                { "name": "Opera", "weight": 0.6 },
                { "name": "Swing", "weight": 0.6 },
                { "name": "Bossa Nova", "weight": 0.65 },
                { "name": "Salsa", "weight": 0.7 },
                { "name": "Tango", "weight": 0.6 },
                { "name": "Flamenco", "weight": 0.65 }
            ]
        }

        prompt = """
        You are a music genre prediction expert. Analyze the following image analysis results and suggest the most appropriate music genres based on the visual elements, mood, colors, and scene context.


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

        Return ONLY a JSON object in this exact format, replacing the genre names and confidence scores with the ones that best match the image:
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
