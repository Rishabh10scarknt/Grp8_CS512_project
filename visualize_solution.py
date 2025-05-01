import networkx as nx
import matplotlib.pyplot as plt
import re 
import sys
import os
import pandas as pd

def visualize_3Dmatch(nodes,triplets):
    # Create a graph
    G = nx.Graph()
    # Assign each node a 'bipartite' type for layout: 0 = man, 1 = woman, 2 = pet
    node_positions = {}
    y_levels = {'Boy': 2, 'Girl': 1, 'Pet': 0}
    # Add nodes with positions
    for m, w, p in nodes:
        G.add_node(m, type='Boy')
        G.add_node(w, type='Girl')
        G.add_node(p, type='Pet')
        node_positions[m] = (m, y_levels['Boy'])
        node_positions[w] = (w, y_levels['Girl'])
        node_positions[p] = (p, y_levels['Pet'])

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
        if n[1]['type'] == 'Boy':
            colors.append('skyblue')
        elif n[1]['type'] == 'Girl':
            colors.append('lightpink')
        else:
            colors.append('lightgreen')

    # Draw
    plt.figure(figsize=(12, 5))
    plt.title('3D Matching Triplet Visualization')
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1000, font_size=10)
    plt.axis('off')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
    
if __name__ =="__main__":
    for sys.argv[1] in os.listdir(os.getcwd()):
        if sys.argv[1].startswith("solution") and sys.argv[1].endswith(".csv"):
            df = pd.read_csv(sys.argv[1])
    
    x = df['Boy'].dropna()
    y = df['Girl'].dropna()
    z = df['Pet'].dropna()
    
    triplets = []
    for i in zip(list(x),list(y),list(z)):
        triplets.append(i)
    
    nodes = list(set(triplets))
    
    visualize_3Dmatch(nodes,triplets)
    