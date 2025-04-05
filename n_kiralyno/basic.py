# Egy 8x8-as mátrix, tele 0-val
chess_board = [[0 for j in range(8)] for i in range(8)] 

# jelölje 0 az üres pozíciót, 1 azt a helyet ahol királynő áll

def hits_another_queen(i,j):
    for col in range(8):
        if chess_board[i][col] == 1 and col != j:
            return True
    for row in range(8):
        if chess_board[row][j] == 1 and row != i:
            return True
    # Átlók ellenőrzése
    for a in range(1,8):
        if i - a >= 0  and j - a >= 0 and chess_board[i-a][j-a] == 1:
            return True
        if i + a < 8 and j - a >= 0 and chess_board[i+a][j-a] == 1:
            return True  
        if i - a >= 0 and j + a < 8 and chess_board[i-a][j+a] == 1:
            return True  
        if i + a < 8 and j + a < 8 and chess_board[i+a][j+a] == 1:
            return True  
    return False
    
    

def is_valid_chess_board():
    """Eldönti, hogy van-e olyan királynő a táblán ami üt egy másikat"""
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] == 1:
                hits_another = hits_another_queen(i,j)
                if hits_another:
                    return False
    return True
                

for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    for f in range(8):
                        for g in range(8):
                            for h in range(8):
                                chess_board[0][a] = 1
                                chess_board[1][b] = 1
                                chess_board[2][c] = 1
                                chess_board[3][d] = 1
                                chess_board[4][e] = 1
                                chess_board[5][f] = 1
                                chess_board[6][g] = 1
                                chess_board[7][h] = 1
                                
                                if is_valid_chess_board():
                                    print(a,b,c,d,e,f,g,h)
                                    
                                chess_board[0][a] = 0
                                chess_board[1][b] = 0
                                chess_board[2][c] = 0
                                chess_board[3][d] = 0
                                chess_board[4][e] = 0
                                chess_board[5][f] = 0
                                chess_board[6][g] = 0
                                chess_board[7][h] = 0
                                
                                