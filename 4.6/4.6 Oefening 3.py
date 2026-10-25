# -- Variabelen --
Telefoonboek = {} # Maakt de dictionary aan

# -- Loop --
while True:
    print("\nTelefoonboek Menu:")
    print("1. Contact toevoegen")
    print("2. Contact opzoeken")
    print("3. Contact verwijderen")
    print("4. Alle contacten weergeven")
    print("5. Afsluiten")

    Keuze = input("Kies een optie: ")
# -- if, elif, else
    if Keuze == "1":
        Naam = input("Naam: ")
        Telefoonnummer = input("Telefoonnummer: ")

        Telefoonboek[Naam] = Telefoonnummer
        print("Contact toegevoegd!")

    elif Keuze == "2":
        Naam = input("Welke naam zoek je? ")

        if Naam in Telefoonboek:
            print("Telefoonnummer:", Telefoonboek[Naam])
        else:
            print("Contact niet gevonden.")

    elif Keuze == "3":
        Naam = input("Welk contact wil je verwijderen? ")

        if Naam in Telefoonboek:
            del Telefoonboek[Naam]
            print("Contact verwijderd!")
        else:
            print("Contact niet gevonden.")

    elif Keuze == "4":
        if len(Telefoonboek) == 0:
            print("Het telefoonboek is leeg.")
        else:
            for Naam, Telefoonnummer in Telefoonboek.items():
                print(Naam, ":", Telefoonnummer)

    elif Keuze == "5":
        print("Telefoonboek afgesloten.")
        break

    else:
        print("Ongeldige keuze.")