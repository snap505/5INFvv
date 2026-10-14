# -- Variabelen --
Voornaam = input("Voornaam: ") # Vraagt voor de voornaam
Achternaam = input("Achternaam: ") # Vraagt voor de achternaam
Functietitel = input("Functietitel: ") # Vraagt voor de functietitel

Naam = f"{Voornaam} {Achternaam}".upper() # Maakt de voor- en achternaam hoofdletters

Breedte = max(len(Naam), len(Functietitel)) + 4 # Maakt de breedte van de naam kaart 4 karakters breeder, 2 aan beide kanten, zodat alles past

Rand = "+" + "-" * Breedte + "+" # Maakt de boven en onder randen van de kaart
Regel_Naam = "|" + Naam.center(Breedte) + "|" # Maakt de regel met de gebruiker's naam
Regel_Functie = "|" + Functietitel.center(Breedte) + "|" # Maakt de regel met de gebruiker's functie titel

# -- Functies --
print(Rand) # Print de rand
print(Regel_Naam) # Print de regel met de naam
print(Regel_Functie) # Print de regel met de functie
print(Rand) # Print de rand