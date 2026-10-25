# -- Functies --
def bereken_vierkant(x):
    return x * x

Getal = float(input("Geef een getal in: "))

Resultaat = bereken_vierkant(Getal)
print(f"Het kwadraat is: {Resultaat:g}")