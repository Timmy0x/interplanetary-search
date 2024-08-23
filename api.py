import requests
import json

def api_search(query):
    data = requests.get(f"https://www.googleapis.com/customsearch/v1?key=AIzaSyDc7p8bARCpsJfhfz7N-4uqGKRL8K6-2D0&cx=c53408e7d5b1447bd&q={query}").text
    data = json.loads(data)

    keys_to_exclude = []
    filtered_items = []
    for item in data["items"]:
        filtered_item = {key: value for key, value in item.items() if key not in keys_to_exclude}
        filtered_items.append(filtered_item)
    
    data["items"] = filtered_items

    return data["items"]