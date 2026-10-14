# -- Variabelen --
Wisselkoers_EUR_naar_USD = 1.12 # De wisselkoers omzetting van euro naar amerikaanse dollar

Bedrag = float((input("Bedrag: "))) # Vraagt het bedrag
BronValuta = input("Bronvaluta (EUR of USD): ").strip().upper() # Vraagt welk valuta er gebruikt wordt

# -- if, elif, else --
if BronValuta == "EUR": # Zet euro om naar amerikaanse dollar
    Doelvaluta = "USD"
    Resultaat = Bedrag * Wisselkoers_EUR_naar_USD
elif BronValuta == "USD": # Zet amerikaanse dollar om naar euro
    Doelvaluta = "EUR"
    Resultaat = Bedrag / Wisselkoers_EUR_naar_USD

# -- Functies --
print(f"{Bedrag:.2f} {BronValuta} is gelijk aan {Resultaat:.2f} {Doelvaluta}") # print het bedrag, de bron valuta en de hoeveelheid van de doel valuta