
import requests
import argparse

parser = argparse.ArgumentParser(description="Fetch a clean GitHub profile card")
parser.add_argument("--user", required=True, help="GitHub username to look up")
args = parser.parse_args()

username = args.user 
try:
    r = requests.get(f"https://api.github.com/users/{username}")
    r.raise_for_status()
    data = r.json()
# print(data)

    print("Name : ",data["name"])
    print("Bio : ",data["bio"])
    print("Repos : ",data["public_repos"])
    print("Followers : ",data["followers"])
    print("Joined : ",data["created_at"])
except  requests.exceptions.HTTPError:
    print("Enter a valid username")