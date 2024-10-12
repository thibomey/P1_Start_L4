# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.

getallen = [1, 5, 8, 9, 85, 70, 84]
getallen.sort()
grootste = 0
for getal in getallen:
    if getal > grootste:
        grootste = getal

print(grootste)