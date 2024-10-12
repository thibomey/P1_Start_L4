# Maak een programma dat:
# - De gebruiker één voor één een naam van een klasgenoot laat intypen. Het programma blijft vragen tot er eens een lege string wordt ingevuld.
# - Je gaat dan deze lijst met namen alfabetisch sorteren.
# - Deze gesorteerde namen ga je dan printen.

Namen = []

while 1==1:
    inputGebruiker = input("Geef mij een naam van een klasgenoot: ")
    if inputGebruiker == "":
        break
    Namen.append(inputGebruiker)
Namen.sort()
print(Namen)