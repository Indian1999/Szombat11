import numpy as np              # terminálba: pip install numpy
import matplotlib.pyplot as plt # terminálba: pip install matplotlib

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
            score_map[i][j] = -10

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

path_matrix = np.ones( (len(map), len(map[0]), 3) )
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "#":
            path_matrix[i][j] = [0,0,0]
        if map[i][j] == "S":
            path_matrix[i][j] = [0,0.5,0]
        if map[i][j] == "E":
            path_matrix[i][j] = [1,1,1]
            
def find_path(i,j):
    if i > 0 and score_map[i-1][j] + 1 == score_map[i][j]:
        path_matrix[i-1][j] = [0,0.5,0]
        find_path(i-1, j)
    elif i < len(map) -1 and score_map[i+1][j] + 1 == score_map[i][j]:
        path_matrix[i+1][j] = [0,0.5,0]
        find_path(i+1, j)
    elif j < len(map[i]) - 1 and score_map[i][j+1] + 1 == score_map[i][j]:
        path_matrix[i][j+1] = [0,0.5,0]
        find_path(i, j+1)
    elif j > 0 and score_map[i][j-1] + 1 == score_map[i][j]:
        path_matrix[i][j-1] = [0,0.5,0]
        find_path(i, j-1)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            find_path(i,j)
            
            
plt.imshow(path_matrix)
plt.axis("off")
plt.savefig("mélységi2\képek\shortest_path.png")
plt.close()
                
                
# Hány különböző lerövidebb út létezik?
shortest_paths = np.zeros((len(map), len(map[0]), 3))
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == ".":
            shortest_paths[i][j] = [1,1,1]
        
shortest_paths_list = [shortest_paths]
def count_shortest_paths(i,j):
    counter = 0
    def f(i,j):
        nonlocal counter
        shortest_paths_list[counter][i][j] = [0,0.8,0]
        if score_map[i][j] == 0:
            counter += 1
            shortest_paths = np.zeros((len(map), len(map[0]), 3))
            for i in range(len(map)):
                for j in range(len(map[i])):
                    if map[i][j] == ".":
                        shortest_paths[i][j] = [1,1,1]
            shortest_paths_list.append(shortest_paths)
            return
        if i > 0 and score_map[i-1][j] + 1 == score_map[i][j]:
            f(i-1,j)
        if i < len(map) -1 and score_map[i+1][j] + 1 == score_map[i][j]:
            f(i+1,j)
        if j < len(map[i]) - 1 and score_map[i][j+1] + 1 == score_map[i][j]:
            f(i,j+1)
        if j > 0 and score_map[i][j-1] + 1 == score_map[i][j]:
            f(i,j-1)
    f(i,j)
    return counter

for row in score_map:
    print(row)
    
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            print(count_shortest_paths(i,j))
            
    
plt.figure(figsize=(5,5))        
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(shortest_paths_list[i])
    plt.axis("off")
plt.show()