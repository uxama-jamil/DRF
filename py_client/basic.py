import requests

endpoint = "https://www.httpbin.org"

get_response = requests.get(endpoint,verify=False) # HTTP request
print(get_response.status_code) #printing raw text response or source code

