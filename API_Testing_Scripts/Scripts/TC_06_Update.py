import requests

base_url="https://reqres.in/api/register"
payload={
    "name": "morp"

}
res_put=requests.patch("https://reqres.in/api/users/2",data=payload)
#res=requests.post(base_url,data=payload)
print(res_put)
print(res_put.json())
assert res_put.json()['job']=="zion resident"