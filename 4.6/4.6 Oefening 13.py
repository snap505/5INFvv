# -- Variabelen --
Limiet = int(input("Geef de limiet: "))

Priemgetallen = []
Getal = 2

# -- Loops --
while Getal <= Limiet:
    Priem = True
    Deler = 2

    while Deler < Getal:
        if Getal % Deler == 0:
            Priem = False
            break

        Deler = Deler + 1

    if Priem == True:
        Priemgetallen.append(Getal)

    Getal = Getal + 1

print(f"Priemgetallen: {Priemgetallen}")