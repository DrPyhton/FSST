for b in range(1, 6):
    u = input(str("Bitt eine Zahl zwischen 1-9 eingeben-->"))
    if u.isnumeric():
        u =int(u)
        if 1 > u > 10:
            print("DIe Zahl ist nicht zwischen 1-9!!")
            break
    print("Die Zahl ist nicht numaric")

