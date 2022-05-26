def parallel(e: list):
    par = float()
    for i in e:
        par += (1 / float(i))
    par = 1 / par
    print(par)


def serie(e: list):
    ser = float()
    for i in e:
        ser += float(i)
    print(ser)


while True:
    eingabe1 = input("Bitte eingeben ob Serie(s) oder Parrallelschaltung(p) bercechnet werden soll(zum beenden q eingeben):")
    if eingabe1 not in "spq":
        continue

    if eingabe1 == "q":
        print("ende")
        quit(0)

    e = input("Widerstände mit kommer trennen")
    e = e.split(",")

    if eingabe1 == "p":
        parallel(e)

    elif eingabe1 == "s":
        serie(e)


