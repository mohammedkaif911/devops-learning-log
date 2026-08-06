import requests

response = requests.get("https://api.github.com/users/mohammedkaif911")
print(f"[STATUS] Connection established successfully! HTTP Code: {response.status_code}")