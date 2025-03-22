import networkx as nx               # pip install networkx
import matplotlib.pyplot as plt     # pip install matplotlib
# ctrl + ö - terminál

#Kezdőállapot
start_node = (0,0,5)

# Egy üres irányított gráfor hozunk létre
G = nx.DiGraph() 

# Ehez a gráfhoz adjuk hozzá a csúcsokat (node) és az éleket (edge)
# Node-ok száma: 10
# Edge-k száma: 34
G.add_node(start_node)
G.add_node((2,0,3))
G.add_node((0,3,2))
G.add_node((0,2,3))
G.add_node((2,3,0))
G.add_node((2,1,2))
G.add_node((2,2,1))
G.add_node((1,3,1))
G.add_node((1,0,4))
G.add_node((0,1,4))
G.add_edge((0,0,5), (2,0,3))
G.add_edge((0,0,5), (0,3,2))
G.add_edge((2,0,3), (0,0,5))
G.add_edge((2,0,3), (2,3,0))
G.add_edge((2,0,3), (0,2,3))
G.add_edge((0,2,3), (2,0,3))
G.add_edge((0,2,3), (0,0,5))
G.add_edge((0,2,3), (0,3,2))
G.add_edge((0,2,3), (2,2,1))

layout = nx.kamada_kawai_layout(G)
nx.draw(G, layout, with_labels = True, arrows=True)
plt.show()

#Több kurzor:
# ctrl + alt + lefele nyíl
# alt lenyomva tartva + kattintgatás



