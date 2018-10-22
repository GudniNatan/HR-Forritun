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
        if move in board and move not in PLAYERS:
            move_index = board.index(move)
            board[move_index] = player
            return int(move) - 1
        print("Illegal move!")

def isWinner(player, board, dimensions, move):
    ''' Check if player has won. Returns boolean. '''
    win = [player for i in range(dimensions)]
    rowNumber = move // dimensions
    
    row = board[rowNumber * dimensions: (rowNumber + 1) * dimensions]
    column = board[move % dimensions::dimensions]
    diagonal1 = board[::dimensions + 1]
    diagonal2 = board[dimensions - 1: -1: dimensions - 1]
    return win in (row, column, diagonal1, diagonal2)

def main():
    dimensions = int(input("Input dimension of the board: "))
    board = [str(x + 1) for x in range(dimensions ** 2)]
    player = PLAYERS[0]
    printBoard(board, dimensions)

    for i in range(1, len(board) + 1):
        move = makeMove(player, board)
        printBoard(board, dimensions)
        if isWinner(player, board, dimensions, move):
            print("Winner is:", player)
            break
        nextPlayerIndex = i % len(PLAYERS) # Rotates through all the players
        player = PLAYERS[nextPlayerIndex]
    else:
        # If len(board) turns pass without a victory, the board is full and the game is a draw
        print("Draw!")

main()