import json
import os
from typing import Any, Dict
from litellm import completion

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"



def get_itinerary(destination: str) -> Dict[str, Any]:
    """
    Returns a JSON-like dict with keys:
      - destination
      - price_range
      - ideal_visit_times
      - top_attractions
    """
    # implement litellm call here to generate a structured travel itinerary for the given destination

    # See https://docs.litellm.ai/docs/ for reference.

    data = completion(
        model = MODEL,
        response_format={ "type": "json_object" },
        messages=[
          {"role": "system", "content": "You are a helpful travel assistant \
           designed to output JSON. Given a destination, you will advise the user on \
           a travel itinerary with the following json keys: 1. destination 2. price range \
           3. ideal_visit_times 4. top_attractions"},
          {"role": "user", "content": f"Create a itinerary for {destination}"}
        ]
    )
    

    return json.loads(data.choices[0].message.content)

