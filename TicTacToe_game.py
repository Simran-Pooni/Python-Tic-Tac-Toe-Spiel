import random

# Globale Variablen:
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Printing Game Board:
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2]),
    print("---------"),
    print(board[3] + " | " + board[4] + " | " + board[5]),
    print("---------"),
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)

# Taking Player Input:
def playerInput(board):
    eingabe = int(input("Gib eine Zahl zwischen 1-9 ein: "))
    if eingabe >= 1 and eingabe <= 9 and board[eingabe-1] == "-":
        board[eingabe-1] = currentPlayer
    else:
        print("In dieses Feld wurde schon bereits eingetragen!")


# Check for win or tie:
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonale(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("Unentschieden!")
        gameRunning = False


def checkWin():
    if checkHorizontal(board) or checkVertical(board) or checkDiagonale(board):
        print(f"Der Gewinner ist {winner}!")

# Switch Player:
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"

# computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayer()



# Gameloop:
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
