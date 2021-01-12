import requests

print("requests version: {}\n".format(requests.__version__))

response = requests.get("http://www.google.com").status_code
print("response code: {}\n".format(response))

raw_code = requests.get("https://raw.githubusercontent.com/toado/CMPUT401-Lab1/main/requests_version_script.py").text
print(raw_code)
