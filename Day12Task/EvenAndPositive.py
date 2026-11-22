#7. Filter Positive Even Numbers from Dataset 
#Scenario: 
#A dataset contains mixed values: 
#arr = [-5, 10, 15, -2, 20, 25, 30] 
#Task: 
#● Convert to NumPy array. 
#● Filter values that are: 
#○ Positive 
#○ Even





import numpy as np
arr=[-5, 10, 15, -2, 20, 25, 30]
nparr=np.array(arr)
positive=nparr[(nparr>0)]
even=nparr[(nparr%2==0)]
print("Original Array",nparr)
print("Positive values:",positive)
print("Even values:",even)



