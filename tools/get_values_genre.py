import json

def consolidate_jsons(json_list):
    """
    Consolidates specified fields from a list of JSON objects into a single JSON object.

    Args:
        json_list (list): A list of JSON objects (dictionaries).
    
    Returns:
        dict: A consolidated JSON object containing the specified fields.
    """
    consolidated_output = {
        "time_of_day": [],
        "visual_elements": [],
        "scene_type": [],
        "color_harmony": [],
        "main_objects": [],
        "spatial_relationships": [],
        "interactions": []
    }

    # Process each JSON object in the input list
    for json_data in json_list:
        if "time_of_day" in json_data:
            consolidated_output["time_of_day"].append(json_data["time_of_day"])
        
        if "visual_elements" in json_data:
            consolidated_output["visual_elements"].extend(json_data["visual_elements"])
        
        if "scene_type" in json_data:
            consolidated_output["scene_type"].append(json_data["scene_type"])
        
        if "color_harmony" in json_data:
            consolidated_output["color_harmony"].append(json_data["color_harmony"])
        
        if "main_objects" in json_data:
            consolidated_output["main_objects"].extend(json_data["main_objects"])
        
        if "spatial_relationships" in json_data:
            consolidated_output["spatial_relationships"].extend(json_data["spatial_relationships"])
        
        if "interactions" in json_data:
            consolidated_output["interactions"].extend(json_data["interactions"])

    # Deduplicate lists if necessary
    for key, value in consolidated_output.items():
        if isinstance(value, list):
            consolidated_output[key] = list({json.dumps(v): v for v in value}.values())  # Remove duplicates

    return consolidated_output
