# Check the following:
#   1) Within each set boy, girl, and pets there are no duplicates
#   2) The set of boys, girls, and pets covered in the solution covers all in input.csv
#   3) All the mappings of (boy, girls, pets) in solution is in input.csv
#

import pandas as pd

def is_valid(problem_df, solution_df):
    for problem_col, solution_col in zip(problem_df.columns, solution_df.columns):
        # Make sure there are no duplicates in solution and make sure it covers all of the input
        set_solution = set(solution_df[solution_col])
        if len(set_solution) < len(solution_df[solution_col]) or set(problem_df[problem_col]) != set_solution: 
            return False
    return True

problem_df = pd.read_csv("input.csv", usecols=["Set1", "Set2", "Set3"])
problem_df = problem_df.dropna()

solution_df = pd.read_csv("solution.csv", usecols=["Boy", "Girl", "Pet"])

with open("input.csv", "r") as file:
    next(file)  # Skip the header
    input_mappings = {tuple(line[line.index("(") + 1: line.index(")")].replace("'", "").split(", ")) for line in file}
with open("solution.csv", "r") as file:
    next(file) # Skip the header
    solution_mappings = {tuple(line.strip().split(",")) for line in file}

if is_valid(problem_df, solution_df) and len(solution_mappings - input_mappings) == 0:
    print("Soluiton is valid.")
else:
    print("Solution is not valid.")
