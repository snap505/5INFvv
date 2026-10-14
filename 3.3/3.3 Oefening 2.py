# -- Variabelen --
Leeftijd = int(input("Hoe oud ben je? ")) # Vraagt de gebruiker's leeftijd

# -- if, elif, else --
if Leeftijd >= 16: # Controleert of de ingegeven leeftijd groter dan of gelijk is aan 16
    print("Je mag naar de film")

elif Leeftijd < 16:
    Pogingen = 0
    # Een while loop, deze loop blijft gaan totdat ofwel: de loop conditie gedaan is of totdat een functie in de loop de loop breekt.
    while Pogingen <= 2:
        BegelijderAanwezig = str(input("Ben je met een volwassene? ja of nee? ")).upper()
        if BegelijderAanwezig == "JA":
            print("Je mag naar de film.")
            break # Breekt de loop
        elif BegelijderAanwezig == "NEE":
            print("Je mag niet naar de film.")
            break # Breekt de loop
        elif Pogingen == 2:
            print("Eruit.")
            break # Breekt de loop
        else:
            print("Dat is geen antwoord op mijn vraag, ik vroeg ja of nee.")
            Pogingen = Pogingen + 1 # Voegt een poging toe aan pogingen -> pogingen = 0 wordt pogingen = 1