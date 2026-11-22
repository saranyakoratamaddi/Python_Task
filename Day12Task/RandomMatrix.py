#10. Random Matrix and Condition Filtering 
#Scenario: 
#● Generate a 3×3 matrix of random numbers (0–50). 
#Task: 
#● Filter elements greater than 25. 
#● Print filtered values.




import random
matrix=[[random.randint(0,50) for i in range(3)]for i in range(3)]
print(matrix)
filtered_val=[num for row in matrix for num in row if num>25]
print("3x3 matrix")
for row in matrix:
    print(row)
print("Filtered values(>25):",filtered_val)
