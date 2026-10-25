# -- variabelen --
woordenboek = {
    "hallo": {
        "Engels": "hello",
        "Frans": "bonjour",
        "Duits": "hallo"
    },
    "wereld": {
        "Engels": "world",
        "Frans": "monde",
        "Duits": "Welt"
    },
    "kat": {
        "Engels": "cat",
        "Frans": "chat",
        "Duits": "Katze"
    },
    "hond": {
        "Engels": "dog",
        "Frans": "chien",
        "Duits": "Hund"
    }
}

Woord = input("Geef een Nederlands woord: ").lower()
Taal = input("Naar welke taal wil je vertalen? (Engels, Frans, Duits): ").capitalize()

# -- if, elif, else --
if Woord in woordenboek:
    if Taal in woordenboek[Woord]:
        Vertaling = woordenboek[Woord][Taal]
        print(f"Vertaling: {Vertaling}")
    else:
        print("Deze taal staat niet in het woordenboek.")
else:
    print("Dit woord staat niet in het woordenboek.")