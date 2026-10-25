# -- Imports --
import random

# -- Functies --
def werp_dobbelsteen():
    return random.randint(1, 6)

for Teller in range(3):
    Resultaat = werp_dobbelsteen()
    print(f"Worp {Teller + 1}: {Resultaat}")