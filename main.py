import random

N, M = (5, 10) # N -> playing field size NxN, M -> numbers of mines

def getTotalMines(PM, i, j) -> int:
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            x = i + k
            y = j + l
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if PM[x*N+y] < 0:
                n += 1
    return n

def createGame(PM):
    """Creation of the playing field: the location of mines
       and counting the number of mines around the cells without mines
    """

    # if the cell has the value n>=0, then there are no mines in it
    # and the number shows the number of mines around the current cell.
    # But all minus numbers are mines


    rng = random.Random()
    n = M
    while n > 0:
        i = rng.randrange(N) # random num from 0 to N
        j = rng.randrange(N)
        if PM[i*N+j] != 0: # if this field has already opened
            continue
        PM[i*N+j] = -1 # write here -1
        n -= 1

    # выяесляем количество мин вокруг клетки
    # (это число будет показоваться игроку при открытии ячейки)
    for i in range(N):
        for j in range(N):
            # если текущая открытая клетка >= 0 то мы присваиваем функцию,
            # которая высчитывает количество мин рядом с этой клеткой
            if PM[i*N+j] == 0:
                PM[i*N+j] = getTotalMines(PM, i, j)


def show(pole):
    """The function displays the state of the current
       playing field
    """
    print("Pole PM: ")
    for i in range(N):
        for j in range(N):
            print(str(pole[i*N+j]).rjust(3), end="")
        print()


def goPlayer():
    """Function for user input of coordinates
       closed cells of the playing field
    """
    run = True
    while run:
        x, y = input("Please enter (x and y): ").split()
        if not x.isdigit() and not y.isdigit():
            print("Please enter a valid numbers...")
            continue

        x = int(x)-1
        y = int(y)-1
        # Are the coordinates out of the field?
        if x < 0 or x >= N or y < 0 or y >= N:
            print("coordinates are out of bounds")
            continue

        run = False
        return(x,y)




def isFinish(PM, P):
    """Determining the current state of the game:
       won, lost, the game continues
    """
    for i in range(N*N):
        if P[i] != -2 and PM[i] < 0:
            return -1
    for i in range(N*N):
        # if the cage is not open yet
        if P[i] == -2 and PM[i] >= 0:
            return 1
        # if the cycle went through and nothing worked,
        # then the player has opened all the cells
    return -2


def startGame():
    """Game launch function: the playing field is displayed,
       the player opens any closed cell, the result is checked
       for the presence of a mine or a winning situation
    """
    # P nad PM - it's a playing fields
    P = [-2]*N*N
    PM = [0]*N*N

    createGame(PM)

    finish = isFinish(PM, P)
    while finish> 0:
        show(P)
        x, y = goPlayer()
        P[x*N+y] = PM[x*N+y]
        finish = isFinish(PM,P)
    return finish


result = startGame()
if result == -1:
    print("You lose !")
else:
    print("You win !")
print("Game over !")