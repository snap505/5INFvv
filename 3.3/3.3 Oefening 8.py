# -- Variabelen --
Bedrag = float(input("Voer het bedrag in: ")) # Vraagt voor een bedrag

# -- if, elif, else --
if 50 <= Bedrag <= 100: # Controleert of het bedrach tussen de 50 en 100 ligt, inclusief de 2 getallen
    Korting = Bedrag/100*5 # Berekent de 5% korting op het bedrag
    TeBetalen = Bedrag - Korting # Berekent de totale prijs
    print("Je krijgt 5% korting!")
    print(f"Je uiteindelijke prijs is: €{TeBetalen:.2f}")
elif 100 < Bedrag: # Controleert of het bedrag hoger ligt dan 100
    Korting = Bedrag/100*10 # Berekent de 10% korting op het bedrag
    TeBetalen = Bedrag - Korting # Berekent de totale prijs
    print("Je krijgt 10% korting!")
    print(f"Je uiteindelijke prijs is: €{TeBetalen:.2f}")
else:
    print("Je krijgt geen korting.")

