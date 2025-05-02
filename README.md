This is a NP-complete reduction problem for 3D matching to Vector Cover by 3 sets (VC3).
The source code is guided by the following procedure:
1) Generate symbolic triplets and mapping of equal cardinality sets of 3 for 3D matching. ( could be a user provided .csv file, check input.csv)
2) Further mappings amongst sets are transformed to a numeric set of triplets. ( The transformation must be polynomial in time)
3) Appoximate solution for the NP-complete VC3 by Algorithm X.
4) Brute force solution to the problem for verifying 3)
5) Backtracking to get the solution to the orginial 3D matching problem.


 For executing the code from scratch, follow these commands on terminal:
 1) python .\generate_data.py <set_of_each_set> <number_random_mapping> (generates input.csv , this can be user defined check input.csv for formating)
    You will be prompted to enter single letter sybmol for each set on the terminal
 2) python .\transform_data.py .\input.csv (generates VC3.csv ,  prints out transformed mapping in form of numeric triplets along with the graph)
 3) python .\algorithmX.py .\VC3.csv ( prints exact VC3 along with the graph, generates solution.cvs that has backtracked solution to the 3D matching problem(e.g Boys,Girls,Pets))
 4) python .\visualize_solution.py .\solution.csv ( visualizes 3D matching solution)

