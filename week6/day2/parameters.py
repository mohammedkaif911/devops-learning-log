import requests

params = {"sort": "updated", "per_page": 3}
r = requests.get("https://api.github.com/users/mohammedkaif911/repos",params = {"per_page": 1})

print(r.url)          #
print(len(r.json()))  
print(r.json()[0]["name"])