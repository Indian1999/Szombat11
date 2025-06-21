import math
level = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,2,0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,3,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
        [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

distances = [[math.inf for j in range(len(level[0]))] for i in range(len(level))]

start_cell = (0,0)
end_cell = (0,0)
for i in range(len(level)):
    for j in range(len(level[i])):
        if level[i][j] == 1:
            distances[i][j] = -1
        if level[i][j] == 2:
            start_cell = (i, j)
            distances[i][j] = 0
        if level[i][j] == 3:
            end_cell = (i, j)
            
def fill_distances(i, j):
    global distances
    values = [distances[i][j]]
    if distances[i+1][j] != -1:
        values.append(distances[i+1][j] + 1)
    if distances[i-1][j] != -1:
        values.append(distances[i-1][j] + 1)
    if distances[i][j+1] != -1:
        values.append(distances[i][j+1] + 1)
    if distances[i][j-1] != -1:
        values.append(distances[i][j-1] + 1)
    distances[i][j] = min(values)
    if distances[i+1][j] > distances[i][j] + 1: # Ha min 2 vel nagyobb, akkor megyünk arra
        fill_distances(i+1, j)
    if distances[i-1][j] > distances[i][j] + 1:
        fill_distances(i-1, j)
    if distances[i][j+1] > distances[i][j] + 1:
        fill_distances(i, j+1)
    if distances[i][j-1] > distances[i][j] + 1:
        fill_distances(i, j-1)
        
fill_distances(start_cell[0], start_cell[1])

print(f"A kezdőpontból a végpontba {distances[end_cell[0]][end_cell[1]]} lépésből lehet eljutni")
#for row in distances:
#    print(row)
        
            

# Hány lépésből tudunk eljutni a 2-es cellából a 3-as cellába?
# 0 - üres mező
# 1 - fal

# Szélségi / Mélységi bejárást (Breadth/Depth First Search)