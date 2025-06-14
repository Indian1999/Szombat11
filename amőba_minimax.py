import math

board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_moves_left():
    return any(cell == " " for row in board for cell in row)

def evaluate():
    # Sorok
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return 1 if row[0] == "X" else -1
    # Oszlopok
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return 1 if board[0][col] == "X" else -1
    # Átlók
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return 1 if board[0][0] == "X" else -1
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return 1 if board[0][2] == "X" else -1
    return 0
