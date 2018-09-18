# Gudni Natan Gunnarsson
# 13.9.2018
# Forritun

CEILING = 10
FLOOR = 1

def move(direction, position):
    '''Evaluates the input and moves the character. Returns the new position.'''
    if direction == "r":
        position += 1
    elif direction == "l":
        position -= 1
    return position

def bind(position):
    '''Binds the characters position between the FLOOR and the CEILING. Returns the new position'''
    if position > CEILING:
        position = CEILING
    elif position < FLOOR:
        position = FLOOR
    print("New position is:", position)
    return position

def getDirection():
    '''Prompts player to input direction and returns it'''
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    return input("Input your choice: ")

def validDirection(direction):
    return direction == "l" or direction == "r"

position = int(input("Input a position between 1 and 10: "))
direction = getDirection()

while validDirection(direction):
    position = move(direction, position)
    position = bind(position)
    direction = getDirection()
print("New position is:", position)