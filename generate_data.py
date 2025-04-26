import numpy as np
import random
import itertools
import sympy as sp 
import sys
import pandas as pd

def shuffled_cycle(lst):
    while True:
        yield from random.sample(lst, len(lst))  # Shuffles and yields all elements

def assign_symbols(set_length : int) -> list:
    # symbolic literals for the sets
    x=str(input("Enter symbol for the first set :"))
    y=str(input("Enter symbol for the second set :"))
    z=str(input("Enter symbol for the third set :"))
    x = [ sp.symbols(x+str(i)) for i in range(set_length) ]
    y = [ sp.symbols(y+str(i)) for i in range(set_length) ]
    z = [ sp.symbols(z+str(i)) for i in range(set_length) ]
    
    return x,y,z

def generate_mapping(set_length: int, iterations: int) -> list:
   
    # create a structured numpy array for the 3 sets 
    dt = np.dtype([("set1",(np.str_ , set_length)),("set2",(np.str_ ,set_length)),("set3",(np.str_ ,set_length))])

    x,y,z = assign_symbols(set_length)
    cycler_x = itertools.cycle(shuffled_cycle(x))
    cycler_y = itertools.cycle(shuffled_cycle(y))
    cycler_z = itertools.cycle(shuffled_cycle(z))

    mappings = []
    for i in range(iterations):
        x_ = next(cycler_x)
        y_ = next(cycler_y)
        z_ = next(cycler_z)
        inp_exp = np.array(([(str(x_),str(y_),str(z_))]),dtype=dt)
        mappings.append(inp_exp[0])

    return x,y,z,mappings

if __name__ == "__main__":
    x,y,z,mappings = generate_mapping(int(sys.argv[1]),int(sys.argv[2]))
    x = [str(i) for i in x]
    y = [str(i) for i in y]
    z = [str(i) for i in z]
    mappings = [str(i) for i in mappings]

    # Find the max length
    max_len = max(len(x), len(y), len(z), len(mappings))

    # Pad shorter lists with empty strings
    def pad(arr, length):
        return arr + [''] * (length - len(arr))

    data = {
           "Set1": pad(x, max_len),
           "Set2": pad(y, max_len),
           "Set3": pad(z, max_len),
           "Mapping": pad(mappings, max_len)
          }

    df = pd.DataFrame(data)
    df.to_csv("input.csv", index=False)