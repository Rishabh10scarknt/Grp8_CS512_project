import networkx as nx
import matplotlib.pyplot as plt
import re

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