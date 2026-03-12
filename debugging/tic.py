#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    return False

def get_input(prompt):
    """
    Prompts the user for a valid board coordinate (0, 1, or 2).

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        int: A valid integer between 0 and 2 inclusive.
    """
    while True:
        try:
            value = int(input(prompt))
            if value not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value (0, 1, or 2).")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0  # BUG FIX 2: track moves to detect a draw

    while not check_winner(board):
        # BUG FIX 2: declare draw after all 9 squares are filled
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            return

        print_board(board)
        # BUG FIX 3: validate row and column input
        row = get_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_input("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1  # BUG FIX 2: increment move counter
            last_player = player  # BUG FIX 1: remember who just played
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + last_player + " wins!")  # BUG FIX 1: use last_player, not player

tic_tac_toe()