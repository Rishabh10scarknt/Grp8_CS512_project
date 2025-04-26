import os
import sys
import ast
import pandas as pd

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
        
    print(transformation(list(x),list(y),list(z),u))