# Gudni Natan Gunnarsson
# 13.9.2018
# Forritun

CEILING = 10
FLOOR = 1

position = int(input("Input an position between 1 and 10: "))

def move(direction):
    '''Evaluates the input and moves the character. Returns whether or not the input was valid.'''
    global position
    if direction == "r":
        position += 1
    elif direction == "l":
        position -= 1
    else:
        return False
    return True

def bind(position):
    '''Binds the characters position between the FLOOR and the CEILING. Returns the new position'''
    if position > CEILING:
        position = CEILING
    elif position < FLOOR:
        position = FLOOR
    return position

def getDirection():
    '''Prompts player to input direction and returns it'''
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    return input("Input your choice: ")

while True:
    direction = getDirection()
    if move(direction):
        position = bind(position)
    else:
        break
    print("New position is:", position)
print("New position is:", position)