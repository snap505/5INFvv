# -- Loops --
while True:
    print("\nWachtwoordvereisten:")
    print("- Minimaal 8 karakters")
    print("- Minstens 1 hoofdletter")
    print("- Minstens 1 cijfer")
    print("- Minstens 1 speciaal karakter (!@#$%^&*)")

    Wachtwoord = input("\nGeef een wachtwoord: ")

    LengteGoed = len(Wachtwoord) >= 8
    HoofdletterGoed = any(Teken.isupper() for Teken in Wachtwoord)
    CijferGoed = any(Teken.isdigit() for Teken in Wachtwoord)
    SpeciaalGoed = any(not Teken.isalnum() for Teken in Wachtwoord)

    if LengteGoed and HoofdletterGoed and CijferGoed and SpeciaalGoed:
        print("Wachtwoord is geldig!")
        break
    else:
        print("Wachtwoord voldoet niet aan alle criteria.")

        if not LengteGoed:
            print("- Het wachtwoord moet minstens 8 karakters bevatten.")
        if not HoofdletterGoed:
            print("- Het wachtwoord moet een hoofdletter bevatten.")
        if not CijferGoed:
            print("- Het wachtwoord moet een cijfer bevatten.")
        if not SpeciaalGoed:
            print("- Het wachtwoord moet een speciaal karakter bevatten.")