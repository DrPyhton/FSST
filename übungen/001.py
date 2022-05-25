import random

y = 1
ya = []

while True:
    x1 = random.randint(1, 6)
    x2 = random.randint(1, 6)


    ya += ["{}-{}".format(x1, x2)]
    y = y + 1

    if x1 == 6 and x2 == 6:
        break

print(ya)
print("{} Versuche".format(y))
