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
