import requests

#wyswietlenie wsyzstkich dodatkowych uslug

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/v1/additionalservice" )
print(response.json())