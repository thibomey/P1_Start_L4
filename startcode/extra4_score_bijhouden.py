# Schrijf een programma genaamd “Score bijhouden”.
# De gebruiker kan:
# - Scores toevoegen
# - De hoogste score bekijken
# - Het gemiddelde berekenen
# - Het programma beëindigen

Scores = []
while 1==1:
    InputWatDoen = input("Wat wil je doen (1= score ingeven 2= hoogste score bekijken): ")
    if InputWatDoen == "1":
        InputScore = input("Geef de score in: ")
        Scores.append(InputScore)
        print("De score is correct opgeslaan!")
    elif InputWatDoen == "2":
        if Scores < 2:
            print("Te weinig scores scores ingegeven")
        else:
            Scores.sort()
            grootste = 0
            for getal in Scores:
                if getal > grootste:
                    grootste = getal
            print(grootste)
    elif InputWatDoen == "3":