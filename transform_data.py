import os
import sys
import ast
import pandas as pd
import plotly.graph_objects as go

def transformation(x: list,y: list ,z: list,mappings: list)-> list:
    X = {}
    Y = {}
    Z = {}
    for i,j in enumerate(x):
        X[str(j)] = i
    for l,k in enumerate(y):
        Y[str(k)] = l+len(y)
    for m,n in enumerate(z):
        Z[str(n)] = m+len(x)+len(y)

    # remove dulplicate mappings if any
    triplets = list(set(tuple(row) for row in mappings))
    three_sets = []
    for i in triplets:
         three_sets.append(tuple((X[i[0]], Y[i[1]], Z[i[2]])))

    return three_sets

def plot_VC3(VC3:list,title="VC3"):
    # Create figure
    fig = go.Figure()

    # Add one trace per tuple
    for triplet in VC3:
        fig.add_trace(go.Scatter(
            x=["First Set", "Second Set", "Third Set"],
            y=list(triplet),
            mode="lines+markers+text",
            name=str(triplet),
            text=[str(triplet[0]), str(triplet[1]), str(triplet[2])],
            textposition="top center"
        ))

    # Update layout for visual style
    fig.update_layout(
        title=title,
        xaxis_title="Mapping",
        yaxis_title="Value",
        xaxis=dict(type='category'),
        plot_bgcolor="#f0f6ff",
        legend_title_text="(First, Second, Third)",
        width=1000,
        height=800
    )
    fig.show()


if  __name__ == "__main__":
    for sys.argv[1] in os.listdir(os.getcwd()):
        if sys.argv[1].startswith("input") and sys.argv[1].endswith(".csv"):
           df = pd.read_csv(sys.argv[1])
    x = df['Set1'].dropna()
    y = df['Set2'].dropna()
    z = df['Set3'].dropna()
    mappings =  df['Mapping'].dropna()
    u = []
    for i in list(mappings):
        u.append(ast.literal_eval(i))
        
    VC3=transformation(list(x),list(y),list(z),u) 
    print(VC3)
    plot_VC3(VC3)
    
    data={"Boy":[t[0] for t in VC3], "Girl":[t[1] for t in VC3], "Pet":[t[2] for t in VC3]}    
    ddf = pd.DataFrame(data)
    ddf.to_csv("VC3.csv", index=False)
