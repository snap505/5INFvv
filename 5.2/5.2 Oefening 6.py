# -- Functies --
def filter_even_getallen(Getallen):
    EvenGetallen = []

    for Getal in Getallen:
        if Getal % 2 == 0:
            EvenGetallen.append(Getal)

    return EvenGetallen

Getallen = [1, 2, 3, 4, 5, 6, 7, 8]
Resultaat = filter_even_getallen(Getallen)

print(f"De even getallen zijn: {Resultaat}")