Mini projekat 3 – testiran i obezbijeđen API

Za ovaj projekat koristim FastAPI primjer obračuna cijene rezervacije sa predavanja iz nedjelje 5. Dodala sam testove i bezbjednosne provjere iz nedjelje 6.

API ima dvije rute:
- GET /health – provjerava da li servis radi.
- POST /cijena – računa cijenu rezervacije na osnovu broja noćenja, cijene po noći i popusta.

Za /cijena potreban je API ključ u zaglavlju X-API-Key. Broj noćenja mora biti od 1 do 30, cijena mora biti pozitivna, a popust od 0 do 1. Neispravni podaci vraćaju status 422. Bez ključa se vraća 401, a ako ključ nije podešen na serveru 503.

Pokretanje na računaru (Python 3.12+):

    python -m pip install -r requirements.txt

U PowerShell-u prvo postaviti ključ (izabrati sopstveni, ne objavljivati ga):

    $env:API_KEY="moj-lokalni-dugacak-tajni-kljuc"
    uvicorn main:app --reload

API dokumentacija: http://127.0.0.1:8000/docs
U dokumentaciji otvoriti Authorize i unijeti API ključ. Primjer zahtjeva za /cijena:

    {"noci": 3, "cijena_noci": 80, "popust": 0.1}

Očekivani iznos je 216.0.

Provjere projekta:

    python -m pytest -q
    ruff check .
    mypy main.py
    bandit -q main.py
    pip-audit -r requirements.txt

Testovi pokrivaju ispravne vrijednosti, granice, nedozvoljene ulaze i API ključ. GitHub Actions automatski pokreće sve navedene provjere pri push-u i pull request-u.

Bezbjednosni rizici i mjere:
1. Neovlašćen pristup – /cijena zahtijeva API ključ. Pravi ključ čuva se u varijabli okruženja, ne u GitHub repozitorijumu. Za javni servis potrebno je dodati HTTPS i jači sistem identiteta/ograničavanje zahtjeva.
2. Neispravni podaci – Pydantic ograničava broj noći, cijenu i popust. Testovi provjeravaju i rubne slučajeve.
3. Ranjive biblioteke – pip-audit provjerava poznate ranjivosti u zavisnostima. Ažuriranja treba provjeravati redovno.
4. Greške u kodu – ruff, mypy, pytest i bandit provjeravaju kvalitet i potencijalne bezbjednosne probleme.

Bezbjednosni pregled: bandit i pip-audit su uključeni u CI, tako da eventualni nalaz zaustavlja provjeru i traži pregled i ispravku prije predaje. Nalazi se provjeravaju u kartici Actions. Projektni API je edukativni primjer, ne gotov produkcioni sistem.
