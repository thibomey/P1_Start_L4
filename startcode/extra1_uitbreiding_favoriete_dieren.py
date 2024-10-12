# Maak een uitbreiding op de oefening favoriete dieren (a).
# - Na het printen van de lijst vraag je welk dier uit de lijst moet.
# - Nadien toon je de lijst opnieuw maar deze keer zonder het gekozen dier.

dieren = []
inputDieren = input("Geef mij 1 dier: ")
dieren.append(inputDieren)
inputDieren = input("Geef mij 1 dier: ")
dieren.append(inputDieren)
inputDieren = input("Geef mij 1 dier: ")
dieren.append(inputDieren)
print(dieren)
inputVerwijdering = input("Welk dier moet ik verwijderen: ")
dieren.remove(inputVerwijdering)
print(dieren)