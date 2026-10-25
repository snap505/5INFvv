# -- Imports --
import random

# -- Variabelen --
Getal = random.randint(1, 100)

# -- Loops --
while True:
    Gok = input("Raad het getal (of typ q om te stoppen): ")

    if Gok.lower() == "q":
        print("Je hebt opgegeven!")
        print(f"Het getal was {Getal}.")
        break

    Gok = int(Gok)

    if Gok > Getal:
        print("Te hoog!")
    elif Gok < Getal:
        print("Te laag!")
    else:
        print("Correct! Je hebt het getal geraden!")
        break