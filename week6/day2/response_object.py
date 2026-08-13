import requests

r = requests.get("https://api.github.com/users/mohammedkaif911")

print(r.status_code)                
print(type(r.text))                 
print(r.headers["Content-Type"])    
print(r.json()["login"])            
# print(r.text["login"]) this will cause type error bcus the r.text will give a string not a list or dict with which we can operate
