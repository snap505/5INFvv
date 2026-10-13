Budget = float(input("Wat is mijn budget?: "))
Prijs_boek = float(input("Wat is de prijs van een boek?: "))
Prijs_Tijdschrift = float(input("Wat is de prijs van een tijdschrift?: "))
Hoeveel_Boeken = int(input("Hoeveel boeken: "))
Hoeveel_Tijdschriften = int(input("Hoeveel tijdschriften: "))

Totaal_Prijs = float((Prijs_boek * Hoeveel_Boeken) + (Prijs_Tijdschrift * Hoeveel_Tijdschriften))

Rest_Budget = float(Budget - Totaal_Prijs)

print(f"Na het kopen van {Hoeveel_Boeken:.0f} en {Hoeveel_Tijdschriften:.0f} heb ik nog €{Rest_Budget:.2f} over.")