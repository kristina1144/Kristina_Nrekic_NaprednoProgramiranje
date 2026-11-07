from rezervacije import ObradaRezervacija


class FakeIzvor:
    def __init__(self, rezervacije):
        self.rezervacije = rezervacije

    def ucitaj(self):
        return self.rezervacije


def test_potvrdjene_rezervacije():
    izvor = FakeIzvor(
        [
            {"broj_osoba": 2, "status": "potvrdjena"},
            {"broj_osoba": 3, "status": "potvrdjena"},
        ]
    )

    obrada = ObradaRezervacija(izvor)
    assert obrada.izracunaj_goste() == 5


def test_otkazane_rezervacije():
    izvor = FakeIzvor(
        [
            {"broj_osoba": 4, "status": "otkazana"},
        ]
    )

    obrada = ObradaRezervacija(izvor)
    assert obrada.izracunaj_goste() == 0


def test_prazna_lista():
    izvor = FakeIzvor([])

    obrada = ObradaRezervacija(izvor)
    assert obrada.izracunaj_goste() == 0
