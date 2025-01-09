import json

def get_highest_confidence_genres(list_of_predicted_genres):
    highest_genres = []  # To store the highest confidence genres for each JSON string
    for object_predicted_genres in list_of_predicted_genres:
        try:
            # Clean the JSON string
            object_predicted_genres = object_predicted_genres.strip("```json\n").strip("```\n")
            
            # Parse the JSON string
            genre_data = json.loads(object_predicted_genres)
            
            # Find the highest confidence genre
            highest_genre = max(genre_data.values(), key=lambda x: x["confidence"])
            
            # Append the result
            highest_genres.append(highest_genre['name'])
        except Exception as e:
            # Handle errors gracefully
            print(f"Error processing JSON: {e}")
            highest_genres.append(None)  # Append None if there's an error
    
    return highest_genres
