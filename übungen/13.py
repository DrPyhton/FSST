import random

counter = 0
spielfeld = [[0] * 6 for _ in range(7)]
spieler = random.randint(1, 2)
default = "\033[0m"
blau = "\033[94m"
gelb = "\033[93m"
rot = "\033[91m"
underline = "\033[4m"
cls = "\033[2J"


def output():
    bildschirm = cls + default + underline + " 1 2 3 4 5 6 7\n" + default
    for y in range(6):
        for x in range(7):
            farbe = blau
            if spielfeld[x][y] == 1:
                farbe = gelb
            elif spielfeld[x][y] == 2:
                farbe = rot
            bildschirm = bildschirm + farbe + " " + str(spielfeld[x][y])
        bildschirm = bildschirm + "\n" + default
    print(bildschirm)


def platz(x):
    return spielfeld[x][0] == 0


def eingabe():
    global counter
    while True:
        output()
        print("Es sind noch {} Züge übrig".format(42 - counter))
        e = input("{}Spieler-{} ist am Zug:".format(default, spieler))
        if e.isnumeric():
            e = int(e)
            if 0 < e < 8:
                if platz(e - 1):
                    counter = counter + 1
                    return e - 1


def platzierung(x):
    for y in range(6):
        if y == 5 and spielfeld[x][y] == 0:
            spielfeld[x][y] = spieler
            return y

        if spielfeld[x][y] != 0:
            spielfeld[x][y - 1] = spieler
            return y - 1


def diagonale():
    oben = [[] for _ in range(12)]
    unten = [[] for _ in range(12)]

    for y in range(6):
        for x in range(7):
            oben[x + y].append(spielfeld[x][y])
            unten[x - y + 5].append(spielfeld[x][y])

    d = []
    for i in range(12):
        if len(unten[i]) > 3:
            d.append(unten[i])

        if len(oben[i]) > 3:
            d.append(oben[i])

    return d


def gewonnen(x, y):
    steine = 0
    for xx in range(7):
        if spielfeld[xx][y] == spieler:
            steine = steine + 1
        else:
            steine = 0
        if steine == 4:
            return True

    steine = 0
    for yy in range(0, 6, 1):
        if spielfeld[x][yy] == spieler:
            steine = steine + 1
        else:
            steine = 0
        if steine == 4:
            return True

    d = diagonale()
    print(d)
    for n in d:
        steine = 0
        for m in n:
            if m == spieler:
                steine = steine + 1
            else:
                steine = 0
            if steine == 4:
                return True
    return False


def unentschieden():
    for x in range(0, 7, 1):
        if platz(x):
            return False
    return True


def neustart():
    ein = input("soll ein neues spiel gestartet werden, ja oder nein?")
    if ein == "nein":
        return False
    else:
        return True


if __main__ := "__name__":
    while True:
        x = eingabe()
        y = platzierung(x)

        if gewonnen(x, y):
            output()
            print("Spieler {} hat gewonnen".format(spieler))
            if not neustart():
                break
            else:
                counter = 0
                spieler = random.randint(1, 2)
                spielfeld = [[0] * 6 for _ in range(7)]

        elif unentschieden():
            output()
            print("Unentschieden")
            if not neustart():
                break
            else:
                spieler = random.randint(1, 2)
                spielfeld = [[0] * 6 for _ in range(7)]
                counter = 0

        if spieler == 1:
            spieler = 2
        else:
            spieler = 1


