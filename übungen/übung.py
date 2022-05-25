import random
import time

x = []
counter = 0
eingabe = input("Bie einen satz eingeben") + " "


def milli():
    return int(round(time.time() * 1000))


m = str()
for y in range(len(eingabe)):
    m = m + eingabe[y]
    if eingabe[y] == " ":
        x.append(m)
        m = ""
        counter = counter + 1


print(x)
print(counter)
print(m)


zufall1 = []
for i in range(0, len(x)):
    while True:
        zufall = random.randint(0, len(x) - 1)
        if zufall in zufall1:
            continue
        break
    zufall1.append(zufall)

g = []

for i in range(0, len(x)):
    g.append(x[zufall1[i]])


print(g)
