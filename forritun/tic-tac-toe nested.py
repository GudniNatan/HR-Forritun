# Gudni Natan Gunnarsson 
# 11.10.2018
# Skilaverkefni 7

PLAYERS = ("X", "O")

def printBoard(board):
    for row in board:
        print(("{:>5}" * len(row)).format(*row))

def turn(player, board):
    ''' Process the current players turn and update the board '''
    while True:
        move = input(player + " position: ").strip()
        for i, line in enumerate(board):
            if move in line:
                board[i][line.index(move)] = player
                return
        print("Illegal move!")

def victory(player, board):
    ''' Check if player has won. Returns boolean. '''
    row_length = len(board)
    win = [player for i in range(row_length)]
    #rows and columns
    for i in range(row_length):
        row = board[i]
        column = [board[j][i] for j in range(row_length)]
        if row == win or column == win:
            return True
    #diagonals
    diagonal1 = [board[i][i] for i in range(row_length)]
    diagonal2 = [board[i][-i-1] for i in range(row_length)]
    if diagonal1 == win or diagonal2 == win:
        return True
    return False

def createGameBoard(dimensions):
    board = list()
    for x in range(dimensions):
        startSquare = x * dimensions + 1
        row = [str(startSquare + y) for y in range(dimensions)]
        board.append(row)
    return board

def main():
    dimensions = int(input("Input dimension of the board: "))
    board = createGameBoard(dimensions)
    printBoard(board)
    player = PLAYERS[0]
    for i in range(dimensions ** 2):
        turn(player, board)
        printBoard(board)
        if victory(player, board):
            print("Winner is:", player)
            break
        nextPlayerIndex = (PLAYERS.index(player) + 1) % len(PLAYERS) # Rotates through all the players
        player = PLAYERS[nextPlayerIndex]
    else:
        # If dimensions ** 2 turns pass without a victory, the board is full and the game is a draw
        print("Draw!")

main()