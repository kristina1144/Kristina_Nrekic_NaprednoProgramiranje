def prosjecna_cijena(cijene):
    if len(cijene) == 0:
        return 0

    return sum(cijene) / len(cijene)
