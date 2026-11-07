from typing import Protocol


class IzvorPodataka(Protocol):
    def ucitaj(self) -> list[dict]: ...


class Izvjestavanje(Protocol):
    def prikazi(self, broj_gostiju: int) -> None: ...


class IzvorRezervacija:
    def __init__(self):
        self.rezervacije = [
            {"ime": "Ana", "broj_osoba": 2, "status": "potvrdjena"},
            {"ime": "Marko", "broj_osoba": 4, "status": "otkazana"},
            {"ime": "Jovana", "broj_osoba": 3, "status": "potvrdjena"},
        ]

    def ucitaj(self) -> list[dict]:
        return self.rezervacije


class ObradaRezervacija:
    def __init__(self, izvor: IzvorPodataka):
        self.izvor = izvor

    def izracunaj_goste(self) -> int:
        ukupno = 0

        for rezervacija in self.izvor.ucitaj():
            if rezervacija["status"] == "potvrdjena":
                ukupno += rezervacija["broj_osoba"]

        return ukupno


class Izvjestaj:
    def prikazi(self, broj_gostiju: int) -> None:
        print("Ukupno gostiju:", broj_gostiju)


def pokreni_obradu(
    izvor: IzvorPodataka,
    izvjestaj: Izvjestavanje,
) -> None:
    obrada = ObradaRezervacija(izvor)
    broj_gostiju = obrada.izracunaj_goste()
    izvjestaj.prikazi(broj_gostiju)
