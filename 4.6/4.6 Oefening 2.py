# -- Variabelen --
Zin = input("Voer een zin in: ")
Woorden = Zin.split()

Frequentie = {}

# -- Loop --
for Woord in Woorden:
    if Woord in Frequentie: # Controleert of het woord in de dictionary van Woorden zit
        Frequentie[Woord] += 1 # Voegt een waarden van 1 toe aan de frequentie van het woord
    else:
        Frequentie[Woord] = 1 # Voegt het woord toe aan de dictionary "Frequentie"

# -- Functies -- 
print("Woordfrequentie:") # Print functie
for Woord in Frequentie:
    print(f"{Woord}: {Frequentie[Woord]}") # Print welke woorden er zijn en hoe vaak ze voor komen