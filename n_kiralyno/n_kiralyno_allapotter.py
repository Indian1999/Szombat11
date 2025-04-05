"""
Megoldja az n királynő problémát
"""
import networkx as nx
import matplotlib.pyplot as plt
import math

def is_valid(node):
    last_index = len(node) - 1
    for i in range(last_index):
        if math.fabs(node[i] - node[last_index]) == math.fabs(i-last_index):
            return False
    return True

n = 8

G = nx.Graph()
start_node = tuple()
G.add_node(start_node)

open_list = [start_node]
visited = [start_node]

end_nodes = []

while len(open_list) > 0:
    current_node = open_list.pop(0)
    if len(current_node) == n:
        end_nodes.append(current_node)
    else:
        for i in range(1, n + 1):
            if i not in current_node:
                # Ebben az oszlopban még tuti nincs királynő
                new_node = tuple(list(current_node) + [i])
                if is_valid(new_node):
                    pass

