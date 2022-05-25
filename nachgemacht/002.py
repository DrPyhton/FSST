zahlen = []

for x in range(0, 3):
    while True:
        if x == 0:
            eingabe = input("Bitte eine Startzahl eingeben:")
        if x == 1:
            eingabe = input("bitte eine höchst Zahl eingeben:")
        if x == 2:
            eingabe = input("Bitte die Schritte angeben:")

        if eingabe.isnumeric():
            eingabe = int(eingabe)
            zahlen.append(eingabe)
            break
        else:
            print("Die eingabe ist keine Zahl")

for x in range(zahlen[0], zahlen[1] + 1, zahlen[2]):
    print(x)
