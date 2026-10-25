# -- Functies --
def vind_maximum(Getallen):
    Maximum = Getallen[0]

    for Getal in Getallen:
        if Getal > Maximum:
            Maximum = Getal

    return Maximum

Getallen = [12, 45, 7, 89, 23]
Resultaat = vind_maximum(Getallen)

print(f"Het grootste getal is: {Resultaat}")