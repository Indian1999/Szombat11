# Depth First Search (Mélységi bejárás)
# ctrl + alt + le/fel nyíl -> egy új kurzort hoz létre (lent/fent)
# alt + bal click -> Egy új kurzort hoz létre ott ahol kattintassz

map = [
[8,9,0,1,0,1,2,3],
[7,8,1,2,1,8,7,4],
[8,7,4,3,0,9,6,5],
[9,6,5,4,9,8,7,4],
[4,5,6,7,8,9,0,3],
[3,2,0,1,9,0,1,2],
[0,1,3,2,9,8,0,1],
[1,0,4,5,6,7,3,2]
]
score_map = [[0 for j in range(len(map[0]))] for i in range(len(map))]
# csupa 0-val lesz feltöltve, de ugyan az a mérete mint a mapnek
def possible_moves(i,j):
    moves = []
    if i > 0 and map[i-1][j] == map[i][j] - 1:
        moves.append("up") 
    if i < len(map) - 1 and map[i+1][j] == map[i][j] - 1:
        moves.append("down") 
    if j < len(map[0]) - 1 and map[i][j+1] == map[i][j] - 1:
        moves.append("right") 
    if j > 0 and map[i][j-1] == map[i][j] - 1:
        moves.append("left") 
    return moves

def increment_scores(a, b):
    visited = []
    def f(i, j):
        if (i,j) not in visited:
            score_map[i][j] += 1
            visited.append((i,j))
            moves = possible_moves(i,j)
            if "up" in moves:
                f(i-1, j)
            if "down" in moves:
                f(i+1, j)
            if "left" in moves:
                f(i, j-1)
            if "right" in moves:
                f(i, j+1)
    f(a,b)

#Keressük meg a 9-eseket:
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 9:
            increment_scores(i,j)
            
# Adjuk össze a 0-k értékeit
total = 0       
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            total += score_map[i][j]
            
print(total)