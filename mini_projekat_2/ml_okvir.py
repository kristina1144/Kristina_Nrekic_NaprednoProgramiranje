"""Jednostavan okvir za ML eksperimente sa projektnim šablonima."""

from abc import ABC, abstractmethod
from functools import wraps
from time import perf_counter

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


# Factory: ime modela se mapira na klasu / konstruktor.
MODELI = {
    "linearni": LogisticRegression,
    "stablo": DecisionTreeClassifier,
    "knn": KNeighborsClassifier,
}


def kreiraj_model(naziv):
    if naziv not in MODELI:
        raise ValueError(f"Nepoznat model: {naziv}")
    if naziv == "linearni":
        return MODELI[naziv](max_iter=200, random_state=42)
    if naziv == "stablo":
        return MODELI[naziv](random_state=42)
    return MODELI[naziv]()


# Strategy: svaka metrika ima isti potpis (tacno, predvidjeno).
METRIKE = {
    "accuracy": accuracy_score,
    "f1": lambda tacno, predvidjeno: f1_score(
        tacno, predvidjeno, average="macro"
    ),
}


def izracunaj_metriku(naziv, tacno, predvidjeno):
    if naziv not in METRIKE:
        raise ValueError(f"Nepoznata metrika: {naziv}")
    return float(METRIKE[naziv](tacno, predvidjeno))


# Decorator: mjeri vrijeme bez izmjene osnovne metode.
def mjeri_vrijeme(funkcija):
    @wraps(funkcija)
    def omotac(*args, **kwargs):
        pocetak = perf_counter()
        rezultat = funkcija(*args, **kwargs)
        trajanje = perf_counter() - pocetak
        print(f"Trajanje {funkcija.__name__}: {trajanje:.4f} s")
        return rezultat

    return omotac


# Template Method: redoslijed ucitavanja, pripreme, treninga i evaluacije.
class Eksperiment(ABC):
    def __init__(self):
        self.pretplatnici = []

    # Observer: svi pretplaceni dobijaju obavjestenje o dogadjaju.
    def pretplati(self, funkcija):
        self.pretplatnici.append(funkcija)

    def objavi(self, dogadjaj, **podaci):
        for funkcija in self.pretplatnici:
            funkcija(dogadjaj, **podaci)

    def pokreni(self):
        podaci = self.ucitaj()
        podaci = self.pripremi(podaci)
        model = self.treniraj(podaci)
        return self.evaluiraj(model, podaci)

    @abstractmethod
    def ucitaj(self):
        pass

    @abstractmethod
    def pripremi(self, podaci):
        pass

    @abstractmethod
    def treniraj(self, podaci):
        pass

    @abstractmethod
    def evaluiraj(self, model, podaci):
        pass


class IrisEksperiment(Eksperiment):
    def __init__(self, naziv_modela="linearni", metrika="accuracy"):
        super().__init__()
        self.naziv_modela = naziv_modela
        self.metrika = metrika

    def ucitaj(self):
        iris = load_iris()
        return iris.data, iris.target

    def pripremi(self, podaci):
        x, y = podaci
        return train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

    @mjeri_vrijeme
    def treniraj(self, podaci):
        x_trening, _, y_trening, _ = podaci
        model = kreiraj_model(self.naziv_modela)
        self.objavi("pocetak_treninga", model=self.naziv_modela)
        model.fit(x_trening, y_trening)
        self.objavi("kraj_treninga", model=self.naziv_modela)
        return model

    def evaluiraj(self, model, podaci):
        _, x_test, _, y_test = podaci
        predvidjeno = model.predict(x_test)
        rezultat = izracunaj_metriku(self.metrika, y_test, predvidjeno)
        self.objavi("kraj_evaluacije", metrika=self.metrika, rezultat=rezultat)
        return rezultat


def ispisi_dogadjaj(dogadjaj, **podaci):
    print(f"Dogadjaj: {dogadjaj} | {podaci}")


if __name__ == "__main__":
    for naziv in MODELI:
        eksperiment = IrisEksperiment(naziv, "accuracy")
        eksperiment.pretplati(ispisi_dogadjaj)
        rezultat = eksperiment.pokreni()
        print(f"{naziv}: accuracy = {rezultat:.3f}\n")
