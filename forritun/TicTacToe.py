# Gudni Natan Gunnarsson
# 13.10.2018
# Skilaverkefni 7

PLAYERS = ("X", "O")


def printBoard(gameBoard):
    ''' Print a formatted version of the game board '''
    for row in gameBoard:
        for space in row:
            print("{:>5}".format(space), end=" ")
        print()


def makeMove(player, board):
    ''' Process the players turn and update the board. Returns move indecies. '''
    while True:
        move = input(player + " position: ").strip()
        try:  # assume move is integer
            move_int = int(move) - 1
        except ValueError:  # move is not an integer
            print("Illegal move!")
            continue
        if 0 <= move_int < len(board) ** 2:  # Within borders
            row = move_int // len(board)
            col = move_int % len(board)
            if board[row][col] not in PLAYERS:  # Not occupied
                board[row][col] = player
                return (row, col)
        print("Illegal move!")


def isWinner(player, board, move):
    ''' Check if player has won. Returns boolean. '''
    row_length = len(board)
    playerWin = [player for i in range(row_length)]

    row = board[move[0]]  # only check relevant row
    column = [board[i][move[1]] for i in range(row_length)]
    diagonal1 = [board[i][i] for i in range(row_length)]  # Diagonal row from top-left to bottom-right
    diagonal2 = [board[i][-i-1] for i in range(row_length)]  # Diagonal row from bottom-left to top-right
    return playerWin in (row, column, diagonal1, diagonal2)


def createGameBoard(dimensions):
    ''' Returns a new game board of size dimensions * dimensions '''
    board = list()
    for i in range(dimensions):
        row = [dimensions * i + j + 1 for j in range(dimensions)]
        board.append(row)
    return board


def main():
    dimensions = int(input("Input dimension of the board: "))
    board = createGameBoard(dimensions)
    player = PLAYERS[0]
    printBoard(board)

    for i in range(1, (dimensions ** 2) + 1):
        move = makeMove(player, board)
        printBoard(board)
        if isWinner(player, board, move):
            print("Winner is:", player)
            break
        nextPlayerIndex = i % len(PLAYERS)  # Rotates through all the players
        player = PLAYERS[nextPlayerIndex]
    else:
        # If dimensions ** 2 turns pass without a victory,
        # the board is full and the game is a draw
        print("Draw!")


main()
