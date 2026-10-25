# -- Variabelen --
producten = {
    "appel": 0.75,
    "banaan": 1.20,
    "sinaasappel": 1.50,
    "kiwi": 2.00,
    "druiven": 2.50,
    "mango": 1.95,
    "ananas": 3.25
}

# Verhoog alle prijzen met 5%
for Product, Prijs in producten.items():
    producten[Product] = round(Prijs * 1.05, 2)

print("Prijzen verhoogd:")
for Product, Prijs in producten.items():
    print(f"{Product}: €{Prijs:.2f}")

# Producten duurder dan €1.50
dure_producten = {}

for Product, Prijs in producten.items():
    if Prijs > 1.50:
        dure_producten[Product] = Prijs

print("\nDure producten:")
for Product, Prijs in dure_producten.items():
    print(f"{Product}: €{Prijs:.2f}")

# Alle sleutels in hoofdletters
hoofdletters = {}

for Product, Prijs in producten.items():
    hoofdletters[Product.upper()] = Prijs

print("\nProducten in hoofdletters:")
for Product, Prijs in hoofdletters.items():
    print(f"{Product}: €{Prijs:.2f}")