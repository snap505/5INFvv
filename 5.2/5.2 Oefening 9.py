# -- Functies --
def fahrenheit_naar_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

def celsius_naar_fahrenheit(temp_c):
    return (temp_c * 9 / 5) + 32

print("Temperatuur Converter")
print("1. Fahrenheit naar Celsius")
print("2. Celsius naar Fahrenheit")

# -- Variabelen --
Keuze = input("Kies een conversie (1 of 2): ")

# -- if, elif, else --
if Keuze == "1":
    Fahrenheit = float(input("Geef de temperatuur in Fahrenheit: "))
    Celsius = fahrenheit_naar_celsius(Fahrenheit)
    print(f"Temperatuur in Celsius: {Celsius:.2f} °C")

elif Keuze == "2":
    Celsius = float(input("Geef de temperatuur in Celsius: "))
    Fahrenheit = celsius_naar_fahrenheit(Celsius)
    print(f"Temperatuur in Fahrenheit: {Fahrenheit:.2f} °F")

else:
    print("Ongeldige keuze.")