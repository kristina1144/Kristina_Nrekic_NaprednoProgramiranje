# Mini projekat 2 – ML eksperimenti

Ovaj projekat pokazuje kako se projektni šabloni mogu koristiti za pokretanje jednostavnih eksperimenata mašinskog učenja. Primjer koristi Iris skup podataka i tri modela iz biblioteke scikit-learn.

U projektu su korišćeni sljedeći šabloni:

- Factory bira i kreira model na osnovu naziva: linearni model, stablo odlučivanja ili kNN.
- Strategy omogućava izbor metrike (accuracy ili macro F1) bez promjene toka eksperimenta.
- Observer obavještava pretplatnike o početku i kraju treninga i o završetku evaluacije.
- Template Method određuje redoslijed koraka: učitavanje, priprema, treniranje, evaluacija.
- Decorator mjeri vrijeme treniranja bez promjene povratne vrijednosti metode.

## Pokretanje

Instalacija biblioteka:

```bash
pip install -r requirements.txt
```

Pokretanje demonstracije:

```bash
python ml_okvir.py
```

Pokretanje testova:

```bash
python -m pytest -v
```

Demonstracija koristi isti Iris skup i istu podjelu podataka (80% trening, 20% test) za sva tri modela. Rezultati zavise od verzije biblioteka, pa nijesu unaprijed fiksirani.

## Dijagram klasa (Mermaid)

```mermaid
classDiagram
    class Eksperiment {
        <<abstract>>
        +pretplati(funkcija)
        +objavi(dogadjaj, podaci)
        +pokreni()
        +ucitaj()*
        +pripremi(podaci)*
        +treniraj(podaci)*
        +evaluiraj(model, podaci)*
    }
    class IrisEksperiment {
        +naziv_modela
        +metrika
        +ucitaj()
        +pripremi(podaci)
        +treniraj(podaci)
        +evaluiraj(model, podaci)
    }
    class Factory {
        <<module functions>>
        +kreiraj_model(naziv)
    }
    class Strategy {
        <<module functions>>
        +izracunaj_metriku(naziv, tacno, predvidjeno)
    }
    class Decorator {
        <<module function>>
        +mjeri_vrijeme(funkcija)
    }
    Eksperiment <|-- IrisEksperiment
    IrisEksperiment ..> Factory : kreira model
    IrisEksperiment ..> Strategy : bira metriku
    IrisEksperiment ..> Decorator : mjeri trening
```

*Napomena:* Factory, Strategy i Decorator su prikazani kao cjeline u dijagramu radi preglednosti, ali su u Python kodu implementirani funkcijama, a ne klasama. Observer je implementiran listom pretplatnika u klasi `Eksperiment`.


