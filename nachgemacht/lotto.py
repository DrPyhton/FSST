import random

spieler = []
zufall2 = []


def zufall():
    global zufall2
    counter = 0
    while counter != 6:
        x = random.randint(1, 45)
        if x in zufall2:
            continue
        zufall2.append(x)
        counter = counter + 1


    return zufall2


def eingabe():
    global spieler
    counter = 1
    while True:
        eingabe1 = input("Bitte die {} von sechs Lotto-zahlein eingeben die zwischen 1 - 45 sind:".format(counter))
        if eingabe1.isnumeric():
            eingabe1 = int(eingabe1)
            if 0 < eingabe1 < 46:
                if eingabe1 in spieler:
                    print("Die Zahl wurde schon eingegeben!")
                    continue
                else:
                    counter = counter + 1
                    spieler.append(eingabe1)
                    if counter == 7:
                        return spieler
            else:
                print("Die Zahl ist nicht zwischen 1 - 45!!")
        else:
            print("Die Zahl ist nicht Numaric!!")


if __name__ == "__main__":
    zufall()
    print(zufall2)
    eingabe()
    counter = 0
    for x in range(6):
        for y in range(6):
            if spieler[x] == zufall2[y]:
                counter = counter + 1

    if spieler == zufall2:
        print("Gewonnen")
    else:
        print("Verloren, du hast {} richtig erraten!".format(counter))

    print(zufall2)
