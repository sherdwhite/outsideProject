import requests

from api.utils import find_astronomical_object


# This API has limited fuzzy search capabilities despite the documentation.
# I am parsing the search text to find a subset of astronomical object notations
# and using the return object to populate the additional data field in the Picture model.
def get_wikipedia_summary(search_text, limit=1):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    object_id = find_astronomical_object(search_text)

    if object_id:
        PARAMS = {
            "action": "opensearch",
            "namespace": "0",
            "search": object_id,
            "limit": str(limit),
            "format": "json",
        }

        response = S.get(url=URL, params=PARAMS)
        data = response.json()

        return data
    else:
        return "Additional data not found."
