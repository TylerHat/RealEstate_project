# board is a list of lists to represent the rows and columns of the game board
board = []
for x in range(5):
    board.append(["O"] * 5)

# function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# place the battleship at a random location on the board
from random import randint
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# start the game
for turn in range(4):
    # ask the player for their guess
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # check if the guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if (turn == 3):
            print("Game Over")
    # print the board after each turn
    print_board(board)
