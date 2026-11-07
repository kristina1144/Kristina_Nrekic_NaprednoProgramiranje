# Napredno programiranje – Domaći zadatak

**Student:** Kristina Nrekić

## Opis

Zadatak je bio da uz pomoć ChatGPT-a napravim funkciju `prosjecna_cijena` i testiram je koristeći pytest i ruff. Radila sam u Google Colabu, sa Python verzijom 3.13.18.

## AI upit

> Uz AI asistenta implementirati funkciju prosjecna_cijena i priložiti test.

Početni kod:

```python
def prosjecna_cijena(cijene):
    return sum(cijene) / len(cijene)
```

## Uočeni nedostatak

Funkcija nije radila za praznu listu `[]`, već je prijavljivala `ZeroDivisionError`. Zato sam dodala provjeru:

```python
def prosjecna_cijena(cijene):
    if len(cijene) == 0:
        return 0

    return sum(cijene) / len(cijene)
```

## Testiranje

Pomoću pytest-a testirala sam liste `[10, 20, 30]`, `[5, 15]` i `[]`.

**Rezultati:**
- pytest: `1 passed`
- ruff check: `All checks passed!`
- ruff format: `2 files already formatted`

Za instalaciju alata:

```bash
pip install -r requirements.txt
```

Za pokretanje testova:

```bash
python -m pytest
```

## Zaključak

AI je generisao funkciju koja je radila za obične liste, ali nije predvidio praznu listu. Nakon ispravke, svi napisani testovi su prošli.
