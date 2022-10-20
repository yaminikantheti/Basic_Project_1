import json

import requests


mydata=open("data.json","r").read()

base_url="https://reqres.in/api/users"
res=requests.post(base_url,data=json.loads(mydata))
print(res)
print(res.json())

assert res.status_code==201, "Post request is failed"

print(res.headers.get("Content-Type"))
assert res.json()["job"] =='sub-junior', "Job details is not matching"
