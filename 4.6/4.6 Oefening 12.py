# -- Variabelen --
Limiet = int(input("Geef de limiet: "))

Fibonacci = []
Getal1 = 0
Getal2 = 1

# -- Loops --
while Getal1 <= Limiet:
    Fibonacci.append(Getal1)

    VolgendGetal = Getal1 + Getal2
    Getal1 = Getal2
    Getal2 = VolgendGetal

print(f"Fibonacci-reeks: {Fibonacci}")