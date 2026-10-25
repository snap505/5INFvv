# -- Functies --
def bereken_bmi(gewicht, lengte):
    return gewicht / (lengte * lengte)

# -- Variabelen --
Gewicht = float(input("Geef je gewicht in kg: "))
Lengte = float(input("Geef je lengte in meter: "))

# -- Berekening --
BMI = bereken_bmi(Gewicht, Lengte)
print(f"Je BMI is: {BMI:.2f}")