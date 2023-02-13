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
for turn in range(10):
    print("TURN #"+ turn)
    # player 1 turn
    if turn % 2 == 0:
        print("Player 1 Turn")
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
    
        # check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print("Player 1 wins! The battleship was at ({}, {})".format(ship_row, ship_col))
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
        print_board(board)
    # player 2 turn (computer)
    else:
        print("Player 2 Turn (Computer)")
        guess_row = random_row(board)
        guess_col = random_col(board)
        print("The computer guessed ({}, {})".format(guess_row, guess_col))
        
        # check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print("Player 2 wins! The battleship was at ({}, {})".format(ship_row, ship_col))
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("The computer already tried that location.")
            else:
                print("The computer missed the battleship!")
                board[guess_row][guess_col] = "X"
        print_board(board)
        
    # check for a draw
    if turn == 10:
        print("Draw!")
