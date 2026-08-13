import requests

response = requests.get("https://api.github.com/users/mohammedkaif911")
print(response.status_code)   # the status LINE you saw in curl
print(response.json())        # the JSON body, turned into a Python dict!