# -- Imports --
import random # Importeert de module "random" zodat er een willekeurig getal gegenereerd kan worden

# -- Variabelen --
TeRadenGetal = random.randint(1,10) # Genereert het getal

GeradenGetal = int(input("Raad een getal: ")) # Vraagt het getal dat de gebruiker raad

# -- if, elif, else --
if GeradenGetal == TeRadenGetal: # Controleert of het geraden getal correct is
    print("Proficiat, je  hebt het getal geraden.")
else:
    print(f"Helaas, je hebt het niet geraden. Het getal was {TeRadenGetal}")
