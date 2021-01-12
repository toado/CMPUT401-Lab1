import requests

print("requests version: {}\n".format(requests.__version__))

response = requests.get("http://www.google.com")
print("response code: {}".format(response.status_code))




