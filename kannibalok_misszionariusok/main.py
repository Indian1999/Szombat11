import networkx as nx # pip install networkx
import matplotlib.pyplot as plt

G = nx.DiGraph() # Üres Directed (irányított) Graph

start_node = (3,3,1)
end_node = (0,0,0)

open_list = [start_node]
visited = [start_node]

# Lehetséges mozgások:
# 1 misszionáriust
# 1 kannibált
# 2 kannibált
# 2 misszionáriust
# 1 misszionáriust 1 kannibált

def is_valid(node):
    """ True, ha a misszionáriusok és kannibálok száma is 0 és 3 között van"""
    return node[0] >= 0 and node[0] <= 3 and node[1] >= 0 and node[1] <= 3

while len(open_list) > 0:
    current_node = open_list.pop(0)
    if current_node[2] == 1: # A tutaj a bal parton van
        if current_node[0] - 1 >= current_node[1] or current_node[0] == 1: # 1 misszionárius
            # Ha legalább annyi misszionárius marad mint kannibál, vagy nem marad misszionárius
            new_node = (current_node[0] - 1, current_node[1], 0)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if 3 - current_node[0] >= 3 - current_node[1] + 1 or current_node[0] == 3: # 1 kannibál
            new_node = (current_node[0], current_node[1] - 1, 0)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if current_node[0] - 2 >= current_node[1] or current_node[0] == 2: # 2 misszionárius
            new_node = (current_node[0] - 2, current_node[1], 0)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if 3 - current_node[0] >= 3 - current_node[1] + 2 or current_node[0] == 3: # 2 kannibál
            new_node = (current_node[0], current_node[1] - 2, 0)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
        
        if 3 - current_node[0] + 1 >= 3 - current_node[1] + 1: #1 misszionárius, 1 kannibál 
            new_node = (current_node[0] - 1, current_node[1] - 1, 0)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
    else: # A tutaj a jobb parton van
        if 3 - current_node[0] - 1 >= 3 - current_node[1] or current_node[0] == 2: # 1 misszionárius
            new_node = (current_node[0] + 1, current_node[1], 1)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if 3 - current_node[0] - 2 >= 3 - current_node[1] or current_node[0] == 1: # 2 misszionárius
            new_node = (current_node[0] + 2, current_node[1], 1)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if current_node[0] >= current_node[1] + 1 or current_node[0] == 0: # 1 kannibál
            new_node = (current_node[0], current_node[1] + 1, 1)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if current_node[0] >= current_node[1] + 2 or current_node[0] == 0: # 2 kannibál
            new_node = (current_node[0], current_node[1] + 2, 1)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
                
        if current_node[0] + 1 >= current_node[1] + 1: # 1 misszionárius, 1 kannibál
            new_node = (current_node[0] + 1, current_node[1] + 1, 1)
            if is_valid(new_node) and new_node not in visited:
                open_list.append(new_node)
                visited.append(new_node)
                G.add_node(new_node)
            if is_valid(new_node):
                G.add_edge(current_node, new_node)
    
layout = nx.shell_layout(G)
nx.draw(G,layout, with_labels = True, arrows=True)
plt.savefig("kannibalok_misszionariusok/allapotter.png")

paths = list(nx.all_simple_paths(G, (3,3,1), (0,0,0)))
for path in paths:
    print(path)