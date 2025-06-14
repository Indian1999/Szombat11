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
        if row[0] == row[1] and row[1] == row[2] and row[1] != " ":
            if row[0] == "X":
                return 1
            else:
                return -1
    # Oszlopok
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]  and board[1][col]!= " ":
            if board[0][col] == "X":
                return 1
            else:
                return -1
    # Átlók
    if board[0][0] == board[1][1] and board[1][1] ==  board[2][2] and board[1][1] != " ":
            if board[1][1] == "X":
                return 1
            else:
                return -1
    if board[0][2] == board[1][1] and board[1][1] ==  board[2][0] and board[1][1] != " ":
            if board[1][1] == "X":
                return 1
            else:
                return -1
    return 0


def minimax(depth, is_maximizing):
    score = evaluate()
    
    if score == 1 or score == -1:
        return score
    if not is_moves_left():
        return 0
    
    if is_maximizing:
        best = -math.inf # negatív végtelen
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(depth+1, False)) # következő rekurzióban a mini játékos jön
                    board[i][j] = " "
        return best
    else:
        best = math.inf # pozitív végtelen
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(depth+1, True)) # következő rekurzióban a max játékos jön
                    board[i][j] = " "
        return best
        
def find_best_move(is_maximizing):
    if is_maximizing:
        best_value = -math.inf # alapból a szg. az X (max)
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    move_value = minimax(0, False)
                    board[i][j] = " "
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)
        return best_move
    else:
        best_value = math.inf 
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    move_value = minimax(0, True)
                    board[i][j] = " "
                    if move_value < best_value:
                        best_value = move_value
                        best_move = (i, j)
        return best_move
        
def move(is_maximizing, is_computer):
    if is_computer:
        row, col = find_best_move(is_maximizing)
        if is_maximizing:
            board[row][col] = "X"
        else:
            board[row][col] = "O"
    else:
        row = int(input("Add meg a sor számát (0-2): "))
        col = int(input("Add meg az oszlop számát (0-2): "))
        while board[row][col] != " " and row < 0 and row > 2 and col < 0 and col > 2:
            print("Érvénytelen cella!")
            row = int(input("Add meg a sor számát (0-2): "))
            col = int(input("Add meg az oszlop számát (0-2): "))
        if is_maximizing:
            board[row][col] = "X"
        else:
            board[row][col] = "O"
        
def game():
    print("Amőba: Te vagy O, a számítógép az X.")
    print_board()
    
    while True:
        move(is_maximizing=True, is_computer=True)
        print_board()
        
        if evaluate() == 1:
            print("X nyert!")
            break
        if evaluate() == -1:
            print("O nyert!")
            break
        if not is_moves_left():
            print("Döntetlen!")
            break
        
        move(is_maximizing=False, is_computer=False)
        print_board()
        
        if evaluate() == 1:
            print("X nyert!")
            break
        if evaluate() == -1:
            print("O nyert!")
            break
        if not is_moves_left():
            print("Döntetlen!")
            break
        
        
game()