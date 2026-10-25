# -- Variabelen --
cijfers = {
    "Nederlands": 7,
    "Engels": 6,
    "Wiskunde": 8,
    "Informatica": 9,
    "Geschiedenis": 5,
    "Aardrijkskunde": 7,
    "Biologie": 6
}

Totaal = 0

# -- Loops --
for Vak, Cijfer in cijfers.items():
    Totaal = Totaal + Cijfer

Gemiddelde = Totaal / len(cijfers)
print("Gemiddelde:", round(Gemiddelde, 1))

# Hoogste en laagste cijfer
Hoogste = max(cijfers.values())
Laagste = min(cijfers.values())

for Vak, Cijfer in cijfers.items():
    if Cijfer == Hoogste:
        print("Hoogste cijfer:", Vak, Hoogste)

    if Cijfer == Laagste:
        print("Laagste cijfer:", Vak, Laagste)

# Voldoendes en onvoldoendes
print("Voldoendes:")

for Vak, Cijfer in cijfers.items():
    if Cijfer >= 6:
        print(Vak, Cijfer)

print("Onvoldoendes:")

for Vak, Cijfer in cijfers.items():
    if Cijfer < 6:
        print(Vak, Cijfer)