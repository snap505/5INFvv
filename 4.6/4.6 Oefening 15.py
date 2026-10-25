# -- Imports --
import random

# -- Variabelen --
Quiz = {
    "Wat is de hoofdstad van Frankrijk?": {
        "opties": ["A. Londen", "B. Parijs", "C. Berlijn", "D. Rome"],
        "antwoord": "B"
    },
    "Hoeveel poten heeft een spin?": {
        "opties": ["A. 6", "B. 8", "C. 10", "D. 12"],
        "antwoord": "B"
    },
    "Welke planeet staat het dichtst bij de zon?": {
        "opties": ["A. Venus", "B. Mars", "C. Mercurius", "D. Jupiter"],
        "antwoord": "C"
    },
    "Wat is 7 * 8?": {
        "opties": ["A. 54", "B. 56", "C. 64", "D. 48"],
        "antwoord": "B"
    },
    "Welke taal gebruiken we voor deze quiz?": {
        "opties": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "antwoord": "C"
    }
}

# -- Loop --
while True:
    Score = 0
    Vragen = list(Quiz.keys())
    random.shuffle(Vragen)
    Teller = 0

    while Teller < len(Vragen):
        Vraag = Vragen[Teller]

        print(f"\n{Vraag}")

        for Optie in Quiz[Vraag]["opties"]:
            print(Optie)

        Antwoord = input("Jouw antwoord (A, B, C of D): ").upper()

        while Antwoord not in ["A", "B", "C", "D"]:
            Antwoord = input("Ongeldig antwoord. Kies A, B, C of D: ").upper()

        if Antwoord == Quiz[Vraag]["antwoord"]:
            print("Correct!")
            Score = Score + 1
        else:
            print(f"Fout! Het juiste antwoord was {Quiz[Vraag]['antwoord']}.")

        Teller = Teller + 1

    print(f"\nQuiz afgelopen! Je score is {Score}/{len(Quiz)}.")

    Opnieuw = input("Wil je de quiz opnieuw spelen? (ja/nee): ").lower()

    if Opnieuw != "ja":
        print("Bedankt voor het spelen!")
        break