import json
import urllib.request

url = "https://official-joke-api.appspot.com/jokes/programming/random"
with urllib.request.urlopen(url) as response:
    joke = json.loads(response.read().decode())[0]
    print(f"😂 {joke['setup']}")
    print(f"punchline: {joke['punchline']}")