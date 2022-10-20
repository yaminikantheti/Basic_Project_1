import requests
import json

p='/api/unknown/23'
base_url="https://reqres.in"



response=requests.get(base_url + p)

print(response.url)
json_resp=response.json()
print(response.json())
assert response.status_code == 200, "Get request is failling"




