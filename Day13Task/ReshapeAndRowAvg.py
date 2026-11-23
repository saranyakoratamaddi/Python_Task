#5. Reshape & Row Averages 
#A dataset: 
#data = np.arange(1, 13) 
#Task: 
#● Reshape it into a 3×4 matrix 
#● Compute average of each row






import numpy as np
data = np.arange(1, 13)
print(data)
matrix=data.reshape(3,4)
avg=np.mean(matrix,axis=1)
print("3x4 Matrix:",matrix)
print("Average of each row:",avg)
