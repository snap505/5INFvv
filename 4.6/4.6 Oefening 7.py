# -- variabelen --
Studenten = {}

# -- Loops --
while True:
    print("\nStudentenbeheer Menu:")
    print("1. Student toevoegen")
    print("2. Studentgegevens weergeven")
    print("3. Cijfer toevoegen")
    print("4. Gemiddelde cijfer berekenen")
    print("5. Studenten per studierichting")
    print("6. Afsluiten")

    Keuze = input("Kies een optie: ")
 # -- if, elif, else --
    if Keuze == "1":
        Studentnummer = input("Studentnummer: ")
        Naam = input("Naam: ")
        Leeftijd = int(input("Leeftijd: "))
        Studierichting = input("Studierichting: ")

        Cijfers = {}

        Studenten[Studentnummer] = {
            "Naam": Naam,
            "Leeftijd": Leeftijd,
            "Studierichting": Studierichting,
            "Cijfers": Cijfers
        }

        print("Student toegevoegd!")

    elif Keuze == "2":
        Studentnummer = input("Studentnummer: ")

        if Studentnummer in Studenten:
            print(f"Naam: {Studenten[Studentnummer]['Naam']}")
            print(f"Leeftijd: {Studenten[Studentnummer]['Leeftijd']}")
            print(f"Studierichting: {Studenten[Studentnummer]['Studierichting']}")
            print(f"Cijfers: {Studenten[Studentnummer]['Cijfers']}")
        else:
            print("Student niet gevonden.")

    elif Keuze == "3":
        Studentnummer = input("Studentnummer: ")

        if Studentnummer in Studenten:
            Vak = input("Vak: ")
            Cijfer = float(input("Cijfer: "))

            Studenten[Studentnummer]["Cijfers"][Vak] = Cijfer
            print("Cijfer toegevoegd!")
        else:
            print("Student niet gevonden.")

    elif Keuze == "4":
        Studentnummer = input("Studentnummer: ")

        if Studentnummer in Studenten:
            Cijfers = Studenten[Studentnummer]["Cijfers"]

            if len(Cijfers) > 0:
                Totaal = 0

                for Vak, Cijfer in Cijfers.items():
                    Totaal = Totaal + Cijfer

                Gemiddelde = Totaal / len(Cijfers)
                print(f"Gemiddelde: {Gemiddelde:.2f}")
            else:
                print("Deze student heeft nog geen cijfers.")
        else:
            print("Student niet gevonden.")

    elif Keuze == "5":
        Studierichting = input("Welke studierichting zoek je? ")
        Gevonden = False

        for Studentnummer, Gegevens in Studenten.items():
            if Gegevens["Studierichting"].lower() == Studierichting.lower():
                print(f"{Gegevens['Naam']} (Studentnummer: {Studentnummer})")
                Gevonden = True

        if Gevonden == False:
            print("Geen studenten gevonden.")

    elif Keuze == "6":
        print("Studentenbeheer afgesloten.")
        break

    else:
        print("Ongeldige keuze.")