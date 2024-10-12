# We gaan aan de gebruiker een aantal instructies vragen en op basis daarvan tekenen.
# - Maak eerst een lege lijst waar de stappen in zullen komen.
# - Maak een oneindige lus:
#     - Vraag een stap aan de gebruiker
#     - Als het gelijk is aan “stop”, breek uit de lus.
#     - Anders, voeg het toe aan de lijst met stappen.
# - Itereer over de stappenlijst om te tekenen.

stappenOmTeTekenen = []
while 1 == 1:
    inputGebruiker = input("Geef mij de stappen (1 per keer): ")
    if inputGebruiker == "Stop":
        break
    else:
        stappenOmTeTekenen.append(inputGebruiker)
for i in stappenOmTeTekenen:
    print(i)