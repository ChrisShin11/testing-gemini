import json

def convert_to_json(text_data):
    """
    Attempts to convert a string representation of JSON data to a JSON object.

    Args:
        text_data: The string containing the JSON data.

    Returns:
        A JSON object if the conversion is successful, otherwise None.
    """
    try:
        # Remove Markdown markers if present
        if text_data.strip().startswith("```") and text_data.strip().endswith("```"):
            text_data = "\n".join(text_data.strip().splitlines()[1:-1])
        
        # Convert the string to JSON
        return json.loads(text_data)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    return None
