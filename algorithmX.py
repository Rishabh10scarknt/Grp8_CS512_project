import os
import sys
import ast
import pandas as pd
import plotly.graph_objects as go
import copy


def solve(X, Y, solution=[]):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)
                    
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

if __name__=="__main__":
    for sys.argv[1] in os.listdir(os.getcwd()):
        if sys.argv[1].startswith("VC3") and sys.argv[1].endswith(".csv"):
            df = pd.read_csv(sys.argv[1])
    
    t = df['Triplets'].dropna()   
    VC3 = []
    for i in list(t):
        VC3.append(ast.literal_eval(i))
    
    # Step 1: Build Y
    Y = {}
    for idx, triplet in enumerate(VC3):
        Y[idx] = list(triplet)

    # Step 2: Build X
    X = {}
    for idx, triplet in Y.items():
        for vertex in triplet:
           if vertex not in X:
               X[vertex] = set()
           X[vertex].add(idx)
           
    # Important: Make a deep copy because Algorithm X modifies X and Y
    solutions = list(solve(copy.deepcopy(X), Y))

    # Store processed solution
    for sol in solutions:
        last = [VC3[i] for i in sol]
    
    #print solution
    print(last)
    
    plot_VC3(last,title="Exact VC3")
