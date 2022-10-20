import requests

#Base_Url="https://reqres.in"
#response = requests.get(Base_Url + "/api/users?page=2")

p="page=2"
response=requests.get("https://reqres.in/api/users",params=p)
print(response.url)
json_response=response.json()
print(json_response['total'])
assert json_response['total'] == 12, "Total data is not matching"

print(json_response['total_pages'])
assert json_response['total_pages'] ==2, "Total pages is not matching"

print(json_response["data"][0])
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "Email domain is not macthing"

assert (json_response["data"][1]["email"]).endswith("reqres.in"), "Email domain is not macthing"

print(json_response["data"][5]["last_name"])
assert json_response["data"][5]["last_name"] != None
