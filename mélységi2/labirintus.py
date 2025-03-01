# ctrl + alt + lefele nyíl
map = [
["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
["#","S",".",".",".",".","#",".",".",".",".",".",".",".","#",".",".",".",".",".","#"],
["#",".",".","#","#","#",".",".","#","#","#","#",".","#","#","#",".","#","#","#","#"],
["#",".",".",".",".","#",".",".",".",".",".","#",".",".",".",".",".","#",".",".","#"],
["#","#",".","#",".","#","#","#",".","#",".","#",".","#",".","#","#","#",".",".","#"],
["#",".",".",".",".",".",".","#",".","#",".",".",".","#",".",".",".",".",".","#","#"],
["#",".",".","#","#","#",".","#","#","#","#","#",".","#",".","#","#","#",".",".","#"],
["#",".",".",".",".","#",".",".",".",".",".",".",".","#",".",".",".","#","E",".","#"],
["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
]

map = []
with open("mélységi2\input.txt", "r", encoding="utf-8") as f:
    for line in f:
        map.append(list(line.strip()))
       
score_map = [[float("inf") for j in range(len(map[i]))] for i in range(len(map))]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "#":
            score_map[i][j] = -1

def possible_moves(i,j):
    moves = []
    if i > 0 and score_map[i-1][j] >= score_map[i][j] + 2:
        moves.append("up")
    if i < len(score_map) - 1 and score_map[i+1][j] >= score_map[i][j] + 2:
        moves.append("down")
    if j < len(score_map[i]) - 1 and score_map[i][j+1] >= score_map[i][j] + 2:
        moves.append("right")
    if j > 0 and score_map[i][j-1] >= score_map[i][j] + 2:
        moves.append("left")
    return moves

def find_values(i,j):
    moves = possible_moves(i,j)
    if "up" in moves:
        score_map[i-1][j] = score_map[i][j] + 1
        find_values(i-1, j)
    if "down" in moves:
        score_map[i+1][j] = score_map[i][j] + 1
        find_values(i+1, j)
    if "right" in moves:
        score_map[i][j+1] = score_map[i][j] + 1
        find_values(i, j+1)
    if "left" in moves:
        score_map[i][j-1] = score_map[i][j] + 1
        find_values(i, j-1)
            
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "E":
            score_map[i][j] = 0
            find_values(i,j)

path_matrix = [[0 for j in range(len(map[i]))] for i in range(len(map))]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "#":
            path_matrix[i][j] = -1
        if map[i][j] == "S":
            path_matrix[i][j] = 9
        if map[i][j] == "E":
            path_matrix[i][j] = 8
            
def find_path(i,j):
    if i > 0 and score_map[i-1][j] + 1 == score_map[i][j]:
        path_matrix[i-1][j] = 1
        find_path(i-1, j)
    elif i < len(map) -1 and score_map[i+1][j] + 1 == score_map[i][j]:
        path_matrix[i+1][j] = 1
        find_path(i+1, j)
    elif j < len(map[i]) - 1 and score_map[i][j+1] + 1 == score_map[i][j]:
        path_matrix[i][j+1] = 1
        find_path(i, j+1)
    elif j > 0 and score_map[i][j-1] + 1 == score_map[i][j]:
        path_matrix[i][j-1] = 1
        find_path(i, j-1)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            find_path(i,j)
                