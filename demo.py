import requests
import json
from bs4 import BeautifulSoup


api =("http://saral.navgurukul.org/api/courses")
a =requests.get(api)
b = BeautifulSoup(a.text,"html.parser")
res = a.json()
print(b)

with open("file.json","w") as data:
    json.dump(res,data,indent=4)
# print(b)

