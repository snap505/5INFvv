# -- Variabelen --
Getal = int(input("voer een getal tussen 1 en 100 in: ")) # Vraagt voor een getal

# -- if, elif, else --
if 1 <= Getal <= 100: # Controleert of het getal tussen 1 en 100 ligt, inclusief die 2 getallen
    print("Het getal ligt binnen het interval")
else:
    print("Het getal ligt buiten het interval")