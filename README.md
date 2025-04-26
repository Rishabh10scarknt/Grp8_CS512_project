This is a NP-complete reduction problem for 3D matching to Vector Cover by 3 sets (VC3).
The source code guided by the following procedure:
1) Generate symbolic triplets and mapping of equal cardinality sets of 3 for 3D matching. ( could be a user provided .csv file, check input.csv)
2) Further mappings amongst sets are transformed to a numeric set of triplets. ( The transformation must be polynomial in time)
3) Appoximate solution for the NP-complete VC3 by Algorithm X.
4) Brute force solution to the problem for verifying 3)
5) Backtracking to get the solution to the orginial 3D matching problem.
   

