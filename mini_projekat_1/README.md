Mini projekat 1 - Refaktoring obrade 

Za ovaj zadatak koristila sam Python 3.13, Google Colab, ChatGPT, pytest i ruff.

Zadatak je bio da se početni kod za obradu rezervacija podijeli na klase i funkcije primjenom SOLID principa S i D.

**AI upiti:**

- Napravi jednostavnu Python skriptu za obradu rezervacija u restoranu.
- Refaktoriši kod primjenom principa Single Responsibility i Dependency Inversion.
- Dodaj Protocol za izvor podataka i izvještavanje.
- Napiši tri pytest testa koristeći zamjenski izvor podataka.

**Šta je promijenjeno:**

Početni kod je koristio globalnu listu rezervacija i jedna funkcija je obavljala obradu i ispis rezultata.

Kod je zatim podijeljen tako da svaka klasa ima svoju odgovornost. Dodati su Protocol interfejsi, a klasa za obradu više ne zavisi direktno od konkretnog izvora podataka.

**Uočeni nedostaci i ispravke:**

Početni kod nije imao jasno odvojene odgovornosti, tipove ni automatske testove. Prilikom refaktorisanja dodate su posebne klase, tipovi i Protocol interfejsi. Za testiranje je napravljen FakeIzvor kako testovi ne bi zavisili od stvarnih podataka.

**Testiranje:**

Testirana su tri slučaja: potvrđene rezervacije, otkazane rezervacije i prazna lista.

Rezultati:
- pytest: 3 passed
- ruff check: All checks passed!
- ruff format: 2 files already formatted

Kroz zadatak sam vidjela kako se jedan jednostavan kod može organizovati tako da bude pregledniji, lakši za testiranje i jednostavniji za kasnije izmjene.
