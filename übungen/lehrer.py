from colorama import Fore, Back

# global variables to define x-y coordinates
x_dim = 7
y_dim = 6


def display(field):
    print('\n\n')
    # nummering for als columns
    for x in range(x_dim):
        print(Fore.WHITE + " {}".format(x), end='')
    print()

    # show the playing field
    for y in range(y_dim):
        for x in range(x_dim):
            print(Fore.WHITE + '|', end='')
            if field[x][y] == 'X':
                print(Fore.RED + "{}".format(field[x][y]), end='')
            elif field[x][y] == 'O':
                print(Fore.GREEN + "{}".format(field[x][y]), end='')
            else:
                print(Fore.WHITE + "{}".format(field[x][y]), end='')

        print(Fore.WHITE + "|")


def check_win(pf, player, s, x, y):
    # return 1 if the current player won the game otherwise return 0
    # check the coloum downwards for same symbol
    counter = 1
    for yy in range(y + 1, y_dim, 1):
        if pf[x][yy] == s:
            counter += 1
        else:
            break
    # already 4 downwards?
    if counter == 4:
        return 1
    else:
        counter = 1

    # now check left and right
    for xx in range(x - 1, -1, -1):
        if pf[xx][y] == s:
            counter += 1
        else:
            break
    for xx in range(x + 1, x_dim, 1):
        if pf[xx][y] == s:
            counter += 1
        else:
            break

    # already 4 left and right?
    if counter >= 4:
        return 1
    else:
        counter = 1

    # now check the diagonals
    # first check to the lower left
    # work with try and except in case we
    # reach the edge of the playing field
    try:
        for i in range(1, 4, 1):
            if pf[x - i][y + i] == s:
                counter += 1
            else:
                break
    except:
        pass
    # now check to the upper right
    try:
        for i in range(1, 4, 1):
            if pf[x + i][y - i] == s:
                counter += 1
            else:
                break
    except:
        pass

    # already 4 or more on this diagonal?
    if counter >= 4:
        return 1
    else:
        counter = 1

    # now check to the lower right
    try:
        for i in range(1, 4, 1):
            if pf[x + i][y + i] == s:
                counter += 1
            else:
                break
    except:
        pass
    # now check to the upper left
    try:
        for i in range(1, 4, 1):
            if pf[x - i][y - i] == s:
                counter += 1
            else:
                break
    except:
        pass
    # already 4 or more on this diagonal?
    if counter >= 4:
        return 1

    return 0


# define playing field and fill it with spaces
playing_field = [[' ' for i in range(y_dim)] for j in range(x_dim)]
display(playing_field)

counter = 0
player = 1
symbol = 'X'

# here starts the main gaming loop
while True:
    x = 0
    y = 0
    if player == 1:
        x = int(input(Fore.RED + "Player {} enter your x-cordinate ->".format(player)))
    else:
        x = int(input(Fore.GREEN + "Player {} enter your x-cordinate ->".format(player)))

    # check if coordinates are actually on the playing field
    if (x < 0 or x >= x_dim):
        print("Wrong coordinates - please try again!")
        continue

    # check if the choosen column has still free places?
    okay = False
    for y in range(y_dim - 1, -1, -1):
        if (playing_field[x][y] == ' '):
            playing_field[x][y] = symbol
            okay = True
            break
    if not okay:
        print("This column is already full, choose another one!")
        continue

    # show the playing field!
    display(playing_field)

    #####check for win will return 1 if the current player won!
    if (check_win(playing_field, player, symbol, x, y) == 1):
        if player == 1:
            print(Fore.RED + "#############################################")
            print(Fore.RED + "Congratulations Player 1, you won the game!!!")
            print(Fore.RED + "#############################################")
        else:
            print(Fore.GREEN + "#############################################")
            print(Fore.GREEN + "Congratulations Player 2, you won the game!!!")
            print(Fore.GREEN + "#############################################")
        break

    # check for a draw
    if (counter == x_dim * y_dim):
        print("DRAW !!!! nobody won this game!")
        break

    # switch player
    if (player == 1):
        player = 2
        symbol = 'O'
    else:
        player = 1
        symbol = 'X'

    # increase counter
    counter += 1
