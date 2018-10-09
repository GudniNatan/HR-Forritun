def getDirections(x, y):
    ''' Returns the directions one could travel in from x, y according to the diagram '''
    n = True
    s = True
    e = True
    w = True

    #check borders
    if y == 3:
        n = False
    elif y == 1:
        s = False
    if x == 1:
        w = False
    elif x == 3:
        e = False

    #check walls
    if y == 1:
        e = False
        w = False
    elif x == 2 and y == 2:
        n = False
        e = False
    elif x == 3 and y == 2:
        w = False
    elif x == 2 and y == 3:
        s = False
    return n, e, s, w


def printAvailableDirections(x, y):
    ''' Prints the directions one could travel in from x, y '''
    n, e, s, w = getDirections(x, y)
    print("You can travel:", end=" ")
    if n:
        print("(N)orth", end="")
        if e or w or s:
            print(" or", end=" ")
    if e:
        print("(E)ast", end="")
        if w or s:
            print(" or", end=" ")
    if s:   
        print("(S)outh", end="")
        if w:
            print(" or", end=" ")
    if w:
        print("(W)est", end="")
    print(".")


def getValidInput(x, y):
    ''' Returns a user inputted direction that one could travel in from x, y '''
    n, e, s, w = getDirections(x, y)
    while True:
        direction = input("Direction: ").upper()
        if direction == "N" and n:
            break
        elif direction == "E" and e:
            break
        elif direction == "S" and s:
            break
        elif direction == "W" and w:
            break
        print("Not a valid direction!")
    return direction


def movePlayer(x, y, direction):
    ''' Returns the moved x, y coordinates according to the direction '''
    if direction == "N":
        y += 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y -= 1
    elif direction == "W":
        x -= 1
    return x, y


def isLeverTile(x, y):
    ''' Returns wether the x, y tile is a lever tile or not'''
    if y == 2 or (x == 2 and y == 3):
        return True
    else:
        return False


def leverPull(coins):
    ''' Promts player to pull the lever, if they do 1 is added to their coin total. '''
    answer = input("Pull a lever (y/n): ")
    if answer.lower() == "y":
        coins += 1
        print("You received 1 coins, your total is now {}.".format(coins))
    return coins


def play():
    coins = 0
    x, y = 1, 1
    while not (x == 3 and y == 1):
        if isLeverTile(x, y):
            coins = leverPull(coins)
        printAvailableDirections(x, y)
        direction = getValidInput(x, y)
        x, y = movePlayer(x, y, direction)
    print("Victory!")


def main():
    cont = "y"
    while cont == "y":
        play()
        cont = input("Play again (y/n): ").lower()


main()
