import requests


r = requests.get("http://petroski.cc")
print(r.status_code)
print(r.ok)
print("done")
