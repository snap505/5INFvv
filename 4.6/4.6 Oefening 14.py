# -- Imports --
import random

# -- Variabelen --
Woorden = ["python", "computer", "dinosaurus", "school", "wereld"]
Woord = random.choice(Woorden)

GeradenLetters = {}
Levens = 6

# -- Loops --
while Levens > 0:
    GeradenLettersOverzicht = ""

    for Letter in Woord:
        if Letter in GeradenLetters:
            GeradenLettersOverzicht = GeradenLettersOverzicht + Letter + " "
        else:
            GeradenLettersOverzicht = GeradenLettersOverzicht + "_ "

    print(f"\nWoord: {GeradenLettersOverzicht}")
    print(f"Levens: {Levens}")

    if all(Letter in GeradenLetters for Letter in Woord):
        print("Proficiat! Je hebt het woord geraden!")
        break

    Gok = input("Raad een letter: ").lower()

    if len(Gok) != 1 or not Gok.isalpha():
        print("Geef één letter in.")
        continue

    if Gok in GeradenLetters:
        print("Deze letter heb je al geraden!")
    else:
        GeradenLetters[Gok] = True

        if Gok in Woord:
            print("Goed geraden!")
        else:
            print(f"Helaas, de letter {Gok} komt niet voor in het woord.")
            Levens = Levens - 1

if Levens == 0:
    print(f"Game over! Het woord was: {Woord}")