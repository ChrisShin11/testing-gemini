import os
import json
from agents.image_analysis_agents.object_detection import ObjectDetectionAgent
from agents.image_analysis_agents.color_analysis import ColorAnalysisAgent
from agents.image_analysis_agents.mood_analysis import MoodAnalysisAgent
from agents.image_analysis_agents.time_analysis import TimeAnalysisAgent
from agents.image_analysis_agents.scene_analysis import SceneAnalysisAgent
from agents.audio_analysis_agents.genre_prediction import GenrePredictionAgent
from tools.string_to_json import convert_to_json  # Import the conversion tool
from tools.get_values_genre import consolidate_jsons
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
    genre_predicting_agent = GenrePredictionAgent()

    # Path to your image
    image_path = "images/jordan.jpg"

    # Analyze image or load from files
    print("🔍 Object Analysis:")
    object_analysis_json = convert_to_json(object_agent.analyze_objects(image_path))
    print(object_analysis_json)
    print("--------------------------------")

    print("🎨 Color Analysis:")
    color_analysis_json = convert_to_json(color_agent.analyze_colors(image_path))
    print(color_analysis_json)
    print("--------------------------------")

    print("🏞️ Scene Analysis:")
    scene_analysis_json = convert_to_json(scene_agent.analyze_scene(image_path))
    print(scene_analysis_json)
    print("--------------------------------")

    print("😊 Mood Analysis:")
    mood_analysis_json = convert_to_json(mood_agent.analyze_mood(image_path))
    print(mood_analysis_json)
    print("--------------------------------")

    print("🕒 Time Analysis:")
    time_analysis_json = convert_to_json(time_agent.analyze_time(image_path))
    print(time_analysis_json)
    print("--------------------------------")

    list_of_jsons = [object_analysis_json, color_analysis_json, scene_analysis_json, mood_analysis_json, time_analysis_json]
    genre_prediction_json = consolidate_jsons(list_of_jsons)
    print(genre_prediction_json)
    print("--------------------------------")


if __name__ == "__main__":
    main()
