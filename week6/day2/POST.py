import requests

payload = {
    "title": "Week 6 Day 2",
    "body": "requests conquered",
    "userId": 1
}

r = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

print(r.status_code)    
print(r.json())         



try:
    r = requests.get("https://api.github.com/users/this_user_does_not_exist_xyz")
    # r.raise_for_status()              # 🚨 throws HTTPError on any 4xx/5xx
    print(r.json()) 
                      # only reached if all is well
except requests.exceptions.HTTPError:
    print("Request failed with status:", r.status_code)



headers = {"Authorization": "Bearer YOUR_TOKEN"}   # the ID card, as a dict entry

r = requests.get(
    "https://api.github.com/users/mohammedkaif911",
    headers=headers
)