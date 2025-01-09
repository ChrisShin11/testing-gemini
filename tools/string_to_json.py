import json

def convert_to_json(json_string):
    try:
        # Clean the JSON string
        cleaned_json_string = json_string.strip("```json\n").strip("```\n")
        
        # Parse the JSON string
        genre_data = json.loads(cleaned_json_string)
        return genre_data
    except Exception as e:
        # Handle errors gracefully
        print(f"Error processing JSON: {e}")
        return None
