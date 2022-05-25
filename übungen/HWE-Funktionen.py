

"""
Die funktionen gehören an den Anfang vom skript!

Richtigerer syntax wäre:

    'def parallel(e: int, e1: int):'
    Damit die ide u. interpreter sicher weiss mit welchem variablen typ sie es zu tun hat.


Versuche die funktionen und die schleifen für die eingabe so umzuschreiben, dass 1. nur eine schleife verwendet wird
und 2. anstelle von fixen 2 widerständen beliebig viele widerstände berechnet werden können.
"""


while True:
    eingabe1 = input("Bitte eingeben ob Serie(s) oder Parrallelschaltung(p) bercechnet werden soll")
    if eingabe1 == "s":
        break
    else:
        if eingabe1 == "p":
            break

while True:
    e = input("bitte ersten wiederstand eingeben")
    if e.isnumeric():
        e = int(e)
        break
while True:
 e1 = input("bitte zweiten wiederstand eingeben")
 if e1.isnumeric():
     e1 = int(e1)
     break

def parallel(e, e1):
    par = 1/(1/e + 1/e1)
    print(par)



def serie(e, e1):
    ser = e + e1
    print(ser)



if eingabe1 == "p":
    parallel(e, e1)

if eingabe1 == "s":
    serie(e, e1)
