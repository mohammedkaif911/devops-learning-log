import requests

# API 1 — a random joke
try:
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    r.raise_for_status()                    
    data = r.json()
    print("JOKE:", data["setup"], "...", data["punchline"])
except requests.exceptions.HTTPError:
    print("Request failed with status:", r.status_code)

# API 2 - bitcoin price in rupees
try:
    r = requests.get("https://api.coingecko.com/api/v3/simple/price",params= {"ids": "bitcoin", "vs_currencies": "inr"})
    r.raise_for_status()
    data = r.json()
    print(data["bitcoin"] ["inr"],"Rs")
except requests.exceptions.HTTPError:
    print("Request failed with status:", r.status_code)

# API 3 - Bengaluru weather rn
try:
    r = requests.get("https://api.open-meteo.com/v1/forecast",params= {"latitude": 12.97, "longitude": 77.59, "current_weather": "true"})
    r.raise_for_status()
    data = r.json()
    print(data["current_weather"]["temperature"],"is the Temperature")   # → 22.6
except requests.exceptions.HTTPError:
    print("Request failed with status:", r.status_code)