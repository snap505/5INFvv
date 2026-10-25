# -- Loops --
while True:
    Getal1 = float(input("Voer het eerste getal in: "))
    Operator = input("Voer de operator in (+, -, *, /): ")
    Getal2 = float(input("Voer het tweede getal in: "))

    if Operator == "+":
        Resultaat = Getal1 + Getal2
        print(f"Resultaat: {Getal1:g} + {Getal2:g} = {Resultaat:g}")

    elif Operator == "-":
        Resultaat = Getal1 - Getal2
        print(f"Resultaat: {Getal1:g} - {Getal2:g} = {Resultaat:g}")

    elif Operator == "*":
        Resultaat = Getal1 * Getal2
        print(f"Resultaat: {Getal1:g} * {Getal2:g} = {Resultaat:g}")

    elif Operator == "/":
        if Getal2 != 0:
            Resultaat = Getal1 / Getal2
            print(f"Resultaat: {Getal1:g} / {Getal2:g} = {Resultaat:g}")
        else:
            print("Fout: delen door nul is niet mogelijk.")

    else:
        print("Ongeldige operator.")

    Verder = input("\nWil je nog een berekening uitvoeren? (ja/nee): ").lower()

    if Verder != "ja":
        print("Rekenmachine afgesloten.")
        break