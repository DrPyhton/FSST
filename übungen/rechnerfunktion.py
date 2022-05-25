e = ()
e1 = ()
e3 = ()
e2 = ()


def eingabe(e):
    global e1, e3, e2
    while True:
        e1 = input("Bitte erste Zahl zum Rechnen eingeben")
        if e1.isnumeric():
            e1 = int(e1)
            break
    while True:
        e3 = input("Bitte den operant eingeben")
        if e3 == "*" or "-" or "/" or "+":
            break

    while True:
        e2 = input("Bitte die zweite Zahl eingeben")
        if e2.isnumeric():
            e2 = int(e2)
            break

    return e, e1, e2, e3


def plus(e):
    e = e1 + e2
    print(e)


def minus(e, e1, e2):
    e = e1 - e2
    print(e)


def durch(e, e1, e2):
    e = e1 / e2
    print(e)


def mal(e, e1, e2):
    e = e1 * e2
    print(e)


while True:
    eingabe(e)
    if e3 == "+":
        plus(e)
    if e3 == "-":
        minus(e, e1, e2)
    if e3 == "*":
        mal(e, e1, e2)
    else:
        durch(e, e1, e2)

    print("Neue Zahlen eingeben!")
