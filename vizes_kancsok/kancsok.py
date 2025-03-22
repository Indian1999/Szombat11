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
G.add_node(start_node) #N1
G.add_node((2, 0, 3))  #N2
G.add_node((0, 3, 2))  #N3
G.add_edge((0, 0, 5), (2, 0, 3))  #E1
G.add_edge((0, 0, 5), (0, 3, 2))  #E2
G.add_node((0, 2, 3))  #N4
G.add_edge((2, 0, 3), (0, 2, 3))  #E3
G.add_node((2, 3, 0))  #N5
G.add_edge((2, 0, 3), (2, 3, 0))  #E4
G.add_edge((2, 0, 3), (0, 0, 5))  #E5
G.add_node((2, 2, 1))  #N6
G.add_edge((0, 2, 3), (2, 2, 1))  #E6
G.add_edge((0, 2, 3), (2, 0, 3))  #E7
G.add_edge((0, 2, 3), (0, 3, 2))  #E8
G.add_edge((0, 2, 3), (0, 0, 5))  #E9
G.add_node((1, 3, 1))  #N7
G.add_edge((2, 2, 1), (1, 3, 1))  #E10
G.add_edge((2, 2, 1), (2, 3, 0))  #E11
G.add_edge((2, 2, 1), (0, 2, 3))  #E12
G.add_edge((2, 2, 1), (2, 0, 3))  #E13
G.add_node((1, 0, 4))  #N8
G.add_edge((1, 3, 1), (2, 2, 1))  #E14
G.add_edge((1, 3, 1), (0, 3, 2))  #E15
G.add_edge((1, 3, 1), (2, 3, 0))  #E16
G.add_edge((1, 3, 1), (1, 0, 4))  #E17
G.add_node((0, 1, 4))  #N9
G.add_edge((1, 0, 4), (1, 3, 1))  #E18
G.add_edge((1, 0, 4), (2, 0, 3))  #E19
G.add_edge((1, 0, 4), (0, 0, 5))  #E20
G.add_edge((1, 0, 4), (0, 1, 4))  #E21
G.add_node((2, 1, 2))  #N10
G.add_edge((0, 1, 4), (1, 0, 4))  #E22
G.add_edge((0, 1, 4), (0, 0, 5))  #E23
G.add_edge((0, 1, 4), (0, 3, 2))  #E24
G.add_edge((0, 1, 4), (2, 1, 2))  #E25
G.add_edge((2, 1, 2), (0, 1, 4))  #E26
G.add_edge((2, 1, 2), (2, 3, 0))  #E27
G.add_edge((2, 1, 2), (2, 0, 3))  #E28
G.add_edge((2, 1, 2), (0, 3, 2))  #E29
G.add_edge((2, 3, 0), (2, 0, 3))  #E30
G.add_edge((2, 3, 0), (0, 3, 2))  #E31
G.add_edge((0, 3, 2), (0, 0, 5))  #E32
G.add_edge((0, 3, 2), (2, 3, 0))  #E33
G.add_edge((0, 3, 2), (2, 1, 2))  #E34

layout = nx.kamada_kawai_layout(G)
nx.draw(G, layout, with_labels = True, arrows=True)
plt.savefig("vizes_kancsok/Képek/állapottér.png")
plt.close()

#Több kurzor:
# ctrl + alt + lefele nyíl
# alt lenyomva tartva + kattintgatás

# pip install scipy



