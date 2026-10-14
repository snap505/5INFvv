# -- Variabelen --
GeheelGetal = int(input("Voer een geheel getal in: ")) # Vraagt een geheel getal

Rest = GeheelGetal%2 # Zoekt de rest van het getal wanneer het gedeelt wordt door 2

# -- if, elif, else
if Rest == 0: # Controleert of de rest gelijk is aan 0, indien wel is het getal even anders niet
    print(f"{GeheelGetal} is even")
else:
    print(f"{GeheelGetal} is oneven")