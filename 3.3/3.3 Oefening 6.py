# -- Variabelen --
Jaar = int(input("Welke jaar is het?: ")) # Vraagt het jaar

# -- if, elif, else --
if Jaar%4 == 0 and Jaar%100 != 0 or Jaar%400 == 0: # Controleert of het jaar deelbaar is door 4 maar niet door 100 en of het deelbaar is door 400
    print("Het is een schrikkelkaar")
else:
    print("Het is geen schrikkeljaar")