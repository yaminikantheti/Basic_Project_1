import requests

base_url="https://reqres.in/api/users"
payload={
    "name": "Yami",
    "job": "leader"
}
res=requests.post(base_url,data=payload)

print(res)
print(res.json())

assert res.status_code==201, "Post request is failed"

