import requests

#dodawanie przykladowej dodatkowej uslugi

BASE = "http://127.0.0.1:5000"

response = requests.put(BASE + "/v1/additionalservice", {
    "reservation_id": 1,
    "name": "odkurzanie",
    "unit_price": 1000,
    "date_from": "01.01.2999",
    "date_to": "01.01.29999"
   } )
print(response.json())