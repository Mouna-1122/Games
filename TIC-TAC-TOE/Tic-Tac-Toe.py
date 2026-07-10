import random

# Display the board
def display_board(board):
    print("\n")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---|---|---")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("\n")


# Choose player's marker
def player_input():
    marker = ""

    while marker not in ["X", "O"]:
        marker = input("Player 1: Choose X or O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


# Place marker
def place_marker(board, marker, position):
    board[position] = marker


# Check win
def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[9] == board[5] == board[1] == mark)
    )


# Decide who goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


# Check if space is free
def space_check(board, position):
    return board[position] == " "


# Check if board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Ask player for position
def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose your position (1-9): "))
        except:
            position = 0

    return position


# Replay option
def replay():
    choice = input("Do you want to play again? (Yes/No): ").lower()
    return choice.startswith("y")


print("Welcome to Tic Tac Toe!")

while True:

    the_board = [" "] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn + " will go first.")

    play_game = input("Are you ready to play? Enter Yes or No: ").lower()

    if play_game.startswith("y"):
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congratulations! Player 1 has won!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"

        else:

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congratulations! Player 2 has won!")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    if not replay():
        print("Thanks for playing!")
        break