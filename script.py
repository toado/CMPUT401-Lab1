import requests

print(requests.__version__)

r = requests.get("https://www.google.com/")

code = requests.get("https://raw.githubusercontent.com/VinnyLuu/CMPUT404Lab1/master/script.py")

f = open("script.py", "w")
f.write(code.text)
f.close

print(code.text)