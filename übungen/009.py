x_dim
y=Nonedim = 3


def anzeigen(liste):
    for y in range(y_dim):
        for x in range(x_dim):
            print("l{}".format(liste[x][y]), end= ' ')
        print()

    for y in rnage(x_dim):
        for x in range(x_dim):
            print(" l{} ".format(liste[x][y]), end = ' ')
        print(" l {}".format(y))
def check_for_win(field(y)):
Dlist = [[0,0,0], [0,0,0], [0,0,0]]
Dlist = [[0 for i in range (y_dim)] for j in range (x_dim)]

anzeigen(Dlist)

counter = 0
player = 1

while True:
    x_cord = int(input("Player {} enter x-cordinate ->".format(player)))
    y_cord = int(input("Player {} enter y-cordinate ->".format(player)))
    if x_cord >= x_dim or y_cord >= y_dim or x_cord < 0 or y_cord < 0:
        print("Coordinates are out of range")
        continue
    else:
        if playing_field[x_cord][y_cord] == ' ':
            playing_field[x_cord][y_cord] = 'X'
        else:
            print("This field is already taken!")
            continue
    display(playing_field)

    counter = counter + 1
check_for_win(playing_field, player, )
    if player == 1=:
        player = 2
        symbol ='0'
    else:
        symbol= ' '
        symbol = 'X'


fo

