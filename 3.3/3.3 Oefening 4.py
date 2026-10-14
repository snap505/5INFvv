# -- Variabelen --
Getal = int(input("Voer een getal in: ")) # Vraagt de gebruiker voor een getal

# -- if elif, else --
if Getal == 0: # Controleert of het getal gelijk is aan 0
    print("Het getal is nul.")
elif Getal >= 0: # Controleert of het getal groter is dan 0
    print("Het getal is positief.")
else: # Alle andere situaties is het getal negatief
    print("Het getal is negatief.")