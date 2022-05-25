import random

counter = 1
namen = []

name = input("einen Namen für den spieler eingeben")

while True:
    grenze = input("Eine Grenze für das Eratten eingeben:")
    if grenze.isnumeric():
        grenze = int(grenze)
        if grenze > 0:
            break
        else:
            print("Die Zahl ist nicht über null")
    else:
        print("Die Zahl ist nicht Numaric")

random = random.randint(1, grenze)


while True:
    spieler = input("({}Versuch)Errate die Zahl!:".format(counter))
    if spieler.isnumeric():
        counter = counter + 1
        spieler = int(spieler)
        if spieler == random:
            print("Die Zahl war {} und du hast {} gebraucht".format(random, counter))
            namen.append(name)
            namen.append(counter)

            break
        if spieler < random:
            print("Die Zahl ist zu klein")
        else:
            print("Die zahl ist zu groß")

    else:
        print("Die Zahl ist nicht numaric")




print(namen)