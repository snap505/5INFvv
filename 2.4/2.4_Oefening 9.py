Wisselkoers_EUR_naar_USD = 1.12

Bedrag = float((input("Bedrag: ")))
BronValuta = input("Bronvaluta (EUR of USD): ").strip().upper()

if BronValuta == "EUR":
    Doelvaluta = "USD"
    Resultaat = Bedrag * Wisselkoers_EUR_naar_USD
if BronValuta == "USD":
    Doelvaluta = "EUR"
    Resultaat == Bedrag / Wisselkoers_EUR_naar_USD

print(f"{Bedrag:.2f} {BronValuta} is gelijk aan {Resultaat:.2f} {Doelvaluta}")