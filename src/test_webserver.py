import requests
import json

url_oi = "http://127.0.0.1:4000/index"

headers = {'Accept': 'application/json', 'x-access-tokens': '769db7cf-9d6b-4496-9645-3bd51799583a'}

r = requests.get(url_oi, headers=headers, verify=False)
print(r)
print(r.json())
