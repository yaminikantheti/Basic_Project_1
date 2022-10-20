import json

import jsonpath as jsonpath
import requests



# API URL
base_url = "https://reqres.in/api/users"

def test_create_new_user():
    # Read input from json file
    file = open("C:\\Users\\HP\\PycharmProjects\\Basic_Project\\API_Testing_Scripts\\Scripts\\data.json" , 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # make POST request
    response=requests.post(base_url, request_json)
    # validating the response code
    assert response.status_code == 201
    # Fetch header from response
    print(response.headers.get("Content-Length"))
    # Parse the response to Json Format
    response_json = json.loads(response.text)
    # Pick ID using Json Path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])











