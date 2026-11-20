import pytest

from ml_okvir import (
    IrisEksperiment,
    izracunaj_metriku,
    kreiraj_model,
    mjeri_vrijeme,
)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def test_factory_linearni():
    assert isinstance(kreiraj_model("linearni"), LogisticRegression)


def test_factory_stablo():
    assert isinstance(kreiraj_model("stablo"), DecisionTreeClassifier)


def test_factory_knn():
    assert isinstance(kreiraj_model("knn"), KNeighborsClassifier)


def test_factory_nepoznat_model():
    with pytest.raises(ValueError, match="Nepoznat model"):
        kreiraj_model("nepostojeci")


def test_strategy_accuracy():
    assert izracunaj_metriku("accuracy", [0, 1, 2], [0, 1, 0]) == pytest.approx(2 / 3)


def test_strategy_f1():
    assert izracunaj_metriku("f1", [0, 1, 2], [0, 1, 2]) == 1.0


def test_strategy_nepoznata_metrika():
    with pytest.raises(ValueError, match="Nepoznata metrika"):
        izracunaj_metriku("pogresna", [0], [0])


def test_observer_prima_dogadjaje():
    dogadjaji = []
    eksperiment = IrisEksperiment("knn")
    eksperiment.pretplati(lambda naziv, **podaci: dogadjaji.append(naziv))
    eksperiment.pokreni()
    assert dogadjaji == ["pocetak_treninga", "kraj_treninga", "kraj_evaluacije"]


def test_iris_eksperiment():
    rezultat = IrisEksperiment("linearni", "accuracy").pokreni()
    assert 0 <= rezultat <= 1


def test_dekorator_cuva_rezultat(capsys):
    @mjeri_vrijeme
    def saberi(a, b):
        return a + b

    assert saberi(2, 3) == 5
    assert "Trajanje saberi" in capsys.readouterr().out
