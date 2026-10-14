# niet van belang Wesley ma ik wou dit. 
# MVG Lorenzo :)
import sys

# -- Variabelen --
Cijfer = int(input("Wat is je cijfer?: "))
# error voorkomen met cijfer
if 100 < Cijfer or Cijfer < 0:
    print("Dat cijfer bestaat niet.")
    sys.exit() # sys.exit() is een functie die het programma stop zet in de terminal als het cijfer niet bestaan

Aanwezigheid = int(input("Wat is je aanwezigheid in procent?: "))
# error voorkomen met Aanwezigheid
if 100 < Aanwezigheid or Aanwezigheid < 0:
    print("Die aanwezigheid is onmogelijk")
    sys.exit() # hetzelfde hier maar voor aanwezigheid

# -- if, elif, else --
# geslaagd
if 50 <= Cijfer <= 100 and 85 <= Aanwezigheid <= 100:
    print("Je bent gelsaagd!")

# gebuisd door beide
elif 0 <= Cijfer < 50 and 0 <= Aanwezigheid <= 85:
    print("Je bent gebuisd door je cijfer en je aanwezigheid.")

#gebuisd door cijfer
elif 0 <= Cijfer < 50:
    print("Je bent gebuisd door je cijfer.")

# gebuisd door aanwezigheid
elif 0 <= Aanwezigheid < 85:
    print("Je bent gebuisd door je aanwezigheid.")


