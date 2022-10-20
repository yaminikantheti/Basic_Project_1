import requests
import json

Base_Url="https://reqres.in"
response = requests.get(Base_Url + "/api/users?page=2")
print(response)
print(response.json())
#print(json.dumps(response.json(), indent=8))
#print(response.content)
#print(response.encoding)
#print(response.headers)
#print(response.headers['content-Type'])
#print(dir(response))
#print(type(response))

#passing assertion for status code

code=response.status_code
assert code == 200,  "Get request is not successful"




