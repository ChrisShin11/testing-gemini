from .track_prediction import TrackPredictionAgent
import json

class GenrePredictionAgent(TrackPredictionAgent):
    def predict_genres_with_confidence(self, analysis_jsons):
        base_prompt = """
        Based on the following image analysis results, 
        suggest 3-5 relevant music genres and their corresponding confidence levels for each analysis. 

        **Image Analysis Results:**
        {formatted_data}

        **Output Format:**
        Provide the output as a JSON array where each element corresponds to an analysis JSON with the following structure:
        [
            {{"genre1": 0.8, "genre2": 0.6, "genre3": 0.4}},
            ...
        ]

        Where:
        - Each object represents the genre suggestions for one analysis JSON.
        - "genre1", "genre2", "genre3" are the suggested genres.
        - 0.8, 0.6, 0.4 are their respective confidence levels (between 0 and 1).

        **Note:** 
        * Confidence levels should reflect the certainty of each genre suggestion. 
        * Use values like 0.9 for very high confidence and 0.1 for low confidence.
        """

        results = []

        for index, analysis_json in enumerate(analysis_jsons, start=1):
            # Dynamically format JSON data into the prompt
            def format_value(value):
                if isinstance(value, list):
                    return ', '.join(
                        json.dumps(item) if isinstance(item, dict) else str(item)
                        for item in value
                    )
                return str(value)

            formatted_data = "\n".join(
                f"* **{key.capitalize()}:** {format_value(value)}"
                for key, value in analysis_json.items()
            )
            
            # Construct the final prompt
            formatted_prompt = base_prompt.format(formatted_data=formatted_data)
            print(f"Formatted Prompt for JSON {index}:", formatted_prompt)  # Debugging

            # Call Gemini to generate genre suggestions with confidence levels
            response = self.predict(formatted_prompt)
            print("Raw Response: ", response)

            # Clean the response by removing backticks
            cleaned_response = response.strip('```json').strip('```').strip()
            print("Cleaned Response: ", cleaned_response)

            try:
                # Parse the cleaned JSON response
                response_json = json.loads(cleaned_response)

                # Add the parsed response to results
                results.append(response_json)

            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing Gemini response for JSON {index}: {e}")
                print("Raw Response:", response)
                results.append({})  # Append empty dict for error cases

        return results
