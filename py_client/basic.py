import requests

endpoint = "https://www.httpbin.org"

get_response = requests.get(endpoint) # HTTP request
print(get_response)
