# -- Variabelen --
Budget = float(input("Wat is mijn budget?: ")) # Vraagt om het budget van de gebruiker
Prijs_boek = float(input("Wat is de prijs van een boek?: ")) # Vraagt om de prijs van een boek
Prijs_Tijdschrift = float(input("Wat is de prijs van een tijdschrift?: ")) # Vraagt om de prijs van een tijdschrift
Hoeveel_Boeken = int(input("Hoeveel boeken: ")) # Vraagt hoeveel boeken de gebruiker koopt
Hoeveel_Tijdschriften = int(input("Hoeveel tijdschriften: ")) # Vraagt hoeveel tijdschriften de gebruiker koopt
Totaal_Prijs = float((Prijs_boek * Hoeveel_Boeken) + (Prijs_Tijdschrift * Hoeveel_Tijdschriften)) # Berekent de totale prijs die de gebruiker moet betalen
Rest_Budget = float(Budget - Totaal_Prijs) # Berekent hoeveel de gebruiker over heeft na de koop

# -- Functies --
print(f"Na het kopen van {Hoeveel_Boeken:.0f} en {Hoeveel_Tijdschriften:.0f} heb ik nog €{Rest_Budget:.2f} over.") # Print een zin waar het zegt hoeveel de gebruiker over heeft