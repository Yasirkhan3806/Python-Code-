import json
import sys
import requests


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
iterate = response.json()
for result in iterate["results"]:
    print(result["trackName"])