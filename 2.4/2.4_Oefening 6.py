# -- Variabelen --
Gewicht = float(input("Geef je gewicht in kg: ")) # Vraagt het gewicht van de gebruiker
Lengte = float(input("Geef je lengte in m: ")) # Vraagt de lengte van de gebruiker

BMI = Gewicht / (Lengte * Lengte) # berekent de BMI van de gebruiker

# -- Functies --
print(f"Je BMI is {BMI:.1f}") # Print de BMI van de gebruiker