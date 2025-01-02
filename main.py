import os
import json
from agents.image_analysis_agents.object_detection import ObjectDetectionAgent
from agents.image_analysis_agents.color_analysis import ColorAnalysisAgent
from agents.image_analysis_agents.mood_analysis import MoodAnalysisAgent
from agents.image_analysis_agents.time_analysis import TimeAnalysisAgent
from agents.image_analysis_agents.scene_analysis import SceneAnalysisAgent
from agents.audio_analysis_agents.genre_prediction import GenrePredictionAgent
from tools.string_to_json import convert_to_json  # Import the conversion tool

# Directory to save and load analysis JSONs
SAVE_DIR = "analysis_results"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_json(data, filename):
    """Save JSON data to a file."""
    with open(os.path.join(SAVE_DIR, filename), "w") as f:
        json.dump(data, f, indent=4)

def load_json(filename):
    """Load JSON data from a file."""
    filepath = os.path.join(SAVE_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return None

def main():
    # Initialize agents
    object_agent = ObjectDetectionAgent()
    color_agent = ColorAnalysisAgent()
    mood_agent = MoodAnalysisAgent()
    time_agent = TimeAnalysisAgent()
    scene_agent = SceneAnalysisAgent()
    genre_predictor = GenrePredictionAgent()

    # Path to your image
    image_path = "images/brown-barber.jpg"

    # Analyze image or load from files
    print("🔍 Object Analysis:")
    object_analysis_json = load_json("object_analysis.json") or convert_to_json(object_agent.analyze_objects(image_path))
    if object_analysis_json:
        save_json(object_analysis_json, "object_analysis.json")
    print(object_analysis_json)

    print("\n🎨 Color Analysis:")
    color_analysis_json = load_json("color_analysis.json") or convert_to_json(color_agent.analyze_colors(image_path))
    if color_analysis_json:
        save_json(color_analysis_json, "color_analysis.json")
    print(color_analysis_json)

    print("\n😊 Mood Analysis:")
    mood_analysis_json = load_json("mood_analysis.json") or convert_to_json(mood_agent.analyze_mood(image_path))
    if mood_analysis_json:
        save_json(mood_analysis_json, "mood_analysis.json")
    print(mood_analysis_json)

    print("\n⏰ Time Analysis:")
    time_analysis_json = load_json("time_analysis.json") or convert_to_json(time_agent.analyze_time(image_path))
    if time_analysis_json:
        save_json(time_analysis_json, "time_analysis.json")
    print(time_analysis_json)

    print("\n🏠 Scene Analysis:")
    scene_analysis_json = load_json("scene_analysis.json") or convert_to_json(scene_agent.analyze_scene(image_path))
    if scene_analysis_json:
        save_json(scene_analysis_json, "scene_analysis.json")
    print(scene_analysis_json)

    # Combine analysis results (assuming successful conversions)
    analysis_jsons = [
        object_analysis_json,
        color_analysis_json,
        mood_analysis_json,
        time_analysis_json,
        scene_analysis_json,
    ]

    # Predict genres with confidence levels
    genre_confidences = genre_predictor.predict_genres_with_confidence(analysis_jsons)
    print("\n🎵 Genre Prediction with Confidence Levels:")
    print(genre_confidences)

if __name__ == "__main__":
    main()
