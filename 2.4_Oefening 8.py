Voornaam = input("Voornaam: ")
Achternaam = input("Achternaam: ")
Functietitel = input("Functietitel: ")

Naam = f"{Voornaam} {Achternaam}".upper()

Breedte = max(len(Naam), len(Functietitel)) + 4

Rand = "+" + "-" * Breedte + "+"
Regel_Naam = "|" + Naam.center(Breedte) + "|"
Regel_Functie = "|" + Functietitel.center(Breedte) + "|"

print(Rand)
print(Regel_Naam)
print(Regel_Functie)
print(Rand)