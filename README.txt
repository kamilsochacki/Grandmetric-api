Celem zadania jest implementacja usługi, która przechowuje informacje o dodatkowych usługach związanych z rezerwacją oraz stworzenie kontenera z tą usługą

Usługa dodatkowa posiada atrybuty:
id - unikalny identyfikator dodatku (generowany automatycznie)
reservation_id - identyfikator rezerwacji, z którą związana jest usługa
name - nazwa danej usługi (np. sprzątanie, parking podziemny itp)
unit_price - cena jednostkowa za usługę
date_from - data rozpoczęcia świadczenia usługi
date_to - data zakończenia świadczenia usługi

- usługa posiada trzy endpointy (dostępne np. przez http://localhost:5000/):
  - POST /v1/additional-service - tworzenie nowej usługi w bazie poprzez wysłanie payloadu np.:
   {
    "reservation_id": 10,
    "name": "sprzątanie",
    "unit_price": 1000.00,
    "date_from": "01.01.2021",
    "date_to": "31.03.2021"
   }

  - GET /v1/additional-service - pobranie wszystkich dodatkowych usług
  - GET /v1/additional-service/{id} - pobranie usługi o id wskazanym w ścieżce
---------------------------------------------------------------------------------------------------

Uruchomienie:

1. Pobierz repozytorium
2. Potrzebujesz Python 3.8.1 oraz Docker 20.10.2 lub wyżej
3. Zbuduj obraz dockerowy poleceniem: docker biuld -t [nazwa obrazu]
4. Uruchom kontener poleceniem: docker run -p 5000:5000 [nazwa obrazu]. Aplikacja uruchamia się w trybie debug i zwraca informację o wysłanych zapytaniach POST oraz GET
5. Usługa dostępna będzie pod adresem http://localhost:5000
6. Z poziomu kontenera poleceniem: python post-example.py dodasz przykładową usługę w bazie
7. Z poziomu kontenera poleceniem: python get-all.py wyświetlisz wszystkie usługi, podobnie pod adresem http://localhost:5000/v1/additionalservice wyświetlisz wsyzstkie usługi w przeglądarce
8. http://localhost:5000/v1/additionalservice/{id} zwróci informacje tylko o konkretnej usłudze (jeżeli usługa o takim id istnieje). Usługa uruchamia się z dwoma testowymi dodatkowymi
 usługami w bazie o id 0 oraz 1
