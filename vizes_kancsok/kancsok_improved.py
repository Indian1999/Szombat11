import networkx as nx
import matplotlib.pyplot as plt

start_node = (0,0,5)
capacities = (2,3,5)

open = [start_node]
visited = [start_node]

G = nx.DiGraph() # Irányított gráf
G.add_node(start_node)

while len(open) > 0:
    current_node = open.pop(0) # A 0. indexű elemet kivesszük a listából (0,0,5) (0,3,2), (1,3,1)
    for i in range(len(current_node)): # i = 0, 1, 2
        if current_node[i] != 0: # Üres kancsóból nem tudunk vizet átönteni
            for j in range(len(current_node)): # 0,1,2
                if i != j: # Önmagába nem önthet vizet egy kancsó
                    amount = min(current_node[i], capacities[j] - current_node[j])
                    new_node = list(current_node)
                    new_node[i] -= amount
                    new_node[j] += amount
                    new_node = tuple(new_node)
                    
                    if new_node not in visited:
                        open.append(new_node)
                        visited.append(new_node)
                        G.add_node(new_node)
                        
                    if current_node != new_node:
                        G.add_edge(current_node, new_node)
                        
                    
                    
    