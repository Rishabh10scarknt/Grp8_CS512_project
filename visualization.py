import networkx as nx
import matplotlib.pyplot as plt
import re
# # Sample triplet data: (man, woman, pet)
# nodes = [
#     ('M1', 'W1', 'P1'),
#     ('M2', 'W2', 'P2'),
#     ('M3', 'W3', 'P3'),
#     ('M4', 'W4', 'P4'),
#     ('M5', 'W5', 'P5'),
#     ('M6', 'W6', 'P6'),
#     ('M7', 'W7', 'P7'),
#     ('M8', 'W8', 'P8'),
#     ('M9', 'W9', 'P9'),
#     ('M10', 'W10', 'P10'),
#     ('M11', 'W11', 'P11'),
#     ('M12', 'W12', 'P12'),
#     ('M13', 'W13', 'P13'),
#     ('M14', 'W14', 'P14'),
#     ('M15', 'W15', 'P15'),
#     ('M16', 'W16', 'P16')
# ]
# triplets = [
#     ('M1', 'W16', 'P3'),
#     ('M2', 'W15', 'P8'),
#     ('M3', 'W14', 'P15'),
#     ('M4', 'W13', 'P2'),
#     ('M5', 'W12', 'P12'),
#     ('M6', 'W11', 'P6'),
#     ('M7', 'W10', 'P16'),
#     ('M8', 'W9', 'P7'),
#     ('M9', 'W8', 'P9'),
#     ('M10', 'W7', 'P1'),
#     ('M11', 'W6', 'P11'),
#     ('M12', 'W5', 'P14'),
#     ('M13', 'W4', 'P13'),
#     ('M14', 'W3', 'P4'),
#     ('M15', 'W2', 'P5'),
#     ('M16', 'W1', 'P10')
# ]

nodes = []
triplets = []
f = open('./input.csv')
with open('./input.csv') as f:
    for line in f.readlines():
        inputs = line.strip().split("\"")
        if len(inputs) > 1:
            nodes.append(inputs[0].split(",")[:-1])
            # triplets.append(inputs[1].split(", "))
            # all = re.findall(r"'([^']*)'", inputs[1])
            triplets.append(re.findall(r"'([^']*)'", inputs[1]))
            
for node in nodes:
    print(node)
print()
for triplet in triplets:
    print(triplet)

    

# Create a graph
G = nx.Graph()

# Assign each node a 'bipartite' type for layout: 0 = man, 1 = woman, 2 = pet
node_positions = {}
y_levels = {'man': 2, 'woman': 1, 'pet': 0}

# Add nodes with positions
for m, w, p in nodes:
    G.add_node(m, type='man')
    G.add_node(w, type='woman')
    G.add_node(p, type='pet')
    node_positions[m] = (m, y_levels['man'])
    node_positions[w] = (w, y_levels['woman'])
    node_positions[p] = (p, y_levels['pet'])

# Flatten position x-coordinates by assigning integers
node_x = {}
x = 0
for node in G.nodes():
    node_x[node] = x
    x += 1

# Update positions with consistent horizontal layout
pos = {}
for node in G.nodes(data=True):
    nodename, ntype = node[0], node[1]['type']
    pos[nodename] = (node_x[nodename], y_levels[ntype])

# Add edges for each triplet
for m, w, p in triplets:
    G.add_edge(m, w)
    G.add_edge(w, p)
    G.add_edge(m, p)

# Color by type
colors = []
for n in G.nodes(data=True):
    if n[1]['type'] == 'man':
        colors.append('skyblue')
    elif n[1]['type'] == 'woman':
        colors.append('lightpink')
    else:
        colors.append('lightgreen')

# Draw
plt.figure(figsize=(10, 5))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1000, font_size=10)
plt.title('3D Matching Triplet Visualization')
plt.axis('off')
plt.show()