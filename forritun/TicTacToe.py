# Gudni Natan Gunnarsson 
# 11.10.2018
# Skilaverkefni 7

PLAYERS = ("X", "O")

def printBoard(board, dimensions):
    for i, space in enumerate(board):
        print("{:>5}".format(space), end=" ")
        if i % dimensions == dimensions - 1:
            print()

def makeMove(player, board):
    ''' Process the current players turn and update the board '''
    while True:
        move = input(player + " position: ").strip()
        if move in board:
            break
        print("Illegal move!")
    move_index = board.index(move)
    board[move_index] = player

def victory(player, board, dimensions):
    ''' Check if player has won. Returns boolean. '''
    win = [player for i in range(dimensions)]
    #rows and columns
    for i in range(dimensions):
        row = board[i * dimensions: (i + 1) * dimensions]
        column = board[i::dimensions]
        if row == win or column == win:
            return True
    #diagonals
    diagonal1 = board[::dimensions + 1]
    diagonal2 = board[dimensions - 1: -1: dimensions - 1]
    if diagonal1 == win or diagonal2 == win:
        return True
    return False

def main():
    dimensions = int(input("Input dimension of the board: "))
    board = [str(x + 1) for x in range(dimensions ** 2)]
    player = PLAYERS[0]
    printBoard(board, dimensions)

    for i in range(len(board)):
        makeMove(player, board)
        printBoard(board, dimensions)
        if victory(player, board, dimensions):
            print("Winner is:", player)
            break
        nextPlayerIndex = (i + 1) % len(PLAYERS) # Rotates through all the players
        player = PLAYERS[nextPlayerIndex]
    else:
        # If len(board) turns pass without a victory, the board is full and the game is a draw
        print("Draw!")

main()