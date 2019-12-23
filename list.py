import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://api.coingecko.com/api/v3/coins/list")

jprint(response.json())
