import requests
import json

# Requests: GET, POST, PUT, DELETE
def fetch_data(url):
    response = requests.get(url)
    if url.endswith('.txt'):
        return response.content
    else:
        data = response.json()
        return data


def create_json_file(filename, lst):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(lst, f, ensure_ascii=False, indent=4)
