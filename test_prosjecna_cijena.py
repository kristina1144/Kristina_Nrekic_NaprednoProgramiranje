from prosjecna_cijena import prosjecna_cijena


def test_prosjecna_cijena():
    assert prosjecna_cijena([10, 20, 30]) == 20
    assert prosjecna_cijena([5, 15]) == 10
    assert prosjecna_cijena([]) == 0
