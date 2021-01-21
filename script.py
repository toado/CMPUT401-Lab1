import requests

print(requests.__version__)

r = requests.get("https://www.google.com/")

code = requests.get("https://raw.githubusercontent.com/toado/CMPUT401-Lab1/main/script.py")

f = open("script.py", "w")
f.write(code.text)
f.close

print(code.text)
